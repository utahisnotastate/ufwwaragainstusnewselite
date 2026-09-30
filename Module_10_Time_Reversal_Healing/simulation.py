"""
Module 10 lab: what a "time-reversal mirror" really does, and what it cannot do.

Four experiments, each computed from first principles:

1. round_trip()                 Optical phase conjugation: a beam crosses a random phase screen, is
                                phase-conjugated, crosses back, and the aberration cancels. Then the
                                two real limits: the medium must not change between passes, and the
                                mirror must capture the whole field.
2. wavefront_shaping_enhancement()  Focusing through strongly scattering "tissue" (a random transmission
                                matrix) by controlling N modes: the Vellekoop-Mosk (pi/4)(N-1)+1 law.
3. ghk_voltage(), nernst()      Bioelectricity: the resting voltage of a cell from ion concentrations.
4. entropy_budget()             Living bodies lower their own entropy by exporting more to their
                                surroundings; the second law holds overall.

Run:  python simulation.py
"""
import numpy as np
from scipy import constants as sc

R_GAS = sc.R                      # J mol^-1 K^-1 (CODATA 2018, exact)
FARADAY = sc.physical_constants["Faraday constant"][0]   # C/mol
K_B = sc.k                        # J/K
T_BODY = 310.15                   # K, 37 C

# Typical mammalian concentrations (mM) and Hodgkin-Katz-style relative permeabilities.
# Textbook values; real cells vary.
IONS_MAMMALIAN = {
    "K":  {"out": 5.0,   "in": 140.0, "z": +1, "P": 1.00},
    "Na": {"out": 145.0, "in": 15.0,  "z": +1, "P": 0.04},
    "Cl": {"out": 110.0, "in": 10.0,  "z": -1, "P": 0.45},
}


# ---------------------------------------------------------------- 1. phase conjugation

def random_phase_screen(n, rms_rad, corr_px, rng):
    """Gaussian random phase screen: white noise smoothed with a Gaussian kernel, rescaled to rms_rad."""
    noise = rng.standard_normal(n)
    k = np.fft.fftfreq(n)
    smooth = np.fft.ifft(np.fft.fft(noise) * np.exp(-0.5 * (2 * np.pi * k * corr_px) ** 2)).real
    smooth -= smooth.mean()
    return rms_rad * smooth / smooth.std()


def propagate(field, dz, wavelength, dx):
    """Paraxial (Fresnel) free-space propagation by the angular-spectrum method. Unitary and reversible."""
    kx = 2 * np.pi * np.fft.fftfreq(field.size, d=dx)
    k = 2 * np.pi / wavelength
    return np.fft.ifft(np.fft.fft(field) * np.exp(-1j * kx ** 2 * dz / (2 * k)))


def fidelity(target, field):
    """Normalised overlap |<target|field>|^2 / (|target|^2 |field|^2). 1 = perfect copy (up to a global phase)."""
    num = abs(np.vdot(target, field)) ** 2
    return float(num / (np.vdot(target, target).real * np.vdot(field, field).real))


def round_trip(rms_rad=2.0, corr_px=4.0, rho=1.0, aperture=None, conjugate=True,
               n=8192, beam_px=800.0, distance=0.5, wavelength=633e-9, dx=5e-6, seed=0):
    """Send a Gaussian beam through a phase screen, propagate `distance`, reflect, come back through the screen.

    rho       correlation between the screen on the way out and the way back (1 = medium unchanged).
    aperture  half-width (m) of the mirror; None = the mirror captures the whole field.
    conjugate True = phase-conjugate mirror (E -> E*); False = ordinary flat mirror (E -> E).

    Returns (fidelity, captured_fraction). Fidelity is measured against what the same mirror
    returns with no screen and no aperture (the perfect return), so both mirror types are
    compared fairly.
    """
    rng = np.random.default_rng(seed)
    x = (np.arange(n) - n / 2) * dx
    e0 = np.exp(-(x / (beam_px * dx)) ** 2).astype(complex)
    phi1 = random_phase_screen(n, rms_rad, corr_px, rng)
    phi2 = rho * phi1 + np.sqrt(max(0.0, 1.0 - rho ** 2)) * random_phase_screen(n, rms_rad, corr_px, rng)
    mask = np.ones(n) if aperture is None else (np.abs(x) <= aperture).astype(float)
    mirror = np.conj if conjugate else (lambda f: f)

    def trip(s_out, s_back, m):
        at_mirror = propagate(e0 * np.exp(1j * s_out), distance, wavelength, dx)
        reflected = mirror(m * at_mirror)
        return propagate(reflected, distance, wavelength, dx) * np.exp(1j * s_back), at_mirror

    out, at_mirror = trip(phi1, phi2, mask)
    ideal, _ = trip(np.zeros(n), np.zeros(n), np.ones(n))
    captured = float(np.sum(mask * abs(at_mirror) ** 2) / np.sum(abs(at_mirror) ** 2))
    return fidelity(ideal, out), captured


