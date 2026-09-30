"""
Module 05 lab: what relativity really says about "time as a map".

Four experiments, each computed from first principles:

1. lorentz_boost(), simultaneity_shift()   Relativity of simultaneity: events that share a "now" in one
                                            frame do not in another. (This is what motivates the block universe.)
2. gps_clock_rates()                        Time dilation you can check every day: GPS satellite clocks vs ground clocks.
3. kerr_metric() and friends                A rotating black hole (Kerr, G = c = M = 1): horizons, the ergosphere,
                                            and the Penrose process that extracts rotational energy.
4. ctc_scan()                               Where the 2420 claim breaks: in Kerr, closed timelike curves appear only
                                            at r < 0, inside the ring singularity, never in the region outside the horizon.

Run:  python simulation.py
"""
import numpy as np
from scipy import constants as sc

C = sc.c                      # m/s (exact)
G = sc.G                      # m^3 kg^-1 s^-2 (CODATA)
GM_EARTH = 3.986004418e14     # m^3/s^2 (WGS84 / IERS geocentric gravitational constant)
R_EARTH_EQ = 6.378137e6       # m, WGS84 equatorial radius
OMEGA_EARTH = 7.2921151467e-5  # rad/s, WGS84 Earth rotation rate
A_GPS = 2.656175e7            # m, nominal GPS orbit semi-major axis (~20,200 km altitude)
L_G = 6.969290134e-10         # IAU 2000 defining constant: 1 - d(TT)/d(TCG), i.e. geoid potential / c^2
SECONDS_PER_DAY = 86_400.0
LIGHT_YEAR = sc.light_year    # m


# ---------------------------------------------------------------- 1. special relativity

def lorentz_boost(t, x, v, c=C):
    """Coordinates (t', x') of the event (t, x) seen from a frame moving at velocity v along +x."""
    beta = v / c
    gamma = 1.0 / np.sqrt(1.0 - beta ** 2)
    return gamma * (t - v * x / c ** 2), gamma * (x - v * t)


def interval(dt, dx, c=C):
    """Minkowski interval s^2 = -c^2 dt^2 + dx^2 (negative = timelike, positive = spacelike)."""
    return -(c * dt) ** 2 + dx ** 2


def simultaneity_shift(distance, v, c=C):
    """Two events simultaneous in frame S, separated by `distance` along x: time gap t2' - t1' in a frame moving at v."""
    t1, _ = lorentz_boost(0.0, 0.0, v, c)
    t2, _ = lorentz_boost(0.0, distance, v, c)
    return t2 - t1


# ---------------------------------------------------------------- 2. GPS clocks

def gps_clock_rates(a=A_GPS, gm=GM_EARTH, r_ground=R_EARTH_EQ, omega=OMEGA_EARTH):
    """Daily clock offsets (seconds/day) of a GPS satellite clock relative to a clock on the equator.

    Weak-field rate of a clock: d(tau)/dt = 1 + Phi/c^2 - v^2/(2c^2), with Phi = -GM/r (spherical Earth).
    Circular orbit: v^2 = GM/a. The ground clock moves at omega * R with Earth's rotation.
    Positive = satellite clock runs fast.
    """
    grav = gm / C ** 2 * (1.0 / r_ground - 1.0 / a)          # higher up -> weaker potential -> faster
    sat_velocity = -gm / (2.0 * a * C ** 2)                   # orbital speed -> slower
    ground_velocity = (omega * r_ground) ** 2 / (2.0 * C ** 2)  # ground clock is itself slowed by rotation
    net = grav + sat_velocity + ground_velocity
    net_geoid = L_G - 1.5 * gm / (a * C ** 2)                 # cross-check using the IAU geoid constant (includes J2)
    return {
        "gravitational": grav * SECONDS_PER_DAY,
        "satellite_velocity": sat_velocity * SECONDS_PER_DAY,
        "ground_rotation": ground_velocity * SECONDS_PER_DAY,
        "net": net * SECONDS_PER_DAY,
        "net_from_geoid_constant": net_geoid * SECONDS_PER_DAY,
        "orbital_speed_m_s": np.sqrt(gm / a),
    }


# ---------------------------------------------------------------- 3. Kerr black hole (G = c = M = 1)

def kerr_metric(r, theta, a):
    """Boyer-Lindquist components (g_tt, g_tphi, g_rr, g_thth, g_phph) of the Kerr metric, M = 1.

    Sigma = r^2 + a^2 cos^2(theta), Delta = r^2 - 2r + a^2.
    """
    r = np.asarray(r, dtype=float)
    sigma = r ** 2 + a ** 2 * np.cos(theta) ** 2
    delta = r ** 2 - 2.0 * r + a ** 2
    s2 = np.sin(theta) ** 2
    g_tt = -(1.0 - 2.0 * r / sigma)
    g_tph = -2.0 * a * r * s2 / sigma
    with np.errstate(divide="ignore"):
        g_rr = sigma / delta                  # infinite on the horizons (a coordinate singularity)
    g_thth = sigma
    g_phph = (r ** 2 + a ** 2 + 2.0 * a ** 2 * r * s2 / sigma) * s2
    return g_tt, g_tph, g_rr, g_thth, g_phph


