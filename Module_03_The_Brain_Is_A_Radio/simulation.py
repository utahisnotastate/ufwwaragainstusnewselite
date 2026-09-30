"""
Module 03 lab: is the brain "tuned" to the Earth's radio hum?

Four experiments, each computed rather than asserted:

1. schumann_frequency()        The Earth-ionosphere cavity really rings: ideal vs observed modes.
2. field_budget()              How strong is that signal at your head, compared with the brain's own fields?
3. plv() + shift_surrogate_test()
                               Real EEG signal processing (Welch spectra, band power, phase locking), and the
                               difference between a test that cannot fail and one that can.
4. decoherence_gap()           The quantum-brain (Orch-OR) timescale problem in numbers.

Everything runs on synthetic EEG-like data. To try real recordings (for example the PhysioNet EEG Motor
Movement/Imagery dataset, sampled at 160 Hz), export channels to a .csv or .npy file and run
    python simulation.py --data my_eeg.csv --fs 160 --channels 0 1
No network access is needed or used.
"""
import argparse

import numpy as np
from scipy import constants as sc
from scipy import signal
from scipy.integrate import trapezoid

C = sc.c
R_EARTH = 6.371e6                    # m, mean radius

# Observed Schumann resonance peaks, Hz (typical values; Nickolaenko & Hayakawa 2002)
SCHUMANN_OBSERVED_HZ = (7.83, 14.3, 20.8, 27.3, 33.8)
SCHUMANN_Q = 4.0                     # lossy cavity: each peak is ~2 Hz wide at 7.8 Hz

# Field magnitudes (orders of magnitude, see SCIENCE.md for sources)
SCHUMANN_B_T = 1e-12                 # magnetic field per mode, ~0.5-1 pT
MEG_B_T = (1e-13, 1e-12)             # brain's own magnetic field just outside the scalp (alpha up to ~1 pT)
EARTH_STATIC_B_T = 5e-5              # geomagnetic field
EEG_V = (1e-5, 1e-4)                 # scalp EEG amplitudes, 10-100 microvolts
TACS_E_V_M = 0.3                     # in-brain field of transcranial AC stimulation, order 0.1-1 V/m
HEAD_RADIUS_M = 0.075
COUPLING_DEMO = 0.07                 # amplitude of a planted Schumann copy in the power demonstration

# Decoherence and neural timescales, seconds
TEGMARK_MICROTUBULE_S = 1e-13        # upper end of Tegmark (2000) estimates for microtubule superpositions
HAGAN_MICROTUBULE_S = 1e-4           # upper end of the Hagan, Hameroff & Tuszynski (2002) rebuttal
NEURAL_S = {"action potential": 1e-3, "gamma cycle (Orch-OR's 25 ms)": 0.025}

BANDS = {"delta": (0.5, 4.0), "theta": (4.0, 8.0), "alpha": (8.0, 13.0), "beta": (13.0, 30.0), "gamma": (30.0, 80.0)}


# ---------------------------------------------------------------- 1. Schumann resonance
def schumann_frequency(n, radius=R_EARTH):
    """Ideal (lossless, thin-shell) Earth-ionosphere cavity modes: f_n = c / (2 pi R) * sqrt(n (n + 1))."""
    n = np.asarray(n, dtype=float)
    return C / (2.0 * np.pi * radius) * np.sqrt(n * (n + 1.0))


# ---------------------------------------------------------------- 2. Field budget
def induced_emf(b_tesla, freq_hz, radius=HEAD_RADIUS_M):
    """Peak EMF (V) that a uniform oscillating field induces around a loop the size of a head (Faraday)."""
    return np.pi * radius ** 2 * 2.0 * np.pi * freq_hz * b_tesla


def induced_e_field(b_tesla, freq_hz, radius=HEAD_RADIUS_M):
    """Peak induced electric field (V/m) at the edge of that loop: E = r * omega * B / 2."""
    return radius * 2.0 * np.pi * freq_hz * b_tesla / 2.0


def field_budget():
    """Compare the Schumann signal with the brain's own fields and with fields known to affect the brain."""
    f1 = SCHUMANN_OBSERVED_HZ[0]
    emf = induced_emf(SCHUMANN_B_T, f1)
    e_in = induced_e_field(SCHUMANN_B_T, f1)
    return {
        "schumann_over_earth_static": SCHUMANN_B_T / EARTH_STATIC_B_T,
        "schumann_over_meg_range": (SCHUMANN_B_T / MEG_B_T[1], SCHUMANN_B_T / MEG_B_T[0]),
        "induced_emf_V": emf,
        "induced_emf_over_eeg": emf / EEG_V[0],
        "induced_E_V_per_m": e_in,
        "tacs_over_induced_E": TACS_E_V_M / e_in,
    }


