"""
Module 08 lab: "instant travel" checked against general relativity and quantum field theory.

Experiments, each computed rather than asserted:

1. The Alcubierre warp bubble (Alcubierre 1994), in geometrized units G = c = 1:
   shape function f(r), York expansion theta (space shrinks ahead, grows behind) and the
   Eulerian energy density T00, which is negative everywhere it is non-zero.
2. total_energy()            Numerical integral of T00 over all space and its thin-wall scaling E ~ -v^2 R^2 sigma / 36.
3. max_wall_thickness_qi()   The Ford-Roman quantum inequality forces the bubble wall down to ~Planck-length
                             thickness, which makes the total negative energy astronomically large.
4. casimir_energy_density()  The best laboratory negative energy (Casimir plates) compared with what a bubble needs.
5. order_reversal_factor()   Faster-than-light signals + relativity of simultaneity = cause and effect can swap.
6. de_broglie_velocities()   The "superluminal matter wave" argument: phase velocity > c, but it carries nothing.

Run:  python simulation.py
"""
import numpy as np
from scipy import constants as sc
from scipy.integrate import quad
from scipy.optimize import brentq

C = sc.c                                   # m/s (exact)
G = sc.G                                   # m^3 kg^-1 s^-2 (CODATA, via scipy)
HBAR = sc.hbar                             # J s
L_PLANCK = np.sqrt(HBAR * G / C ** 3)      # m, ~1.6e-35
J_PER_GEOM_METRE = C ** 4 / G              # converts a geometrized energy (metres) to joules
KG_PER_GEOM_METRE = C ** 2 / G             # converts a geometrized mass (metres) to kilograms
M_SUN = 1.98847e30                         # kg (IAU 2015 nominal G*M_sun divided by CODATA G)
M_JUPITER = 1.89813e27                     # kg
MARS_DISTANCE_M = (5.46e10, 4.01e11)       # closest and farthest Earth-Mars distance, m (approximate)


# ---------------------------------------------------------------- 1. Alcubierre geometry (G = c = 1)

def _sech2(x):
    """sech^2(x) computed without overflow for huge |x|."""
    e = np.exp(-2.0 * np.abs(x))
    return 4.0 * e / (1.0 + e) ** 2


def shape_function(r, R, sigma):
    """Alcubierre's top-hat: f = [tanh(sigma(r+R)) - tanh(sigma(r-R))] / (2 tanh(sigma R)). f(0)=1, f(inf)=0."""
    r = np.asarray(r, dtype=float)
    return (np.tanh(sigma * (r + R)) - np.tanh(sigma * (r - R))) / (2.0 * np.tanh(sigma * R))


def shape_derivative(r, R, sigma):
    """df/dr = sigma [sech^2(sigma(r+R)) - sech^2(sigma(r-R))] / (2 tanh(sigma R))."""
    r = np.asarray(r, dtype=float)
    return sigma * (_sech2(sigma * (r + R)) - _sech2(sigma * (r - R))) / (2.0 * np.tanh(sigma * R))


def wall_thickness(R, sigma):
    """Linear-extrapolation wall thickness 1/|f'(R)|. Tends to 2/sigma for a thin wall (sigma R >> 1)."""
    return 1.0 / abs(float(shape_derivative(R, R, sigma)))


def _bubble_radius(x, y, z, x_s):
    return np.sqrt((np.asarray(x, dtype=float) - x_s) ** 2 + np.asarray(y, dtype=float) ** 2
                   + np.asarray(z, dtype=float) ** 2)


def york_expansion(x, y, z, v_s, R, sigma, x_s=0.0):
    """Expansion of the volume elements of Eulerian observers: theta = v_s (x - x_s)/r_s * df/dr_s.

    theta < 0 (space contracting) ahead of the bubble, theta > 0 (expanding) behind it.
    """
    r_s = _bubble_radius(x, y, z, x_s)
    with np.errstate(invalid="ignore", divide="ignore"):
        th = v_s * (np.asarray(x, dtype=float) - x_s) / r_s * shape_derivative(r_s, R, sigma)
    return np.where(r_s == 0.0, 0.0, th)


def energy_density(x, y, z, v_s, R, sigma, x_s=0.0):
    """Eulerian energy density T00 = -(1/8pi) v_s^2 (y^2+z^2)/(4 r_s^2) (df/dr_s)^2, in geometrized units (1/m^2).

    Multiply by c^4/G (J_PER_GEOM_METRE) to get J/m^3.
    """
    r_s = _bubble_radius(x, y, z, x_s)
    rho2 = np.asarray(y, dtype=float) ** 2 + np.asarray(z, dtype=float) ** 2
    with np.errstate(invalid="ignore", divide="ignore"):
        t00 = -(1.0 / (8.0 * np.pi)) * v_s ** 2 * rho2 / (4.0 * r_s ** 2) * shape_derivative(r_s, R, sigma) ** 2
    return np.where(r_s == 0.0, 0.0, t00)


