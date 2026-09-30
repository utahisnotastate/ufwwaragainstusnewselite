# 🔬 Module 6 — The Science Behind the Story

> The [lesson](readme.md) is told from the year 2420. This page is the 2025 reality check: what is established, where the story's claim breaks, and what would have to be true for it to work. Everything here can be checked with the [lab code](simulation.py).

## The 2420 claim in one sentence

All shapes in nature are "frozen sound": a standing wave arranges matter the way a violin bow arranges sand on a plate, so the right sound can build matter, dissolve it, or make a stone weightless.

## Level 1 — What's real

**Chladni figures are real, and they are beautiful physics.** Ernst Chladni (1787) bowed sand‑covered metal plates and found that the sand collects along the **nodal lines**, where the plate does not move. Each note gives a different figure. What sets the figures is the equation of motion of the plate.

**A drum skin and a plate obey different equations.** A stretched membrane (a drum skin) obeys the wave (Helmholtz) equation, $\nabla^2 w + k^2 w = 0$. A fixed‑edge square membrane of side $L$ has frequencies

$$f_{mn} = \frac{c}{2L}\sqrt{m^2+n^2}.$$

A Chladni plate is a thin, stiff **plate**, governed by the Kirchhoff biharmonic equation

$$D\,\nabla^4 w - \rho h\,\omega^2 w = 0, \qquad D = \frac{E h^3}{12(1-\nu^2)} .$$

For a simply supported square plate the exact answer is $\omega_{mn} = \sqrt{D/\rho h}\;\pi^2 (m^2+n^2)/L^2$, so $f_{mn} \propto m^2 + n^2$, **not** $\sqrt{m^2+n^2}$. That is a real, testable lesson: the (1,2) mode sits at $\sqrt{5/2} = 1.58$ times the fundamental on a drum, but at $5/2 = 2.5$ times on a plate. The lab solves both equations numerically (a 5‑point Helmholtz stencil and a 13‑point biharmonic stencil) and matches the exact results to better than 0.5 %, with the expected second‑order convergence.

When two modes have the same frequency (for example (1,2) and (2,1) on a square), the plate vibrates in a mixture, $\sin m\pi x\,\sin n\pi y \pm \sin n\pi x\,\sin m\pi y$. These mixtures produce the diagonals, rings and stars of real Chladni figures; the lab checks that the "−" mixture has a nodal line exactly on the diagonal. Chladni's own free‑edge plates are harder to solve (Leissa 1969 collects the classic results). For circular plates, **Chladni's law** $f \approx C\,(m + 2n)^p$, with $m$ nodal diameters, $n$ nodal circles and $p \approx 2$ for flat plates, is a good empirical rule (Rossing 1982).

**Sound really can push, trap and levitate small objects.** A standing wave exerts a steady **acoustic radiation force** on a particle much smaller than the wavelength. Gor'kov (1962) showed it comes from a potential,

$$U = 2\pi R^3\left[\frac{f_1\,\langle p^2\rangle}{3\rho_0 c_0^2} - \frac{f_2\,\rho_0\langle v^2\rangle}{2}\right], \qquad \mathbf F = -\nabla U,$$

$$f_1 = 1 - \frac{\kappa_p}{\kappa_0}, \qquad f_2 = \frac{2(\rho_p-\rho_0)}{2\rho_p+\rho_0} .$$

Because $\mathbf F = -\nabla U$, this force is **conservative** (an earlier draft of this module called it non‑conservative, which was wrong): no net work is done carrying a particle around a closed path, and particles settle at the minima of $U$. In a 1D standing wave $p = p_0\cos kx\cos\omega t$ it becomes $F = 4\pi\Phi\,kR^3 E_\text{ac}\sin 2kx$, with contrast factor $\Phi = f_1/3 + f_2/2$ and energy density $E_\text{ac} = p_0^2/4\rho_0 c_0^2$ (Bruus 2012). The lab checks the numerical gradient of $U$ against this formula, shows zero net work over a wavelength, and lets particles drift:

- polystyrene in water ($\Phi = +0.22$) collects at **pressure nodes**,
- a lipid droplet in water ($\Phi = -0.07$) collects at **pressure antinodes**.

This is the working principle of acoustofluidic cell sorters and of **acoustic levitators**. Marzo et al. (2015) built holographic acoustic tweezers from arrays of 40 kHz transducers that levitate and move millimetre beads in air. The lab estimates the pressure needed: about 280 Pa (140 dB) for a foam bead and about 1.8 kPa (156 dB) for solid polystyrene, independent of bead size as long as the bead is much smaller than the 8.6 mm wavelength.

**Snowflakes are hexagonal for a real reason, but it isn't sound.** Ordinary ice (ice Ih) has a hexagonal crystal lattice set by the geometry of hydrogen bonds between water molecules. The six‑fold shape of a snow crystal comes from that lattice and from how vapour diffuses onto it (Libbrecht 2005).

## Level 2 — Where the claim breaks

**1. The pattern scale is the wavelength.** Sound can only organise matter on the scale of half a wavelength: 4.3 mm at 40 kHz in air. To place individual atoms (~0.1 nm) you would need a 0.2 nm wavelength. The lab shows why that is impossible:

| Medium | Frequency needed | Limit |
|---|---|---|
| Solid ($c \approx 5$ km/s) | ~25 THz | Silicon's highest vibration is 15.6 THz, and the shortest wave a lattice can carry is twice the atomic spacing, 0.47 nm. |
| Air | ~1.7 × 10¹² Hz | Sound does not exist below the molecular mean free path (~66 nm), which caps it near 5 GHz. |

