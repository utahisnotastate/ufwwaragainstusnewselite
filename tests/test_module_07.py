import numpy as np
import pytest

FOLDER = "Module_07_DNA_Antenna"


# ---------------------------------------------------------------- geometry and the antenna idea

def test_b_dna_geometry(sim):
    g = sim.b_dna_geometry()
    assert 3.4 <= g["pitch_nm"] <= 3.6
    assert g["circumference_nm"] == pytest.approx(2 * np.pi, rel=1e-12)   # pi x 2.0 nm
    assert g["twist_deg_per_bp"] == pytest.approx(34.3, abs=0.1)
    assert g["pitch_angle_deg"] > 14          # outside Kraus's 12-14 degree sweet spot


def test_kraus_band_brackets_circumference(sim):
    lo, hi = sim.helical_antenna_band(6.0)
    assert lo == pytest.approx(4.5) and hi == pytest.approx(8.0)
    assert lo < 6.0 < hi


def test_dna_helix_would_tune_to_euv_not_visible(sim):
    lo, hi = sim.helical_antenna_band(sim.b_dna_geometry()["circumference_nm"])
    assert 4.5 < lo < hi < 9.0
    assert sim.photon_energy_ev(hi) > 100           # > 100 eV: extreme UV / soft X-ray
    m_lo, m_hi = sim.biophoton_mismatch()
    assert m_lo > 30 and m_hi > 120


def test_photon_energy_reference(sim):
    assert sim.photon_energy_ev(1239.84198) == pytest.approx(1.0, rel=1e-6)


def test_photon_hits_scale_with_flux(sim):
    assert sim.photon_hits_per_turn(200.0) == pytest.approx(2 * sim.photon_hits_per_turn(100.0))
    assert sim.photon_hits_per_turn(100.0) == pytest.approx(100 * 2.0 * 3.57e-14, rel=1e-9)


# ---------------------------------------------------------------- UV absorption

def test_uv_extinction_per_nucleotide(sim):
    uv = sim.uv_absorption()
    assert uv["eps_per_nt"] == pytest.approx(6600, rel=0.02)     # classic value for native dsDNA
    assert 0.25 < uv["hypochromicity"] < 0.45                    # stacking weakens absorption by ~30-40 %
    assert uv["photon_energy_ev"] == pytest.approx(4.77, abs=0.01)


def test_single_stranded_rule_gives_less_hypochromism(sim):
    ss = sim.uv_absorption(conc_ug_per_ml=33.0)                   # ssDNA rule: A260 = 1 for ~33 µg/mL
    ds = sim.uv_absorption(conc_ug_per_ml=50.0)
    assert ss["hypochromicity"] < ds["hypochromicity"]


# ---------------------------------------------------------------- FRET

def test_fret_limits(sim):
    assert float(sim.fret_efficiency(5.0, 5.0)) == pytest.approx(0.5)
    assert float(sim.fret_efficiency(0.0, 5.0)) == 1.0
    e1, e2 = sim.fret_efficiency([50.0, 100.0], 5.0)
    assert e1 / e2 == pytest.approx(64, rel=1e-4)                 # r^-6 tail


def test_fret_along_dna_is_monotonic_and_short_ranged(sim):
    e = sim.fret_along_dna(np.arange(1, 60))
    assert np.all(np.diff(e) < 0)
    assert float(sim.fret_along_dna(15)) == pytest.approx(0.5, abs=0.05)
    assert float(sim.fret_along_dna(60)) < 0.01


# ---------------------------------------------------------------- Peyrard-Bishop

def test_morse_minimum_and_plateau(sim):
    assert float(sim.morse(0.0)) == 0.0
    assert float(sim.morse(50.0)) == pytest.approx(sim.PB["D"])
    assert float(sim.morse(-0.1)) > 0 and float(sim.morse(0.1)) > 0


def test_numeric_hessian_modes_match_analytic_dispersion(sim):
    n = 24
    w_num = sim.pb_mode_frequencies_numeric(n=n)
    q = 2 * np.pi * np.arange(n) / n
    w_exact = np.sort(sim.pb_dispersion(q))
    assert np.allclose(w_num, w_exact, rtol=1e-4)


