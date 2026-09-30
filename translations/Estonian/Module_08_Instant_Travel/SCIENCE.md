# 🔬 8. moodul — Teadus loo taga

> [Õppetund](readme.md) on jutustatud aastast 2420. See lehekülg on 2025. aasta reaalsuskontroll: mis on kindlakstehtud, kus loo väide murdub ja mis peaks olema tõsi, et see töötaks. Kõike siin saab kontrollida [laborikoodiga](../../../Module_08_Instant_Travel/simulation.py).

## 2420. aasta väide ühes lauses

Vahemaa on illusioon: kui häälestad oma keha sihtkoha „sagedusele“, kaod siit ja ilmud sinna nullajaga, ilma kiiruspiiranguta, sest jätsid ruumi vahele selle asemel et seda ületada.

## Tase 1 — Mis on päris

**Üldrelatiivsusteooria lubab „liigutada ruumi sinu asemel“ — paberil.** Miguel Alcubierre (1994) kirjutas üles aegruumi, milles lameda ruumi mull viiakse edasi mis tahes kiirusel $v_s$, isegi valgusest kiiremini. Ühikutes, kus $G = c = 1$:

$$ds^2 = -dt^2 + \big(dx - v_s f(r_s)\,dt\big)^2 + dy^2 + dz^2,$$

$$f(r) = \frac{\tanh\!\big(\sigma(r+R)\big) - \tanh\!\big(\sigma(r-R)\big)}{2\tanh(\sigma R)},$$

kus $r_s$ on kaugus mulli keskmest $x_s(t)$, $R$ on mulli raadius ja $1/\sigma$ seab seina paksuse. $f = 1$ sees (reisija hõljub vabalangemises, tundmata kiirendust) ja $f \to 0$ kaugel.

- **Ruum kahaneb ees ja kasvab taga.** Vaatlejate mahuelementide paisumine lõikes (Yorki paisumine) on

$$\theta = v_s\,\frac{x - x_s}{r_s}\,\frac{df}{dr_s},$$

mis on negatiivne mulli ees, positiivne selle taga ning null sees ja kaugel. Labor kinnitab kõik neli omadust numbriliselt.

- **Hind on negatiivne energia.** Einsteini võrrandid ütlevad, millist ainet oleks vaja selle geomeetria tegemiseks. Lõikes paigal olevate vaatlejate jaoks on energiatihedus

$$T^{00} = -\frac{1}{8\pi}\,\frac{v_s^2\,(y^2+z^2)}{4\,r_s^2}\left(\frac{df}{dr_s}\right)^2 \;\le\; 0 .$$

See on **negatiivne kõikjal, kus see ei ole null**: nõrga energiatingimuse rikkumine. Integreerides üle kogu ruumi (labor teeb seda numbriliselt ja kontrollib jõhkra 3‑D summa vastu) annab peene seina jaoks

$$E \;\approx\; -\frac{v_s^2 R^2 \sigma}{36} \qquad (G=c=1),$$

nii et energiaarve kasvab kiiruse ruuduga, mulli suuruse ruuduga ja pöördvõrdeliselt seina paksusega.

- **Negatiivne energiatihedus eksisteerib — natuke.** Kahe paralleelse peegli vahel kaugusel $d$ on kvantvaakumi energiatihedus $u = -\pi^2\hbar c/(720\,d^4)$ (Casimir, 1948). Sellest tulenevat jõudu on mõõdetud (nt Lamoreaux, 1997). Juures $d = 100$ nm, $u \approx -4$ J/m³.

- **„Teleportatsioon“ on füüsikas päris sõna — info jaoks, mitte kehade jaoks.** Kvantteleportatsioon (Bennett jt, 1993; esmalt näitasid Bouwmeester jt, 1997) kannab osakese kvant*oleku* teisele osakesele, mis on juba sihtkohas. See vajab tavalist klassikalist sõnumit, saadetud valguse kiirusel või allpool, et töö lõpetada. Miski ei reisi valgusest kiiremini ja ainet ei liigutata.

- **Kaks kella.** Sümpaatiline resonants on päris, aga teine kell heliseb, sest helilained kannavad energiat üle toa umbes 343 m/s. See on aeglane, tavaline ülekanne läbi õhu, mitte hüpe.

## Tase 2 — Kus väide murdub

**1. Kvant‑ebavõrdsused muljuvad seina.** Kvantväljateooria lubab negatiivset energiat, aga ainult natuke ja ainult lühidalt. Massitu skalaarvälja jaoks lamedas aegruumis leiab vaatleja, kes keskmistab energiatihedust Lorentzi kaaluga laiusega $t_0$, alati (Ford & Roman)

