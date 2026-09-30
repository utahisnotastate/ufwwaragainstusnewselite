# 🔬 Module 2 — The Science Behind the Story

> The [lesson](readme.md) is told from the year 2420. This page is the 2025 reality check: what is established, where the story's claim breaks, and what would have to be true for it to work. Everything here can be checked with the [lab code](simulation.py).

## The 2420 claim in one sentence

Gravity is not a pull: space is full of a fast, isotropic flux, and two masses shield each other from it, so the unbalanced flux pushes them together.

## Level 1 — What's real

The idea has a real name and a long history: **Le Sage gravity** (Nicolas Fatio de Duillier, 1690; Georges‑Louis Le Sage, 1748). It was taken seriously by Kelvin, Maxwell and Poincaré, and the geometry is correct:

- A small body sees a second body of radius $R$ at distance $d$ as a disk covering a cone of half‑angle $\theta_0$, with $\sin\theta_0 = R/d$.
- If rays arrive equally from every direction, the missing momentum from that cone is

$$F \;\propto\; \tfrac12\int_{\cos\theta_0}^{1} u\,du \;=\; \frac{1-\cos^2\theta_0}{4} \;=\; \frac{R^2}{4d^2}.$$

That is an **inverse‑square law from pure geometry**. The lab confirms it by throwing two million random rays and counting the blocked ones; no force law is put in.

A flux of energy density $u$ moving at $c$, with each body absorbing a cross‑section $\sigma = h\,m$ proportional to its mass, gives

$$F = \frac{u\,\sigma_1\sigma_2}{4\pi r^2} = \frac{u\,h^2}{4\pi}\,\frac{m_1 m_2}{r^2}, \qquad\text{so matching Newton needs}\qquad u = \frac{4\pi G}{h^2}.$$

## Level 2 — Where the claim breaks

Physicists abandoned Le Sage gravity because of three problems. All three show up in the lab as numbers, not opinions.

**1. Saturation (mass proportionality).** A shadow only grows with mass while the body is nearly transparent. For a uniform sphere of optical radius $\tau = \mu R$, the absorbed fraction is

$$f(\tau) = 1 - \frac{1-(1+2\tau)e^{-2\tau}}{2\tau^2} \;\xrightarrow{\tau\ll 1}\; \tfrac43\tau.$$

At $\tau = 1$ the shadow is already only 53 % of the "proportional to mass" value. Real gravity is proportional to mass to better than one part in $10^{13}$ (the MICROSCOPE equivalence‑principle test) and shows no measurable self‑shielding (lunar laser ranging).

**2. Drag.** A body moving at $v$ through an isotropic flux runs into more of it from the front than from the back. For an absorber the force is $F = \tfrac43\,\sigma u\,v/c$. With $u$ fixed by $G$, Earth's orbital speed would decay in a time

$$t_\text{decay} = \frac{3\,h\,c}{16\pi G}.$$

**3. Heating.** Absorbed flux is absorbed energy: $P = \sigma u c = 4\pi G\,m\,c/h$.

**The dilemma.** Small $h$ keeps Earth transparent (good for problem 1), but then the orbit stops in a fraction of a second and Earth absorbs about $10^{45}$ W. Large $h$ tames the drag, but then Earth is opaque and gravity would no longer scale with mass. The lab test `test_no_coefficient_escapes_both_drag_and_saturation` sweeps 30 orders of magnitude of $h$ and finds no value that works. Richard Feynman makes this same argument in *The Feynman Lectures on Physics* (Vol. I, §7‑7).

The original lesson's "refutation of drag" — that a steady flux at constant velocity produces no drag — does not survive. The drag comes from the *body's* motion through the flux, not from the flux accelerating.

## Level 3 — What would have to be true

To rescue a pushing‑gravity model you would need all of these at once. Each is a clear, testable target:

- **A flux that carries momentum but not energy into matter**, or re‑emits exactly what it absorbs, so there is no heating. But re‑emission refills the shadow and kills the force. That is Maxwell's objection (1875).
- **Drag that vanishes for moving bodies.** This requires the flux to be Lorentz‑invariant, like the quantum vacuum, but a Lorentz‑invariant vacuum has no rest frame to push *from* and gives no net shadow force at all.
- **Tiny, measurable deviations**: gravity weakening slightly behind a third body (eclipse "shielding", searched for by Majorana in 1920 and later by eclipse gravimetry, with no confirmed effect) and small violations of mass proportionality in very dense bodies.

Modern physics describes gravity as spacetime curvature (general relativity), which passes every test so far, including gravitational waves (LIGO, 2015) and black‑hole imaging (EHT, 2019). A pushing model would have to reproduce all of those too.

## Run the lab

```bash
python Module_02_Gravity_Is_Pushing/simulation.py
python -m pytest tests/test_module_02.py
```

| Experiment | What it shows |
|---|---|
| `shadow_force` | Monte Carlo ray counting gives $1/d^2$ with no force law put in. |
| `absorbed_fraction`, `mass_proportionality` | Shadows stop tracking mass once bodies become opaque. |
| `drag_and_heating` | Tuning the flux to reproduce $G$ forces a choice between drag and heating on one side and saturation on the other. |

## Try it yourself

1. Change `R2` in `shadow_force`. At what distance does the Monte Carlo result stop matching the simple $R^2/4d^2$ law, and why?
2. Using `absorbed_fraction`, find the optical radius at which a body's shadow is 1 % weaker than "proportional to mass".
3. Redo `drag_and_heating` for the Moon (7.35 × 10²² kg, 1.02 km/s around Earth). Is the dilemma any easier?
4. Look up the MICROSCOPE result (Touboul et al., 2022). Convert its bound into a maximum allowed optical radius for a test mass.

## References

- Feynman, Leighton & Sands, *The Feynman Lectures on Physics*, Vol. I, §7‑7 "What is gravity?" (1963).
- Edwards, M. R. (ed.), *Pushing Gravity: New Perspectives on Le Sage's Theory of Gravitation*, Apeiron (2002). A sympathetic collection that also sets out the historical objections.
- Poincaré, H., *Science and Method*, Book III (1908). The heating objection.
- Maxwell, J. C., "Atom", *Encyclopaedia Britannica*, 9th ed. (1875). The re‑emission objection.
- Touboul, P. et al., "MICROSCOPE mission: final results of the test of the equivalence principle", *Phys. Rev. Lett.* **129**, 121102 (2022).
- Abbott, B. P. et al. (LIGO/Virgo), "Observation of gravitational waves from a binary black hole merger", *Phys. Rev. Lett.* **116**, 061102 (2016).
