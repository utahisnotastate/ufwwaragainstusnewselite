# 🔬 Module 3 — The Science Behind the Story

> The [lesson](readme.md) is told from the year 2420. This page is the 2025 reality check: what is established, where the story's claim breaks, and what would have to be true for it to work. Everything here can be checked with the [lab code](simulation.py).

## The 2420 claim in one sentence

The brain does not make the mind but receives it, like a radio tuned to a broadcast in a "Time channel"; light jams that channel, and two brains tuned to the same frequency share thoughts.

## Level 1 — What's real

**Brains really do produce electrical rhythms.** Hans Berger recorded the first human EEG in the 1920s. Scalp electrodes pick up voltages of about 10–100 µV from millions of neurons firing in step. The rhythms are sorted into conventional bands (edges vary a little between labs):

| Band | Frequency | Typically associated with |
|---|---|---|
| delta | 0.5–4 Hz | deep sleep |
| theta | 4–8 Hz | drowsiness, memory tasks |
| alpha | 8–13 Hz | relaxed wakefulness, eyes closed |
| beta | 13–30 Hz | active thinking, movement |
| gamma | 30–80 Hz | local processing, attention |

**There is a real echo of "light squelches the signal".** Berger noticed that the alpha rhythm shrinks when you open your eyes ("alpha blocking"). It also shrinks with mental effort, so it reflects what the brain is *doing*, not photons interfering with a hidden channel.

**The Earth really hums.** Lightning strikes (about 50 per second worldwide) ring the cavity between the ground and the ionosphere. For an ideal, lossless thin shell of radius $R_E$ the modes are

$$f_n = \frac{c}{2\pi R_E}\sqrt{n(n+1)}, \qquad f_1 \approx 10.6\ \text{Hz}.$$

The observed peaks are at about 7.8, 14.3, 20.8, 27.3 and 33.8 Hz, roughly 75–80 % of the ideal values, because the ionosphere is a lossy, imperfect mirror (Schumann predicted the resonance in 1952; Balser & Wagner observed it in 1960). The 7.83 Hz fundamental happens to sit at the theta/alpha boundary.

**The brain's own fields are tiny too.** Outside the head the brain's magnetic field is about 100 fT–1 pT (magnetoencephalography, MEG). The Schumann magnetic field is also of order 1 pT. That is why MEG is done in magnetically shielded rooms.

**Measuring rhythms and synchrony.** The lab implements the standard tools:

- *Welch power spectrum* $S(f)$: average the squared Fourier transform of overlapping windowed segments.
- *Band power*: $P_\text{band} = \int_{f_1}^{f_2} S(f)\,df$. Summed over all frequencies this equals the signal's variance (the tests check this).
- *Instantaneous phase*: band‑pass filter, then take the analytic signal $x(t) + i\,\mathcal{H}[x](t) = A(t)e^{i\phi(t)}$ via the Hilbert transform.
- *Phase‑locking value* (Lachaux et al., 1999): $\text{PLV} = \left|\langle e^{i(\phi_1(t) - \phi_2(t))}\rangle_t\right|$, which is 1 for a constant phase difference and near 0 for unrelated phases.

"Brain‑to‑brain synchrony" is a real finding in hyperscanning studies, where two people are recorded at once. But it arises mostly because both people see and hear the same things at the same time, not because a signal passes between them (Burgess, 2013).

## Level 2 — Where the claim breaks

**1. Matching a frequency is not coupling.** A 1 pT field at 7.83 Hz induces, around a head‑sized loop (radius 7.5 cm),

$$\mathcal{E} = \pi r^2 \cdot 2\pi f B \approx 9\times10^{-13}\ \text{V}, \qquad E = \tfrac12 r\,\omega B \approx 2\times10^{-12}\ \text{V/m}.$$

That is about $10^{-7}$ of a 10 µV EEG signal. Transcranial alternating‑current stimulation, which can measurably nudge brain rhythms, puts roughly 0.1–1 V/m into the brain: about $10^{11}$ times more. Being "tuned to 7.83 Hz" gives no mechanism for the Schumann field to do anything.

**2. The test that cannot fail.** A common way to "show" brain–Earth resonance is to compare a signal with a perfect 7.83 Hz sine. Any two steady signals at the same frequency have a constant phase difference, so the PLV is 1 *by construction*. The lab does this and gets PLV = 1.000. It then asks the right question: is the PLV larger than you would get with the two records slid out of alignment by a few seconds? For a pure sine, sliding changes nothing, so the surrogate test returns p = 1: no evidence at all.

**3. A test that can fail.** The real Schumann field is not a perfect sine; lightning drives it randomly, so its phase wanders (quality factor $Q \approx 4$). The lab simulates EEG and an independent Schumann magnetometer record, then runs a time‑shift surrogate test on 100 synthetic recordings:

| Case | Fraction with p < 0.05 |
|---|---|
| No coupling | ≈ 5 % (the false‑positive rate a calibrated test should have) |
| Weak coupling built in (0.5 % of EEG power) | ≈ 93 % |
| Two EEG channels sharing one alpha source | 100 % |
| Two EEG channels with independent alpha sources | ≈ 4 % |

Because the test detects coupling when it really exists, its "no" means something. This is the standard that any claim of brain–Schumann coupling has to pass.

**4. Photon quenching.** There is no published, replicated evidence that light suppresses thought, or that infrared cameras photograph "tulpoid" mental forms. The inside of your skull is already almost dark, and people think perfectly well in bright sunlight. The eye's sensitivity curve comes from the absorption spectra of the photopigments in the retina, which are measured directly.

**5. Memory as a live broadcast from the past.** This is a lovely image, but the evidence points firmly the other way:

- Damage to specific brain structures removes specific abilities. The patient H.M. lost the ability to form new long‑term memories after surgery removed parts of both hippocampi (Scoville & Milner, 1957).
- In mice, the particular neurons active during learning can be tagged and later reactivated with light, which triggers the memory (Liu et al., 2012).
- Memories are *reconstructed* and can change: how a question is worded alters what people later report seeing (Loftus & Palmer, 1974). A live broadcast from the past would not be edited by the question.

The radio analogy in the homework ("the song is still in the air") makes a testable prediction: some other receiver should be able to play your song. No such receiver has ever been found.

**6. The quantum brain (Orch‑OR).** Hameroff and Penrose proposed that quantum superpositions in microtubules inside neurons collapse on timescales of about 25 ms and that this is linked to consciousness. It is a real, published, and contested hypothesis. The main objection is timing: Tegmark (2000) estimated that such superpositions decohere in $10^{-13}$ s or less. The lab computes the gap:

| Neural timescale | vs Tegmark's $10^{-13}$ s | vs the rebuttal estimate $10^{-4}$ s (Hagan et al., 2002) |
|---|---|---|
| action potential, 1 ms | $10^{10}$ | $10^{1}$ |
| gamma cycle, 25 ms | $10^{11}$ | $10^{2.4}$ |

Even the most favourable published estimate falls short. Orch‑OR also would not make the brain a *receiver*; it is still a theory of the brain producing the mind.

## Level 3 — What would have to be true

For the brain to be a Schumann‑tuned receiver, these would have to show up. Each is a clear experiment:

- **Coupling that passes a surrogate test.** Record EEG together with a local magnetometer. A preregistered analysis should find PLV between them above a time‑shift surrogate null, repeated in independent labs.
- **Coupling that disappears when the field is removed.** Repeat inside a magnetically shielded room, which cuts the 1 pT field by orders of magnitude. If the "coupling" survives, it is not coming from the Schumann field.
- **A mechanism with the right size.** Something in neural tissue would need to respond to fields about $10^{11}$ times weaker than those known to affect it, and above thermal noise.
- **For "photon quenching"**: a replicated, blinded experiment in which some mental phenomenon appears in darkness and disappears in light, with the light level as the only thing changed.

Real open questions remain. How consciousness arises from brain activity (the "hard problem") is unsolved. Whether quantum effects play any functional role in biology is actively studied. Gravity‑related wave‑function collapse, which Orch‑OR relies on, is being tested; an underground experiment ruled out the simplest parameter‑free version of the Diósi–Penrose model (Donadi et al., 2021).

## Run the lab

```bash
python Module_03_The_Brain_Is_A_Radio/simulation.py
python Module_03_The_Brain_Is_A_Radio/simulation.py --data my_eeg.csv --fs 160 --channels 0 1
python -m pytest tests/test_module_03.py
```

| Experiment | What it shows |
|---|---|
| `schumann_frequency` | Ideal cavity modes (10.6, 18.3, … Hz) vs the observed 7.83, 14.3, … Hz. |
| `field_budget`, `induced_emf`, `induced_e_field` | The Schumann field is the brain's own size outside the head, but induces ~10⁻¹² V/m inside it. |
| `pink_noise`, `synthetic_eeg_pair`, `schumann_record` | Synthetic EEG (1/f background plus alpha bursts) and a wandering‑phase Schumann trace. |
| `welch_psd`, `band_power`, `spectral_slope` | Standard EEG spectral analysis. |
| `plv`, `shift_surrogate_test`, `detection_rate` | Phase locking, the sine‑vs‑sine trap, and a calibrated test with measured false‑positive rate and power. |
| `decoherence_gap` | Orch‑OR's timing problem in orders of magnitude. |
| `load_user_eeg` | Optional: your own recording as `.csv` or `.npy` (samples × channels). No network is used. |