$$\langle\rho\rangle \;\ge\; -\frac{3\hbar}{32\pi^2 c^3\,t_0^4}.$$

Mida lühem aeg, seda negatiivsemat energiat lubatakse, aga piir pinguldub kui $t_0^{-4}$. Pfenning & Ford (1997) rakendasid seda Alcubierre’i mullile diskreetimisaegadega, mis on lühikesed võrreldes seina kõverusskaalaga, ja leidsid, et sein saab olla kõige rohkem suurusjärgus sada Plancki pikkust paks $v_s \sim c$ korral ning et kogu negatiivne energia ületab siis kaugele nähtava Universumi massi.

Labor taastoodab *suurusjärgu* lihtsama otseteega: see nõuab, et kõige negatiivsem $T^{00}$ seinal austaks piiri koos $t_0 = 0{,}1\,\Delta/c$ ($\Delta$ = seina paksus). 100 m mulli jaoks $v_s = c$ juures:

| Suurus | Laboriväärtus |
|---|---|
| Suurim lubatud seina paksus | $1{,}6\times10^{-33}$ m ≈ 98 Plancki pikkust |
| Kogu negatiivne energia | $\approx -4\times10^{79}$ J |
| Massiekvivalent | $\approx -5\times10^{62}$ kg (umbes $10^{32}$ Päikest) |

Tavaline aine kogu vaadeldavas Universumis on suurusjärgus $10^{53}$ kg. Otsetee on jämedam kui Pfenning & Fordi arvutus, seega usalda ainult selle suurusjärku $v_s \sim c$ juures, mitte selle sõltuvust kiirusest.

**2. Isegi „mõistlik“ sein on käeulatusest väljas.** Unusta kvant‑ebavõrdsus ja luba 1 m paks sein: labor annab kokku umbes −400 Jupiteri massi, tippenergiatihedusega $\approx -10^{42}$ J/m³. Selle saamine Casimiri plaatidelt vajaks neid umbes $4\times10^{-18}$ m vahega, umbes 400 korda väiksem kui prooton. Parim laboratoorne negatiivne energia jääb lühikeseks rohkem kui 40 suurusjärgu võrra.

**3. Valgusest kiirem tähendab, et põhjus ja tagajärg võivad vahetuda.** Kui signaal katab kauguse $\Delta x$ ajaga $\Delta t$ kiirusel $u > c$, mõõdab vaatleja, kes liigub kiirusel $V$,

$$\Delta t' = \gamma\,\Delta t\left(1 - \frac{uV}{c^2}\right),$$

mis on **negatiivne** mis tahes $V > c^2/u$ korral, täiesti tavaline alavalguskiirus. $u = 10c$ korral näeb igaüks, kes liigub kiiremini kui $0{,}1c$, reisijat saabumas enne lahkumist. Kaks sellist reisi saab kombineerida ringreisiks, mis naaseb enne algust. Everett (1996) näitas, et see kehtib just warp‑ajamitele. $u \le c$ korral ei leia labor ühtegi vaatlejat, kes näeks järjekorra pöördumist.

**4. „Ülivalguselised ainelained“ ei kanna midagi.** Algne tõestus toetub sellele, et de Broglie lained on „faasis efektiivselt ülivalguselised“. See osa on tõsi: faasikiirus on $v_p = c^2/v > c$. Aga osake, selle energia ja mis tahes sõnum liiguvad grupikiirusel $v_g = d\omega/dk = v$, ja $v_p v_g = c^2$ täpselt. 25 kg lapse jaoks, kes kõnnib 1 m/s, annab labor $v_p \approx 9\times10^{16}$ m/s ja $v_g = 1{,}000$ m/s.

**5. „Sobita sihtkoha resonants ja ilmu“ ei oma füüsikalist alust.** Ükski mõõdetud koha omadus ei tööta nagu raadiosagedus, millele keha saaks häälestuda, ja ükski teadaolev mehhanism ei liiguta ainet, sest kaks asja võnguvad sarnaselt. See on loo osa, mis on puhas lugu. See on armas pilt; see lihtsalt ei ole see, kuidas füüsika töötab. Iga teadaolev viis aine või info saamiseks siit sinna kas võtab vähemalt valguse reisiaja (raketid, raadio, kvantteleportatsioon klassikalise sõnumiga) või, nagu warp‑mull, eksisteerib ainult paberil ja vajab ainet, mida keegi pole kunagi näinud.