# ---------------------------------------------------------------- 3. Synthetic EEG and signal processing
def pink_noise(n, fs, rng):
    """Zero-mean, unit-variance noise with power spectral density proportional to 1/f."""
    spec = np.fft.rfft(rng.standard_normal(n))
    f = np.fft.rfftfreq(n, 1.0 / fs)
    spec[0] = 0.0
    spec[1:] /= np.sqrt(f[1:])
    x = np.fft.irfft(spec, n)
    return x / x.std()


def narrowband_noise(n, fs, f0, q, rng):
    """Unit-variance noise concentrated around f0 with quality factor q (bandwidth f0 / q): a 'rhythm'
    whose phase wanders, like a real brain rhythm or the lightning-driven Schumann field."""
    half = f0 / (2.0 * q)
    x = bandpass(rng.standard_normal(n), fs, (f0 - half, f0 + half), order=2)
    return x / x.std()


def burst_envelope(n, fs, rng, rate_hz=0.4, width_s=0.6):
    """Random Gaussian bursts (alpha comes and goes), scaled so the peak envelope is ~1."""
    t = np.arange(n) / fs
    centres = rng.uniform(0.0, n / fs, rng.poisson(rate_hz * n / fs) + 1)
    env = np.exp(-0.5 * ((t[:, None] - centres[None, :]) / width_s) ** 2).sum(axis=1)
    return env / env.max()


def synthetic_eeg_pair(kind, duration_s=60.0, fs=250.0, seed=0, alpha_gain=1.5, lag_s=0.012):
    """Two EEG-like channels (arbitrary units ~ 10 uV): 1/f background plus 10 Hz alpha bursts.

    kind = 'shared'      : both channels see the same alpha generator (second one delayed by lag_s).
    kind = 'independent' : each channel has its own alpha generator; no true coupling.
    """
    rng = np.random.default_rng(seed)
    n = int(duration_s * fs)
    alpha1 = narrowband_noise(n, fs, 10.0, 5.0, rng) * burst_envelope(n, fs, rng)
    if kind == "shared":
        alpha2 = np.roll(alpha1, int(round(lag_s * fs)))
    elif kind == "independent":
        alpha2 = narrowband_noise(n, fs, 10.0, 5.0, rng) * burst_envelope(n, fs, rng)
    else:
        raise ValueError("kind must be 'shared' or 'independent'")
    x = pink_noise(n, fs, rng) + alpha_gain * alpha1
    y = pink_noise(n, fs, rng) + alpha_gain * alpha2
    return x, y


def schumann_record(n, fs, seed=0, f0=SCHUMANN_OBSERVED_HZ[0], q=SCHUMANN_Q):
    """A magnetometer-like Schumann trace: narrowband noise at 7.83 Hz, Q ~ 4 (driven by random lightning)."""
    return narrowband_noise(n, fs, f0, q, np.random.default_rng(seed))


def welch_psd(x, fs, seg_s=4.0):
    """Welch power spectral density (units^2 / Hz) with Hann windows of seg_s seconds and 50 % overlap."""
    return signal.welch(x, fs=fs, nperseg=int(seg_s * fs))


def band_power(f, pxx, band):
    """Power in a frequency band: the integral of the PSD over [lo, hi)."""
    m = (f >= band[0]) & (f < band[1])
    return float(trapezoid(pxx[m], f[m]))


def bandpass(x, fs, band, order=4):
    """Zero-phase Butterworth band-pass filter."""
    sos = signal.butter(order, band, btype="bandpass", fs=fs, output="sos")
    return signal.sosfiltfilt(sos, x)


def instantaneous_phase(x, fs, band, trim_s=1.0):
    """Phase of the analytic (Hilbert) signal after band-pass filtering; filter edges trimmed off."""
    k = int(trim_s * fs)
    return np.angle(signal.hilbert(bandpass(x, fs, band)))[k:len(x) - k]


def plv_from_phases(p1, p2):
    """Phase-locking value |<exp(i (phi1 - phi2))>|: 1 = constant phase difference, ~0 = no relation."""
    return float(np.abs(np.mean(np.exp(1j * (p1 - p2)))))


def plv(x, y, fs, band):
    """Phase-locking value between two signals in a frequency band."""
    return plv_from_phases(instantaneous_phase(x, fs, band), instantaneous_phase(y, fs, band))


