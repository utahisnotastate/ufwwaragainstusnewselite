# 🔬 Moduuli 10 — Tarinan takana oleva tiede

> [Oppitunti](readme.md) kerrotaan vuodesta 2420. Tämä sivu on vuoden 2025 todellisuustarkistus: mikä on vakiintunutta, missä tarinan väite pettää, ja mitä pitäisi olla totta, jotta se toimisi. Kaikki tässä voidaan tarkistaa [laboratoriokoodilla](../../../Module_10_Time_Reversal_Healing/simulation.py).

> ⚕️ **Terveysmuistutus.** Mikään tässä oppitunnissa ei ole lääketieteellistä neuvontaa tai hoitoa. Ajan kääntämiseen perustuvaa parantamista ei ole olemassa tänään. Jos olet sairas tai loukkaantunut, mene lääkäriin; leikkaukset ja lääkkeet pelastavat henkiä.

## Vuoden 2420 väite yhdessä lauseessa

„Vaihekonjugaattipeili“ voi tallentaa sairaan tai vanhentuneen kehon vääristyneen „aallon“, lähettää sen takaisin ajassa käännettynä ja siten kumota vaurion, palauttaen kehon aiemman, terveen tilan.

## Taso 1 — Mikä on totta

**Vaihekonjugaatio on oikeaa optiikkaa.** Vuonna 1972 Zel'dovich ja työtoverit osoittivat, että stimuloidussa Brillouin-sironnassa heijastunut valo palaa aaltorintamaltaan käännettynä: sisään tullessaan sekaisin mennyt säde palaa ulos sekaannus purettuna. Pian sen jälkeen Hellwarth ja Yariv osoittivat saman degeneroidulla neliaaltosekoituksella $\chi^{(3)}$- (Kerr-tyyppisessä) epälineaarisessa aineessa. Jos saapuva kenttä on

$$E(\mathbf r, t) = \mathrm{Re}\big[A(\mathbf r)\,e^{i(kz-\omega t)}\big],$$

vaihekonjugaattipeili palauttaa $A^*(\mathbf r)\,e^{i(-kz-\omega t)}$. Monokromaattiselle aallolle se on täsmälleen ajassa käännetty aalto: jokainen säde kulkee polkunsa taaksepäin.

**Miksi se kumoaa vääristymän.** Ohut aberroiva kerros kertoo kentän $e^{i\phi(x)}$:llä. Vaihekonjugaation jälkeen kenttä kantaa $e^{-i\phi(x)}$:ää, ja saman kerroksen ylittäminen uudelleen antaa $e^{-i\phi}e^{+i\phi} = 1$. Vapaan tilan eteneminen on unitaarinen, joten se kumotaan samalla tavalla. Laboratorio lähettää säteen 2 radiaanisen satunnaisvaihepeilin läpi ja takaisin: konjugaattipeili palauttaa alkuperäisen säteen fideliteetillä $1.000000$, kun tavallinen peili palauttaa fideliteetin $0.0025$.

**Kudoksen läpi tarkentaminen on oikea tutkimusala.** Biologinen kudos sirottaa valoa monta kertaa. Yaqoob et al. (2008) käyttivät optista vaihekonjugaatiota kumoamaan sirontaa kananrintakudosviipaleiden läpi („sameuden vaimennus“). Vellekoop ja Mosk (2007) tarkensivat valoa *läpi* läpinäkymättömän kerroksen säätämällä sisääntulevan säteen $N$:n segmentin vaiheita. Täysin kehittyneelle speklelle odotettu kirkkausvahvistus on

$$\eta = \frac{\pi}{4}(N-1) + 1.$$

Laboratorio toistaa tämän lain satunnaisilla siirtomatriiseilla (esimerkiksi $N = 1024$ antaa $805$ ennustettua $804.5$:ttä vastaan). Näitä menetelmiä kehitetään kuvantamiseen ja valon toimittamiseen syvälle kudokseen.

**Biosähköisyys on oikeaa, mitattavaa fysiikkaa.** Jokainen solu pitää jännitettä kalvonsa yli. Yhdelle ionilajille tasapaino- (Nernst-) potentiaali on

$$E_\text{ion} = \frac{RT}{zF}\ln\frac{[\text{ion}]_\text{out}}{[\text{ion}]_\text{in}},$$

joka antaa $E_K = -89$ mV lämpötilassa 37 °C arvoilla $[K]_o = 5$ mM, $[K]_i = 140$ mM. Useilla ioneilla lepojännite määräytyy Goldman–Hodgkin–Katz -yhtälöstä:

$$V_m = \frac{RT}{F}\ln\frac{P_K[K]_o + P_{Na}[Na]_o + P_{Cl}[Cl]_i}{P_K[K]_i + P_{Na}[Na]_i + P_{Cl}[Cl]_o}.$$

Oppikirjan nisäkäsarvoilla laboratorio saa $-67$ mV. Michael Levinin ryhmä ja muut tutkivat, miten näiden jännitteiden kuviot auttavat ohjaamaan alkionkehitystä ja regeneraatiota eläimissä kuten sammakoissa ja litamadoissa (Levin, 2021). Tämä on aktiivista perustutkimusta, ei terapiaa.

