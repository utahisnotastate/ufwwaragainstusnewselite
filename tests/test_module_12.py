import numpy as np
import pytest

FOLDER = "Module_12_The_Psychotronic_Internet"


# ---------------------------------------------------------------- skin depth

def test_seawater_skin_depth_at_navy_elf_frequency(sim):
    assert sim.skin_depth(76.0, 4.0) == pytest.approx(28.9, abs=0.1)


def test_copper_skin_depth_published_values(sim):
    assert sim.skin_depth(1e6, sim.SIGMA_COPPER) * 1e6 == pytest.approx(65.2, abs=0.3)   # um
    assert sim.skin_depth(60.0, sim.SIGMA_COPPER) * 1e3 == pytest.approx(8.4, abs=0.1)   # mm


def test_skin_depth_scales_as_inverse_root_frequency_and_conductivity(sim):
    assert sim.skin_depth(100.0, 4.0) / sim.skin_depth(400.0, 4.0) == pytest.approx(2.0)
    assert sim.skin_depth(100.0, 1.0) / sim.skin_depth(100.0, 9.0) == pytest.approx(3.0)
    f = np.logspace(1, 6, 11)
    slope = np.polyfit(np.log(f), np.log(sim.skin_depth(f, 4.0)), 1)[0]
    assert slope == pytest.approx(-0.5, abs=1e-12)


def test_full_formula_reduces_to_skin_depth_for_good_conductors(sim):
    for f in (76.0, 3e3, 1e5):
        assert sim.attenuation_length(f, 4.0) == pytest.approx(sim.skin_depth(f, 4.0), rel=1e-3)


def test_full_formula_departs_when_displacement_current_dominates(sim):
    # at 2.4 GHz, omega*eps > sigma for seawater: the good-conductor formula underestimates the depth
    assert sim.attenuation_length(2.4e9, 4.0) > 1.5 * sim.skin_depth(2.4e9, 4.0)
    # weak-loss limit: alpha -> (sigma/2) sqrt(mu/eps)
    sigma, eps_r = 1e-4, 80.0
    alpha = sigma / 2 * np.sqrt(sim.MU0 / (eps_r * sim.EPS0))
    assert sim.attenuation_length(1e9, sigma, eps_r) == pytest.approx(1 / alpha, rel=1e-4)


def test_shield_absorption_is_8_686_dB_per_skin_depth(sim):
    d = sim.skin_depth(1e6, sim.SIGMA_COPPER)
    assert sim.shield_absorption_db(d, 1e6) == pytest.approx(8.686, abs=1e-3)
    assert sim.shield_absorption_db(3 * d, 1e6) == pytest.approx(3 * 8.686, abs=3e-3)


# ---------------------------------------------------------------- static screening

def test_field_inside_conducting_sphere_vanishes(sim):
    pts = np.array([[0, 0, 0], [0.4, -0.2, 0.3], [0, 0, -0.6]], dtype=float)
    e = sim.conducting_sphere_field(pts, n=300)
    assert np.all(np.linalg.norm(e, axis=1) < 1e-3)


def test_field_outside_sphere_matches_dipole_solution(sim):
    for p in (np.array([0, 0, 2.0]), np.array([1.5, 0.5, 1.0]), np.array([3.0, 0, 0])):
        e = sim.conducting_sphere_field(p, n=300)[0]
        assert np.allclose(e, sim.sphere_field_outside_theory(p), atol=1e-3)


def test_surface_charge_really_does_something(sim):
    """Guard against a trivially-zero result: outside on the equator the field is weakened (E_z < E0)."""
    e = sim.conducting_sphere_field(np.array([1.5, 0, 0]), n=300)[0]
    assert e[2] < 0.8


# ---------------------------------------------------------------- counter-wound coils

@pytest.mark.parametrize("kd", [1e-3, 0.05, 0.5, 2.0, 10.0])
def test_numerical_far_field_matches_closed_form(sim, kd):
    assert sim.antiparallel_pair_power(kd) == pytest.approx(float(sim.antiparallel_pair_power_theory(kd)), rel=1e-3)


def test_small_pair_is_a_weak_quadrupole(sim):
    for kd in (1e-3, 1e-2):
        assert sim.antiparallel_pair_power(kd) == pytest.approx(kd ** 2 / 5, rel=1e-3)
    assert sim.antiparallel_pair_power(0.0) == 0.0


def test_well_separated_coils_radiate_independently(sim):
    assert sim.antiparallel_pair_power(200.0) == pytest.approx(2.0, rel=0.01)


def test_counterwound_near_field_falls_one_power_faster(sim):
    assert sim.falloff_exponent(sim.loop_axis_field) == pytest.approx(-3.0, abs=0.01)
    assert sim.falloff_exponent(sim.counterwound_axis_field) == pytest.approx(-4.0, abs=0.01)


def test_loop_centre_field(sim):
    # B = mu0 I / (2R) at the centre of a loop
    assert sim.loop_axis_field(0.0, 2.0, 0.1) == pytest.approx(sim.MU0 * 2.0 / 0.2)


# ---------------------------------------------------------------- Aharonov-Bohm

def test_flux_quantum_h_over_e(sim):
    assert sim.FLUX_QUANTUM == pytest.approx(4.135667696e-15, rel=1e-9)
    assert sim.aharonov_bohm_phase(sim.FLUX_QUANTUM) == pytest.approx(2 * np.pi)


# ---------------------------------------------------------------- speed limit and entanglement

def test_light_delays(sim):
    assert sim.light_delay(384_400e3) == pytest.approx(1.282, abs=0.001)
    assert 3.0 < sim.light_delay(54.6e9) / 60 < 3.1
    assert 22.0 < sim.light_delay(401e9) / 60 < 22.5


@pytest.mark.parametrize("angle", [None, 0.0, 0.7, np.pi / 2, 2.1, np.pi])
def test_no_communication_bob_always_sees_half_half(sim, angle):
    assert np.allclose(sim.bob_state(angle), np.eye(2) / 2, atol=1e-12)


def test_measurement_changes_the_joint_state_even_though_bob_cannot_tell(sim):
    """Alice's measurement is not a no-op: the joint state changes, yet Bob's local state does not."""
    ops = [np.kron(sim._projector(0.7, k), np.eye(2)) for k in (0, 1)]
    after = sum(o @ sim.RHO_BELL @ o for o in ops)
    assert not np.allclose(after, sim.RHO_BELL)


def test_bell_correlations_follow_cos_squared(sim):
    for a, b in ((0.0, 0.0), (0.0, np.pi / 3), (0.4, 1.9), (0.0, np.pi)):
        assert sim.same_outcome_probability(a, b) == pytest.approx(np.cos((a - b) / 2) ** 2)


def test_partial_trace_detects_a_non_maximally_mixed_state(sim):
    """The no-signalling check could fail: a product state |0>|0> gives Bob a pure |0>."""
    psi = np.array([1.0, 0, 0, 0])
    assert np.allclose(sim.bob_state(None, np.outer(psi, psi)), [[1, 0], [0, 0]])


# ---------------------------------------------------------------- brains and bandwidth

def test_brain_field_is_dipolar(sim):
    assert sim.brain_field(0.04) == pytest.approx(sim.MEG_FIELD_T)
    assert sim.brain_field(1.0) / sim.brain_field(2.0) == pytest.approx(8.0)
    assert sim.brain_field(1.0) < 1e-15


def test_bandwidth_numbers(sim):
    assert sim.bci_bits_per_second(90.0, 1.0) == pytest.approx(1.5)
    assert sim.transfer_time(1e6, 39.0) / 3600 == pytest.approx(57.0, abs=0.1)
