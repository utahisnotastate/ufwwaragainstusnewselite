# 🔬 5. moodul — Teadus loo taga

> [Õppetund](readme.md) on jutustatud aastast 2420. See lehekülg on 2025. aasta reaalsuskontroll: mis on kindlakstehtud, kus loo väide murdub ja mis peaks olema tõsi, et see töötaks. Kõike siin saab kontrollida [laborikoodiga](../../../Module_05_Time_Is_A_Map/simulation.py).

## 2420. aasta väide ühes lauses

Minevik, olevik ja tulevik kõik eksisteerivad koos nagu kohad kaardil, reaalsus „vilgub“ kaadrist kaadrisse ja ajarännak on lihtsalt faasi nihutamine kaardi teise ossa.

## Tase 1 — Mis on päris

**Aeg on tõepoolest osa neljamõõtmelisest geomeetriast.** Erirelatiivsusteoorias on suurus, milles iga vaatleja nõustub, mitte aeg kahe sündmuse vahel ega kaugus nende vahel, vaid **Minkowski intervall**

$$s^2 = -c^2\,\Delta t^2 + \Delta x^2 + \Delta y^2 + \Delta z^2 .$$

Negatiivne $s^2$ (ajalik) tähendab, et üks sündmus saab teist põhjustada; positiivne $s^2$ (ruumiline) tähendab, et kumbki ei saa. Labor kontrollib, et Lorentzi teisendus $t' = \gamma\,(t - vx/c^2)$, $x' = \gamma\,(x - vt)$ jätab $s^2$ muutumatuks.

**„Praegu“ sõltub sellest, kes küsib.** Kaks sündmust samal ajal $t$, aga kaugusel $L$, on vaatleja jaoks, kes liigub kiirusel $v$, ajas eraldatud

$$\Delta t' = -\gamma\,\frac{vL}{c^2}.$$

Andromeeda galaktika jaoks ($L \approx 2{,}5$ miljonit valgusaastat) nihutab lihtsalt 1,4 m/s kõndimine seda, millised Andromeeda sündmused loevad „praeguks“, umbes **4 päeva** võrra (labor arvutab selle; näide on Penrose’i „Andromeeda paradoks“). See samaaegsuse relatiivsus on põhjus, miks paljud füüsikafilosoofid kaitsevad **eternalismi**, „plokk‑universumi“ vaadet, milles kõik sündmused on võrdselt reaalsed (Rietdijk 1966, Putnam 1967). See on õigustatud relatiivsusteooria tõlgendus. See ei ole ainus ja ükski katse ei saa seda rivaalidest eristada, sest nad kõik teevad samu ennustusi.

**Kellad tiksuvad tõepoolest erineva kiirusega ja me korrigeerime seda iga päev.** Kella kiirus koordinaataja suhtes on nõrga välja piiris

$$\frac{d\tau}{dt} \approx 1 + \frac{\Phi}{c^2} - \frac{v^2}{2c^2}, \qquad \Phi = -\frac{GM}{r}.$$

GPS‑satelliidi jaoks ($a \approx 26\,562$ km, $v \approx 3{,}87$ km/s) võrreldes kellaga ekvaatoril arvutab labor esimestest printsiipidest:

| Efekt | µs päevas |
|---|---|
| Nõrgem gravitatsioon kõrgusel (jookseb kiiresti) | +45.7 |
| Orbiidi kiirus (jookseb aeglaselt) | −7.2 |
| Maakella enda pöörlemine | +0.1 |
| **Neto** | **+38.5** |

Avaldatud arvud tsiteeritakse tavaliselt +45,9, −7,2 ja +38,6 µs/päev; väikesed erinevused tulevad sellest, kuidas Maa kuju ja pöörlemist modelleeritakse (labori ristkontroll IAU geoidi konstandiga $L_G$ annab +38,58). Korrigeerimata oleks see kaugusviga umbes 11 km päevas. Relativistlikke kellanihkeid mõõdeti ka otse, lennutades aatomkelli ümber maailma (Hafele & Keating 1972).

**Pöörlevad mustad augud lohistavad aegruumi.** Kerri meetrika (Kerr 1963) Boyer–Lindquisti koordinaatides, koos $G = c = M = 1$, omab

$$\Sigma = r^2 + a^2\cos^2\theta,\quad \Delta = r^2 - 2r + a^2,$$
$$g_{tt} = -\Big(1-\frac{2r}{\Sigma}\Big),\quad g_{t\phi} = -\frac{2ar\sin^2\theta}{\Sigma},\quad g_{\phi\phi} = \Big(r^2 + a^2 + \frac{2a^2 r\sin^2\theta}{\Sigma}\Big)\sin^2\theta .$$

