"""
Module 07 lab: DNA as a physical object, and why it is not a radio antenna.

Six experiments, each computed from first principles:

1. b_dna_geometry(), helical_antenna_band()   If B-DNA were a metal helix, what would it tune to?  (~6 nm: EUV/soft X-ray.)
2. uv_absorption()                            What DNA really absorbs: UV near 260 nm, weakened by base stacking.
3. fret_efficiency()                          Real, short-range energy transfer along DNA: the Förster 'ruler'.
4. peyrard_bishop_*                           A physical model of base-pair opening (melting) and of DNA's vibrations.
5. debye_length(), water_permittivity()       Where the claim breaks: salt water screens charges within ~0.8 nm and
                                              absorbs microwaves within millimetres to centimetres.
6. rf_photon_vs_thermal()                     Radio photons carry ~10^-4 of the thermal energy kT.

Run:  python simulation.py
"""
import numpy as np
from scipy import constants as sc

# B-DNA (textbook averages)
RISE_NM = 0.34              # nm per base pair along the axis
BP_PER_TURN = 10.5          # base pairs per helical turn in solution
DIAMETER_NM = 2.0           # nm
PERSISTENCE_LENGTH_NM = 50.0  # nm, bending stiffness scale of dsDNA in physiological salt
T_BODY = 310.15             # K

# Water at 25 °C, single Debye relaxation (approximate literature values)
EPS_STATIC = 78.4
EPS_INF = 5.2
TAU_WATER = 8.3e-12         # s  (relaxation frequency ~19 GHz)
SIGMA_SALINE = 1.6          # S/m, ~0.15 M NaCl at 25 °C

EV = sc.electron_volt
KB_EV = sc.k / EV


# ---------------------------------------------------------------- 1. geometry and the antenna idea

def b_dna_geometry(rise=RISE_NM, bp_per_turn=BP_PER_TURN, diameter=DIAMETER_NM):
    """Pitch, circumference and pitch angle of the B-DNA helix (nm, degrees)."""
    pitch = rise * bp_per_turn
    circumference = np.pi * diameter
    return {
        "pitch_nm": pitch,
        "circumference_nm": circumference,
        "twist_deg_per_bp": 360.0 / bp_per_turn,
        "pitch_angle_deg": np.degrees(np.arctan(pitch / circumference)),
    }


def helical_antenna_band(circumference_nm):
    """Kraus axial (end-fire) mode of a helical antenna: 3/4 < C/lambda < 4/3. Returns (lambda_min, lambda_max) in nm."""
    return circumference_nm / (4.0 / 3.0), circumference_nm / (3.0 / 4.0)


def photon_energy_ev(wavelength_nm):
    """E = h c / lambda, in eV."""
    return sc.h * sc.c / (np.asarray(wavelength_nm, float) * 1e-9) / EV


def biophoton_mismatch(band_nm=(200.0, 800.0), circumference_nm=None):
    """How far the ultraweak-photon band sits from the helix's 'tuned' wavelength (C / lambda = 1)."""
    c = circumference_nm or b_dna_geometry()["circumference_nm"]
    return band_nm[0] / c, band_nm[1] / c


def photon_hits_per_turn(flux_per_cm2_s=100.0, rise=RISE_NM, bp_per_turn=BP_PER_TURN, diameter=DIAMETER_NM):
    """Photons per second landing on the side of one helical turn if a biophoton flux were aimed at it."""
    area_cm2 = (diameter * rise * bp_per_turn) * 1e-14      # nm^2 -> cm^2
    return flux_per_cm2_s * area_cm2


# ---------------------------------------------------------------- 2. UV absorption

