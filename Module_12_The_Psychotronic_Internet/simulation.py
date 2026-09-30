"""
Module 12 lab: what can carry a thought from one head to another?

Six experiments, each computed from first principles:

1. skin_depth(), attenuation_length()   Conductors (seawater, copper, a Faraday cage) block changing fields.
2. conducting_sphere_field()            Conductors also block *static* fields: numerically add up the field of
                                        the induced surface charge and watch it cancel the outside field.
3. antiparallel_pair_power()            "Scalar wave" coils: two opposite currents cancel, and what little
                                        is left radiates as an ordinary (quadrupole) wave, not a new kind.
4. aharonov_bohm_phase()                The real, tested case where potentials matter.
5. light_delay(), bob_state()           Nothing carries a message faster than light, not even entanglement.
6. brain_field(), transfer_time()       How weak brain fields are, and how slow human "bandwidth" is.

Run:  python simulation.py
"""
import numpy as np
from scipy import constants as sc
from scipy.integrate import quad

MU0 = sc.mu_0
EPS0 = sc.epsilon_0
C = sc.c
H = sc.h
E_CHARGE = sc.e
FLUX_QUANTUM = H / E_CHARGE           # h/e, the Aharonov-Bohm period (Wb)

SIGMA_SEAWATER = 4.0                  # S/m, typical
EPS_R_WATER = 80.0                    # static relative permittivity (a simplification at GHz)
SIGMA_COPPER = 5.96e7                 # S/m at 20 C

LIGHT_YEAR = sc.light_year
DISTANCES_M = {
    "Earth-Moon (mean)": 384_400e3,
    "Earth-Mars (closest possible)": 54.6e9,
    "Earth-Mars (farthest)": 401e9,
    "Proxima Centauri": 4.2465 * LIGHT_YEAR,
}

SPEECH_BITS_S = 39.0                  # Coupe et al. (2019), average across 17 languages
BCI_CHARS_PER_MIN = 90.0              # Willett et al. (2021), handwriting BCI
ENGLISH_BITS_PER_CHAR = 1.0           # Shannon (1951) estimate, roughly 0.6-1.3
MEG_FIELD_T = 1e-12                   # ~pT: strong brain rhythms at MEG sensors
MEG_SOURCE_DISTANCE_M = 0.04          # sources sit a few cm below the sensors
EARTH_FIELD_T = 50e-6


# ---------------------------------------------------------------- 1. skin depth

def skin_depth(freq_hz, sigma, mu_r=1.0):
    """Good-conductor skin depth delta = sqrt(2 / (mu sigma omega)) in metres."""
    return np.sqrt(2.0 / (mu_r * MU0 * sigma * 2.0 * np.pi * freq_hz))


def attenuation_length(freq_hz, sigma, eps_r=EPS_R_WATER, mu_r=1.0):
    """1/alpha for a plane wave in a lossy medium, valid whether or not sigma >> omega*eps.

    alpha = omega sqrt(mu eps / 2) * sqrt( sqrt(1 + (sigma/(omega eps))^2) - 1 ).
    Reduces to skin_depth() when sigma >> omega*eps.
    """
    w = 2.0 * np.pi * freq_hz
    eps, mu = eps_r * EPS0, mu_r * MU0
    loss = sigma / (w * eps)
    # sqrt(1+x^2)-1 written as x^2/(sqrt(1+x^2)+1) to avoid cancellation for small x
    alpha = w * np.sqrt(mu * eps / 2.0) * np.sqrt(loss ** 2 / (np.sqrt(1.0 + loss ** 2) + 1.0))
    return 1.0 / alpha


def shield_absorption_db(thickness_m, freq_hz, sigma=SIGMA_COPPER):
    """Absorption loss of a conducting sheet: 20 log10(e^(t/delta)) = 8.686 t/delta dB."""
    return 20.0 * np.log10(np.e) * thickness_m / skin_depth(freq_hz, sigma)


# ---------------------------------------------------------------- 2. static screening

def conducting_sphere_field(points, e0=1.0, radius=1.0, n=600):
    """Total field at `points` (N x 3) for a conducting sphere in a uniform field e0 along z.

    The external field induces surface charge sigma = 3 eps0 e0 cos(theta) (the known solution).
    Here we do NOT use the known interior answer: we numerically sum Coulomb's law over that
    charge (midpoint rule on theta, phi) and add the external field.
    """
    th = (np.arange(n) + 0.5) * np.pi / n
    ph = (np.arange(2 * n) + 0.5) * np.pi / n
    th, ph = np.meshgrid(th, ph, indexing="ij")
    src = radius * np.stack([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)], axis=-1).reshape(-1, 3)
    dq = (3.0 * EPS0 * e0 * np.cos(th) * radius ** 2 * np.sin(th) * (np.pi / n) ** 2).reshape(-1)
    out = []
    for p in np.atleast_2d(points):
        d = p - src
        r3 = np.linalg.norm(d, axis=1) ** 3
        e = (dq[:, None] * d / r3[:, None]).sum(axis=0) / (4.0 * np.pi * EPS0)
        out.append(e + np.array([0.0, 0.0, e0]))
    return np.array(out)


