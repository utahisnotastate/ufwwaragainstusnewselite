# 🔬 Moduuli 11 — Tarinan takana oleva tiede

> [Oppitunti](readme.md) kerrotaan vuodesta 2420. Tämä sivu on vuoden 2025 todellisuustarkistus: mikä on vakiintunutta, missä tarinan väite pettää, ja mitä pitäisi olla totta, jotta se toimisi. Kaikki tässä voidaan tarkistaa [laboratoriokoodilla](../../../Module_11_Low_Energy_Transmutation/simulation.py).

## Vuoden 2420 väite yhdessä lauseessa

Ytimiä voidaan hellävaroen „taittaa uudelleen“ toisiksi alkuaineiksi huoneenlämmössä metallihilojen, entsyymien tai bakteerien avulla ilman korkeita energioita, joten kultaa voidaan kasvattaa ja ydinjäte muuttaa lannoitteeksi.

## Taso 1 — Mikä on totta

**Transmutaatio on totta.** Ytimet muuttuvat todella toisiksi alkuaineiksi: tähdissä, reaktoreissa, kiihdyttimissä ja radioaktiivisessa hajoamisessa. Elohopea‑196 voidaan jopa muuttaa kullaksi reaktorissa: $^{196}$Hg vangitsee neutronin ja tulee $^{197}$Hg:ksi, joka hajoaa elektronisieppauksella $^{197}$Au:ksi. Se toimii, mutta tuottaa mitättömiä määriä suurella kustannuksella.

**Coulombin seinä.** Kaksi ydintä varauksilla $Z_1e$, $Z_2e$ hylkivät toisiaan energialla $Z_1Z_2e^2/(4\pi\varepsilon_0 r)$, jossa $e^2/4\pi\varepsilon_0 = 1.44$ MeV·fm. Kosketusetäisyydellä ($r \approx 1.2(A_1^{1/3}+A_2^{1/3})$ fm) se on noin **0,48 MeV kahdelle deuteronille** ja **5,2 MeV protonille ja kalium‑39:lle**. Huoneenlämpö antaa hiukkasille noin $kT = 0.026$ eV: noin 20 miljoonaa kertaa liian vähän ylittämiseen.

**Tunnelointi.** Kvanttimekaniikka antaa ydinten tunneloida seinän läpi. Paljaalle Coulombin seinälle todennäköisyys on Gamow-tekijä

$$P(E) = e^{-2\pi\eta} = \exp\!\left(-\sqrt{E_G/E}\right),\qquad \eta = Z_1Z_2\,\alpha\sqrt{\frac{\mu c^2}{2E}},\qquad E_G = 2\mu c^2\,(\pi\alpha Z_1Z_2)^2 .$$

D–D:lle $E_G = 0.986$ MeV (laboratorio toistaa Bosch ja Halen vakion $\sqrt{E_G} = 31.40$ keV$^{1/2}$). Poikkileikkaukset kirjoitetaan

$$\sigma(E) = \frac{S(E)}{E}\,e^{-\sqrt{E_G/E}},$$

missä astrofysikaalinen S‑tekijä $S(E)$ vaihtelee hitaasti: noin 55 keV·b kummallekin kahdesta pääasiallisesta D–D-haarasta. Termisen kaasun yli keskiarvoistettuna tämä antaa D–D-reaktiivisuuksia noin 25 %:n sisällä julkaistuista arvoista 2–10 keV:ssä (testi laboratoriossa).

**Elektroniseulonta on totta ja avoin tutkimuskysymys.** Elektronit ydinten ympärillä kumoavat osittain niiden hylkimisen. Pienillä etäisyyksillä potentiaali näyttää $e^2/r - U_e$:ltä, mikä nostaa matalaenergisia poikkileikkauksia

$$f(E) \approx \exp\!\left(\pi\eta\,\frac{U_e}{E}\right)\qquad (U_e \ll E)$$

(Assenbaum, Langanke & Rolfs, 1987). Deuteriumkaasulle odotettu (adiabaattinen) arvo on $U_e \approx 28$ eV. Keilakokeet keV-energioilla metalleihin ladatulla deuteriumilla ovat raportoineet paljon suurempia arvoja, muutamia satoja eV (esimerkiksi noin 300 eV tantaalissa; Raiola et al., 2002). Miksi nämä arvot ovat niin suuria, on edelleen kiistanalaista.

**Energian kirjanpito.** Ydinreaktiot vapauttavat tai absorboivat energiaa $Q = (\sum m_\text{in} - \sum m_\text{out})c^2$. Mitatuista massoista: D + D → T + p vapauttaa 4,03 MeV; D + D → ³He + n vapauttaa 3,27 MeV (kumpikin noin 50 % ajasta); D + D → ⁴He + γ vapauttaa 23,85 MeV mutta tapahtuu vain noin kerran $10^7$ fuusiota kohti. K‑39 + p → Ca‑40 vapauttaisi 8,33 MeV.

## Taso 2 — Missä väite pettää