# ---------------------------------------------------------------- 2. total negative energy

def total_energy(v_s, R, sigma):
    """Integral of T00 over all space (geometrized, metres).

    In spherical coordinates about the bubble centre, (y^2+z^2)/r^2 = sin^2(theta) and the angular
    integral of sin^3(theta) dtheta dphi is 8 pi / 3, leaving E = -(v_s^2/12) * integral r^2 f'(r)^2 dr.
    The radial integral is done numerically.
    """
    w = 1.0 / sigma
    upper = R + 60.0 * w
    lo, hi = max(0.0, R - 60.0 * w), upper
    integrand = lambda r: r ** 2 * float(shape_derivative(r, R, sigma)) ** 2
    inner = quad(integrand, 0.0, lo, limit=200)[0] if lo > 0 else 0.0
    wall = quad(integrand, lo, hi, points=[R], limit=400)[0]
    return -(v_s ** 2 / 12.0) * (inner + wall)


def total_energy_thin_wall(v_s, R, sigma):
    """Thin-wall limit of total_energy: f' ~ -(sigma/2) sech^2(sigma(r-R)) and the integral of sech^4 is 4/(3 sigma),
    so the radial integral is ~ R^2 sigma / 3 and E ~ -v_s^2 R^2 sigma / 36 (geometrized metres)."""
    return -v_s ** 2 * R ** 2 * sigma / 36.0


# ---------------------------------------------------------------- 3. quantum inequality

def qi_bound(t0):
    """Ford-Roman quantum inequality, massless scalar field, 4-D Minkowski, Lorentzian sampling time t0 (s).

    <rho> >= -3 hbar / (32 pi^2 c^3 t0^4)   [J/m^3]
    The -3/(32 pi^2) constant is the value for this field and sampling function; other fields and
    sampling functions change the O(1) constant, not the t0^-4 scaling.
    """
    return -3.0 * HBAR / (32.0 * np.pi ** 2 * C ** 3 * np.asarray(t0, dtype=float) ** 4)


def peak_negative_energy_density_SI(v_s, R, delta):
    """Most negative T00 of a thin-walled bubble (on the wall, perpendicular to the motion), in J/m^3."""
    sigma = 2.0 / delta
    t00 = energy_density(0.0, R, 0.0, v_s, R, sigma)   # point at r_s = R, rho = R
    return float(t00) * J_PER_GEOM_METRE


def max_wall_thickness_qi(v_s, R=100.0, sampling_fraction=0.1):
    """Largest wall thickness (m) allowed if the peak negative energy density must obey the quantum inequality
    sampled over t0 = sampling_fraction * delta / c (the sampling time must be short compared with the
    curvature scale for the flat-space bound to apply, as in Pfenning & Ford 1997).

    Found by root-finding; the closed form it should reproduce is delta = sqrt(3/pi) L_P / (beta^2 v_s).
    """
    def mismatch(log_delta):
        d = np.exp(log_delta)
        return np.log(-peak_negative_energy_density_SI(v_s, R, d)) - np.log(-qi_bound(sampling_fraction * d / C))
    return float(np.exp(brentq(mismatch, np.log(1e-40), np.log(1e3), xtol=1e-12)))


def warp_energy_budget(v_s, R, delta):
    """Total (negative) energy of a thin-walled bubble, as joules and as equivalent mass."""
    e_geom = total_energy_thin_wall(v_s, R, 2.0 / delta)
    return {
        "energy_J": e_geom * J_PER_GEOM_METRE,
        "mass_kg": e_geom * KG_PER_GEOM_METRE,
        "solar_masses": e_geom * KG_PER_GEOM_METRE / M_SUN,
        "jupiter_masses": e_geom * KG_PER_GEOM_METRE / M_JUPITER,
    }


# ---------------------------------------------------------------- 4. Casimir comparison

def casimir_energy_density(d):
    """Energy density between ideal parallel plates a distance d apart: -pi^2 hbar c / (720 d^4)  [J/m^3]."""
    return -np.pi ** 2 * HBAR * C / (720.0 * np.asarray(d, dtype=float) ** 4)


def casimir_gap_for(u):
    """Plate separation (m) whose Casimir energy density equals u (u < 0, J/m^3)."""
    return (np.pi ** 2 * HBAR * C / (720.0 * abs(u))) ** 0.25


# ---------------------------------------------------------------- 5. causality

def order_reversal_factor(u, V):
    """dt'/dt for a signal of speed u (m/s) seen from a frame moving at V (m/s): gamma (1 - u V / c^2).

    Negative means the arrival happens *before* the departure in that frame.
    """
    if abs(V) >= C:
        raise ValueError("Observers must move slower than light.")
    gamma = 1.0 / np.sqrt(1.0 - (V / C) ** 2)
    return gamma * (1.0 - u * V / C ** 2)


def reversing_frame_speed(u):
    """Slowest observer speed that sees the signal arrive before it left: c^2/u, or None if u <= c."""
    return C ** 2 / u if u > C else None