def uv_absorption(conc_ug_per_ml=50.0, mw_per_nt=330.0, eps_mono=(15.4e3, 7.4e3, 11.5e3, 8.7e3)):
    """Extinction coefficient per nucleotide from the lab rule 'A260 = 1 for 50 µg/mL dsDNA' (1 cm path).

    eps_mono: approximate 260 nm extinction coefficients (M^-1 cm^-1) of dAMP, dCMP, dGMP, dTMP.
    Hypochromicity = how much weaker the stacked double helix absorbs than its free nucleotides.
    """
    molar_nt = conc_ug_per_ml * 1e-3 / mw_per_nt            # g/L / (g/mol) = mol/L of nucleotides
    eps_polymer = 1.0 / molar_nt                            # A = eps * c * l with A = 1, l = 1 cm
    eps_free = float(np.mean(eps_mono))
    return {
        "eps_per_nt": eps_polymer,
        "eps_free_nt": eps_free,
        "hypochromicity": 1.0 - eps_polymer / eps_free,
        "photon_energy_ev": float(photon_energy_ev(260.0)),
    }


# ---------------------------------------------------------------- 3. FRET along the helix

def fret_efficiency(r_nm, R0_nm=5.0):
    """Förster efficiency E = 1 / (1 + (r / R0)^6)."""
    return 1.0 / (1.0 + (np.asarray(r_nm, float) / R0_nm) ** 6)


def fret_along_dna(n_bp, R0_nm=5.0, rise=RISE_NM):
    """FRET efficiency between dyes n_bp base pairs apart (axial distance only; linkers and twist ignored)."""
    return fret_efficiency(np.asarray(n_bp, float) * rise, R0_nm)


# ---------------------------------------------------------------- 4. Peyrard-Bishop model

PB = dict(k=0.06, D=0.04, a=4.45)   # eV/Å^2, eV, 1/Å : illustrative values of the size used in the PB literature
PB_MASS_AMU = 300.0


def morse(y, D=PB["D"], a=PB["a"]):
    """On-site Morse potential for the stretch y (Å) of a base pair: V = D (exp(-a y) - 1)^2."""
    return D * (np.exp(-a * np.asarray(y, float)) - 1.0) ** 2


def pb_energy(y, k=PB["k"], D=PB["D"], a=PB["a"]):
    """Potential energy (eV) of a ring of base pairs: sum of k/2 (y_n - y_{n-1})^2 + V(y_n)."""
    y = np.asarray(y, float)
    return 0.5 * k * np.sum((y - np.roll(y, 1)) ** 2) + np.sum(morse(y, D, a))


def pb_mode_frequencies_numeric(n=24, h=1e-4, **p):
    """Small-oscillation angular frequencies (rad/s) from a finite-difference Hessian of pb_energy at y = 0."""
    H = np.empty((n, n))
    e = lambda y: pb_energy(y, **p)
    for i in range(n):
        for j in range(n):
            yp = np.zeros(n)
            def f(di, dj):
                y = yp.copy(); y[i] += di; y[j] += dj
                return e(y)
            H[i, j] = (f(h, h) - f(h, -h) - f(-h, h) + f(-h, -h)) / (4 * h * h)
    H_si = H * EV / 1e-20                                   # eV/Å^2 -> J/m^2
    lam = np.linalg.eigvalsh(H_si) / (PB_MASS_AMU * sc.atomic_mass)
    return np.sqrt(np.sort(lam))


def pb_dispersion(q, k=PB["k"], D=PB["D"], a=PB["a"]):
    """Analytic phonon branch: m omega^2 = 2 D a^2 + 4 k sin^2(q/2)."""
    k_si, K0_si = k * EV / 1e-20, 2 * D * a ** 2 * EV / 1e-20
    return np.sqrt((K0_si + 4 * k_si * np.sin(np.asarray(q) / 2) ** 2) / (PB_MASS_AMU * sc.atomic_mass))


def pb_transfer_integral(T, y_min=-0.5, y_max=20.0, n=600, k=PB["k"], D=PB["D"], a=PB["a"]):
    """Classical thermodynamics of the PB chain by the transfer-integral method.

    The partition function of a long chain is dominated by the top eigenvector phi0 of the kernel
    K(y, y') = exp(-beta [k/2 (y - y')^2 + V(y)/2 + V(y')/2]). Returns (<y>, <y^2> - <y>^2) in Å, Å^2.
    If <y> keeps growing when the box y_max grows, the pair is unbound: the strands have separated.
    """
    y = np.linspace(y_min, y_max, n)
    beta = 1.0 / (KB_EV * T)
    V = morse(y, D, a)
    K = np.exp(-beta * (0.5 * k * (y[:, None] - y[None, :]) ** 2 + 0.5 * V[:, None] + 0.5 * V[None, :]))
    w, v = np.linalg.eigh(K)
    p = v[:, -1] ** 2
    p /= p.sum()
    mean = float(np.sum(p * y))
    return mean, float(np.sum(p * y * y) - mean ** 2)


