# 🔬 Module 9 — The Science Behind the Story

> The [lesson](readme.md) is told from the year 2420. This page is the 2025 reality check: what is established, where the story's claim breaks, and what would have to be true for it to work. Everything here can be checked with the [lab code](simulation.py).

## The 2420 claim in one sentence

Two invisible "scalar" (longitudinal) beams that pass harmlessly through the Earth can be crossed anywhere in the sky to create instant hot or cold pockets, and a grid of those pockets steers storms and the jet stream electrically.

## Level 1 — What's real

**The atmosphere really is an electric circuit.** The ionosphere sits at roughly $+250$ kV relative to the ground. In fair weather this drives a tiny downward current, about $2$ pA/m², through weakly conducting air, with a surface field of about $100$–$130$ V/m. Thunderstorms around the world act as the battery that keeps it charged. The lab turns these typical values into totals:

| Quantity | How it is computed | Lab value |
|---|---|---|
| Total current | $J \times 4\pi R_\oplus^2$ | ≈ 1 kA |
| Power | $V_\text{ion} \times I$ | ≈ 250 MW |
| Earth's surface charge | $\varepsilon_0 E \times 4\pi R_\oplus^2$ (Gauss) | ≈ $5\times10^5$ C |
| Air conductivity at the ground | $J/E$ | ≈ $2\times10^{-14}$ S/m |
| Discharge time without storms | $\varepsilon_0/\sigma$ | ≈ 9 minutes |

**Electricity can push air.** Ions accelerated in a strong field drag neutral molecules along: this is the "ionic wind" or electrohydrodynamic thrust. For a current $I$ crossing a gap $d$ with ion mobility $\mu$, the one‑dimensional thrust is $T = I d/\mu$, so the thrust per watt is $T/P = d/(\mu V)$. MIT flew a 5 m‑span aeroplane with no moving parts on this principle (Xu et al., 2018).

**Clouds form on particles, and theory says exactly when.** Water does not condense on its own at the humidities found in air. It condenses on tiny particles (cloud condensation nuclei), such as sea salt. Köhler theory (1936) gives the equilibrium saturation ratio over a solution droplet of radius $r$ containing salt mass $m_s$:

$$S(r) = a_w \exp\!\left(\frac{A}{r}\right) \;\approx\; 1 + \frac{A}{r} - \frac{B}{r^3}, \qquad A = \frac{2\sigma M_w}{R T \rho_w},\quad B = \frac{3\, i\, m_s M_w}{4\pi \rho_w M_s}.$$

The curvature (Kelvin) term $A/r$ makes small droplets evaporate; the dissolved salt (Raoult) term $B/r^3$ lowers the vapour pressure. The curve has a peak at

$$r_c = \sqrt{3B/A}, \qquad S_c - 1 = \sqrt{\frac{4A^3}{27B}} \;\propto\; m_s^{-1/2}.$$

The lab finds the peak of the full expression numerically and confirms $S_c - 1 \propto m_s^{-1/2}$ and $r_c \propto m_s^{1/2}$. For NaCl ($i \approx 2$) it gives:

| Dry diameter | Critical supersaturation | Cross‑check: κ‑Köhler with measured κ = 1.28 |
|---|---|---|
| 20 nm | 1.14 % | 1.16 % |
| 50 nm | 0.29 % | 0.29 % |
| 100 nm | 0.10 % | 0.10 % |
| 200 nm | 0.036 % | 0.037 % |

Below the peak the droplet is a stable **haze** particle. Haze exists well below 100 % humidity: a salt crystal dissolves (deliquesces) at about 75 % RH, and the lab computes 75.5 % from the solution's water activity. Only when the air's supersaturation exceeds $S_c$ does the droplet grow without limit and become a cloud droplet ("activation"). Real clouds rarely exceed about 1 % supersaturation, which is why the particle population, not the voltage, decides where droplets form.

**Ions do help make new particles.** Charge stabilises small molecular clusters. The CERN CLOUD experiment (Kirkby et al., 2011) showed that ionisation from cosmic rays measurably increases the rate at which sulfuric‑acid–ammonia particles form. Those particles are nanometres across and must grow for hours to days before they are large enough to seed clouds.

**Cloud seeding is real but modest.** Silver iodide seeding of suitable winter clouds over mountains has been directly observed to produce extra snowfall (French et al., 2018). Over whole seasons and regions the effect is small and hard to prove statistically.

**HAARP is real.** It is an ionospheric research facility in Alaska whose high‑frequency transmitter has 3.6 MW of power. It heats small patches of the ionosphere, far above the weather (weather lives in the lowest ~15 km). There is no demonstrated effect on weather.

**Focusing is real.** A magnifying glass makes a hot spot because it gathers light from a large area into a small one. Two crossed beams also make bright and dark fringes where they interfere.

## Level 2 — Where the claim breaks

