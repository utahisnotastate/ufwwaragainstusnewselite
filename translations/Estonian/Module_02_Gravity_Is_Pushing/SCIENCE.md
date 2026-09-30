# 🔬 2. moodul — Teadus loo taga

> [Õppetund](readme.md) on jutustatud aastast 2420. See lehekülg on 2025. aasta reaalsuskontroll: mis on kindlakstehtud, kus loo väide murdub ja mis peaks olema tõsi, et see töötaks. Kõike siin saab kontrollida [laborikoodiga](../../../Module_02_Gravity_Is_Pushing/simulation.py).

## 2420. aasta väide ühes lauses

Gravitatsioon ei ole tõmme: ruum on täis kiiret, isotroopset voogu ja kaks massi varjestavad teineteist selle eest, nii et tasakaalustamata voog lükkab nad kokku.

## Tase 1 — Mis on päris

Ideel on päris nimi ja pikk ajalugu: **Le Sage’i gravitatsioon** (Nicolas Fatio de Duillier, 1690; Georges‑Louis Le Sage, 1748). Seda võtsid tõsiselt Kelvin, Maxwell ja Poincaré ning geomeetria on õige:

- Väike keha näeb teist keha raadiusega $R$ kaugusel $d$ kettana, mis katab poole‑nurgaga $\theta_0$ koonuse, kus $\sin\theta_0 = R/d$.
- Kui kiired saabuvad võrdselt igast suunast, on puuduv impulsid sellest koonusest

$$F \;\propto\; \tfrac12\int_{\cos\theta_0}^{1} u\,du \;=\; \frac{1-\cos^2\theta_0}{4} \;=\; \frac{R^2}{4d^2}.$$

See on **pöördruutsõltuvus puhtast geomeetriast**. Labor kinnitab seda, visates kaks miljonit juhuslikku kiirt ja lugedes blokeerituid; jõuseadust sisse ei panda.

Energiatiheduse $u$ voog, mis liigub kiirusel $c$, kus iga keha neelab ristlõike $\sigma = h\,m$ proportsionaalselt oma massiga, annab

$$F = \frac{u\,\sigma_1\sigma_2}{4\pi r^2} = \frac{u\,h^2}{4\pi}\,\frac{m_1 m_2}{r^2}, \qquad\text{nii et Newtoniga sobitumiseks on vaja}\qquad u = \frac{4\pi G}{h^2}.$$

## Tase 2 — Kus väide murdub

Füüsikud loobusid Le Sage’i gravitatsioonist kolme probleemi pärast. Kõik kolm ilmuvad laboris numbritena, mitte arvamustena.

**1. Küllastumine (massiproportsionaalsus).** Vari kasvab massiga ainult seni, kuni keha on peaaegu läbipaistev. Ühtlase sfääri optilise raadiusega $\tau = \mu R$ jaoks on neeldunud murdosa

$$f(\tau) = 1 - \frac{1-(1+2\tau)e^{-2\tau}}{2\tau^2} \;\xrightarrow{\tau\ll 1}\; \tfrac43\tau.$$

Juures $\tau = 1$ on vari juba ainult 53 % „massiga proportsionaalsest“ väärtusest. Päris gravitatsioon on massiga proportsionaalne paremini kui üks osa $10^{13}$‑st (MICROSCOPE ekvivalentsusprintsiibi test) ega näita mõõdetavat iservarjestust (kuu laserkaugusmõõtmine).

**2. Takistus.** Keha, mis liigub kiirusel $v$ läbi isotroopse voo, põrkab eest rohkem vastu kui tagant. Neelaja jaoks on jõud $F = \tfrac43\,\sigma u\,v/c$. Kui $u$ on fikseeritud $G$‑ga, laguneks Maa orbiidi kiirus ajaga

$$t_\text{decay} = \frac{3\,h\,c}{16\pi G}.$$

**3. Kuumenemine.** Neeldunud voog on neeldunud energia: $P = \sigma u c = 4\pi G\,m\,c/h$.

