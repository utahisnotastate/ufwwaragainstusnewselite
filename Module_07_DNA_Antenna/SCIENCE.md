# 🔬 Module 7 — The Science Behind the Story

> The [lesson](readme.md) is told from the year 2420. This page is the 2025 reality check: what is established, where the story's claim breaks, and what would have to be true for it to work. Everything here can be checked with the [lab code](simulation.py).

## The 2420 claim in one sentence

DNA is a coil‑shaped antenna that receives instructions from an information field, including your own thoughts and feelings, and rewrites the body to match.

## Level 1 — What's real

**DNA's shape is known precisely.** B‑DNA, the form found in cells, is a right‑handed double helix (Watson & Crick 1953; Franklin & Gosling 1953) with

- a diameter of about **2.0 nm**,
- a rise of **0.34 nm** per base pair,
- about **10.5 base pairs per turn** in solution (34.3° of twist per step), so a pitch of **3.4–3.6 nm**.

It is also stiff over short distances: its persistence length is about 50 nm in physiological salt.

**DNA really does interact with light, strongly, in the ultraviolet.** DNA absorbs most strongly near **260 nm** (4.77 eV per photon). The everyday lab rule "an absorbance of 1 at 260 nm means 50 µg/mL of double‑stranded DNA" gives about **6600 M⁻¹cm⁻¹ per nucleotide**. The double helix absorbs roughly 30–40 % less than the same bases as free nucleotides (the lab gets 39 % using approximate textbook nucleotide values). This **hypochromism** happens because stacked bases couple electronically. After UV excitation, the excitation can be shared across several stacked bases, and the stacking controls how fast the energy is dissipated (Crespo‑Hernández, Cohen & Kohler 2005). This is real, fast physics, and it helps protect DNA from UV damage. It works over a few bases, a few nanometres.

**Energy can hop along DNA, over nanometres.** Förster resonance energy transfer (FRET) moves an excitation from a donor dye to an acceptor with efficiency

$$E = \frac{1}{1 + (r/R_0)^6},$$

where $R_0$ is typically about 5 nm. Placed along a DNA helix, dyes 15 base pairs apart (5.1 nm) transfer about half their energy; at 30 base pairs it is about 1 %. This steep $r^{-6}$ fall‑off is why FRET is used as a "spectroscopic ruler" (Stryer & Haugland 1967), often with DNA itself as the ruler.

**DNA vibrates and "breathes".** The Peyrard–Bishop model (1989) treats each base pair as a stretch $y_n$ held by a Morse potential $V(y) = D\,(e^{-ay} - 1)^2$ (the hydrogen bonds) and coupled to its neighbours by stacking springs:

$$H = \sum_n \left[\frac{p_n^2}{2m} + \frac{k}{2}(y_n - y_{n-1})^2 + D\,(e^{-a y_n} - 1)^2\right].$$

Small oscillations form a phonon band, $m\omega^2 = 2Da^2 + 4k\sin^2(q/2)$, in the terahertz range. The lab checks this against a numerical Hessian. The lab also solves the model's thermodynamics exactly with the transfer‑integral method: base pairs open a little more as temperature rises, and above a threshold the strands come apart (denaturation, or "melting"). With the illustrative harmonic‑stacking parameters used here, that happens near 490 K, well above real DNA's 340–370 K. Dauxois, Peyrard & Bishop (1993) showed that adding nonlinear stacking gives the sharp melting seen in experiments. The point is qualitative: DNA's dynamics are ordinary thermal physics.

**Genes are regulated by the environment, through chemistry.** Epigenetic marks (DNA methylation, histone modifications) change which genes are expressed. They respond to diet, hormones and experience; in rats, for example, maternal care changes methylation of a stress‑hormone receptor gene in the offspring (Weaver et al. 2004). The signals are molecules: hormones, transcription factors and enzymes.

**About "junk DNA".** About 1–2 % of the human genome codes for proteins. Regulatory elements (promoters, enhancers) and non‑coding RNAs are real and important. The ENCODE project (2012) reported "biochemical function" for 80 % of the genome, but that definition counted any biochemical activity, such as being transcribed once or being bound by a protein. It was strongly contested, for example by Graur et al. (2013), who argued that function should mean something selection preserves. The share of the genome under evolutionary constraint is estimated to be far lower.

## Level 2 — Where the claim breaks