**Elämä laskee omaa entropiaansa koko ajan, laillisesti.** Lepäävä ihminen vapauttaa noin 100 W lämpöä. Päivässä $8.6\times10^6$ J lähtee kehosta lämpötilassa 310 K ja vie mukanaan $Q/T_\text{body} \approx 27{,}900$ J/K entropiaa, ja saapuu 293 K:n huoneeseen arvolla $Q/T_\text{room} \approx 29{,}500$ J/K. Solut korjaavat DNA:ta, vaihtavat proteiineja ja parantavat haavoja maksamalla paikallisesta järjestyksestä suuremmalla entropian viennillä. Toinen pääsääntö pätee keholle plus ympäristölle.

## Taso 2 — Missä väite pettää

**1. Vaihekonjugaattipeili kääntää aallon, ei ainetta.** Yllä oleva kumoaminen toimii, koska *sama* kerros ylitetään kahdesti. Se kääntää valokentän; se ei käännä atomeja, joiden läpi valo kulki. Keho ei ole heijastettava aalto: sen solut, proteiinit ja DNA ovat ainetta, johon tarinan peili ei koskaan vaikuta.

**2. Väliaineen ei saa muuttua kulkujen välillä.** Jos aberroiva kerros muuttuu, paluumatka ei enää kumoa ensimmäistä. Gaussin vaihepeileille rms-vaiheella $\sigma$ ja korrelaatiolla $\rho$ kulkujen välillä fideliteetti on

$$F = e^{-2\sigma^2(1-\rho)}.$$

Laboratorio mittaa $F = 0.92$ arvolla $\rho = 0.99$, $0.44$ arvolla $\rho = 0.9$ ja noin $0$ arvolla $\rho = 0.5$ (teoria $0.92$, $0.45$, $0.02$). Elävä kudos järjestytyy jatkuvasti uudelleen, ja in vivo -optiset kokeet on korjattava lyhyissä ikkunoissa (tyypillisesti millisekunneissa). Tarina haluaa „kääntää“ muutoksia, jotka ovat kertyneet *vuosikymmenten* aikana, kun $\rho \approx 0$ ja fideliteetti on nolla. Sirontakudosmallissa ennen kudoksen liikettä opittu korjaus antaa vahvistuksen $0.92$: ei parempi kuin ei korjausta lainkaan.

**3. Peilin on kaapattava koko kenttä.** Laboratorio näyttää tarkan tuloksen: muuttumattomalla väliaineella fideliteetti on yhtä suuri kuin peilin sieppaaman tehon osuus (ero alle $10^{-15}$). Mikä karkaa, on lopullisesti menetetty. Valon hallitsemiseksi vain 1 cm² kudoksesta 800 nm:ssä tarvittaisiin noin $6\times10^{8}$ itsenäistä moodia. Mikään tarinassa ei selitä, miten kaapataan jokaisen molekyylin „aalto“ kehossa.

**4. „Nuorta kuviota“ ei ole tallennettu „aikakanavaan“.** Fysiikalla ei ole tallennetta kehon menneestä tilasta odottamassa toistoa. Tieto siitä, miten solusi olivat järjestäytyneet 20-vuotiaana, on levinnyt ympäristöön lämpönä — sama entropian vienti kuin yllä. Energia ei ole rajoite (100 W voisi periaatteessa maksaa noin $3\times10^{22}$ bitin pyyhkimisen sekunnissa Landauerin rajalla $kT\ln 2$). Puuttuu tieto ja mekanismi, joka toimii jokaiseen molekyyliin.

**5. „Priore-kone“.** Antoine Priore rakensi sähkömagneettisia laitteita Ranskassa 1960–70-luvuilla ja raportoi vaikutuksia kasvaimiin ja infektioihin eläimissä. Tuloksia ei koskaan toistettu tai validoitu itsenäisesti, eivätkä laitteet ole hyväksytty hoito.

**6. Kirurgia ja lääketiede eivät ole „tietokoneen lyömistä vasaralla“.** Moderni lääketiede rakentuu vahvasti fysiikkaan ja kemiaan, ja se toimii: rokotteet, antibiootit, anestesia ja kirurgia pelastavat miljoonia henkiä. Oppitunnin vastakkainasettelu on osa fiktiota.

## Taso 3 — Mitä pitäisi olla totta

Jotta „ajan kääntämiseen perustuva parantaminen“ olisi olemassa, kaikkien näiden pitäisi päteä. Jokainen on konkreettinen tavoite:

- **Fyysinen kantaja kehon tilalle**, joka voidaan „heijastaa“. Testi: osoita, että jokin kenttä kehon ulkopuolella koodaa kudoksen rakenteen solutarkkuudella ja voidaan mitata.
- **Tallennettu menneen tilan ennätys.** Testi: palauta todennettavissa oleva aiempi tila (esimerkiksi vanha arpikuvio) tänään tehdystä mittauksesta, ilman aiempia valokuvia tai näytteitä.
- **Mekanismi, joka muuttaa palautetun aallon uudelleenjärjestetyiksi molekyyleiksi** tavoilla, jotka vastaavat tunnettua kemiaa eivätkä kypsennä kudosta.
- **Koherenssi ajan yli.** Minkä tahansa „kääntämisen“ pitäisi toimia, vaikka keho muuttuu millisekunti–vuosi -aikaskaaloilla, mikä tuhoaa konjugaatiofideliteetin kuten yllä näytettiin.

