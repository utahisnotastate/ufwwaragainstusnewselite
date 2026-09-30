# 🔬 Module 1 — The Science Behind the Story

> The [lesson](readme.md) is told from the year 2420. This page is the 2025 reality check: what is established, where the story's claim breaks, and what would have to be true for it to work. Everything here can be checked with the [lab code](simulation.py).

## The 2420 claim in one sentence

Empty space is a high‑pressure "ocean" of zero‑point energy, and an engine only has to open a valve in it to get free power.

## Level 1 — What's real

**The vacuum is not "nothing".** Quantum mechanics says a harmonic oscillator can never be perfectly still: its lowest energy is $E_0 = \tfrac12\hbar\omega$, not zero. The electromagnetic field is a collection of such oscillators, one per mode, so even with every photon removed each mode keeps its $\tfrac12\hbar\omega$. This zero‑point energy is part of standard physics, and it has measurable consequences (the Lamb shift, spontaneous emission, and the one below).

**The Casimir effect.** Put two parallel uncharged mirrors a distance $d$ apart. Only modes that fit between them survive inside, while all modes exist outside. The difference in zero‑point energy gives an attraction. For perfect mirrors (Casimir, 1948):

$$\frac{E}{A} = -\frac{\pi^2\hbar c}{720\,d^3}, \qquad P = -\frac{\partial (E/A)}{\partial d} = -\frac{\pi^2\hbar c}{240\,d^4}.$$

The lab evaluates these with CODATA constants: $P \approx -1.30\times10^{-3}$ Pa at $d = 1\ \mu$m and $\approx -13$ Pa at 100 nm. It reaches one atmosphere only at about 11 nm. The force has been measured, first convincingly by Lamoreaux (1997, sphere–plate, 0.6–6 µm), then with an AFM by Mohideen & Roy (1998) and between parallel plates by Bressi et al. (2002).

**Real mirrors.** Real metals stop reflecting at frequencies above their plasma frequency $\omega_p$, so the ideal formula overestimates the force at short range. Lifshitz theory (1956) handles real materials. At zero temperature, for two identical half‑spaces,

$$\frac{E}{A} = \frac{\hbar}{4\pi^2}\int_0^\infty d\xi\int_0^\infty k\,dk \sum_{\mathrm{TE,TM}} \ln\!\left(1 - r^2 e^{-2\kappa d}\right), \qquad \kappa = \sqrt{k^2 + \xi^2/c^2},$$

with Fresnel coefficients evaluated at imaginary frequency $i\xi$:

$$r_{\mathrm{TE}} = \frac{\kappa - K}{\kappa + K},\qquad r_{\mathrm{TM}} = \frac{\varepsilon\kappa - K}{\varepsilon\kappa + K},\qquad K = \sqrt{k^2 + \varepsilon(i\xi)\,\xi^2/c^2}.$$

For gold the lab uses the Drude model $\varepsilon(i\xi) = 1 + \omega_p^2/[\xi(\xi+\gamma)]$ with $\hbar\omega_p = 9.0$ eV and $\hbar\gamma = 35$ meV. The integrator is checked three ways: with $r = 1$ it reproduces Casimir's closed forms to $10^{-6}$; its pressure equals $-\partial(E/A)/\partial d$; and at sub‑nanometre gaps it turns into non‑retarded van der Waals attraction, $E/A \to -A_H/(12\pi d^2)$, with a Hamaker constant $A_H \approx 2.1\times10^{-19}$ J that matches an independent one‑dimensional integral to 0.1 %.

| $d$ | gold / perfect mirror |
|---|---|
| 10 nm | 0.08 |
| 100 nm | 0.44 |
| 1 µm | 0.88 |
| 10 µm | 0.98 |

## Level 2 — Where the claim breaks

**1. Zero‑point energy is the floor, not a reservoir.** It is the energy of the *ground state*, the lowest state the field can be in. Extracting energy means going to a lower state, and there isn't one. The submarine analogy fails at exactly this point: sea water can flow in because the inside of the submarine is at lower pressure. Nothing can be at "lower pressure" than the vacuum's ground state.