- Horisondid $r_\pm = 1 \pm \sqrt{1-a^2}$, mis eksisteerivad ainult $a \le 1$ korral.
- **Ergosfäär** asub $r_+$ ja $r_\text{ergo} = 1 + \sqrt{1 - a^2\cos^2\theta}$ vahel, kus $g_{tt} = 0$. Selle sees muutub „paigal seista“ suund $\partial_t$ ruumiliseks: **ükski vaatleja ei saa paigal jääda**, kõike lohistatakse auguga kaasa. Labor kontrollib $g_{tt}=0$ sellel pinnal ja $g_{tt}$ märki mõlemal pool seda.
- **Penrose’i protsess** (Penrose 1969): osake jaguneb ergosfääri sees, üks tükk kukub sisse negatiivse energiaga ja teine põgeneb suurema energiaga kui algne. Labor lahendab energia ja impulsimomendi säilivuse selle jagunemise jaoks ja taastab õpiku maksimumi $\eta = \tfrac12\big(\sqrt{2/r_+}-1\big)$, mis on **20,7 %** $a = 1$ korral.
- Kogu energia, mida kunagi saab ammutada, on seatud **taandumatust massist** (Christodoulou 1970), $M_\text{irr} = \tfrac12\sqrt{r_+^2 + a^2}$: kõige rohkem $1 - M_\text{irr}/M = $ **29,3 %** ekstremaalse augu jaoks.

## Tase 2 — Kus väide murdub

**1. Erimeelsus „praegu“ suhtes ei ole sama kui minevikku jõudmine.** Labor tõstab kaks sündmusepaari läbi 199 kiiruse kuni $0{,}99c$. Ruumiline paar vahetab järjekorda 50 neist. Ajaline paar, selline, mis saab olla põhjus ja tagajärg, **ei tee seda kunagi**. Relatiivsusteooria laseb vaatlejatel erineda sündmuste järjekorras, mis teineteist ei mõjuta. See ei lase kunagi kellelgi näha tagajärge enne selle põhjust.

**2. „Aeg on vilkumine“ ja „ajarännak on faasinihe“ ei oma füüsikat taga.** Ükski teooria ei ennusta reaalsuse positiivset/negatiivset „tiksu“, idee ei tee ühtegi mõõdetavat arvu ja ümber maailma võrreldud kellad näitavad sujuvaid, ennustatavaid kiirusi, nagu ülaltoodud GPS‑numbrid näitavad. Nagu kirjutatud, ei saa väidet testida.

**3. Õppetund segab kahte erinevat ideed.** Plokk‑universum (üks fikseeritud neljamõõtmeline ajalugu) ja „paljud maailmad“ (Everett 1957; hargnevad kvantajalood) on eraldi tõlgendused. Kumbki ei sisalda valikut, millist „rulli“ mängida. „Teadvuse valgus, mis liigub mööda ussi miljardeid kordi sekundis“ on metafoor, mitte füüsikaline mehhanism.

**4. Kus üldrelatiivsusteooria *lubab* ajasilmuseid, on need kaugel käeulatusest.** Suletud ajaline kõver (CTC) on rada läbi aegruumi, mis naaseb omaenda minevikku. Täpsed lahendid CTC‑dega eksisteerivad: Gödeli pöörlev universum (1949), van Stockumi ja Tipleri lõpmatult pikad pöörlevad silindrid (Tipler 1974) ja Kerri lahendi sisemus (Carter 1968). Kerris on aasa ümber telje ajaline kõikjal, kus $g_{\phi\phi} < 0$. Labor skaneerib $r$ iga spinni jaoks ja leiab **$g_{\phi\phi} < 0$ ainult $r < 0$ korral**, piirkonnas, kuhu jõutakse ainult läbi rõngassingulaarsuse; $a = 1$ ekvaatoril on selle serv täpselt $r = -1$. Selle õppetunni varasem mustand tegi kaks viga, mille vastu labor nüüd testib:

- see kasutas $a = 1{,}2$, millel **puudub üldse horisont** (paljas singulaarsus, mida looduses ei oodata tekkivat), ja
- see käsitles $\partial_t$ ruumiliseks muutumist ergosfääri sees kui ajamasinat. Ergosfääri sees on $g_{\phi\phi}$ endiselt positiivne: see on **raami lohistamine, mitte CTC**.

