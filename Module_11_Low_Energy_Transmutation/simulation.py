"""
Module 11 lab: can nuclei be "refolded" at room temperature?

Five experiments, each computed from first principles and published nuclear data:

1. coulomb_barrier(), gamow_energy()   The electric wall around every nucleus and the quantum tunnelling
                                       factor exp(-sqrt(E_G/E)) that decides how often it is crossed.
2. wkb_exponent()                      Tunnelling through a *screened* Coulomb wall (electrons partly cancel
                                       the repulsion), computed numerically with the WKB integral.
3. fusion_power_density()              An optimistic D-D fusion rate inside palladium deuteride at room
                                       temperature, as a function of the screening energy U_e.
4. neutrons_per_watt(), dose_rate()    Why 1 W of ordinary D-D fusion would be easy to detect and dangerous.
5. q_value(), transmutation_cost()     The energy bookkeeping of turning one element into another.

Run:  python simulation.py
"""
import numpy as np
from scipy import constants as sc
from scipy.integrate import quad
from scipy.optimize import brentq

ALPHA = sc.fine_structure
HBARC = sc.physical_constants["reduced Planck constant times c in MeV fm"][0]     # 197.327 MeV fm
E2 = ALPHA * HBARC                                                                  # e^2/(4 pi eps0) = 1.44 MeV fm
U_MEV = sc.physical_constants["atomic mass constant energy equivalent in MeV"][0]   # 931.494 MeV
M_D_MEV = sc.physical_constants["deuteron mass energy equivalent in MeV"][0]        # 1875.613 MeV
MEV_J = sc.physical_constants["electron volt"][0] * 1e6
K_B_EV = sc.physical_constants["Boltzmann constant in eV/K"][0]

# Atomic masses in u, AME2020 (Wang et al. 2021).
MASS_U = {
    "n": 1.00866491595, "H1": 1.00782503223, "H2": 2.01410177812, "H3": 3.01604928132,
    "He3": 3.01602932197, "He4": 4.00260325413, "K39": 38.9637064864, "Ca40": 39.9625908520,
    "Au197": 196.9665701, "Pb208": 207.9766525,
}

# D-D astrophysical S-factors near zero energy (keV b), Bosch & Hale (1992). Both branches roughly equal.
S_DD_KEV_B = {"p+T": 55.6, "n+He3": 53.7}
S_DD_TOTAL = sum(S_DD_KEV_B.values())

# Palladium: 12.02 g/cm^3, 106.42 g/mol.
N_PD_CM3 = 12.02 / 106.42 * sc.N_A

# Neutron fluence-to-ambient-dose conversion near 2.5 MeV, ~400 pSv cm^2 (ICRP 74, rounded).
NEUTRON_DOSE_SV_CM2 = 4.0e-10


# ---------------------------------------------------------------- 1. the Coulomb wall

def reduced_mass(m1_mev, m2_mev):
    """Reduced mass (MeV/c^2)."""
    return m1_mev * m2_mev / (m1_mev + m2_mev)


MU_DD = reduced_mass(M_D_MEV, M_D_MEV)


def coulomb_barrier(z1, z2, a1, a2, r0=1.2):
    """Coulomb energy (MeV) when two nuclei of radius r0*A^(1/3) fm just touch."""
    return z1 * z2 * E2 / (r0 * (a1 ** (1 / 3) + a2 ** (1 / 3)))


def gamow_energy(z1=1, z2=1, mu=MU_DD):
    """Gamow energy E_G = 2 mu c^2 (pi alpha Z1 Z2)^2 in MeV."""
    return 2.0 * mu * (np.pi * ALPHA * z1 * z2) ** 2


def sommerfeld(e_mev, z1=1, z2=1, mu=MU_DD):
    """Sommerfeld parameter eta = Z1 Z2 alpha sqrt(mu c^2 / 2E)."""
    return z1 * z2 * ALPHA * np.sqrt(mu / (2.0 * e_mev))


