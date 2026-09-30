"""
Module 06 lab: what sound really can (and cannot) organise.

Four experiments, each computed from first principles:

1. membrane_frequencies(), membrane_modes_fd()   A drum skin (Helmholtz equation): f_mn ∝ sqrt(m^2 + n^2).
2. plate_frequencies(), plate_modes_fd()         A Chladni plate is a thin *plate* (Kirchhoff biharmonic equation):
                                                 for a simply supported square plate, f_mn ∝ (m^2 + n^2).
                                                 A finite-difference eigen-solver checks both against theory.
3. gorkov_*                                      Acoustic radiation force on a small particle in a standing wave:
                                                 a conservative force F = -dU/dx that herds particles to nodes.
4. atom_scale_sound()                            Where the 2420 claim breaks: the wavelength sets the scale of
                                                 the pattern, and sound cannot be made short enough to place atoms.

Run:  python simulation.py
"""
import numpy as np
from scipy import constants as sc
from scipy.sparse import diags, identity, kron, lil_matrix
from scipy.sparse.linalg import eigsh

# Media (approximate textbook values near 20-25 °C)
RHO_AIR, C_AIR = 1.204, 343.2              # kg/m^3, m/s (dry air, 20 °C)
RHO_WATER, C_WATER = 998.0, 1482.0         # kg/m^3, m/s (20 °C)
RHO_PS, C_PS = 1050.0, 2350.0              # polystyrene bead
RHO_EPS = 25.0                             # expanded polystyrene foam (typical levitation bead), density only
RHO_LIPID, C_LIPID = 920.0, 1450.0         # lipid / fat droplet (illustrative)
RHO_GRANITE = 2700.0                       # kg/m^3
P_ATM = sc.atm                             # Pa
G_EARTH = sc.g                             # m/s^2


# ---------------------------------------------------------------- 1. membrane (drum skin)

def membrane_frequencies(m, n, L=1.0, c=1.0):
    """Fixed-edge square membrane of side L and wave speed c: f_mn = (c / 2L) sqrt(m^2 + n^2)."""
    return c / (2.0 * L) * np.sqrt(np.asarray(m, float) ** 2 + np.asarray(n, float) ** 2)


def _laplacian_dirichlet(N, h):
    """5-point Laplacian on N x N interior points with w = 0 on the boundary."""
    d2 = diags([1.0, -2.0, 1.0], [-1, 0, 1], shape=(N, N)) / h ** 2
    eye = identity(N)
    return (kron(d2, eye) + kron(eye, d2)).tocsc()


def membrane_modes_fd(N=40, L=1.0, c=1.0, k=6):
    """Lowest k frequencies of the square membrane from a finite-difference Helmholtz eigen-solve."""
    lam = eigsh(-_laplacian_dirichlet(N, L / (N + 1)), k=k, sigma=0.0, which="LM")[0]
    return np.sort(c * np.sqrt(lam) / (2.0 * np.pi))


# ---------------------------------------------------------------- 2. plate (real Chladni physics)

def plate_frequencies(m, n, L=1.0, D=1.0, rho_h=1.0):
    """Simply supported square Kirchhoff plate: omega_mn = sqrt(D / rho h) * pi^2 (m^2 + n^2) / L^2."""
    m, n = np.asarray(m, float), np.asarray(n, float)
    return np.sqrt(D / rho_h) * np.pi ** 2 * (m ** 2 + n ** 2) / L ** 2 / (2.0 * np.pi)


def biharmonic_simply_supported(N, h):
    """13-point finite-difference stencil for the biharmonic operator (nabla^4) on N x N interior nodes.

    Simply supported edges: w = 0 on the boundary and the ghost node beyond it is w_ghost = -w_mirror
    (this enforces zero bending moment, i.e. nabla^2 w = 0 on the edge).
    """
    idx = lambda i, j: i * N + j
    stencil = {(0, 0): 20.0,
               (1, 0): -8.0, (-1, 0): -8.0, (0, 1): -8.0, (0, -1): -8.0,
               (1, 1): 2.0, (1, -1): 2.0, (-1, 1): 2.0, (-1, -1): 2.0,
               (2, 0): 1.0, (-2, 0): 1.0, (0, 2): 1.0, (0, -2): 1.0}

    def reflect(p):
        """Map an index to (interior index, sign); boundary nodes (p = -1 or N) are zero."""
        if 0 <= p < N:
            return p, 1.0
        if p == -1 or p == N:
            return None, 0.0
        return (-p - 2, -1.0) if p < -1 else (2 * N - p, -1.0)   # ghost node: odd reflection

    A = lil_matrix((N * N, N * N))
    for i in range(N):
        for j in range(N):
            for (di, dj), w in stencil.items():
                pi_, si = reflect(i + di)
                pj, sj = reflect(j + dj)
                if pi_ is None or pj is None:
                    continue
                A[idx(i, j), idx(pi_, pj)] += w * si * sj
    return (A / h ** 4).tocsc()