**Oikeita avoimia kysymyksiä, jotka ovat lähempänä tarinan henkeä:**

- Kuinka pitkälle aaltorintaman muotoilu ja optinen vaihekonjugaatio voivat viedä tarkennusta, kuvantamista ja valon toimittamista syvälle elävään kudokseen?
- Voidaanko biosähköisiä signaaleja käyttää regeneraation ohjaamiseen eläimissä ja myöhemmin turvallisesti ihmisissä? (Varhaista tutkimusta; ei hyväksyttyjä terapioita.)
- Mikä asettaa kehon oman korjauksen rajat, ja voiko biologia (esimerkiksi kantasolu- ja regeneratiivinen lääketiede) laajentaa niitä?

## Aja laboratorio

```bash
python Module_10_Time_Reversal_Healing/simulation.py
python -m pytest tests/test_module_10.py
```

| Koe | Mitä se näyttää |
|---|---|
| `round_trip` | Vaihekonjugaatio kumoaa satunnaisen aberraation tarkasti; tavallinen peili ei. |
| `round_trip(rho=...)`, `decorrelation_fidelity_theory` | Jos väliaine muuttuu kulkujen välillä, fideliteetti putoaa kuten $e^{-2\sigma^2(1-\rho)}$. |
| `round_trip(aperture=...)` | Fideliteetti on yhtä suuri kuin peilin kaappaaman kentän osuus. |
| `wavefront_shaping_enhancement`, `vellekoop_mosk_theory` | Tarkentaminen sirontaväliaineiden läpi noudattaa $\tfrac{\pi}{4}(N-1)+1$:tä ja menetetään, jos väliaine muuttuu. |
| `nernst`, `ghk_voltage` | Todelliset kalvojännitteet ionipitoisuuksista (noin $-67$ mV levossa). |
| `entropy_budget`, `landauer_bits_per_second` | Elämä laskee paikallista entropiaa viemällä enemmän ulos; toinen pääsääntö pätee kokonaisuudessaan. |

## Kokeile itse

1. Funktiossa `round_trip` nosta `rms_rad` arvosta 2 arvoon 4. Kuinka paljon hitaammin väliaine saa muuttua (kuinka lähellä 1:tä $\rho$:n on oltava), jotta fideliteetti pysyy 90 %:ssa? Tarkista vasten $e^{-2\sigma^2(1-\rho)}$.
2. Käytä `with_changes`-funktiota löytääksesi solunulkoisen kaliumtason, jossa lepojännite saavuttaa $-55$ mV. (Lääkärit seuraavat veren kaliumia tarkasti tästä syystä.)
3. Aja `wavefront_shaping_enhancement` väliaineella, joka muuttuu vain *osittain*: sekoita vanha ja uusi siirtomatriisi muodossa $\sqrt{\rho}\,t_\text{old} + \sqrt{1-\rho}\,t_\text{new}$. Miten vahvistus putoaa $\rho$:n mukana?
4. Tee `entropy_budget` uudelleen huoneelle lämpötilassa 35 °C. Mitä tapahtuu nettopentropiantuotannolle, ja miksi kuumat ympäristöt tekevät lämmön poistamisesta vaikeampaa?

## Viitteet

- Zel'dovich, B. Ya., Popovichev, V. I., Ragul'skii, V. V. & Faizullov, F. S., "Connection between the wave fronts of the reflected and exciting light in stimulated Mandel'shtam‑Brillouin scattering", *JETP Lett.* **15**, 109 (1972).
- Hellwarth, R. W., "Generation of time‑reversed wave fronts by nonlinear refraction", *J. Opt. Soc. Am.* **67**, 1 (1977).
- Yariv, A., "Phase conjugate optics and real‑time holography", *IEEE J. Quantum Electron.* **14**, 650 (1978).
- Vellekoop, I. M. & Mosk, A. P., "Focusing coherent light through opaque strongly scattering media", *Opt. Lett.* **32**, 2309 (2007).
- Yaqoob, Z., Psaltis, D., Feld, M. S. & Yang, C., "Optical phase conjugation for turbidity suppression in biological samples", *Nature Photonics* **2**, 110 (2008).
- Goldman, D. E., "Potential, impedance, and rectification in membranes", *J. Gen. Physiol.* **27**, 37 (1943).
- Hodgkin, A. L. & Katz, B., "The effect of sodium ions on the electrical activity of the giant axon of the squid", *J. Physiol.* **108**, 37 (1949).
- Levin, M., "Bioelectric signaling: Reprogrammable circuits underlying embryogenesis, regeneration, and cancer", *Cell* **184**, 1971 (2021).
- Landauer, R., "Irreversibility and heat generation in the computing process", *IBM J. Res. Dev.* **5**, 183 (1961).