def gamow_factor(e_mev, z1=1, z2=1, mu=MU_DD):
    """Tunnelling probability through a bare Coulomb wall, exp(-2 pi eta) = exp(-sqrt(E_G/E))."""
    return np.exp(-np.sqrt(gamow_energy(z1, z2, mu) / e_mev))


def dd_cross_section_barn(e_mev, s_kev_b=S_DD_TOTAL):
    """sigma(E) = S(E)/E * exp(-sqrt(E_G/E)) with constant S; E is the centre-of-mass energy."""
    return s_kev_b / (e_mev * 1e3) * gamow_factor(e_mev)


# ---------------------------------------------------------------- 2. screening

def screening_enhancement(e_mev, u_e_mev, mu=MU_DD):
    """Assenbaum-Langanke-Rolfs enhancement f = exp(pi eta U_e / E). Valid for U_e << E."""
    return np.exp(np.pi * sommerfeld(e_mev, mu=mu) * u_e_mev / e_mev)


def screening_length(u_e_mev, z1=1, z2=1):
    """Screening length a (fm) of V = Z1Z2 e^2 exp(-r/a)/r, chosen so that V ~ Z1Z2 e^2/r - U_e at small r."""
    return z1 * z2 * E2 / u_e_mev


def wkb_exponent(e_mev, a_fm=np.inf, z1=1, z2=1, mu=MU_DD, r_nuc=0.0):
    """WKB exponent G, with tunnelling probability exp(-G), for V(r) = Z1Z2 e^2 exp(-r/a)/r.

    G = (2/hbar) * integral from r_nuc to the turning point of sqrt(2 mu (V - E)) dr.
    a_fm = inf is the bare Coulomb wall, for which G -> sqrt(E_G/E) as r_nuc -> 0.
    """
    k = z1 * z2 * E2

    def v(r):
        return k / r if np.isinf(a_fm) else k * np.exp(-r / a_fm) / r

    if np.isinf(a_fm):
        r_t = k / e_mev
    else:
        hi = k / e_mev
        r_t = brentq(lambda r: v(r) - e_mev, 1e-12 * hi, hi, xtol=1e-12 * hi, rtol=1e-13)
    if r_nuc >= r_t:
        return 0.0
    # substitute r = r_t u^2 to remove the 1/sqrt(r) singularity at r = 0
    f = lambda u: np.sqrt(max(v(r_t * u * u) - e_mev, 0.0)) * 2.0 * r_t * u
    val, _ = quad(f, np.sqrt(r_nuc / r_t), 1.0, limit=200, epsabs=0.0, epsrel=1e-10)
    return 2.0 * np.sqrt(2.0 * mu) / HBARC * val


# ---------------------------------------------------------------- 3. fusion in a metal lattice

def dd_reactivity_cm3_s(temp_k=300.0, u_e_ev=0.0, s_kev_b=S_DD_TOTAL):
    """Maxwell-averaged <sigma v> (cm^3/s) for D-D with Yukawa screening energy U_e.

    Deliberately optimistic: treats deuterium as a gas whose every pair is screened by U_e and whose
    high-energy Maxwell tail is fully available. Integrated on a log grid in log space (no underflow).
    """
    kt = K_B_EV * temp_k * 1e-6                          # MeV
    a = np.inf if u_e_ev <= 0 else screening_length(u_e_ev * 1e-6)
    e = np.logspace(np.log10(kt * 1e-2), np.log10(max(kt * 1e4, 2e-3)), 500)   # MeV
    g = np.array([wkb_exponent(ei, a) for ei in e])
    # <sigma v> = sqrt(8/(pi mu)) (kT)^-3/2 * integral S exp(-G) exp(-E/kT) dE
    log_f = np.log(s_kev_b * 1e-3 * 1e-24) - g - e / kt    # MeV cm^2 units inside S
    peak = log_f.max()
    integral = np.trapezoid(np.exp(log_f - peak), e) * MEV_J ** 2   # J^2 cm^2 (scaled by exp(-peak))
    mu_kg = MU_DD * MEV_J / sc.c ** 2
    pref = np.sqrt(8.0 / (np.pi * mu_kg)) * (kt * MEV_J) ** -1.5      # SI: kg^-1/2 J^-3/2
    return float(pref * integral * 100.0 * np.exp(peak))            # m/s * cm^2 -> cm^3/s


