# 🔬 Moduuli 4 — Tarinan takana oleva tiede

> [Oppitunti](readme.md) kerrotaan vuodesta 2420. Tämä sivu on vuoden 2025 todellisuustarkistus: mikä on vakiintunutta, missä tarinan väite pettää, ja mitä pitäisi olla totta, jotta se toimisi. Kaikki tässä voidaan tarkistaa [laboratoriokoodilla](../../../Module_04_Matter_Is_Frozen_Light/simulation.py).

## Vuoden 2420 väite yhdessä lauseessa

Aine on valoa, joka on vangittu pieneen pyörivään silmukkaan (torukseen), joten elektroni on ympyrässä juokseva fotoni, ja massa on vain „jäätynyttä valoa“.

## Taso 1 — Mikä on totta

**Massa ja energia ovat todella samaa valuuttaa.** Einsteinin $E = mc^2$ (1905) on yksi fysiikan parhaiten testatuista yhtälöistä. Aina kun energia poistuu järjestelmästä, massa poistuu sen mukana:

| Prosessi | Vapautunut energia | Massa joka katoaa |
|---|---|---|
| 1 kg kuivan puun poltto | $1.6\times10^{7}$ J | $1.8\times10^{-7}$ g ($2\times10^{-10}$ puusta) |
| 15 kilotonnin fissiopommi | $6.3\times10^{13}$ J | 0,7 g |

Joten oppitunnin „halkojen polttaminen avaa solmut“ sisältää jotain totta: tuhka ja kaasut ovat todella kevyempiä määrällä $\Delta m = E/c^2$. Mutta atomit ovat yhä kaikki siellä. Vain murto-osa $10^{-10}$ massasta lähtee.

**Suurin osa massastasi on todella energiaa, vain ei valoa.** Protonin paino on 938,27 MeV/c². Sen kolmen valenssikvarkin lepomassat (ylös, ylös, alas; noin 2,2 + 2,2 + 4,7 MeV Particle Data Groupin skeemassa) summautuvat vain noin **1 %**:iin siitä. Loppu on karkeiden lähellä valonnopeutta liikkuvien kvarkkien energiaa ja niitä sitovan gluonikentän energiaa, jota kuvaa kvanttikromodynamiikka (QCD). Hila-QCD laskee hadronimassat tästä muutaman prosentin tarkkuudella (Dürr et al., 2008). Kun lasketaan mukaan myös virtuaalisten „meri“-kvarkkien (mukaan lukien outo kvarkki) kvarkkimassaosuus, kvarkkimassan osuus nousee suunnilleen 10 %:iin, yhä pieni osa. Siinä mielessä „massa on enimmäkseen kenttäenergiaa“ on oikeaa fysiikkaa, ja se on syvempi väite kuin tarina esittää.

**Aine todella muuttuu valoksi, ja valo aineeksi.**

- *Aine → valo.* Elektroni ja positroni annihiloituvat kahdeksi 511 keV:n fotoniksi. Sairaalan PET-skannerit havaitsevat juuri näitä fotonipareja joka päivä.
- *Valo → aine.* Breit ja Wheeler (1934) laskivat, että kaksi fotonia voi tehdä elektroni–positroni-parin, jos niillä on yhdessä tarpeeksi energiaa. Energiat $E_1, E_2$ kohtaavat kulmassa $\theta$; invariantin $s = 2E_1E_2(1-\cos\theta)$ on saavutettava $(2m_ec^2)^2$:

$$E_1E_2(1-\cos\theta) \;\ge\; 2(m_ec^2)^2.$$

Vastakkain törmätessä kaksi 511 keV:n fotonia on täsmälleen kynnyksellä. Sen yläpuolella poikkileikkaus on

$$\sigma_{\gamma\gamma} = \frac{\pi r_e^2}{2}(1-\beta^2)\left[(3-\beta^4)\ln\frac{1+\beta}{1-\beta} - 2\beta(2-\beta^2)\right], \qquad \beta = \sqrt{1 - \frac{4m_e^2c^4}{s}},$$

