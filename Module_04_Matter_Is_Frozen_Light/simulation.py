"""
Module 04 lab: is matter "frozen light"?

Four experiments, each computed rather than asserted:

1. mass_defect()                  E = mc^2 at everyday and nuclear scales, and where a proton's mass comes from.
2. breit_wheeler_*()              Light really can become matter: threshold, cross section, and an independent
                                  check of the cross section against Dirac's annihilation formula.
3. schwinger_field()              How strong a field must be to rip pairs straight out of the vacuum.
4. loop_magnetic_moment(), qed_anomaly()
                                  The "photon running in a circle" electron model versus quantum electrodynamics.

Run:  python simulation.py
"""
import numpy as np
from scipy import constants as sc

C = sc.c
HBAR = sc.hbar
E_CHARGE = sc.e
EPS0 = sc.epsilon_0
M_E = sc.m_e
M_MU = sc.physical_constants["muon mass"][0]
EV = sc.electron_volt
MEC2_EV = M_E * C ** 2 / EV                                    # 510 998.95 eV
R_E = sc.physical_constants["classical electron radius"][0]   # m
SIGMA_T = 8.0 * np.pi / 3.0 * R_E ** 2                        # Thomson cross section, m^2
MU_B = sc.physical_constants["Bohr magneton"][0]
LAMBDA_C_BAR = sc.physical_constants["reduced Compton wavelength"][0]
M_PROTON_MEV = sc.physical_constants["proton mass energy equivalent in MeV"][0]

# Light-quark masses, MS-bar at 2 GeV (Particle Data Group 2022): scheme-dependent, uncertain by ~10-20 %
M_UP_MEV, M_DOWN_MEV = 2.16, 4.67

# Measured electron magnetic moment, g/2 (Fan et al., PRL 130, 071801 (2023))
MEASURED_G_OVER_2 = 1.00115965218059
# Fine-structure constant from rubidium atom recoil, independent of g-2 (Morel et al., Nature 588, 61 (2020))
ALPHA_RB = 1.0 / 137.035999206
# Mass-independent QED coefficients of a_e = sum A_n (alpha/pi)^n (Schwinger; Petermann/Sommerfield;
# Laporta & Remiddi; Laporta), as tabulated in CODATA
QED_COEFFS = (0.5, -0.328478965579193, 1.181241456587, -1.912245764926)

ELECTRON_SIZE_BOUND_M = 1e-18          # order of the bound from high-energy e+e- scattering (LEP)
RECORD_LASER_W_CM2 = 1.1e23            # Yoon et al., Optica 8, 630 (2021)
TNT_KT_J = 4.184e12                    # J per kiloton of TNT (definition)
WOOD_J_PER_KG = 1.6e7                  # typical heat of combustion of dry wood, ~16 MJ/kg


# ---------------------------------------------------------------- 1. E = mc^2
def mass_defect(energy_j):
    """Mass (kg) that disappears when energy_j joules are released: m = E / c^2."""
    return energy_j / C ** 2


def proton_valence_quark_fraction(m_up=M_UP_MEV, m_down=M_DOWN_MEV):
    """Fraction of the proton's mass made up by the rest masses of its valence quarks (uud)."""
    return (2.0 * m_up + m_down) / M_PROTON_MEV


# ---------------------------------------------------------------- 2. Breit-Wheeler pair production
def mandelstam_s(e1_ev, e2_ev, theta):
    """Invariant s (eV^2) of two photons with energies e1, e2 and angle theta between their directions."""
    return 2.0 * e1_ev * e2_ev * (1.0 - np.cos(theta))


def breit_wheeler_threshold(e1_ev, theta=np.pi):
    """Smallest e2 (eV) that can make an e+e- pair with a photon of energy e1: e1 e2 (1 - cos theta) >= 2 (mc^2)^2."""
    return 2.0 * MEC2_EV ** 2 / (e1_ev * (1.0 - np.cos(theta)))


def pair_beta(s_ev2):
    """Speed (v/c) of each lepton in the centre-of-mass frame, beta = sqrt(1 - 4 m^2 c^4 / s); 0 below threshold."""
    x = 1.0 - 4.0 * MEC2_EV ** 2 / np.asarray(s_ev2, dtype=float)
    return np.sqrt(np.clip(x, 0.0, None))