def shift_surrogate_test(x, y, fs, band, n_surr=199, min_shift_s=2.0, seed=0):
    """Is the observed PLV larger than PLVs between x and time-shifted copies of y?

    Shifting y by more than its correlation time destroys any genuine moment-to-moment coupling but keeps
    each signal's own spectrum and rhythmicity. Every statistic (observed and null) uses the same number of
    samples, so finite-sample bias cancels. Returns dict(plv, null, p) with p = (1 + #null >= obs) / (1 + N).
    """
    px = instantaneous_phase(x, fs, band)
    py = instantaneous_phase(y, fs, band)
    n = len(px)
    max_shift = n // 3
    m = n - max_shift
    min_shift = int(min_shift_s * fs)
    if max_shift <= min_shift:
        raise ValueError("Record too short for the requested minimum shift.")
    rng = np.random.default_rng(seed)
    shifts = rng.choice(np.arange(min_shift, max_shift + 1), size=min(n_surr, max_shift - min_shift + 1), replace=False)
    zx, zy = np.exp(1j * px[:m]), np.exp(-1j * py)       # unit phasors; PLV = |mean(zx * conj(zy))|
    obs = float(np.abs(np.mean(zx * zy[:m])))
    null = np.array([np.abs(np.mean(zx * zy[k:k + m])) for k in shifts])
    tol = 1e-6                     # FFT-Hilbert edge ripple moves a perfect PLV of 1 by ~1e-7
    p = (1.0 + np.sum(null >= obs - tol)) / (1.0 + len(null))
    return {"plv": obs, "null": null, "p": float(p)}


def detection_rate(make_pair, fs, band, n_rep=40, alpha=0.05, n_surr=99):
    """Fraction of independent recordings in which shift_surrogate_test gives p < alpha.

    make_pair(seed) -> (x, y). With no true coupling this is the false-positive rate (should be ~alpha);
    with coupling it is the test's power.
    """
    hits = [shift_surrogate_test(*make_pair(s), fs, band, n_surr=n_surr, seed=s)["p"] < alpha for s in range(n_rep)]
    return float(np.mean(hits))


def spectral_slope(x, fs, fmin=2.0, fmax=40.0):
    """Log-log slope of the Welch PSD between fmin and fmax (1/f noise gives -1)."""
    f, pxx = welch_psd(x, fs)
    m = (f >= fmin) & (f <= fmax)
    return float(np.polyfit(np.log(f[m]), np.log(pxx[m]), 1)[0])


# ---------------------------------------------------------------- 4. Quantum-brain timescales
def decoherence_gap(tau_decoherence=TEGMARK_MICROTUBULE_S, tau_neural=NEURAL_S["action potential"]):
    """Orders of magnitude between how long a quantum superposition survives and how long a neural event takes."""
    return float(np.log10(tau_neural / tau_decoherence))


# ---------------------------------------------------------------- Optional real data
def load_user_eeg(path):
    """Load a user-supplied recording as an array of shape (n_samples, n_channels) from .npy or .csv/.txt."""
    path = str(path)
    if path.endswith(".npy"):
        data = np.load(path)
    else:
        try:
            data = np.loadtxt(path, delimiter=",")
        except ValueError:
            data = np.loadtxt(path, delimiter=",", skiprows=1)
    data = np.asarray(data, dtype=float)
    return data[:, None] if data.ndim == 1 else data