# ---------------------------------------------------------------- 6. de Broglie waves

def de_broglie_velocities(m, v):
    """Phase and group velocity of a free particle's matter wave, from omega(k) = sqrt(c^2 k^2 + (m c^2/hbar)^2)."""
    gamma = 1.0 / np.sqrt(1.0 - (v / C) ** 2)
    k = gamma * m * v / HBAR
    omega = np.sqrt((C * k) ** 2 + (m * C ** 2 / HBAR) ** 2)
    return {"wavelength_m": 2.0 * np.pi / k, "phase_velocity": omega / k, "group_velocity": C ** 2 * k / omega}


# ---------------------------------------------------------------- report

def main():
    R, sigma, v = 1.0, 8.0, 1.0
    print("1) Alcubierre bubble, R = 1, sigma = 8, v_s = c  (geometrized units)")
    print(f"   f(0) = {float(shape_function(0.0, R, sigma)):.4f}   f(3R) = {float(shape_function(3.0, R, sigma)):.2e}")
    ahead, behind = float(york_expansion(R, 0, 0, v, R, sigma)), float(york_expansion(-R, 0, 0, v, R, sigma))
    print(f"   York expansion at the front wall = {ahead:+.3f} (space shrinks), rear wall = {behind:+.3f} (space grows)")
    xs, ys = np.meshgrid(np.linspace(-3, 3, 241), np.linspace(-3, 3, 241))
    t00 = energy_density(xs, ys, 0.0, v, R, sigma)
    print(f"   T00 on a 241x241 grid: max = {t00.max():.2e}, min = {t00.min():.3e}"
          f"  -> {'negative everywhere it is non-zero' if t00.max() <= 0 else 'POSITIVE somewhere'}\n")

    print("2) Total energy (numerical integral) vs thin-wall formula -v^2 R^2 sigma / 36")
    for s in (4.0, 16.0, 64.0):
        print(f"   sigma R = {s:5.0f}   numerical = {total_energy(1.0, 1.0, s):+.5f}   "
              f"thin wall = {total_energy_thin_wall(1.0, 1.0, s):+.5f}")
    print("   Thinner walls cost MORE negative energy (E grows like 1/thickness).\n")

    print("3) Quantum inequality -> wall thickness -> total energy, for a 100 m bubble")
    print(f"   Planck length = {L_PLANCK:.3e} m")
    print("   v_s/c   max wall (m)   (Planck lengths)   energy (J)    mass-equivalent (kg)   (solar masses)")
    for vs in (0.1, 1.0, 10.0):
        d = max_wall_thickness_qi(vs, R=100.0)
        b = warp_energy_budget(vs, 100.0, d)
        print(f"   {vs:5.1f}   {d:11.2e}   {d / L_PLANCK:12.0f}      {b['energy_J']:+.2e}   {b['mass_kg']:+.2e}"
              f"            {b['solar_masses']:+.1e}")
    print("   (Ordinary matter in the whole observable universe is of order 1e53 kg.)")
    b1 = warp_energy_budget(1.0, 100.0, 1.0)
    print(f"   Even a generous 1 m wall at v = c needs {b1['jupiter_masses']:+.1f} Jupiter masses of negative energy.\n")

    print("4) Casimir plates vs the bubble")
    for d in (1e-6, 1e-7, 1e-8):
        print(f"   plates {d:.0e} m apart: {float(casimir_energy_density(d)):+.2e} J/m^3")
    need = peak_negative_energy_density_SI(1.0, 100.0, 1.0)
    print(f"   bubble wall (1 m thick, v = c) needs {need:+.2e} J/m^3 "
          f"-> plates {casimir_gap_for(need):.1e} m apart (a proton is ~1.7e-15 m across)\n")

    print("5) Causality: a signal sent at u = 10 c")
    V = reversing_frame_speed(10 * C)
    print(f"   Any observer faster than {V / C:.2f} c sees it arrive before it left; "
          f"at 0.5 c, dt'/dt = {order_reversal_factor(10 * C, 0.5 * C):+.2f}")
    print(f"   Same test for u = 0.99 c: reversing observer speed = {reversing_frame_speed(0.99 * C)}\n")

    print("6) de Broglie waves of an 8-year-old (25 kg) walking at 1 m/s")
    dbw = de_broglie_velocities(25.0, 1.0)
    print(f"   wavelength = {dbw['wavelength_m']:.2e} m, phase velocity = {dbw['phase_velocity']:.2e} m/s,"
          f" group velocity = {dbw['group_velocity']:.3f} m/s")
    print("   The phase outruns light, but the child (and any message) travels at the group velocity.")
    lo, hi = (d / C / 60 for d in MARS_DISTANCE_M)
    print(f"   For comparison, light itself takes {lo:.1f} to {hi:.1f} minutes to reach Mars.")


if __name__ == "__main__":
    main()