def breit_wheeler_cross_section(beta):
    """Total cross section (m^2) for gamma gamma -> e+ e- (Breit & Wheeler 1934):
    sigma = (pi r_e^2 / 2)(1 - beta^2)[(3 - beta^4) ln((1 + beta)/(1 - beta)) - 2 beta (2 - beta^2)]."""
    b = np.asarray(beta, dtype=float)
    return np.pi * R_E ** 2 / 2.0 * (1.0 - b ** 2) * ((3.0 - b ** 4) * 2.0 * np.arctanh(b) - 2.0 * b * (2.0 - b ** 2))


def dirac_annihilation_cross_section(gamma):
    """Total cross section (m^2) for e+ e- -> gamma gamma, positron of Lorentz factor gamma hitting an electron at
    rest (Dirac 1930). Used as an independent check of Breit-Wheeler via detailed balance."""
    g = np.asarray(gamma, dtype=float)
    root = np.sqrt(g ** 2 - 1.0)
    return np.pi * R_E ** 2 / (g + 1.0) * ((g ** 2 + 4.0 * g + 1.0) / (g ** 2 - 1.0) * np.log(g + root) - (g + 3.0) / root)


def breit_wheeler_from_annihilation(beta):
    """Breit-Wheeler cross section rebuilt from Dirac's formula: sigma_gg = 2 beta^2 sigma_ann (detailed balance:
    same matrix element, ratio of final-state momenta squared, factor 2 for identical photons)."""
    b = np.asarray(beta, dtype=float)
    gamma_cm = 1.0 / np.sqrt(1.0 - b ** 2)
    return 2.0 * b ** 2 * dirac_annihilation_cross_section(2.0 * gamma_cm ** 2 - 1.0)


def compton_edge(e_electron_ev, e_laser_ev):
    """Maximum energy (eV) of a laser photon back-scattered head-on off an electron beam: E x / (1 + x),
    x = 4 E w0 / (mc^2)^2."""
    x = 4.0 * e_electron_ev * e_laser_ev / MEC2_EV ** 2
    return e_electron_ev * x / (1.0 + x)


def min_laser_photons(e_gamma_ev, e_laser_ev, theta=np.pi):
    """Kinematic lower bound on how many laser photons must be absorbed together with one gamma to make a pair."""
    return int(np.ceil(breit_wheeler_threshold(e_gamma_ev, theta) / e_laser_ev))


# ---------------------------------------------------------------- 3. Schwinger critical field
def schwinger_field():
    """Critical field E_crit = m_e^2 c^3 / (e hbar) in V/m: one electron charge gains m_e c^2 over a Compton length."""
    return M_E ** 2 * C ** 3 / (E_CHARGE * HBAR)


def field_to_intensity_w_cm2(e_field):
    """Cycle-averaged intensity c eps0 E^2 / 2 of a plane wave with peak field e_field (W/cm^2)."""
    return C * EPS0 * e_field ** 2 / 2.0 / 1e4


def intensity_to_field(intensity_w_cm2):
    """Peak field (V/m) of a plane wave with the given intensity (W/cm^2)."""
    return np.sqrt(2.0 * intensity_w_cm2 * 1e4 / (C * EPS0))


def schwinger_suppression_log10(e_field):
    """log10 of the exponential factor exp(-pi E_crit / E) that controls vacuum pair creation in a static field."""
    return float(-np.pi * schwinger_field() / e_field / np.log(10.0))


# ---------------------------------------------------------------- 4. The "light in a loop" electron
def loop_magnetic_moment(radius, charge=E_CHARGE, speed=C):
    """Magnetic moment (J/T) of a charge circulating at `speed` on a circle: I * area = (q v / 2 pi r) pi r^2 = q v r / 2."""
    return charge * speed * radius / 2.0


def toroidal_model_moment(mass=M_E):
    """The photon-in-a-loop estimate: put the charge at the reduced Compton radius hbar / (m c), moving at c."""
    return loop_magnetic_moment(HBAR / (mass * C))


def qed_anomaly(order=4, alpha=ALPHA_RB):
    """Electron anomaly a_e = (g - 2)/2 from the mass-independent QED series truncated after `order` loops."""
    x = alpha / np.pi
    return float(sum(a * x ** (n + 1) for n, a in enumerate(QED_COEFFS[:order])))