**2. A Casimir cavity is a spring, not a well.** The force depends only on position, so it is conservative. You can get work once by letting the plates snap together, but you must pay the same work to pull them apart. The lab integrates the force around a closed cycle (1 µm → 100 nm → 1 µm), using different sampling grids for the two strokes so the answer isn't built in:

| Plates (1 m²) | work gained moving in | work paid moving out | net |
|---|---|---|---|
| perfect mirrors | $+4.33\times10^{-7}$ J | $-4.33\times10^{-7}$ J | $\sim10^{-13}$ J (quadrature error, $\sim10^{-6}$ of a stroke) |
| gold | $+2.24\times10^{-7}$ J | $-2.24\times10^{-7}$ J | $\sim10^{-13}$ J |

Even the one‑way collapse is small. A square metre of perfect mirrors falling from 1 µm to 10 nm gives at most $4.3\times10^{-4}$ J. An AA battery holds about $10^4$ J.

**3. Moving mirrors make light, but the energy comes from the motor.** The dynamical Casimir effect is real. Wilson et al. (2011) modulated the effective length of a superconducting circuit at gigahertz frequencies and detected photon pairs coming out of the vacuum. Each pair's energy adds up to one quantum of the drive ($\hbar\omega_1 + \hbar\omega_2 = \hbar\omega_\text{drive}$), so the power out comes from the pump. It is a way to *convert* energy, not to find it.

**4. The "10⁹⁵ g/cm³" ocean is contradicted by gravity.** The story's number comes from the Planck density $c^5/(\hbar G^2) \approx 5\times10^{96}$ kg/m³ $\approx 5\times10^{93}$ g/cm³, which is what you get by summing $\tfrac12\hbar\omega$ over modes up to the Planck length. Energy gravitates, and the vacuum energy that the expansion of the universe actually shows (dark energy) is only

$$\rho_\Lambda c^2 = \Omega_\Lambda\,\frac{3H_0^2c^2}{8\pi G} \approx 5\times10^{-10}\ \text{J/m}^3.$$

The naive estimate, $\hbar c\,k_\text{max}^4/(16\pi^2)$ with $k_\text{max} = 1/\ell_P$, is about $3\times10^{111}$ J/m³. That is a mismatch of **~10¹²¹**, the *cosmological constant problem* (Weinberg, 1989). This is an open problem, but it points the opposite way from the story: whatever the vacuum does, it does not act like an enormous reservoir.

**5. The vacuum does not push like water.** A Lorentz‑invariant vacuum energy has pressure $p = -\rho c^2$, a tension rather than a crushing pressure. The same in every frame and every direction, it has no gradient, and only a gradient gives a force. The Casimir force exists because the plates change the mode structure, and it vanishes when the plates are removed.

The in‑universe "proof" also says Fermi's weak‑interaction theory fails at high energies "if space's contribution is ignored". Fermi theory does break down (around a few hundred GeV). It was repaired by the electroweak theory, whose predicted W and Z bosons were found at CERN in 1983, not by vacuum energy extraction.

## Level 3 — What would have to be true

For a vacuum engine to work, at least one of these would have to be discovered. Each is testable:

- **A state below the vacuum.** Any system that gives net energy from "the vacuum" in a closed cycle would be a lower‑energy state than the ground state. Precision Casimir experiments measure forces at the 1 % level. A cycle that returns net work would show up as a hysteresis loop in force versus distance. None has been seen.
- **Non‑conservative Casimir forces.** A force that depended on the direction of motion (not just on position) at zero temperature would be new physics. Friction‑like "quantum friction" between surfaces sliding sideways is predicted but tiny, and it still takes energy *from* the motion.
- **A resolution of the cosmological constant problem that leaves huge usable energy.** Candidate solutions (supersymmetric cancellations, anthropic selection, modified gravity) make the effective vacuum energy small. None makes it large and accessible.