def plate_modes_fd(N=40, L=1.0, D=1.0, rho_h=1.0, k=6):
    """Lowest k frequencies of the simply supported plate from D nabla^4 w = rho h omega^2 w."""
    lam = eigsh(biharmonic_simply_supported(N, L / (N + 1)), k=k, sigma=0.0, which="LM")[0]
    return np.sort(np.sqrt(D / rho_h * lam) / (2.0 * np.pi))


def chladni_pattern(m, n, sign=+1, N=201):
    """Displacement of the degenerate mode pair sin(m pi x) sin(n pi y) +- sin(n pi x) sin(m pi y) on [0,1]^2.

    Sand collects where this is zero (the nodal lines). Degenerate pairs are what give the star- and
    ring-like Chladni figures instead of plain checkerboards.
    """
    x = np.linspace(0.0, 1.0, N)
    X, Y = np.meshgrid(x, x, indexing="ij")
    s = np.sin
    return s(m * np.pi * X) * s(n * np.pi * Y) + sign * s(n * np.pi * X) * s(m * np.pi * Y)


# ---------------------------------------------------------------- 3. acoustic radiation force (Gor'kov)

def contrast_factors(rho_p, c_p, rho_0, c_0):
    """Gor'kov monopole f1 = 1 - kappa_p/kappa_0 and dipole f2 = 2(rho_p - rho_0)/(2 rho_p + rho_0).

    Compressibility kappa = 1 / (rho c^2). For a rigid/incompressible particle pass c_p = np.inf.
    """
    f1 = 1.0 - (rho_0 * c_0 ** 2) / (rho_p * c_p ** 2)
    f2 = 2.0 * (rho_p - rho_0) / (2.0 * rho_p + rho_0)
    return f1, f2


def acoustic_contrast(rho_p, c_p, rho_0, c_0):
    """Acoustic contrast factor Phi = f1/3 + f2/2. Phi > 0: particles go to pressure nodes."""
    f1, f2 = contrast_factors(rho_p, c_p, rho_0, c_0)
    return f1 / 3.0 + f2 / 2.0


def gorkov_potential_1d(x, R, p0, freq, rho_p, c_p, rho_0, c_0):
    """Gor'kov potential U = 2 pi R^3 [ f1 <p^2> / (3 rho0 c0^2) - f2 rho0 <v^2> / 2 ] in p = p0 cos(kx) cos(wt).

    Time averages: <p^2> = p0^2 cos^2(kx) / 2, <v^2> = p0^2 sin^2(kx) / (2 rho0^2 c0^2). Valid for R << wavelength.
    """
    k = 2.0 * np.pi * freq / c_0
    f1, f2 = contrast_factors(rho_p, c_p, rho_0, c_0)
    p2 = p0 ** 2 * np.cos(k * x) ** 2 / 2.0
    v2 = p0 ** 2 * np.sin(k * x) ** 2 / (2.0 * rho_0 ** 2 * c_0 ** 2)
    return 2.0 * np.pi * R ** 3 * (f1 * p2 / (3.0 * rho_0 * c_0 ** 2) - f2 * rho_0 * v2 / 2.0)


def gorkov_force_1d(x, R, p0, freq, rho_p, c_p, rho_0, c_0, dx=None):
    """F = -dU/dx, by central differences on the Gor'kov potential."""
    k = 2.0 * np.pi * freq / c_0
    dx = dx or 1e-6 / k
    U = lambda s: gorkov_potential_1d(s, R, p0, freq, rho_p, c_p, rho_0, c_0)
    return -(U(x + dx) - U(x - dx)) / (2.0 * dx)


def standing_wave_force_amplitude(R, p0, freq, rho_p, c_p, rho_0, c_0):
    """Closed form for the same force: F = 4 pi Phi k R^3 E_ac sin(2kx), with E_ac = p0^2 / (4 rho0 c0^2)."""
    k = 2.0 * np.pi * freq / c_0
    e_ac = p0 ** 2 / (4.0 * rho_0 * c_0 ** 2)
    return 4.0 * np.pi * acoustic_contrast(rho_p, c_p, rho_0, c_0) * k * R ** 3 * e_ac


