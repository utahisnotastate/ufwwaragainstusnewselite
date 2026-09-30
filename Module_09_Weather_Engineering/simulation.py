"""
Module 09 lab: can electricity and "scalar beams" steer the weather?

Experiments, each computed rather than asserted:

1. global_circuit()             Earth's real fair-weather electric circuit: current, power, charge, conductivity.
2. Koehler theory               How a salt particle becomes a cloud droplet: haze below 100 % humidity,
                                activation only above a small critical supersaturation.
3. Thomson nucleation           Can ions make droplets without salt? Only at several-hundred-percent supersaturation.
4. ion_wind_thrust()            Electrohydrodynamic "ion wind" is real, but tiny.
5. Energy budget                Latent heat of storms vs every electrical lever we have.
6. crossed_beams(), skin_depth()  Interference only moves energy around; radio waves do not pass through the sea.

Run:  python simulation.py
"""
import numpy as np
from scipy import constants as sc
from scipy.optimize import brentq, minimize_scalar

K_B = sc.k                     # J/K
R_GAS = sc.R                   # J mol^-1 K^-1
EPS0 = sc.epsilon_0            # F/m
MU0 = sc.mu_0                  # H/m
E_CHARGE = sc.e                # C
N_A = sc.N_A
G0 = sc.g                      # m/s^2, standard gravity

# Water and salt (textbook values, ~25 C unless noted)
M_W = 0.018015                 # kg/mol
RHO_W = 997.0                  # kg/m^3
SIGMA_W = 0.0720               # N/m, surface tension of water at 25 C
T_ROOM = 298.15                # K
M_NACL = 0.058443              # kg/mol
RHO_NACL = 2165.0              # kg/m^3
I_NACL = 2.0                   # ideal van 't Hoff factor
NACL_SAT_MOLALITY = 6.15       # mol/kg, solubility at 25 C (~36 g per 100 g water)
NACL_SAT_OSMOTIC_COEFF = 1.27  # osmotic coefficient of NaCl(aq) near saturation (Robinson & Stokes tables)
KAPPA_NACL = 1.28              # hygroscopicity parameter (Petters & Kreidenweis 2007)

# Cold water for nucleation (0 C)
T_COLD = 273.15
SIGMA_W_COLD = 0.0756
RHO_W_COLD = 999.8
EPS_R_WATER = 80.0

# Atmosphere and Earth
L_V = 2.5e6                    # J/kg, latent heat of vaporisation (0 C: 2.501e6)
CP_AIR = 1004.0                # J kg^-1 K^-1
P_SURFACE = 101_325.0          # Pa
R_EARTH = 6.371e6              # m
SOLAR_CONSTANT = 1361.0        # W/m^2 (Kopp & Lean 2011)
ALBEDO = 0.30
IONOSPHERE_POTENTIAL = 250e3   # V
FAIR_WEATHER_FIELD = 120.0     # V/m at the surface (typical 100-130)
FAIR_WEATHER_CURRENT = 2e-12   # A/m^2
ION_MOBILITY = 2e-4            # m^2 V^-1 s^-1, small air ions (typical 1.5-2e-4)
HAARP_POWER = 3.6e6            # W, transmitter power of the HAARP ionospheric research instrument


# ---------------------------------------------------------------- 1. global electric circuit

def global_circuit(potential=IONOSPHERE_POTENTIAL, field=FAIR_WEATHER_FIELD, current_density=FAIR_WEATHER_CURRENT):
    """Totals implied by typical fair-weather values: current, power, resistance, surface charge, conductivity."""
    area = 4.0 * np.pi * R_EARTH ** 2
    current = current_density * area
    conductivity = current_density / field                 # Ohm's law at the surface, S/m
    return {
        "current_A": current,
        "power_W": potential * current,
        "resistance_ohm": potential / current,
        "earth_charge_C": EPS0 * field * area,               # Gauss's law
        "surface_conductivity_S_m": conductivity,
        "relaxation_time_s": EPS0 / conductivity,            # how fast the circuit would discharge without storms
    }