def pb_harmonic_variance(T, k=PB["k"], D=PB["D"], a=PB["a"]):
    """Low-temperature check: classical harmonic chain variance kT / sqrt(K0 (K0 + 4k)), K0 = 2 D a^2 (Å^2)."""
    K0 = 2 * D * a ** 2
    return KB_EV * T / np.sqrt(K0 * (K0 + 4 * k))


def pb_denaturation_temperature(T_grid=np.arange(300.0, 701.0, 10.0), rel=0.2):
    """First temperature where <y> depends on the box size (by more than rel): the chain has come unbound."""
    for T in T_grid:
        small = pb_transfer_integral(T, y_max=20.0, n=300)[0]
        big = pb_transfer_integral(T, y_max=40.0, n=600)[0]
        if big > (1 + rel) * small:
            return float(T)
    return None


def pb_continuum_estimate(k=PB["k"], D=PB["D"], a=PB["a"]):
    """Continuum-limit estimate of the unbinding temperature, T_c = 2 sqrt(2 k D) / (a k_B)."""
    return 2.0 * np.sqrt(2.0 * k * D) / (a * KB_EV)


# ---------------------------------------------------------------- 5. screening and absorption in water

def debye_length(ionic_strength_M, T=298.15, eps_r=EPS_STATIC):
    """Debye screening length (m) of a 1:1 electrolyte: sqrt(eps_r eps0 k T / (2 N_A e^2 I))."""
    I = np.asarray(ionic_strength_M, float) * 1e3             # mol/m^3
    return np.sqrt(eps_r * sc.epsilon_0 * sc.k * T / (2.0 * sc.N_A * sc.e ** 2 * I))


def screened_fraction(r_m, ionic_strength_M=0.15):
    """Fraction of a bare charge's potential that survives at distance r in salt water: exp(-r / lambda_D)."""
    return np.exp(-np.asarray(r_m, float) / debye_length(ionic_strength_M))


def water_permittivity(freq_hz, sigma=SIGMA_SALINE, eps_s=EPS_STATIC, eps_inf=EPS_INF, tau=TAU_WATER):
    """Complex relative permittivity of saline: Debye relaxation plus ionic conduction (e^{+i w t} convention)."""
    w = 2.0 * np.pi * np.asarray(freq_hz, float)
    return eps_inf + (eps_s - eps_inf) / (1.0 + 1j * w * tau) - 1j * sigma / (w * sc.epsilon_0)


def field_penetration_depth(freq_hz, **kw):
    """Depth (m) at which a plane wave's field amplitude falls to 1/e: 1 / [(w/c) Im sqrt(eps)]."""
    w = 2.0 * np.pi * np.asarray(freq_hz, float)
    n_complex = np.sqrt(water_permittivity(freq_hz, **kw))
    return 1.0 / (w / sc.c * np.abs(n_complex.imag))


def short_dipole_radiation_resistance(length_m, freq_hz):
    """Free-space radiation resistance of a short dipole, 80 pi^2 (L / lambda)^2 ohms (L << lambda)."""
    return 80.0 * np.pi ** 2 * (length_m * freq_hz / sc.c) ** 2


# ---------------------------------------------------------------- 6. energy scales

def rf_photon_vs_thermal(freq_hz, T=T_BODY):
    """Photon energy h f divided by the thermal energy k T."""
    return sc.h * np.asarray(freq_hz, float) / (sc.k * T)


