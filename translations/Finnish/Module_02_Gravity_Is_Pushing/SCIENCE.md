# 🔬 Moduuli 2 — Tarinan takana oleva tiede

> [Oppitunti](readme.md) kerrotaan vuodesta 2420. Tämä sivu on vuoden 2025 todellisuustarkistus: mikä on vakiintunutta, missä tarinan väite pettää, ja mitä pitäisi olla totta, jotta se toimisi. Kaikki tässä voidaan tarkistaa [laboratoriokoodilla](../../../Module_02_Gravity_Is_Pushing/simulation.py).

## Vuoden 2420 väite yhdessä lauseessa

Painovoima ei ole veto: avaruus on täynnä nopeaa, isotropista vuota, ja kaksi massaa varjostavat toisiaan siltä, joten epätasapainoinen vuosi työntää ne yhteen.

## Taso 1 — Mikä on totta

Idealla on oikea nimi ja pitkä historia: **Le Sagen painovoima** (Nicolas Fatio de Duillier, 1690; Georges‑Louis Le Sage, 1748). Sitä ottivat vakavasti Kelvin, Maxwell ja Poincaré, ja geometria on oikein:

- Pieni kappale näkee toisen säteeltä $R$ etäisyydellä $d$ kiekona, joka peittää kartion puolikulmalla $\theta_0$, jossa $\sin\theta_0 = R/d$.
- Jos säteet saapuvat yhtä paljon joka suunnasta, puuttuva impulssi tuosta kartiosta on

$$F \;\propto\; \tfrac12\int_{\cos\theta_0}^{1} u\,du \;=\; \frac{1-\cos^2\theta_0}{4} \;=\; \frac{R^2}{4d^2}.$$

Se on **käänteinen neliölaki puhtaasta geometriasta**. Laboratorio vahvistaa sen heittämällä kaksi miljoonaa satunnaista sädettä ja laskemalla estetyt; voimalakia ei syötetä sisään.

Energiatiheyden $u$ vuola nopeudella $c$, kun kukin kappale absorboi poikkileikkauksen $\sigma = h\,m$ suhteessa massaansa, antaa

$$F = \frac{u\,\sigma_1\sigma_2}{4\pi r^2} = \frac{u\,h^2}{4\pi}\,\frac{m_1 m_2}{r^2}, \qquad\text{joten Newtonin vastaavuus vaatii}\qquad u = \frac{4\pi G}{h^2}.$$

## Taso 2 — Missä väite pettää

Fyysikot hylkäsivät Le Sagen painovoiman kolmen ongelman takia. Kaikki kolme näkyvät laboratoriossa lukuina, eivät mielipiteinä.

**1. Kyllästyminen (massasuhteellisuus).** Varjo kasvaa massan mukana vain niin kauan kuin kappale on lähes läpinäkyvä. Tasaiselle pallolle optisella säteellä $\tau = \mu R$ absorboitu osuus on

$$f(\tau) = 1 - \frac{1-(1+2\tau)e^{-2\tau}}{2\tau^2} \;\xrightarrow{\tau\ll 1}\; \tfrac43\tau.$$

Kun $\tau = 1$, varjo on jo vain 53 % „suhteessa massaan“ -arvosta. Oikea painovoima on suhteessa massaan paremmin kuin yksi osa $10^{13}$:sta (MICROSCOPE-ekvivalenssiperiaatetesti) eikä näytä mitattavaa itsevarjostusta (kuun laseretäisyysmittaus).

**2. Veto.** Kappale nopeudella $v$ isotropisen vuon läpi törmää siihen enemmän edestä kuin takaa. Absorboijalle voima on $F = \tfrac43\,\sigma u\,v/c$. Kun $u$ kiinnitetään $G$:llä, Maan kiertonopeus vaimenisi ajassa

$$t_\text{decay} = \frac{3\,h\,c}{16\pi G}.$$

**3. Kuumeneminen.** Absorboitu vuola on absorboitua energiaa: $P = \sigma u c = 4\pi G\,m\,c/h$.

**Dilemma.** Pieni $h$ pitää Maan läpinäkyvänä (hyvä ongelmalle 1), mutta silloin rata pysähtyy murto-osassa sekuntia ja Maa absorboi noin $10^{45}$ W. Suuri $h$ kesyttää vedon, mutta silloin Maa on läpinäkymätön eikä painovoima enää skaalaudu massan mukaan. Laboratoriotesti `test_no_coefficient_escapes_both_drag_and_saturation` pyyhkii 30 kertaluokkaa $h$:ssa eikä löydä arvoa, joka toimisi. Richard Feynman esittää saman argumentin teoksessa *The Feynman Lectures on Physics* (Vol. I, §7‑7).

