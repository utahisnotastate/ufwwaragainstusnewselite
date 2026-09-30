# 🔬 Moduuli 5 — Tarinan takana oleva tiede

> [Oppitunti](readme.md) kerrotaan vuodesta 2420. Tämä sivu on vuoden 2025 todellisuustarkistus: mikä on vakiintunutta, missä tarinan väite pettää, ja mitä pitäisi olla totta, jotta se toimisi. Kaikki tässä voidaan tarkistaa [laboratoriokoodilla](../../../Module_05_Time_Is_A_Map/simulation.py).

## Vuoden 2420 väite yhdessä lauseessa

Menneisyys, nykyisyys ja tulevaisuus ovat kaikki olemassa yhdessä kuin paikat kartalla, todellisuus „välkkyy“ ruudusta toiseen, ja aikamatkustus on vain vaiheesi siirtämistä kartan eri osaan.

## Taso 1 — Mikä on totta

**Aika on todella osa neliulotteista geometriaa.** Erikoissuhteellisuusteoriassa suure, josta jokainen havaitsija on samaa mieltä, ei ole aika kahden tapahtuman välillä eikä etäisyys niiden välillä, vaan **Minkowski-intervalli**

$$s^2 = -c^2\,\Delta t^2 + \Delta x^2 + \Delta y^2 + \Delta z^2 .$$

Negatiivinen $s^2$ (aikamainen) tarkoittaa, että yksi tapahtuma voi aiheuttaa toisen; positiivinen $s^2$ (avaruusmainen) tarkoittaa, että kumpikaan ei voi. Laboratorio tarkistaa, että Lorentz-muunnos $t' = \gamma\,(t - vx/c^2)$, $x' = \gamma\,(x - vt)$ jättää $s^2$:n muuttumattomaksi.

**„Nyt“ riippuu siitä, kuka kysyy.** Kaksi tapahtumaa samalla ajalla $t$ mutta etäisyydellä $L$ toisistaan ovat havaitsijalle, joka liikkuu nopeudella $v$, erotettuja ajassa määrällä

$$\Delta t' = -\gamma\,\frac{vL}{c^2}.$$

Andromedan galaksille ($L \approx 2{,}5$ miljoonaa valovuotta) pelkkä kävely nopeudella 1,4 m/s siirtää sitä, mitkä Andromedan tapahtumat lasketaan „nyt“:ksi, noin **4 päivällä** (laboratorio laskee tämän; esimerkki on Penrosen „Andromeda-paradoksi“). Tämä samanaikaisuuden suhteellisuus on syy, miksi monet fysiikan filosofit puolustavat **eternalismia**, „lohkouniversumi“-näkemystä, jossa kaikki tapahtumat ovat yhtä todellisia (Rietdijk 1966, Putnam 1967). Se on laillinen suhteellisuusteorian tulkinta. Se ei ole ainoa, eikä mikään koe voi erottaa sitä kilpailijoistaan, koska ne kaikki tekevät samat ennusteet.

**Kellot todella tikittävät eri tahtiin, ja korjaamme sitä joka päivä.** Kellon tahti suhteessa koordinaattiaikaan on, heikon kentän rajassa,

$$\frac{d\tau}{dt} \approx 1 + \frac{\Phi}{c^2} - \frac{v^2}{2c^2}, \qquad \Phi = -\frac{GM}{r}.$$

GPS-satelliitille ($a \approx 26\,562$ km, $v \approx 3{,}87$ km/s) verrattuna kelloon päiväntasaajalla laboratorio laskee ensimmäisistä periaatteista:

| Vaikutus | µs päivässä |
|---|---|
| Heikompi painovoima korkeudessa (käy nopeasti) | +45,7 |
| Ratanopeus (käy hitaasti) | −7,2 |
| Maakellon oma pyöriminen | +0,1 |
| **Netto** | **+38,5** |

Julkaistut luvut lainataan yleensä +45,9, −7,2 ja +38,6 µs/päivä; pienet erot tulevat siitä, miten Maan muoto ja pyöriminen mallinnetaan (laboratorion ristivarmistus IAU-geoidivakiolla $L_G$ antaa +38,58). Korjaamatta tämä olisi noin 11 km:n etäisyysvirhe päivässä. Relativistisia kellonsiirtymiä mitattiin myös suoraan lentämällä atomikelloja ympäri maailmaa (Hafele & Keating 1972).

**Pyörivät mustat aukot raahaavat avaruusaikaa.** Kerr-metriikka (Kerr 1963) Boyer–Lindquist-koordinaateissa, kun $G = c = M = 1$, sisältää