def sphere_field_outside_theory(point, e0=1.0, radius=1.0):
    """Analytic outside field: uniform field plus a dipole p = 4 pi eps0 R^3 e0."""
    r = np.linalg.norm(point)
    rhat = point / r
    pz = np.array([0.0, 0.0, radius ** 3 * e0])
    return np.array([0.0, 0.0, e0]) + (3.0 * rhat * np.dot(pz, rhat) - pz) / r ** 3


# ---------------------------------------------------------------- 3. counter-wound coils

def antiparallel_pair_power(kd, n_theta=4001):
    """Radiated power of two opposite magnetic dipoles on the z axis, separated by d, relative to ONE dipole.

    Far-field amplitude of a z-directed dipole ~ sin(theta). Each dipole's field carries the phase
    exp(-i k z_i cos theta). Sum the two with opposite signs and integrate |sum|^2 over the sphere.
    """
    th = np.linspace(0.0, np.pi, n_theta)
    single = np.sin(th)
    pair = np.sin(th) * (np.exp(-1j * kd / 2 * np.cos(th)) - np.exp(1j * kd / 2 * np.cos(th)))
    w = np.sin(th)
    return float(np.trapezoid(np.abs(pair) ** 2 * w, th) / np.trapezoid(np.abs(single) ** 2 * w, th))


def antiparallel_pair_power_theory(kd):
    """Closed form of the same integral: 2 - 6 (sin x - x cos x)/x^3, which is x^2/5 for small x."""
    x = np.asarray(kd, dtype=float)
    return 2.0 - 6.0 * (np.sin(x) - x * np.cos(x)) / x ** 3


def loop_axis_field(z, current=1.0, radius=0.05, z0=0.0):
    """Exact on-axis B (tesla) of a circular loop at height z0: mu0 I R^2 / (2 (R^2 + (z-z0)^2)^(3/2))."""
    return MU0 * current * radius ** 2 / (2.0 * (radius ** 2 + (z - z0) ** 2) ** 1.5)


def falloff_exponent(field_fn, z1=10.0, z2=100.0):
    """Slope of log|B| vs log z between z1 and z2."""
    return float(np.log(abs(field_fn(z2)) / abs(field_fn(z1))) / np.log(z2 / z1))


def counterwound_axis_field(z, current=1.0, radius=0.05, gap=0.01):
    """Two loops with opposite currents, `gap` apart: the fields nearly cancel."""
    return loop_axis_field(z, current, radius, +gap / 2) - loop_axis_field(z, current, radius, -gap / 2)


# ---------------------------------------------------------------- 4. Aharonov-Bohm

def aharonov_bohm_phase(flux_wb):
    """Phase shift (rad) between paths enclosing magnetic flux Phi: e Phi / hbar = 2 pi Phi/(h/e)."""
    return 2.0 * np.pi * flux_wb / FLUX_QUANTUM


# ---------------------------------------------------------------- 5. speed limit and entanglement

def light_delay(distance_m):
    """One-way light travel time in seconds."""
    return distance_m / C


def _projector(angle, outcome):
    """Projector onto spin up/down along an axis at `angle` in the x-z plane."""
    v = np.array([np.cos(angle / 2), np.sin(angle / 2)]) if outcome == 0 else \
        np.array([-np.sin(angle / 2), np.cos(angle / 2)])
    return np.outer(v, v.conj())


BELL = np.array([1.0, 0.0, 0.0, 1.0]) / np.sqrt(2.0)   # (|00> + |11>)/sqrt 2
RHO_BELL = np.outer(BELL, BELL.conj())


def bob_state(alice_angle=None, rho=RHO_BELL):
    """Bob's density matrix after Alice measures at alice_angle (None = she does nothing).

    Bob does not learn Alice's result, so average over it: rho_B = Tr_A sum_k (P_k x 1) rho (P_k x 1).
    """
    if alice_angle is not None:
        ops = [np.kron(_projector(alice_angle, k), np.eye(2)) for k in (0, 1)]
        rho = sum(o @ rho @ o for o in ops)
    return np.trace(rho.reshape(2, 2, 2, 2), axis1=0, axis2=2)


def same_outcome_probability(alice_angle, bob_angle, rho=RHO_BELL):
    """P(Alice and Bob get the same result): the correlations ARE there, only no message is."""
    return float(sum(np.trace(np.kron(_projector(alice_angle, k), _projector(bob_angle, k)) @ rho).real
                     for k in (0, 1)))


# ---------------------------------------------------------------- 6. brains and bandwidth

def brain_field(distance_m):
    """Rough dipole falloff of a ~pT brain field measured ~4 cm from its source: B ~ 1/r^3."""
    return MEG_FIELD_T * (MEG_SOURCE_DISTANCE_M / distance_m) ** 3


def bci_bits_per_second(chars_per_min=BCI_CHARS_PER_MIN, bits_per_char=ENGLISH_BITS_PER_CHAR):
    """Information rate of a character-output interface."""
    return chars_per_min / 60.0 * bits_per_char


