import numpy as np
import pytest

FOLDER = "Module_08_Instant_Travel"

R, SIGMA, V = 1.0, 8.0, 1.0


def test_shape_function_is_one_inside_and_zero_far_away(sim):
    assert float(sim.shape_function(0.0, R, SIGMA)) == pytest.approx(1.0, abs=1e-12)
    assert float(sim.shape_function(0.5, R, SIGMA)) == pytest.approx(1.0, abs=1e-3)
    assert abs(float(sim.shape_function(5.0, R, SIGMA))) < 1e-12
    assert float(sim.shape_function(R, R, SIGMA)) == pytest.approx(0.5, abs=1e-6)


def test_shape_derivative_matches_finite_difference(sim):
    r = np.linspace(0.2, 2.5, 50)
    h = 1e-6
    fd = (sim.shape_function(r + h, R, SIGMA) - sim.shape_function(r - h, R, SIGMA)) / (2 * h)
    assert np.allclose(sim.shape_derivative(r, R, SIGMA), fd, atol=1e-6)


def test_derivative_is_stable_for_planck_thin_walls(sim):
    sigma = 2.0 / 1.6e-33
    assert np.isfinite(float(sim.shape_derivative(100.0, 100.0, sigma)))
    assert sim.wall_thickness(100.0, sigma) == pytest.approx(1.6e-33, rel=1e-9)


def test_wall_thickness_tends_to_two_over_sigma(sim):
    assert sim.wall_thickness(1.0, 50.0) == pytest.approx(2.0 / 50.0, rel=1e-9)
    assert abs(sim.wall_thickness(1.0, 0.5) / (2.0 / 0.5) - 1) > 0.1    # thick-wall regime differs


def test_expansion_vanishes_inside_and_far_outside(sim):
    wall = abs(float(sim.york_expansion(R, 0, 0, V, R, SIGMA)))        # |theta| on the front wall = v sigma / 2
    assert wall == pytest.approx(V * SIGMA / 2, rel=1e-6)
    for p in [(0, 0, 0), (0.3, 0.2, 0), (-0.3, 0, 0.2), (6, 0, 0), (-6, 1, 0), (0, 8, 0)]:
        assert abs(float(sim.york_expansion(*p, V, R, SIGMA))) < 1e-3 * wall


def test_expansion_is_antisymmetric_contracting_ahead(sim):
    xs = np.linspace(0.6, 1.4, 9)
    ahead = sim.york_expansion(xs, 0.3, 0.0, V, R, SIGMA)
    behind = sim.york_expansion(-xs, 0.3, 0.0, V, R, SIGMA)
    assert np.allclose(ahead, -behind)
    assert np.all(ahead < 0) and np.all(behind > 0)
    assert np.allclose(sim.york_expansion(0.0, np.linspace(0.5, 2, 5), 0.0, V, R, SIGMA), 0.0)


def test_expansion_follows_bubble_centre(sim):
    a = sim.york_expansion(1.0, 0.2, 0.0, V, R, SIGMA)
    b = sim.york_expansion(11.0, 0.2, 0.0, V, R, SIGMA, x_s=10.0)
    assert float(a) == pytest.approx(float(b))


def test_weak_energy_condition_violated_everywhere(sim):
    g = np.linspace(-3, 3, 61)
    x, y, z = np.meshgrid(g, g, g, indexing="ij")
    t00 = sim.energy_density(x, y, z, V, R, SIGMA)
    assert np.all(t00 <= 0.0)
    assert t00.min() < -1e-2                                  # and genuinely negative on the wall
    assert np.all(sim.energy_density(np.linspace(-3, 3, 13), 0.0, 0.0, V, R, SIGMA) == 0.0)  # zero on the axis


def test_peak_energy_density_matches_thin_wall_estimate(sim):
    sigma = 40.0
    r = np.linspace(0.8, 1.2, 40001)
    peak = np.max(-sim.energy_density(0.0, r, 0.0, V, R, sigma))     # equator, rho = r
    assert peak == pytest.approx(V ** 2 * sigma ** 2 / (128 * np.pi), rel=1e-3)


def test_energy_density_scales_as_v_squared(sim):
    a = sim.energy_density(0.3, 0.9, 0.2, 1.0, R, SIGMA)
    b = sim.energy_density(0.3, 0.9, 0.2, 3.0, R, SIGMA)
    assert float(b / a) == pytest.approx(9.0)


def test_total_energy_matches_direct_3d_integration(sim):
    """Independent check of the angular reduction: brute-force Riemann sum on a 3-D grid."""
    sigma = 4.0
    g = np.linspace(-3, 3, 121)
    d = g[1] - g[0]
    x, y, z = np.meshgrid(g, g, g, indexing="ij")
    brute = sim.energy_density(x, y, z, V, R, sigma).sum() * d ** 3
    assert brute == pytest.approx(sim.total_energy(V, R, sigma), rel=0.02)


