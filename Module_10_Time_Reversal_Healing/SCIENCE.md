# 🔬 Module 10 — The Science Behind the Story

> The [lesson](readme.md) is told from the year 2420. This page is the 2025 reality check: what is established, where the story's claim breaks, and what would have to be true for it to work. Everything here can be checked with the [lab code](simulation.py).

> ⚕️ **Health note.** Nothing in this lesson is medical advice or a treatment. Time-reversal healing does not exist today. If you are sick or injured, please see a doctor; surgery and medicines save lives.

## The 2420 claim in one sentence

A "phase‑conjugate mirror" can record the distorted "wave" of a sick or aged body, send it back time‑reversed, and so undo the damage, restoring the body's earlier, healthy state.

## Level 1 — What's real

**Phase conjugation is real optics.** In 1972 Zel'dovich and co‑workers showed that light reflected by stimulated Brillouin scattering comes back with its wavefront reversed: a beam that was scrambled on the way in is unscrambled on the way out. Soon after, Hellwarth and Yariv showed the same thing with degenerate four‑wave mixing in a $\chi^{(3)}$ (Kerr‑type) nonlinear material. If the incoming field is

$$E(\mathbf r, t) = \mathrm{Re}\big[A(\mathbf r)\,e^{i(kz-\omega t)}\big],$$

a phase‑conjugate mirror returns $A^*(\mathbf r)\,e^{i(-kz-\omega t)}$. For a monochromatic wave that is exactly the time‑reversed wave: every ray retraces its path.

**Why that undoes distortion.** A thin aberrating layer multiplies the field by $e^{i\phi(x)}$. After phase conjugation the field carries $e^{-i\phi(x)}$, and crossing the same layer again gives $e^{-i\phi}e^{+i\phi} = 1$. Free‑space propagation is unitary, so it is undone the same way. The lab sends a beam through a 2‑radian random phase screen and back: the conjugate mirror returns the original beam with fidelity $1.000000$, while an ordinary mirror returns fidelity $0.0025$.

**Focusing through tissue is a real research field.** Biological tissue scatters light many times. Yaqoob et al. (2008) used optical phase conjugation to undo scattering through chicken‑breast tissue slices ("turbidity suppression"). Vellekoop and Mosk (2007) focused light *through* an opaque layer by adjusting the phases of $N$ segments of the input beam. For fully developed speckle, the expected brightness gain is

$$\eta = \frac{\pi}{4}(N-1) + 1.$$

The lab reproduces this law with random transmission matrices (for example $N = 1024$ gives $805$ against the predicted $804.5$). These methods are being developed for imaging and light delivery deep in tissue.

**Bioelectricity is real, measurable physics.** Every cell holds a voltage across its membrane. For one ion species, the equilibrium (Nernst) potential is

$$E_\text{ion} = \frac{RT}{zF}\ln\frac{[\text{ion}]_\text{out}}{[\text{ion}]_\text{in}},$$

which gives $E_K = -89$ mV at 37 °C for $[K]_o = 5$ mM, $[K]_i = 140$ mM. With several ions the resting voltage is set by the Goldman–Hodgkin–Katz equation:

$$V_m = \frac{RT}{F}\ln\frac{P_K[K]_o + P_{Na}[Na]_o + P_{Cl}[Cl]_i}{P_K[K]_i + P_{Na}[Na]_i + P_{Cl}[Cl]_o}.$$

With textbook mammalian values the lab gets $-67$ mV. Michael Levin's group and others study how patterns of these voltages help guide embryonic development and regeneration in animals such as frogs and flatworms (Levin, 2021). This is active basic research, not a therapy.

**Life lowers its own entropy all the time, legally.** A resting human releases about 100 W of heat. Per day, $8.6\times10^6$ J leaves a body at 310 K, carrying out $Q/T_\text{body} \approx 27{,}900$ J/K of entropy, and enters a 293 K room as $Q/T_\text{room} \approx 29{,}500$ J/K. Cells repair DNA, replace proteins and heal wounds by paying for local order with a larger entropy export. The second law holds for body plus surroundings.

## Level 2 — Where the claim breaks

**1. A phase‑conjugate mirror reverses a wave, not matter.** The cancellation above works because the *same* layer is crossed twice. It reverses the light field; it does not reverse the atoms the light passed through. A body is not a wave to be reflected: its cells, proteins and DNA are matter that the story's mirror never acts on.

**2. The medium must not change between passes.** If the aberrating layer changes, the return trip no longer cancels the first. For Gaussian phase screens with rms phase $\sigma$ and correlation $\rho$ between passes, the fidelity is

$$F = e^{-2\sigma^2(1-\rho)}.$$

The lab measures $F = 0.92$ at $\rho = 0.99$, $0.44$ at $\rho = 0.9$ and about $0$ at $\rho = 0.5$ (theory $0.92$, $0.45$, $0.02$). Living tissue rearranges constantly, and in‑vivo optical experiments must correct within short windows (typically milliseconds). The story wants to "reverse" changes accumulated over *decades*, when $\rho \approx 0$ and the fidelity is zero. In the scattering‑tissue model, a correction learned before the tissue moved gives a gain of $0.92$: no better than no correction at all.

**3. The mirror must capture the whole field.** The lab shows an exact result: with an unchanged medium, the fidelity equals the fraction of the power that the mirror intercepts (difference below $10^{-15}$). Whatever escapes is lost for good. To control light over just 1 cm² of tissue at 800 nm you would need about $6\times10^{8}$ independent modes. Nothing in the story explains how to capture the "wave" of every molecule in a body.

