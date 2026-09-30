# 🔬 Module 11 — The Science Behind the Story

> The [lesson](readme.md) is told from the year 2420. This page is the 2025 reality check: what is established, where the story's claim breaks, and what would have to be true for it to work. Everything here can be checked with the [lab code](simulation.py).

## The 2420 claim in one sentence

Nuclei can be gently "refolded" into other elements at room temperature, by metal lattices, enzymes or bacteria, with no need for high energies, so gold can be grown and nuclear waste turned into fertiliser.

## Level 1 — What's real

**Transmutation is real.** Nuclei do change into other elements: in stars, in reactors, in accelerators and in radioactive decay. Mercury‑196 can even be turned into gold in a reactor: $^{196}$Hg captures a neutron to become $^{197}$Hg, which decays by electron capture to $^{197}$Au. It works, but produces tiny amounts at great cost.

**The Coulomb wall.** Two nuclei with charges $Z_1e$, $Z_2e$ repel each other with energy $Z_1Z_2e^2/(4\pi\varepsilon_0 r)$, where $e^2/4\pi\varepsilon_0 = 1.44$ MeV·fm. At touching distance ($r \approx 1.2(A_1^{1/3}+A_2^{1/3})$ fm) that is about **0.48 MeV for two deuterons** and **5.2 MeV for a proton and potassium‑39**. Room temperature gives particles about $kT = 0.026$ eV: some 20 million times too little to climb over.

**Tunnelling.** Quantum mechanics lets nuclei tunnel through the wall. For a bare Coulomb wall the probability is the Gamow factor

$$P(E) = e^{-2\pi\eta} = \exp\!\left(-\sqrt{E_G/E}\right),\qquad \eta = Z_1Z_2\,\alpha\sqrt{\frac{\mu c^2}{2E}},\qquad E_G = 2\mu c^2\,(\pi\alpha Z_1Z_2)^2 .$$

