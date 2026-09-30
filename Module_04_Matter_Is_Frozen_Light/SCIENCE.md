# 🔬 Module 4 — The Science Behind the Story

> The [lesson](readme.md) is told from the year 2420. This page is the 2025 reality check: what is established, where the story's claim breaks, and what would have to be true for it to work. Everything here can be checked with the [lab code](simulation.py).

## The 2420 claim in one sentence

Matter is light trapped in a tiny spinning loop (a torus), so an electron is a photon running in a circle, and mass is just "frozen light".

## Level 1 — What's real

**Mass and energy really are the same currency.** Einstein's $E = mc^2$ (1905) is one of the best‑tested equations in physics. Whenever energy leaves a system, mass leaves with it:

| Process | Energy released | Mass that disappears |
|---|---|---|
| Burning 1 kg of dry wood | $1.6\times10^{7}$ J | $1.8\times10^{-7}$ g ($2\times10^{-10}$ of the wood) |
| A 15‑kiloton fission bomb | $6.3\times10^{13}$ J | 0.7 g |

So the lesson's "burning a log unties the knots" contains something true: the ash and gases really are lighter by $\Delta m = E/c^2$. But the atoms are all still there. Only a fraction $10^{-10}$ of the mass goes.

**Most of your mass really is energy, just not light.** A proton weighs 938.27 MeV/c². The rest masses of its three valence quarks (up, up, down; about 2.2 + 2.2 + 4.7 MeV in the Particle Data Group's scheme) add up to only about **1 %** of that. The rest is the energy of quarks moving at close to the speed of light and of the gluon field that binds them, described by quantum chromodynamics (QCD). Lattice QCD computes hadron masses from this with a few percent accuracy (Dürr et al., 2008). Counting the quark‑mass contribution of the virtual "sea" quarks as well (including strange quarks) raises the quark‑mass share to roughly 10 %, still a small part. In that sense "mass is mostly field energy" is real physics, and it is a deeper statement than the story makes.

**Matter really turns into light, and light into matter.**

- *Matter → light.* An electron and a positron annihilate into two 511 keV photons. Hospital PET scanners detect exactly these photon pairs every day.
- *Light → matter.* Breit and Wheeler (1934) calculated that two photons can make an electron–positron pair if they carry enough energy between them. With energies $E_1, E_2$ meeting at angle $\theta$, the invariant $s = 2E_1E_2(1-\cos\theta)$ must reach $(2m_ec^2)^2$:

$$E_1E_2(1-\cos\theta) \;\ge\; 2(m_ec^2)^2.$$

Head‑on, two 511 keV photons are exactly at threshold. Above it the cross section is

$$\sigma_{\gamma\gamma} = \frac{\pi r_e^2}{2}(1-\beta^2)\left[(3-\beta^4)\ln\frac{1+\beta}{1-\beta} - 2\beta(2-\beta^2)\right], \qquad \beta = \sqrt{1 - \frac{4m_e^2c^4}{s}},$$

where $r_e$ is the classical electron radius and $\beta$ is each lepton's speed in the centre‑of‑mass frame. It peaks at $1.70\times10^{-25}$ cm² $\approx 0.256\,\sigma_T$ near $\beta = 0.70$. The lab checks the formula independently: rebuilding it from Dirac's (1930) formula for the reverse process $e^+e^-\to\gamma\gamma$, using detailed balance $\sigma_{\gamma\gamma} = 2\beta^2\sigma_\text{ann}$, agrees to $10^{-13}$.

**Experiments.** SLAC experiment E‑144 (Burke et al., 1997) back‑scattered a 527 nm laser off 46.6 GeV electrons to make gamma rays of up to 29.2 GeV, which then collided with the same intense laser. Kinematics alone says that at least 4 laser photons had to be absorbed at once, so this was *nonlinear, multiphoton* Breit–Wheeler. STAR at RHIC (Adam et al., 2021) saw $e^+e^-$ pairs from the intense electromagnetic fields of gold nuclei passing close to each other, which act as clouds of *quasi‑real* photons. A clean collision of two beams of real photons has not yet been done; proposals exist (Pike et al., 2014).

**Pulling pairs out of the vacuum.** A strong enough electric field can create pairs directly. The scale is where a field gives an electron its rest energy over one Compton length (Sauter, Heisenberg–Euler, Schwinger):

$$E_\text{crit} = \frac{m_e^2c^3}{e\hbar} \approx 1.32\times10^{18}\ \text{V/m}, \qquad I_\text{crit} \approx 2.3\times10^{29}\ \text{W/cm}^2.$$

## Level 2 — Where the claim breaks

**1. "An electron is a photon running in a circle" gets its one success for free.** The model (Williamson & van der Mark, 1997) places a charge $e$ moving at $c$ on a loop of radius $r = \hbar/(m_ec) = 3.86\times10^{-13}$ m, the reduced Compton wavelength. A circulating charge has magnetic moment

$$\mu = I\cdot\pi r^2 = \frac{ec}{2\pi r}\,\pi r^2 = \frac{ecr}{2} = \frac{e\hbar}{2m_e} = \mu_B,$$

exactly the Bohr magneton. But $r$ was chosen from $m_e$, and $\mu_B$ is *defined* as $e\hbar/2m_e$, so this is an algebraic identity. The lab shows that the same recipe gives "the right magneton" for any mass you choose. It cannot fail, so it predicts nothing.

**2. It misses what the electron actually does.** The measured moment is not $\mu_B$ but $1.00115965218059\,\mu_B$ (Fan et al., 2023). Quantum electrodynamics predicts that extra 0.116 %:

$$a_e = \frac{g-2}{2} = \frac{1}{2}\frac{\alpha}{\pi} - 0.3285\left(\frac{\alpha}{\pi}\right)^2 + 1.1812\left(\frac{\alpha}{\pi}\right)^3 - 1.9122\left(\frac{\alpha}{\pi}\right)^4 + \dots$$

The lab uses $\alpha$ from rubidium atom‑recoil measurements (Morel et al., 2020), which does not depend on $g-2$, so the comparison is not circular:

| Model | predicted $g/2$ | off by |
|---|---|---|
| photon loop | 1 (exactly) | $1.2\times10^{-3}$ |
| QED, 1 loop (Schwinger's $\alpha/2\pi$) | 1.0011614 | $1.8\times10^{-6}$ |
| QED, 2 loops | 1.001159637 | $1.5\times10^{-8}$ |
| QED, 3 loops | 1.00115965223 | $5\times10^{-11}$ |
| QED, 4 loops | 1.00115965218 | $5\times10^{-12}$ |

The remaining $5\times10^{-12}$ is the expected size of terms the lab leaves out (five‑loop QED, loops of heavier muons and taus, hadronic and weak effects). QED is about $10^{8}$ times closer than the loop model.

**3. The electron is far smaller than the loop.** High‑energy electron–positron scattering at LEP shows no sign of electron structure down to about $10^{-18}$ m. The model's loop is $4\times10^{5}$ times larger. Structure that big would change how electrons scatter at energies probed decades ago.

**4. Other things the model has to explain but doesn't.** A photon has no charge, so where does the electron's charge $-e$ come from? A photon has spin 1; the electron has spin ½. The muon and tau have exactly the same charge as the electron but different masses. And a single photon, however energetic, has $s = 0$ and can never become a massive particle by itself; something else (a nucleus, a second photon, a strong field) is always needed. Light does not bend into a closed loop by itself either.

**5. Light is not a practical source of matter.** Two 2 eV sunlight photons fall short of the pair threshold by a factor of $6.5\times10^{10}$ in $s$; a sunlight photon would need a 131 GeV gamma ray as a partner. Tearing pairs from the vacuum with a field is controlled by the factor $e^{-\pi E_\text{crit}/E}$. The most intense laser so far, about $1.1\times10^{23}$ W/cm² (Yoon et al., 2021), reaches $9\times10^{14}$ V/m $= 7\times10^{-4}\,E_\text{crit}$, giving a factor of about $10^{-1983}$. (Real laser pulses oscillate and are focused, so the precise rate differs, but it stays utterly negligible.)

**6. Why things feel solid.** Not because of spinning light. Matter is stable and incompressible because electrons are fermions: the Pauli exclusion principle, together with electrostatics, keeps atoms from collapsing into each other (Dyson & Lenard, 1967; Lieb, 1976). The ceiling‑fan picture is a nice image, but the real mechanism is quantum statistics.

## Level 3 — What would have to be true

A "frozen light" model of the electron would need to pass all of these tests, each of which has a precise measured target:

- **Predict $a_e = 0.00115965218\ldots$** with no parameter fitted to it, as QED does from $\alpha$ alone.
- **Explain charge, spin ½, and three generations** (electron, muon, tau) with one mechanism, and predict their mass ratios (206.77 and 3477.2). The Standard Model does not predict these masses either; they are an open question, so a model that did would be a major discovery.
- **Show structure at ~$10^{-13}$ m** in electron scattering (a "form factor"). Present data rule this out by more than five orders of magnitude.

Real open questions nearby: the first collision of two beams of real photons above the Breit–Wheeler threshold; experiments approaching the Schwinger field in the electron's own rest frame (strong‑field QED with lasers and high‑energy electron beams); and why the Higgs couplings, and so the quark and lepton masses, have the values they do.

## Run the lab

```bash
python Module_04_Matter_Is_Frozen_Light/simulation.py
python -m pytest tests/test_module_04.py
```

| Experiment | What it shows |
|---|---|
| `mass_defect`, `proton_valence_quark_fraction` | $E = mc^2$ at chemical and nuclear scales; quark rest masses are ~1 % of a proton. |
| `breit_wheeler_threshold`, `pair_beta`, `breit_wheeler_cross_section` | Light into matter: threshold and cross section. |
| `breit_wheeler_from_annihilation`, `dirac_annihilation_cross_section` | Independent check of the cross section by detailed balance. |
| `compton_edge`, `min_laser_photons` | Why SLAC E‑144 was a multiphoton process. |
| `schwinger_field`, `schwinger_suppression_log10` | How far today's lasers are from tearing pairs from the vacuum. |
| `loop_magnetic_moment`, `toroidal_model_moment`, `qed_anomaly` | The photon‑loop model's built‑in "success" and its miss, versus QED. |

## Try it yourself

1. How energetic must a gamma ray be to make pairs on the cosmic microwave background (typical photon energy about $6\times10^{-4}$ eV)? This is why the universe is opaque to the highest‑energy gamma rays.
2. Use `toroidal_model_moment` with the muon mass and compare with the measured muon anomaly $a_\mu \approx 0.00116592$. Does the loop model do any better for the muon?
3. Compute the rest energy of a 30 kg child with `mass_defect` in reverse ($E = mc^2$). How many 15‑kiloton bombs is that? Why doesn't anything like that ever happen by itself? (Hint: what conserved quantities would have to vanish?)
4. Plot `breit_wheeler_cross_section` against $s/(2m_ec^2)^2$ and check the high‑energy form $\sigma \approx \frac{4\pi r_e^2 m_e^2c^4}{s}\left[\ln\frac{s}{m_e^2c^4} - 1\right]$.
5. Replace `ALPHA_RB` with the caesium value $\alpha^{-1} = 137.035999046$ (Parker et al., 2018). How much does the 4‑loop prediction move, compared with the measurement uncertainty of $1.3\times10^{-13}$ in $g/2$?

## References

- Einstein, A., "Ist die Trägheit eines Körpers von seinem Energieinhalt abhängig?", *Ann. Phys.* **18**, 639 (1905).
- Breit, G. & Wheeler, J. A., "Collision of two light quanta", *Phys. Rev.* **46**, 1087 (1934).
- Dirac, P. A. M., "On the annihilation of electrons and protons", *Proc. Camb. Phil. Soc.* **26**, 361 (1930).
- Schwinger, J., "On quantum‑electrodynamics and the magnetic moment of the electron", *Phys. Rev.* **73**, 416 (1948).
- Schwinger, J., "On gauge invariance and vacuum polarization", *Phys. Rev.* **82**, 664 (1951).
- Burke, D. L. et al., "Positron production in multiphoton light‑by‑light scattering", *Phys. Rev. Lett.* **79**, 1626 (1997).
- Adam, J. et al. (STAR Collaboration), "Measurement of e⁺e⁻ momentum and angular distributions from linearly polarized photon collisions", *Phys. Rev. Lett.* **127**, 052302 (2021).
- Pike, O. J., Mackenroth, F., Hill, E. G. & Rose, S. J., "A photon–photon collider in a vacuum hohlraum", *Nat. Photon.* **8**, 434 (2014).
- Yoon, J. W. et al., "Realization of laser intensity over 10²³ W/cm²", *Optica* **8**, 630 (2021).
- Williamson, J. G. & van der Mark, M. B., "Is the electron a photon with toroidal topology?", *Ann. Fond. Louis de Broglie* **22**, 133 (1997).
- Fan, X., Myers, T. G., Sukra, B. A. D. & Gabrielse, G., "Measurement of the electron magnetic moment", *Phys. Rev. Lett.* **130**, 071801 (2023).
- Morel, L., Yao, Z., Cladé, P. & Guellati‑Khélifa, S., "Determination of the fine‑structure constant with an accuracy of 81 parts per trillion", *Nature* **588**, 61 (2020).
- Parker, R. H., Yu, C., Zhong, W., Estey, B. & Müller, H., "Measurement of the fine‑structure constant as a test of the Standard Model", *Science* **360**, 191 (2018).
- Laporta, S. & Remiddi, E., "The analytical value of the electron (g−2) at order α³ in QED", *Phys. Lett. B* **379**, 283 (1996).
- Laporta, S., "High‑precision calculation of the 4‑loop contribution to the electron g‑2 in QED", *Phys. Lett. B* **772**, 232 (2017).
- Workman, R. L. et al. (Particle Data Group), "Review of Particle Physics", *Prog. Theor. Exp. Phys.* **2022**, 083C01 (2022).
- Dürr, S. et al., "Ab initio determination of light hadron masses", *Science* **322**, 1224 (2008).
- Dyson, F. J. & Lenard, A., "Stability of matter. I", *J. Math. Phys.* **8**, 423 (1967).
- Lieb, E. H., "The stability of matter", *Rev. Mod. Phys.* **48**, 553 (1976).