def settle_positions(x0, R, p0, freq, rho_p, c_p, rho_0, c_0, mobility=1.0, steps=4000):
    """Overdamped motion dx/dt = mobility * F(x): where do particles end up? (dimensionless time stepping)"""
    k = 2.0 * np.pi * freq / c_0
    fmax = abs(standing_wave_force_amplitude(R, p0, freq, rho_p, c_p, rho_0, c_0))
    x = np.array(x0, dtype=float)
    dt = 0.05 / (k * mobility * fmax) if fmax > 0 else 0.0   # largest step is 0.05 / k (a small fraction of a wavelength)
    for _ in range(steps):
        x = x + dt * mobility * gorkov_force_1d(x, R, p0, freq, rho_p, c_p, rho_0, c_0)
    return x


def levitation_pressure(freq, rho_p, c_p=np.inf, rho_0=RHO_AIR, c_0=C_AIR):
    """Pressure amplitude p0 whose peak standing-wave force equals a bead's weight (independent of R for R << lambda).

    Weight (4/3) pi R^3 rho_p g = 4 pi Phi k R^3 E_ac  ->  E_ac = rho_p g / (3 Phi k).
    """
    k = 2.0 * np.pi * freq / c_0
    e_ac = rho_p * G_EARTH / (3.0 * acoustic_contrast(rho_p, c_p, rho_0, c_0) * k)
    return np.sqrt(4.0 * rho_0 * c_0 ** 2 * e_ac)


def spl_db(p_amplitude):
    """Sound pressure level (dB re 20 µPa) of a sinusoid with amplitude p (rms = p / sqrt 2)."""
    return 20.0 * np.log10(p_amplitude / np.sqrt(2.0) / 20e-6)


# ---------------------------------------------------------------- 4. where it breaks: atoms

def mean_free_path_air(T=293.15, p=P_ATM, d=3.7e-10):
    """Kinetic-theory mean free path k T / (sqrt 2 pi d^2 p) for air molecules of diameter d."""
    return sc.k * T / (np.sqrt(2.0) * np.pi * d ** 2 * p)


def atom_scale_sound(target=1e-10, c_solid=5000.0, lattice_const=5.431e-10, max_phonon_cm=520.7,
                     cohesive_ev=4.63):
    """What would it take to arrange matter atom-by-atom with sound?

    target:        feature size to control (m); an atom is ~1e-10 m.
    c_solid:       typical longitudinal sound speed in a solid (m/s).
    lattice_const: silicon lattice constant (m); shortest lattice wave is ~2 x the atomic spacing.
    max_phonon_cm: silicon's zone-centre optical phonon (Raman line), the highest phonon frequency, in cm^-1.
    cohesive_ev:   energy to pull one atom out of a silicon crystal (eV/atom, Kittel).
    Pattern features are half a wavelength apart, so the wavelength needed is 2 * target.
    """
    lam_needed = 2.0 * target
    atom_spacing = lattice_const * np.sqrt(3.0) / 4.0          # Si nearest-neighbour distance
    return {
        "target_m": target,
        "wavelength_needed_m": lam_needed,
        "freq_in_solid_Hz": c_solid / lam_needed,
        "shortest_lattice_wavelength_m": 2.0 * atom_spacing,
        "max_phonon_freq_Hz": max_phonon_cm * 100.0 * sc.c,
        "freq_in_air_Hz": C_AIR / lam_needed,
        "air_cutoff_Hz": C_AIR / mean_free_path_air(),         # no sound below ~ one mean free path
        "air_mean_free_path_m": mean_free_path_air(),
        "max_phonon_energy_eV": sc.h * max_phonon_cm * 100.0 * sc.c / sc.electron_volt,
        "cohesive_energy_eV": cohesive_ev,
    }