def horizons(a):
    """Outer and inner horizons r+- = 1 +- sqrt(1 - a^2). Returns None for a > 1 (no horizon: naked singularity)."""
    if abs(a) > 1.0:
        return None
    s = np.sqrt(1.0 - a ** 2)
    return 1.0 + s, 1.0 - s


def ergosurface(a, theta):
    """Outer boundary of the ergosphere, r_ergo = 1 + sqrt(1 - a^2 cos^2 theta), where g_tt = 0."""
    return 1.0 + np.sqrt(1.0 - a ** 2 * np.cos(theta) ** 2)


def static_observer_norm(r, theta, a):
    """g(dt, dt) for an observer with u proportional to d/dt (sitting still). < 0 timelike, > 0 spacelike."""
    return kerr_metric(r, theta, a)[0]


def penrose_gain(a, r):
    """Energy gained in one Penrose split at radius r in the equatorial plane (M = 1, units of incoming energy).

    A particle of unit mass, falling from rest at infinity (E0 = 1), reaches a turning point at r and
    splits into two photons that also move tangentially. Conservation of E = -p_t and L = p_phi fixes
    both photons. Returns the energy of the escaping photon minus E0 (> 0 means energy was extracted),
    or 0 if no split with a negative-energy fragment exists at that radius.
    """
    g_tt, g_tph, _, _, g_phph = kerr_metric(r, np.pi / 2, a)
    det = g_tt * g_phph - g_tph ** 2
    i_tt, i_tph, i_phph = g_phph / det, -g_tph / det, g_tt / det      # inverse metric (t, phi block)
    # Photon with p^r = 0: i_tt x^2 - 2 i_tph x + i_phph = 0, x = E/L
    disc = i_tph ** 2 - i_tt * i_phph
    if disc < 0:
        return 0.0
    x1 = (i_tph + np.sqrt(disc)) / i_tt
    x2 = (i_tph - np.sqrt(disc)) / i_tt
    # Incoming particle, unit mass, E0 = 1, p^r = 0: i_phph L^2 - 2 i_tph L + i_tt + 1 = 0
    roots = np.roots([i_phph, -2.0 * i_tph, i_tt + 1.0])
    best = 0.0
    for L0 in roots:
        if abs(L0.imag) > 1e-12:
            continue
        L1, L2 = np.linalg.solve([[1.0, 1.0], [x1, x2]], [L0.real, 1.0])
        e1, e2 = x1 * L1, x2 * L2
        if min(e1, e2) < 0:
            best = max(best, max(e1, e2) - 1.0)
    return float(best)


def penrose_max_efficiency_numeric(a, eps=1e-5):
    """Numerical Penrose efficiency for a split just outside the outer horizon (the optimum).

    The gain converges linearly in eps; for a -> 1 the two photon roots nearly coincide, so eps
    much below 1e-5 loses floating-point precision.
    """
    r_plus = horizons(a)[0]
    return penrose_gain(a, r_plus * (1.0 + eps))


def penrose_max_efficiency_formula(a):
    """Textbook result: eta_max = (sqrt(2M / r+) - 1) / 2. For a = 1 this is (sqrt 2 - 1)/2 = 20.7 %."""
    return 0.5 * (np.sqrt(2.0 / horizons(a)[0]) - 1.0)


def irreducible_mass(a):
    """M_irr = sqrt(r+^2 + a^2) / 2 (M = 1). Horizon area A = 16 pi M_irr^2 can never decrease."""
    r_plus = horizons(a)[0]
    return np.sqrt(r_plus ** 2 + a ** 2) / 2.0


def max_extractable_fraction(a):
    """Largest fraction of a Kerr black hole's mass that can ever be extracted: 1 - M_irr / M."""
    return 1.0 - irreducible_mass(a)


# ---------------------------------------------------------------- 4. where time travel would have to live

def ctc_scan(a, r_min=-3.0, r_max=6.0, n=90_001, theta=np.pi / 2):
    """Scan r for g_phiphi < 0, i.e. where the closed loop phi -> phi + 2 pi (t, r, theta fixed) is timelike.

    Returns (r_lo, r_hi) bounding the region where g_phiphi < 0, or None if there is none.
    """
    r = np.linspace(r_min, r_max, n)
    r = r[np.abs(r) > 1e-9]                    # skip the singular point r = 0 at the equator
    g_phph = kerr_metric(r, theta, a)[4]
    bad = r[g_phph < 0]
    if bad.size == 0:
        return None
    return float(bad.min()), float(bad.max())


