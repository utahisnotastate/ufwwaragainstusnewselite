import numpy as np
import pytest

FOLDER = "Module_11_Low_Energy_Transmutation"


# ---------------------------------------------------------------- Coulomb wall and Gamow factor

def test_coulomb_constant_is_1_44_MeV_fm(sim):
    assert sim.E2 == pytest.approx(1.439964, rel=1e-5)


def test_dd_gamow_energy_matches_bosch_hale_constant(sim):
    # Bosch & Hale (1992) give B_G = 31.3970 keV^1/2 for D(d,n) and D(d,p), i.e. E_G = B_G^2.
    assert np.sqrt(sim.gamow_energy() * 1e3) == pytest.approx(31.397, abs=0.01)
    assert sim.gamow_energy() == pytest.approx(0.986, abs=0.001)


def test_two_pi_eta_equals_sqrt_gamow_ratio(sim):
    for e in (1e-6, 1e-3, 0.1):
        assert 2 * np.pi * sim.sommerfeld(e) == pytest.approx(np.sqrt(sim.gamow_energy() / e))


def test_gamow_energy_scales_with_charges_squared_and_mass(sim):
    base = sim.gamow_energy(1, 1, 1000.0)
    assert sim.gamow_energy(2, 3, 1000.0) / base == pytest.approx(36.0)
    assert sim.gamow_energy(1, 1, 2000.0) / base == pytest.approx(2.0)


def test_dd_contact_barrier_is_a_few_hundred_keV(sim):
    assert 0.35 < sim.coulomb_barrier(1, 1, 2, 2) < 0.6
    # barrier grows with Z1*Z2
    assert sim.coulomb_barrier(19, 1, 39, 1) > 10 * sim.coulomb_barrier(1, 1, 2, 2)


def test_gamow_factor_limits(sim):
    assert sim.gamow_factor(1e6) == pytest.approx(1.0, abs=1e-3)       # far above the barrier
    assert sim.gamow_factor(1e-6) < 1e-300 or sim.gamow_factor(1e-6) == 0.0
    e = np.logspace(-4, 0, 20)
    assert np.all(np.diff(sim.gamow_factor(e)) > 0)


# ---------------------------------------------------------------- WKB and screening

@pytest.mark.parametrize("e", [1e-5, 1e-3, 0.05])
def test_wkb_reproduces_analytic_bare_coulomb(sim, e):
    assert sim.wkb_exponent(e) == pytest.approx(np.sqrt(sim.gamow_energy() / e), rel=1e-6)


def test_wkb_with_nuclear_radius_matches_closed_form(sim):
    e, r_n = 0.01, 3.0
    r_t = sim.E2 / e
    x = r_n / r_t
    closed = 2 * np.sqrt(2 * sim.MU_DD * e) / sim.HBARC * r_t * (np.arccos(np.sqrt(x)) - np.sqrt(x * (1 - x)))
    assert sim.wkb_exponent(e, r_nuc=r_n) == pytest.approx(closed, rel=1e-6)


def test_huge_screening_length_approaches_bare_coulomb(sim):
    e = 1e-3
    assert sim.wkb_exponent(e, a_fm=1e9) == pytest.approx(sim.wkb_exponent(e), rel=1e-4)


def test_screening_always_helps_and_more_screening_helps_more(sim):
    e = 1e-3
    g = [sim.wkb_exponent(e, sim.screening_length(u * 1e-6)) for u in (10.0, 100.0, 1000.0)]
    assert g[0] > g[1] > g[2]
    assert sim.wkb_exponent(e) > g[0]


def test_assenbaum_formula_matches_wkb_when_screening_is_small(sim):
    """For U_e << E, ln f = pi eta U_e / E should equal the drop in the WKB exponent."""
    e, u = 0.05, 100e-6
    drop = sim.wkb_exponent(e) - sim.wkb_exponent(e, sim.screening_length(u))
    assert np.log(sim.screening_enhancement(e, u)) == pytest.approx(drop, rel=0.03)


def test_screening_length_for_adiabatic_dd(sim):
    # U_e = 28 eV corresponds to a ~0.5 Angstrom (51,000 fm) screening length
    assert sim.screening_length(28e-6) == pytest.approx(5.14e4, rel=0.01)


# ---------------------------------------------------------------- rates

@pytest.mark.parametrize("t_kev, published", [(2.0, 5.4e-21), (5.0, 1.8e-19), (10.0, 1.2e-18)])
def test_thermal_dd_reactivity_matches_published_values(sim, t_kev, published):
    """NRL Plasma Formulary D-D reactivities (both branches); constant S is good to ~25% here."""
    temp = t_kev * 1e3 / sim.K_B_EV
    assert sim.dd_reactivity_cm3_s(temp) == pytest.approx(published, rel=0.3)


def test_unscreened_room_temperature_fusion_is_negligible(sim):
    assert sim.fusion_power_density(0.0) < 1e-200
    assert sim.fusion_power_density(28.0) < 1e-80


def test_fusion_power_scales_as_loading_squared(sim):
    assert sim.fusion_power_density(500.0, loading=0.5) / sim.fusion_power_density(500.0) == pytest.approx(0.25)


def test_fusion_power_is_extremely_sensitive_to_screening(sim):
    assert sim.fusion_power_density(880.0) / sim.fusion_power_density(720.0) > 50


# ---------------------------------------------------------------- Q values and neutrons

def test_dd_q_values_from_masses(sim):
    assert sim.q_value(["H2", "H2"], ["H3", "H1"]) == pytest.approx(4.03, abs=0.01)
    assert sim.q_value(["H2", "H2"], ["He3", "n"]) == pytest.approx(3.27, abs=0.01)
    assert sim.q_value(["H2", "H2"], ["He4"]) == pytest.approx(23.85, abs=0.01)


def test_one_watt_of_dd_fusion_gives_about_1e12_neutrons(sim):
    assert sim.neutrons_per_watt() == pytest.approx(8.55e11, rel=0.01)


def test_dose_rate_falls_as_inverse_square(sim):
    assert sim.dose_rate_sv_per_hour(1.0, 1.0) / sim.dose_rate_sv_per_hour(1.0, 2.0) == pytest.approx(4.0)
    assert sim.dose_rate_sv_per_hour(1.0, 1.0) > 1.0      # > 1 Sv/h at 1 m from 1 W


def test_potassium_to_calcium_is_exothermic_but_blocked(sim):
    assert sim.q_value(["K39", "H1"], ["Ca40"]) == pytest.approx(8.33, abs=0.01)
    assert sim.coulomb_barrier(19, 1, 39, 1) > 4.0


def test_lead_to_gold_costs_energy(sim):
    cost = sim.transmutation_cost_mev("Pb208", "Au197", 3, 8)
    assert 70 < cost < 85
    assert sim.energy_per_gram(1.0, 1.0) == pytest.approx(9.648e10, rel=1e-3)   # 1 MeV per atom, 1 g/mol
