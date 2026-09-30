# 🔬 Moduuli 3 — Tarinan takana oleva tiede

> [Oppitunti](readme.md) kerrotaan vuodesta 2420. Tämä sivu on vuoden 2025 todellisuustarkistus: mikä on vakiintunutta, missä tarinan väite pettää, ja mitä pitäisi olla totta, jotta se toimisi. Kaikki tässä voidaan tarkistaa [laboratoriokoodilla](../../../Module_03_The_Brain_Is_A_Radio/simulation.py).

## Vuoden 2420 väite yhdessä lauseessa

Aivot eivät tee mieltä vaan vastaanottavat sen, kuin radio joka on viritetty lähetykseen „Aikakanavalla“; valo häiritsee tuota kanavaa, ja kaksi samalle taajuudelle viritettyä aivoa jakavat ajatuksia.

## Taso 1 — Mikä on totta

**Aivot todella tuottavat sähköisiä rytmejä.** Hans Berger tallensi ensimmäisen ihmisen EEG:n 1920-luvulla. Päänahan elektrodit poimivat noin 10–100 µV jännitteitä miljoonien neuronien synkronoidusta laukeamisesta. Rytmit lajitellaan tavanomaisiin kaistoihin (rajat vaihtelevat hieman laboratorioiden välillä):

| Kaista | Taajuus | Tyypillisesti liitetty |
|---|---|---|
| delta | 0,5–4 Hz | syvä uni |
| theta | 4–8 Hz | uneliaisuus, muistitehtävät |
| alpha | 8–13 Hz | rentoutunut valveillaolo, silmät kiinni |
| beta | 13–30 Hz | aktiivinen ajattelu, liike |
| gamma | 30–80 Hz | paikallinen prosessointi, tarkkaavaisuus |

**„Valo tukahduttaa signaalin“ -ajatuksella on todellinen kaiku.** Berger huomasi, että alpha-rytmi pienenee, kun avaat silmät („alpha-esto“). Se pienenee myös henkisellä ponnistelulla, joten se heijastaa sitä, mitä aivot *tekevät*, ei fotonien häirintää piilotettuun kanavaan.

**Maa todella humisee.** Salamaniskut (noin 50 sekunnissa maailmanlaajuisesti) soittavat onteloa maanpinnan ja ionosfäärin välillä. Ihanteelliselle, häviöttömälle ohuelle kuorelle säteellä $R_E$ moodit ovat

$$f_n = \frac{c}{2\pi R_E}\sqrt{n(n+1)}, \qquad f_1 \approx 10.6\ \text{Hz}.$$

Havaitut huiput ovat noin 7,8, 14,3, 20,8, 27,3 ja 33,8 Hz, suunnilleen 75–80 % ihanteellisista arvoista, koska ionosfääri on häviöllinen, epätäydellinen peili (Schumann ennusti resonanssin vuonna 1952; Balser & Wagner havaitsivat sen vuonna 1960). Perustaajuus 7,83 Hz sattuu theta/alpha-rajalle.

**Aivojen omat kentätkin ovat pieniä.** Pään ulkopuolella aivojen magneettikenttä on noin 100 fT–1 pT (magnetoenkefalografia, MEG). Schumannin magneettikenttä on myös kertaluokkaa 1 pT. Siksi MEG tehdään magneettisesti suojatuissa huoneissa.

**Rytmien ja synkronian mittaaminen.** Laboratorio toteuttaa vakiotyökalut:

- *Welch-tehospektri* $S(f)$: keskiarvoista limittäisten ikkunoidun segmenttien Fourier-muunnoksen neliö.
- *Kaistateho*: $P_\text{band} = \int_{f_1}^{f_2} S(f)\,df$. Summattuna kaikille taajuuksille tämä vastaa signaalin varianssia (testit tarkistavat tämän).
- *Hetkellinen vaihe*: kaistanpäästösuodatus, sitten analyyttinen signaali $x(t) + i\,\mathcal{H}[x](t) = A(t)e^{i\phi(t)}$ Hilbert-muunnoksen kautta.
- *Vaihelukitusarvo* (Lachaux et al., 1999): $\text{PLV} = \left|\langle e^{i(\phi_1(t) - \phi_2(t))}\rangle_t\right|$, joka on 1 vakiovaihe-erolla ja lähellä 0:aa riippumattomilla vaiheilla.

„Aivoista aivoihin -synkronia“ on todellinen löydös hyperskannaus-tutkimuksissa, joissa kaksi ihmistä tallennetaan samanaikaisesti. Mutta se syntyy enimmäkseen siksi, että molemmat näkevät ja kuulevat samat asiat samaan aikaan, ei siksi että signaali kulkisi heidän välillään (Burgess, 2013).

