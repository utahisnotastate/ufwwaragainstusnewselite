# 🔬 Module 5 — The Science Behind the Story

> The [lesson](readme.md) is told from the year 2420. This page is the 2025 reality check: what is established, where the story's claim breaks, and what would have to be true for it to work. Everything here can be checked with the [lab code](simulation.py).

## The 2420 claim in one sentence

Past, present and future all exist together like places on a map, reality "flickers" from frame to frame, and time travel is just shifting your phase to a different part of the map.

## Level 1 — What's real

**Time really is part of a four‑dimensional geometry.** In special relativity, the quantity every observer agrees on is not the time between two events or the distance between them, but the **Minkowski interval**

$$s^2 = -c^2\,\Delta t^2 + \Delta x^2 + \Delta y^2 + \Delta z^2 .$$

Negative $s^2$ (timelike) means one event can cause the other; positive $s^2$ (spacelike) means neither can. The lab checks that the Lorentz transformation $t' = \gamma\,(t - vx/c^2)$, $x' = \gamma\,(x - vt)$ leaves $s^2$ unchanged.

**"Now" depends on who is asking.** Two events at the same time $t$ but a distance $L$ apart are, for an observer moving at $v$, separated in time by

$$\Delta t' = -\gamma\,\frac{vL}{c^2}.$$

For the Andromeda galaxy ($L \approx 2.5$ million light years), simply walking at 1.4 m/s shifts which Andromeda events count as "now" by about **4 days** (the lab computes this; the example is Penrose's "Andromeda paradox"). This relativity of simultaneity is why many philosophers of physics defend **eternalism**, the "block universe" view in which all events are equally real (Rietdijk 1966, Putnam 1967). It is a legitimate interpretation of relativity. It is not the only one, and no experiment can distinguish it from its rivals, because they all make the same predictions.

**Clocks really do tick at different rates, and we correct for it every day.** A clock's rate relative to coordinate time is, in the weak‑field limit,

$$\frac{d\tau}{dt} \approx 1 + \frac{\Phi}{c^2} - \frac{v^2}{2c^2}, \qquad \Phi = -\frac{GM}{r}.$$

For a GPS satellite ($a \approx 26\,562$ km, $v \approx 3.87$ km/s) compared with a clock on the equator, the lab computes from first principles:

| Effect | µs per day |
|---|---|
| Weaker gravity at altitude (runs fast) | +45.7 |
| Orbital speed (runs slow) | −7.2 |
| Ground clock's own rotation | +0.1 |
| **Net** | **+38.5** |

Published figures are usually quoted as +45.9, −7.2 and +38.6 µs/day; the small differences come from how Earth's shape and rotation are modelled (the lab's cross‑check using the IAU geoid constant $L_G$ gives +38.58). Uncorrected, this would be a ranging error of about 11 km per day. Relativistic clock shifts were also measured directly by flying atomic clocks around the world (Hafele & Keating 1972).

**Rotating black holes drag spacetime.** The Kerr metric (Kerr 1963) in Boyer–Lindquist coordinates, with $G = c = M = 1$, has

$$\Sigma = r^2 + a^2\cos^2\theta,\quad \Delta = r^2 - 2r + a^2,$$
$$g_{tt} = -\Big(1-\frac{2r}{\Sigma}\Big),\quad g_{t\phi} = -\frac{2ar\sin^2\theta}{\Sigma},\quad g_{\phi\phi} = \Big(r^2 + a^2 + \frac{2a^2 r\sin^2\theta}{\Sigma}\Big)\sin^2\theta .$$