**1. There are no longitudinal radio waves in empty space.** In vacuum Gauss's law reads $\nabla\cdot\mathbf E = 0$. For a wave $\mathbf E_0 e^{i\mathbf k\cdot\mathbf x}$ that means $\mathbf k\cdot\mathbf E_0 = 0$: the field must be perpendicular to the direction of travel. The "scalar" and longitudinal parts of the potentials can be changed by a gauge transformation without changing any measurable field, and they carry no energy. Whittaker (1903) showed that fields can be *written* in terms of two scalar functions. This is a mathematical rewriting of ordinary electromagnetism, not a new kind of wave. Longitudinal electric waves do exist inside plasmas (Langmuir waves), but they need the plasma to exist and do not cross rock or ocean.

**2. Radio waves do not pass through the Earth.** Conductors absorb electromagnetic waves within a skin depth $\delta \approx \sqrt{2/(\omega\mu_0\sigma)}$. The lab uses the exact formula:

| Frequency | Seawater ($\sigma$ = 4 S/m) | Rock ($\sigma$ = 10⁻³ S/m) |
|---|---|---|
| 10 Hz | 80 m | 5 km |
| 1 kHz | 8 m | 500 m |
| 1 MHz | 0.25 m | 21 m |

After 1000 km of rock, even a 10 Hz wave keeps a fraction $e^{-199} \approx 10^{-87}$ of its amplitude. This is why submarines are contacted with extremely low frequencies and huge antennas, and even then only near the surface.

**3. Crossing beams moves energy; it cannot create it or remove it.** Where two coherent beams of intensity $I_1$ and $I_2$ overlap, the time‑averaged intensity is

$$I = I_1 + I_2 + 2\sqrt{I_1 I_2}\cos\Delta\phi .$$

Dark fringes are always paired with bright ones, and the average over the pattern is exactly $I_1 + I_2$. The lab checks both. A "cold mode" in which the crossing point sucks heat out of the air would need negative intensity. Cooling air means pumping its heat somewhere else, which takes work and must dump even more heat nearby (the second law of thermodynamics). The magnifying glass cannot make a cold spot, either.

**4. The weather is enormously more powerful than any electrical lever.** Weather is driven by sunlight ($\approx 1.2\times10^{17}$ W absorbed by Earth) and by the latent heat released when water vapour condenses:

| Energy source or sink | Lab value |
|---|---|
| One thunderstorm (2 cm of rain over a 5 km radius) | ≈ $4\times10^{15}$ J |
| Average hurricane (1.5 cm/day of rain over a 665 km radius, NOAA's method) | ≈ $6\times10^{14}$ W |
| Warming the air over 100 km × 100 km by just 1 K | ≈ $10^{17}$ J |
| The entire global electric circuit | ≈ $2.5\times10^{8}$ W |
| HAARP transmitter | $3.6\times10^{6}$ W |
| A large ground ion array (100 kV × 1 mA) | 100 W |

At 100 W, the 1 K warming would take about 30 million years. Even if all of HAARP's power were absorbed in the lower atmosphere (it is not), it would take about 900 years. A hurricane outpowers the ion array by a factor of about $6\times10^{12}$. The ion wind from that array is a push of about 0.25 N, the weight of a 25 g object, applied to weather systems that contain billions of tonnes of moving air.

**5. Ions cannot make clouds directly.** Thomson's theory of droplet formation on a charge adds an electrostatic term to the classical free energy of a pure water droplet:

$$\Delta G(r) = -\tfrac43\pi r^3 n_l k T\ln S \;+\; 4\pi r^2\sigma \;+\; \frac{q^2}{8\pi\varepsilon_0}\left(1-\frac{1}{\varepsilon_r}\right)\left(\frac1r - \frac1{r_0}\right).$$

For $S \le 1$ the bulk term is positive, so $\Delta G$ has no maximum and no critical radius exists: droplets never grow, charged or not. For $S > 1$ the charge lowers the barrier, but the lab finds that the barrier only drops to ~60 kT (roughly one droplet per cm³ per second) at $S \approx 4.1$ for neutral clusters and $S \approx 2.5$ with one elementary charge. C. T. R. Wilson's cloud chambers of the 1890s found the same kind of number: ions trigger droplets only at supersaturations of a few hundred percent. At a realistic $S = 1.01$ the barrier is over $10^6$ kT. In real air, salt and other particles activate at less than 1 % supersaturation, long before ions matter. (Continuum theory is rough for clusters only a few molecules across; the ordering, not the exact digits, is robust.)

**6. Ground ionisers for rain.** Several commercial projects have claimed rain enhancement from arrays of ground‑based ionisers. The evidence published so far is weak and disputed: small claimed effects, no independent randomised trials, and no accepted mechanism that gets from extra ions to extra rain at realistic supersaturations.

**7. "A wall of air as hard as concrete."** At constant pressure, cooling air by 30 K raises its density by only about 10 % ($\rho \propto 1/T$). No temperature change makes air behave like a solid to a missile.

## Level 3 — What would have to be true

- **A new, long‑range field** that propagates through rock and ocean with negligible loss, is not an ordinary electromagnetic wave, and couples strongly to air. It would also show up in precision tests of electromagnetism. A photon with a tiny mass would have a longitudinal mode, but laboratory and astrophysical upper limits on the photon mass are extraordinarily small (the Particle Data Group lists bounds of order $10^{-18}$ eV).
- **An energy source to match the weather**: at least $10^{15}$–$10^{17}$ J per event, delivered in hours. That is the entire output of a 1 GW power station running for days to years, which would have to be beamed into the sky without heating anything on the way.
- **Testable targets**: a controlled, randomised experiment in which a device (ioniser array, beam or otherwise) produces a statistically significant change in rainfall or pressure compared with untreated control days, replicated by independent groups. That is the standard applied to cloud seeding, and the reason its measured effects are described as modest.
- **Open questions that are real science**: how much ions from cosmic rays affect cloud cover (CLOUD's results suggest the effect on today's climate is small); how the global electric circuit responds to changing thunderstorm activity; how to make EHD propulsion more efficient.

## Run the lab

```bash
python Module_09_Weather_Engineering/simulation.py
python -m pytest tests/test_module_09.py
```

| Experiment | What it shows |
|---|---|
| `global_circuit` | Current, power, charge and conductivity of Earth's fair‑weather circuit. |
| `saturation_ratio`, `critical_point`, `equilibrium_radius` | Köhler theory: haze below 100 % RH, activation above $S_c$, $S_c - 1 \propto m_s^{-1/2}$. |
| `deliquescence_rh` | Why salt crystals dissolve at ~75 % RH (and why the ideal‑solution answer is too high). |
| `thomson_free_energy`, `nucleation_barrier`, `saturation_for_barrier` | Ions lower the nucleation barrier, but only at supersaturations far beyond real clouds. |
| `ion_wind_thrust`, `thrust_per_power` | Ion wind is real but produces tiny forces. |
| `rain_latent_heat`, `hurricane_heat_power`, `column_heating_energy` | The weather's energy budget vs every electrical lever. |
| `crossed_beams`, `skin_depth` | Interference redistributes energy; radio waves die within metres to kilometres in the ground and sea. |

## Try it yourself

1. Use `critical_point` to find the dry NaCl diameter that activates at exactly 0.5 % supersaturation. Then check your answer with `kappa_critical_saturation`.
2. Plot `saturation_ratio` for a 50 nm particle from its dry radius to 10 μm (use any plotting tool you like). Mark the haze branch, the peak and the activated branch.
3. Change `eps_r` in `thomson_free_energy` from 80 to 1. What happens to the benefit of the charge, and why?
4. How many 1 GW power stations, running for one day, would it take to match the latent heat of the lab's thunderstorm?
5. Using `skin_depth`, find the frequency at which a wave loses only half its amplitude in 100 m of seawater. How long would an antenna for that frequency need to be (take a quarter wavelength)?

## References

- Köhler, H., "The nucleus in and the growth of hygroscopic droplets", *Trans. Faraday Soc.* **32**, 1152 (1936).
- Petters, M. D. & Kreidenweis, S. M., "A single parameter representation of hygroscopic growth and cloud condensation nucleus activity", *Atmos. Chem. Phys.* **7**, 1961 (2007).
- Pruppacher, H. R. & Klett, J. D., *Microphysics of Clouds and Precipitation*, 2nd ed., Kluwer (1997). Köhler and Thomson theory, ion‑induced nucleation.
- Rogers, R. R. & Yau, M. K., *A Short Course in Cloud Physics*, 3rd ed., Pergamon (1989).
- Seinfeld, J. H. & Pandis, S. N., *Atmospheric Chemistry and Physics*, 3rd ed., Wiley (2016). Deliquescence and CCN activation.
- Robinson, R. A. & Stokes, R. H., *Electrolyte Solutions*, 2nd ed., Butterworths (1959). Osmotic coefficients of NaCl solutions.
- Kirkby, J. et al., "Role of sulphuric acid, ammonia and galactic cosmic rays in atmospheric aerosol nucleation", *Nature* **476**, 429 (2011).
- Rycroft, M. J., Israelsson, S. & Price, C., "The global atmospheric electric circuit, solar activity and climate change", *J. Atmos. Sol.‑Terr. Phys.* **62**, 1563 (2000).
- Xu, H. et al., "Flight of an aeroplane with solid‑state propulsion", *Nature* **563**, 532 (2018).
- French, J. R. et al., "Precipitation formation from orographic cloud seeding", *Proc. Natl. Acad. Sci. USA* **115**, 1168 (2018).
- Whittaker, E. T., "On the partial differential equations of mathematical physics", *Math. Ann.* **57**, 333 (1903).
- Jackson, J. D., *Classical Electrodynamics*, 3rd ed., Wiley (1999). Transversality of vacuum waves, skin depth.
- Kopp, G. & Lean, J. L., "A new, lower value of total solar irradiance: Evidence and climate significance", *Geophys. Res. Lett.* **38**, L01706 (2011).
- NOAA Atlantic Oceanographic and Meteorological Laboratory, Hurricane Research Division, *Hurricane FAQ* ("How much energy does a hurricane release?"). Source of the rainfall‑based heat‑release method.
