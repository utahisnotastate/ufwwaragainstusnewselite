import numpy as np
import pytest

FOLDER = "Module_05_Time_Is_A_Map"


# ---------------------------------------------------------------- special relativity

def test_interval_is_invariant_under_boosts(sim):
    t, x = 3.7, 1.2e9
    for v in (-0.9 * sim.C, 1e3, 0.6 * sim.C):
        t2, x2 = sim.lorentz_boost(t, x, v)
        assert sim.interval(t2, x2) == pytest.approx(sim.interval(t, x), rel=1e-9)


def test_boost_there_and_back_is_identity(sim):
    t, x = 2.0, -4.0e8
    t2, x2 = sim.lorentz_boost(*sim.lorentz_boost(t, x, 0.8 * sim.C), -0.8 * sim.C)
    assert (t2, x2) == (pytest.approx(t), pytest.approx(x))


def test_simultaneity_shift_matches_gamma_v_L_over_c2(sim):
    L, v = 1.0e12, 0.6 * sim.C                     # gamma = 1.25
    assert sim.simultaneity_shift(L, v) == pytest.approx(-1.25 * v * L / sim.C ** 2)
    assert sim.simultaneity_shift(L, 0.0) == 0.0


def test_timelike_order_never_flips_but_spacelike_order_can(sim):
    boosts = np.linspace(-0.999, 0.999, 401) * sim.C
    assert all(sim.lorentz_boost(1.0, 0.9 * sim.C, v)[0] > 0 for v in boosts)
    assert any(sim.lorentz_boost(1.0, 1.1 * sim.C, v)[0] < 0 for v in boosts)


# ---------------------------------------------------------------- GPS

def test_gps_offsets_match_published_values(sim):
    g = sim.gps_clock_rates()
    us = 1e-6
    assert g["gravitational"] == pytest.approx(45.9 * us, rel=0.01)
    assert g["satellite_velocity"] == pytest.approx(-7.2 * us, rel=0.01)
    assert g["net"] == pytest.approx(38.6 * us, rel=0.01)
    assert g["net_from_geoid_constant"] == pytest.approx(g["net"], rel=0.005)


def test_gps_orbit_is_about_12_hours(sim):
    period = 2 * np.pi * sim.A_GPS / sim.gps_clock_rates()["orbital_speed_m_s"]
    assert period / 3600 == pytest.approx(11.97, abs=0.02)   # half a sidereal day


def test_clock_on_the_ground_gains_nothing_against_itself(sim):
    g = sim.gps_clock_rates(a=sim.R_EARTH_EQ, omega=np.sqrt(sim.GM_EARTH / sim.R_EARTH_EQ ** 3))
    assert g["gravitational"] == 0.0
    assert g["net"] == pytest.approx(0.0, abs=1e-15)          # co-orbiting clocks tick together


# ---------------------------------------------------------------- Kerr

@pytest.mark.parametrize("a", [0.0, 0.3, 0.7, 0.99, 1.0])
def test_horizons_are_zeros_of_delta(sim, a):
    for r in sim.horizons(a):
        assert r ** 2 - 2 * r + a ** 2 == pytest.approx(0.0, abs=1e-12)


def test_no_horizon_for_overspinning(sim):
    assert sim.horizons(1.2) is None


def test_schwarzschild_limit(sim):
    g_tt, g_tph, g_rr, g_thth, g_phph = sim.kerr_metric(5.0, 0.8, 0.0)
    assert g_tt == pytest.approx(-(1 - 2 / 5))
    assert g_tph == 0.0
    assert g_rr == pytest.approx(1 / (1 - 2 / 5))
    assert g_phph == pytest.approx(25 * np.sin(0.8) ** 2)


def test_kerr_t_phi_determinant_identity(sim):
    """A classic check of the Kerr components: g_tphi^2 - g_tt g_phiphi = Delta sin^2(theta)."""
    rng = np.random.default_rng(3)
    for _ in range(20):
        a, r, th = rng.uniform(0, 1), rng.uniform(0.2, 10), rng.uniform(0.1, 3.0)
        g_tt, g_tph, _, _, g_phph = sim.kerr_metric(r, th, a)
        assert g_tph ** 2 - g_tt * g_phph == pytest.approx((r * r - 2 * r + a * a) * np.sin(th) ** 2, rel=1e-9, abs=1e-12)


