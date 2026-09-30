# 🔬 Module 8 — The Science Behind the Story

> The [lesson](readme.md) is told from the year 2420. This page is the 2025 reality check: what is established, where the story's claim breaks, and what would have to be true for it to work. Everything here can be checked with the [lab code](simulation.py).

## The 2420 claim in one sentence

Distance is an illusion: if you tune your body to the "frequency" of a destination you vanish here and appear there in zero time, with no speed limit, because you skipped space instead of crossing it.

## Level 1 — What's real

**General relativity does allow "moving space instead of moving you" — on paper.** Miguel Alcubierre (1994) wrote down a spacetime in which a bubble of flat space is carried along at any speed $v_s$, even faster than light. In units where $G = c = 1$:

$$ds^2 = -dt^2 + \big(dx - v_s f(r_s)\,dt\big)^2 + dy^2 + dz^2,$$

$$f(r) = \frac{\tanh\!\big(\sigma(r+R)\big) - \tanh\!\big(\sigma(r-R)\big)}{2\tanh(\sigma R)},$$

where $r_s$ is the distance from the bubble centre $x_s(t)$, $R$ is the bubble radius and $1/\sigma$ sets the wall thickness. $f = 1$ inside (the passenger floats in free fall, feeling no acceleration) and $f \to 0$ far away.

- **Space shrinks in front and grows behind.** The expansion of the volume elements of observers at rest in the slicing (York expansion) is

$$\theta = v_s\,\frac{x - x_s}{r_s}\,\frac{df}{dr_s},$$

which is negative ahead of the bubble, positive behind it, and zero inside and far away. The lab confirms all four properties numerically.

- **The price is negative energy.** Einstein's equations tell you what matter would be needed to make this geometry. For observers at rest in the slicing, the energy density is

$$T^{00} = -\frac{1}{8\pi}\,\frac{v_s^2\,(y^2+z^2)}{4\,r_s^2}\left(\frac{df}{dr_s}\right)^2 \;\le\; 0 .$$

It is **negative everywhere it is non-zero**: a violation of the weak energy condition. Integrating over all space (the lab does this numerically, and checks it against a brute‑force 3‑D sum) gives, for a thin wall,

$$E \;\approx\; -\frac{v_s^2 R^2 \sigma}{36} \qquad (G=c=1),$$

so the energy bill grows with the square of speed, with the square of bubble size, and in inverse proportion to the wall thickness.

- **Negative energy density exists — a little.** Between two parallel mirrors a distance $d$ apart, the quantum vacuum has energy density $u = -\pi^2\hbar c/(720\,d^4)$ (Casimir, 1948). The resulting force has been measured (e.g. Lamoreaux, 1997). At $d = 100$ nm, $u \approx -4$ J/m³.

- **"Teleportation" is a real word in physics — for information, not bodies.** Quantum teleportation (Bennett et al., 1993; first demonstrated by Bouwmeester et al., 1997) transfers the quantum *state* of a particle to another particle that is already at the destination. It needs an ordinary classical message, sent at or below the speed of light, to finish the job. Nothing travels faster than light and no matter is moved.

- **Two bells.** Sympathetic resonance is real, but the second bell rings because sound waves carry energy across the room at about 343 m/s. It is a slow, ordinary transfer through the air, not a jump.

## Level 2 — Where the claim breaks

**1. The quantum inequalities crush the wall.** Quantum field theory allows negative energy, but only a little, and only briefly. For a massless scalar field in flat spacetime, an observer who averages the energy density with a Lorentzian weighting of width $t_0$ always finds (Ford & Roman)

$$\langle\rho\rangle \;\ge\; -\frac{3\hbar}{32\pi^2 c^3\,t_0^4}.$$

The shorter the time, the more negative energy is allowed, but the bound tightens as $t_0^{-4}$. Pfenning & Ford (1997) applied this to the Alcubierre bubble with sampling times short compared with the wall's curvature scale and found that the wall can be at most of order a hundred Planck lengths thick for $v_s \sim c$, and that the total negative energy then far exceeds the mass of the visible universe.