Alkuperäisen oppitunnin „vedon kumoaminen“ — että vakaa vuola vakiolla nopeudella ei tuota vetoa — ei selviä. Veto tulee *kappaleen* liikkeestä vuon läpi, ei vuon kiihdyttämisestä.

## Taso 3 — Mitä pitäisi olla totta

Työntävän painovoiman pelastamiseksi tarvittaisiin kaikki nämä kerralla. Jokainen on selvä, testattava kohde:

- **Vuola, joka kantaa impulssia mutta ei energiaa aineeseen**, tai uudelleenemittoi täsmälleen sen mitä absorboi, joten kuumenemista ei ole. Mutta uudelleenemissio täyttää varjon ja tappaa voiman. Se on Maxwellin vastaväite (1875).
- **Veto, joka katoaa liikkuville kappaleille.** Tämä vaatii vuon olevan Lorentz-invariantti, kuten kvanttityhjiö, mutta Lorentz-invariantilla tyhjiöllä ei ole lepotilaa, josta työntää, eikä se anna nettovarjovoimaa lainkaan.
- **Pieniä, mitattavia poikkeamia**: painovoima heikkenee hieman kolmannen kappaleen takana (pimennyksen „varjostus“, jota etsi Majorana 1920 ja myöhemmin pimennysgravimetria, ilman vahvistettua vaikutusta) ja pieniä massasuhteellisuuden rikkomuksia hyvin tiheissä kappaleissa.

Moderni fysiikka kuvaa painovoiman avaruusajan kaareutumisena (yleinen suhteellisuusteoria), joka läpäisee jokaisen testin tähän mennessä, mukaan lukien gravitaatioaallot (LIGO, 2015) ja mustien aukkojen kuvantaminen (EHT, 2019). Työntömallin pitäisi toistaa nekin.

## Aja laboratorio

```bash
python Module_02_Gravity_Is_Pushing/simulation.py
python -m pytest tests/test_module_02.py
```

| Koe | Mitä se näyttää |
|---|---|
| `shadow_force` | Monte Carlo -sädelaskenta antaa $1/d^2$:n ilman syötettyä voimalakia. |
| `absorbed_fraction`, `mass_proportionality` | Varjot lakkaavat seuraamasta massaa, kun kappaleet muuttuvat läpinäkymättömiksi. |
| `drag_and_heating` | Vuon säätäminen $G$:n toistamiseksi pakottaa valinnan vedon ja kuumenemisen sekä kyllästymisen välillä. |

## Kokeile itse

1. Muuta `R2` funktiossa `shadow_force`. Millä etäisyydellä Monte Carlo -tulos lakkaa vastaamasta yksinkertaista $R^2/4d^2$-lakia, ja miksi?
2. Käytä `absorbed_fraction`-funktiota löytääksesi optisen säteen, jossa kappaleen varjo on 1 % heikompi kuin „suhteessa massaan“.
3. Tee `drag_and_heating` uudelleen Kuulle (7,35 × 10²² kg, 1,02 km/s Maan ympäri). Onko dilemma yhtään helpompi?
4. Katso MICROSCOPE-tulos (Touboul et al., 2022). Muunna sen raja testimassan maksimaaliseksi sallituksi optiseksi säteeksi.

## Viitteet

- Feynman, Leighton & Sands, *The Feynman Lectures on Physics*, Vol. I, §7‑7 "What is gravity?" (1963).
- Edwards, M. R. (ed.), *Pushing Gravity: New Perspectives on Le Sage's Theory of Gravitation*, Apeiron (2002). A sympathetic collection that also sets out the historical objections.
- Poincaré, H., *Science and Method*, Book III (1908). The heating objection.
- Maxwell, J. C., "Atom", *Encyclopaedia Britannica*, 9th ed. (1875). The re‑emission objection.
- Touboul, P. et al., "MICROSCOPE mission: final results of the test of the equivalence principle", *Phys. Rev. Lett.* **129**, 121102 (2022).
- Abbott, B. P. et al. (LIGO/Virgo), "Observation of gravitational waves from a binary black hole merger", *Phys. Rev. Lett.* **116**, 061102 (2016).