## Taso 2 — Missä väite pettää

**1. Taajuuden vastaavuus ei ole kytkentää.** 1 pT:n kenttä taajuudella 7,83 Hz indusoi pään kokoisen silmukan ympärille (säde 7,5 cm)

$$\mathcal{E} = \pi r^2 \cdot 2\pi f B \approx 9\times10^{-13}\ \text{V}, \qquad E = \tfrac12 r\,\omega B \approx 2\times10^{-12}\ \text{V/m}.$$

Se on noin $10^{-7}$ 10 µV:n EEG-signaalista. Transkraniaalinen vaihtovirtaärsytys, joka voi mitattavasti työntää aivorytmejä, tuo aivoihin suunnilleen 0,1–1 V/m: noin $10^{11}$ kertaa enemmän. „Viritettynä 7,83 Hz:lle“ ei anna mekanismia sille, että Schumann-kenttä tekisi mitään.

**2. Testi, joka ei voi epäonnistua.** Yleinen tapa „näyttää“ aivo–Maa-resonanssia on verrata signaalia täydelliseen 7,83 Hz:n sineen. Millä tahansa kahdella vakaalla saman taajuuden signaalilla on vakio vaihe-ero, joten PLV on 1 *rakenteeltaan*. Laboratorio tekee tämän ja saa PLV = 1,000. Sitten se kysyy oikean kysymyksen: onko PLV suurempi kuin se, jonka saisit, jos kaksi tallennetta liu'utetaan muutaman sekunnin pois kohdistuksesta? Puhtaalle sinille liu'utus ei muuta mitään, joten surrogaattitesti palauttaa p = 1: ei mitään näyttöä.

**3. Testi, joka voi epäonnistua.** Todellinen Schumann-kenttä ei ole täydellinen sini; salama ajaa sitä satunnaisesti, joten sen vaihe harhailee (laatutekijä $Q \approx 4$). Laboratorio simuloi EEG:tä ja itsenäistä Schumann-magnetometritallennetta, sitten ajaa aika-siirto-surrogaattitestin 100 synteettiselle tallenteelle:

| Tapaus | Osuus jossa p < 0,05 |
|---|---|
| Ei kytkentää | ≈ 5 % (väärien positiivisten osuus, joka kalibroidulla testillä pitäisi olla) |
| Heikko sisäänrakennettu kytkentä (0,5 % EEG-tehosta) | ≈ 93 % |
| Kaksi EEG-kanavaa jakavat yhden alpha-lähteen | 100 % |
| Kaksi EEG-kanavaa itsenäisillä alpha-lähteillä | ≈ 4 % |

Koska testi havaitsee kytkennän, kun sitä todella on, sen „ei“ tarkoittaa jotain. Tämä on standardi, jonka minkä tahansa aivo–Schumann-kytkentäväitteen on läpäistävä.

**4. Fotoni-sammutus.** Ei ole julkaistua, toistettua näyttöä siitä, että valo tukahduttaisi ajatuksen, tai että infrapunakamerat kuvaisivat „tulpoidisia“ mielenmuotoja. Kallosi sisäpuoli on jo lähes pimeä, ja ihmiset ajattelevat täysin hyvin kirkkaassa auringonvalossa. Silmän herkkyyskäyrä tulee verkkokalvon fotopigmenttien absorptiospektreistä, jotka mitataan suoraan.

**5. Muisti elävänä lähetyksenä menneisyydestä.** Tämä on kaunis kuva, mutta näyttö osoittaa lujasti toiseen suuntaan:

- Vaurio tietyissä aivorakenteissa poistaa tiettyjä kykyjä. Potilas H.M. menetti kyvyn muodostaa uusia pitkäkestoisia muistoja leikkauksen jälkeen, jossa poistettiin osia molemmista hippokampuksista (Scoville & Milner, 1957).
- Hiirillä oppimisen aikana aktiiviset neuronit voidaan merkitä ja myöhemmin aktivoida uudelleen valolla, mikä laukaisee muiston (Liu et al., 2012).
- Muistot *rekonstruktoidaan* ja voivat muuttua: kysymyksen muotoilu muuttaa sitä, mitä ihmiset myöhemmin raportoivat nähneensä (Loftus & Palmer, 1974). Elävä lähetys menneisyydestä ei muokkautuisi kysymyksen mukaan.

Kotitehtävän radioanalogia („laulu on yhä ilmassa“) tekee testattavan ennusteen: jonkin muun vastaanottimen pitäisi pystyä soittamaan laulusi. Mitään sellaista vastaanotinta ei ole koskaan löydetty.

