import numpy as np
import pytest

FOLDER = "Module_09_Weather_Engineering"


# ---------------------------------------------------------------- global circuit

def test_global_circuit_matches_textbook_totals(sim):
    gc = sim.global_circuit()
    assert 800 < gc["current_A"] < 1500              # ~1 kA
    assert 150e6 < gc["power_W"] < 400e6             # a few hundred MW
    assert 150 < gc["resistance_ohm"] < 350          # ~200-300 ohm column resistance
    assert 3e5 < gc["earth_charge_C"] < 8e5          # ~5e5 C
    assert 100 < gc["relaxation_time_s"] < 1000      # minutes: storms must keep recharging it


def test_global_circuit_ohm_and_gauss(sim):
    gc = sim.global_circuit(potential=100e3, field=100.0, current_density=1e-12)
    area = 4 * np.pi * sim.R_EARTH ** 2
    assert gc["current_A"] * gc["resistance_ohm"] == pytest.approx(100e3)
    assert gc["earth_charge_C"] == pytest.approx(sim.EPS0 * 100.0 * area)


# ---------------------------------------------------------------- Koehler

def test_kelvin_length_is_about_a_nanometre(sim):
    assert sim.kelvin_A() == pytest.approx(1.05e-9, rel=0.03)


def test_pure_water_droplet_follows_kelvin(sim):
    r = 1e-7
    assert float(sim.saturation_ratio(r, 1e-30)) == pytest.approx(np.exp(sim.kelvin_A() / r), rel=1e-6)


def test_full_and_approximate_koehler_agree_for_dilute_droplets(sim):
    m = sim.salt_mass_from_dry_diameter(100e-9)
    r_num, S_num = sim.critical_point(m)
    r_an, S_an = sim.critical_point_analytic(m)
    assert r_num == pytest.approx(r_an, rel=0.02)
    assert (S_num - 1) == pytest.approx(S_an - 1, rel=0.03)


def test_critical_supersaturation_scales_as_inverse_root_salt_mass(sim):
    masses = np.logspace(-19, -16, 7)
    pts = [sim.critical_point(m) for m in masses]
    slope_s = np.polyfit(np.log(masses), np.log([s - 1 for _, s in pts]), 1)[0]
    slope_r = np.polyfit(np.log(masses), np.log([r for r, _ in pts]), 1)[0]
    assert slope_s == pytest.approx(-0.5, abs=0.02)
    assert slope_r == pytest.approx(0.5, abs=0.02)


def test_typical_ccn_activate_between_0p1_and_1_percent(sim):
    for D in (25e-9, 50e-9, 100e-9):
        _, S_c = sim.critical_point(sim.salt_mass_from_dry_diameter(D))
        assert 0.001 <= S_c - 1 <= 0.01


def test_agrees_with_published_kappa_for_nacl(sim):
    """i = 2 ideal Koehler vs kappa-Koehler with the measured kappa = 1.28 (Petters & Kreidenweis 2007)."""
    for D in (40e-9, 100e-9, 200e-9):
        _, S_c = sim.critical_point(sim.salt_mass_from_dry_diameter(D))
        assert (S_c - 1) == pytest.approx(sim.kappa_critical_saturation(D) - 1, rel=0.08)


def test_haze_exists_below_saturation_and_grows_with_humidity(sim):
    m = sim.salt_mass_from_dry_diameter(100e-9)
    radii = [sim.equilibrium_radius(S, m) for S in (0.8, 0.9, 0.95, 0.99, 1.0)]
    assert all(r is not None for r in radii)
    assert all(b > a for a, b in zip(radii, radii[1:]))
    assert radii[0] > sim.dry_radius(m)                           # wet particle is bigger than the crystal
    r = radii[1]                                                 # stable branch: dS/dr > 0
    assert float(sim.saturation_ratio(r * 1.01, m) - sim.saturation_ratio(r * 0.99, m)) > 0


def test_no_stable_droplet_above_critical_supersaturation(sim):
    m = sim.salt_mass_from_dry_diameter(100e-9)
    _, S_c = sim.critical_point(m)
    assert sim.equilibrium_radius(S_c * 0.9999, m) is not None
    assert sim.equilibrium_radius(S_c * 1.0001, m) is None