# ---------------------------------------------------------------- 2. Koehler theory

def kelvin_A(T=T_ROOM, sigma=SIGMA_W, rho_w=RHO_W):
    """Curvature (Kelvin) length A = 2 sigma M_w / (R T rho_w), about 1 nm."""
    return 2.0 * sigma * M_W / (R_GAS * T * rho_w)


def raoult_B(m_s, i=I_NACL, M_s=M_NACL, rho_w=RHO_W):
    """Solute term B = 3 i m_s M_w / (4 pi rho_w M_s)  (m^3)."""
    return 3.0 * i * m_s * M_W / (4.0 * np.pi * rho_w * M_s)


def dry_radius(m_s, rho_s=RHO_NACL):
    """Radius of the dry salt crystal of mass m_s, treated as a sphere."""
    return (3.0 * m_s / (4.0 * np.pi * rho_s)) ** (1.0 / 3.0)


def salt_mass_from_dry_diameter(D, rho_s=RHO_NACL):
    return rho_s * np.pi * D ** 3 / 6.0


def saturation_ratio(r, m_s, T=T_ROOM, i=I_NACL, approx=False):
    """Equilibrium saturation ratio over a solution droplet of radius r containing salt mass m_s.

    Full form: S = a_w exp(A/r), with ideal Raoult activity a_w = n_w / (n_w + i n_s) and the
    water volume = droplet volume - salt volume.  approx=True gives the classic S = 1 + A/r - B/r^3.
    """
    r = np.asarray(r, dtype=float)
    A = kelvin_A(T)
    if approx:
        return 1.0 + A / r - raoult_B(m_s, i) / r ** 3
    water_mass = RHO_W * (4.0 / 3.0 * np.pi * r ** 3 - m_s / RHO_NACL)
    n_w, n_s = water_mass / M_W, m_s / M_NACL
    return n_w / (n_w + i * n_s) * np.exp(A / r)


def critical_point(m_s, T=T_ROOM, i=I_NACL):
    """Peak of the full Koehler curve, found numerically: (critical radius, critical saturation ratio)."""
    lo = np.log(dry_radius(m_s) * 1.001)
    res = minimize_scalar(lambda lr: -np.log(saturation_ratio(np.exp(lr), m_s, T, i)),
                          bounds=(lo, np.log(1e-3)), method="bounded", options={"xatol": 1e-10})
    r_c = float(np.exp(res.x))
    return r_c, float(saturation_ratio(r_c, m_s, T, i))


def critical_point_analytic(m_s, T=T_ROOM, i=I_NACL):
    """Approximate Koehler peak: r_c = sqrt(3B/A), S_c = 1 + sqrt(4 A^3 / (27 B))."""
    A, B = kelvin_A(T), raoult_B(m_s, i)
    return np.sqrt(3.0 * B / A), 1.0 + np.sqrt(4.0 * A ** 3 / (27.0 * B))


def kappa_critical_saturation(D_dry, kappa=KAPPA_NACL, T=T_ROOM):
    """kappa-Koehler (Petters & Kreidenweis 2007) critical saturation: ln S_c = sqrt(4 A_D^3 / (27 kappa D_dry^3)),
    with A_D = 4 sigma M_w / (R T rho_w)."""
    A_D = 2.0 * kelvin_A(T)
    return float(np.exp(np.sqrt(4.0 * A_D ** 3 / (27.0 * kappa * D_dry ** 3))))


def equilibrium_radius(S, m_s, T=T_ROOM):
    """Stable (haze) droplet radius at ambient saturation ratio S, or None if S exceeds the critical value
    (then no stable size exists and the droplet grows without limit: it has 'activated')."""
    r_c, S_c = critical_point(m_s, T)
    if S >= S_c:
        return None
    lo = dry_radius(m_s) * (1.0 + 1e-9)
    return float(brentq(lambda r: saturation_ratio(r, m_s, T) - S, lo, r_c, xtol=1e-15, rtol=1e-12))