$$\Sigma = r^2 + a^2\cos^2\theta,\quad \Delta = r^2 - 2r + a^2,$$
$$g_{tt} = -\Big(1-\frac{2r}{\Sigma}\Big),\quad g_{t\phi} = -\frac{2ar\sin^2\theta}{\Sigma},\quad g_{\phi\phi} = \Big(r^2 + a^2 + \frac{2a^2 r\sin^2\theta}{\Sigma}\Big)\sin^2\theta .$$

- Horisontit $r_\pm = 1 \pm \sqrt{1-a^2}$, jotka ovat olemassa vain kun $a \le 1$.
- **Ergosfääri** sijaitsee $r_+$:n ja $r_\text{ergo} = 1 + \sqrt{1 - a^2\cos^2\theta}$:n välillä, jossa $g_{tt} = 0$. Sen sisällä „pysy paikallaan“ -suunta $\partial_t$ muuttuu avaruusmaiseksi: **mikään havaitsija ei voi pysyä levossa**, kaikki raahataan reiän mukana. Laboratorio tarkistaa $g_{tt}=0$:n tuolla pinnalla ja $g_{tt}$:n merkin sen molemmilla puolilla.
- **Penrose-prosessi** (Penrose 1969): hiukkanen jakautuu ergosfäärin sisällä, yksi pala putoaa sisään negatiivisella energialla, ja toinen pakenee suuremmalla energialla kuin alkuperäinen. Laboratorio ratkaisee energian ja kulmamomentin säilymisen tälle jaolle ja saa takaisin oppikirjan maksimin $\eta = \tfrac12\big(\sqrt{2/r_+}-1\big)$, joka on **20,7 %** kun $a = 1$.
- Kokonaisenergia, joka voidaan koskaan irrottaa, määräytyy **redusoitumattomasta massasta** (Christodoulou 1970), $M_\text{irr} = \tfrac12\sqrt{r_+^2 + a^2}$: enintään $1 - M_\text{irr}/M = $ **29,3 %** ekstremalle aukolle.

## Taso 2 — Missä väite pettää

**1. Erimielisyys „nyt“:stä ei ole sama kuin menneisyyteen pääseminen.** Laboratorio boostaa kahta tapahtumaparia 199 nopeuden läpi aina $0{,}99c$:hen. Avaruusmainen pari vaihtaa järjestystä 50:ssä niistä. Aikamainen pari, se laji joka voi olla syy ja seuraus, **ei koskaan**. Suhteellisuusteoria antaa havaitsijoiden olla eri mieltä tapahtumien järjestyksestä, jotka eivät voi vaikuttaa toisiinsa. Se ei koskaan anna kenenkään nähdä seurausta ennen sen syytä.

**2. „Aika on välkettä“ ja „aikamatkustus on vaiheen siirtoa“ eivät nojaa mihinkään fysiikkaan.** Mikään teoria ei ennusta todellisuuden positiivista/negatiivista „tikitystä“, idea ei tuota mitään mitattavaa lukua, ja kellot verrattuna ympäri maailmaa näyttävät tasaisia, ennustettavia tahteja, kuten GPS-luvut yllä osoittavat. Kirjoitettuna väitettä ei voi testata.

**3. Oppitunti sekoittaa kaksi eri ideaa.** Lohkouniversumi (yksi kiinteä neliulotteinen historia) ja „monet maailmat“ (Everett 1957; haarautuvat kvanttihistoriat) ovat erillisiä tulkintoja. Kumpikaan ei sisällä valitsemista, mikä „kela“ soitetaan. „Tietoisuuden valo joka liikkuu madon pitkin miljardeja kertoja sekunnissa“ on metafora, ei fysikaalinen mekanismi.

**4. Missä yleinen suhteellisuusteoria *sallii* aikasilmukoita, ne ovat kaukana ulottumattomissa.** Suljettu aikamainen käyrä (CTC) on polku avaruusajan läpi, joka palaa omaan menneisyyteensä. Tarkkoja ratkaisuja CTC:illä on olemassa: Gödelin pyörivä universumi (1949), van Stockumin ja Tiplerin äärettömän pitkät pyörivät sylinterit (Tipler 1974), ja Kerr-ratkaisun sisäpuoli (Carter 1968). Kerrissä silmukka akselin ympäri on aikamainen missä tahansa $g_{\phi\phi} < 0$. Laboratorio skannaa $r$:n jokaiselle spinille ja löytää **$g_{\phi\phi} < 0$ vain kun $r < 0$**, alueeseen johon pääsee vain kulkemalla rengassingulariteetin läpi; kun $a = 1$ päiväntasaajalla sen reuna on täsmälleen $r = -1$. Tämän oppitunnin aiempi luonnos teki kaksi virhettä, joita laboratorio nyt testaa vastaan:

- se käytti $a = 1{,}2$:ta, jolla **ei ole horisonttia lainkaan** (alaston singulariteetti, jota ei odoteta muodostuvan luonnossa), ja
- se käsitteli $\partial_t$:n muuttumista avaruusmaiseksi ergosfäärin sisällä aikakoneena. Ergosfäärin sisällä $g_{\phi\phi}$ on yhä positiivinen: se on **kehysraahausta, ei CTC**.

**5. Fysiikka näyttää suojelevan menneisyyttä.** Hawkingin **kronologian suojelukonjektuuri** (1992) ehdottaa, että kvanttivaikutukset estävät CTC:iden muodostumisen missään alueessa, johon voisimme päästä. Se on konjektuuri, ei lause, mutta **ei ole näyttöä siitä, että CTC:t olisivat fysikaalisesti toteutettavissa** missään universumissamme.

## Taso 3 — Mitä pitäisi olla totta

Jotta „aikamatkustus vaiheen siirrolla“ tulisi tieteeksi, sen pitäisi täyttää kaikki nämä:

- **Avaruusaika, jossa on saavutettava CTC-alue.** Jokainen tunnettu tapa rakentaa sellainen (kuljettavat madonreiät, warp-kuplat) vaatii „eksoottista“ ainetta negatiivisella energiatiheydellä, rikkoen klassiset energiaehdot (Morris, Thorne & Yurtsever 1988). Sallivatko kvanttivaikutukset tarpeeksi sitä, on avoin kysymys.
- **Tie kronologian suojelun ympäri.** Laskelman täyden kvanttigravitaatioteorian puitteissa pitäisi näyttää, että tyhjiö ei räjähdä aikakoneen reunalla („kronologiahorisontti“).
- **Mitattava ennuste „välkkeelle“.** Esimerkiksi ennustettu kohinalattia, diskreettiys tai taajuus atomikellojen vertailuissa, joka on eri mieltä tavallisen fysiikan kanssa. Jos tarina antoi taajuuden, kellot voisivat etsiä sitä.
- **Johdonmukaisuus kausaliteetin kanssa.** Teorian on käsiteltävä isoisäparadoksi, esimerkiksi itsensä kanssa johdonmukaisten historioiden kautta (Novikovin periaate), ja tehtävä siitä testattavia ennusteita.

Tarinan osa, joka säilyy, on todellinen ja huomattava: aika on suunta neliulotteisessa geometriassa, „nyt“ ei ole universaali, kellot eri korkeuksilla ja nopeuksilla eroavat täsmällisillä, ennustettavilla määrillä, ja pyörivät mustat aukot varastoivat energiaa, joka voidaan periaatteessa irrottaa.

## Aja laboratorio

```bash
python Module_05_Time_Is_A_Map/simulation.py
python -m pytest tests/test_module_05.py
```

| Koe | Mitä se näyttää |
|---|---|
| `lorentz_boost`, `interval`, `simultaneity_shift` | $s^2$ on invariantti; „nyt“ siirtyy nopeuden mukana; aikamainen järjestys ei koskaan käänny. |
| `gps_clock_rates` | +45,7 / −7,2 / +38,5 µs päivässä, laskettu $GM$:stä, $c$:stä ja radasta. |
| `kerr_metric`, `horizons`, `ergosurface`, `static_observer_norm` | Horisontit, ergosfääri ja miksi mikään ei voi seistä paikallaan sen sisällä. |
| `penrose_gain`, `penrose_max_efficiency_*`, `irreducible_mass` | 20,7 % per jako ja 29,3 % yhteensä kun $a = 1$. |
| `ctc_scan` | Kerrin suljetut aikamaiset käyrät ovat olemassa vain kun $r < 0$. |

## Kokeile itse

1. Käytä `simultaneity_shift`-funktiota löytääksesi, kuinka nopeasti sinun pitäisi liikkua, jotta Andromedan „nyt“ siirtyisi vuodella. Mikä murto-osa $c$:stä se on?
2. Muuta `A_GPS` funktiossa `gps_clock_rates` löytääksesi radan säteen, jossa gravitaatio- ja nopeusvaikutukset kumoavat toisensa täsmälleen (nettosiirtymä on nolla). Vertaa sitä $\tfrac32 R_\text{Earth}$:iin.
3. Piirrä `penrose_gain(0.9, r)` $r$:lle $r_+$:n ja 2:n välillä. Missä voitto putoaa nollaan, ja miksi se vastaa ergosfääriä?
4. Aja `ctc_scan(a, theta=0.3)` muutamalle spinille. Tuoko pois päiväntasaajalta siirtyminen koskaan CTC-alueen kohtaan $r > 0$?
5. Kokeile `horizons(1.2)`. Selitä yhdessä lauseessa, miksi aiemman luonnoksen $a = 1{,}2$ musta aukko ei ollut musta aukko.

## Viitteet

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