**1. Tunnelointiluvut huoneenlämmössä.** Arvolla $E = kT = 0.026$ eV paljas D–D Gamow-tekijä on $10^{-2682}$. Jopa laboratorion WKB-laskelma 800 eV:n seulonnalla antaa $10^{-24}$ parille lämpöenergiassa. Pari „näkee“ seulonnan hyödyn vasta kun se on jo lähempänä kuin seulontapituus, $a = e^2/U_e \approx 1800$ fm.

**2. Optimistinen nopeusarvio.** Laboratorio laskee D–D-fuusion palladiumdeuteridissä (PdD, $6.8\times10^{22}$ D/cm³) 300 K:ssä käsitellen jokaista paria seulottuna $U_e$:llä ja mukaan lukien koko Maxwell-häntä nopeista törmäyksistä. Tämä malli on tarkoituksella antelias:

| $U_e$ | Teho (W/cm³) |
|---|---|
| 0 (paljas) | $2\times10^{-254}$ |
| 28 eV (kaasu) | $9\times10^{-101}$ |
| 300 eV | $7\times10^{-19}$ |
| 800 eV | $9\times10^{-4}$ |

Tulos muuttuu noin 260:n kertoimella ±10 %:n muutoksella $U_e$:ssä, ja 1 W/cm³ vaatisi $U_e \approx 1050$ eV. Vastaus riippuu siis kokonaan siitä, pätevätkö keV-keilan seulonta-arvot huoneenlämpöisiin deuteroneihin — mitä kukaan ei ole osoittanut. Koonin ja Nauenberg (1989) laskivat, että kaksi deuteronia D₂-molekyylissä, vain 0,74 Å:n päässä toisistaan, fuusioituvat noin $10^{-64}$ kertaa sekunnissa.

**3. Puuttuvat neutronit (ratkaiseva testi).** Jos lämpö tulisi tavallisesta D–D-fuusiosta, puolet reaktioista lähettäisi 2,45 MeV:n neutronin. Käyttäen yllä olevia Q-arvoja:

$$\frac{1\ \text{W}}{\tfrac12(4.03+3.27)\ \text{MeV}} = 1.7\times10^{12}\ \text{fusions/s} \;\Rightarrow\; 8.6\times10^{11}\ \text{neutrons/s per watt}.$$

1 m:n etäisyydellä suojaamattomasta 1 W:n lähteestä se on noin 10 Sv tunnissa: tyypillisesti tappava annos noin puolessa tunnissa. Tästä tulee „kuolleen jatko-opiskelijan“ vitsi. Neutronidetektorit voivat laskea yksittäisiä neutroneja, joten jopa $10^{-12}$ W D–D-fuusiota on mitattavissa. Kylmäfuusiokokeet raportoivat wattitason ylimääräistä lämpöä ilman mitään näitä neutroni-, tritium- tai gammantuottoja. Joten joko lämpö ei ole D–D-fuusiota tai se ei ole ydinperäistä.

**4. Vuoden 1989 väitteitä ei vahvistettu.** Fleischmann ja Pons (1989) raportoivat ylimääräistä lämpöä palladiumelektrodeista raskasvedessä. Monet laboratoriot yrittivät toistaa sen eivätkä voineet tehdä sitä luotettavasti. Berlinguette et al. (2019) monivuotinen ohjelma tutki uudelleen pääväitteet huolellisella kalorimetrialla eikä löytänyt näyttöä poikkeavasta lämmöstä tai ydintuotteista, samalla kun se totesi hyödyllistä materiaalitiedettä matkan varrella.

**5. Kanat ja bakteerit.** Entsyymit toimivat kemiallisilla energioilla noin 0,5 eV (esimerkiksi ATP-hydrolyysi). K‑39 + p → Ca‑40 -este on 5,2 MeV, kymmenen miljoonaa kertaa korkeampi, ja laboratorion tunnelointitodennäköisyys ruumiinlämmössä on $10^{-49515}$. Louis Kervranin biologisen transmutaation väitteitä ei ole toistettu kontrolloiduissa olosuhteissa. Munivat kanat ottavat kalsiumia ruoasta ja erityisestä varastosta luissaan; kalsiumköyhällä ruokavaliolla kuoren laatu heikkenee.

**6. „Taittaminen“ ei ole ilmaista.** Lyijy‑208:n muuttaminen kulta‑197:ksi tarkoittaa 3 protonin ja 8 neutronin poistamista. Massat sanovat, että tämä maksaa vähintään 77 MeV atomia kohti, noin 10 MWh kultagrammaa kohti, ennen mitään häviöitä. Ytimen sidosenergia on syy: osat pidetään yhdessä, ja niiden erottaminen maksaa energiaa.

## Taso 3 — Mitä pitäisi olla totta

Jotta huoneenlämpöinen transmutaatio olisi totta, kaikkien näiden pitäisi olla osoitettu. Jokainen on selkeä, testattava tavoite:

- **Seulonta, joka toimii lämpöenergioilla.** Mittaa matalaenergisiä D–D-tuottoja metalleissa lähestyen eV-skaalaa ja näytä tehollinen $U_e$ yli noin 1 keV, joka pätee hilassa lepääviin deuteroneihin.
- **Ydintuotteet, jotka vastaavat lämpöä.** Jokaisen ydinlämmön joulen on tultava oikealla määrällä neutroneja, tritiumia, ³He:tä, ⁴He:tä tai gammasäteitä. Mittaa ne samassa ajossa, sokealla analyysillä.
- **Mekanismi, joka muuttaa haarautumista.** Jos neutroneja ei ole, jonkin uuden fysiikan on lähetettävä energia hilaan nopeiden hiukkasten sijaan, ja se on ennustettava etukäteen ja sitten havaittava.
- **Itsenäinen toisto** laboratorioilta, jotka eivät suunnitelleet alkuperäistä koetta, avoimella datalla.

**Oikeita avoimia tutkimuskysymyksiä:** miksi mitatut seulontaenergiat metalleissa ovat niin suuria; miten vety käyttäytyy metallihiloissa (tärkeää vedyn varastoinnille ja haurastumiselle); ja matalaenergiset ydinpoikkileikkaukset tähtiastrofysiikkaa varten, mitattuina syvällä maan alla (esimerkiksi LUNA:ssa Italiassa).

## Aja laboratorio

```bash
python Module_11_Low_Energy_Transmutation/simulation.py
python -m pytest tests/test_module_11.py
```

| Koe | Mitä se näyttää |
|---|---|
| `coulomb_barrier`, `gamow_energy`, `gamow_factor` | Coulombin seinä ja paljas tunnelointitodennäköisyys, tarkistettu Bosch–Halen $\sqrt{E_G}$:tä vasten. |
| `wkb_exponent`, `screening_enhancement` | Numeerinen WKB-tunnelointi seulotun seinän läpi; toistaa analyyttiset Gamow- ja Assenbaum-tulokset niiden rajoissa. |
| `dd_reactivity_cm3_s`, `fusion_power_density` | Termiset D–D-nopeudet (vastaavat julkaistuja arvoja keV:ssä) ja optimistinen huoneenlämpöarvio PdD:lle. |
| `q_value`, `neutrons_per_watt`, `dose_rate_sv_per_hour` | Q-arvot mitatuista massoista ja neutronivuo, jonka 1 W D–D-fuusiota tuottaisi. |
| `transmutation_cost_mev` | Lyijy → kulta -muunnoksen vähimmäisenergiakustannus. |

## Kokeile itse

1. Käytä `screening_needed`-funktiota löytääksesi $U_e$:n, joka antaisi 1 mW/cm³, ja vertaa sitä ~300 eV:iin mitattuna tantaalissa.
2. Vaihda `temp_k` funktiossa `fusion_power_density` arvoon 600 K. Kuinka paljon lämpötilan kaksinkertaistaminen auttaa verrattuna 10 %:n nousuun $U_e$:ssä?
3. Laske neutroniannosnopeus 3 m:n etäisyydellä 0,1 W:n lähteestä. Kuinka paksu vesisuojan pitäisi olla? (Etsi nopeiden neutronien vaimennuspituus vedessä.)
4. Käytä `q_value`-funktiota tarkistaaksesi, vapauttaako ¹²C + ¹²C → ²⁴Mg energiaa, sitten käytä `coulomb_barrier`- ja `gamow_energy`-funktioita nähdäksesi, miksi se tapahtuu vain massiivisten tähtien sisällä.

## Viitteet

- Gamow, G., "Zur Quantentheorie des Atomkernes", *Z. Phys.* **51**, 204 (1928).
- Assenbaum, H. J., Langanke, K. & Rolfs, C., "Effects of electron screening on low‑energy fusion cross sections", *Z. Phys. A* **327**, 461 (1987).
- Bosch, H.‑S. & Hale, G. M., "Improved formulas for fusion cross‑sections and thermal reactivities", *Nucl. Fusion* **32**, 611 (1992).
- Raiola, F. et al., "Enhanced electron screening in d(d,p)t for deuterated Ta", *Eur. Phys. J. A* **13**, 377 (2002).
- Koonin, S. E. & Nauenberg, M., "Calculated fusion rates in isotopic hydrogen molecules", *Nature* **339**, 690 (1989).
- Fleischmann, M., Pons, S. & Hawkins, M., "Electrochemically induced nuclear fusion of deuterium", *J. Electroanal. Chem.* **261**, 301 (1989).
- Berlinguette, C. P. et al., "Revisiting the cold case of cold fusion", *Nature* **570**, 45 (2019).
- Wang, M. et al., "The AME 2020 atomic mass evaluation (II)", *Chinese Phys. C* **45**, 030003 (2021). Atomimassojen lähde.
- ICRP Publication 74, *Conversion Coefficients for use in Radiological Protection against External Radiation* (1996). Likimääräisen neutroniannoskertoimen lähde.
- Huba, J. D., *NRL Plasma Formulary* (Naval Research Laboratory, päivitetään säännöllisesti). Testeissä käytetyt taulukoidut D–D-reaktiivisuudet.