The lab reproduces the *order of magnitude* with a simpler shortcut: it requires the most negative $T^{00}$ on the wall to respect the bound with $t_0 = 0.1\,\Delta/c$ ($\Delta$ = wall thickness). For a 100 m bubble at $v_s = c$:

| Quantity | Lab value |
|---|---|
| Largest allowed wall thickness | $1.6\times10^{-33}$ m ≈ 98 Planck lengths |
| Total negative energy | $\approx -4\times10^{79}$ J |
| Mass equivalent | $\approx -5\times10^{62}$ kg (about $10^{32}$ Suns) |

Ordinary matter in the entire observable universe is of order $10^{53}$ kg. The shortcut is cruder than Pfenning & Ford's calculation, so trust only its order of magnitude at $v_s \sim c$, not its dependence on speed.

**2. Even a "reasonable" wall is out of reach.** Forget the quantum inequality and allow a 1 m thick wall: the lab gives a total of about $-400$ Jupiter masses, with peak energy density $\approx -10^{42}$ J/m³. Getting that from Casimir plates would need them about $4\times10^{-18}$ m apart, roughly 400 times smaller than a proton. The best laboratory negative energy is short by more than 40 orders of magnitude.

**3. Faster than light means cause and effect can swap.** If a signal covers distance $\Delta x$ in time $\Delta t$ at speed $u > c$, an observer moving at speed $V$ measures

$$\Delta t' = \gamma\,\Delta t\left(1 - \frac{uV}{c^2}\right),$$

which is **negative** for any $V > c^2/u$, a perfectly ordinary sub‑light speed. For $u = 10c$, anyone moving faster than $0.1c$ sees the traveller arrive before leaving. Two such trips can be combined into a round trip that returns before it started. Everett (1996) showed this applies to warp drives specifically. For $u \le c$ the lab finds no observer who sees the order reversed.

**4. "Superluminal matter waves" carry nothing.** The original proof leans on de Broglie waves being "effectively superluminal in phase". That part is true: the phase velocity is $v_p = c^2/v > c$. But the particle, its energy and any message move at the group velocity $v_g = d\omega/dk = v$, and $v_p v_g = c^2$ exactly. For a 25 kg child walking at 1 m/s the lab gives $v_p \approx 9\times10^{16}$ m/s and $v_g = 1.000$ m/s.

**5. "Match the destination's resonance and appear" has no physical basis.** No measured property of a place works like a radio frequency that a body could tune to, and no known mechanism moves matter because two things vibrate alike. This is the part of the story that is pure story. It is a lovely image; it just isn't how physics works. Every known way of getting matter or information from here to there either takes at least the light‑travel time (rockets, radio, quantum teleportation with its classical message) or, like the warp bubble, exists only on paper and needs matter nobody has ever seen.

**6. Continuity of the traveller.** The homework answer ("you are not faxed, you slide") is a philosophical position, not physics. Quantum teleportation *destroys* the original state as it recreates it elsewhere (the no‑cloning theorem forbids keeping both), which is closer to the "fax" picture than the lesson admits.

## Level 3 — What would have to be true