missä $r_e$ on klassinen elektronin säde ja $\beta$ on kunkin leptonin nopeus massakeskipistejärjestelmässä. Se huipentuu arvoon $1.70\times10^{-25}$ cm² $\approx 0.256\,\sigma_T$ lähellä $\beta = 0.70$. Laboratorio tarkistaa kaavan itsenäisesti: rakentamalla sen uudelleen Dirac’n (1930) kaavasta käänteiselle prosessille $e^+e^-\to\gamma\gamma$, käyttäen yksityiskohtaista tasapainoa $\sigma_{\gamma\gamma} = 2\beta^2\sigma_\text{ann}$, sopii $10^{-13}$:aan.

**Kokeet.** SLAC-koe E‑144 (Burke et al., 1997) takaisinsirrotti 527 nm:n laserin 46,6 GeV:n elektroneista tuottaakseen gammasäteitä jopa 29,2 GeV:iin, jotka sitten törmäsivät samaan intensiiviseen laserin. Pelkkä kinematiikka sanoo, että vähintään 4 laserfotonia oli absorboitava kerralla, joten tämä oli *epälineaarinen, monifotoninen* Breit–Wheeler. STAR RHIC:llä (Adam et al., 2021) näki $e^+e^-$-pareja kultaytimien intensiivisistä sähkömagneettisista kentistä niiden kulkiessa läheltä toisiaan, jotka toimivat *kvasireaalisten* fotonien pilvinä. Kahden reaalisen fotonisäteen puhdasta törmäystä ei ole vielä tehty; ehdotuksia on (Pike et al., 2014).

**Paria tyhjästä.** Tarpeeksi voimakas sähkökenttä voi luoda pareja suoraan. Asteikko on se, jossa kenttä antaa elektronille sen lepoenergian yhden Compton-pituuden matkalla (Sauter, Heisenberg–Euler, Schwinger):

$$E_\text{crit} = \frac{m_e^2c^3}{e\hbar} \approx 1.32\times10^{18}\ \text{V/m}, \qquad I_\text{crit} \approx 2.3\times10^{29}\ \text{W/cm}^2.$$

## Taso 2 — Missä väite pettää

**1. „Elektroni on ympyrässä juokseva fotoni“ saa yhden onnistumisensa ilmaiseksi.** Malli (Williamson & van der Mark, 1997) sijoittaa varauksen $e$ liikkumaan nopeudella $c$ silmukkaan säteellä $r = \hbar/(m_ec) = 3.86\times10^{-13}$ m, redusoitu Compton-aallonpituus. Kiertävällä varauksella on magneettinen momentti

$$\mu = I\cdot\pi r^2 = \frac{ec}{2\pi r}\,\pi r^2 = \frac{ecr}{2} = \frac{e\hbar}{2m_e} = \mu_B,$$

täsmälleen Bohrin magnetoni. Mutta $r$ valittiin $m_e$:stä, ja $\mu_B$ *määritellään* $e\hbar/2m_e$:ksi, joten tämä on algebrallinen identiteetti. Laboratorio näyttää, että sama resepti antaa „oikean magnetonin“ mille tahansa valitsemallesi massalle. Se ei voi epäonnistua, joten se ei ennusta mitään.

**2. Se ohittaa sen, mitä elektroni todella tekee.** Mitattu momentti ei ole $\mu_B$ vaan $1.00115965218059\,\mu_B$ (Fan et al., 2023). Kvanttisähködynamiikka ennustaa tuon ylimääräisen 0,116 %:

$$a_e = \frac{g-2}{2} = \frac{1}{2}\frac{\alpha}{\pi} - 0.3285\left(\frac{\alpha}{\pi}\right)^2 + 1.1812\left(\frac{\alpha}{\pi}\right)^3 - 1.9122\left(\frac{\alpha}{\pi}\right)^4 + \dots$$

