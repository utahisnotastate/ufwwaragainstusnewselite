# 🔬 Moduuli 8 — Tarinan takana oleva tiede

> [Oppitunti](readme.md) kerrotaan vuodesta 2420. Tämä sivu on vuoden 2025 todellisuustarkistus: mikä on vakiintunutta, missä tarinan väite pettää, ja mitä pitäisi olla totta, jotta se toimisi. Kaikki tässä voidaan tarkistaa [laboratoriokoodilla](../../../Module_08_Instant_Travel/simulation.py).

## Vuoden 2420 väite yhdessä lauseessa

Etäisyys on harha: jos virität kehosi määränpään „taajuuteen“, katoat täältä ja ilmestyt sinne nolla‑ajassa, ilman nopeusrajaa, koska hyppäsit avaruuden yli sen sijaan, että ylittäisit sen.

## Taso 1 — Mikä on totta

**Yleinen suhteellisuusteoria todella sallii „avaruuden liikuttamisen itsesi sijaan“ — paperilla.** Miguel Alcubierre (1994) kirjoitti avaruusajan, jossa litteän avaruuden kupla kuljetetaan millä tahansa nopeudella $v_s$, jopa valoa nopeammin. Yksiköissä joissa $G = c = 1$:

$$ds^2 = -dt^2 + \big(dx - v_s f(r_s)\,dt\big)^2 + dy^2 + dz^2,$$

$$f(r) = \frac{\tanh\!\big(\sigma(r+R)\big) - \tanh\!\big(\sigma(r-R)\big)}{2\tanh(\sigma R)},$$

missä $r_s$ on etäisyys kuplan keskipisteestä $x_s(t)$, $R$ on kuplan säde ja $1/\sigma$ asettaa seinämän paksuuden. $f = 1$ sisällä (matkustaja leijuu vapaassa pudotuksessa, ilman kiihtyvyyden tunnetta) ja $f \to 0$ kaukana.

- **Avaruus kutistuu edessä ja kasvaa takana.** Viipalointiin levossa olevien havaitsijoiden tilavuuselementtien laajeneminen (York‑laajeneminen) on

$$\theta = v_s\,\frac{x - x_s}{r_s}\,\frac{df}{dr_s},$$

joka on negatiivinen kuplan edessä, positiivinen takana, ja nolla sisällä sekä kaukana. Laboratorio vahvistaa kaikki neljä ominaisuutta numeerisesti.

- **Hinta on negatiivinen energia.** Einsteinin yhtälöt kertovat, millaista ainetta tarvittaisiin tämän geometrian tekemiseen. Viipalointiin levossa oleville havaitsijoille energiatiheys on

$$T^{00} = -\frac{1}{8\pi}\,\frac{v_s^2\,(y^2+z^2)}{4\,r_s^2}\left(\frac{df}{dr_s}\right)^2 \;\le\; 0 .$$

Se on **negatiivinen kaikkialla, missä se on nollasta poikkeava**: heikon energiaehdon rikkomus. Integrointi koko avaruuden yli (laboratorio tekee tämän numeerisesti ja tarkistaa sen raakaa 3‑D‑summaa vasten) antaa ohuelle seinämälle

$$E \;\approx\; -\frac{v_s^2 R^2 \sigma}{36} \qquad (G=c=1),$$

joten energialasku kasvaa nopeuden neliön, kuplan koon neliön ja seinämän paksuuden käänteisen verrannollisuuden mukaan.

- **Negatiivista energiatiheyttä on olemassa — vähän.** Kahden rinnakkaisen peilin välillä etäisyydellä $d$ kvanttityhjiöllä on energiatiheys $u = -\pi^2\hbar c/(720\,d^4)$ (Casimir, 1948). Tuloksena oleva voima on mitattu (esim. Lamoreaux, 1997). Kun $d = 100$ nm, $u \approx -4$ J/m³.

- **„Teleportaatio“ on oikea sana fysiikassa — informaatiolle, ei kehoille.** Kvanttiteleportaatio (Bennett et al., 1993; ensimmäisenä osoittivat Bouwmeester et al., 1997) siirtää hiukkasen kvantti*tilan* toiseen hiukkaseen, joka on jo määränpäässä. Se tarvitsee tavallisen klassisen viestin, joka lähetetään valon nopeudella tai sitä hitaammin, työn loppuunsaattamiseksi. Mikään ei kulje valoa nopeammin eikä ainetta siirretä.

- **Kaksi kelloa.** Sympaattinen resonanssi on totta, mutta toinen kello soi, koska ääniaallot kantavat energiaa huoneen poikki noin 343 m/s. Se on hidas, tavallinen siirto ilman kautta, ei hyppy.

## Taso 2 — Missä väite pettää

**1. Kvanttiepäyhtälöt murskaavat seinämän.** Kvanttikenttäteoria sallii negatiivisen energian, mutta vain vähän ja vain lyhyesti. Massattomalle skalaarikentälle litteässä avaruusajassa havaitsija, joka keskiarvoistaa energiatiheyden Lorentz‑painotuksella leveydellä $t_0$, löytää aina (Ford & Roman)