def test_kerr_is_asymptotically_flat(sim):
    g_tt, g_tph, g_rr, _, _ = sim.kerr_metric(1e8, 1.0, 0.9)
    assert g_tt == pytest.approx(-1, abs=1e-7) and g_rr == pytest.approx(1, abs=1e-7) and abs(g_tph) < 1e-7


@pytest.mark.parametrize("a", [0.4, 0.9, 1.0])
@pytest.mark.parametrize("theta", [0.3, 1.0, np.pi / 2])
def test_g_tt_vanishes_on_ergosurface(sim, a, theta):
    assert sim.kerr_metric(sim.ergosurface(a, theta), theta, a)[0] == pytest.approx(0.0, abs=1e-12)


def test_ergosurface_touches_horizon_at_poles(sim):
    a = 0.8
    assert sim.ergosurface(a, 0.0) == pytest.approx(sim.horizons(a)[0])
    assert sim.ergosurface(a, np.pi / 2) == pytest.approx(2.0)


def test_static_observer_timelike_outside_spacelike_inside(sim):
    a, th = 0.9, np.pi / 2
    r_plus, r_ergo = sim.horizons(a)[0], sim.ergosurface(a, th)
    assert sim.static_observer_norm(r_ergo * 1.01, th, a) < 0
    assert sim.static_observer_norm(10.0, th, a) < 0
    for r in np.linspace(r_plus * 1.001, r_ergo * 0.999, 20):
        assert sim.static_observer_norm(r, th, a) > 0


# ---------------------------------------------------------------- Penrose process

def test_penrose_extremal_efficiency_is_20_7_percent(sim):
    assert sim.penrose_max_efficiency_formula(1.0) == pytest.approx((np.sqrt(2) - 1) / 2)
    assert sim.penrose_max_efficiency_numeric(1.0) == pytest.approx(0.2071, abs=5e-4)


@pytest.mark.parametrize("a", [0.3, 0.6, 0.9, 0.99])
def test_penrose_numeric_matches_formula(sim, a):
    assert sim.penrose_max_efficiency_numeric(a) == pytest.approx(sim.penrose_max_efficiency_formula(a), rel=1e-3)


def test_no_energy_extraction_outside_ergosphere_or_without_spin(sim):
    assert sim.penrose_gain(0.9, 2.5) == 0.0
    assert sim.penrose_gain(0.9, 4.0) == 0.0
    assert sim.penrose_max_efficiency_numeric(0.0) == pytest.approx(0.0, abs=1e-6)


def test_penrose_gain_grows_toward_horizon(sim):
    gains = [sim.penrose_gain(0.9, r) for r in (1.9, 1.7, 1.5)]
    assert gains[0] < gains[1] < gains[2]


def test_irreducible_mass_and_extractable_energy(sim):
    assert sim.irreducible_mass(0.0) == pytest.approx(1.0)
    assert sim.irreducible_mass(1.0) == pytest.approx(1 / np.sqrt(2))
    assert sim.max_extractable_fraction(1.0) == pytest.approx(0.2929, abs=1e-4)
    # A single Penrose split cannot beat the total rotational energy available
    for a in (0.5, 0.9, 1.0):
        assert sim.penrose_max_efficiency_formula(a) < sim.max_extractable_fraction(a) + 1e-12


# ---------------------------------------------------------------- where CTCs live

@pytest.mark.parametrize("a", [0.3, 0.9, 1.0, 1.2])
def test_ctcs_only_at_negative_r(sim, a):
    lo, hi = sim.ctc_scan(a)
    assert hi < 0
    assert sim.ctc_scan(a, r_min=1e-6, r_max=50.0) is None


def test_ctc_boundary_extremal_equator(sim):
    """For a = 1 at the equator, g_phiphi ∝ (r^3 + r + 2)/r, which changes sign at r = -1."""
    lo, _ = sim.ctc_scan(1.0)
    assert lo == pytest.approx(-1.0, abs=1e-3)


def test_no_ctcs_for_schwarzschild(sim):
    assert sim.ctc_scan(0.0) is None


def test_ergosphere_is_not_a_ctc(sim):
    """The bad draft's mistake: d/dt going spacelike inside the ergosphere is frame dragging, not a time loop."""
    a, th = 0.9, np.pi / 2
    r = 0.5 * (sim.horizons(a)[0] + sim.ergosurface(a, th))
    g_tt, _, _, _, g_phph = sim.kerr_metric(r, th, a)
    assert g_tt > 0 and g_phph > 0