def main():
    g = b_dna_geometry()
    lo, hi = helical_antenna_band(g["circumference_nm"])
    print("1) If B-DNA were a metal helical antenna")
    print(f"   pitch {g['pitch_nm']:.2f} nm, circumference {g['circumference_nm']:.2f} nm, "
          f"pitch angle {g['pitch_angle_deg']:.0f} deg (Kraus's best helices: 12-14 deg)")
    print(f"   axial-mode band: {lo:.1f}-{hi:.1f} nm  = photons of {photon_energy_ev(hi):.0f}-{photon_energy_ev(lo):.0f} eV "
          f"(extreme UV / soft X-ray)")
    m_lo, m_hi = biophoton_mismatch()
    print(f"   biophoton band 200-800 nm is {m_lo:.0f}x to {m_hi:.0f}x longer than the 'tuned' wavelength")
    hits = photon_hits_per_turn(100.0)
    print(f"   at a generous 100 photons/s/cm^2, one helical turn is hit once every "
          f"{1 / hits / sc.year:.0f} years\n")

    uv = uv_absorption()
    print("2) What DNA really absorbs")
    print(f"   260 nm photons ({uv['photon_energy_ev']:.2f} eV): eps = {uv['eps_per_nt']:.0f} /M/cm per nucleotide in the helix vs "
          f"{uv['eps_free_nt']:.0f} for free nucleotides")
    print(f"   -> hypochromicity {100 * uv['hypochromicity']:.0f}%: stacking couples the bases' excited states\n")

    print("3) FRET along the helix (R0 = 5 nm)")
    for n in (5, 10, 15, 20, 30):
        print(f"   {n:3d} bp apart ({n * RISE_NM:4.1f} nm): efficiency {100 * float(fret_along_dna(n)):5.1f}%")
    print(f"   -> energy hops nanometres, not metres; 50% point at {5.0 / RISE_NM:.0f} bp\n")

    print("4) Peyrard-Bishop base-pair model (k = 0.06 eV/A^2, D = 0.04 eV, a = 4.45 1/A, m = 300 amu)")
    w = pb_mode_frequencies_numeric()
    print(f"   vibrations: {w.min() / (2 * np.pi * sc.c * 100):.0f}-{w.max() / (2 * np.pi * sc.c * 100):.0f} cm^-1 "
          f"({w.min() / (2 * np.pi) / 1e12:.2f}-{w.max() / (2 * np.pi) / 1e12:.2f} THz), analytic "
          f"{pb_dispersion(0) / (2 * np.pi) / 1e12:.2f}-{pb_dispersion(np.pi) / (2 * np.pi) / 1e12:.2f} THz")
    for T in (250, 300, 350, 400):
        mean, var = pb_transfer_integral(T)
        print(f"   T = {T} K: mean base-pair stretch {mean:.2f} A (spread {np.sqrt(var):.2f} A)")
    Td = pb_denaturation_temperature()
    print(f"   strands come apart (unbound) near {Td:.0f} K in this toy parameter set; continuum estimate "
          f"{pb_continuum_estimate():.0f} K\n")

    print("5) Salt water: screening and absorption")
    lam = debye_length(0.15)
    print(f"   Debye length at 150 mM: {lam * 1e9:.2f} nm; a charge's field at 10 nm is x{float(screened_fraction(10e-9)):.0e}")
    for f in (1e9, 10e9, 100e9):
        print(f"   {f / 1e9:5.0f} GHz: field falls to 1/e within {field_penetration_depth(f) * 1e3:7.2f} mm of tissue-like saline")
    L = PERSISTENCE_LENGTH_NM * 1e-9
    print(f"   a stiff {PERSISTENCE_LENGTH_NM:.0f} nm DNA segment as a 1 GHz dipole: radiation resistance "
          f"{short_dipole_radiation_resistance(L, 1e9):.0e} ohm (a working antenna: ~50 ohm)\n")

    print("6) Energy per photon vs thermal jiggling at body temperature")
    for f in (1e9, 1e11):
        print(f"   {f / 1e9:5.0f} GHz photon = {rf_photon_vs_thermal(f):.1e} kT")
    print(f"   260 nm UV photon = {rf_photon_vs_thermal(sc.c / 260e-9):.0f} kT: why UV (not radio) changes DNA chemistry")


if __name__ == "__main__":
    main()