$$\langle\rho\rangle \;\ge\; -\frac{3\hbar}{32\pi^2 c^3\,t_0^4}.$$

Mitä lyhyempi aika, sitä enemmän negatiivista energiaa sallitaan, mutta raja kiristyy kuten $t_0^{-4}$. Pfenning & Ford (1997) sovelsivat tätä Alcubierre‑kuplaan näytteenottoajoilla, jotka ovat lyhyitä verrattuna seinämän kaarevuusasteikkoon, ja havaitsivat, että seinämä voi olla enintään luokkaa sata Planckin pituutta paksu kun $v_s \sim c$, ja että kokonaisnegatiivinen energia ylittää silloin näkyvän maailmankaikkeuden massan kauas.

Laboratorio toistaa *suuruusluokan* yksinkertaisemmalla oikotiellä: se vaatii, että seinämän negatiivisin $T^{00}$ kunnioittaa rajaa arvolla $t_0 = 0{,}1\,\Delta/c$ ($\Delta$ = seinämän paksuus). 100 m:n kuplalle nopeudella $v_s = c$:

| Suure | Laboratorion arvo |
|---|---|
| Suurin sallittu seinämän paksuus | $1{,}6\times10^{-33}$ m ≈ 98 Planckin pituutta |
| Kokonaisnegatiivinen energia | $\approx -4\times10^{79}$ J |
| Massaekvivalentti | $\approx -5\times10^{62}$ kg (noin $10^{32}$ Aurinkoa) |

Tavallinen aine koko havaittavassa maailmankaikkeudessa on luokkaa $10^{53}$ kg. Oikotie on karkeampi kuin Pfenning & Fordin laskelma, joten luota vain sen suuruusluokkaan kun $v_s \sim c$, ei sen riippuvuuteen nopeudesta.

**2. Jopa „kohtuullinen“ seinämä on ulottumattomissa.** Unohda kvanttiepäyhtälö ja salli 1 m paksu seinämä: laboratorio antaa yhteensä noin −400 Jupiterin massaa, huippenergitiheydellä $\approx -10^{42}$ J/m³. Sen saaminen Casimir‑levyistä vaatisi ne noin $4\times10^{-18}$ m:n etäisyydelle, karkeasti 400 kertaa pienemmän kuin protoni. Paras laboratorionegatiivinen energia jää yli 40 kertaluokkaa vajaaksi.

**3. Valoa nopeampi tarkoittaa, että syy ja seuraus voivat vaihtaa paikkaa.** Jos signaali kattaa etäisyyden $\Delta x$ ajassa $\Delta t$ nopeudella $u > c$, nopeudella $V$ liikkuva havaitsija mittaa

$$\Delta t' = \gamma\,\Delta t\left(1 - \frac{uV}{c^2}\right),$$

joka on **negatiivinen** mille tahansa $V > c^2/u$, täysin tavalliselle alivalonopeudelle. Kun $u = 10c$, kuka tahansa joka liikkuu nopeammin kuin $0{,}1c$ näkee matkustajan saapuvan ennen lähtöä. Kaksi tällaista matkaa voidaan yhdistää menopaluuksi, joka palaa ennen kuin se alkoi. Everett (1996) osoitti, että tämä pätee erityisesti warp‑ajoihin. Kun $u \le c$, laboratorio ei löydä havaitsijaa, joka näkisi järjestyksen kääntyvän.

**4. „Yliluminaliset materiiaaallot“ eivät kanna mitään.** Alkuperäinen todiste nojaa siihen, että de Broglie‑aallot ovat „vaiheeltaan tehokkaasti yliluminaalisia“. Se osa on totta: vaiheenopeus on $v_p = c^2/v > c$. Mutta hiukkanen, sen energia ja mikä tahansa viesti kulkevat ryhmänopeudella $v_g = d\omega/dk = v$, ja $v_p v_g = c^2$ täsmälleen. 25 kg:n lapselle joka kävelee 1 m/s laboratorio antaa $v_p \approx 9\times10^{16}$ m/s ja $v_g = 1{,}000$ m/s.

**5. „Sovita määränpään resonanssi ja ilmesty“:llä ei ole fysikaalista perustaa.** Mikään mitattu paikan ominaisuus ei toimi kuin radiotaajuus, johon keho voisi virittyä, eikä mikään tunnettu mekanismi siirrä ainetta siksi, että kaksi asiaa värähtelee samoin. Tämä on tarinan se osa, joka on puhdasta tarinaa. Se on kaunis kuva; se ei vain ole fysiikan tapa toimia. Jokainen tunnettu tapa saada ainetta tai informaatiota täältä sinne joko kestää vähintään valonkulkuajan (raketit, radio, kvanttiteleportaatio klassisine viesteineen) tai, kuten warp‑kupla, on olemassa vain paperilla ja tarvitsee ainetta, jota kukaan ei ole koskaan nähnyt.

