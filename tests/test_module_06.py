import numpy as np
import pytest

FOLDER = "Module_06_Language_of_Reality"

LOWEST_SIX = np.array([(1, 1), (1, 2), (2, 1), (2, 2), (1, 3), (3, 1)])


# ---------------------------------------------------------------- membrane vs plate

def test_membrane_fundamental(sim):
    assert sim.membrane_frequencies(1, 1, L=2.0, c=340.0) == pytest.approx(340.0 / 4.0 * np.sqrt(2))


def test_membrane_fd_matches_sqrt_law(sim):
    exact = np.sort(sim.membrane_frequencies(*LOWEST_SIX.T))
    assert np.allclose(sim.membrane_modes_fd(N=40), exact, rtol=5e-3)


def test_plate_fd_matches_m2_plus_n2_law(sim):
    exact = np.sort(sim.plate_frequencies(*LOWEST_SIX.T))
    assert np.allclose(sim.plate_modes_fd(N=40), exact, rtol=1e-2)


def test_plate_fd_converges_at_second_order(sim):
    exact = sim.plate_frequencies(1, 1)
    e20 = abs(sim.plate_modes_fd(N=19, k=1)[0] / exact - 1)
    e40 = abs(sim.plate_modes_fd(N=39, k=1)[0] / exact - 1)   # h halves exactly (h = 1/(N+1))
    assert e40 == pytest.approx(e20 / 4, rel=0.1)


def test_plate_and_membrane_ratios_differ(sim):
    """The testable lesson: f21/f11 is sqrt(5/2) for a drum skin but 5/2 for a plate."""
    fd_mem, fd_pla = sim.membrane_modes_fd(N=40, k=2), sim.plate_modes_fd(N=40, k=2)
    assert fd_mem[1] / fd_mem[0] == pytest.approx(np.sqrt(2.5), rel=5e-3)
    assert fd_pla[1] / fd_pla[0] == pytest.approx(2.5, rel=1e-2)


def test_plate_frequency_scaling_with_size_and_stiffness(sim):
    f = sim.plate_frequencies(2, 3, L=1.0, D=4.0)
    assert sim.plate_frequencies(2, 3, L=2.0, D=4.0) == pytest.approx(f / 4)   # f ∝ 1/L^2 (membrane: 1/L)
    assert sim.plate_frequencies(2, 3, L=1.0, D=16.0) == pytest.approx(2 * f)  # f ∝ sqrt(D)


def test_biharmonic_stencil_is_symmetric_and_positive(sim):
    A = sim.biharmonic_simply_supported(12, 1.0 / 13)
    assert abs(A - A.T).max() < 1e-9
    assert np.linalg.eigvalsh(A.toarray()).min() > 0


def test_chladni_antisymmetric_pair_has_diagonal_nodal_line(sim):
    w = sim.chladni_pattern(1, 2, sign=-1)
    assert np.max(np.abs(np.diag(w))) < 1e-12
    w_plus = sim.chladni_pattern(1, 2, sign=+1)
    assert np.max(np.abs(np.diag(w_plus))) > 0.5          # the '+' pair is NOT zero on the diagonal


# ---------------------------------------------------------------- Gor'kov radiation force

W = dict(rho_0=998.0, c_0=1482.0)


def test_contrast_factor_limits(sim):
    f1, f2 = sim.contrast_factors(998.0, 1482.0, **W)       # particle identical to the fluid
    assert f1 == pytest.approx(0) and f2 == pytest.approx(0)
    f1, f2 = sim.contrast_factors(1e9, np.inf, 1.2, 343.0)   # rigid, very dense sphere in air
    assert f1 == pytest.approx(1.0) and f2 == pytest.approx(1.0, abs=1e-6)
    assert sim.acoustic_contrast(1e9, np.inf, 1.2, 343.0) == pytest.approx(5 / 6, abs=1e-6)