def decorrelation_fidelity_theory(rms_rad, rho):
    """Expected fidelity when the screen changes: |<exp(i dphi)>|^2 = exp(-Var dphi) = exp(-2 s^2 (1 - rho))."""
    return float(np.exp(-2.0 * rms_rad ** 2 * (1.0 - rho)))


# ---------------------------------------------------------------- 2. strongly scattering media

def wavefront_shaping_enhancement(n_modes, trials=200, seed=0, fresh_medium=False):
    """Mean focus enhancement from phase-only shaping of n_modes inputs through a random medium.

    Each input mode reaches the target speckle with a circular-Gaussian complex coefficient t_n
    (fully developed speckle). Setting input phases to -arg(t_n) adds all contributions in phase.
    Enhancement = focused intensity / mean intensity with random input phases.
    If fresh_medium is True the medium is replaced by an uncorrelated one after the phases are
    learned (the tissue moved), and the old correction is applied to the new medium.
    """
    rng = np.random.default_rng(seed)
    t = (rng.standard_normal((trials, n_modes)) + 1j * rng.standard_normal((trials, n_modes))) / np.sqrt(2)
    correction = np.exp(-1j * np.angle(t))
    if fresh_medium:
        t = (rng.standard_normal((trials, n_modes)) + 1j * rng.standard_normal((trials, n_modes))) / np.sqrt(2)
    focused = np.abs(np.sum(t * correction, axis=1)) ** 2
    reference = np.sum(np.abs(t) ** 2, axis=1)       # <|sum t_n e^{i random}|^2> = sum |t_n|^2
    return float(np.mean(focused) / np.mean(reference))


def vellekoop_mosk_theory(n_modes):
    """Expected phase-only enhancement for Rayleigh-distributed amplitudes (Vellekoop & Mosk 2007)."""
    return np.pi / 4 * (n_modes - 1) + 1


def modes_in_area(area_m2, wavelength=800e-9):
    """Number of independent optical modes (speckle grains) over an area: roughly area / (lambda/2)^2."""
    return area_m2 / (wavelength / 2) ** 2


# ---------------------------------------------------------------- 3. bioelectricity

def nernst(c_out, c_in, z=1, temp=T_BODY):
    """Nernst equilibrium potential in volts: (RT/zF) ln(c_out/c_in)."""
    return R_GAS * temp / (z * FARADAY) * np.log(c_out / c_in)


def ghk_voltage(ions=IONS_MAMMALIAN, temp=T_BODY):
    """Goldman-Hodgkin-Katz resting voltage (volts) for monovalent ions.

    Cations contribute P*c_out to the numerator, anions P*c_in (their charge flips the direction).
    """
    num = den = 0.0
    for ion in ions.values():
        if ion["z"] == +1:
            num += ion["P"] * ion["out"]
            den += ion["P"] * ion["in"]
        elif ion["z"] == -1:
            num += ion["P"] * ion["in"]
            den += ion["P"] * ion["out"]
        else:
            raise ValueError("This GHK form handles monovalent ions only.")
    return R_GAS * temp / FARADAY * np.log(num / den)


def with_changes(ions=IONS_MAMMALIAN, **changes):
    """Copy of an ion table with changes, e.g. with_changes(K_out=10.0, Na_P=0.5)."""
    new = {name: dict(v) for name, v in ions.items()}
    for key, value in changes.items():
        name, field = key.split("_")
        new[name][field] = value
    return new


# ---------------------------------------------------------------- 4. entropy

def entropy_budget(power_w=100.0, t_body=T_BODY, t_env=293.15, seconds=86400.0):
    """Entropy flows when a body at t_body dumps metabolic heat into surroundings at t_env.

    Returns entropy (J/K) over `seconds`: leaving the body, arriving in the environment, and the
    net production in the heat flow (always >= 0 when t_body >= t_env).
    """
    q = power_w * seconds
    leaving = q / t_body
    arriving = q / t_env
    return {"heat_J": q, "leaving_body_J_K": leaving, "arriving_env_J_K": arriving,
            "produced_J_K": arriving - leaving}