**6. Matkustajan jatkuvuus.** Kotitehtävän vastaus („sinua ei faksata, vaan liu'ut“) on filosofinen kanta, ei fysiikkaa. Kvanttiteleportaatio *tuhoaa* alkuperäisen tilan samalla kun se luo sen uudelleen muualla (ei‑kloonauslause kieltää molempien pitämisen), mikä on lähempänä „faksi“‑kuvaa kuin oppitunti myöntää.

## Taso 3 — Mitä pitäisi olla totta

- **Negatiivisen energian lähde, joka kiertää kvanttiepäyhtälöt tai jota ne eivät sido**, tiheyksillä $10^{40}$ J/m³ tai enemmän, ylläpidettynä makroskooppisilla alueilla. Mikä tahansa laboratorionäyttö negatiivisesta energiatiheydestä kauas Casimir‑efektin yli olisi ensimmäinen askel.
- **Keino kausaliteettiongelman ympäri.** Joko suosittu viitekehys, joka rikkoo samanaikaisuuden suhteellisuuden (Lorentz‑invarianttisuuden testit rajoittavat tiukasti), tai periaate, joka kieltää suljetut silmukat (Hawkingin kronologian suojelukonjektuuri ehdottaa, että luonto tekee juuri tämän; sitä ei ole todistettu).
- **Parempi geometria.** Tutkimus on nakertanut lukuja mutta ei ydintongelmaa:
  - Van Den Broeck (1999) löysi kuplan, jolla on pieni ulkopinta ja suuri sisätila, vähentäen kokonaisenergian muutamaan auringonmassaan, mikä on yhä negatiivista energiaa astronomisessa mittakaavassa.
  - Lentz (2021) ehdotti yliluminaalisia „solitoneja“, joiden väitettiin tarvitsevan vain positiivista energiaa; muut kirjoittajat ovat väittäneet, että tämä väite ei pidä.
  - Bobrick & Martire (2021) antoivat yleisen kehikon ja päättelivät, että **yliluminaliset** warp‑ajot tarvitsevat yhä negatiivista energiaa, kun taas aliluminaliset voidaan periaatteessa rakentaa positiivisesta energiasta.
  - Fell & Heisenberg (2021) rakensivat aliluminalisen warp‑ratkaisun, jonka lähteenä on positiivinen energia.
- **Testattavat kohteet**: mikä tahansa laboratorion havainto negatiivisesta energiatiheydestä, joka ylittää kvanttiepäyhtälörajan sen näytteenottoajalle; mikä tahansa signaali, joka saapuu ennen kuin se olisi voitu lähettää valolla, mikä näkyisi myös Lorentz‑invarianttisuuden rikkomuksena tarkkuustesteissä.

## Aja laboratorio

```bash
python Module_08_Instant_Travel/simulation.py
python -m pytest tests/test_module_08.py
```

| Koe | Mitä se näyttää |
|---|---|
| `shape_function`, `york_expansion` | Avaruus kutistuu kuplan edessä ja laajenee takana; litteä sisällä ja kaukana. |
| `energy_density` | $T^{00} \le 0$ kaikkialla: heikko energiaehto rikotaan. |
| `total_energy`, `total_energy_thin_wall` | Kaiken negatiivisen energian numeerinen integraali; skaalautuu kuten $v_s^2 R^2/\Delta$. |
| `qi_bound`, `max_wall_thickness_qi`, `warp_energy_budget` | Kvanttiepäyhtälö pakottaa Planckin ohuet seinämät ja $\sim10^{62}$ kg negatiivista energiaa. |
| `casimir_energy_density`, `casimir_gap_for` | Laboratorionegatiivinen energia on monia kertaluokkia liian pieni. |
| `order_reversal_factor`, `reversing_frame_speed` | Valoa nopeampi + suhteellisuusteoria = seuraukset ennen syitä joillekin havaitsijoille. |
| `de_broglie_velocities` | Vaiheenopeus ylittää $c$:n, ryhmänopeus (todellinen hiukkanen) ei. |

## Kokeile itse

1. Käytä `total_energy`-funktiota selvittääksesi, miten kokonaisenergia muuttuu, kun kaksinkertaistat kuplan säteen $R$ pitäen seinämän paksuuden kiinteänä. Selitä vastaus ohuen seinämän kaavasta.
2. Muuta `sampling_fraction` funktiossa `max_wall_thickness_qi` arvosta 0,1 arvoon 0,5. Kuinka paljon seinämän paksuus ja kokonaisenergia muuttuvat? Miksi johtopäätös säilyy?
3. Käyttäen `order_reversal_factor`-funktiota, löydä hitain havaitsija, joka näkee $1{,}01c$:llä lähetetyn signaalin saapuvan ennen kuin se lähti. Mitä tapahtuu kun $u \to c$?
4. Etsi Casimir‑levyjen etäisyys, joka antaa 1 km:n seinämän energiatiheyden kun $v_s = 0{,}01c$. Onko se suurempi kuin atomi?
5. Laske valonkulkuaika Proxima Centauriin (4,24 valovuotta) ja vertaa sitä aikaan, jonka $0{,}1c$:n luotain veisi.

## Viitteet

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