Laboratorio käyttää $\alpha$:ta rubidium-atomirekyylimittauksista (Morel et al., 2020), joka ei riipu $g-2$:sta, joten vertailu ei ole kehämäinen:

| Malli | ennustettu $g/2$ | virhe |
|---|---|---|
| fotonisilmukka | 1 (täsmälleen) | $1.2\times10^{-3}$ |
| QED, 1 silmukka (Schwingerin $\alpha/2\pi$) | 1.0011614 | $1.8\times10^{-6}$ |
| QED, 2 silmukkaa | 1.001159637 | $1.5\times10^{-8}$ |
| QED, 3 silmukkaa | 1.00115965223 | $5\times10^{-11}$ |
| QED, 4 silmukkaa | 1.00115965218 | $5\times10^{-12}$ |

Jäljelle jäävä $5\times10^{-12}$ on odotettu koko termeille, jotka laboratorio jättää pois (viisisilmukkainen QED, raskaampien muonien ja tauiden silmukat, hadroniset ja heikot vaikutukset). QED on noin $10^{8}$ kertaa lähempänä kuin silmukkamalli.

**3. Elektroni on paljon pienempi kuin silmukka.** Korkeaenergiset elektroni–positroni-sirontakokeet LEP:llä eivät näytä merkkiä elektronin rakenteesta noin $10^{-18}$ m:iin asti. Mallin silmukka on $4\times10^{5}$ kertaa suurempi. Näin suuri rakenne olisi muuttanut elektronien sirontaa energioilla, joita tutkittiin vuosikymmeniä sitten.

**4. Muuta, mitä mallin pitäisi selittää mutta ei selitä.** Fotonilla ei ole varausta, joten mistä elektronin varaus $-e$ tulee? Fotonilla on spin 1; elektronilla spin ½. Muonilla ja taulla on täsmälleen sama varaus kuin elektronilla mutta eri massat. Ja yksittäisellä fotonilla, miten energinen tahansa, on $s = 0$, eikä se voi koskaan tulla massiiviseksi hiukkaseksi yksinään; jotain muuta (ydin, toinen fotoni, voimakas kenttä) tarvitaan aina. Valo ei myöskään taivu suljetuksi silmukaksi itsestään.

**5. Valo ei ole käytännöllinen aineen lähde.** Kaksi 2 eV:n auringonvalofotonia jäävät parikynnyksestä jälkeen tekijällä $6.5\times10^{10}$ $s$:ssä; auringonvalofotoni tarvitsisi 131 GeV:n gammasäteen partneriksi. Paria tyhjästä kentällä hallitsee tekijä $e^{-\pi E_\text{crit}/E}$. Intensiivisin laser tähän mennessä, noin $1.1\times10^{23}$ W/cm² (Yoon et al., 2021), saavuttaa $9\times10^{14}$ V/m $= 7\times10^{-4}\,E_\text{crit}$, antaen tekijän noin $10^{-1983}$. (Todelliset laserpulssit värähtelevät ja fokusoidaan, joten tarkka nopeus eroaa, mutta se pysyy täysin mitättömänä.)

**6. Miksi asiat tuntuvat kiinteiltä.** Ei siksi että valo pyörii. Aine on stabiilia ja kokoonpuristumatonta, koska elektronit ovat fermioneja: Paulin kieltosääntö yhdessä sähköstatiikan kanssa estää atomeja romahtamasta toisiinsa (Dyson & Lenard, 1967; Lieb, 1976). Kattotuulettimen kuva on mukava, mutta todellinen mekanismi on kvanttitilastotiede.

## Taso 3 — Mitä pitäisi olla totta

Elektronin „jäätynyt valo“ -mallin pitäisi läpäistä kaikki nämä testit, joista kullakin on tarkka mitattu kohde:

- **Ennusta $a_e = 0.00115965218\ldots$** ilman siihen sovitettua parametria, kuten QED tekee pelkästä $\alpha$:sta.
- **Selitä varaus, spin ½ ja kolme sukupolvea** (elektroni, muon, tau) yhdellä mekanismilla, ja ennusta niiden massasuhteet (206,77 ja 3477,2). Standardimalli ei ennusta näitä massoja sekään; ne ovat avoin kysymys, joten malli joka sen tekisi olisi suuri löytö.
- **Näytä rakenne ~$10^{-13}$ m:ssä** elektronisironnassa („muototekijä“). Nykyinen data sulkee tämän pois yli viidellä kertaluokalla.

Läheisiä todellisia avoimia kysymyksiä: ensimmäinen kahden reaalisen fotonisäteen törmäys Breit–Wheeler-kynnyksen yläpuolella; kokeet, jotka lähestyvät Schwinger-kenttää elektronin omassa lepokehyksessä (voimakenttä-QED lasereilla ja korkeaenergisillä elektronisäteillä); ja miksi Higgs-kytkennöillä, ja siten kvarkkien ja leptonien massoilla, on juuri ne arvot jotka niillä on.

## Aja laboratorio

```bash
python Module_04_Matter_Is_Frozen_Light/simulation.py
python -m pytest tests/test_module_04.py
```

| Koe | Mitä se näyttää |
|---|---|
| `mass_defect`, `proton_valence_quark_fraction` | $E = mc^2$ kemiallisilla ja ydinasteikoilla; kvarkkien lepomassat ovat ~1 % protonista. |
| `breit_wheeler_threshold`, `pair_beta`, `breit_wheeler_cross_section` | Valo aineeksi: kynnys ja poikkileikkaus. |
| `breit_wheeler_from_annihilation`, `dirac_annihilation_cross_section` | Poikkileikkauksen itsenäinen tarkistus yksityiskohtaisella tasapainolla. |
| `compton_edge`, `min_laser_photons` | Miksi SLAC E‑144 oli monifotoniprosessi. |
| `schwinger_field`, `schwinger_suppression_log10` | Kuinka kaukana nykyiset laserit ovat parien irrottamisesta tyhjästä. |
| `loop_magnetic_moment`, `toroidal_model_moment`, `qed_anomaly` | Fotonisilmukkamallin sisäänrakennettu „onnistuminen“ ja sen ohitus vs QED. |

## Kokeile itse

1. Kuinka energinen gammasäteen täytyy olla tehdäksen pareja kosmisen mikroaaltotaustan päällä (tyypillinen fotonienergia noin $6\times10^{-4}$ eV)? Siksi universumi on läpinäkymätön korkeimmille gammasäteille.
2. Käytä `toroidal_model_moment`-funktiota muonin massalla ja vertaa mitattuun muonin anomaliaan $a_\mu \approx 0.00116592$. Tekeekö silmukkamalli yhtään paremmin muonille?
3. Laske 30 kg:n lapsen lepoenergia `mass_defect`-funktiolla käänteisesti ($E = mc^2$). Kuinka monta 15 kilotonnin pommia se on? Miksi mitään sellaista ei koskaan tapahdu itsestään? (Vihje: mitkä säilyvät suureet joutuisivat katoamaan?)
4. Piirrä `breit_wheeler_cross_section` vastaan $s/(2m_ec^2)^2$ ja tarkista korkeaenergiamuoto $\sigma \approx \frac{4\pi r_e^2 m_e^2c^4}{s}\left[\ln\frac{s}{m_e^2c^4} - 1\right]$.
5. Korvaa `ALPHA_RB` cesium-arvolla $\alpha^{-1} = 137.035999046$ (Parker et al., 2018). Kuinka paljon 4-silmukan ennuste liikkuu verrattuna mittausepävarmuuteen $1.3\times10^{-13}$ $g/2$:ssa?

## Viitteet

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