def test_total_energy_thin_wall_limit_and_scaling(sim):
    for s in (20.0, 80.0):
        assert sim.total_energy(1.0, 1.0, s) == pytest.approx(sim.total_energy_thin_wall(1.0, 1.0, s), rel=2e-3)
    # numerically: E ~ R^2 and ~ sigma (i.e. ~ 1/thickness)
    assert sim.total_energy(1.0, 2.0, 40.0) / sim.total_energy(1.0, 1.0, 40.0) == pytest.approx(4.0, rel=5e-3)
    assert sim.total_energy(1.0, 1.0, 80.0) / sim.total_energy(1.0, 1.0, 40.0) == pytest.approx(2.0, rel=5e-3)
    assert sim.total_energy(1.0, 1.0, 40.0) < 0


def test_quantum_inequality_scaling_and_units(sim):
    assert float(sim.qi_bound(1e-9) / sim.qi_bound(2e-9)) == pytest.approx(16.0)
    assert float(sim.qi_bound(1.0)) < 0
    # dimensional check: hbar / (c^3 t^4) at t = Planck time equals Planck energy density up to the constant
    t_p = sim.L_PLANCK / sim.C
    planck_density = sim.C ** 7 / (sim.HBAR * sim.G ** 2)
    assert abs(float(sim.qi_bound(t_p))) / planck_density == pytest.approx(3 / (32 * np.pi ** 2), rel=1e-9)


def test_qi_forces_planck_scale_walls(sim):
    d1 = sim.max_wall_thickness_qi(1.0, R=100.0, sampling_fraction=0.1)
    assert d1 == pytest.approx(np.sqrt(3 / np.pi) * sim.L_PLANCK / (0.1 ** 2 * 1.0), rel=1e-6)
    assert 10 < d1 / sim.L_PLANCK < 1000
    assert sim.max_wall_thickness_qi(2.0, 100.0) == pytest.approx(d1 / 2, rel=1e-6)
    assert sim.max_wall_thickness_qi(1.0, 100.0, 0.2) == pytest.approx(d1 / 4, rel=1e-6)


def test_warp_bubble_needs_more_than_the_observable_universe(sim):
    d = sim.max_wall_thickness_qi(1.0, R=100.0)
    b = sim.warp_energy_budget(1.0, 100.0, d)
    assert b["mass_kg"] < -1e60                        # vs ~1e53 kg of ordinary matter in the observable universe
    assert b["energy_J"] == pytest.approx(b["mass_kg"] * sim.C ** 2)


def test_casimir_values(sim):
    # 1 micron: pi^2 hbar c / 720 / d^4 ~ 4.3e-4 J/m^3; energy per area = density * d
    u = float(sim.casimir_energy_density(1e-6))
    assert u == pytest.approx(-4.33e-4, rel=5e-3)
    assert float(sim.casimir_energy_density(1e-7) / sim.casimir_energy_density(1e-6)) == pytest.approx(1e4)
    assert sim.casimir_gap_for(u) == pytest.approx(1e-6)


def test_casimir_cannot_supply_a_warp_wall(sim):
    need = sim.peak_negative_energy_density_SI(1.0, 100.0, 1.0)
    assert sim.casimir_gap_for(need) < 1e-15            # plates closer than a proton is wide


def test_superluminal_signal_reverses_order_for_some_observer(sim):
    u = 2 * sim.C
    V = sim.reversing_frame_speed(u)
    assert V == pytest.approx(0.5 * sim.C)
    assert sim.order_reversal_factor(u, 0.49 * sim.C) > 0
    assert sim.order_reversal_factor(u, 0.51 * sim.C) < 0


def test_subluminal_signal_never_reverses(sim):
    assert sim.reversing_frame_speed(0.999 * sim.C) is None
    for V in np.linspace(-0.999, 0.999, 41) * sim.C:
        assert sim.order_reversal_factor(0.999 * sim.C, V) > 0


def test_de_broglie_phase_is_superluminal_but_group_is_not(sim):
    for m, v in [(9.109e-31, 1e6), (25.0, 1.0), (1.67e-27, 0.9 * 2.99792458e8)]:
        w = sim.de_broglie_velocities(m, v)
        assert w["group_velocity"] == pytest.approx(v, rel=1e-9)
        assert w["phase_velocity"] * w["group_velocity"] == pytest.approx(sim.C ** 2, rel=1e-9)
        assert w["phase_velocity"] > sim.C