**Dilemma.** Väike $h$ hoiab Maa läbipaistvana (hea probleemi 1 jaoks), aga siis peatub orbiit murdosa sekundiga ja Maa neelab umbes $10^{45}$ W. Suur $h$ taltsutab takistust, aga siis on Maa läbipaistmatu ja gravitatsioon ei skaleeruks enam massiga. Laboritest `test_no_coefficient_escapes_both_drag_and_saturation` pühkib 30 suurusjärku $h$‑st ega leia ühtegi väärtust, mis töötaks. Richard Feynman teeb sama argumendi teoses *The Feynman Lectures on Physics* (Vol. I, §7‑7).

Algse õppetunni „takistuse ümberlükkamine“ — et püsiv voog konstantsel kiirusel ei tekita takistust — ei pea vastu. Takistus tuleb *keha* liikumisest läbi voo, mitte voo kiirenemisest.

## Tase 3 — Mis peaks olema tõsi

Tõukava gravitatsiooni mudeli päästmiseks peaksid kõik need korraga olema tõsi. Igaüks on selge, testitav sihtmärk:

- **Voog, mis kannab ainesse impulssi, aga mitte energiat**, või kiirgab täpselt selle, mida neelab, nii et kuumenemist ei ole. Aga taaskiirgus täidab varju ja tapab jõu. See on Maxelli vastuväide (1875).
- **Takistus, mis kaob liikuvate kehade jaoks.** See nõuab, et voog oleks Lorentzi‑invariantne nagu kvantvaakum, aga Lorentzi‑invariantne vaakumil puudub puhkesüsteem, millest *lükata*, ja ei anna üldse netovarjejõudu.
- **Tillukesed, mõõdetavad kõrvalekalded**: gravitatsioon nõrgeneb veidi kolmanda keha taga (varjutuse „varjestus“, mida otsis Majorana 1920. aastal ja hiljem varjutuse gravimeetria, ilma kinnitatud efektita) ja väikesed massiproportsionaalsuse rikkumised väga tihedates kehades.

Moodne füüsika kirjeldab gravitatsiooni kui aegruumi kõverust (üldrelatiivsusteooria), mis läbib iga seni tehtud testi, sealhulgas gravitatsioonilained (LIGO, 2015) ja mustade aukude kujutamine (EHT, 2019). Tõukav mudel peaks ka kõik need taastootma.

## Käivita labor

```bash
python Module_02_Gravity_Is_Pushing/simulation.py
python -m pytest tests/test_module_02.py
```

| Katse | Mida see näitab |
|---|---|
| `shadow_force` | Monte Carlo kiirte lugemine annab $1/d^2$ ilma jõuseaduseta. |
| `absorbed_fraction`, `mass_proportionality` | Varjud lõpetavad massiga jälgimise, kui kehad muutuvad läbipaistmatuks. |
| `drag_and_heating` | Voo häälestamine $G$ taastootmiseks sunnib valima takistuse ja kuumenemise ning küllastumise vahel. |

## Proovi ise

1. Muuda `R2` funktsioonis `shadow_force`. Millel kaugusel lõpetab Monte Carlo tulemus sobimise lihtsa $R^2/4d^2$ seadusega ja miks?
2. Kasutades `absorbed_fraction`, leia optiline raadius, millel keha vari on 1 % nõrgem kui „massiga proportsionaalne“.
3. Tee `drag_and_heating` uuesti Kuule (7,35 × 10²² kg, 1,02 km/s ümber Maa). Kas dilemma on kergem?
4. Otsi üles MICROSCOPE tulemus (Touboul jt, 2022). Teisenda selle piir maksimaalseks lubatud optiliseks raadiuseks testmassi jaoks.

## Viited

- Feynman, Leighton & Sands, *The Feynman Lectures on Physics*, Vol. I, §7‑7 "What is gravity?" (1963).
- Edwards, M. R. (ed.), *Pushing Gravity: New Perspectives on Le Sage's Theory of Gravitation*, Apeiron (2002). A sympathetic collection that also sets out the historical objections.
- Poincaré, H., *Science and Method*, Book III (1908). The heating objection.
- Maxwell, J. C., "Atom", *Encyclopaedia Britannica*, 9th ed. (1875). The re‑emission objection.
- Touboul, P. et al., "MICROSCOPE mission: final results of the test of the equivalence principle", *Phys. Rev. Lett.* **129**, 121102 (2022).
- Abbott, B. P. et al. (LIGO/Virgo), "Observation of gravitational waves from a binary black hole merger", *Phys. Rev. Lett.* **116**, 061102 (2016).
