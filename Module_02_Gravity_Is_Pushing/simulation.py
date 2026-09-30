"""
Module 02 lab: Le Sage "pushing gravity", simulated honestly.

Three experiments, each computed from first principles (no force law is assumed):

1. shadow_force()        Monte Carlo ray counting: does a shadow give 1/r^2?  (Yes.)
2. absorbed_fraction()   Saturation: does the push stay proportional to mass?  (Only if bodies are nearly transparent.)
3. drag_and_heating()    The Poincare/Feynman problem: what does a flux strong enough to explain G do to a moving planet?

Run:  python simulation.py
"""
import numpy as np

G = 6.67430e-11          # m^3 kg^-1 s^-2 (CODATA 2018)
C = 299_792_458.0        # m/s
M_EARTH = 5.9722e24      # kg
R_EARTH = 6.371e6        # m
RHO_EARTH = 5514.0       # kg/m^3, mean density
V_EARTH_ORBIT = 29_780.0  # m/s
SECONDS_PER_YEAR = 3.156e7


def shadow_force(d, R2=1.0, n=2_000_000, seed=0):
    """Net push on a small absorber (body 1) from the shadow of a sphere of radius R2 at distance d.

    Rays arrive from isotropically random directions. Rays arriving from inside body 2's cone
    are blocked. Each blocked ray is momentum that would have pushed body 1 away from body 2,
    so its absence leaves a net push *toward* body 2.

    Returns the net force along +x in units of the total incoming momentum flux.
    """
    if d <= R2:
        raise ValueError("Body 1 must sit outside body 2.")
    rng = np.random.default_rng(seed)
    u = rng.uniform(-1.0, 1.0, n)                      # cos(angle between arrival direction and +x); uniform = isotropic
    blocked = u > np.sqrt(1.0 - (R2 / d) ** 2)          # arrival direction lies inside body 2's cone
    return float(np.mean(u * blocked))


def shadow_force_exact(d, R2=1.0):
    """Closed form of the Monte Carlo integral: (1/2) * integral_{cos t0}^{1} u du = (R2/d)^2 / 4."""
    return (R2 / d) ** 2 / 4.0


def absorbed_fraction(tau):
    """Fraction of a uniform beam absorbed by a uniform sphere of optical radius tau = mu * R.

    Averages 1 - exp(-mu * chord) over the sphere's disk. For tau << 1 this tends to 4*tau/3,
    i.e. proportional to volume (and so to mass). For tau >> 1 it saturates at 1: the body
    only casts a shadow as big as its outline, no matter how much mass is inside.
    """
    tau = np.asarray(tau, dtype=float)
    x = 2.0 * tau
    with np.errstate(divide="ignore", invalid="ignore"):
        f = 1.0 - (1.0 - (1.0 + x) * np.exp(-x)) / (2.0 * tau ** 2)
    small = tau < 1e-4
    return np.where(small, 4.0 * tau / 3.0 - tau ** 2, f)   # series avoids cancellation for tiny tau


def mass_proportionality(tau):
    """Shadow strength relative to the ideal 'proportional to mass' value 4*tau/3. 1.0 = perfect."""
    tau = np.asarray(tau, dtype=float)
    return absorbed_fraction(tau) / (4.0 * tau / 3.0)


def drag_and_heating(h, mass=M_EARTH, v=V_EARTH_ORBIT):
    """Consequences of a Le Sage flux tuned to reproduce G, for mass-attenuation coefficient h (m^2/kg).

    A small body of mass m absorbs a cross-section sigma = h * m. With isotropic flux of energy
    density u moving at c, the shadow force between two bodies is u * sigma1 * sigma2 / (4 pi r^2),
    so matching Newton requires u = 4 pi G / h^2.

    A body moving at v << c through that flux feels the standard absorber drag
    F = (4/3) sigma u v / c, and absorbs power P = sigma u c.
    """
    u = 4.0 * np.pi * G / h ** 2                 # J/m^3 needed to explain G
    sigma = h * mass                             # m^2
    drag = (4.0 / 3.0) * sigma * u * v / C       # N
    return {
        "energy_density_J_m3": u,
        "drag_N": drag,
        "velocity_decay_time_s": mass * v / drag,  # time for drag to remove the orbital speed
        "absorbed_power_W": sigma * u * C,
        "earth_optical_radius": h * RHO_EARTH * R_EARTH,
    }


def main():
    print("1) Shadow force from Monte Carlo ray counting (no force law assumed)")
    for d in (4.0, 8.0, 16.0):
        print(f"   d = {d:5.1f}   Monte Carlo = {shadow_force(d):.4e}   exact = {shadow_force_exact(d):.4e}")
    print(f"   F(4)/F(8) = {shadow_force(4.0) / shadow_force(8.0):.2f}   (inverse square predicts 4.00)\n")

    print("2) Does the shadow stay proportional to mass?  (1.00 = yes)")
    for tau in (1e-6, 1e-2, 0.1, 1.0, 10.0):
        print(f"   optical radius {tau:8.0e}  ->  {float(mass_proportionality(tau)):.3f}")
    print()

    print("3) The drag and heating dilemma for Earth (flux tuned to reproduce G)")
    print("   h (m^2/kg)   Earth optical radius   orbit stops in        absorbed power")
    for h in (1e-21, 1e-12, 1e-3, 1.0):
        r = drag_and_heating(h)
        years = r["velocity_decay_time_s"] / SECONDS_PER_YEAR
        print(f"   {h:9.0e}    {r['earth_optical_radius']:18.2e}   {years:10.2e} years   {r['absorbed_power_W']:10.2e} W")
    print("   Small h: Earth is transparent (good) but stops orbiting almost instantly and is vaporised.")
    print("   Large h: drag is tolerable but Earth is opaque, so gravity would stop scaling with mass.")
    print("   Sunlight delivers ~1.7e17 W to Earth; Earth has orbited for ~4.5e9 years.")


if __name__ == "__main__":
    main()