## Try it yourself

1. Real data: download a few runs of the PhysioNet EEG Motor Movement/Imagery dataset (109 volunteers, 64 channels, 160 Hz, EDF format). Convert two channels to CSV (for example with the MNE‑Python library) and run the lab with `--data`. Compare eyes‑open and eyes‑closed baseline runs: does alpha power change as Berger found?
2. With your own data, compute the PLV between two *neighbouring* electrodes and two *distant* ones. Why are neighbours almost always "significantly locked"? (Hint: volume conduction, where one source reaches both electrodes.)
3. Implement a phase‑randomized surrogate (keep the Fourier amplitudes of one channel, randomize its phases) and use it against a perfect 7.83 Hz sine reference. Show that it too cannot tell a steady 7.83 Hz rhythm from real entrainment. What property of the reference makes every surrogate method fail?
4. Lower `COUPLING_DEMO` until `detection_rate` falls to about 50 %. How does that power change if you double the recording length?
5. Use `induced_e_field` to find the magnetic field at 7.83 Hz that would induce 0.1 V/m in a head. How does it compare with an MRI scanner's field (a few tesla, but static)?

## References

- Berger, H., "Über das Elektrenkephalogramm des Menschen", *Archiv für Psychiatrie und Nervenkrankheiten* **87**, 527 (1929).
- Schumann, W. O., "Über die strahlungslosen Eigenschwingungen einer leitenden Kugel, die von einer Luftschicht und einer Ionosphärenhülle umgeben ist", *Z. Naturforsch. A* **7**, 149 (1952).
- Balser, M. & Wagner, C. A., "Observations of Earth–ionosphere cavity resonances", *Nature* **188**, 638 (1960).
- Nickolaenko, A. P. & Hayakawa, M., *Resonances in the Earth–Ionosphere Cavity*, Kluwer (2002).
- Hämäläinen, M., Hari, R., Ilmoniemi, R. J., Knuutila, J. & Lounasmaa, O. V., "Magnetoencephalography — theory, instrumentation, and applications to noninvasive studies of the working human brain", *Rev. Mod. Phys.* **65**, 413 (1993).
- Lachaux, J.‑P., Rodriguez, E., Martinerie, J. & Varela, F. J., "Measuring phase synchrony in brain signals", *Hum. Brain Mapp.* **8**, 194 (1999).
- Theiler, J., Eubank, S., Longtin, A., Galdrikian, B. & Farmer, J. D., "Testing for nonlinearity in time series: the method of surrogate data", *Physica D* **58**, 77 (1992).
- Burgess, A. P., "On the interpretation of synchronization in EEG hyperscanning studies: a cautionary note", *Front. Hum. Neurosci.* **7**, 881 (2013).
- Schalk, G., McFarland, D. J., Hinterberger, T., Birbaumer, N. & Wolpaw, J. R., "BCI2000: a general‑purpose brain‑computer interface (BCI) system", *IEEE Trans. Biomed. Eng.* **51**(6), 1034 (2004). Source of the PhysioNet EEG Motor Movement/Imagery dataset.
- Goldberger, A. L. et al., "PhysioBank, PhysioToolkit, and PhysioNet", *Circulation* **101**(23), e215 (2000).
- Scoville, W. B. & Milner, B., "Loss of recent memory after bilateral hippocampal lesions", *J. Neurol. Neurosurg. Psychiatry* **20**, 11 (1957).
- Liu, X. et al., "Optogenetic stimulation of a hippocampal engram activates fear memory recall", *Nature* **484**, 381 (2012).
- Loftus, E. F. & Palmer, J. C., "Reconstruction of automobile destruction: an example of the interaction between language and memory", *J. Verbal Learn. Verbal Behav.* **13**, 585 (1974).
- Hameroff, S. & Penrose, R., "Orchestrated reduction of quantum coherence in brain microtubules: a model for consciousness", *Math. Comput. Simul.* **40**, 453 (1996).
- Hameroff, S. & Penrose, R., "Consciousness in the universe: a review of the 'Orch OR' theory", *Phys. Life Rev.* **11**, 39 (2014).
- Tegmark, M., "Importance of quantum decoherence in brain processes", *Phys. Rev. E* **61**, 4194 (2000).
- Hagan, S., Hameroff, S. R. & Tuszyński, J. A., "Quantum computation in brain microtubules: decoherence and biological feasibility", *Phys. Rev. E* **65**, 061901 (2002).
- Donadi, S. et al., "Underground test of gravity‑related wave function collapse", *Nat. Phys.* **17**, 74 (2021).
