"""
Module 01 lab: the "Vacuum Ocean", measured honestly.

Four experiments, each computed from first principles:

1. casimir_pressure_ideal()   Casimir's 1948 result for perfect mirrors: the vacuum really does push.
2. lifshitz_pressure()        The same force for real gold plates (Lifshitz theory, Drude model), by
                              numerical integration over imaginary frequency and wavevector.
3. closed_cycle_work()        Can a Casimir cavity run an engine? Push the plates together, pull them
                              apart, and add up the work around the loop.
4. cosmological_constant_gap() The "10^95 g/cm^3" vacuum: what the naive estimate predicts versus the
                              vacuum energy that gravity actually sees.

Run:  python simulation.py
"""
import numpy as np
from scipy import constants as sc

HBAR = sc.hbar                      # J s   (CODATA, via scipy.constants)
C = sc.c                            # m/s
G = sc.G                            # m^3 kg^-1 s^-2
EV = sc.electron_volt               # J

# Gold, Drude model on the imaginary axis (values used by Lambrecht & Reynaud, Eur. Phys. J. D 8, 309 (2000))
GOLD_PLASMA_EV = 9.0                # hbar * omega_p
GOLD_DAMPING_EV = 0.035             # hbar * gamma

# Observed dark energy, Planck 2018 (Planck Collaboration, A&A 641, A6 (2020))
H0_KM_S_MPC = 67.4
OMEGA_LAMBDA = 0.685
MPC = 3.0856775814913673e22         # m
AA_BATTERY_J = 1.0e4                # alkaline AA cell: ~2.5 Ah at 1.5 V is ~1.3e4 J; order of magnitude

# Fixed Gauss-Legendre grids for the Lifshitz integral (dimensionless y = 2*kappa*d, t = xi/(c*kappa))
_Y_MAX = 60.0


def _gauss(n, a, b):
    x, w = np.polynomial.legendre.leggauss(n)
    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w


def casimir_pressure_ideal(d):
    """Casimir pressure between perfect mirrors, P = -pi^2 hbar c / (240 d^4) (Pa, negative = attractive)."""
    d = np.asarray(d, dtype=float)
    return -np.pi ** 2 * HBAR * C / (240.0 * d ** 4)


def casimir_energy_ideal(d):
    """Casimir energy per unit area between perfect mirrors, E/A = -pi^2 hbar c / (720 d^3) (J/m^2)."""
    d = np.asarray(d, dtype=float)
    return -np.pi ** 2 * HBAR * C / (720.0 * d ** 3)


def drude_epsilon(xi, plasma_ev=GOLD_PLASMA_EV, damping_ev=GOLD_DAMPING_EV):
    """Drude permittivity at imaginary frequency i*xi (xi in rad/s): 1 + wp^2 / (xi (xi + gamma))."""
    wp = plasma_ev * EV / HBAR
    gamma = damping_ev * EV / HBAR
    return 1.0 + wp ** 2 / (xi * (xi + gamma))


def _reflection_squares(d, y, t, material):
    """r_TE^2 and r_TM^2 on the (y, t) grid. material = 'ideal' or a permittivity function eps(xi)."""
    if material == "ideal":
        one = np.ones(np.broadcast(y, t).shape)
        return one, one
    xi = C * y * t / (2.0 * d)                      # imaginary frequency, rad/s
    eps = material(xi)
    s = np.sqrt(1.0 + (eps - 1.0) * t ** 2)        # K / kappa inside the metal
    r_te = (1.0 - s) / (1.0 + s)
    r_tm = (eps - s) / (eps + s)
    return r_te ** 2, r_tm ** 2


