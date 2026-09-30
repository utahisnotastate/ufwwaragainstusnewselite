# 🔬 Moduuli 12 — Tarinan takana oleva tiede

> [Oppitunti](readme.md) kerrotaan vuodesta 2420. Tämä sivu on vuoden 2025 todellisuustarkistus: mikä on vakiintunutta, missä tarinan väite pettää, ja mitä pitäisi olla totta, jotta se toimisi. Kaikki tässä voidaan tarkistaa [laboratoriokoodilla](../../../Module_12_The_Psychotronic_Internet/simulation.py).

## Vuoden 2420 väite yhdessä lauseessa

Ihmismielet voidaan yhdistää suoraan, ilman puhelimia tai johtoja, planeetanlaajuisen „Noosfäärin“ kautta, jota „psykotroninen verkko“ vahvistaa, joten kysymyksiin vastataan heti ja taidot voidaan ladata sekunneissa.

## Taso 1 — Mikä on totta

**Aivot ovat sähköisiä, ja niiden kentät voidaan mitata.** Neuronit tuottavat virtoja, joiden kentät voidaan tallentaa pään ulkopuolelta: EEG (mikrovoltteja päänahalla) ja MEG (magneettikenttiä suuruusluokassa 100 fT – 1 pT antureissa muutaman senttimetrin päässä lähteistä, noin $10^{-8}$ Maan kentästä).

**Aivo–tietokone-liitännät ovat totta.** Implantoitujen elektrodiryhmien (esimerkiksi BrainGate-kokeissa) avulla halvaantuneet ihmiset ohjaavat kursoreita, robottikäsivarsia ja tekstiä. Willett et al. (2021) dekoodasivat kuviteltua käsialaa noin 90 merkin minuuttinopeudella, ja myöhempi työ dekoodasi yritettyä puhetta noin 62 sanan minuuttinopeudella (Willett et al., 2023). Nämä ovat lääketieteellisiä laitteita, jotka lukevat signaaleja aivoihin tai niiden päälle sijoitetuista elektrodeista; ne eivät tavoita muiden ihmisten aivoja ilman kautta.

**Johtimet seulovat kenttiä.** Johtimeen tuleva vaihtuva kenttä vaimenee ihosyvyyden yli

$$\delta = \sqrt{\frac{2}{\mu\sigma\omega}} \;\propto\; f^{-1/2}.$$

Merivedessä ($\sigma \approx 4$ S/m) $\delta = 29$ m taajuudella 76 Hz, Yhdysvaltain laivaston ELF-sukellusvenelähettimien taajuudella, 4,6 m taajuudella 3 kHz ja 0,25 m taajuudella 1 MHz. Taajuudella 2,4 GHz veden siirtovirta on suurempi kuin sen konduktiovirta ($\omega\varepsilon/\sigma \approx 2.7$), joten tarvitaan yleinen kaava ja se antaa noin 1 cm. Kuparisessa $\delta = 9{,}2$ mm taajuudella 50 Hz ja 65 µm taajuudella 1 MHz: 1 mm:n kuparilevy absorboi noin 133 dB taajuudella 1 MHz. Siksi Faradayn häkit toimivat.

**Myös staattiset kentät seulotaan.** Johtimessa varaukset liikkuvat, kunnes kenttä sisällä on nolla. Johtavalle pallolle tasaisessa kentässä $E_0$ indusoitu pintavaraus on $\sigma_s = 3\varepsilon_0E_0\cos\theta$. Laboratorio ei oleta vastausta: se summaa Coulombin lain tuon pintavarauksen yli numeerisesti ja löytää kokonaiskentän sisällä alle $10^{-4}E_0$, kun taas ulkopuolella se vastaa oppikirjan dipoliratkaisua.

**Potentiaalit ovat todellisia, ja merkitsevät tarkalla tavalla.** Whittaker osoitti vuosina 1903–1904, että aaltoyhtälön ratkaisut ja sähkömagneettinen kenttä itse voidaan kirjoittaa skalaarifunktioilla. Se on oikeaa matematiikkaa, mutta se kuvaa *samoja* kenttiä $\mathbf E$ ja $\mathbf B$, ei uudenlaista aaltoa. Ainoa paikka, jossa potentiaaleilla on suoraan havaittavia vaikutuksia, on Aharonov–Bohm-ilmiö (1959): elektroni, joka kulkee magneettivuon $\Phi$ alueen ympäri, saa vaiheen

$$\Delta\varphi = \frac{e\Phi}{\hbar} = 2\pi\,\frac{\Phi}{h/e},\qquad h/e = 4.14\times10^{-15}\ \text{Wb},$$

vaikka magneettikenttä sen polulla olisi nolla. Tonomura et al. (1986) vahvistivat sen kentän ollessa täysin suljettu suprajohtavaan suojukseen. Ilmiö riippuu vain suljetun silmukan ympäröimästä vuosta, ja se seuraa standardista kvanttielektrodynamiikkaa.