**6. Reisija pidevus.** Koduülesande vastus („sind ei faksita, sa libised“) on filosoofiline seisukoht, mitte füüsika. Kvantteleportatsioon *hävitab* algse oleku, kui see seda mujal taastab (no‑cloning teoreem keelab mõlema hoidmise), mis on lähemal „faksi“ pildile kui õppetund tunnistab.

## Tase 3 — Mis peaks olema tõsi

- **Negatiivse energia allikas, mis väldib kvant‑ebavõrdsusi või ei ole nendega seotud**, tihedustel $10^{40}$ J/m³ või rohkem, ülalhoitud makroskoopilistes piirkondades. Mis tahes laboritõend negatiivsest energiatihedusest kaugele üle Casimiri efekti oleks esimene samm.
- **Tee ümber põhjuslikkuse probleemi.** Kas eelistatud taustsüsteem, mis murdub samaaegsuse relatiivsuse (tugevalt piiratud Lorentzi invariantsuse testidega), või printsiip, mis keelab suletud silmuseid (Hawkingi kronoloogiakaitse hüpotees pakub, et loodus teeb just seda; see on tõestamata).
- **Parem geomeetria.** Uuringud on numbreid nühkinud, aga mitte tuumprobleemi:
  - Van Den Broeck (1999) leidis mulli tillukese välispinna ja suure sisemusega, vähendades koguenergiat mõne päikesemassini, mis on endiselt negatiivne energia astronoomilisel skaalal.
  - Lentz (2021) pakkus ülivalguselisi „solitone“, millel väidetavalt on vaja ainult positiivset energiat; teised autorid on väitnud, et see väide ei pea.
  - Bobrick & Martire (2021) andsid üldraamistiku ja järeldasid, et **ülivalguselised** warp‑ajamid vajavad endiselt negatiivset energiat, samas kui alavalguselisi saab põhimõtteliselt ehitada positiivsest energiast.
  - Fell & Heisenberg (2021) konstrueerisid alavalguselise warp‑lahendi, mille allikaks on positiivne energia.
- **Testitavad sihtmärgid**: mis tahes laborivaatlus negatiivsest energiatihedusest, mis ületab kvant‑ebavõrdsuse piiri oma diskreetimisaja jaoks; mis tahes signaal, mis saabub enne, kui valgus oleks saanud selle saata, mis ilmneks ka Lorentzi invariantsuse rikkumisena täppistestides.

## Käivita labor

```bash
python Module_08_Instant_Travel/simulation.py
python -m pytest tests/test_module_08.py
```

| Katse | Mida see näitab |
|---|---|
| `shape_function`, `york_expansion` | Ruum tõmbub mulli ees kokku ja paisub taga; lame sees ja kaugel. |
| `energy_density` | $T^{00} \le 0$ kõikjal: nõrk energiatingimus on rikutud. |
| `total_energy`, `total_energy_thin_wall` | Kogu negatiivse energia numbriline integraal; skaleerub kui $v_s^2 R^2/\Delta$. |
| `qi_bound`, `max_wall_thickness_qi`, `warp_energy_budget` | Kvant‑ebavõrdsus sunnib Planck‑peeneid seinu ja $\sim10^{62}$ kg negatiivset energiat. |
| `casimir_energy_density`, `casimir_gap_for` | Laboratoorne negatiivne energia on paljude suurusjärkude võrra liiga väike. |
| `order_reversal_factor`, `reversing_frame_speed` | Valgusest kiirem + relatiivsus = tagajärjed enne põhjuseid mõnele vaatlejale. |
| `de_broglie_velocities` | Faasikiirus ületab $c$, grupikiirus (tegelik osake) mitte. |

## Proovi ise

1. Kasuta `total_energy`, et leida, kuidas koguenergia muutub, kui kahekordistad mulli raadiuse $R$, hoides seina paksuse fikseerituna. Selgita vastust peene seina valemist.
2. Muuda `sampling_fraction` funktsioonis `max_wall_thickness_qi` 0,1‑st 0,5‑ks. Kui palju muutuvad seina paksus ja koguenergia? Miks järeldus ellu jääb?
3. Kasutades `order_reversal_factor`, leia aeglasem vaatleja, kes näeb signaali saadetud $1{,}01c$ juures saabumas enne lahkumist. Mis juhtub kui $u \to c$?
4. Leia Casimiri plaadivähe, mis annab 1 km seina energiatiheduse $v_s = 0{,}01c$ juures. Kas see on suurem kui aatom?
5. Arvuta valguse reisiaeg Proxima Centaurini (4,24 valgusaastat) ja võrdle seda ajaga, mida võtaks 0,1c sond.

## Viited

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