def transfer_time(n_bytes, bits_per_second):
    """Seconds to move n_bytes at a given rate."""
    return 8.0 * n_bytes / bits_per_second


# ---------------------------------------------------------------- report

def main():
    print("1) How deep fields reach into conductors")
    print("   medium       frequency     good-conductor delta    full formula 1/alpha")
    for f in (76.0, 3e3, 1e6, 2.4e9):
        print(f"   seawater   {f:10.3g} Hz   {skin_depth(f, SIGMA_SEAWATER):12.4g} m"
              f"      {attenuation_length(f, SIGMA_SEAWATER):12.4g} m")
    for f in (50.0, 1e6):
        print(f"   copper     {f:10.3g} Hz   {skin_depth(f, SIGMA_COPPER) * 1e3:12.4g} mm")
    print(f"   1 mm copper sheet absorbs {shield_absorption_db(1e-3, 1e6):.0f} dB at 1 MHz and "
          f"{shield_absorption_db(1e-3, 50.0):.2f} dB at 50 Hz")
    ratio = 2.4e9 * 2 * np.pi * EPS_R_WATER * EPS0 / SIGMA_SEAWATER
    print(f"   (at 2.4 GHz, omega*eps/sigma = {ratio:.1f}, so the good-conductor formula no longer applies)")
    print()

    print("2) A static field and a conducting sphere (field of the induced charge summed numerically)")
    inside = np.array([[0, 0, 0], [0.3, 0.2, -0.5], [0, 0, 0.8]], dtype=float)
    for p, e in zip(inside, conducting_sphere_field(inside)):
        print(f"   inside  at {p}:  |E|/E0 = {np.linalg.norm(e):.1e}")
    p_out = np.array([0.0, 0.0, 2.0])
    print(f"   outside at {p_out}: E_z/E0 = {conducting_sphere_field(p_out)[0, 2]:.4f}"
          f"   (theory {sphere_field_outside_theory(p_out)[2]:.4f})")
    print()

    print("3) Counter-wound coils: do opposite currents emit a new 'scalar' wave?")
    single = falloff_exponent(loop_axis_field)
    pair = falloff_exponent(counterwound_axis_field)
    print(f"   near field on axis falls as z^{single:.2f} for one loop, z^{pair:.2f} for the counter-wound pair")
    print("   radiated power of the pair relative to one coil:")
    for kd in (1e-3, 1e-2, 0.1, 1.0, 10.0):
        print(f"      k*d = {kd:6g}:  {antiparallel_pair_power(kd):.3e}   (theory {antiparallel_pair_power_theory(kd):.3e})")
    print(f"   perfect overlap (d = 0): {antiparallel_pair_power(0.0):.1e} -> no field and no wave of any kind")
    print()

    print("4) Aharonov-Bohm: potentials matter only through the flux they enclose")
    print(f"   flux quantum h/e = {FLUX_QUANTUM:.4e} Wb")
    for phi in (FLUX_QUANTUM / 2, FLUX_QUANTUM):
        print(f"   enclosed flux {phi:.3e} Wb -> phase {aharonov_bohm_phase(phi) / np.pi:.2f} pi")
    print()

    print("5) The speed limit")
    for name, d in DISTANCES_M.items():
        t = light_delay(d)
        unit = (t, "s") if t < 120 else (t / 60, "min") if t < 7200 else (t / sc.Julian_year, "years")
        print(f"   {name:31s} {unit[0]:8.3g} {unit[1]}")
    diffs = [np.abs(bob_state(a) - bob_state(None)).max() for a in np.linspace(0, 2 * np.pi, 13)]
    print(f"   Entanglement: Bob's state changes by at most {max(diffs):.1e} whatever Alice does,")
    print(f"   although their results agree {same_outcome_probability(0.0, 0.0):.2f} of the time at equal angles"
          f" and {same_outcome_probability(0.0, np.pi / 2):.2f} at 90 degrees.")
    print()

    print("6) Brains and bandwidth")
    for r in (0.04, 1.0, 10.0, 1000.0):
        print(f"   brain magnetic field at {r:7.2f} m: {brain_field(r):.1e} T"
              f"   ({brain_field(r) / EARTH_FIELD_T:.0e} of Earth's field)")
    bci_lo, bci_hi = bci_bits_per_second(), bci_bits_per_second(bits_per_char=np.log2(27))
    print(f"   speech ~{SPEECH_BITS_S:.0f} bit/s; handwriting BCI ~{bci_lo:.1f}-{bci_hi:.1f} bit/s"
          " (1 bit/char English entropy to log2(27) bits/char raw alphabet)")
    print(f"   gigabit fibre 1e9 bit/s = {1e9 / SPEECH_BITS_S:.0e}x speech")
    t = transfer_time(1e6, SPEECH_BITS_S)
    print(f"   a 1 MB manual at speech rate: {t / 3600:.0f} hours; in 5 s it would need"
          f" {8e6 / 5:.1e} bit/s ({8e6 / 5 / SPEECH_BITS_S:.0e}x speech)")


if __name__ == "__main__":
    main()