def deliquescence_rh(molality=NACL_SAT_MOLALITY, osmotic_coeff=NACL_SAT_OSMOTIC_COEFF, nu=I_NACL):
    """Water activity of a saturated solution, a_w = exp(-nu m phi M_w): the humidity at which a dry crystal dissolves.
    osmotic_coeff = 1 gives the ideal-solution answer."""
    return float(np.exp(-nu * molality * osmotic_coeff * M_W))


# ---------------------------------------------------------------- 3. Thomson (ion-induced) nucleation

def thomson_free_energy(r, S, charge=E_CHARGE, T=T_COLD, sigma=SIGMA_W_COLD, eps_r=EPS_R_WATER, r0=3e-10):
    """Free energy (J) to form a pure-water droplet of radius r around a charge q at saturation ratio S.

    dG = -(4/3) pi r^3 n_l k T ln S  +  4 pi r^2 sigma  +  q^2/(8 pi eps0) (1 - 1/eps_r) (1/r - 1/r0)
    (bulk)                             (surface)          (Thomson/Born term; zero for charge = 0)
    """
    r = np.asarray(r, dtype=float)
    n_l = RHO_W_COLD * N_A / M_W
    bulk = -(4.0 / 3.0) * np.pi * r ** 3 * n_l * K_B * T * np.log(S)
    surface = 4.0 * np.pi * r ** 2 * sigma
    ion = charge ** 2 / (8.0 * np.pi * EPS0) * (1.0 - 1.0 / eps_r) * (1.0 / r - 1.0 / r0)
    return bulk + surface + ion


def nucleation_barrier(S, charge=E_CHARGE, T=T_COLD, r0=3e-10):
    """Barrier height (J) and critical radius (m). Barrier = max of dG minus the stable-cluster minimum before it.

    For S <= 1 the bulk term is positive, dG has no maximum and droplets never grow: returns (inf, None).
    For S > 1 with no maximum the barrier has vanished altogether: returns (0.0, None).
    """
    r = np.logspace(np.log10(r0), -3, 60_000)
    g = thomson_free_energy(r, S, charge, T, r0=r0)
    dg = np.diff(g)
    peaks = np.where((dg[:-1] > 0) & (dg[1:] <= 0))[0] + 1
    if len(peaks) == 0:
        return (np.inf, None) if S <= 1.0 else (0.0, None)
    k = peaks[0]
    res = minimize_scalar(lambda x: -float(thomson_free_energy(x, S, charge, T, r0=r0)),
                          bounds=(r[k - 1], r[k + 1]), method="bounded", options={"xatol": 1e-16})
    g_max = -res.fun
    g_min = min(0.0, float(g[:k].min())) if charge == 0 else float(g[:k].min())
    return g_max - g_min, float(res.x)


def neutral_barrier_analytic(S, T=T_COLD, sigma=SIGMA_W_COLD):
    """Classical nucleation theory: r* = 2 sigma v_m / (kT ln S), dG* = 16 pi sigma^3 v_m^2 / (3 (kT ln S)^2)."""
    v_m = M_W / (RHO_W_COLD * N_A)
    kTlnS = K_B * T * np.log(S)
    return 16.0 * np.pi * sigma ** 3 * v_m ** 2 / (3.0 * kTlnS ** 2), 2.0 * sigma * v_m / kTlnS


def saturation_for_barrier(barrier_kT=60.0, charge=E_CHARGE, T=T_COLD):
    """Saturation ratio at which the nucleation barrier falls to barrier_kT (a ~60 kT barrier corresponds to
    roughly one droplet per cm^3 per second for water; the exact figure depends on a kinetic prefactor)."""
    f = lambda S: nucleation_barrier(S, charge, T)[0] / (K_B * T) - barrier_kT
    return float(brentq(f, 1.05, 50.0, xtol=1e-6))


