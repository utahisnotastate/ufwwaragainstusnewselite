import numpy as np
import pytest

FOLDER = "Module_04_Matter_Is_Frozen_Light"


def test_electron_rest_energy(sim):
    assert sim.MEC2_EV == pytest.approx(510_998.95, abs=0.01)   # CODATA


def test_mass_defect_of_a_15_kiloton_bomb_is_under_a_gram(sim):
    assert sim.mass_defect(15 * sim.TNT_KT_J) == pytest.approx(6.98e-4, rel=1e-3)   # kg


def test_proton_mass_is_mostly_not_quark_rest_mass(sim):
    assert 0.005 < sim.proton_valence_quark_fraction() < 0.02


def test_breit_wheeler_threshold_head_on_and_angle(sim):
    assert sim.breit_wheeler_threshold(sim.MEC2_EV, np.pi) == pytest.approx(sim.MEC2_EV)
    assert sim.breit_wheeler_threshold(sim.MEC2_EV, np.pi / 2) == pytest.approx(2 * sim.MEC2_EV)
    assert float(sim.pair_beta(sim.mandelstam_s(sim.MEC2_EV, sim.MEC2_EV, np.pi))) == pytest.approx(0.0, abs=1e-6)
    assert float(sim.pair_beta(sim.mandelstam_s(1.0, 1.0, np.pi))) == 0.0          # far below threshold


def test_sunlight_cannot_make_pairs_with_sunlight(sim):
    assert sim.breit_wheeler_threshold(2.0) > 1e11


def test_cross_section_matches_dirac_annihilation_by_detailed_balance(sim):
    beta = np.array([0.01, 0.1, 0.3, 0.5, 0.7, 0.9, 0.99])
    assert np.allclose(sim.breit_wheeler_cross_section(beta), sim.breit_wheeler_from_annihilation(beta), rtol=1e-9)


def test_cross_section_near_threshold_is_pi_re2_beta(sim):
    beta = 1e-4
    assert float(sim.breit_wheeler_cross_section(beta)) == pytest.approx(np.pi * sim.R_E ** 2 * beta, rel=1e-6)


def test_cross_section_high_energy_asymptote(sim):
    s_over_m2 = 1e8                                  # s / (m c^2)^2
    beta = np.sqrt(1 - 4 / s_over_m2)
    expected = 4 * np.pi * sim.R_E ** 2 / s_over_m2 * (np.log(s_over_m2) - 1)
    assert float(sim.breit_wheeler_cross_section(beta)) == pytest.approx(expected, rel=1e-5)


def test_cross_section_peak_is_quarter_thomson(sim):
    b = np.linspace(1e-4, 1 - 1e-6, 100_001)
    sig = sim.breit_wheeler_cross_section(b)
    i = np.argmax(sig)
    assert sig[i] / sim.SIGMA_T == pytest.approx(0.256, abs=0.002)
    assert sig[i] * 1e4 == pytest.approx(1.70e-25, rel=0.01)       # cm^2
    assert b[i] == pytest.approx(0.70, abs=0.01)


def test_e144_kinematics_require_multiphoton_absorption(sim):
    edge = sim.compton_edge(46.6e9, 2.35)
    assert edge == pytest.approx(29.2e9, rel=0.01)
    assert sim.min_laser_photons(edge, 2.35) >= 2


def test_compton_edge_low_energy_limit(sim):
    # for x << 1 the edge is 4 gamma^2 w0 (here gamma ~ 200, x ~ 1.5e-5)
    e, w = 1e8, 1e-2
    gamma = e / sim.MEC2_EV
    assert sim.compton_edge(e, w) == pytest.approx(4 * gamma ** 2 * w, rel=1e-4)


def test_schwinger_field(sim):
    assert sim.schwinger_field() == pytest.approx(1.323e18, rel=1e-3)
    assert sim.intensity_to_field(sim.field_to_intensity_w_cm2(1e15)) == pytest.approx(1e15)


def test_record_laser_far_below_schwinger(sim):
    e = sim.intensity_to_field(sim.RECORD_LASER_W_CM2)
    assert e / sim.schwinger_field() < 1e-2
    assert sim.schwinger_suppression_log10(e) < -1000


def test_loop_moment_equals_bohr_magneton_by_construction(sim):
    assert sim.toroidal_model_moment() == pytest.approx(sim.MU_B, rel=1e-10)
    # same identity for any mass: the recipe cannot fail, so it cannot predict
    m = 3.7 * sim.M_E
    assert sim.toroidal_model_moment(m) == pytest.approx(sim.E_CHARGE * sim.HBAR / (2 * m), rel=1e-12)


def test_leading_qed_is_schwinger_term(sim):
    assert sim.qed_anomaly(1) == pytest.approx(sim.ALPHA_RB / (2 * np.pi))
    a_meas = sim.MEASURED_G_OVER_2 - 1
    assert sim.qed_anomaly(1) == pytest.approx(a_meas, rel=2e-3)


def test_qed_series_converges_on_measurement(sim):
    a_meas = sim.MEASURED_G_OVER_2 - 1
    errors = [abs(a_meas - sim.qed_anomaly(k)) for k in range(1, 5)]
    assert all(b < a for a, b in zip(errors, errors[1:]))
    assert errors[-1] < 1e-11                      # rest: 5-loop, muon/tau loops, hadronic, weak terms


def test_measured_moment_matches_codata(sim):
    from scipy.constants import physical_constants as pc
    assert sim.MEASURED_G_OVER_2 == pytest.approx(-pc["electron mag. mom. to Bohr magneton ratio"][0], abs=1e-12)


def test_loop_model_misses_anomaly_that_qed_gets(sim):
    a_meas = sim.MEASURED_G_OVER_2 - 1
    model_error = a_meas                           # model predicts g/2 = 1
    qed_error = abs(a_meas - sim.qed_anomaly(4))
    assert model_error / qed_error > 1e7


def test_electron_size_bound_versus_compton_radius(sim):
    assert sim.LAMBDA_C_BAR == pytest.approx(3.8616e-13, rel=1e-4)
    assert sim.LAMBDA_C_BAR / sim.ELECTRON_SIZE_BOUND_M > 1e5