**Ihmisen viestintänopeudet ovat mitattavissa.** 17 kielen yli puhe kantaa noin 39 bittiä sekunnissa (Coupé et al., 2019). Kirjoitettu englanti kantaa karkeasti 1 bitin merkkiä kohti, kun sen redundanssi on laskettu (Shannon, 1951).

## Taso 2 — Missä väite pettää

**1. Mikään ei kuljeta tietoa valoa nopeammin.** „PING! Vastaus ilmestyy mieleesi heti“ ei ole mahdollista todellisilla etäisyyksillä:

| Yhteys | Yksisuuntainen valoviive |
|---|---|
| Maa–Kuu | 1,28 s |
| Maa–Mars (lähimmästä kauimpaan) | 3,0–22,3 min |
| Proxima Centauri | 4,25 vuotta |

„Marsin pääkaupunki“ -kysymys saa vastauksensa aikaisintaan 6–45 minuuttia myöhemmin, meno-paluu.

**2. Kietoutuminen ei voi lähettää viestejä.** Kietoutuneelle parille laboratorio laskee Bobin paikallisen tilan sen jälkeen kun Alice mittaa minkä tahansa akselin suunnassa, ja löytää sen olevan aina täsmälleen $\tfrac12\mathbb 1$ (ero alle $10^{-15}$), sama kuin jos hän ei tekisi mitään. Korrelaatiot ovat todellisia (heidän tuloksensa ovat yhtä mieltä todennäköisyydellä $\cos^2(\Delta\theta/2)$), mutta ne näkyvät vasta kun kaksi tallennetta verrataan tavallisen kanavan yli. Tämä on ei-kommunikaatio-lause.

**3. Aivokentät ovat paljon liian heikkoja tavoittamaan ketään.** Dipolikenttä putoaa kuten $1/r^3$. Noin 4 cm:n päästä lähteestään mitattu 1 pT:n aivosignaali on noin $6\times10^{-17}$ T etäisyydellä 1 m ja $6\times10^{-26}$ T etäisyydellä 1 km, yli $10^{20}$ kertaa heikompi kuin Maan kenttä. Parhaat magnetometrit tarvitsevat suojattuja huoneita ja antureita päänahalla.

**4. „Skalaari“-kelat säteilevät ei mitään uutta.** Vastakkain käämitty (bifilaari) kela ajaa kaksi vastakkaista virtaa niin, että kentät kumoavat toisensa. Laboratorio laskee sekä sen, mitä jää läheltä, että sen, mikä säteilee:

- Akselilla yhden silmukan kenttä putoaa kuten $z^{-3.00}$; vastakkain käämityn parin jäännös putoaa kuten $z^{-4.00}$: tavallinen korkeampi multipoli.
- Kaukaa pari säteilee $(kd)^2/5$ yhden kelan tehosta, kun kelat ovat lähellä toisiaan ($kd \ll 1$). Arvolla $d = 0$ säteily on täsmälleen nolla. Mitään lisä-„skalaari“-aaltoa ei ilmesty, ja jos potentiaalitkin kumoavat, mitään ei jää vaikuttamaan — Aharonov–Bohm tai muuten.

**5. Suojaus.** Jos psykotroninen signaali olisi sähkömagneettinen, metallihuone, sukellusvene tai muutama metri merivettä katkaisisi sen, kuten yllä olevat ihosyvyydet näyttävät. Jos se ei ole sähkömagneettinen, tarina tarvitsee uuden luonnonvoiman, jota mikään koe ei ole nähnyt.

**6. Kaistanleveys.** 1 Mt:n lentokäsikirjan siirto puheen nopeudella kestää noin 57 tuntia. Sen lataaminen 5 s:ssä vaatisi $1.6\times10^6$ bit/s, noin 40 000 kertaa puheen nopeuden. Nykyiset BCI:t toimivat muutamalla bitillä sekunnissa. Emme myöskään tiedä, miten kirjoittaa taitoja tai muistoja aivoihin: se vaatisi synapsien tarkkaa muuttamista valtavan neuronimäärän yli.

**7. Noosfääri on filosofiaa, ei fysiikkaa.** Vernadsky ja Teilhard de Chardin käyttivät „noosfääriä“ kasvavasta ihmisajattelun pallosta ja sen vaikutuksesta planeettaan. Se on harkittu idea yhteiskunnasta ja evoluutiosta, ei mitattu ilmakehän kerros. Mehiläiset kyllä kommunikoivat, mutta fyysisten signaalien kautta: pyrstötanssi (waggle dance), feromonit ja värähtelyt.

## Taso 3 — Mitä pitäisi olla totta

Jotta psykotroninen internet olisi olemassa, kaikkien näiden pitäisi olla osoitettu. Jokainen on testattavissa:

- **Kantaja, joka ulottuu aivoista aivoihin.** Testi: lähettäjä ja vastaanottaja erillisissä Faraday-suojatuissa huoneissa, satunnaisilla kohdeviesteillä, sokealla pisteytyksellä ja etukäteen rekisteröidyllä analyysillä, toistettuna itsenäisissä laboratorioissa.
- **Tapa kiertää valonnopeus**, joka myös kumoaisi suhteellisuusteorian ja kausaliteetin. Testi: viesti, joka saapuu ennen kuin valo olisi voinut kuljettaa sen.
- **Luku–kirjoitus-liitäntä muistoille ja taidoille**: ymmärrys siitä, miten taito on tallennettu synapseihin riittävän hyvin, jotta se voidaan kirjoittaa toisiin aivoihin.

**Oikeita avoimia kysymyksiä lähellä tarinaa:** Kuinka nopeita ja turvallisia BCI:t voivat tulla, ja voidaanko ne tehdä ilman leikkausta? Kuinka suuren osan aivojen tiedosta ei-invasiiviset menetelmät (EEG, MEG, optisesti pumpattavat magnetometrit, funktionaalinen ultraääni) voivat lukea? Mitkä ovat yksityisyys- ja eettiset säännöt „hermodatalle“?

## Aja laboratorio

```bash
python Module_12_The_Psychotronic_Internet/simulation.py
python -m pytest tests/test_module_12.py
```

| Koe | Mitä se näyttää |
|---|---|
| `skin_depth`, `attenuation_length`, `shield_absorption_db` | Merivesi ja metalli estävät vaihtuvia kenttiä; $\delta \propto f^{-1/2}$. |
| `conducting_sphere_field` | Coulombin lain summaus indusoidun varauksen yli antaa nollakentän johtimen sisällä. |
| `antiparallel_pair_power`, `counterwound_axis_field` | Vastakkaiset virrat jättävät tavallisen, nopeammin vaimenevan multipolin, ei uutta aaltoa. |
| `aharonov_bohm_phase` | Potentiaalien oikea, mitattu vaikutus. |
| `light_delay`, `bob_state`, `same_outcome_probability` | Valonopeuden viiveet; kietoutuminen korreloi mutta ei voi signaloida. |
| `brain_field`, `bci_bits_per_second`, `transfer_time` | Kuinka heikkoja aivokentät ovat ja kuinka hitaita ihmisen datanopeudet ovat. |

## Kokeile itse

1. Etsi taajuus, jolla meriveden ihosyvyys on 100 m. Miksi laivaston sukellusveneradio lähetti vain muutaman merkin minuutissa?
2. Funktiossa `bob_state` korvaa Bell-tila tilalla $(\lvert00\rangle + \lvert11\rangle)$ plus pienellä $\lvert01\rangle$-sekoituksella (normalisoi se). Muuttaako Alicen kulman valinta nyt Bobin tilaa?
3. Funktiolla `antiparallel_pair_power`, kuinka kaukana toisistaan kahden vastakkaisen 1 kHz:n kelan on oltava (km:inä), ennen kuin ne säteilevät yhtä paljon kuin yksi kela?
4. Etsi lukemisen informaationopeus. Kuinka kauan kestäisi lukea kaikki internetissä sillä nopeudella?

## Viitteet

- Whittaker, E. T., "On the partial differential equations of mathematical physics", *Math. Ann.* **57**, 333 (1903).
- Whittaker, E. T., "On an expression of the electromagnetic field due to electrons by means of two scalar potential functions", *Proc. London Math. Soc.* **s2‑1**, 367 (1904).
- Aharonov, Y. & Bohm, D., "Significance of electromagnetic potentials in the quantum theory", *Phys. Rev.* **115**, 485 (1959).
- Tonomura, A. et al., "Evidence for Aharonov‑Bohm effect with magnetic field completely shielded from electron wave", *Phys. Rev. Lett.* **56**, 792 (1986).
- Ghirardi, G. C., Rimini, A. & Weber, T., "A general argument against superluminal transmission through the quantum mechanical measurement process", *Lett. Nuovo Cimento* **27**, 293 (1980).
- Nielsen, M. A. & Chuang, I. L., *Quantum Computation and Quantum Information*, Cambridge University Press (2000).
- Hämäläinen, M. et al., "Magnetoencephalography—theory, instrumentation, and applications to noninvasive studies of the working human brain", *Rev. Mod. Phys.* **65**, 413 (1993).
- Willett, F. R. et al., "High‑performance brain‑to‑text communication via handwriting", *Nature* **593**, 249 (2021).
- Willett, F. R. et al., "A high‑performance speech neuroprosthesis", *Nature* **620**, 1031 (2023).
- Coupé, C., Oh, Y. M., Dediu, D. & Pellegrino, F., "Different languages, similar encoding efficiency: Comparable information rates across the human communicative niche", *Science Advances* **5**, eaaw2594 (2019).
- Shannon, C. E., "Prediction and entropy of printed English", *Bell Syst. Tech. J.* **30**, 50 (1951).
- Vernadsky, V. I., "The biosphere and the noosphere", *American Scientist* **33**, 1 (1945).
- Teilhard de Chardin, P., *The Phenomenon of Man* (1955; englanninkielinen käännös 1959).
