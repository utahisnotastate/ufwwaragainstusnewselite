import numpy as np
import pytest

FOLDER = "Module_01_Zero_Point_Energy"


def test_ideal_casimir_pressure_published_values(sim):
    # pi^2 hbar c / 240 = 1.300e-27 N m^2: 1.30 mPa at 1 um, 13.0 Pa at 100 nm (Casimir 1948)
    assert float(sim.casimir_pressure_ideal(1e-6)) == pytest.approx(-1.300e-3, rel=2e-3)
    assert float(sim.casimir_pressure_ideal(1e-7)) == pytest.approx(-13.00, rel=2e-3)


def test_ideal_scaling_laws(sim):
    assert float(sim.casimir_pressure_ideal(1e-7) / sim.casimir_pressure_ideal(2e-7)) == pytest.approx(16.0)
    assert float(sim.casimir_energy_ideal(1e-7) / sim.casimir_energy_ideal(2e-7)) == pytest.approx(8.0)


def test_ideal_pressure_is_minus_derivative_of_energy(sim):
    d, h = 3e-7, 1e-11
    dEdd = (sim.casimir_energy_ideal(d + h) - sim.casimir_energy_ideal(d - h)) / (2 * h)
    assert float(-dEdd) == pytest.approx(float(sim.casimir_pressure_ideal(d)), rel=1e-6)


@pytest.mark.parametrize("d", [1e-8, 1e-7, 1e-6, 1e-5])
def test_lifshitz_integrator_reproduces_perfect_mirror_closed_form(sim, d):
    """The numerical double integral with r = 1 must land on Casimir's analytic result."""
    assert sim.lifshitz_pressure(d, "ideal") == pytest.approx(float(sim.casimir_pressure_ideal(d)), rel=1e-6)
    assert sim.lifshitz_energy(d, "ideal") == pytest.approx(float(sim.casimir_energy_ideal(d)), rel=1e-6)


def test_gold_reduction_factor_between_zero_and_one_and_rising(sim):
    ds = [1e-8, 1e-7, 3e-7, 1e-6, 3e-6, 1e-5]
    ratios = [sim.gold_reduction_factor(d) for d in ds]
    assert all(0.0 < r < 1.0 for r in ratios)
    assert all(b > a for a, b in zip(ratios, ratios[1:]))
    assert ratios[1] < 0.6          # ~100 nm: noticeably below ideal (plasma wavelength ~ 138 nm)
    assert ratios[-1] > 0.95        # 10 um: approaches the perfect-mirror limit


def test_lifshitz_pressure_matches_derivative_of_lifshitz_energy(sim):
    d, h = 3e-7, 2e-10
    dEdd = (sim.lifshitz_energy(d + h) - sim.lifshitz_energy(d - h)) / (2 * h)
    assert -dEdd == pytest.approx(sim.lifshitz_pressure(d), rel=1e-4)


def test_short_range_limit_is_nonretarded_van_der_waals(sim):
    """At d << c/wp the energy must go as -A/(12 pi d^2), with A from an independent 1-D integral."""
    A = sim.hamaker_constant()
    assert 1e-19 < A < 5e-19        # metals: a few 1e-19 J
    d = 2e-10
    assert -12 * np.pi * d ** 2 * sim.lifshitz_energy(d) == pytest.approx(A, rel=5e-3)
    slope = np.log(sim.lifshitz_energy(4e-10) / sim.lifshitz_energy(2e-10)) / np.log(2.0)
    assert slope == pytest.approx(-2.0, abs=0.02)


def test_long_range_slope_tends_to_minus_four(sim):
    slope = np.log(sim.lifshitz_pressure(4e-5) / sim.lifshitz_pressure(2e-5)) / np.log(2.0)
    assert slope == pytest.approx(-4.0, abs=0.03)


def test_drude_epsilon_limits(sim):
    assert sim.drude_epsilon(1e25) == pytest.approx(1.0, abs=1e-6)       # transparent far above wp
    assert sim.drude_epsilon(1e10) > 1e8                                    # nearly a perfect conductor at low xi


@pytest.mark.parametrize("which", ["ideal", "gold"])
def test_closed_cycle_nets_zero_work(sim, which):
    fn = (lambda x: float(sim.casimir_pressure_ideal(x))) if which == "ideal" else sim.lifshitz_pressure
    w_in, w_out, net = sim.closed_cycle_work(fn, 1e-6, 1e-7)
    assert w_in > 0 and w_out < 0
    assert abs(net) < 1e-5 * w_in


def test_single_stroke_equals_energy_difference(sim):
    w_in, _, _ = sim.closed_cycle_work(lambda x: float(sim.casimir_pressure_ideal(x)), 1e-6, 1e-7)
    assert w_in == pytest.approx(sim.one_shot_energy(1e-6, 1e-7), rel=1e-5)


def test_one_shot_energy_is_tiny(sim):
    assert sim.one_shot_energy(1e-6, 1e-8) < 1e-3   # J per square metre of perfect mirrors


def test_planck_density_matches_codata_planck_units(sim):
    from scipy.constants import physical_constants as pc
    m_p, l_p = pc["Planck mass"][0], pc["Planck length"][0]
    assert sim.planck_density() == pytest.approx(m_p / l_p ** 3, rel=1e-4)


def test_observed_dark_energy_density(sim):
    assert sim.observed_dark_energy_density() == pytest.approx(5.3e-10, rel=0.05)


def test_cosmological_constant_gap_about_120_orders(sim):
    assert 118 < sim.cosmological_constant_gap() < 124
