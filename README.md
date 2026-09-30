# The "Lost" Curriculum of the 2420s — Obvious Physics for Humans

[![tests](https://github.com/utahisnotastate/ufwwaragainstusnewselite/actions/workflows/tests.yml/badge.svg)](https://github.com/utahisnotastate/ufwwaragainstusnewselite/actions/workflows/tests.yml)

☕ Support this project: [ko-fi.com/utah23](https://ko-fi.com/utah23) · Why I made this: [ABOUT.md](ABOUT.md)

Twelve big ideas, each taught three ways:

| Layer | File | What it is |
|---|---|---|
| 📖 **The story** | `readme.md` | A lesson written as if from a school in the year 2420, for bright 8‑year‑olds and curious adults. Science fiction built around a real question. |
| 🔬 **The science** | `SCIENCE.md` | The 2025 reality check: what is established, where the story's claim breaks (with numbers), and what would have to be true for it to work. With real references. |
| 🧪 **The lab** | `simulation.py` | Runnable Python that computes every number in the science page. Tested against textbook limits and published measurements. |

Each module also keeps its in‑universe `PHYSICS_PROOF.md`: the 2420 archive's own argument, clearly labelled as part of the story.

**Why this format?** The stories are the hook. They ask the questions kids actually ask: *Is space really empty? Why does gravity pull? Could we travel instantly?* The science pages answer them honestly, including "no, and here's the calculation that shows why." Learning where a beautiful idea breaks teaches more physics than being told it works.

---

## Quick start

```bash
python -m pip install -r requirements.txt
python Module_02_Gravity_Is_Pushing/simulation.py   # run one lab
python -m pytest                                    # check every lab
```

Requires Python 3.10+ with NumPy and SciPy. No plotting library or internet connection needed.

---

## Module index

| # | Module | The 2420 story says… | What the lab computes |
|---|---|---|---|
| 1 | 🌊 [The Vacuum Ocean](Module_01_Zero_Point_Energy/readme.md) · [science](Module_01_Zero_Point_Energy/SCIENCE.md) | Space is a high‑pressure plenum we can tap for free energy. | Casimir force (ideal and Lifshitz theory for real gold), why a closed cycle yields zero net work. |
| 2 | 📉 [Gravity Is Pushing](Module_02_Gravity_Is_Pushing/readme.md) · [science](Module_02_Gravity_Is_Pushing/SCIENCE.md) | Masses shadow each other from a cosmic flux. | Monte Carlo shadowing gives 1/r², then the drag, heating and saturation problems that sank Le Sage gravity. |
| 3 | 📻 [The Brain Is a Radio](Module_03_The_Brain_Is_A_Radio/readme.md) · [science](Module_03_The_Brain_Is_A_Radio/SCIENCE.md) | Mind is a signal the brain tunes into. | Real EEG signal processing, Schumann resonances, and how to test phase‑locking against a proper null. |
| 4 | 🍩 [Matter Is Frozen Light](Module_04_Matter_Is_Frozen_Light/readme.md) · [science](Module_04_Matter_Is_Frozen_Light/SCIENCE.md) | Particles are light running in circles. | Breit–Wheeler pair creation, the Schwinger field, where proton mass comes from, and why the "light loop" electron is a tautology. |
| 5 | 🗺️ [Time Is a Map](Module_05_Time_Is_A_Map/readme.md) · [science](Module_05_Time_Is_A_Map/SCIENCE.md) | Past and future are coordinates you can visit. | GPS clock corrections, relativity of simultaneity, Kerr ergospheres and the Penrose process. |
| 6 | 🔊 [The Language of Reality](Module_06_Language_of_Reality/readme.md) · [science](Module_06_Language_of_Reality/SCIENCE.md) | Sound shapes matter. | Chladni plate modes, acoustic radiation forces, and why sound can't place atoms. |
| 7 | 🧬 [DNA as an Antenna](Module_07_DNA_Antenna/readme.md) · [science](Module_07_DNA_Antenna/SCIENCE.md) | DNA receives instructions from a field. | Helical antenna theory vs DNA's real size, Debye screening in the cell, FRET and DNA dynamics. |
| 8 | ⚡ [Instant Travel](Module_08_Instant_Travel/readme.md) · [science](Module_08_Instant_Travel/SCIENCE.md) | Fold space and step across. | The Alcubierre warp metric, its negative‑energy bill, and quantum inequality limits. |
| 9 | ⛈️ [Weather Engineering](Module_09_Weather_Engineering/readme.md) · [science](Module_09_Weather_Engineering/SCIENCE.md) | Steer storms with crossed waves. | Köhler droplet activation, ion‑induced nucleation, and the energy gap between machines and storms. |
| 10 | ⏳ [Time‑Reversal Healing](Module_10_Time_Reversal_Healing/readme.md) · [science](Module_10_Time_Reversal_Healing/SCIENCE.md) | A time‑mirror undoes illness. | Optical phase conjugation and its limits, cell membrane voltages, and the entropy budget of life. |
| 11 | ⚗️ [Precipitating Gold](Module_11_Low_Energy_Transmutation/readme.md) · [science](Module_11_Low_Energy_Transmutation/SCIENCE.md) | Resonant lattices make fusion easy. | Coulomb barriers, Gamow tunnelling, electron screening, and the neutron count 1 W of fusion would produce. |
| 12 | 🌐 [The Psychotronic Internet](Module_12_The_Psychotronic_Internet/readme.md) · [science](Module_12_The_Psychotronic_Internet/SCIENCE.md) | Minds link instantly through the vacuum. | Skin depth in seawater and Faraday cages, why "scalar" coils radiate nothing new, and real brain–computer interface bandwidths. |

Modules build on each other, so start at Module 1. Health note: nothing here is medical advice (see Module 10).

---

## Translations

Estonian, Finnish, Russian, Japanese and Chinese (Simplified) versions of the **stories** live in [`translations/`](translations/README.md). They were made before the science pages and labs were added, so they don't include those yet.

---

## Contributing

Corrections are the most valuable contribution: a wrong number, a missing caveat, a better reference. See [CONTRIBUTING.md](CONTRIBUTING.md) for the module layout and the rules for code and citations.

## Intent

This curriculum uses science fiction to make physics questions irresistible, then answers them honestly. The stories are imaginative; the science pages and code aim to be correct. If you find a place where they aren't, please open an issue.