def test_gradient_of_gorkov_matches_closed_form_force(sim):
    R, p0, f = 5e-6, 2e5, 2e6
    k = 2 * np.pi * f / W["c_0"]
    x = np.linspace(0.01, 1.3, 50) / k
    F_num = sim.gorkov_force_1d(x, R, p0, f, 1050.0, 2350.0, **W)
    F_amp = sim.standing_wave_force_amplitude(R, p0, f, 1050.0, 2350.0, **W)
    assert np.allclose(F_num, F_amp * np.sin(2 * k * x), rtol=1e-5, atol=1e-6 * abs(F_amp))


def test_force_is_conservative_zero_net_work_over_wavelength(sim):
    f = 2e6
    x = np.linspace(0, W["c_0"] / f, 4001)
    F = sim.gorkov_force_1d(x, 5e-6, 2e5, f, 1050.0, 2350.0, **W)
    assert abs(np.trapezoid(F, x)) < 1e-6 * np.max(np.abs(F)) * x[-1]


def test_force_scales_as_R3_and_p0_squared(sim):
    args = (1050.0, 2350.0, W["rho_0"], W["c_0"])
    F = sim.standing_wave_force_amplitude(5e-6, 1e5, 2e6, *args)
    assert sim.standing_wave_force_amplitude(1e-5, 1e5, 2e6, *args) == pytest.approx(8 * F)
    assert sim.standing_wave_force_amplitude(5e-6, 2e5, 2e6, *args) == pytest.approx(4 * F)


def test_positive_contrast_goes_to_nodes_negative_to_antinodes(sim):
    f = 2e6
    lam = W["c_0"] / f
    x0 = np.linspace(0.03, 0.97, 8) * lam / 2
    ps = sim.settle_positions(x0, 5e-6, 2e5, f, 1050.0, 2350.0, **W)
    lipid = sim.settle_positions(x0, 5e-6, 2e5, f, 920.0, 1450.0, **W)
    assert sim.acoustic_contrast(1050.0, 2350.0, **W) > 0 > sim.acoustic_contrast(920.0, 1450.0, **W)
    assert np.allclose(np.cos(2 * np.pi * ps / lam), 0, atol=1e-3)            # pressure nodes
    assert np.allclose(np.abs(np.cos(2 * np.pi * lipid / lam)), 1, atol=1e-3)  # pressure antinodes


def test_levitation_pressure_balances_weight(sim):
    rho_p, f = 1050.0, 40e3
    p0 = sim.levitation_pressure(f, rho_p)
    R = 1e-3
    F = sim.standing_wave_force_amplitude(R, p0, f, rho_p, np.inf, sim.RHO_AIR, sim.C_AIR)
    assert F == pytest.approx(4 / 3 * np.pi * R ** 3 * rho_p * sim.G_EARTH)
    assert 150 < sim.spl_db(p0) < 165          # standing-wave levitators run at roughly this level


def test_spl_reference(sim):
    assert sim.spl_db(20e-6 * np.sqrt(2)) == pytest.approx(0.0)


# ---------------------------------------------------------------- where it breaks

def test_air_mean_free_path(sim):
    assert sim.mean_free_path_air() == pytest.approx(66e-9, rel=0.1)    # textbook ~ 65-68 nm at STP


def test_atoms_need_wavelengths_matter_cannot_carry(sim):
    a = sim.atom_scale_sound()
    assert a["freq_in_solid_Hz"] > 1e13                                  # tens of THz
    assert a["max_phonon_freq_Hz"] == pytest.approx(15.6e12, rel=0.01)  # Si Raman line, 520.7 cm^-1
    assert a["freq_in_solid_Hz"] > a["max_phonon_freq_Hz"]
    assert a["shortest_lattice_wavelength_m"] > a["wavelength_needed_m"]
    assert a["freq_in_air_Hz"] > 100 * a["air_cutoff_Hz"]
    assert a["max_phonon_energy_eV"] == pytest.approx(0.0645, rel=0.01)  # h c x 520.7 cm^-1
    assert a["cohesive_energy_eV"] > 50 * a["max_phonon_energy_eV"]


def test_stone_levitation_needs_more_than_an_atmosphere(sim):
    f = sim.C_AIR / 20.0                       # wavelength 10x a 2 m block
    assert sim.levitation_pressure(f, sim.RHO_GRANITE) > sim.P_ATM