def test_deliquescence_near_75_percent(sim):
    assert sim.deliquescence_rh() == pytest.approx(0.753, abs=0.01)
    assert sim.deliquescence_rh(osmotic_coeff=1.0) > 0.79          # ideal solution misses by ~5 points


# ---------------------------------------------------------------- Thomson nucleation

def test_neutral_barrier_matches_classical_nucleation_theory(sim):
    for S in (2.0, 4.0):
        b_num, r_num = sim.nucleation_barrier(S, charge=0.0)
        b_an, r_an = sim.neutral_barrier_analytic(S)
        assert b_num == pytest.approx(b_an, rel=1e-4)
        assert r_num == pytest.approx(r_an, rel=1e-4)


def test_no_critical_radius_below_saturation(sim):
    for S in (0.5, 0.9, 1.0):
        for q in (0.0, sim.E_CHARGE):
            barrier, r_c = sim.nucleation_barrier(S, charge=q)
            assert barrier == np.inf and r_c is None
    r = np.logspace(-9, -6, 200)
    assert np.all(np.diff(sim.thomson_free_energy(r, 0.9, charge=0.0)) > 0)


def test_charge_lowers_the_barrier(sim):
    for S in (1.5, 2.0, 3.0):
        assert sim.nucleation_barrier(S, sim.E_CHARGE)[0] < sim.nucleation_barrier(S, 0.0)[0]


def test_homogeneous_nucleation_needs_about_fourfold_supersaturation(sim):
    s_neutral = sim.saturation_for_barrier(60.0, charge=0.0)
    s_ion = sim.saturation_for_barrier(60.0, charge=sim.E_CHARGE)
    assert 3.5 < s_neutral < 5.0
    assert 1.5 < s_ion < s_neutral
    kT = sim.K_B * sim.T_COLD
    assert sim.nucleation_barrier(1.01, sim.E_CHARGE)[0] / kT > 1e5   # hopeless at cloud supersaturations


# ---------------------------------------------------------------- ion wind and energy

def test_ion_wind_thrust_scaling(sim):
    assert sim.ion_wind_thrust(1e-3, 0.1) == pytest.approx(2 * sim.ion_wind_thrust(1e-3, 0.05))
    assert sim.thrust_per_power(20e3, 0.05) == pytest.approx(2 * sim.thrust_per_power(40e3, 0.05))
    assert 1e-3 < sim.thrust_per_power(40e3, 0.05) < 2e-2          # a few N/kW


def test_hurricane_heat_release(sim):
    assert sim.hurricane_heat_power() == pytest.approx(6.0e14, rel=0.05)


def test_ion_array_is_hopelessly_small(sim):
    array_power = 100e3 * 1e-3
    assert sim.hurricane_heat_power() / array_power > 1e12
    assert sim.rain_latent_heat(0.02, 5e3) > 1e15
    assert sim.global_circuit()["power_W"] < 1e-5 * sim.solar_power_absorbed()


def test_column_heating_and_solar_power(sim):
    assert sim.column_heating_energy(1.0, 1.0) == pytest.approx(1.037e7, rel=0.01)   # ~1e4 kg/m^2 of air
    assert sim.solar_power_absorbed() == pytest.approx(1.2e17, rel=0.03)


# ---------------------------------------------------------------- beams and skin depth

def test_interference_conserves_energy_and_is_never_negative(sim):
    ph = np.linspace(0, 2 * np.pi, 4001)[:-1]
    for I1, I2 in [(1.0, 1.0), (1.0, 0.25), (3.0, 0.1)]:
        I = sim.crossed_beams(ph, I1, I2)
        assert I.min() >= -1e-12
        assert I.mean() == pytest.approx(I1 + I2, rel=1e-9)


def test_skin_depth_good_conductor_limit(sim):
    for f, s in [(10.0, 4.0), (1e3, 4.0), (100.0, 1e-2)]:
        good = np.sqrt(2 / (2 * np.pi * f * sim.MU0 * s))
        assert float(sim.skin_depth(f, s, 81.0)) == pytest.approx(good, rel=1e-3)
    assert float(sim.skin_depth(1e3, 4.0, 81.0)) == pytest.approx(7.96, rel=0.01)    # seawater, 1 kHz


def test_skin_depth_frequency_scaling(sim):
    assert float(sim.skin_depth(10.0, 4.0) / sim.skin_depth(1000.0, 4.0)) == pytest.approx(10.0, rel=1e-3)
