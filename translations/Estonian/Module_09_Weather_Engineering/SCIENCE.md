# 🔬 9. moodul — Teadus loo taga

> [Õppetund](readme.md) on jutustatud aastast 2420. See lehekülg on 2025. aasta reaalsuskontroll: mis on kindlakstehtud, kus loo väide murdub ja mis peaks olema tõsi, et see töötaks. Kõike siin saab kontrollida [laborikoodiga](../../../Module_09_Weather_Engineering/simulation.py).

## 2420. aasta väide ühes lauses

Kaks nähtamatut „skalaar“‑ (pikilaine) kiirt, mis lähevad kahjutult läbi Maa, saab ristata kõikjal taevas, et luua hetkelisi kuumi või külmi taskuid, ja nende taskute võrk juhib torme ja joavoolu elektriliselt.

## Tase 1 — Mis on päris

**Atmosfäär on tõepoolest elektriline vooluring.** Ionosfäär istub umbes $+250$ kV suhtes maapinnaga. Selge ilmaga juhib see tillukese allapoole suunatud voolu, umbes $2$ pA/m², läbi nõrgalt juhtiva õhu, pinnaväljaga umbes $100$–$130$ V/m. Äikesetormid ümber maailma toimivad patareina, mis hoiab seda laetuna. Labor muudab need tüüpilised väärtused kogusummadeks:

| Suurus | Kuidas arvutatakse | Laboriväärtus |
|---|---|---|
| Kogu vool | $J \times 4\pi R_\oplus^2$ | ≈ 1 kA |
| Võimsus | $V_\text{ion} \times I$ | ≈ 250 MW |
| Maa pinnalaeng | $\varepsilon_0 E \times 4\pi R_\oplus^2$ (Gauss) | ≈ $5\times10^5$ C |
| Õhu juhtivus maapinnal | $J/E$ | ≈ $2\times10^{-14}$ S/m |
| Tühjenemisaeg ilma tormideta | $\varepsilon_0/\sigma$ | ≈ 9 minutit |

**Elekter saab õhku lükata.** Tugevas väljas kiirendatud ioonid lohistavad neutraalseid molekule kaasa: see on „ioonituul“ ehk elektrohüdrodünaamiline tõuge. Voolu $I$ jaoks, mis ületab vahe $d$ iooniliikuvusega $\mu$, on ühemõõtmeline tõuge $T = I d/\mu$, nii et tõuge vati kohta on $T/P = d/(\mu V)$. MIT lennutas 5 m tiivaulatusega lennukit ilma liikuvate osadeta sellel põhimõttel (Xu jt, 2018).

**Pilved moodustuvad osakestel ja teooria ütleb täpselt millal.** Vesi ei kondenseeru iseenesest õhus leiduvatel niiskustel. See kondenseerub tillukestel osakestel (pilvekondensatsioonituumad), näiteks meresoolal. Köhleri teooria (1936) annab tasakaalu küllastussuhte lahustilga raadiusega $r$, mis sisaldab soolamassi $m_s$:

$$S(r) = a_w \exp\!\left(\frac{A}{r}\right) \;\approx\; 1 + \frac{A}{r} - \frac{B}{r^3}, \qquad A = \frac{2\sigma M_w}{R T \rho_w},\quad B = \frac{3\, i\, m_s M_w}{4\pi \rho_w M_s}.$$

Kõveruse (Kelvini) liige $A/r$ paneb väikesed tilgad aurustuma; lahustunud sool (Raoulti) liige $B/r^3$ alandab aururõhku. Kõveral on tipp

$$r_c = \sqrt{3B/A}, \qquad S_c - 1 = \sqrt{\frac{4A^3}{27B}} \;\propto\; m_s^{-1/2}.$$

Labor leiab täieliku avaldise tipu numbriliselt ja kinnitab $S_c - 1 \propto m_s^{-1/2}$ ning $r_c \propto m_s^{1/2}$. NaCl jaoks ($i \approx 2$) annab see:

| Kuiv diameeter | Kriitiline üleküllastus | Ristkontroll: κ‑Köhler mõõdetud κ = 1,28 |
|---|---|---|
| 20 nm | 1.14 % | 1.16 % |
| 50 nm | 0.29 % | 0.29 % |
| 100 nm | 0.10 % | 0.10 % |
| 200 nm | 0.036 % | 0.037 % |

Allpool tippu on tilk stabiilne **udu**‑osake. Udu eksisteerib hästi allpool 100 % niiskust: soolakristall lahustub (delikvestseerub) umbes 75 % RH juures ja labor arvutab 75,5 % lahuse veeaktiivsusest. Ainult kui õhu üleküllastus ületab $S_c$, kasvab tilk piiramatult ja muutub pilvetilgaks („aktiveerumine“). Päris pilved ületavad harva umbes 1 % üleküllastust, mistõttu otsustab tilkade tekkekoha osakeste populatsioon, mitte pinge.