- **A source of negative energy that evades or is not bound by the quantum inequalities**, at densities of $10^{40}$ J/m³ or more, sustained over macroscopic regions. Any laboratory evidence of negative energy density far beyond the Casimir effect would be a first step.
- **A way around the causality problem.** Either a preferred reference frame that breaks the relativity of simultaneity (tightly constrained by tests of Lorentz invariance), or a principle that forbids closed loops (Hawking's chronology protection conjecture proposes that nature does exactly this; it is unproven).
- **Better geometry.** Research has chipped away at the numbers but not the core problem:
  - Van Den Broeck (1999) found a bubble with a tiny outer surface and a large interior, reducing the total energy to a few solar masses, which is still negative energy on an astronomical scale.
  - Lentz (2021) proposed superluminal "solitons" claimed to need only positive energy; other authors have argued that this claim does not hold.
  - Bobrick & Martire (2021) gave a general framework and concluded that **superluminal** warp drives still require negative energy, while subluminal ones can in principle be built from positive energy.
  - Fell & Heisenberg (2021) constructed a subluminal warp solution sourced by positive energy.
- **Testable targets**: any laboratory observation of negative energy density exceeding the quantum‑inequality bound for its sampling time; any signal that arrives before it could have been sent by light, which would also show up as a violation of Lorentz invariance in precision tests.

## Run the lab

```bash
python Module_08_Instant_Travel/simulation.py
python -m pytest tests/test_module_08.py
```

| Experiment | What it shows |
|---|---|
| `shape_function`, `york_expansion` | Space contracts ahead of the bubble and expands behind; flat inside and far away. |
| `energy_density` | $T^{00} \le 0$ everywhere: the weak energy condition is violated. |
| `total_energy`, `total_energy_thin_wall` | Numerical integral of all the negative energy; scales as $v_s^2 R^2/\Delta$. |
| `qi_bound`, `max_wall_thickness_qi`, `warp_energy_budget` | The quantum inequality forces Planck‑thin walls and $\sim10^{62}$ kg of negative energy. |
| `casimir_energy_density`, `casimir_gap_for` | Laboratory negative energy is many orders of magnitude too small. |
| `order_reversal_factor`, `reversing_frame_speed` | Faster than light + relativity = effects before causes for some observers. |
| `de_broglie_velocities` | Phase velocity exceeds $c$, group velocity (the actual particle) does not. |

## Try it yourself

1. Use `total_energy` to find how the total energy changes when you double the bubble radius $R$ while keeping the wall thickness fixed. Explain the answer from the thin‑wall formula.
2. Change `sampling_fraction` in `max_wall_thickness_qi` from 0.1 to 0.5. How much do the wall thickness and total energy change? Why does the conclusion survive?
3. Using `order_reversal_factor`, find the slowest observer who sees a signal sent at $1.01c$ arrive before it left. What happens as $u \to c$?
4. Find the Casimir plate separation that gives the energy density of a 1 km wall at $v_s = 0.01c$. Is it larger than an atom?
5. Compute the light‑travel time to Proxima Centauri (4.24 light‑years) and compare it with the time a 0.1c probe would take.

## References

- Alcubierre, M., "The warp drive: hyper‑fast travel within general relativity", *Class. Quantum Grav.* **11**, L73 (1994).
- Ford, L. H. & Roman, T. A., "Averaged energy conditions and quantum inequalities", *Phys. Rev. D* **51**, 4277 (1995).
- Ford, L. H. & Roman, T. A., "Restrictions on negative energy density in flat spacetime", *Phys. Rev. D* **55**, 2082 (1997).
- Pfenning, M. J. & Ford, L. H., "The unphysical nature of 'warp drive'", *Class. Quantum Grav.* **14**, 1743 (1997).
- Everett, A. E., "Warp drive and causality", *Phys. Rev. D* **53**, 7365 (1996).
- Van Den Broeck, C., "A 'warp drive' with more reasonable total energy requirements", *Class. Quantum Grav.* **16**, 3973 (1999).
- Lentz, E. W., "Breaking the warp barrier: hyper‑fast solitons in Einstein–Maxwell‑plasma theory", *Class. Quantum Grav.* **38**, 075015 (2021).
- Bobrick, A. & Martire, G., "Introducing physical warp drives", *Class. Quantum Grav.* **38**, 105009 (2021).
- Fell, S. D. B. & Heisenberg, L., "Positive energy warp drive from hidden geometric structures", *Class. Quantum Grav.* **38**, 155020 (2021).
- Casimir, H. B. G., "On the attraction between two perfectly conducting plates", *Proc. K. Ned. Akad. Wet.* **51**, 793 (1948).
- Lamoreaux, S. K., "Demonstration of the Casimir force in the 0.6 to 6 μm range", *Phys. Rev. Lett.* **78**, 5 (1997).
- Hawking, S. W., "Chronology protection conjecture", *Phys. Rev. D* **46**, 603 (1992).
- Bennett, C. H. et al., "Teleporting an unknown quantum state via dual classical and Einstein–Podolsky–Rosen channels", *Phys. Rev. Lett.* **70**, 1895 (1993).
- Bouwmeester, D. et al., "Experimental quantum teleportation", *Nature* **390**, 575 (1997).