def _lifshitz(d, material, kind, n_y, n_t):
    """Lifshitz formula at T = 0 for two identical half-spaces across a vacuum gap d.

    With kappa^2 = k^2 + xi^2/c^2, substitute y = 2 kappa d and t = xi / (c kappa):
      E/A = hbar c / (32 pi^2 d^3) * int y^2 dy int dt  sum_pol ln(1 - r^2 e^-y)
      P   = -hbar c / (32 pi^2 d^4) * int y^3 dy int dt  sum_pol r^2 e^-y / (1 - r^2 e^-y)
    For r = 1 these reduce exactly to Casimir's closed forms, which the tests check.
    """
    y, wy = _gauss(n_y, 0.0, _Y_MAX)
    t, wt = _gauss(n_t, 0.0, 1.0)
    Y, T = np.meshgrid(y, t, indexing="ij")
    W = np.outer(wy, wt)
    ey = np.exp(-Y)
    total = 0.0
    for r2 in _reflection_squares(d, Y, T, material):
        if kind == "energy":
            total += np.sum(W * Y ** 2 * np.log1p(-r2 * ey))
        else:
            total += np.sum(W * Y ** 3 * r2 * ey / (1.0 - r2 * ey))
    if kind == "energy":
        return HBAR * C / (32.0 * np.pi ** 2 * d ** 3) * total
    return -HBAR * C / (32.0 * np.pi ** 2 * d ** 4) * total


def lifshitz_pressure(d, material=drude_epsilon, n_y=160, n_t=100):
    """Casimir pressure (Pa) between two half-spaces of `material` ('ideal' or eps(xi)) at separation d (m)."""
    return float(_lifshitz(float(d), material, "pressure", n_y, n_t))


def lifshitz_energy(d, material=drude_epsilon, n_y=160, n_t=100):
    """Casimir energy per unit area (J/m^2) from the Lifshitz formula."""
    return float(_lifshitz(float(d), material, "energy", n_y, n_t))


def gold_reduction_factor(d):
    """Real-gold pressure divided by the perfect-mirror pressure at the same separation (0 < ratio < 1)."""
    return lifshitz_pressure(d) / float(casimir_pressure_ideal(d))


def hamaker_constant(material=drude_epsilon, n_terms=50):
    """Non-retarded Hamaker constant (J) of two half-spaces, an independent 1-D check of the short-range limit.

    A = (3 hbar / 4 pi) int_0^inf dxi sum_n Delta(i xi)^(2n) / n^3,  Delta = (eps - 1)/(eps + 1),
    and at separations far below the plasma wavelength E/A -> -A / (12 pi d^2).
    """
    from scipy.integrate import quad
    n = np.arange(1, n_terms + 1, dtype=float)
    wp = GOLD_PLASMA_EV * EV / HBAR        # integrate in x = xi / wp so the quadrature sees O(1) numbers

    def integrand(x):
        eps = material(x * wp)
        delta2 = ((eps - 1.0) / (eps + 1.0)) ** 2
        return float(np.sum(delta2 ** n / n ** 3))

    val, _ = quad(integrand, 0.0, np.inf, limit=200)
    return 3.0 * HBAR * wp / (4.0 * np.pi) * val


def closed_cycle_work(pressure_fn, d_far, d_near, n_in=201, n_out=301, area=1.0):
    """Work done BY the Casimir force on one plate over a closed cycle far -> near -> far (J).

    The two strokes are sampled on different grids (so the zero is not built in by symmetry) and
    integrated with Simpson's rule. Returns (work_in, work_out, net).
    """
    from scipy.integrate import simpson
    d_in = np.geomspace(d_far, d_near, n_in)
    d_out = np.linspace(d_near, d_far, n_out)
    f_in = np.array([pressure_fn(x) for x in d_in]) * area
    f_out = np.array([pressure_fn(x) for x in d_out]) * area
    w_in = simpson(f_in, x=d_in)       # force < 0 and d decreasing: positive work extracted
    w_out = simpson(f_out, x=d_out)    # pulling apart against the force: negative (work paid in)
    return float(w_in), float(w_out), float(w_in + w_out)


def one_shot_energy(d_start, d_end, area=1.0):
    """Maximum energy (J) a single collapse from d_start to d_end can give (perfect mirrors, the upper bound)."""
    return float(area * (casimir_energy_ideal(d_start) - casimir_energy_ideal(d_end)))


def planck_density():
    """Planck mass density c^5 / (hbar G^2) in kg/m^3: the scale behind the '10^95 g/cm^3' vacuum."""
    return C ** 5 / (HBAR * G ** 2)


