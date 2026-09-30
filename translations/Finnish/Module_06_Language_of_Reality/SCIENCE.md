# 🔬 Moduuli 6 — Tarinan takana oleva tiede

> [Oppitunti](readme.md) kerrotaan vuodesta 2420. Tämä sivu on vuoden 2025 todellisuustarkistus: mikä on vakiintunutta, missä tarinan väite pettää, ja mitä pitäisi olla totta, jotta se toimisi. Kaikki tässä voidaan tarkistaa [laboratoriokoodilla](../../../Module_06_Language_of_Reality/simulation.py).

## Vuoden 2420 väite yhdessä lauseessa

Kaikki muodot luonnossa ovat „jäätynyttä ääntä“: seisova aalto järjestää ainetta kuten viulunjousi järjestää hiekkaa levyllä, joten oikea ääni voi rakentaa ainetta, liuottaa sitä tai tehdä kivestä painottoman.

## Taso 1 — Mikä on totta

**Chladnin kuviot ovat todellisia, ja ne ovat kaunista fysiikkaa.** Ernst Chladni (1787) jousitti hiekalla peitettyjä metallilevyjä ja havaitsi, että hiekka kerääntyy **solmulinjoille**, joissa levy ei liiku. Jokainen nuotti antaa eri kuvion. Kuviot määrää levyn liikeyhtälö.

**Rumpukalvo ja levy noudattavat eri yhtälöitä.** Kiristetty kalvo (rumpukalvo) noudattaa aalto- (Helmholtz-) yhtälöä, $\nabla^2 w + k^2 w = 0$. Kiinteäreunaisen neliökalvon sivulla $L$ taajuudet ovat

$$f_{mn} = \frac{c}{2L}\sqrt{m^2+n^2}.$$

Chladnin levy on ohut, jäykkä **levy**, jota hallitsee Kirchhoffin biharmoninen yhtälö

$$D\,\nabla^4 w - \rho h\,\omega^2 w = 0, \qquad D = \frac{E h^3}{12(1-\nu^2)} .$$

Yksinkertaisesti tuetulle neliölevylle tarkka vastaus on $\omega_{mn} = \sqrt{D/\rho h}\;\pi^2 (m^2+n^2)/L^2$, joten $f_{mn} \propto m^2 + n^2$, **ei** $\sqrt{m^2+n^2}$. Se on todellinen, testattava opetus: moodi (1,2) istuu $\sqrt{5/2} = 1{,}58$ kertaa perustaajuudella rummulla, mutta $5/2 = 2{,}5$ kertaa levyllä. Laboratorio ratkaisee molemmat yhtälöt numeerisesti (5-pisteen Helmholtz-stencil ja 13-pisteen biharmoninen stencil) ja vastaa tarkkoja tuloksia paremmin kuin 0,5 %:iin, odotetulla toisen kertaluvun konvergenssilla.

Kun kahdella moodilla on sama taajuus (esimerkiksi (1,2) ja (2,1) neliöllä), levy värähtelee seoksessa, $\sin m\pi x\,\sin n\pi y \pm \sin n\pi x\,\sin m\pi y$. Nämä seokset tuottavat todellisten Chladnin kuvioiden diagonaalit, renkaat ja tähdet; laboratorio tarkistaa, että „−“-seoksella on solmulinja täsmälleen diagonaalilla. Chladnin omat vapaa-reunaiset levyt ovat vaikeampia ratkaista (Leissa 1969 kokoaa klassiset tulokset). Pyöreille levyille **Chladnin laki** $f \approx C\,(m + 2n)^p$, jossa $m$ solmuhalkaisijaa, $n$ solmurenkaita ja $p \approx 2$ litteille levyille, on hyvä empiirinen sääntö (Rossing 1982).

**Ääni voi todella työntää, vangita ja levitoida pieniä kappaleita.** Seisova aalto kohdistaa vakaan **akustisen säteilyvoiman** hiukkaseen, joka on paljon aallonpituutta pienempi. Gor'kov (1962) näytti, että se tulee potentiaalista,

$$U = 2\pi R^3\left[\frac{f_1\,\langle p^2\rangle}{3\rho_0 c_0^2} - \frac{f_2\,\rho_0\langle v^2\rangle}{2}\right], \qquad \mathbf F = -\nabla U,$$

$$f_1 = 1 - \frac{\kappa_p}{\kappa_0}, \qquad f_2 = \frac{2(\rho_p-\rho_0)}{2\rho_p+\rho_0} .$$

Koska $\mathbf F = -\nabla U$, tämä voima on **konservatiivinen** (moduulin aiempi luonnos kutsui sitä epäkonservatiiviseksi, mikä oli väärin): suljetulla polulla hiukkasen kantamisesta ei tehdä nettovoimaa, ja hiukkaset asettuvat $U$:n minimoihin. 1D-seisovassa aallossa $p = p_0\cos kx\cos\omega t$ siitä tulee $F = 4\pi\Phi\,kR^3 E_\text{ac}\sin 2kx$, kontrastitekijällä $\Phi = f_1/3 + f_2/2$ ja energiatiheydellä $E_\text{ac} = p_0^2/4\rho_0 c_0^2$ (Bruus 2012). Laboratorio tarkistaa $U$:n numeerisen gradientin tätä kaavaa vastaan, näyttää nollan nettovoiman aallonpituuden yli, ja antaa hiukkasten ajautua:

- polystyreeni vedessä ($\Phi = +0{,}22$) kerääntyy **painesolmuihin**,
- lipidipisara vedessä ($\Phi = -0{,}07$) kerääntyy **paineantinodeihin**.

Tämä on akustofluidisten solulajittelijoiden ja **akustisten levitattoreiden** toimintaperiaate. Marzo et al. (2015) rakensivat holografiset akustiset pinsetit 40 kHz:n anturien ryhmistä, jotka levitovat ja liikuttavat millimetripalloja ilmassa. Laboratorio arvioi tarvittavan paineen: noin 280 Pa (140 dB) vaahtopallolle ja noin 1,8 kPa (156 dB) kiinteälle polystyreenille, riippumatta pallon koosta niin kauan kuin pallo on paljon pienempi kuin 8,6 mm:n aallonpituus.

**Lumihiutaleet ovat kuusikulmaisia oikeasta syystä, mutta se ei ole ääni.** Tavallisella jäällä (jää Ih) on kuusikulmainen kidehila, jonka määräävät vety-sidosten geometria vesimolekyylien välillä. Lumikiteen kuusinkertainen muoto tulee tuosta hilasta ja siitä, miten höyry diffundoituu sen päälle (Libbrecht 2005).

## Taso 2 — Missä väite pettää

**1. Kuvion mittakaava on aallonpituus.** Ääni voi järjestää ainetta vain puolen aallonpituuden mittakaavassa: 4,3 mm taajuudella 40 kHz ilmassa. Yksittäisten atomien (~0,1 nm) sijoittamiseen tarvittaisiin 0,2 nm:n aallonpituus. Laboratorio näyttää, miksi se on mahdotonta:

| Väliaine | Tarvittava taajuus | Raja |
|---|---|---|
| Kiinteä ($c \approx 5$ km/s) | ~25 THz | Pii:n korkein värähtely on 15,6 THz, ja lyhin aalto jonka hila voi kantaa on kaksi kertaa atomiväli, 0,47 nm. |
| Ilma | ~1,7 × 10¹² Hz | Ääntä ei ole olemassa molekyylien vapaan matkan (~66 nm) alapuolella, mikä rajaa sen lähelle 5 GHz. |

Atomin mittakaavassa „ääni“ (fononit) on atomit itse värähtelemässä. Se ei voi olla malli, joka sijoittaa ne.

**2. Värähtelyt ratsastavat sidoksilla; ne eivät tee niitä.** Pii:n korkein fononi kantaa 65 meV. Yhden atomin poistaminen kiteestä maksaa 4,63 eV, noin 70 kertaa enemmän. Mikä pitää aineen koossa, on elektronien kvanttimekaniikka (kemialliset sidokset), ei ylläpitävä sävel.

**3. Suuria kiviä ei voi laulaa ilmaan.** Gor'kovin kaava pätee vain kappaleisiin, jotka ovat paljon aallonpituutta pienempiä. 2 m:n lohkolle aallonpituuden on oltava kymmeniä metrejä (noin 17 Hz). Graniitin pitäminen tuolla taajuudella tarvitsee 1,4 ilmakehän paineamplitudin: kunkin syklin matalapaineisen puoliskon pitäisi pudota **tyhjiön alle**, mitä ilma ei voi tehdä. Mikään akustiikassa ei saa kappaletta „unohtamaan olevansa raskas“. Vaihekonjugaatio eli „aikakäännetty akustiikka“ on todellista (Fink 1997), mutta se fokusoi aallot takaisin lähteeseensä. Se ei kumoa painoa.

**4. Teorian nimet eivät pidä.** „Formon-teoria“ (Bearden) **ei ole tunnustettu teoria fysiikassa**: sillä ei ole vertaisarvioitua muotoilua eikä kokeellista tukea. „Skalaariäänellä joka työntää avaruusaikaa“ ei ole vastinetta fysiikassa. Pitkittäisaallot ovat vain tavallista ääntä (ilmassa kaikki ääni on pitkittäistä), ja ne työntävät ainetta, ei avaruusaikaa. Hans Jennyn *Cymatics* (1967) on kaunis valokuvallinen tallenne värähtelykuvioista, mutta se ei näytä, että aine olisi „jäätynyttä ääntä“.

## Taso 3 — Mitä pitäisi olla totta

Jotta „aineen rakentaminen äänellä“ olisi enemmän kuin metafora, sen tarvittaisiin kaikki nämä:

- **Aalto, jolla on atomin mittakaavan aallonpituus ja joka ei koostu atomeista joita se järjestää.** Valolla ja elektronisäteillä on näin lyhyitä aallonpituuksia. Siksi optiset pinsetit, elektronimikroskoopit ja skannaavat „atomikirjoitus“-luotaimet toimivat, ja ne tekevät sen sähkömagnetismin kautta, ei äänen.
- **Energia per kvantti verrattavissa sidosenergioihin (eV).** Vain silloin aalto voisi tehdä tai rikkoa sidoksia suoraan. Äänikvantit huipentuvat kymmeniin meV:ihin.
- **Kvantitatiivinen ennuste.** Esimerkiksi tietty taajuus, joka mitattavasti muuttaa kiteen rakennetta tai kiven painoa, jota laboratorio voisi sitten testata. Mitään ei ole julkaistu.

Todelliset, avoimet rajat ovat vaatimattomampia ja yhä jännittäviä: akustiset hologrammit jotka kokoavat monta hiukkasta kerralla, solujen ja kudosten akustinen manipulointi, ja fononikiteet jotka on suunniteltu ohjaamaan ääntä ja lämpöä.

## Aja laboratorio

```bash
python Module_06_Language_of_Reality/simulation.py
python -m pytest tests/test_module_06.py
```

| Koe | Mitä se näyttää |
|---|---|
| `membrane_frequencies`, `membrane_modes_fd` | Rumpukalvo: $f \propto \sqrt{m^2+n^2}$, vahvistettu äärellisdifferenssiratkaisulla. |
| `plate_frequencies`, `plate_modes_fd`, `biharmonic_simply_supported` | Levy: $f \propto m^2+n^2$, vahvistettu 13-pisteen biharmonisella ratkaisulla. |
| `chladni_pattern` | Degeneroituneet moodiseokset ja niiden solmulinjat (joihin hiekka kerääntyy). |
| `gorkov_potential_1d`, `gorkov_force_1d`, `settle_positions` | Konservatiivinen säteilyvoima; positiivinen kontrasti menee solmuihin, negatiivinen antinodeihin. |
| `levitation_pressure`, `spl_db` | 140–156 dB levittaa palloja; kivi tarvitsee „tyhjiön alle“ -paineita. |
| `atom_scale_sound`, `mean_free_path_air` | Miksi ääni ei voi sijoittaa atomeja. |

## Kokeile itse

1. Funktiossa `biharmonic_simply_supported` vaihda haamu-solmun merkki $-1$:stä $+1$:een. Tämä muuttaa reunat „yksinkertaisesti tuetuista“ „puristetuiksi“. Mitä tapahtuu suhteelle $f_{21}/f_{11}$? (Puristetut levyt ovat lähempänä oikeita kelloja ja symbaaleja.)
2. Piirrä `chladni_pattern(1, 3, sign=+1)` ja `sign=-1` kuvina (käytä mitä tahansa piirrostyökalua) ja merkitse missä $|w|$ on pieni. Kumpi näyttää enemmän Chladnin kuviolta jonka olet nähnyt?
3. Käytä `levitation_pressure`-funktiota löytääksesi taajuuden, jolla 1 mm:n vesipisara voidaan levitoida 150 dB:llä. Onko pisara yhä paljon aallonpituutta pienempi?
4. Toista `atom_scale_sound` timantille, jonka äänennopeus on noin 18 km/s ja jonka korkein fononi on noin 1332 cm⁻¹. Pääseekö se lähemmäs „atomien sijoittamista“?
5. Laske $\Phi$ punasoluille plasmassa (etsi likimääräiset tiheydet ja äänennopeudet). Menevätkö ne solmuihin vai antinodeihin?

## Viitteet

- Chladni, E. F. F., *Entdeckungen über die Theorie des Klanges*, Leipzig (1787).
- Leissa, A. W., *Vibration of Plates*, NASA SP‑160 (1969).
- Fletcher, N. H. & Rossing, T. D., *The Physics of Musical Instruments*, 2nd ed., Springer (1998). Plate modes and Chladni patterns.
- Rossing, T. D., "Chladni's law for vibrating plates", *Am. J. Phys.* **50**, 271 (1982).
- Gor'kov, L. P., "On the forces acting on a small particle in an acoustical field in an ideal fluid", *Sov. Phys. Dokl.* **6**, 773 (1962).
- Bruus, H., "Acoustofluidics 7: The acoustic radiation force on small particles", *Lab Chip* **12**, 1014 (2012).
- Marzo, A. et al., "Holographic acoustic elements for manipulation of levitated objects", *Nat. Commun.* **6**, 8661 (2015).
- Fink, M., "Time reversed acoustics", *Physics Today* **50**(3), 34 (1997).
- Libbrecht, K. G., "The physics of snow crystals", *Rep. Prog. Phys.* **68**, 855 (2005).
- Kittel, C., *Introduction to Solid State Physics*, 8th ed., Wiley (2005). Cohesive energies and phonons.
- Jenny, H., *Kymatik / Cymatics*, Basilius Presse (1967).
