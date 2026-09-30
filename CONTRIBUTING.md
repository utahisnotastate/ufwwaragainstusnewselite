# Contributing

Thanks for helping. The most valuable contributions are **corrections**: a wrong number, an overstated claim, a missing caveat, or a better reference.

## Module layout

Every `Module_NN_Name/` folder contains:

| File | Role | Rules |
|---|---|---|
| `readme.md` | 📖 The 2420 story lesson | Starts with the title and the "Story mode" banner, then `Lesson Title`, `Source`, `Concept` bullets and numbered sections. Imaginative, but never tells a reader to skip real medical care. |
| `PHYSICS_PROOF.md` | 📜 The in‑universe argument | Starts with the "In‑universe document" banner. Sections: For the 8‑Year‑Old, Subject, The Axiom, The Mechanism, The Proof/Implication. |
| `SCIENCE.md` | 🔬 The 2025 reality check | Sections: The 2420 claim in one sentence · Level 1 — What's real · Level 2 — Where the claim breaks · Level 3 — What would have to be true · Run the lab · Try it yourself · References. |
| `simulation.py` | 🧪 The lab | Standalone; NumPy and SciPy only; importable pure functions plus a `main()` report. |

Tests live in `tests/test_module_NN.py` and load the lab with the shared `sim` fixture (set `FOLDER = "Module_NN_Name"` at the top of the file).

## Rules for the lab code

1. **No circular verification.** Never derive a parameter from the answer and then "confirm" the answer. If the result is guaranteed by construction, say so in a comment and don't present it as evidence.
2. **No hardcoded verdicts.** Every conclusion that is printed must be computed.
3. **Show where it breaks.** Each lab includes at least one calculation that tests the story's claim against measurement, not only the parts that are true.
4. **Tests must be able to fail.** Check analytic limits, scaling laws and published values, not values the code copied from itself.
5. Keep each test file under a few seconds.

## Rules for citations

- Only cite sources you have checked: authors, year, journal, volume and page.
- Prefer primary papers and standard textbooks. A contested claim should cite both sides.
- Say "no evidence" plainly and kindly where that is the state of knowledge.

## Before opening a pull request

```bash
python -m pip install -r requirements.txt
python -m pytest
```

If you change an English lesson, mention it in the pull request so the translations can be updated.