For D–D, $E_G = 0.986$ MeV (the lab reproduces Bosch and Hale's constant $\sqrt{E_G} = 31.40$ keV$^{1/2}$). Cross sections are written as

$$\sigma(E) = \frac{S(E)}{E}\,e^{-\sqrt{E_G/E}},$$

where the astrophysical S‑factor $S(E)$ is slowly varying: about 55 keV·b for each of the two main D–D branches. Averaged over a thermal gas this gives D–D reactivities within about 25 % of the published values from 2 to 10 keV (a test in the lab).

**Electron screening is real and an open research question.** Electrons around the nuclei partly cancel their repulsion. At small distances the potential looks like $e^2/r - U_e$, which boosts low‑energy cross sections by

$$f(E) \approx \exp\!\left(\pi\eta\,\frac{U_e}{E}\right)\qquad (U_e \ll E)$$

(Assenbaum, Langanke & Rolfs, 1987). For deuterium gas the expected (adiabatic) value is $U_e \approx 28$ eV. Beam experiments at keV energies on deuterium loaded into metals have reported much larger values, a few hundred eV (for example about 300 eV in tantalum; Raiola et al., 2002). Why these values are so large is still debated.

**Energy bookkeeping.** Nuclear reactions release or absorb energy $Q = (\sum m_\text{in} - \sum m_\text{out})c^2$. From measured masses: D + D → T + p releases 4.03 MeV; D + D → ³He + n releases 3.27 MeV (each about 50 % of the time); D + D → ⁴He + γ releases 23.85 MeV but happens only about once per $10^7$ fusions. K‑39 + p → Ca‑40 would release 8.33 MeV.

## Level 2 — Where the claim breaks

**1. The tunnelling numbers at room temperature.** At $E = kT = 0.026$ eV the bare D–D Gamow factor is $10^{-2682}$. Even the lab's WKB calculation with 800 eV screening gives $10^{-24}$ for a pair at thermal energy. The pair only "sees" the benefit of screening once it is already closer than the screening length, $a = e^2/U_e \approx 1800$ fm.

**2. An optimistic rate estimate.** The lab computes D–D fusion in palladium deuteride (PdD, $6.8\times10^{22}$ D/cm³) at 300 K, treating every pair as screened by $U_e$ and including the whole Maxwell tail of fast collisions. This model is deliberately generous:

| $U_e$ | Power (W/cm³) |
|---|---|
| 0 (bare) | $2\times10^{-254}$ |
| 28 eV (gas) | $9\times10^{-101}$ |
| 300 eV | $7\times10^{-19}$ |
| 800 eV | $9\times10^{-4}$ |

The result changes by a factor of about 260 for a ±10 % change in $U_e$, and 1 W/cm³ would need $U_e \approx 1050$ eV. So the answer depends entirely on whether keV‑beam screening values apply to room‑temperature deuterons, which nobody has shown. Koonin and Nauenberg (1989) calculated that the two deuterons in a D₂ molecule, only 0.74 Å apart, fuse at about $10^{-64}$ per second.

**3. The missing neutrons (the decisive test).** If the heat came from ordinary D–D fusion, half the reactions would emit a 2.45 MeV neutron. Using the Q‑values above:

$$\frac{1\ \text{W}}{\tfrac12(4.03+3.27)\ \text{MeV}} = 1.7\times10^{12}\ \text{fusions/s} \;\Rightarrow\; 8.6\times10^{11}\ \text{neutrons/s per watt}.$$

At 1 m from an unshielded 1 W source that is roughly 10 Sv per hour: a typically lethal dose in about half an hour. This is the origin of the "dead graduate student" joke. Neutron detectors can count single neutrons, so even $10^{-12}$ W of D–D fusion is measurable. The cold‑fusion experiments reported watt‑level excess heat with nothing like these neutron, tritium or gamma yields. So either the heat is not D–D fusion or it is not nuclear.

**4. The 1989 claims were not confirmed.** Fleischmann and Pons (1989) reported excess heat from palladium electrodes in heavy water. Many laboratories tried to reproduce it and could not do so reliably. A multi‑year programme by Berlinguette et al. (2019) re‑examined the main claims with careful calorimetry and found no evidence of anomalous heat or nuclear products, while noting useful materials science along the way.

**5. Chickens and bacteria.** Enzymes work with chemical energies of about 0.5 eV (for example, ATP hydrolysis). The K‑39 + p → Ca‑40 barrier is 5.2 MeV, ten million times higher, and the lab's tunnelling probability at body temperature is $10^{-49515}$. Louis Kervran's claims of biological transmutation have not been reproduced under controlled conditions. Laying hens draw calcium from food and from a special reserve in their bones; on a calcium‑poor diet, shell quality falls.

**6. "Folding" is not free.** Turning lead‑208 into gold‑197 means removing 3 protons and 8 neutrons. The masses say this costs at least 77 MeV per atom, about 10 MWh per gram of gold, before any losses. Nuclear binding energy is the reason: the pieces are held together, and taking them apart costs energy.

## Level 3 — What would have to be true

For room‑temperature transmutation to be real, all of these would have to be shown. Each is a clear, testable target:

- **Screening that works at thermal energies.** Measure low‑energy D–D yields in metals at energies approaching the eV scale and show an effective $U_e$ above roughly 1 keV that applies to deuterons at rest in the lattice.
- **Nuclear products matching the heat.** Every joule of nuclear heat must come with the right number of neutrons, tritium, ³He, ⁴He or gamma rays. Measure them in the same run, with blind analysis.
- **A mechanism that changes the branching.** If there are no neutrons, some new physics must send the energy into the lattice instead of into fast particles, and it must be predicted in advance and then observed.
- **Independent replication** by labs that did not design the original experiment, with open data.

**Open research questions that are real:** why measured screening energies in metals are so large; how hydrogen behaves in metal lattices (important for hydrogen storage and embrittlement); and low‑energy nuclear cross sections for stellar astrophysics, measured deep underground (for example at LUNA in Italy).

## Run the lab

```bash
python Module_11_Low_Energy_Transmutation/simulation.py
python -m pytest tests/test_module_11.py
```

| Experiment | What it shows |
|---|---|
| `coulomb_barrier`, `gamow_energy`, `gamow_factor` | The Coulomb wall and the bare tunnelling probability, checked against Bosch–Hale's $\sqrt{E_G}$. |
| `wkb_exponent`, `screening_enhancement` | Numerical WKB tunnelling through a screened wall; it reproduces the analytic Gamow and Assenbaum results in their limits. |
| `dd_reactivity_cm3_s`, `fusion_power_density` | Thermal D–D rates (matching published values at keV) and an optimistic room‑temperature estimate for PdD. |
| `q_value`, `neutrons_per_watt`, `dose_rate_sv_per_hour` | Q‑values from measured masses and the neutron flux that 1 W of D–D fusion would produce. |
| `transmutation_cost_mev` | The minimum energy cost of lead → gold. |

## Try it yourself

1. Use `screening_needed` to find the $U_e$ that would give 1 mW/cm³, and compare it with the ~300 eV measured in tantalum.
2. Change `temp_k` in `fusion_power_density` to 600 K. How much does doubling the temperature help compared with a 10 % increase in $U_e$?
3. Compute the neutron dose rate at 3 m from a 0.1 W source. How thick would a water shield need to be? (Look up the attenuation length of fast neutrons in water.)
4. Use `q_value` to check whether ¹²C + ¹²C → ²⁴Mg releases energy, then use `coulomb_barrier` and `gamow_energy` to see why it only happens inside massive stars.

## References

- Gamow, G., "Zur Quantentheorie des Atomkernes", *Z. Phys.* **51**, 204 (1928).
- Assenbaum, H. J., Langanke, K. & Rolfs, C., "Effects of electron screening on low‑energy fusion cross sections", *Z. Phys. A* **327**, 461 (1987).
- Bosch, H.‑S. & Hale, G. M., "Improved formulas for fusion cross‑sections and thermal reactivities", *Nucl. Fusion* **32**, 611 (1992).
- Raiola, F. et al., "Enhanced electron screening in d(d,p)t for deuterated Ta", *Eur. Phys. J. A* **13**, 377 (2002).
- Koonin, S. E. & Nauenberg, M., "Calculated fusion rates in isotopic hydrogen molecules", *Nature* **339**, 690 (1989).
- Fleischmann, M., Pons, S. & Hawkins, M., "Electrochemically induced nuclear fusion of deuterium", *J. Electroanal. Chem.* **261**, 301 (1989).
- Berlinguette, C. P. et al., "Revisiting the cold case of cold fusion", *Nature* **570**, 45 (2019).
- Wang, M. et al., "The AME 2020 atomic mass evaluation (II)", *Chinese Phys. C* **45**, 030003 (2021). Source of the atomic masses.
- ICRP Publication 74, *Conversion Coefficients for use in Radiological Protection against External Radiation* (1996). Source of the approximate neutron dose coefficient.
- Huba, J. D., *NRL Plasma Formulary* (Naval Research Laboratory, revised regularly). Tabulated D–D reactivities used in the tests.
