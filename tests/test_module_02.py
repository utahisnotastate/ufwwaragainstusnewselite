import numpy as np
import pytest

FOLDER = "Module_02_Gravity_Is_Pushing"


def test_monte_carlo_matches_exact_integral(sim):
    for d in (4.0, 8.0):
        assert sim.shadow_force(d) == pytest.approx(sim.shadow_force_exact(d), rel=0.05)


def test_inverse_square_emerges_from_ray_counting(sim):
    ratio = sim.shadow_force(4.0, n=4_000_000) / sim.shadow_force(8.0, n=4_000_000, seed=1)
    assert ratio == pytest.approx(4.0, rel=0.05)


def test_exact_shadow_is_inverse_square_at_large_distance(sim):
    assert sim.shadow_force_exact(100.0) / sim.shadow_force_exact(200.0) == pytest.approx(4.0)


def test_transparent_body_absorbs_in_proportion_to_volume(sim):
    tau = np.array([1e-8, 1e-6, 1e-4, 1e-3])
    assert np.allclose(sim.absorbed_fraction(tau), 4 * tau / 3, rtol=2e-3)


def test_opaque_body_saturates(sim):
    assert float(sim.absorbed_fraction(50.0)) == pytest.approx(1.0, abs=1e-3)
    assert float(sim.mass_proportionality(10.0)) < 0.1


def test_series_and_closed_form_agree_at_the_switch(sim):
    below, above = sim.absorbed_fraction(0.99e-4), sim.absorbed_fraction(1.01e-4)
    assert float(above / below) == pytest.approx(1.01 / 0.99, rel=1e-3)


def test_flux_tuned_to_G_reproduces_newton(sim):
    h, m1, m2, r = 1e-10, 10.0, 20.0, 3.0
    u = sim.drag_and_heating(h)["energy_density_J_m3"]
    push = u * (h * m1) * (h * m2) / (4 * np.pi * r ** 2)
    assert push == pytest.approx(sim.G * m1 * m2 / r ** 2)


def test_no_coefficient_escapes_both_drag_and_saturation(sim):
    """The Poincare/Feynman dilemma: survive 4.5 Gyr of drag AND stay transparent (optical radius < 0.01)."""
    age_s = 4.5e9 * sim.SECONDS_PER_YEAR
    for h in np.logspace(-25, 5, 301):
        r = sim.drag_and_heating(h)
        assert not (r["velocity_decay_time_s"] > age_s and r["earth_optical_radius"] < 0.01)