Open questions that remain real and interesting: why the observed vacuum energy is so small but not zero; whether Casimir forces can be made repulsive for practical nano‑machines (they can in some media: Munday, Capasso & Parsegian, *Nature* **457**, 170 (2009)); and how temperature and material response combine at micrometre scales, still an active debate.

## Run the lab

```bash
python Module_01_Zero_Point_Energy/simulation.py
python -m pytest tests/test_module_01.py
```

| Experiment | What it shows |
|---|---|
| `casimir_pressure_ideal`, `casimir_energy_ideal` | Casimir's closed forms: the vacuum really pushes, strongly only at nanometres. |
| `lifshitz_pressure`, `lifshitz_energy`, `gold_reduction_factor` | Real gold plates by numerical integration over imaginary frequency; weaker than ideal, approaching it at micrometres. |
| `hamaker_constant` | Independent check of the short‑range (van der Waals) limit. |
| `closed_cycle_work`, `one_shot_energy` | A closed cycle nets zero work; one‑way collapse gives tiny, non‑repeatable energy. |
| `planck_density`, `naive_vacuum_energy_density`, `observed_dark_energy_density`, `cosmological_constant_gap` | The ~10¹²¹ gap between the naive "ocean" and what gravity measures. |

## Try it yourself

1. Change `GOLD_PLASMA_EV` to aluminium's ≈ 12.5 eV. How does the gold/ideal ratio at 100 nm change, and why does a higher plasma frequency help?
2. Using `casimir_pressure_ideal`, find the separation at which the Casimir pressure equals the pressure of sunlight on a mirror (about 9 µPa).
3. Try to design a cheating cycle: pass a pressure function to `closed_cycle_work` that is the ideal law on the way in and the gold law on the way out. You get net work — now explain what physical process would have to swap the plates' material at 100 nm, and what it would cost.
4. In `naive_vacuum_energy_density`, what cutoff $k_\text{max}$ would make the naive estimate match the observed dark‑energy density? Convert it to a length. (You should get tens of micrometres, a fraction of a millimetre, which is one reason sub‑millimetre tests of gravity are interesting.)

## References

- Casimir, H. B. G., "On the attraction between two perfectly conducting plates", *Proc. K. Ned. Akad. Wet.* **51**, 793 (1948).
- Lifshitz, E. M., "The theory of molecular attractive forces between solids", *Sov. Phys. JETP* **2**, 73 (1956).
- Lamoreaux, S. K., "Demonstration of the Casimir force in the 0.6 to 6 µm range", *Phys. Rev. Lett.* **78**, 5 (1997).
- Mohideen, U. & Roy, A., "Precision measurement of the Casimir force from 0.1 to 0.9 µm", *Phys. Rev. Lett.* **81**, 4549 (1998).
- Bressi, G., Carugno, G., Onofrio, R. & Ruoso, G., "Measurement of the Casimir force between parallel metallic surfaces", *Phys. Rev. Lett.* **88**, 041804 (2002).
- Lambrecht, A. & Reynaud, S., "Casimir force between metallic mirrors", *Eur. Phys. J. D* **8**, 309 (2000). Source of the gold Drude parameters.
- Bordag, M., Mohideen, U. & Mostepanenko, V. M., "New developments in the Casimir effect", *Phys. Rep.* **353**, 1 (2001).
- Wilson, C. M. et al., "Observation of the dynamical Casimir effect in a superconducting circuit", *Nature* **479**, 376 (2011).
- Munday, J. N., Capasso, F. & Parsegian, V. A., "Measured long‑range repulsive Casimir–Lifshitz forces", *Nature* **457**, 170 (2009).
- Weinberg, S., "The cosmological constant problem", *Rev. Mod. Phys.* **61**, 1 (1989).
- Planck Collaboration (Aghanim, N. et al.), "Planck 2018 results. VI. Cosmological parameters", *Astron. Astrophys.* **641**, A6 (2020).