def naive_vacuum_energy_density(k_max=None):
    """Zero-point energy density of one massless field cut off at k_max (default: 1 / Planck length), J/m^3.

    Summing hbar*omega/2 over modes: u = int d^3k/(2 pi)^3 * hbar c k / 2 = hbar c k_max^4 / (16 pi^2).
    """
    if k_max is None:
        k_max = 1.0 / np.sqrt(HBAR * G / C ** 3)
    return HBAR * C * k_max ** 4 / (16.0 * np.pi ** 2)


def observed_dark_energy_density(h0_km_s_mpc=H0_KM_S_MPC, omega_lambda=OMEGA_LAMBDA):
    """Dark-energy density Omega_Lambda * rho_crit * c^2 in J/m^3, rho_crit = 3 H0^2 / (8 pi G)."""
    h0 = h0_km_s_mpc * 1e3 / MPC
    return omega_lambda * 3.0 * h0 ** 2 / (8.0 * np.pi * G) * C ** 2


def cosmological_constant_gap():
    """log10 of (naive vacuum energy) / (observed dark energy): the 'worst prediction in physics'."""
    return float(np.log10(naive_vacuum_energy_density() / observed_dark_energy_density()))


def main():
    print("1) The vacuum really does push: Casimir pressure between perfect mirrors")
    for d in (1e-6, 1e-7, 1e-8):
        print(f"   d = {d * 1e9:7.1f} nm   P = {float(casimir_pressure_ideal(d)):11.3e} Pa   "
              f"E/A = {float(casimir_energy_ideal(d)):11.3e} J/m^2")
    atm = sc.atm
    d_atm = (np.pi ** 2 * HBAR * C / (240.0 * atm)) ** 0.25
    print(f"   The pull reaches one atmosphere only at d = {d_atm * 1e9:.1f} nm.\n")

    print("2) Real gold plates (Lifshitz theory, Drude model, T = 0)")
    print("   d          P_gold (Pa)    P_ideal (Pa)   gold/ideal")
    for d in (1e-8, 1e-7, 3e-7, 1e-6, 3e-6, 1e-5):
        pg, pi_ = lifshitz_pressure(d), float(casimir_pressure_ideal(d))
        print(f"   {d * 1e9:7.0f} nm  {pg:11.3e}   {pi_:11.3e}   {pg / pi_:8.3f}")
    print("   Real metals stop reflecting above their plasma frequency, so the force is weaker at short range.")
    d0 = 2e-10
    print(f"   Short-range check: -12 pi d^2 E/A at {d0 * 1e9:.1f} nm = {-12 * np.pi * d0 ** 2 * lifshitz_energy(d0):.3e} J, "
          f"independent Hamaker integral = {hamaker_constant():.3e} J\n")

    print("3) Can the Vacuum Ocean run an engine?  Closed cycle 1 um -> 100 nm -> 1 um, 1 m^2 plates")
    for name, fn in (("perfect mirrors", lambda x: float(casimir_pressure_ideal(x))), ("gold", lifshitz_pressure)):
        w_in, w_out, net = closed_cycle_work(fn, 1e-6, 1e-7)
        print(f"   {name:15s}  gained moving in = {w_in:10.4e} J   paid moving out = {w_out:11.4e} J   "
              f"net = {net:10.2e} J  ({abs(net) / w_in:.1e} of one stroke)")
    e_once = one_shot_energy(1e-6, 1e-8)
    print(f"   Letting 1 m^2 of perfect mirrors collapse once from 1 um to 10 nm yields at most {e_once:.2e} J.")
    print(f"   An AA battery stores about {AA_BATTERY_J:.0e} J, i.e. {AA_BATTERY_J / e_once:.1e} such one-way collapses, "
          "and each must be reset by paying the energy back.\n")

    print("4) How big is the 'ocean'?  Naive zero-point estimate versus what gravity measures")
    rho_p = planck_density()
    print(f"   Planck density c^5/(hbar G^2)          = {rho_p:.2e} kg/m^3 = {rho_p * 1e-3:.1e} g/cm^3")
    print(f"   Naive vacuum energy, Planck cutoff      = {naive_vacuum_energy_density():.2e} J/m^3")
    print(f"   Observed dark-energy density (Planck)   = {observed_dark_energy_density():.2e} J/m^3")
    print(f"   Mismatch: 10^{cosmological_constant_gap():.0f}.  Whatever the vacuum holds, gravity does not see an ocean.")


if __name__ == "__main__":
    main()