**6. Kvanttiaivot (Orch‑OR).** Hameroff ja Penrose ehdottivat, että kvanttisuperpositiot neuronien mikrotubuluksissa romahtavat noin 25 ms:n aikaskaaloilla ja että tämä liittyy tietoisuuteen. Se on todellinen, julkaistu ja kiistanalainen hypoteesi. Pääasiallinen vastaväite on ajoitus: Tegmark (2000) arvioi, että sellaiset superpositiot dekoheroivat $10^{-13}$ s:ssa tai vähemmässä. Laboratorio laskee aukon:

| Hermoston aikaskaala | vs Tegmarkin $10^{-13}$ s | vs vastaväitearvio $10^{-4}$ s (Hagan et al., 2002) |
|---|---|---|
| aktiopotentiaali, 1 ms | $10^{10}$ | $10^{1}$ |
| gamma-sykli, 25 ms | $10^{11}$ | $10^{2.4}$ |

Jopa suotuisin julkaistu arvio jää vajaaksi. Orch‑OR ei myöskään tekisi aivoista *vastaanotinta*; se on yhä teoria aivoista mielen tuottajana.

## Taso 3 — Mitä pitäisi olla totta

Jotta aivot olisivat Schumann-viritetty vastaanotin, näiden pitäisi näkyä. Jokainen on selvä koe:

- **Kytkentä, joka läpäisee surrogaattitestin.** Tallenna EEG yhdessä paikallisen magnetometrin kanssa. Ennakkorekisteröidyn analyysin pitäisi löytää PLV niiden väliltä aika-siirto-surrogaattinollan yläpuolelta, toistettuna itsenäisissä laboratorioissa.
- **Kytkentä, joka katoaa, kun kenttä poistetaan.** Toista magneettisesti suojatussa huoneessa, joka leikkaa 1 pT:n kentän kertaluokilla. Jos „kytkentä“ säilyy, se ei tule Schumann-kentästä.
- **Mekanismi oikealla koolla.** Jonkin hermokudoksessa pitäisi vastata kenttiin noin $10^{11}$ kertaa heikompiin kuin niihin, joiden tiedetään vaikuttavan siihen, ja lämpökohinan yläpuolella.
- **„Fotoni-sammutukselle“**: toistettu, sokkoutettu koe, jossa jokin mielen ilmiö ilmestyy pimeässä ja katoaa valossa, valotason ollessa ainoa muutettu asia.

Todellisia avoimia kysymyksiä jää. Miten tietoisuus syntyy aivotoiminnasta („kova ongelma“) on ratkaisematta. Onko kvanttivaikutuksilla mitään toiminnallista roolia biologiassa, tutkitaan aktiivisesti. Painovoimaan liittyvää aaltofunktion romahtamista, johon Orch‑OR nojaa, testataan; maanalainen koe sulki pois Diósi–Penrose-mallin yksinkertaisimman parametrittomän version (Donadi et al., 2021).

## Aja laboratorio

```bash
python Module_03_The_Brain_Is_A_Radio/simulation.py
python Module_03_The_Brain_Is_A_Radio/simulation.py --data my_eeg.csv --fs 160 --channels 0 1
python -m pytest tests/test_module_03.py
```

| Koe | Mitä se näyttää |
|---|---|
| `schumann_frequency` | Ihanteelliset ontelomoodit (10,6, 18,3, … Hz) vs havaitut 7,83, 14,3, … Hz. |
| `field_budget`, `induced_emf`, `induced_e_field` | Schumann-kenttä on aivojen oman kentän koko pään ulkopuolella, mutta indusoi ~10⁻¹² V/m sen sisällä. |
| `pink_noise`, `synthetic_eeg_pair`, `schumann_record` | Synteettinen EEG (1/f-tausta plus alpha-purseet) ja harhailevan vaiheen Schumann-jälki. |
| `welch_psd`, `band_power`, `spectral_slope` | Vakiomainen EEG-spektrianalyysi. |
| `plv`, `shift_surrogate_test`, `detection_rate` | Vaihelukitus, sini-vs-sini-ansa ja kalibroitu testi mitatulla väärien positiivisten osuudella ja teholla. |
| `decoherence_gap` | Orch‑OR:n ajoitusongelma kertaluokissa. |
| `load_user_eeg` | Valinnainen: oma tallenteesi `.csv`- tai `.npy`-muodossa (näytteet × kanavat). Verkkoa ei käytetä. |

## Kokeile itse