def main():
    print("1-2) Membrane vs plate: frequency ratios f_mn / f_11 (the two are different physics)")
    modes = [(1, 1), (1, 2), (2, 2), (1, 3), (2, 3)]
    mem = membrane_frequencies(*np.array(modes).T)
    pla = plate_frequencies(*np.array(modes).T)
    for (m, n), fm, fp in zip(modes, mem / mem[0], pla / pla[0]):
        print(f"   ({m},{n})   membrane sqrt(m^2+n^2) ratio = {fm:5.3f}    plate (m^2+n^2) ratio = {fp:5.3f}")
    fd_m, fd_p = membrane_modes_fd(), plate_modes_fd()
    ex_m = np.sort(membrane_frequencies(*np.array([(1, 1), (1, 2), (2, 1), (2, 2), (1, 3), (3, 1)]).T))
    ex_p = np.sort(plate_frequencies(*np.array([(1, 1), (1, 2), (2, 1), (2, 2), (1, 3), (3, 1)]).T))
    print(f"   Finite-difference solver (40x40 grid), worst error vs theory: membrane "
          f"{100 * np.max(np.abs(fd_m / ex_m - 1)):.2f}%, plate {100 * np.max(np.abs(fd_p / ex_p - 1)):.2f}%")
    w = chladni_pattern(1, 2, sign=-1)
    print(f"   Chladni figure (1,2)-(2,1): max |w| on the diagonal x = y is {np.max(np.abs(np.diag(w))):.1e} "
          f"(a nodal line: sand collects there)\n")

    print("3) Acoustic radiation force in a 1D standing wave (Gor'kov, R << wavelength)")
    for name, rho, c in (("polystyrene in water", RHO_PS, C_PS), ("lipid droplet in water", RHO_LIPID, C_LIPID)):
        phi = acoustic_contrast(rho, c, RHO_WATER, C_WATER)
        f = 2e6
        lam = C_WATER / f
        x_end = settle_positions(np.linspace(0.03, 0.97, 8) * lam / 2, 5e-6, 2e5, f, rho, c, RHO_WATER, C_WATER)
        cos_end = np.abs(np.cos(2 * np.pi * x_end / lam))
        where = "pressure NODES (|cos kx| = 0)" if np.all(cos_end < 1e-3) else (
            "pressure ANTINODES (|cos kx| = 1)" if np.all(cos_end > 1 - 1e-3) else "mixed")
        print(f"   {name:24s} Phi = {phi:+.3f}  -> particles settle at {where}")
    x = np.linspace(0, C_WATER / 2e6, 2001)
    Fx = gorkov_force_1d(x, 5e-6, 2e5, 2e6, RHO_PS, C_PS, RHO_WATER, C_WATER)
    work = np.trapezoid(Fx, x)
    print(f"   Work over one full wavelength: {work:.1e} J (vs peak force x wavelength "
          f"{np.max(np.abs(Fx)) * x[-1]:.1e} J): the force is conservative.")
    p_lev = levitation_pressure(40e3, RHO_EPS)
    p_ps = levitation_pressure(40e3, RHO_PS)
    print(f"   Levitating in air at 40 kHz (wavelength {1e3 * C_AIR / 40e3:.1f} mm): foam bead needs p0 = {p_lev:.0f} Pa "
          f"({spl_db(p_lev):.0f} dB), solid polystyrene {p_ps:.0f} Pa ({spl_db(p_ps):.0f} dB)")
    f_stone = C_AIR / (10 * 2.0)            # a 2 m block must be << wavelength: take wavelength = 10 x size
    p_stone = levitation_pressure(f_stone, RHO_GRANITE)
    print(f"   A 2 m granite block ({f_stone:.0f} Hz so it stays << wavelength) needs p0 = {p_stone / 1e3:.0f} kPa "
          f"= {p_stone / P_ATM:.2f} atm ({spl_db(p_stone):.0f} dB)")
    verdict = ("impossible: the pressure troughs would have to fall below vacuum" if p_stone > P_ATM
               else "possible in principle, but deep in the nonlinear (shock-wave) regime")
    print(f"   -> {verdict}\n")

    print("4) Could sound place atoms?")
    a = atom_scale_sound()
    print(f"   Wavelength needed for 0.1 nm features:    {a['wavelength_needed_m'] * 1e9:.2f} nm")
    print(f"   Frequency that requires in a solid:        {a['freq_in_solid_Hz'] / 1e12:.0f} THz")
    print(f"   Highest phonon in silicon:                 {a['max_phonon_freq_Hz'] / 1e12:.1f} THz "
          f"(a factor {a['freq_in_solid_Hz'] / a['max_phonon_freq_Hz']:.1f} too low)")
    print(f"   Shortest wave a lattice can carry:         {a['shortest_lattice_wavelength_m'] * 1e9:.2f} nm "
          f"({a['shortest_lattice_wavelength_m'] / a['wavelength_needed_m']:.1f}x longer than needed)")
    print(f"   In air: needs {a['freq_in_air_Hz']:.1e} Hz, but sound stops at ~{a['air_cutoff_Hz']:.1e} Hz "
          f"(mean free path {a['air_mean_free_path_m'] * 1e9:.0f} nm)")
    print(f"   Energy of silicon's highest phonon: {a['max_phonon_energy_eV'] * 1e3:.1f} meV vs "
          f"{a['cohesive_energy_eV']:.2f} eV binding each atom ({a['cohesive_energy_eV'] / a['max_phonon_energy_eV']:.0f}x):"
          f" vibrations ride on bonds, they do not make them.")
    spacing = C_AIR / 40e3 / 2
    print(f"   Pattern spacing is half a wavelength: {spacing * 1e3:.1f} mm at 40 kHz in air, "
          f"{spacing / a['target_m']:.0e} times coarser than an atom.")


if __name__ == "__main__":
    main()
