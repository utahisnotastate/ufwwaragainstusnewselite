# 🔬 Module 12 — The Science Behind the Story

> The [lesson](readme.md) is told from the year 2420. This page is the 2025 reality check: what is established, where the story's claim breaks, and what would have to be true for it to work. Everything here can be checked with the [lab code](simulation.py).

## The 2420 claim in one sentence

Human minds can be linked directly, without phones or wires, through a planet‑wide "Noosphere" amplified by a "psychotronic grid", so that questions are answered instantly and skills can be downloaded in seconds.

## Level 1 — What's real

**Brains are electrical, and their fields can be measured.** Neurons produce currents whose fields can be recorded outside the head: EEG (microvolts on the scalp) and MEG (magnetic fields of roughly 100 fT to 1 pT at sensors a few centimetres from the sources, about $10^{-8}$ of Earth's field).

**Brain–computer interfaces are real.** Implanted electrode arrays (for example in the BrainGate trials) let people with paralysis control cursors, robot arms and text. Willett et al. (2021) decoded imagined handwriting at about 90 characters per minute, and later work decoded attempted speech at about 62 words per minute (Willett et al., 2023). These are medical devices that read signals from electrodes placed in or on the brain; they do not reach other people's brains through the air.

**Conductors screen fields.** A changing field entering a conductor decays over the skin depth

$$\delta = \sqrt{\frac{2}{\mu\sigma\omega}} \;\propto\; f^{-1/2}.$$

In seawater ($\sigma \approx 4$ S/m), $\delta = 29$ m at 76 Hz, the frequency of the US Navy's ELF submarine transmitters, 4.6 m at 3 kHz and 0.25 m at 1 MHz. At 2.4 GHz, water's displacement current is larger than its conduction current ($\omega\varepsilon/\sigma \approx 2.7$), so the general formula is needed and gives about 1 cm. In copper, $\delta = 9.2$ mm at 50 Hz and 65 µm at 1 MHz: a 1 mm copper sheet absorbs about 133 dB at 1 MHz. That is why Faraday cages work.

**Static fields are screened too.** In a conductor, charges move until the field inside is zero. For a conducting sphere in a uniform field $E_0$, the induced surface charge is $\sigma_s = 3\varepsilon_0E_0\cos\theta$. The lab does not assume the answer: it adds up Coulomb's law over that surface charge numerically and finds the total field inside is below $10^{-4}E_0$, while outside it matches the textbook dipole solution.

**Potentials are real, and matter in a precise way.** Whittaker showed in 1903–1904 that solutions of the wave equation, and the electromagnetic field itself, can be written using scalar functions. That is correct mathematics, but it describes the *same* fields $\mathbf E$ and $\mathbf B$, not a new kind of wave. The one place where potentials have directly observable effects is the Aharonov–Bohm effect (1959): an electron passing around a region of magnetic flux $\Phi$ picks up a phase

$$\Delta\varphi = \frac{e\Phi}{\hbar} = 2\pi\,\frac{\Phi}{h/e},\qquad h/e = 4.14\times10^{-15}\ \text{Wb},$$

even if the magnetic field on its path is zero. Tonomura et al. (1986) confirmed it with the field fully enclosed in a superconducting shield. The effect depends only on the enclosed flux around a closed loop, and it follows standard quantum electrodynamics.

**Human communication rates are measurable.** Across 17 languages, speech carries about 39 bits per second (Coupé et al., 2019). Written English carries roughly 1 bit per character once its redundancy is counted (Shannon, 1951).

## Level 2 — Where the claim breaks

**1. Nothing carries information faster than light.** "PING! The answer pops into your mind instantly" is not possible across real distances:

| Link | One‑way light delay |
|---|---|
| Earth–Moon | 1.28 s |
| Earth–Mars (closest to farthest) | 3.0 to 22.3 min |
| Proxima Centauri | 4.25 years |

A "capital of Mars" question gets its answer at the earliest 6 to 45 minutes later, round trip.

**2. Entanglement cannot send messages.** For an entangled pair, the lab computes Bob's local state after Alice measures along any axis and finds it is always exactly $\tfrac12\mathbb 1$ (difference below $10^{-15}$), the same as if she did nothing. The correlations are real (their results agree with probability $\cos^2(\Delta\theta/2)$), but they only show up when the two records are compared over an ordinary channel. This is the no‑communication theorem.

**3. Brain fields are far too weak to reach anyone.** A dipole field falls as $1/r^3$. A 1 pT brain signal measured about 4 cm from its source is about $6\times10^{-17}$ T at 1 m and $6\times10^{-26}$ T at 1 km, more than $10^{20}$ times weaker than Earth's field. The best magnetometers need shielded rooms and sensors on the scalp.

**4. "Scalar" coils radiate nothing new.** A counter‑wound (bifilar) coil drives two opposite currents so that the fields cancel. The lab computes both what is left close by and what radiates:

- On the axis, one loop's field falls as $z^{-3.00}$; the counter‑wound pair's leftover falls as $z^{-4.00}$: an ordinary higher multipole.
- Far away, the pair radiates $(kd)^2/5$ of one coil's power when the coils are close together ($kd \ll 1$). For $d = 0$ the radiation is exactly zero. No additional "scalar" wave appears, and if the potentials also cancel, nothing is left to have an effect, Aharonov–Bohm or otherwise.

**5. Shielding.** If a psychotronic signal were electromagnetic, a metal room, a submarine or a few metres of seawater would cut it off, as shown by the skin depths above. If it is not electromagnetic, the story needs a new force of nature, which no experiment has seen.

**6. Bandwidth.** A 1 MB flight manual at the speed of speech takes about 57 hours to transfer. Downloading it in 5 s would need $1.6\times10^6$ bit/s, about 40,000 times the rate of speech. Real BCIs today run at a few bits per second. Nor do we know how to write skills or memories into a brain: that would require precisely changing synapses across huge numbers of neurons.

**7. The Noosphere is philosophy, not physics.** Vernadsky and Teilhard de Chardin used "noosphere" for the growing sphere of human thought and its effect on the planet. It is a thoughtful idea about society and evolution, not a measured layer of the atmosphere. Bees do communicate, but through physical signals: the waggle dance, pheromones and vibrations.

## Level 3 — What would have to be true

For a psychotronic internet to exist, all of these would have to be shown. Each is testable:

- **A carrier that reaches from brain to brain.** Test: a sender and receiver in separate Faraday‑shielded rooms, with random target messages, blind scoring and pre‑registered analysis, repeated by independent labs.
- **A way around the speed of light**, which would also overturn relativity and causality. Test: a message that arrives before light could have carried it.
- **A read–write interface for memories and skills**: understanding how a skill is stored in synapses well enough to write it into a different brain.

**Real open questions close to the story:** How fast and how safe can BCIs become, and can they be made without surgery? How much of the brain's information can non‑invasive methods (EEG, MEG, optically pumped magnetometers, functional ultrasound) read? What are the privacy and ethics rules for "neural data"?

## Run the lab

```bash
python Module_12_The_Psychotronic_Internet/simulation.py
python -m pytest tests/test_module_12.py
```

| Experiment | What it shows |
|---|---|
| `skin_depth`, `attenuation_length`, `shield_absorption_db` | Seawater and metal block changing fields; $\delta \propto f^{-1/2}$. |
| `conducting_sphere_field` | Summing Coulomb's law over induced charge gives zero field inside a conductor. |
| `antiparallel_pair_power`, `counterwound_axis_field` | Opposite currents leave an ordinary, faster‑decaying multipole, not a new wave. |
| `aharonov_bohm_phase` | The real, measured effect of potentials. |
| `light_delay`, `bob_state`, `same_outcome_probability` | Light‑speed delays; entanglement correlates but cannot signal. |
| `brain_field`, `bci_bits_per_second`, `transfer_time` | How weak brain fields are and how slow human data rates are. |

## Try it yourself

1. Find the frequency at which seawater's skin depth is 100 m. Why did the Navy's submarine radio send only a few characters per minute?
2. In `bob_state`, replace the Bell state with $(\lvert00\rangle + \lvert11\rangle)$ plus a small $\lvert01\rangle$ admixture (normalise it). Does Alice's choice of angle now change Bob's state?
3. Using `antiparallel_pair_power`, how far apart must two opposite 1 kHz coils be (in km) before they radiate as much as a single coil?
4. Look up the information rate of reading. How long would it take to read everything on the internet at that rate?

## References

- Whittaker, E. T., "On the partial differential equations of mathematical physics", *Math. Ann.* **57**, 333 (1903).
- Whittaker, E. T., "On an expression of the electromagnetic field due to electrons by means of two scalar potential functions", *Proc. London Math. Soc.* **s2‑1**, 367 (1904).
- Aharonov, Y. & Bohm, D., "Significance of electromagnetic potentials in the quantum theory", *Phys. Rev.* **115**, 485 (1959).
- Tonomura, A. et al., "Evidence for Aharonov‑Bohm effect with magnetic field completely shielded from electron wave", *Phys. Rev. Lett.* **56**, 792 (1986).
- Ghirardi, G. C., Rimini, A. & Weber, T., "A general argument against superluminal transmission through the quantum mechanical measurement process", *Lett. Nuovo Cimento* **27**, 293 (1980).
- Nielsen, M. A. & Chuang, I. L., *Quantum Computation and Quantum Information*, Cambridge University Press (2000).
- Hämäläinen, M. et al., "Magnetoencephalography—theory, instrumentation, and applications to noninvasive studies of the working human brain", *Rev. Mod. Phys.* **65**, 413 (1993).
- Willett, F. R. et al., "High‑performance brain‑to‑text communication via handwriting", *Nature* **593**, 249 (2021).
- Willett, F. R. et al., "A high‑performance speech neuroprosthesis", *Nature* **620**, 1031 (2023).
- Coupé, C., Oh, Y. M., Dediu, D. & Pellegrino, F., "Different languages, similar encoding efficiency: Comparable information rates across the human communicative niche", *Science Advances* **5**, eaaw2594 (2019).
- Shannon, C. E., "Prediction and entropy of printed English", *Bell Syst. Tech. J.* **30**, 50 (1951).
- Vernadsky, V. I., "The biosphere and the noosphere", *American Scientist* **33**, 1 (1945).
- Teilhard de Chardin, P., *The Phenomenon of Man* (1955; English translation 1959).