- Horizons at $r_\pm = 1 \pm \sqrt{1-a^2}$, which exist only for $a \le 1$.
- The **ergosphere** lies between $r_+$ and $r_\text{ergo} = 1 + \sqrt{1 - a^2\cos^2\theta}$, where $g_{tt} = 0$. Inside it the "stand still" direction $\partial_t$ becomes spacelike: **no observer can stay at rest**, everything is dragged around with the hole. The lab checks $g_{tt}=0$ on that surface, and the sign of $g_{tt}$ on both sides of it.
- The **Penrose process** (Penrose 1969): a particle splits inside the ergosphere, one piece falls in with negative energy, and the other escapes with more energy than the original. The lab solves the energy and angular‑momentum conservation for this split and recovers the textbook maximum $\eta = \tfrac12\big(\sqrt{2/r_+}-1\big)$, which is **20.7 %** for $a = 1$.
- The total energy that can ever be extracted is set by the **irreducible mass** (Christodoulou 1970), $M_\text{irr} = \tfrac12\sqrt{r_+^2 + a^2}$: at most $1 - M_\text{irr}/M = $ **29.3 %** for an extremal hole.

## Level 2 — Where the claim breaks

**1. Disagreeing about "now" is not the same as reaching the past.** The lab boosts two pairs of events through 199 velocities up to $0.99c$. The spacelike pair swaps order in 50 of them. The timelike pair, the kind that can be cause and effect, **never** does. Relativity lets observers disagree about the ordering of events that cannot affect each other. It never lets anyone see an effect before its cause.

**2. "Time is a flicker" and "time travel is phase shifting" have no physics behind them.** No theory predicts a positive/negative "tick" of reality, the idea makes no number that could be measured, and clocks compared across the world show smooth, predictable rates, as the GPS numbers above show. As written, the claim cannot be tested.

**3. The lesson mixes two different ideas.** The block universe (one fixed four‑dimensional history) and "many worlds" (Everett 1957; branching quantum histories) are separate interpretations. Neither one includes choosing which "reel" to play. The "light of consciousness moving along the worm billions of times a second" is a metaphor, not a physical mechanism.

**4. Where general relativity *does* allow time loops, they are far out of reach.** A closed timelike curve (CTC) is a path through spacetime that returns to its own past. Exact solutions with CTCs exist: Gödel's rotating universe (1949), van Stockum's and Tipler's infinitely long rotating cylinders (Tipler 1974), and the inside of the Kerr solution (Carter 1968). In Kerr, the loop around the axis is timelike wherever $g_{\phi\phi} < 0$. The lab scans $r$ for every spin and finds **$g_{\phi\phi} < 0$ only at $r < 0$**, a region reached only by passing through the ring singularity; for $a = 1$ at the equator its edge is exactly at $r = -1$. An earlier draft of this lesson made two errors that the lab now tests against:

- it used $a = 1.2$, which has **no horizon at all** (a naked singularity, not expected to form in nature), and
- it treated $\partial_t$ becoming spacelike inside the ergosphere as a time machine. Inside the ergosphere $g_{\phi\phi}$ is still positive: that is **frame dragging, not a CTC**.

**5. Physics seems to protect the past.** Hawking's **chronology protection conjecture** (1992) proposes that quantum effects stop CTCs from forming in any region we could reach. It is a conjecture, not a theorem, but there is **no evidence that CTCs are physically realisable** anywhere in our universe.

## Level 3 — What would have to be true

For "time travel by phase shifting" to become science, it would need to meet all of these:

- **A spacetime with an accessible CTC region.** Every known way to build one (traversable wormholes, warp bubbles) requires "exotic" matter with negative energy density, violating the classical energy conditions (Morris, Thorne & Yurtsever 1988). Whether quantum effects allow enough of it is an open question.
- **A way around chronology protection.** A calculation in a full theory of quantum gravity would have to show that the vacuum does not blow up at the edge of the time machine (the "chronology horizon").
- **A measurable prediction for "flicker".** For example, a predicted noise floor, discreteness or frequency in atomic‑clock comparisons that disagrees with standard physics. If the story gave a frequency, clocks could look for it.
- **Consistency with causality.** A theory must handle the grandfather paradox, for example through self‑consistent histories (the Novikov principle), and make testable predictions about it.

