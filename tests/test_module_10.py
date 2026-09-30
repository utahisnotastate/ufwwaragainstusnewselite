import numpy as np
import pytest

FOLDER = "Module_10_Time_Reversal_Healing"


# ---------------------------------------------------------------- phase conjugation

def test_free_space_propagation_is_unitary_and_reversible(sim):
    rng = np.random.default_rng(3)
    f = rng.standard_normal(1024) + 1j * rng.standard_normal(1024)
    g = sim.propagate(f, 0.3, 633e-9, 5e-6)
    assert np.vdot(g, g).real == pytest.approx(np.vdot(f, f).real, rel=1e-12)
    assert np.allclose(sim.propagate(g, -0.3, 633e-9, 5e-6), f)
    assert not np.allclose(g, f)   # propagation actually does something


def test_phase_conjugation_cancels_a_static_aberration(sim):
    f, captured = sim.round_trip(rms_rad=3.0, seed=5)
    assert captured == pytest.approx(1.0)
    assert f == pytest.approx(1.0, abs=1e-9)


def test_ordinary_mirror_does_not_cancel_the_aberration(sim):
    assert sim.round_trip(rms_rad=2.0, conjugate=False)[0] < 0.05
    # with no aberration both mirrors are perfect: the comparison is fair
    assert sim.round_trip(rms_rad=0.0, conjugate=False)[0] == pytest.approx(1.0, abs=1e-9)


def test_changing_medium_follows_gaussian_decorrelation_law(sim):
    for rho in (0.99, 0.95, 0.9):
        f = np.mean([sim.round_trip(rms_rad=2.0, rho=rho, seed=s)[0] for s in range(6)])
        assert f == pytest.approx(sim.decorrelation_fidelity_theory(2.0, rho), rel=0.08)


def test_fidelity_falls_monotonically_as_medium_decorrelates(sim):
    f = [sim.round_trip(rho=r, seed=1)[0] for r in (1.0, 0.99, 0.9, 0.5)]
    assert all(a > b for a, b in zip(f, f[1:]))


def test_partial_capture_fidelity_equals_captured_fraction(sim):
    """Analytic result: with an unchanged medium, fidelity = power fraction the mirror intercepts."""
    for a in (3e-3, 1e-3, 3e-4):
        f, captured = sim.round_trip(aperture=a, seed=2)
        assert 0.0 < captured < 1.0
        assert f == pytest.approx(captured, rel=1e-8)


# ---------------------------------------------------------------- wavefront shaping

@pytest.mark.parametrize("n", [10, 100, 400])
def test_vellekoop_mosk_enhancement(sim, n):
    assert sim.wavefront_shaping_enhancement(n, trials=400) == pytest.approx(sim.vellekoop_mosk_theory(n), rel=0.05)


def test_enhancement_is_lost_when_the_medium_is_replaced(sim):
    assert sim.wavefront_shaping_enhancement(400, trials=400, fresh_medium=True) == pytest.approx(1.0, abs=0.15)


def test_mode_count_scales_with_area_over_lambda_squared(sim):
    assert sim.modes_in_area(4e-4) / sim.modes_in_area(1e-4) == pytest.approx(4.0)
    assert sim.modes_in_area(1e-4, 400e-9) / sim.modes_in_area(1e-4, 800e-9) == pytest.approx(4.0)


# ---------------------------------------------------------------- bioelectricity

def test_potassium_nernst_potential_at_body_temperature(sim):
    assert sim.nernst(5.0, 140.0) * 1e3 == pytest.approx(-89.1, abs=0.3)


def test_nernst_slope_is_61_5_mV_per_decade_at_37C(sim):
    assert (sim.nernst(10.0, 1.0) - sim.nernst(1.0, 1.0)) * 1e3 == pytest.approx(61.5, abs=0.1)


def test_nernst_is_zero_for_equal_concentrations_and_flips_with_charge(sim):
    assert sim.nernst(7.0, 7.0) == 0.0
    assert sim.nernst(110.0, 10.0, z=-1) == pytest.approx(-sim.nernst(110.0, 10.0, z=1))


def test_ghk_resting_voltage_is_physiological(sim):
    v = sim.ghk_voltage() * 1e3
    assert -80.0 < v < -60.0
    # the resting voltage must lie between the K and Na equilibrium potentials
    assert sim.nernst(5.0, 140.0) * 1e3 < v < sim.nernst(145.0, 15.0) * 1e3


def test_ghk_reduces_to_nernst_for_a_single_permeant_ion(sim):
    only_k = sim.with_changes(Na_P=0.0, Cl_P=0.0)
    assert sim.ghk_voltage(only_k) == pytest.approx(sim.nernst(5.0, 140.0))
    only_na = sim.with_changes(K_P=0.0, Cl_P=0.0)
    assert sim.ghk_voltage(only_na) == pytest.approx(sim.nernst(145.0, 15.0))


def test_raising_extracellular_potassium_depolarises(sim):
    assert sim.ghk_voltage(sim.with_changes(K_out=10.0)) > sim.ghk_voltage()


def test_with_changes_does_not_mutate_the_default_table(sim):
    sim.with_changes(K_out=50.0)
    assert sim.IONS_MAMMALIAN["K"]["out"] == 5.0


# ---------------------------------------------------------------- entropy

def test_entropy_budget_obeys_second_law(sim):
    b = sim.entropy_budget(100.0, 310.15, 293.15, 86400.0)
    assert b["produced_J_K"] > 0
    assert b["arriving_env_J_K"] == pytest.approx(8.64e6 / 293.15)
    # no production if body and room are at the same temperature
    assert sim.entropy_budget(100.0, 300.0, 300.0)["produced_J_K"] == pytest.approx(0.0, abs=1e-9)


def test_landauer_limit_value(sim):
    # k T ln2 at 300 K = 2.87e-21 J per bit
    assert 1.0 / sim.landauer_bits_per_second(1.0, 300.0) == pytest.approx(2.871e-21, rel=1e-3)