def test_pb_gap_is_set_by_morse_curvature(sim):
    w0 = sim.pb_dispersion(0.0)
    K0 = 2 * sim.PB["D"] * sim.PB["a"] ** 2 * sim.EV / 1e-20
    assert w0 == pytest.approx(np.sqrt(K0 / (sim.PB_MASS_AMU * sim.sc.atomic_mass)))


def test_transfer_integral_matches_harmonic_chain_at_low_T(sim):
    """As T -> 0 the Morse well is harmonic; the anharmonic correction to the variance grows ∝ T."""
    dev = []
    for T in (1.0, 2.0):
        w = 0.2 * np.sqrt(T)
        _, var = sim.pb_transfer_integral(T, y_min=-w, y_max=w, n=400)
        dev.append(var / sim.pb_harmonic_variance(T) - 1)
    assert abs(dev[0]) < 0.01
    assert dev[1] / dev[0] == pytest.approx(2.0, rel=0.05)


def test_base_pairs_bound_at_body_temperature(sim):
    small = sim.pb_transfer_integral(310.0, y_max=20.0, n=300)[0]
    big = sim.pb_transfer_integral(310.0, y_max=40.0, n=600)[0]
    assert big == pytest.approx(small, rel=1e-3) and small < 1.0


def test_strands_separate_when_hot(sim):
    small = sim.pb_transfer_integral(650.0, y_max=20.0, n=300)[0]
    big = sim.pb_transfer_integral(650.0, y_max=40.0, n=600)[0]
    assert big > 1.5 * small


def test_opening_grows_with_temperature(sim):
    means = [sim.pb_transfer_integral(T, n=300)[0] for T in (200, 300, 400)]
    assert means[0] < means[1] < means[2]


# ---------------------------------------------------------------- screening and absorption

def test_debye_length_matches_0304_over_sqrt_I(sim):
    for I in (0.001, 0.01, 0.15, 1.0):
        assert sim.debye_length(I) * 1e9 == pytest.approx(0.304 / np.sqrt(I), rel=0.01)


def test_debye_length_physiological(sim):
    assert 0.7e-9 < sim.debye_length(0.15) < 0.8e-9


def test_screening_kills_long_range_fields(sim):
    assert float(sim.screened_fraction(sim.debye_length(0.15))) == pytest.approx(np.exp(-1))
    assert float(sim.screened_fraction(10e-9)) < 1e-5


def test_water_debye_model_limits(sim):
    eps_low = sim.water_permittivity(1e3, sigma=0.0)
    eps_high = sim.water_permittivity(1e15, sigma=0.0)
    assert eps_low.real == pytest.approx(sim.EPS_STATIC, rel=1e-6)
    assert eps_high.real == pytest.approx(sim.EPS_INF, rel=1e-4)
    f = np.logspace(9, 12, 3001)
    loss = -sim.water_permittivity(f, sigma=0.0).imag
    assert f[np.argmax(loss)] == pytest.approx(1 / (2 * np.pi * sim.TAU_WATER), rel=0.01)   # ~19 GHz


def test_microwaves_die_within_centimetres(sim):
    depths = sim.field_penetration_depth(np.array([1e9, 1e10, 1e11]))
    assert np.all(np.diff(depths) < 0)
    assert 0.01 < depths[0] < 0.05          # cm-scale at 1 GHz
    assert depths[2] < 1e-3                 # sub-mm at 100 GHz


def test_short_dipole_resistance_formula(sim):
    lam = 1.0
    f = sim.sc.c / lam
    assert sim.short_dipole_radiation_resistance(0.1 * lam, f) == pytest.approx(0.8 * np.pi ** 2)
    assert sim.short_dipole_radiation_resistance(50e-9, 1e9) < 1e-9


def test_rf_photons_are_far_below_kT(sim):
    assert sim.rf_photon_vs_thermal(1e9) == pytest.approx(1.55e-4, rel=0.02)
    assert sim.rf_photon_vs_thermal(sim.sc.c / 260e-9) > 100