The part of the story that survives is real and remarkable: time is a direction in a four‑dimensional geometry, "now" is not universal, clocks at different heights and speeds disagree by exact, predictable amounts, and spinning black holes store energy that can in principle be extracted.

## Run the lab

```bash
python Module_05_Time_Is_A_Map/simulation.py
python -m pytest tests/test_module_05.py
```

| Experiment | What it shows |
|---|---|
| `lorentz_boost`, `interval`, `simultaneity_shift` | $s^2$ is invariant; "now" shifts with velocity; timelike order never flips. |
| `gps_clock_rates` | +45.7 / −7.2 / +38.5 µs per day, computed from $GM$, $c$ and the orbit. |
| `kerr_metric`, `horizons`, `ergosurface`, `static_observer_norm` | Horizons, ergosphere, and why nothing can stand still inside it. |
| `penrose_gain`, `penrose_max_efficiency_*`, `irreducible_mass` | 20.7 % per split and 29.3 % in total for $a = 1$. |
| `ctc_scan` | Kerr's closed timelike curves exist only at $r < 0$. |

## Try it yourself

1. Use `simultaneity_shift` to find how fast you would have to move for Andromeda's "now" to shift by one year. What fraction of $c$ is that?
2. Change `A_GPS` in `gps_clock_rates` to find the orbit radius where the gravitational and velocity effects cancel exactly (the net shift is zero). Compare it with $\tfrac32 R_\text{Earth}$.
3. Plot `penrose_gain(0.9, r)` for $r$ between $r_+$ and 2. Where does the gain drop to zero, and why does that match the ergosurface?
4. Run `ctc_scan(a, theta=0.3)` for a few spins. Does moving off the equator ever bring the CTC region to $r > 0$?
5. Try `horizons(1.2)`. Explain in one sentence why the earlier draft's $a = 1.2$ black hole was not a black hole.

## References

- Kerr, R. P., "Gravitational field of a spinning mass as an example of algebraically special metrics", *Phys. Rev. Lett.* **11**, 237 (1963).
- Boyer, R. H. & Lindquist, R. W., "Maximal analytic extension of the Kerr metric", *J. Math. Phys.* **8**, 265 (1967).
- Carter, B., "Global structure of the Kerr family of gravitational fields", *Phys. Rev.* **174**, 1559 (1968).
- Penrose, R., "Gravitational collapse: the role of general relativity", *Riv. Nuovo Cimento* **1**, 252 (1969).
- Christodoulou, D., "Reversible and irreversible transformations in black‑hole physics", *Phys. Rev. Lett.* **25**, 1596 (1970).
- Gödel, K., "An example of a new type of cosmological solutions of Einstein's field equations of gravitation", *Rev. Mod. Phys.* **21**, 447 (1949).
- Tipler, F. J., "Rotating cylinders and the possibility of global causality violation", *Phys. Rev. D* **9**, 2203 (1974).
- Morris, M. S., Thorne, K. S. & Yurtsever, U., "Wormholes, time machines, and the weak energy condition", *Phys. Rev. Lett.* **61**, 1446 (1988).
- Hawking, S. W., "Chronology protection conjecture", *Phys. Rev. D* **46**, 603 (1992).
- Ashby, N., "Relativity in the Global Positioning System", *Living Rev. Relativ.* **6**, 1 (2003).
- Hafele, J. C. & Keating, R. E., "Around‑the‑world atomic clocks", *Science* **177**, 166 and 168 (1972).
- Putnam, H., "Time and physical geometry", *J. Philos.* **64**, 240 (1967). Rietdijk, C. W., "A rigorous proof of determinism derived from the special theory of relativity", *Philos. Sci.* **33**, 341 (1966).
- Penrose, R., *The Emperor's New Mind*, Oxford University Press (1989). The Andromeda example.
- Everett, H., "'Relative state' formulation of quantum mechanics", *Rev. Mod. Phys.* **29**, 454 (1957).