At the atomic scale, "sound" (phonons) is the atoms themselves jiggling. It cannot be a template that places them.

**2. Vibrations ride on bonds; they don't make them.** Silicon's highest phonon carries 65 meV. Removing one atom from the crystal costs 4.63 eV, about 70 times more. What holds matter together is the quantum mechanics of electrons (chemical bonds), not a sustaining tone.

**3. Big stones can't be sung into the air.** The Gor'kov formula only applies to objects much smaller than the wavelength. For a 2 m block, the wavelength must be tens of metres (about 17 Hz). Holding up granite at that frequency needs a pressure amplitude of 1.4 atmospheres: the low‑pressure half of each cycle would have to fall **below vacuum**, which air cannot do. Nothing in acoustics makes an object "forget it is heavy". Phase conjugation, or "time‑reversed acoustics", is real (Fink 1997), but it refocuses waves back onto their source. It does not cancel weight.

**4. The theory names don't hold up.** "Formon theory" (Bearden) is **not a recognised theory in physics**: it has no peer‑reviewed formulation or experimental support. "Scalar sound that pushes spacetime" has no counterpart in physics. Longitudinal waves are just ordinary sound (in air, all sound is longitudinal), and they push matter, not spacetime. Hans Jenny's *Cymatics* (1967) is a lovely photographic record of vibration patterns, but it does not show that matter is "frozen sound".

## Level 3 — What would have to be true

For "building matter with sound" to be more than a metaphor, it would need all of these:

- **A wave with an atomic‑scale wavelength that is not made of the atoms it arranges.** Light and electron beams do have wavelengths this short. That is why optical tweezers, electron microscopes and scanning‑probe "atom writing" work, and they do it through electromagnetism, not sound.
- **Energy per quantum comparable to bond energies (eV).** Only then could a wave make or break bonds directly. Sound quanta top out at tens of meV.
- **A quantitative prediction.** For example, a specific frequency that measurably changes a crystal's structure or a stone's weight, which a lab could then test. None has been published.

Real, open frontiers are more modest and still exciting: acoustic holograms that assemble many particles at once, acoustic manipulation of cells and tissues, and phononic crystals engineered to steer sound and heat.

## Run the lab

```bash
python Module_06_Language_of_Reality/simulation.py
python -m pytest tests/test_module_06.py
```

| Experiment | What it shows |
|---|---|
| `membrane_frequencies`, `membrane_modes_fd` | Drum skin: $f \propto \sqrt{m^2+n^2}$, confirmed by a finite‑difference solve. |
| `plate_frequencies`, `plate_modes_fd`, `biharmonic_simply_supported` | Plate: $f \propto m^2+n^2$, confirmed by a 13‑point biharmonic solve. |
| `chladni_pattern` | Degenerate mode mixtures and their nodal lines (where sand collects). |
| `gorkov_potential_1d`, `gorkov_force_1d`, `settle_positions` | Conservative radiation force; positive contrast goes to nodes, negative to antinodes. |
| `levitation_pressure`, `spl_db` | 140–156 dB levitates beads; a stone needs "below‑vacuum" pressures. |
| `atom_scale_sound`, `mean_free_path_air` | Why sound cannot place atoms. |

## Try it yourself

1. In `biharmonic_simply_supported`, change the ghost‑node sign from $-1$ to $+1$. This turns the edges from "simply supported" to "clamped". What happens to $f_{21}/f_{11}$? (Clamped plates are closer to real bells and cymbals.)
2. Plot `chladni_pattern(1, 3, sign=+1)` and `sign=-1` as images (use any plotting tool) and mark where $|w|$ is small. Which one looks more like a Chladni figure you've seen?
3. Use `levitation_pressure` to find the frequency at which a 1 mm water droplet can be levitated with 150 dB. Is the droplet still much smaller than the wavelength?
4. Repeat `atom_scale_sound` for diamond, whose sound speed is about 18 km/s and whose highest phonon is about 1332 cm⁻¹. Does it get closer to "placing atoms"?
5. Compute $\Phi$ for red blood cells in plasma (look up approximate densities and sound speeds). Would they go to nodes or antinodes?

## References

- Chladni, E. F. F., *Entdeckungen über die Theorie des Klanges*, Leipzig (1787).
- Leissa, A. W., *Vibration of Plates*, NASA SP‑160 (1969).
- Fletcher, N. H. & Rossing, T. D., *The Physics of Musical Instruments*, 2nd ed., Springer (1998). Plate modes and Chladni patterns.
- Rossing, T. D., "Chladni's law for vibrating plates", *Am. J. Phys.* **50**, 271 (1982).
- Gor'kov, L. P., "On the forces acting on a small particle in an acoustical field in an ideal fluid", *Sov. Phys. Dokl.* **6**, 773 (1962).
- Bruus, H., "Acoustofluidics 7: The acoustic radiation force on small particles", *Lab Chip* **12**, 1014 (2012).
- Marzo, A. et al., "Holographic acoustic elements for manipulation of levitated objects", *Nat. Commun.* **6**, 8661 (2015).
- Fink, M., "Time reversed acoustics", *Physics Today* **50**(3), 34 (1997).
- Libbrecht, K. G., "The physics of snow crystals", *Rep. Prog. Phys.* **68**, 855 (2005).
- Kittel, C., *Introduction to Solid State Physics*, 8th ed., Wiley (2005). Cohesive energies and phonons.
- Jenny, H., *Kymatik / Cymatics*, Basilius Presse (1967).