**Ioonid aitavad tõepoolest uusi osakesi teha.** Laeng stabiliseerib väikseid molekulaarseid klastreid. CERN CLOUD eksperiment (Kirkby jt, 2011) näitas, et kosmiliste kiirte ionisatsioon suurendab mõõdetavalt väävelhape–ammoniaak osakeste tekkekiirust. Need osakesed on nanomeetrite ulatuses ja peavad tundide kuni päevade jooksul kasvama, enne kui nad on piisavalt suured pilvede külvamiseks.

**Pilvekülvamine on päris, aga tagasihoidlik.** Sobivate talvepilvede hõbejodiidiga külvamist mägede kohal on otse vaadeldud ekstra lumesaju tootmisena (French jt, 2018). Tervete hooaegade ja piirkondade peale on efekt väike ja statistiliselt raske tõestada.

**HAARP on päris.** See on ionosfääriuuringute rajatis Alaskas, mille kõrgsagedus‑saatjal on 3,6 MW võimsust. See kuumutab väikseid ionosfääri laike, kaugel ilmast (ilm elab madalaimas ~15 km). Ilmale ei ole näidatud mõju.

**Fokusseerimine on päris.** Suurendusklaas teeb kuuma täpi, sest kogub valguse suurelt alalt väikesesse. Kaks ristatud kiirt teevad ka heledaid ja tumedaid ribasid, kus nad interferentsivad.

## Tase 2 — Kus väide murdub

**1. Tühjas ruumis ei ole longitudinaalseid raadiolaineid.** Vaakumis ütleb Gaussi seadus $\nabla\cdot\mathbf E = 0$. Laine $\mathbf E_0 e^{i\mathbf k\cdot\mathbf x}$ jaoks tähendab see $\mathbf k\cdot\mathbf E_0 = 0$: väli peab olema risti liikumissuunaga. Potentsiaalide „skalaar“‑ ja longitudinaalsed osad saab muuta kalibreerimisteisendusega ilma ühtegi mõõdetavat välja muutmata ja need ei kanna energiat. Whittaker (1903) näitas, et välju saab *kirjutada* kahe skalaarfunktsiooni kaudu. See on tavalise elektromagnetismi matemaatiline ümberkirjutus, mitte uut tüüpi laine. Longitudinaalsed elektrilained eksisteerivad plasma sees (Langmuiri lained), aga nad vajavad plasma olemasolu ega ületa kivi ega ookeani.

**2. Raadiolained ei lähe läbi Maa.** Juhid neelavad elektromagnetlaineid naha sügavuse $\delta \approx \sqrt{2/(\omega\mu_0\sigma)}$ piires. Labor kasutab täpset valemit:

| Sagedus | Merevesi ($\sigma$ = 4 S/m) | Kivi ($\sigma$ = 10⁻³ S/m) |
|---|---|---|
| 10 Hz | 80 m | 5 km |
| 1 kHz | 8 m | 500 m |
| 1 MHz | 0.25 m | 21 m |

Pärast 1000 km kivi säilitab isegi 10 Hz laine murdosa $e^{-199} \approx 10^{-87}$ oma amplituudist. Seetõttu võetakse allveelaevadega ühendust äärmiselt madalate sageduste ja hiiglaslike antennidega ning isegi siis ainult pinna lähedal.

**3. Ristatud kiired liigutavad energiat; nad ei saa seda luua ega eemaldada.** Kus kaks koherentset kiirt intensiivsusega $I_1$ ja $I_2$ kattuvad, on aja‑keskmistatud intensiivsus

$$I = I_1 + I_2 + 2\sqrt{I_1 I_2}\cos\Delta\phi .$$

Tumedad ribad on alati paaris heledatega ja keskmine üle mustri on täpselt $I_1 + I_2$. Labor kontrollib mõlemat. „Külm režiim“, milles ristumispunkt imeb õhust soojust, vajaks negatiivset intensiivsust. Õhu jahutamine tähendab selle soojuse pumpamist kuhugi mujale, mis võtab tööd ja peab lähedusse dumpama veelgi rohkem soojust (termodünaamika teine seadus). Suurendusklaas ei saa ka külma täppi teha.

**4. Ilm on tohutult võimsam kui ükski elektriline hoob.** Ilma juhib päikesevalgus ($\approx 1{,}2\times10^{17}$ W, mida Maa neelab) ja latentsoojus, mis vabaneb, kui veeaur kondenseerub:

| Energiaallikas või ‑neelaja | Laboriväärtus |
|---|---|
| Üks äikesetorm (2 cm vihma 5 km raadiuse üle) | ≈ $4\times10^{15}$ J |
| Keskmine orkaan (1,5 cm/päev vihma 665 km raadiuse üle, NOAA meetod) | ≈ $6\times10^{14}$ W |
| Õhu soojendamine 100 km × 100 km üle vaid 1 K | ≈ $10^{17}$ J |
| Kogu globaalne elektriline vooluring | ≈ $2{,}5\times10^{8}$ W |
| HAARP saatja | $3{,}6\times10^{6}$ W |
| Suur maapealne ioonmassiiv (100 kV × 1 mA) | 100 W |

100 W juures võtaks 1 K soojendamine umbes 30 miljonit aastat. Isegi kui kogu HAARP‑i võimsus neelduks madalamas atmosfääris (see ei neeldu), võtaks see umbes 900 aastat. Orkaan ületab ioonmassiivi võimsust teguriga umbes $6\times10^{12}$. Selle massiivi ioonituul on tõuge umbes 0,25 N, 25 g objekti kaal, rakendatud ilmasüsteemidele, mis sisaldavad miljardeid tonne liikuvat õhku.

**5. Ioonid ei saa pilvi otse teha.** Thomsoni teooria tilga tekkest laengul lisab elektrostaatilise liikme puhta veetilga klassikalisele vabaenergiale:

$$\Delta G(r) = -\tfrac43\pi r^3 n_l k T\ln S \;+\; 4\pi r^2\sigma \;+\; \frac{q^2}{8\pi\varepsilon_0}\left(1-\frac{1}{\varepsilon_r}\right)\left(\frac1r - \frac1{r_0}\right).$$

$S \le 1$ korral on mahuliige positiivne, nii et $\Delta G$‑l puudub maksimum ja kriitilist raadiust ei ole: tilgad ei kasva kunagi, laetud või mitte. $S > 1$ korral alandab laeng barjääri, aga labor leiab, et barjäär langeb ~60 kT‑ni (umbes üks tilk cm³ kohta sekundis) alles $S \approx 4{,}1$ juures neutraalsete klastrite jaoks ja $S \approx 2{,}5$ ühe elementaarlaenguga. C. T. R. Wilsoni pilvekambrid 1890. aastatel leidsid sama tüüpi numbri: ioonid käivitavad tilgad ainult mõnesaja protsendi üleküllastustel. Realistliku $S = 1{,}01$ juures on barjäär üle $10^6$ kT. Päris õhus aktiveeruvad sool ja teised osakesed alla 1 % üleküllastusel, ammu enne kui ioonid loevad. (Kontiinumteooria on jäme ainult mõne molekuli suuruste klastrite jaoks; järjestus, mitte täpsed numbrid, on robustne.)

**6. Maapealsed ionisaatorid vihma jaoks.** Mitmed kommertsprojektid on väitnud vihma suurendamist maapealsete ionisaatorite massiividest. Seni avaldatud tõendid on nõrgad ja vaidlustatud: väikesed väidetud efektid, puuduvad sõltumatud juhuslikustatud katsed ja puudub aktsepteeritud mehhanism, mis jõuaks ekstra ioonidest ekstra vihmani realistlikel üleküllastustel.

**7. „Õhusein, mis on kõva nagu betoon.“** Konstantse rõhu juures tõstab õhu jahutamine 30 K võrra selle tihedust ainult umbes 10 % ($\rho \propto 1/T$). Ükski temperatuurimuutus ei paneks õhku raketi jaoks käituma nagu tahkis.

## Tase 3 — Mis peaks olema tõsi

- **Uus, pikamaa väli**, mis levib läbi kivi ja ookeani tühise kaoga, ei ole tavaline elektromagnetlaine ja haakub tugevalt õhuga. See ilmneks ka elektromagnetismi täppistestides. Footon tillukese massiga omaks longitudinaalset moodi, aga laboratoorsed ja astrofüüsikalised ülemised piirid footoni massile on erakordselt väikesed (Particle Data Group loetleb piire suurusjärgus $10^{-18}$ eV).
- **Energiaallikas, mis sobib ilmaga**: vähemalt $10^{15}$–$10^{17}$ J sündmuse kohta, kohale toimetatud tundide jooksul. See on terve 1 GW elektrijaama väljund päevade kuni aastate jooksul, mis tuleks taevasse kiirata ilma teel midagi kuumutamata.
- **Testitavad sihtmärgid**: kontrollitud, juhuslikustatud katse, milles seade (ionisaatorimassiiv, kiir või muu) toodab statistiliselt olulise muutuse sademetes või rõhus võrreldes töötlemata kontrollipäevadega, korduvalt sõltumatute rühmade poolt. See on standard, mida rakendatakse pilvekülvamisele, ja põhjus, miks selle mõõdetud efekte kirjeldatakse tagasihoidlikena.
- **Avatud küsimused, mis on päris teadus**: kui palju mõjutavad kosmiliste kiirte ioonid pilvkattet (CLOUD‑i tulemused viitavad, et efekt tänasele kliimale on väike); kuidas globaalne elektriline vooluring reageerib muutuvale äikesetegevusele; kuidas teha EHD‑tõuget efektiivsemaks.