# ---------------------------------------------------------------- 4. ion wind

def ion_wind_thrust(current, gap, mobility=ION_MOBILITY):
    """One-dimensional electrohydrodynamic thrust T = I d / mu (N) for ion current I across a gap d."""
    return current * gap / mobility


def thrust_per_power(voltage, gap, mobility=ION_MOBILITY):
    """T / P = d / (mu V)  (N/W), since P = I V."""
    return gap / (mobility * voltage)


# ---------------------------------------------------------------- 5. energy budget

def rain_latent_heat(rain_depth, radius):
    """Latent heat (J) released by condensing the water that falls as rain_depth (m) over a disk of radius (m)."""
    return RHO_W * rain_depth * np.pi * radius ** 2 * L_V


def hurricane_heat_power(rain_rate=0.015, radius=665e3):
    """Average heat release (W) of a hurricane raining rain_rate m/day over a disk of given radius
    (the estimate used in NOAA's Hurricane Research Division FAQ)."""
    return rain_latent_heat(rain_rate, radius) / 86_400.0


def column_heating_energy(area, delta_T):
    """Energy (J) to warm the whole atmospheric column above an area by delta_T (column mass = p_s / g)."""
    return (P_SURFACE / G0) * area * CP_AIR * delta_T


def solar_power_absorbed():
    """Sunlight absorbed by Earth (W): S0 pi R^2 (1 - albedo)."""
    return SOLAR_CONSTANT * np.pi * R_EARTH ** 2 * (1.0 - ALBEDO)


# ---------------------------------------------------------------- 6. crossed beams and penetration

def crossed_beams(phase, I1=1.0, I2=1.0):
    """Time-averaged intensity where two coherent beams overlap with relative phase `phase`:
    I = I1 + I2 + 2 sqrt(I1 I2) cos(phase). Never negative; averaged over the fringes it is I1 + I2."""
    return I1 + I2 + 2.0 * np.sqrt(I1 * I2) * np.cos(np.asarray(phase, dtype=float))


def skin_depth(frequency, conductivity, eps_r=1.0):
    """Exact 1/e amplitude penetration depth (m) of a plane wave in a medium with conductivity (S/m) and eps_r."""
    w = 2.0 * np.pi * np.asarray(frequency, dtype=float)
    eps = eps_r * EPS0
    loss = conductivity / (w * eps)
    alpha = w * np.sqrt(MU0 * eps / 2.0) * np.sqrt(np.sqrt(1.0 + loss ** 2) - 1.0)
    return 1.0 / alpha


# ---------------------------------------------------------------- report