1. Todellinen data: lataa muutama ajo PhysioNet EEG Motor Movement/Imagery -aineistosta (109 vapaaehtoista, 64 kanavaa, 160 Hz, EDF-muoto). Muunna kaksi kanavaa CSV:ksi (esimerkiksi MNE‑Python-kirjastolla) ja aja laboratorio lipulla `--data`. Vertaa silmät auki- ja silmät kiinni -perusajoja: muuttuuko alpha-teho kuten Berger löysi?
2. Omalla datallasi laske PLV kahden *naapurielektrodin* ja kahden *etäisen* välillä. Miksi naapurit ovat melkein aina „merkitsevästi lukittuneita“? (Vihje: tilavuusjohtavuus, jossa yksi lähde saavuttaa molemmat elektrodit.)
3. Toteuta vaiherandomisoitu surrogaatti (pidä yhden kanavan Fourier-amplitudit, randomisoi sen vaiheet) ja käytä sitä täydellistä 7,83 Hz:n sini-referenssiä vastaan. Näytä, että sekään ei erota tasaista 7,83 Hz:n rytmiä todellisesta synkronoinnista. Mikä referenssin ominaisuus saa jokaisen surrogaattimenetelmän epäonnistumaan?
4. Laske `COUPLING_DEMO` kunnes `detection_rate` putoaa noin 50 %:iin. Miten tuo teho muuttuu, jos kaksinkertaistat tallennuksen pituuden?
5. Käytä `induced_e_field`-funktiota löytääksesi magneettikentän taajuudella 7,83 Hz, joka indusoisi 0,1 V/m päähän. Miten se vertautuu MRI-skannerin kenttään (muutama tesla, mutta staattinen)?

## Viitteet

- Berger, H., "Über das Elektrenkephalogramm des Menschen", *Archiv für Psychiatrie und Nervenkrankheiten* **87**, 527 (1929).
- Schumann, W. O., "Über die strahlungslosen Eigenschwingungen einer leitenden Kugel, die von einer Luftschicht und einer Ionosphärenhülle umgeben ist", *Z. Naturforsch. A* **7**, 149 (1952).
- Balser, M. & Wagner, C. A., "Observations of Earth–ionosphere cavity resonances", *Nature* **188**, 638 (1960).
- Nickolaenko, A. P. & Hayakawa, M., *Resonances in the Earth–Ionosphere Cavity*, Kluwer (2002).
- Hämäläinen, M., Hari, R., Ilmoniemi, R. J., Knuutila, J. & Lounasmaa, O. V., "Magnetoencephalography — theory, instrumentation, and applications to noninvasive studies of the working human brain", *Rev. Mod. Phys.* **65**, 413 (1993).
- Lachaux, J.‑P., Rodriguez, E., Martinerie, J. & Varela, F. J., "Measuring phase synchrony in brain signals", *Hum. Brain Mapp.* **8**, 194 (1999).
- Theiler, J., Eubank, S., Longtin, A., Galdrikian, B. & Farmer, J. D., "Testing for nonlinearity in time series: the method of surrogate data", *Physica D* **58**, 77 (1992).
- Burgess, A. P., "On the interpretation of synchronization in EEG hyperscanning studies: a cautionary note", *Front. Hum. Neurosci.* **7**, 881 (2013).
- Schalk, G., McFarland, D. J., Hinterberger, T., Birbaumer, N. & Wolpaw, J. R., "BCI2000: a general‑purpose brain‑computer interface (BCI) system", *IEEE Trans. Biomed. Eng.* **51**(6), 1034 (2004). Source of the PhysioNet EEG Motor Movement/Imagery dataset.
- Goldberger, A. L. et al., "PhysioBank, PhysioToolkit, and PhysioNet", *Circulation* **101**(23), e215 (2000).
- Scoville, W. B. & Milner, B., "Loss of recent memory after bilateral hippocampal lesions", *J. Neurol. Neurosurg. Psychiatry* **20**, 11 (1957).
- Liu, X. et al., "Optogenetic stimulation of a hippocampal engram activates fear memory recall", *Nature* **484**, 381 (2012).
- Loftus, E. F. & Palmer, J. C., "Reconstruction of automobile destruction: an example of the interaction between language and memory", *J. Verbal Learn. Verbal Behav.* **13**, 585 (1974).
- Hameroff, S. & Penrose, R., "Orchestrated reduction of quantum coherence in brain microtubules: a model for consciousness", *Math. Comput. Simul.* **40**, 453 (1996).
- Hameroff, S. & Penrose, R., "Consciousness in the universe: a review of the 'Orch OR' theory", *Phys. Life Rev.* **11**, 39 (2014).
- Tegmark, M., "Importance of quantum decoherence in brain processes", *Phys. Rev. E* **61**, 4194 (2000).
- Hagan, S., Hameroff, S. R. & Tuszyński, J. A., "Quantum computation in brain microtubules: decoherence and biological feasibility", *Phys. Rev. E* **65**, 061901 (2002).
- Donadi, S. et al., "Underground test of gravity‑related wave function collapse", *Nat. Phys.* **17**, 74 (2021).
