import numpy as np
import pytest

FOLDER = "Module_03_The_Brain_Is_A_Radio"
FS = 250.0


def test_ideal_schumann_fundamental(sim):
    # c / (2 pi R_E) * sqrt(2) = 10.59 Hz for R_E = 6371 km
    assert float(sim.schumann_frequency(1)) == pytest.approx(10.59, abs=0.01)


def test_schumann_mode_ratios(sim):
    f = sim.schumann_frequency(np.array([1, 2, 3]))
    assert f[1] / f[0] == pytest.approx(np.sqrt(3.0))
    assert f[2] / f[0] == pytest.approx(np.sqrt(6.0))


def test_observed_schumann_below_ideal(sim):
    ideal = sim.schumann_frequency(np.arange(1, 6))
    ratio = np.array(sim.SCHUMANN_OBSERVED_HZ) / ideal
    assert np.all((ratio > 0.7) & (ratio < 0.9))


def test_field_budget_orders_of_magnitude(sim):
    fb = sim.field_budget()
    assert fb["induced_emf_V"] == pytest.approx(np.pi * 0.075 ** 2 * 2 * np.pi * 7.83 * 1e-12)
    assert fb["induced_emf_over_eeg"] < 1e-6          # nanovolt-scale pickup vs microvolt EEG
    assert fb["tacs_over_induced_E"] > 1e9
    assert fb["schumann_over_earth_static"] < 1e-7


def test_induced_field_scales_linearly_with_frequency_and_field(sim):
    assert sim.induced_e_field(2e-12, 7.83) == pytest.approx(2 * sim.induced_e_field(1e-12, 7.83))
    assert sim.induced_e_field(1e-12, 15.66) == pytest.approx(2 * sim.induced_e_field(1e-12, 7.83))


def test_pink_noise_has_one_over_f_slope(sim):
    x = sim.pink_noise(int(120 * FS), FS, np.random.default_rng(0))
    assert x.std() == pytest.approx(1.0)
    assert sim.spectral_slope(x, FS) == pytest.approx(-1.0, abs=0.15)


def test_welch_finds_sine_and_band_power_matches_amplitude(sim):
    t = np.arange(int(60 * FS)) / FS
    a, f0 = 3.0, 10.0
    f, pxx = sim.welch_psd(a * np.sin(2 * np.pi * f0 * t), FS)
    assert f[np.argmax(pxx)] == pytest.approx(f0, abs=0.25)
    assert sim.band_power(f, pxx, sim.BANDS["alpha"]) == pytest.approx(a ** 2 / 2, rel=0.02)
    assert sim.band_power(f, pxx, sim.BANDS["beta"]) < 1e-3 * a ** 2


def test_band_powers_sum_to_variance(sim):
    x = np.random.default_rng(1).standard_normal(int(60 * FS))
    f, pxx = sim.welch_psd(x, FS)
    assert sim.band_power(f, pxx, (0.0, FS / 2 + 1)) == pytest.approx(x.var(), rel=0.03)


def test_alpha_dominates_synthetic_eeg(sim):
    x, _ = sim.synthetic_eeg_pair("independent", 60, FS, seed=2)
    f, pxx = sim.welch_psd(x, FS)
    m = (f >= 4) & (f <= 20)
    assert 8.5 < f[m][np.argmax(pxx[m])] < 11.5


def test_plv_limits(sim):
    rng = np.random.default_rng(3)
    x = rng.standard_normal(int(60 * FS))
    assert sim.plv(x, x, FS, (8, 12)) == pytest.approx(1.0, abs=1e-9)
    t = np.arange(int(60 * FS)) / FS
    assert sim.plv(np.sin(2 * np.pi * 10 * t), np.sin(2 * np.pi * 10 * t + 1.0), FS, (8, 12)) == pytest.approx(1.0, abs=1e-4)
    y = rng.standard_normal(len(x))
    assert sim.plv(x, y, FS, (8, 12)) < 0.2


def test_sine_versus_sine_is_perfect_plv_but_not_evidence(sim):
    t = np.arange(int(60 * FS)) / FS
    res = sim.shift_surrogate_test(np.sin(2 * np.pi * 7.83 * t + 0.7), np.sin(2 * np.pi * 7.83 * t), FS, (6.5, 9.5))
    assert res["plv"] > 0.999
    assert res["p"] > 0.5


def test_shared_source_detected(sim):
    res = sim.shift_surrogate_test(*sim.synthetic_eeg_pair("shared", 60, FS, seed=5), FS, (8, 12))
    assert res["p"] < 0.01
    assert res["plv"] > np.percentile(res["null"], 99)


def test_false_positive_rate_is_calibrated(sim):
    rate = sim.detection_rate(lambda s: sim.synthetic_eeg_pair("independent", 30, FS, seed=s), FS, (8, 12), n_rep=60)
    assert rate <= 0.15        # nominal 0.05; 0.15 is > 3 binomial standard errors above it


def test_weak_schumann_coupling_is_detectable(sim):
    n = int(60 * FS)

    def make(seed, c):
        x, _ = sim.synthetic_eeg_pair("independent", 60, FS, seed=100 + seed)
        s = sim.schumann_record(n, FS, seed=500 + seed)
        return x + c * s, s

    assert sim.detection_rate(lambda s: make(s, 0.15), FS, (6.5, 9.5), n_rep=20) >= 0.9
    assert sim.detection_rate(lambda s: make(s, 0.0), FS, (6.5, 9.5), n_rep=20) <= 0.2


def test_decoherence_gap(sim):
    assert sim.decoherence_gap(1e-13, 1e-3) == pytest.approx(10.0)
    assert sim.decoherence_gap() >= 9


def test_load_user_eeg_roundtrip(sim, tmp_path):
    data = np.random.default_rng(6).standard_normal((500, 3))
    np.save(tmp_path / "eeg.npy", data)
    np.savetxt(tmp_path / "eeg.csv", data, delimiter=",", header="a,b,c", comments="")
    assert np.allclose(sim.load_user_eeg(tmp_path / "eeg.npy"), data)
    assert np.allclose(sim.load_user_eeg(tmp_path / "eeg.csv"), data)
    np.save(tmp_path / "one.npy", data[:, 0])
    assert sim.load_user_eeg(tmp_path / "one.npy").shape == (500, 1)