**4. There is no "young pattern" stored in a "time channel".** Physics has no record of a body's past state waiting to be replayed. The information about how your cells were arranged at age 20 has been spread into the environment as heat, the same entropy export described above. Energy is not the limit (100 W could in principle pay for erasing about $3\times10^{22}$ bits per second at the Landauer limit $kT\ln 2$). What is missing is the information and a mechanism to act on every molecule.

**5. The "Priore machine".** Antoine Priore built electromagnetic devices in France in the 1960s–70s and reported effects on tumours and infections in animals. The results were never independently reproduced or validated, and the devices are not an accepted treatment.

**6. Surgery and medicine are not "hitting the computer with a hammer".** Modern medicine is heavily built on physics and chemistry, and it works: vaccines, antibiotics, anaesthesia and surgery save many millions of lives. The lesson's contrast is part of the fiction.

## Level 3 — What would have to be true

For "time‑reversal healing" to exist, all of these would have to hold. Each is a concrete target:

- **A physical carrier for a body's state** that can be "reflected". Test: show that some field outside the body encodes tissue structure at cellular resolution and can be measured.
- **A stored record of the past state.** Test: recover a verifiable earlier state (for example, an old scar pattern) from a measurement made today, with no prior photographs or samples.
- **A mechanism that turns a returned wave into rearranged molecules**, in ways that match known chemistry and do not cook the tissue.
- **Coherence over time.** Any "reversal" would have to work although the body changes on millisecond‑to‑year timescales, which destroys conjugation fidelity as shown above.

**Real open questions that are closer to the story's spirit:**

- How far can wavefront shaping and optical phase conjugation push focusing, imaging and light delivery deep inside living tissue?
- Can bioelectric signals be used to steer regeneration in animals, and later safely in humans? (Early research; no approved therapies.)
- What sets the limits of the body's own repair, and can biology (for example stem‑cell and regenerative medicine) extend it?

## Run the lab

```bash
python Module_10_Time_Reversal_Healing/simulation.py
python -m pytest tests/test_module_10.py
```

| Experiment | What it shows |
|---|---|
| `round_trip` | Phase conjugation cancels a random aberration exactly; an ordinary mirror does not. |
| `round_trip(rho=...)`, `decorrelation_fidelity_theory` | If the medium changes between passes, fidelity drops as $e^{-2\sigma^2(1-\rho)}$. |
| `round_trip(aperture=...)` | Fidelity equals the fraction of the field the mirror captures. |
| `wavefront_shaping_enhancement`, `vellekoop_mosk_theory` | Focusing through scattering media follows $\tfrac{\pi}{4}(N-1)+1$ and is lost if the medium changes. |
| `nernst`, `ghk_voltage` | Real membrane voltages from ion concentrations (about $-67$ mV at rest). |
| `entropy_budget`, `landauer_bits_per_second` | Life lowers local entropy by exporting more; the second law holds overall. |

## Try it yourself

1. In `round_trip`, raise `rms_rad` from 2 to 4. How much more slowly can the medium change (how close to 1 must $\rho$ be) to keep 90 % fidelity? Check against $e^{-2\sigma^2(1-\rho)}$.
2. Use `with_changes` to find the extracellular potassium level at which the resting voltage reaches $-55$ mV. (Doctors watch blood potassium closely for this reason.)
3. Run `wavefront_shaping_enhancement` with a medium that only *partly* changes: mix the old and new transmission matrices as $\sqrt{\rho}\,t_\text{old} + \sqrt{1-\rho}\,t_\text{new}$. How does the gain fall with $\rho$?
4. Redo `entropy_budget` for a room at 35 °C. What happens to the net entropy production, and why do hot environments make it harder to shed heat?

## References

- Zel'dovich, B. Ya., Popovichev, V. I., Ragul'skii, V. V. & Faizullov, F. S., "Connection between the wave fronts of the reflected and exciting light in stimulated Mandel'shtam‑Brillouin scattering", *JETP Lett.* **15**, 109 (1972).
- Hellwarth, R. W., "Generation of time‑reversed wave fronts by nonlinear refraction", *J. Opt. Soc. Am.* **67**, 1 (1977).
- Yariv, A., "Phase conjugate optics and real‑time holography", *IEEE J. Quantum Electron.* **14**, 650 (1978).
- Vellekoop, I. M. & Mosk, A. P., "Focusing coherent light through opaque strongly scattering media", *Opt. Lett.* **32**, 2309 (2007).
- Yaqoob, Z., Psaltis, D., Feld, M. S. & Yang, C., "Optical phase conjugation for turbidity suppression in biological samples", *Nature Photonics* **2**, 110 (2008).
- Goldman, D. E., "Potential, impedance, and rectification in membranes", *J. Gen. Physiol.* **27**, 37 (1943).
- Hodgkin, A. L. & Katz, B., "The effect of sodium ions on the electrical activity of the giant axon of the squid", *J. Physiol.* **108**, 37 (1949).
- Levin, M., "Bioelectric signaling: Reprogrammable circuits underlying embryogenesis, regeneration, and cancer", *Cell* **184**, 1971 (2021).
- Landauer, R., "Irreversibility and heat generation in the computing process", *IBM J. Res. Dev.* **5**, 183 (1961).