def main():
    gc = global_circuit()
    print("1) The real global electric circuit (fair-weather values)")
    print(f"   total current {gc['current_A']:.0f} A, power {gc['power_W'] / 1e6:.0f} MW, "
          f"resistance {gc['resistance_ohm']:.0f} ohm")
    print(f"   Earth's surface charge {gc['earth_charge_C']:.1e} C; surface air conductivity "
          f"{gc['surface_conductivity_S_m']:.1e} S/m; discharges in ~{gc['relaxation_time_s']:.0f} s without thunderstorms\n")

    print("2) Koehler theory for NaCl particles (25 C)")
    print("   dry diameter   critical radius   critical supersaturation   (kappa-Koehler check)")
    for D in (20e-9, 50e-9, 100e-9, 200e-9):
        m = salt_mass_from_dry_diameter(D)
        r_c, S_c = critical_point(m)
        print(f"   {D * 1e9:6.0f} nm      {r_c * 1e6:8.3f} um        {100 * (S_c - 1):8.3f} %"
              f"            {100 * (kappa_critical_saturation(D) - 1):.3f} %")
    m = salt_mass_from_dry_diameter(100e-9)
    print("   Haze: equilibrium radius of that 100 nm particle vs relative humidity")
    for S in (0.80, 0.90, 0.99, 1.0005):
        r = equilibrium_radius(S, m)
        print(f"     RH {100 * S:7.2f} %  ->  r = {r * 1e6:.3f} um")
    r_c, S_c = critical_point(m)
    print(f"     RH {100 * 1.002:7.2f} %  ->  {equilibrium_radius(1.002, m)}  (above S_c = {S_c:.5f}: activates)")
    print(f"   Deliquescence RH of NaCl: {100 * deliquescence_rh():.1f} % (non-ideal), "
          f"{100 * deliquescence_rh(osmotic_coeff=1.0):.1f} % if the solution were ideal (measured: ~75 %)\n")

    print("3) Droplets from ions alone (Thomson theory, 0 C, pure water)")
    for S in (0.9, 1.01, 2.0, 4.0):
        bn, bi = nucleation_barrier(S, 0.0)[0], nucleation_barrier(S, E_CHARGE)[0]
        print(f"   S = {S:4.2f}   barrier neutral = {bn / (K_B * T_COLD):10.3g} kT   one ion = {bi / (K_B * T_COLD):10.3g} kT")
    s_n, s_i = saturation_for_barrier(60.0, 0.0), saturation_for_barrier(60.0, E_CHARGE)
    print(f"   Barrier falls to 60 kT at S = {s_n:.2f} (neutral) and S = {s_i:.2f} (singly charged).")
    print(f"   Real clouds rarely exceed S = 1.01. Even with an ion, droplets need ~{100 * (s_i - 1):.0f} % supersaturation;")
    print("   in real air, salt and other particles (Koehler, above) activate long before that.")
    print("   (Continuum theory is only rough for clusters this small; the ordering, not the digits, is the point.)\n")

    print("4) Ion wind")
    print(f"   Thrust per power at 40 kV across 5 cm: {1e3 * thrust_per_power(40e3, 0.05):.1f} N/kW")
    print(f"   A 100 kV x 1 mA ground array (100 W), 5 cm gap: {ion_wind_thrust(1e-3, 0.05):.2f} N of push\n")

    array_power = 100e3 * 1e-3
    storm = rain_latent_heat(0.02, 5e3)
    hurricane = hurricane_heat_power()
    column = column_heating_energy((100e3) ** 2, 1.0)
    print("5) Energy budget")
    print(f"   Thunderstorm (2 cm of rain over a 5 km radius): {storm:.1e} J of latent heat")
    print(f"   Hurricane heat release: {hurricane:.1e} W   (whole global circuit: {gc['power_W']:.1e} W)")
    print(f"   Sunlight absorbed by Earth: {solar_power_absorbed():.2e} W")
    print(f"   Warming the air over 100 km x 100 km by 1 K: {column:.1e} J")
    yr = 3.156e7
    print(f"     at 100 W (ion array): {column / array_power / yr:.1e} years;"
          f" at 3.6 MW (HAARP, if every watt were absorbed): {column / HAARP_POWER / yr:.0f} years")
    print(f"   The hurricane out-powers the ion array by a factor of {hurricane / array_power:.0e}\n")

    print("6) Crossing beams and 'waves through the Earth'")
    ph = np.linspace(0, 2 * np.pi, 10_001)[:-1]
    I = crossed_beams(ph)
    print(f"   Two unit beams: brightest fringe {I.max():.2f}, darkest {I.min():.2f}, average {I.mean():.3f}"
          " -> energy is moved, never created or destroyed")
    for f in (10.0, 1e3, 1e6):
        print(f"   {f:9.0f} Hz: skin depth in seawater {skin_depth(f, 4.0, 81.0):8.2f} m, "
              f"in rock {skin_depth(f, 1e-3, 10.0):9.0f} m")
    frac = np.exp(-1e6 / skin_depth(10.0, 1e-3, 10.0))
    print(f"   Amplitude left after 1000 km of rock at 10 Hz: {frac:.1e} (the Earth is 12 742 km across)")


if __name__ == "__main__":
    main()