## Käivita labor

```bash
python Module_09_Weather_Engineering/simulation.py
python -m pytest tests/test_module_09.py
```

| Katse | Mida see näitab |
|---|---|
| `global_circuit` | Maa selge ilma vooluringi vool, võimsus, laeng ja juhtivus. |
| `saturation_ratio`, `critical_point`, `equilibrium_radius` | Köhleri teooria: udu allpool 100 % RH, aktiveerumine üle $S_c$, $S_c - 1 \propto m_s^{-1/2}$. |
| `deliquescence_rh` | Miks soolakristallid lahustuvad ~75 % RH juures (ja miks ideaallahuse vastus on liiga kõrge). |
| `thomson_free_energy`, `nucleation_barrier`, `saturation_for_barrier` | Ioonid alandavad nukleatsioonibarjääri, aga ainult üleküllastustel kaugel üle päris pilvede. |
| `ion_wind_thrust`, `thrust_per_power` | Ioonituul on päris, aga toodab tillukesi jõude. |
| `rain_latent_heat`, `hurricane_heat_power`, `column_heating_energy` | Ilma energiabilanss vs iga elektriline hoob. |
| `crossed_beams`, `skin_depth` | Interferents jaotab energiat ümber; raadiolained surevad meetrite kuni kilomeetrite piires maapinnas ja meres. |

## Proovi ise

1. Kasuta `critical_point`, et leida kuiv NaCl diameeter, mis aktiveerub täpselt 0,5 % üleküllastusel. Seejärel kontrolli vastust `kappa_critical_saturation`‑iga.
2. Joonista `saturation_ratio` 50 nm osakesele selle kuivraadiusest 10 μm‑ni. Märgi udu haru, tipp ja aktiveerunud haru.
3. Muuda `eps_r` funktsioonis `thomson_free_energy` 80‑st 1‑ks. Mis juhtub laengu kasuga ja miks?
4. Mitu 1 GW elektrijaama, mis töötavad ühe päeva, läheks vaja, et sobitada labori äikesetormi latentsoojust?
5. Kasutades `skin_depth`, leia sagedus, millel laine kaotab ainult poole oma amplituudist 100 m merevees. Kui pikk peaks selle sageduse antenn olema (võta veerand lainepikkust)?

## Viited

- Köhler, H., "The nucleus in and the growth of hygroscopic droplets", *Trans. Faraday Soc.* **32**, 1152 (1936).
- Petters, M. D. & Kreidenweis, S. M., "A single parameter representation of hygroscopic growth and cloud condensation nucleus activity", *Atmos. Chem. Phys.* **7**, 1961 (2007).
- Pruppacher, H. R. & Klett, J. D., *Microphysics of Clouds and Precipitation*, 2nd ed., Kluwer (1997). Köhler and Thomson theory, ion‑induced nucleation.
- Rogers, R. R. & Yau, M. K., *A Short Course in Cloud Physics*, 3rd ed., Pergamon (1989).
- Seinfeld, J. H. & Pandis, S. N., *Atmospheric Chemistry and Physics*, 3rd ed., Wiley (2016). Deliquescence and CCN activation.
- Robinson, R. A. & Stokes, R. H., *Electrolyte Solutions*, 2nd ed., Butterworths (1959). Osmotic coefficients of NaCl solutions.
- Kirkby, J. et al., "Role of sulphuric acid, ammonia and galactic cosmic rays in atmospheric aerosol nucleation", *Nature* **476**, 429 (2011).
- Rycroft, M. J., Israelsson, S. & Price, C., "The global atmospheric electric circuit, solar activity and climate change", *J. Atmos. Sol.‑Terr. Phys.* **62**, 1563 (2000).
- Xu, H. et al., "Flight of an aeroplane with solid‑state propulsion", *Nature* **563**, 532 (2018).
- French, J. R. et al., "Precipitation formation from orographic cloud seeding", *Proc. Natl. Acad. Sci. USA* **115**, 1168 (2018).
- Whittaker, E. T., "On the partial differential equations of mathematical physics", *Math. Ann.* **57**, 333 (1903).
- Jackson, J. D., *Classical Electrodynamics*, 3rd ed., Wiley (1999). Transversality of vacuum waves, skin depth.
- Kopp, G. & Lean, J. L., "A new, lower value of total solar irradiance: Evidence and climate significance", *Geophys. Res. Lett.* **38**, L01706 (2011).
- NOAA Atlantic Oceanographic and Meteorological Laboratory, Hurricane Research Division, *Hurricane FAQ* ("How much energy does a hurricane release?"). Source of the rainfall‑based heat‑release method.