def landauer_bits_per_second(power_w=100.0, temp=T_BODY):
    """Upper bound on bits erasable per second with this heat budget: P / (k T ln 2)."""
    return power_w / (K_B * temp * np.log(2))


# ---------------------------------------------------------------- report

def main():
    print("1) Optical phase conjugation through a random phase screen (rms 2 rad)")
    f_pcm, cap = round_trip()
    f_flat, _ = round_trip(conjugate=False)
    print(f"   phase-conjugate mirror: fidelity = {f_pcm:.6f}   (captured {cap:.3f} of the field)")
    print(f"   ordinary flat mirror:   fidelity = {f_flat:.4f}")
    print(f"   -> the conjugate mirror returns a {f_pcm / f_flat:.0f}x better copy of the original beam.")
    print()

    print("   (a) Medium changes between passes (rho = correlation of the screen)")
    print("       rho     simulated   theory exp(-2 s^2 (1-rho))")
    for rho in (1.0, 0.99, 0.9, 0.5, 0.0):
        sim = np.mean([round_trip(rho=rho, seed=s)[0] for s in range(4)])
        print(f"       {rho:4.2f}    {sim:8.4f}    {decorrelation_fidelity_theory(2.0, rho):8.4f}")
    print("       (at rho = 0 the simulation sits on a floor ~ 1/(number of screen cells in the beam))")
    print()

    print("   (b) Mirror captures only part of the field")
    print("       half-width     captured    fidelity")
    worst = 0.0
    for a in (5e-3, 2e-3, 1e-3, 5e-4, 2e-4):
        f, c = round_trip(aperture=a)
        worst = max(worst, abs(f - c))
        print(f"       {a * 1e3:5.1f} mm      {c:8.4f}    {f:8.4f}")
    print(f"       -> fidelity = captured fraction (largest difference {worst:.1e}): what the mirror misses is lost.")
    print()

    print("2) Focusing through strongly scattering 'tissue' by shaping N input modes")
    print("       N        simulated    (pi/4)(N-1)+1    after tissue moves")
    for n in (16, 64, 256, 1024):
        print(f"   {n:6d}    {wavefront_shaping_enhancement(n):10.1f}    {vellekoop_mosk_theory(n):10.1f}"
              f"    {wavefront_shaping_enhancement(n, fresh_medium=True):10.2f}")
    moved = wavefront_shaping_enhancement(1024, fresh_medium=True)
    print(f"   If the tissue rearranges, the learned 1024-mode correction gives {moved:.2f}x: plain speckle again.")
    print(f"   Modes to control over just 1 cm^2 at 800 nm: {modes_in_area(1e-4):.1e}.")
    print("   These techniques focus light; they do not reverse the state of cells.")
    print()

    print("3) Bioelectricity: the resting voltage of a typical mammalian cell at 37 C")
    for name, ion in IONS_MAMMALIAN.items():
        e = nernst(ion["out"], ion["in"], ion["z"]) * 1e3
        print(f"   Nernst {name:2s}: {e:7.1f} mV   ([out] {ion['out']:5.1f} mM, [in] {ion['in']:5.1f} mM)")
    print(f"   GHK resting voltage: {ghk_voltage() * 1e3:.1f} mV")
    print(f"   Raise [K]out 5 -> 10 mM (hyperkalemia): {ghk_voltage(with_changes(K_out=10.0)) * 1e3:.1f} mV")
    print(f"   Open Na channels (P_Na 0.04 -> 20):     {ghk_voltage(with_changes(Na_P=20.0)) * 1e3:+.1f} mV"
          "  (near the action-potential peak)")
    print()

    print("4) Entropy budget of a resting human (100 W, body 37 C, room 20 C), per day")
    b = entropy_budget()
    print(f"   heat released:          {b['heat_J']:.2e} J")
    print(f"   entropy leaving body:   {b['leaving_body_J_K']:.0f} J/K")
    print(f"   entropy reaching room:  {b['arriving_env_J_K']:.0f} J/K")
    verdict = "holds" if b["produced_J_K"] > 0 else "is VIOLATED"
    print(f"   net entropy produced:   {b['produced_J_K']:+.0f} J/K  (the second law {verdict} overall)")
    print(f"   Landauer bound: 100 W could pay for erasing up to {landauer_bits_per_second():.1e} bits/s.")
    print("   Energy is not the obstacle to repair. Knowing and steering every molecule is.")


if __name__ == "__main__":
    main()