def main():
    print("1) Relativity of simultaneity (the real root of the 'block universe')")
    d = 2.5e6 * LIGHT_YEAR                   # distance to the Andromeda galaxy, ~2.5 million light years
    for v in (1.4, 30.0, 0.5 * C):
        shift = simultaneity_shift(d, v)
        print(f"   moving at v = {v:9.3g} m/s: 'now' on Andromeda shifts by "
              f"{abs(shift) / SECONDS_PER_DAY:10.4g} days ({abs(shift) / sc.year:.3g} years)")
    boosts = np.linspace(-0.99, 0.99, 199) * C
    t, x = 1.0, 0.5 * C                      # timelike pair: 1 s apart, half a light-second apart
    timelike_flips = int(sum(lorentz_boost(t, x, v)[0] <= 0 for v in boosts))
    t, x = 1.0, 2.0 * C                      # spacelike pair: 1 s apart, two light-seconds apart
    spacelike_flips = int(sum(lorentz_boost(t, x, v)[0] <= 0 for v in boosts))
    print(f"   Of {boosts.size} boosts up to 0.99c: a timelike pair is reversed in {timelike_flips}, "
          f"a spacelike pair in {spacelike_flips}.")
    print(f"   -> Observers {'can' if spacelike_flips else 'cannot'} disagree about the order of spacelike-separated events,"
          f" and {'can' if timelike_flips else 'cannot'} disagree about cause-before-effect.\n")

    print("2) GPS clocks (microseconds per day, + means the satellite clock runs fast)")
    g = gps_clock_rates()
    print(f"   gravitational (higher = faster) {g['gravitational'] * 1e6:+8.2f}")
    print(f"   satellite speed ({g['orbital_speed_m_s'] / 1e3:.2f} km/s)    {g['satellite_velocity'] * 1e6:+8.2f}")
    print(f"   ground clock's rotation         {g['ground_rotation'] * 1e6:+8.2f}")
    print(f"   net                             {g['net'] * 1e6:+8.2f}   (geoid-constant cross-check {g['net_from_geoid_constant'] * 1e6:+.2f})")
    print(f"   Uncorrected, that is a ranging error of {g['net'] * C / 1e3:.1f} km per day.\n")

    print("3) Kerr black hole, M = 1")
    for a in (0.0, 0.5, 0.9, 1.0):
        rp, rm = horizons(a)
        print(f"   a = {a:3.1f}  r+ = {rp:.4f}  r- = {rm:.4f}  equatorial ergosurface = {ergosurface(a, np.pi / 2):.1f}"
              f"  Penrose max = {100 * penrose_max_efficiency_numeric(a):5.2f}% (formula {100 * penrose_max_efficiency_formula(a):5.2f}%)"
              f"  extractable = {100 * max_extractable_fraction(a):5.2f}%")
    a = 0.9
    r_in = 0.5 * (horizons(a)[0] + ergosurface(a, np.pi / 2))
    print(f"   Static observer at a = 0.9: g_tt(r = 3) = {static_observer_norm(3.0, np.pi / 2, a):+.3f} (timelike), "
          f"g_tt(r = {r_in:.2f}, inside ergosphere) = {static_observer_norm(r_in, np.pi / 2, a):+.3f} (spacelike: cannot stand still)\n")

    print("4) Where closed timelike curves live (g_phiphi < 0, equatorial plane)")
    regions = []
    for a in (0.5, 0.9, 1.0, 1.2):
        region = ctc_scan(a)
        regions.append(region)
        hz = horizons(a)
        hz_txt = f"outer horizon r+ = {hz[0]:.3f}" if hz else "NO horizon: a naked singularity (a > M)"
        where = f"{region[0]:+.3f} < r < {region[1]:+.3f}" if region else "none"
        print(f"   a = {a:3.1f}  CTC region: {where:24s} {hz_txt}")
    outside = [r for r in regions if r is not None and r[1] > 0]
    print(f"   CTC regions reaching r > 0: {len(outside)} of {len(regions)}. They sit 'through' the ring singularity.")
    r_in, a = 1.72, 0.9
    g_tt, _, _, _, g_phph = kerr_metric(r_in, np.pi / 2, a)
    print(f"   Inside the ergosphere (a = 0.9, r = {r_in}): g_tt = {g_tt:+.3f}, g_phiphi = {g_phph:+.3f}. d/dt turned spacelike,")
    print(f"   but the phi-loop is still {'spacelike' if g_phph > 0 else 'TIMELIKE'}: frame dragging is not a closed timelike curve.")


if __name__ == "__main__":
    main()