def fusion_power_density(u_e_ev, temp_k=300.0, loading=1.0):
    """D-D fusion power per cm^3 of PdD_x: 0.5 n^2 <sigma v> * <Q> (W/cm^3)."""
    n = loading * N_PD_CM3
    rate = 0.5 * n * n * dd_reactivity_cm3_s(temp_k, u_e_ev)
    return rate * mean_dd_q() * MEV_J


def screening_needed(power_w_cm3=1.0, temp_k=300.0):
    """Screening energy U_e (eV) that would make the optimistic model give power_w_cm3."""
    f = lambda log_u: np.log(max(fusion_power_density(10 ** log_u, temp_k), 1e-300)) - np.log(power_w_cm3)
    return 10 ** brentq(f, 1.0, 6.0, xtol=1e-3)


# ---------------------------------------------------------------- 4. the missing neutrons

def q_value(reactants, products):
    """Q (MeV) from atomic masses: (sum reactants - sum products) * 931.494 MeV/u."""
    return (sum(MASS_U[r] for r in reactants) - sum(MASS_U[p] for p in products)) * U_MEV


def mean_dd_q():
    """Energy per D-D fusion averaged over the two ~50% branches (MeV)."""
    return 0.5 * (q_value(["H2", "H2"], ["H3", "H1"]) + q_value(["H2", "H2"], ["He3", "n"]))


def neutrons_per_watt():
    """Neutrons/s from 1 W of ordinary D-D fusion (half the reactions give n + He-3)."""
    return 0.5 / (mean_dd_q() * MEV_J)


def dose_rate_sv_per_hour(power_w=1.0, distance_m=1.0):
    """Approximate neutron dose rate at distance_m from an unshielded point source (Sv/h)."""
    flux = power_w * neutrons_per_watt() / (4.0 * np.pi * (distance_m * 100.0) ** 2)   # n cm^-2 s^-1
    return flux * NEUTRON_DOSE_SV_CM2 * 3600.0


# ---------------------------------------------------------------- 5. transmutation bookkeeping

def transmutation_cost_mev(start, end, protons_out, neutrons_out):
    """Minimum energy (MeV) to take nucleus `start` to `end` by removing nucleons (negative = released)."""
    return -q_value([start], [end] + ["H1"] * protons_out + ["n"] * neutrons_out)


def energy_per_gram(mev_per_atom, molar_mass_g):
    """J per gram of product for a given energy per atom."""
    return mev_per_atom * MEV_J * sc.N_A / molar_mass_g


# ---------------------------------------------------------------- report