**1. If DNA were an antenna, it would be tuned to X‑rays, not thoughts or biophotons.** A helical antenna radiates along its axis (Kraus's "axial mode") when its circumference $C$ satisfies $\tfrac34 < C/\lambda < \tfrac43$. For B‑DNA, $C = \pi \times 2.0\text{ nm} = 6.3$ nm, so

$$\lambda \approx 4.7\text{–}8.4\text{ nm} \quad (150\text{–}260\text{ eV}),$$

which is extreme ultraviolet or soft X‑ray light, and it ionises molecules. The ultraweak "biophoton" emission reported from living tissue (200–800 nm; see Cifra & Pospíšil 2014) is **30–130 times too long**. Its pitch angle (30°) is also outside Kraus's best range of 12–14°. On top of that, DNA is not a metal wire: its backbone does not carry free electrons the way an antenna does.

**2. Biophotons are far too few to carry instructions.** Even a generous 100 photons per second per cm², all aimed at DNA, would hit a given helical turn about **once every 4400 years**.

**3. Salt water screens and absorbs.** Cells are salty water. At 150 mM the **Debye screening length** is

$$\lambda_D = \sqrt{\frac{\varepsilon_r\varepsilon_0 k_B T}{2 N_A e^2 I}} \approx \frac{0.304}{\sqrt{I\,[\text{M}]}}\ \text{nm} \approx 0.78\text{ nm}.$$

A charge's electrostatic field is already down to a few parts per million 10 nm away. Oscillating fields do get through, but a Debye‑relaxation model of saline water (conductivity about 1.6 S/m) shows that microwaves fall to $1/e$ within about **2.6 cm at 1 GHz, 2.4 mm at 10 GHz and 0.24 mm at 100 GHz**. A 50 nm stiff DNA segment acting as a 1 GHz dipole would have a radiation resistance of about $10^{-11}\ \Omega$, compared with about 50 Ω for a working antenna. It is an extraordinarily poor antenna.

**4. Radio photons are too weak to do chemistry.** A 1 GHz photon carries $1.5\times10^{-4}\,k_BT$ at body temperature. Molecules are jostled by thousands of times more energy every picosecond. That is why UV (178 $k_BT$ per photon at 260 nm) damages DNA and radio does not.

**5. The "phantom leaf" and "mitogenetic radiation" stories.** Controlled studies of corona‑discharge (Kirlian) photography found that the images depend strongly on moisture, pressure and exposure conditions (Pehek, Kyler & Faust 1976). The "phantom leaf" is not an established effect. Gurwitsch's mitogenetic radiation and Kaznacheyev's "cytopathic transfer" claims were not established by independent replication.

**6. There is no evidence that DNA receives "morphogenetic instructions" from a field.** How bodies take shape is studied in detail, and it works through genes, proteins, gradients of signalling molecules, and mechanical and electrical cues between cells. Your feelings really can affect your body, through nerves, hormones and the immune system, and epigenetics is part of that story. But the messengers are molecules, not a broadcast.

## Level 3 — What would have to be true

To make "DNA as an antenna" a scientific hypothesis, someone would need to show all of these:

- **A receiver that works in salt water.** Either a signal frequency that penetrates tissue *and* couples to a 2 nm helix, or a mechanism (for example, a molecular resonance) that is not washed out by screening and thermal noise. A measurable test: a specific frequency that changes gene expression in a cell culture, with a dose–response curve, blinding and independent replication.
- **Enough energy per signal.** Changing DNA chemistry needs energies near an electronvolt per event, or an amplifier inside the cell that turns a tiny signal into a big response while beating $k_BT$ noise.
- **A carrier for "information from the field".** The story needs a named physical field with a measurable strength and a predicted spectrum. As written, it predicts no number that could be checked.

The open questions nearby are real and interesting: how far charge can travel along DNA (a few nanometres, by hopping between stacked bases), how UV energy is shared among stacked bases, how DNA "breathing" helps proteins read it, and how much of the non‑coding genome matters.

## Run the lab

```bash
python Module_07_DNA_Antenna/simulation.py
python -m pytest tests/test_module_07.py
```

| Experiment | What it shows |
|---|---|
| `b_dna_geometry`, `helical_antenna_band`, `biophoton_mismatch` | A DNA‑sized helix would be tuned to ~6 nm (EUV/soft X‑ray), 30–130× shorter than biophotons. |
| `photon_hits_per_turn` | Biophoton fluxes are vanishingly small at the molecular scale. |
| `uv_absorption` | ~6600 M⁻¹cm⁻¹ per nucleotide at 260 nm and ~39 % hypochromism from stacking. |
| `fret_efficiency`, `fret_along_dna` | Energy transfer along DNA: 50 % at ~15 bp, ~1 % at 30 bp. |
| `pb_mode_frequencies_numeric`, `pb_dispersion`, `pb_transfer_integral` | Peyrard–Bishop vibrations (THz) and thermal opening and denaturation. |
| `debye_length`, `water_permittivity`, `field_penetration_depth` | 0.78 nm screening; microwaves absorbed within mm–cm. |
| `short_dipole_radiation_resistance`, `rf_photon_vs_thermal` | DNA is a hopeless RF antenna; radio photons are ≪ $k_BT$. |

## Try it yourself

1. Use `debye_length` to find the salt concentration at which the screening length would reach 1 µm. Could a living cell survive in water that pure?
2. Change `R0_nm` in `fret_along_dna` to 3 nm and 7 nm. How many base pairs does the 50 % point move?
3. In `pb_transfer_integral`, double `D`. How does the unbinding temperature from `pb_denaturation_temperature` change? Compare with `pb_continuum_estimate`, which scales as $\sqrt{kD}$.
4. The human genome in one cell is about $6.4\times10^9$ base pairs (both copies). Use `RISE_NM` to find the total length of DNA in one cell. If it were a straight half‑wave dipole in vacuum, what frequency would it be tuned to, and how far would that frequency travel in saline (`field_penetration_depth`)?
5. Find the frequency where `rf_photon_vs_thermal` equals 1 at body temperature. What part of the spectrum is that?

## References

- Watson, J. D. & Crick, F. H. C., "Molecular structure of nucleic acids", *Nature* **171**, 737 (1953).
- Franklin, R. E. & Gosling, R. G., "Molecular configuration in sodium thymonucleate", *Nature* **171**, 740 (1953).
- Kraus, J. D., *Antennas*, 2nd ed., McGraw‑Hill (1988). Helical antenna modes.
- Crespo‑Hernández, C. E., Cohen, B. & Kohler, B., "Base stacking controls excited‑state dynamics in A·T DNA", *Nature* **436**, 1141 (2005).
- Cavaluzzi, M. J. & Borer, P. N., "Revised UV extinction coefficients for nucleoside‑5′‑monophosphates and unpaired DNA and RNA", *Nucleic Acids Res.* **32**, e13 (2004).
- Förster, T., "Zwischenmolekulare Energiewanderung und Fluoreszenz", *Ann. Phys.* **437**, 55 (1948).
- Stryer, L. & Haugland, R. P., "Energy transfer: a spectroscopic ruler", *Proc. Natl. Acad. Sci. USA* **58**, 719 (1967).
- Peyrard, M. & Bishop, A. R., "Statistical mechanics of a nonlinear model for DNA denaturation", *Phys. Rev. Lett.* **62**, 2755 (1989).
- Dauxois, T., Peyrard, M. & Bishop, A. R., "Entropy‑driven DNA denaturation", *Phys. Rev. E* **47**, R44 (1993).
- Israelachvili, J. N., *Intermolecular and Surface Forces*, 3rd ed., Academic Press (2011). Debye length.
- Kaatze, U., "Complex permittivity of water as a function of frequency and temperature", *J. Chem. Eng. Data* **34**, 371 (1989).
- Cifra, M. & Pospíšil, P., "Ultra‑weak photon emission from biological samples: definition, mechanisms, properties, detection and applications", *J. Photochem. Photobiol. B* **139**, 2 (2014).
- Pehek, J. O., Kyler, H. J. & Faust, D. L., "Image modulation in corona discharge photography", *Science* **194**, 263 (1976).
- Weaver, I. C. G. et al., "Epigenetic programming by maternal behavior", *Nat. Neurosci.* **7**, 847 (2004).
- ENCODE Project Consortium, "An integrated encyclopedia of DNA elements in the human genome", *Nature* **489**, 57 (2012).
- Graur, D. et al., "On the immortality of television sets: 'function' in the human genome according to the evolution‑free gospel of ENCODE", *Genome Biol. Evol.* **5**, 578 (2013).