def _report_pair(x, y, fs, band, label):
    res = shift_surrogate_test(x, y, fs, band)
    null95 = np.percentile(res["null"], 95)
    verdict = "significant" if res["p"] < 0.05 else "not significant"
    print(f"   {label:52s} PLV = {res['plv']:.3f}   null 95% = {null95:.3f}   p = {res['p']:.3f}  ({verdict})")
    return res


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", help="optional .csv or .npy file, samples x channels")
    ap.add_argument("--fs", type=float, default=160.0, help="sampling rate of --data in Hz")
    ap.add_argument("--channels", type=int, nargs=2, default=(0, 1))
    args = ap.parse_args(argv)

    print("1) The Earth really hums: Schumann resonances")
    print("   n   ideal lossless cavity   observed   observed/ideal")
    for n, fo in enumerate(SCHUMANN_OBSERVED_HZ, start=1):
        fi = float(schumann_frequency(n))
        print(f"   {n}   {fi:10.2f} Hz          {fo:6.2f} Hz   {fo / fi:8.3f}")
    print("   The real cavity is lossy (the ionosphere is a poor conductor), which lowers every peak.\n")

    fb = field_budget()
    print("2) How loud is the hum at your head?")
    print(f"   Schumann magnetic field / Earth's static field      = {fb['schumann_over_earth_static']:.0e}")
    lo, hi = fb["schumann_over_meg_range"]
    print(f"   Schumann field / brain's own field outside the head  = {lo:.0f} to {hi:.0f}  (similar size: why MEG needs shielded rooms)")
    print(f"   EMF induced around a head-sized loop at 7.83 Hz      = {fb['induced_emf_V']:.1e} V "
          f"= {fb['induced_emf_over_eeg']:.0e} of a 10 uV EEG signal")
    print(f"   Induced electric field in the head                   = {fb['induced_E_V_per_m']:.1e} V/m; brain stimulation "
          f"(tACS, ~{TACS_E_V_M} V/m) is {fb['tacs_over_induced_E']:.0e} times stronger\n")

    fs, dur = 250.0, 60.0
    n = int(fs * dur)
    t = np.arange(n) / fs
    x, _ = synthetic_eeg_pair("independent", dur, fs, seed=1)
    f, pxx = welch_psd(x, fs)
    total = band_power(f, pxx, (0.5, 80.0))
    print("3) Signal processing on 60 s of synthetic EEG (1/f background + 10 Hz alpha bursts)")
    print("   " + "   ".join(f"{b} {100 * band_power(f, pxx, r) / total:4.1f}%" for b, r in BANDS.items()))
    m = (f >= 4) & (f <= 20)
    print(f"   Alpha peak at {f[m][np.argmax(pxx[m])]:.2f} Hz; background spectral slope {spectral_slope(pink_noise(n, fs, np.random.default_rng(2)), fs):.2f} (1/f gives -1)\n")

    sband = (6.5, 9.5)
    ref = np.sin(2 * np.pi * 7.83 * t)
    print("   a) The flawed test: compare against a perfect 7.83 Hz sine")
    naive = _report_pair(np.sin(2 * np.pi * 7.83 * t + 0.7), ref, fs, sband, "7.83 Hz sine vs 7.83 Hz sine")
    if naive["plv"] > 0.99 and naive["p"] >= 0.05:
        print("      PLV is ~1 by construction, and the surrogate test correctly reports that this proves nothing:")
        print("      any two steady signals at the same frequency are 'locked', whether or not they are connected.")
    reps = 100
    print(f"   b) A test that can fail: EEG vs a realistic (wandering-phase) Schumann record, {reps} recordings each")

    def eeg_vs_schumann(coupling):
        def make(seed):
            x_, _ = synthetic_eeg_pair("independent", dur, fs, seed=100 + seed)
            s_ = schumann_record(n, fs, seed=500 + seed)
            return x_ + coupling * s_, s_
        return make

    fpr = detection_rate(eeg_vs_schumann(0.0), fs, sband, reps)
    power = detection_rate(eeg_vs_schumann(COUPLING_DEMO), fs, sband, reps)
    se = 100 * np.sqrt(0.05 * 0.95 / reps)
    print(f"      no coupling:          p < 0.05 in {100 * fpr:5.1f}% of recordings "
          f"(a calibrated test gives 5 +/- {se:.1f}%)")
    print(f"      weak coupling built in ({COUPLING_DEMO} x record): detected in {100 * power:5.1f}% of recordings")
    if power > 0.8 and fpr < 0.1:
        print("      The test can say yes, so its 'no' means something.")
    print(f"   c) Two EEG channels, 8-12 Hz, {reps} recordings each")
    for kind in ("shared", "independent"):
        rate = detection_rate(lambda sd, k=kind: synthetic_eeg_pair(k, dur, fs, seed=900 + sd), fs, (8.0, 12.0), reps)
        print(f"      {kind:11s} alpha generator(s): p < 0.05 in {100 * rate:5.1f}% of recordings")
    print()

    print("4) Quantum brain (Orch-OR) timescales")
    for name, tn in NEURAL_S.items():
        print(f"   {name:30s} / Tegmark decoherence 1e-13 s = 10^{decoherence_gap(TEGMARK_MICROTUBULE_S, tn):.0f};"
              f"  / rebuttal estimate 1e-4 s = 10^{decoherence_gap(HAGAN_MICROTUBULE_S, tn):.1f}")
    worst = min(decoherence_gap(HAGAN_MICROTUBULE_S, tn) for tn in NEURAL_S.values())
    if worst > 0:
        print(f"   Even the most favourable published estimate is 10^{worst:.1f} too short for the neural timescales above.")
    else:
        print("   With these inputs a decoherence estimate reaches neural timescales; check the assumptions.")

    if args.data:
        data = load_user_eeg(args.data)
        i, j = args.channels
        print(f"\n5) Your data: {data.shape[0]} samples x {data.shape[1]} channels at {args.fs} Hz, channels {i} and {j}")
        f, pxx = welch_psd(data[:, i], args.fs)
        total = band_power(f, pxx, (0.5, min(80.0, args.fs / 2 - 1)))
        print("   " + "   ".join(f"{b} {100 * band_power(f, pxx, r) / total:4.1f}%" for b, r in BANDS.items() if r[1] < args.fs / 2))
        _report_pair(data[:, i], data[:, j], args.fs, (8.0, 12.0), "alpha-band PLV between your channels")
        print("   Nearby electrodes share volume-conducted sources, so high PLV there is expected, not telepathy.")


if __name__ == "__main__":
    main()