**5. Füüsika näib minevikku kaitsvat.** Hawkingi **kronoloogiakaitse hüpotees** (1992) pakub, et kvantefektid peatavad CTC‑de tekkimise igas piirkonnas, kuhu me võiksime jõuda. See on hüpotees, mitte teoreem, aga **puuduvad tõendid, et CTC‑d on meie Universumis füüsikaliselt realiseeritavad**.

## Tase 3 — Mis peaks olema tõsi

Selleks et „ajarännak faasinihkega“ saaks teaduseks, peaks see täitma kõik need:

- **Aegruum ligipääsetava CTC‑piirkonnaga.** Iga teadaolev viis ühe ehitamiseks (läbitavad ussiaugud, warp‑mullid) nõuab „eksootilist“ ainet negatiivse energiatihedusega, rikkudes klassikalisi energiatingimusi (Morris, Thorne & Yurtsever 1988). Kas kvantefektid lubavad sellest piisavalt, on avatud küsimus.
- **Tee ümber kronoloogiakaitse.** Arvutus täielikus kvantgravitatsiooni teoorias peaks näitama, et vaakum ei plahvata ajamasina serval („kronoloogiahorisont“).
- **Mõõdetav ennustus „vilkumisele“.** Näiteks ennustatud müralagi, diskreetsus või sagedus aatomkellade võrdlustes, mis ei nõustu standardfüüsikaga. Kui lugu annaks sageduse, võiksid kellad seda otsida.
- **Kooskõla põhjuslikkusega.** Teooria peab käsitlema vanaisaparadoksi, näiteks läbi isejärjekindlate ajalugude (Novikovi printsiip), ja tegema selle kohta testitavaid ennustusi.

Lugu osa, mis ellu jääb, on päris ja märkimisväärne: aeg on suund neljamõõtmelises geomeetrias, „praegu“ ei ole universaalne, kellad erinevatel kõrgustel ja kiirustel erinevad täpsete, ennustatavate summade võrra ning pöörlevad mustad augud salvestavad energiat, mida saab põhimõtteliselt ammutada.

## Käivita labor

```bash
python Module_05_Time_Is_A_Map/simulation.py
python -m pytest tests/test_module_05.py
```

| Katse | Mida see näitab |
|---|---|
| `lorentz_boost`, `interval`, `simultaneity_shift` | $s^2$ on invariantne; „praegu“ nihkub kiirusega; ajaline järjekord ei pöördu kunagi. |
| `gps_clock_rates` | +45,7 / −7,2 / +38,5 µs päevas, arvutatud $GM$‑st, $c$‑st ja orbiidist. |
| `kerr_metric`, `horizons`, `ergosurface`, `static_observer_norm` | Horisondid, ergosfäär ja miks miski ei saa selle sees paigal seista. |
| `penrose_gain`, `penrose_max_efficiency_*`, `irreducible_mass` | 20,7 % jagunemise kohta ja 29,3 % kokku $a = 1$ korral. |
| `ctc_scan` | Kerri suletud ajalised kõverad eksisteerivad ainult $r < 0$ juures. |

## Proovi ise

1. Kasuta `simultaneity_shift`, et leida, kui kiiresti peaksid liikuma, et Andromeeda „praegu“ nihkuks ühe aasta võrra. Milline murdosa $c$‑st see on?
2. Muuda `A_GPS` funktsioonis `gps_clock_rates`, et leida orbiidi raadius, kus gravitatsioonilised ja kiirusefektid täpselt tühistuvad (neto nihe on null). Võrdle seda $\tfrac32 R_\text{Earth}$‑iga.
3. Joonista `penrose_gain(0.9, r)` $r$ jaoks $r_+$ ja 2 vahel. Kus langeb võit nulli ja miks see sobib ergosfääriga?
4. Käivita `ctc_scan(a, theta=0.3)` mõne spinni jaoks. Kas ekvaatorilt eemale liikumine toob kunagi CTC‑piirkonna $r > 0$ juurde?
5. Proovi `horizons(1.2)`. Selgita ühes lauses, miks varasema mustandi $a = 1{,}2$ must auk ei olnud must auk.

## Viited

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
- Penrose, R., *The Emperor's New Mind*, Oxford University Press (1989). The Andromeeda example.
- Everett, H., "'Relative state' formulation of quantum mechanics", *Rev. Mod. Phys.* **29**, 454 (1957).