def main():
    print("1) E = mc^2 is real, and mass is mostly energy")
    print(f"   Electron rest energy m_e c^2 = {MEC2_EV / 1e6:.6f} MeV")
    for label, e in (("Burning 1 kg of dry wood", WOOD_J_PER_KG), ("A 15 kiloton fission bomb", 15 * TNT_KT_J)):
        print(f"   {label:28s} releases {e:.1e} J -> mass lost {mass_defect(e) * 1e3:.2e} g")
    print(f"   So burning wood converts {mass_defect(WOOD_J_PER_KG):.1e} of its mass; 'untying' is real but tiny.")
    f = proton_valence_quark_fraction()
    print(f"   Valence quark rest masses (uud) are {100 * f:.1f}% of the proton's {M_PROTON_MEV:.2f} MeV;"
          f" the other {100 * (1 - f):.0f}% is QCD energy (quark motion, gluon fields, sea quarks).\n")

    print("2) Light into matter: the Breit-Wheeler process  gamma + gamma -> e+ + e-")
    print(f"   Head-on threshold for two equal photons: {breit_wheeler_threshold(MEC2_EV) / 1e3:.1f} keV each")
    sun = 2.0
    print(f"   A {sun:.0f} eV sunlight photon needs a partner of at least {breit_wheeler_threshold(sun) / 1e9:.0f} GeV (head-on).")
    print(f"   Two sunlight photons fall short of threshold by a factor {4 * MEC2_EV ** 2 / mandelstam_s(sun, sun, np.pi):.1e} in s.")
    b = np.linspace(1e-4, 1 - 1e-6, 200_001)
    sig = breit_wheeler_cross_section(b)
    i = int(np.argmax(sig))
    print(f"   Peak cross section {sig[i] * 1e4:.2e} cm^2 = {sig[i] / SIGMA_T:.3f} sigma_Thomson at beta = {b[i]:.2f}")
    chk = np.array([0.05, 0.5, 0.95])
    dev = np.max(np.abs(breit_wheeler_cross_section(chk) / breit_wheeler_from_annihilation(chk) - 1))
    print(f"   Independent check against Dirac's annihilation formula (detailed balance): max deviation {dev:.1e}")
    e_edge = compton_edge(46.6e9, 2.35)
    print(f"   SLAC E-144: 46.6 GeV electrons + 527 nm laser -> Compton photons up to {e_edge / 1e9:.1f} GeV;")
    print(f"   making a pair then needs >= {min_laser_photons(e_edge, 2.35)} laser photons at once (nonlinear, multiphoton).")
    print("   STAR (2021) used quasi-real photons from the fields of colliding gold nuclei, not free laser light.\n")

    print("3) Tearing pairs from the vacuum with a field (Schwinger)")
    ec = schwinger_field()
    e_rec = intensity_to_field(RECORD_LASER_W_CM2)
    print(f"   E_crit = {ec:.3e} V/m  (intensity {field_to_intensity_w_cm2(ec):.1e} W/cm^2)")
    print(f"   Record laser {RECORD_LASER_W_CM2:.1e} W/cm^2 -> {e_rec:.1e} V/m = {e_rec / ec:.1e} E_crit;"
          f" pair factor exp(-pi E_crit/E) = 10^{schwinger_suppression_log10(e_rec):.0f}\n")

    print("4) Is the electron a photon running in a circle?")
    mu_model = toroidal_model_moment()
    print(f"   Loop radius hbar/(m_e c) = {LAMBDA_C_BAR:.3e} m;  moment e c r / 2 = {mu_model:.6e} J/T")
    print(f"   Bohr magneton e hbar/(2 m_e) = {MU_B:.6e} J/T;  ratio = {mu_model / MU_B:.15f}")
    mu_ratio_muon = toroidal_model_moment(M_MU) / (E_CHARGE * HBAR / (2 * M_MU))
    print(f"   Same recipe for the muon gives its magneton again (ratio {mu_ratio_muon:.15f}): the radius was chosen")
    print("   from the mass, so matching the magneton is a restatement, not a prediction.")
    a_meas = MEASURED_G_OVER_2 - 1.0
    print(f"   Measured g/2 = {MEASURED_G_OVER_2:.14f}.  Photon-loop model: 1 exactly, off by {a_meas:.3e}")
    for k in range(1, len(QED_COEFFS) + 1):
        a = qed_anomaly(k)
        print(f"   QED to {k} loop(s): g/2 = {1 + a:.14f}   off by {abs(a_meas - a):.1e}")
    print(f"   After 4 loops QED is {a_meas / abs(a_meas - qed_anomaly(4)):.0e} times closer than the loop model.")
    print(f"   Scattering experiments: electron radius < ~{ELECTRON_SIZE_BOUND_M:.0e} m, "
          f"{LAMBDA_C_BAR / ELECTRON_SIZE_BOUND_M:.0e} times smaller than the model's loop.")


if __name__ == "__main__":
    main()