def main():
    eg = gamow_energy()
    print("1) The Coulomb wall around deuterium")
    print(f"   barrier when two deuterons touch:  {coulomb_barrier(1, 1, 2, 2) * 1e3:.0f} keV")
    print(f"   Gamow energy E_G for D-D:          {eg:.4f} MeV   (sqrt = {np.sqrt(eg * 1e3):.2f} keV^1/2)")
    kt300 = K_B_EV * 300.0
    print(f"   room temperature kT:               {kt300:.4f} eV")
    for e_ev in (kt300, 28.0, 800.0, 10e3):
        p = -np.sqrt(eg / (e_ev * 1e-6)) / np.log(10)
        print(f"   tunnelling at E = {e_ev:9.3f} eV:   10^{p:8.1f}")
    print()

    print("2) Electron screening (real, measured at keV beam energies)")
    print("   E (keV)   U_e = 28 eV (gas)   U_e = 300 eV   U_e = 800 eV   (enhancement exp(pi eta U_e/E))")
    for e_kev in (50.0, 10.0, 5.0, 2.0):
        row = [screening_enhancement(e_kev * 1e-3, u * 1e-6) for u in (28.0, 300.0, 800.0)]
        print(f"   {e_kev:6.1f}      {row[0]:10.3f}        {row[1]:10.3f}    {row[2]:10.3g}")
    print("   Screening matters at keV energies. At room temperature the pair never gets close enough:")
    for u in (28.0, 800.0):
        g = wkb_exponent(kt300 * 1e-6, screening_length(u * 1e-6))
        print(f"   WKB tunnelling at kT with U_e = {u:5.0f} eV (screening length {screening_length(u * 1e-6):6.0f} fm):"
              f" 10^{-g / np.log(10):.0f}")
    print()

    print("3) Optimistic D-D fusion power in PdD at 300 K (every pair screened, full Maxwell tail)")
    for u in (0.0, 28.0, 300.0, 800.0, 3000.0):
        p = fusion_power_density(u)
        print(f"   U_e = {u:6.0f} eV  ->  {p:9.2e} W/cm^3")
    u1 = screening_needed(1.0)
    print(f"   Screening needed for 1 W/cm^3 in this model: U_e ~ {u1:.0f} eV")
    p800 = fusion_power_density(800.0)
    print(f"   The rate changes by {fusion_power_density(880.0) / fusion_power_density(720.0):.0f}x for a +/-10% change"
          " in U_e: the answer rests entirely on an untested extrapolation")
    print("   of keV-beam screening data down to room-temperature deuterons.")
    print(f"   Even so, {p800:.1e} W/cm^3 of D-D fusion would emit {p800 * neutrons_per_watt():.1e} neutrons/s per cm^3.")
    print()

    print("4) If 1 W really came from ordinary D-D fusion")
    q_t, q_n = q_value(["H2", "H2"], ["H3", "H1"]), q_value(["H2", "H2"], ["He3", "n"])
    print(f"   Q(D+D -> T+p) = {q_t:.3f} MeV,  Q(D+D -> He3+n) = {q_n:.3f} MeV,"
          f"  Q(D+D -> He4+gamma) = {q_value(['H2', 'H2'], ['He4']):.2f} MeV")
    print(f"   reactions per second per watt: {1.0 / (mean_dd_q() * MEV_J):.2e}")
    print(f"   neutrons per second per watt:  {neutrons_per_watt():.2e}")
    d = dose_rate_sv_per_hour()
    print(f"   neutron dose rate 1 m away:    ~{d:.0f} Sv/h  (about {5.0 / d * 60:.0f} minutes to a"
          " typically lethal ~5 Sv)")
    print(f"   A detector counting even 1 neutron/s could see {1.0 / neutrons_per_watt():.0e} W of D-D fusion.")
    print()

    print("5) Energy bookkeeping for 'refolding' nuclei")
    q_kca = q_value(["K39", "H1"], ["Ca40"])
    verdict = "energy allowed" if q_kca > 0 else "energy forbidden"
    print(f"   K-39 + p -> Ca-40:  Q = {q_kca:+.2f} MeV ({verdict}), barrier = {coulomb_barrier(19, 1, 39, 1):.1f} MeV")
    mu_kp = reduced_mass(MASS_U["K39"] * U_MEV, MASS_U["H1"] * U_MEV)
    kt_body = K_B_EV * 310.0 * 1e-6
    print(f"   tunnelling at body temperature: 10^{-np.sqrt(gamow_energy(19, 1, mu_kp) / kt_body) / np.log(10):.0f}")
    cost = transmutation_cost_mev("Pb208", "Au197", 3, 8)
    print(f"   Pb-208 -> Au-197 + 3p + 8n costs at least {cost:.1f} MeV per atom"
          f" = {energy_per_gram(cost, 197.0) / 3.6e9:.1f} MWh per gram of gold")
    print(f"   A chemical bond or ATP hydrolysis supplies ~0.5 eV: {cost * 1e6 / 0.5:.1e}x too little.")


if __name__ == "__main__":
    main()
