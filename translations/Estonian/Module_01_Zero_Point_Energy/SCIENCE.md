# 🔬 1. moodul — Teadus loo taga

> [Õppetund](readme.md) on jutustatud aastast 2420. See lehekülg on 2025. aasta reaalsuskontroll: mis on kindlakstehtud, kus loo väide murdub ja mis peaks olema tõsi, et see töötaks. Kõike siin saab kontrollida [laborikoodiga](../../../Module_01_Zero_Point_Energy/simulation.py).

## 2420. aasta väide ühes lauses

Tühi ruum on nullpunktienergia kõrgsurve‑„ookean“ ja mootoril tuleb vaid avada selles klapp, et saada tasuta jõudu.

## Tase 1 — Mis on päris

**Vaakum ei ole „mitte midagi“.** Kvantmehaanika ütleb, et harmooniline ostsillaator ei saa kunagi olla täiesti paigal: selle madalaim energia on $E_0 = \tfrac12\hbar\omega$, mitte null. Elektromagnetväli on selliste ostsillaatorite kogum, üks iga moodi kohta, nii et isegi kui iga footon on eemaldatud, säilitab iga mood oma $\tfrac12\hbar\omega$. See nullpunktienergia on standardfüüsika osa ja sellel on mõõdetavaid tagajärgi (Lambi nihe, spontaanne kiirgus ja alljärgnev).

**Casimiri efekt.** Aseta kaks paralleelset laadimata peeglit kaugusele $d$. Nende vahele jäävad ainult moodid, mis sinna mahuvad, samal ajal kui väljaspool eksisteerivad kõik moodid. Nullpunktienergia erinevus annab tõmbejõu. Täiuslike peeglite jaoks (Casimir, 1948):

$$\frac{E}{A} = -\frac{\pi^2\hbar c}{720\,d^3}, \qquad P = -\frac{\partial (E/A)}{\partial d} = -\frac{\pi^2\hbar c}{240\,d^4}.$$

Labor hindab neid CODATA konstantidega: $P \approx -1.30\times10^{-3}$ Pa juures $d = 1\ \mu$m ja $\approx -13$ Pa juures 100 nm. Ühe atmosfäärini jõuab see alles umbes 11 nm juures. Jõudu on mõõdetud, esmalt veenvalt Lamoreaux (1997, sfäär–plaat, 0,6–6 µm), seejärel AFM‑iga Mohideen & Roy (1998) ja paralleelplaatide vahel Bressi jt (2002).

**Päris peeglid.** Päris metallid lõpetavad peegeldamise sagedustel üle nende plasma‑sageduse $\omega_p$, nii et ideaalne valem ülehindab jõudu lühikesel kaugusel. Lifshitzi teooria (1956) käsitleb päris materjale. Nulltemperatuuril, kahe identse poolruumi jaoks,

$$\frac{E}{A} = \frac{\hbar}{4\pi^2}\int_0^\infty d\xi\int_0^\infty k\,dk \sum_{\mathrm{TE,TM}} \ln\!\left(1 - r^2 e^{-2\kappa d}\right), \qquad \kappa = \sqrt{k^2 + \xi^2/c^2},$$

Fresneli koefitsientidega, mis on hinnatud imaginaarsagedusel $i\xi$:

$$r_{\mathrm{TE}} = \frac{\kappa - K}{\kappa + K},\qquad r_{\mathrm{TM}} = \frac{\varepsilon\kappa - K}{\varepsilon\kappa + K},\qquad K = \sqrt{k^2 + \varepsilon(i\xi)\,\xi^2/c^2}.$$

Kulla jaoks kasutab labor Drude’i mudelit $\varepsilon(i\xi) = 1 + \omega_p^2/[\xi(\xi+\gamma)]$ koos $\hbar\omega_p = 9.0$ eV ja $\hbar\gamma = 35$ meV. Integraatorit kontrollitakse kolmel viisil: $r = 1$ korral taastoodab see Casimiri kinniseid vorme täpsusega $10^{-6}$; selle rõhk võrdub $-\partial(E/A)/\partial d$; ja subnanomeetrilistel vahedel muutub see mitte‑retarditud van der Waalsi tõmbeks, $E/A \to -A_H/(12\pi d^2)$, Hamakeri konstandiga $A_H \approx 2.1\times10^{-19}$ J, mis sobib sõltumatu ühemõõtmelise integraaliga 0,1 % täpsusega.

| $d$ | kuld / täiuslik peegel |
|---|---|
| 10 nm | 0.08 |
| 100 nm | 0.44 |
| 1 µm | 0.88 |
| 10 µm | 0.98 |

## Tase 2 — Kus väide murdub

**1. Nullpunktienergia on põrand, mitte reservuaar.** See on *põhioleku* energia, madalaim olek, milles väli saab olla. Energia ammutamine tähendab minekut madalamasse olekusse ja seda ei ole. Allveelaeva analoogia luhtub just siin: meravesi saab sisse voolata, sest allveelaeva sees on madalam rõhk. Miski ei saa olla „madalama rõhuga“ kui vaakumi põhiolek.

**2. Casimiri õõnsus on vedru, mitte kaev.** Jõud sõltub ainult asukohast, seega on see konservatiivne. Saad tööd üks kord, lastes plaatidel kokku lüüa, aga pead maksma sama töö nende lahutamiseks. Labor integreerib jõudu ümber suletud tsükli (1 µm → 100 nm → 1 µm), kasutades kahe käigu jaoks erinevaid diskreetimisvõrke, et vastus ei oleks sisse ehitatud:

| Plaadid (1 m²) | töö sisse liikudes | töö välja liikudes | neto |
|---|---|---|---|
| täiuslikud peeglid | $+4.33\times10^{-7}$ J | $-4.33\times10^{-7}$ J | $\sim10^{-13}$ J (kvadratuuri viga, $\sim10^{-6}$ käigust) |
| kuld | $+2.24\times10^{-7}$ J | $-2.24\times10^{-7}$ J | $\sim10^{-13}$ J |

Isegi ühesuunaline kokkulangemine on väike. Ruutmeeter täiuslikke peegleid, mis kukuvad 1 µm‑lt 10 nm‑le, annab kõige rohkem $4.3\times10^{-4}$ J. AA‑patarei hoiab umbes $10^4$ J.

**3. Liikuvad peeglid teevad valgust, aga energia tuleb mootorist.** Dünaamiline Casimiri efekt on päris. Wilson jt (2011) moduleerisid ülijuhtiva ahela efektiivset pikkust gigahertsisagedustel ja tuvastasid vaakumist tulevaid footonipaare. Iga paari energia liidetakse üheks ajami kvandiks ($\hbar\omega_1 + \hbar\omega_2 = \hbar\omega_\text{drive}$), nii et väljundvõimsus tuleb pumbast. See on viis energiat *muundada*, mitte leida.

**4. „10⁹⁵ g/cm³“ ookean on gravitatsiooniga vastuolus.** Loo number tuleb Plancki tihedusest $c^5/(\hbar G^2) \approx 5\times10^{96}$ kg/m³ $\approx 5\times10^{93}$ g/cm³, mille saad, kui summeerid $\tfrac12\hbar\omega$ moodide üle kuni Plancki pikkuseni. Energia gravitatsioonib ja vaakumienergia, mida Universumi paisumine tegelikult näitab (tumeenergia), on ainult

$$\rho_\Lambda c^2 = \Omega_\Lambda\,\frac{3H_0^2c^2}{8\pi G} \approx 5\times10^{-10}\ \text{J/m}^3.$$

Naiivne hinnang, $\hbar c\,k_\text{max}^4/(16\pi^2)$ koos $k_\text{max} = 1/\ell_P$, on umbes $3\times10^{111}$ J/m³. See on mittevastavus **~10¹²¹**, *kosmoloogilise konstandi probleem* (Weinberg, 1989). See on avatud probleem, aga see osutab loole vastupidises suunas: mida iganes vaakum teeb, ei käitu see nagu tohutu reservuaar.

**5. Vaakum ei suru nagu vesi.** Lorentzi‑invariantse vaakumienergia rõhk on $p = -\rho c^2$, pinge pigem kui muljuv rõhk. Sama igas taustsüsteemis ja igas suunas, sellel puudub gradient ja ainult gradient annab jõu. Casimiri jõud eksisteerib, sest plaadid muudavad moodistruktuuri, ja kaob, kui plaadid eemaldatakse.

Universumisisene „tõestus“ ütleb ka, et Fermi nõrga vastastikmõju teooria luhtub kõrgetel energiatel, „kui ruumi panust eiratakse“. Fermi teooria tõepoolest laguneb (umbes mõnesaja GeV juures). Selle parandas elektro‑nõrk teooria, mille ennustatud W‑ ja Z‑bosonid leiti CERNis 1983. aastal, mitte vaakumienergia ammutamise abil.

## Tase 3 — Mis peaks olema tõsi

Selleks et vaakumimootor töötaks, peaks vähemalt üks neist olema avastatud. Igaüks on testitav:

- **Olek vaakumi all.** Iga süsteem, mis annab suletud tsüklis netotööd „vaakumist“, oleks madalama energiaga olek kui põhiolek. Täppis‑Casimiri katsed mõõdavad jõude 1 % tasemel. Tsükkel, mis tagastab netotööd, ilmneks hüstereesisilmusena jõu versus kauguse graafikul. Ühtegi ei ole nähtud.
- **Mitte‑konservatiivsed Casimiri jõud.** Jõud, mis sõltuks liikumise suunast (mitte ainult asukohast) nulltemperatuuril, oleks uus füüsika. Hõõrdumiselaadne „kvant‑hõõrdumine“ külgsuunas libisevate pindade vahel on ennustatud, aga tilluke, ja see võtab endiselt energiat *liikumisest*.
- **Kosmoloogilise konstandi probleemi lahendus, mis jätab tohutu kasutatava energia.** Kandidaatlahendused (supersümmeetrilised tühistamised, antropiline valik, muudetud gravitatsioon) teevad efektiivse vaakumienergia väikeseks. Ükski ei tee seda suureks ja kättesaadavaks.

Avatud küsimused, mis jäävad päriseks ja huvitavaks: miks on vaadeldud vaakumienergia nii väike, aga mitte null; kas Casimiri jõude saab teha tõrjuvateks praktiliste nanomasinate jaoks (mõnes keskkonnas saab: Munday, Capasso & Parsegian, *Nature* **457**, 170 (2009)); ja kuidas temperatuur ning materjali vastus kombineeruvad mikromeetriskaaladel — endiselt aktiivne debatt.

## Käivita labor

```bash
python Module_01_Zero_Point_Energy/simulation.py
python -m pytest tests/test_module_01.py
```

| Katse | Mida see näitab |
|---|---|
| `casimir_pressure_ideal`, `casimir_energy_ideal` | Casimiri kinnised vormid: vaakum tõepoolest surub, tugevasti ainult nanomeetritel. |
| `lifshitz_pressure`, `lifshitz_energy`, `gold_reduction_factor` | Päris kuldplaadid numbrilise integreerimisega üle imaginaarsageduse; nõrgemad kui ideaalsed, lähenedes mikromeetritel. |
| `hamaker_constant` | Sõltumatu kontroll lühikese ulatuse (van der Waalsi) piirile. |
| `closed_cycle_work`, `one_shot_energy` | Suletud tsükkel annab null netoöö; ühesuunaline kokkulangemine annab tillukese, mittekorduva energia. |
| `planck_density`, `naive_vacuum_energy_density`, `observed_dark_energy_density`, `cosmological_constant_gap` | ~10¹²¹ lõhe naiivse „ookeani“ ja selle vahel, mida gravitatsioon mõõdab. |

## Proovi ise

1. Muuda `GOLD_PLASMA_EV` alumiiniumi ≈ 12,5 eV‑ks. Kuidas muutub kuld/ideaalne suhe 100 nm juures ja miks aitab kõrgem plasma‑sagedus?
2. Kasutades `casimir_pressure_ideal`, leia vahekaugus, millel Casimiri rõhk võrdub päikesevalguse rõhuga peeglile (umbes 9 µPa).
3. Proovi kavandada petutsüklit: anna `closed_cycle_work`‑ile rõhufunktsioon, mis on ideaalne seadus sisse liikudes ja kulla seadus välja liikudes. Saad netotööd — selgita nüüd, milline füüsikaline protsess peaks plaatide materjali 100 nm juures vahetama ja mida see maksaks.
4. Funktsioonis `naive_vacuum_energy_density`, milline lõige $k_\text{max}$ paneks naiivse hinnangu sobima vaadeldud tumeenergia tihedusega? Teisenda see pikkuseks. (Peaksid saama kümneid mikromeetreid, millimeetri murdosa — üks põhjus, miks submillimeetrilised gravitatsioonitestid on huvitavad.)

## Viited

- Casimir, H. B. G., "On the attraction between two perfectly conducting plates", *Proc. K. Ned. Akad. Wet.* **51**, 793 (1948).
- Lifshitz, E. M., "The theory of molecular attractive forces between solids", *Sov. Phys. JETP* **2**, 73 (1956).
- Lamoreaux, S. K., "Demonstration of the Casimir force in the 0.6 to 6 µm range", *Phys. Rev. Lett.* **78**, 5 (1997).
- Mohideen, U. & Roy, A., "Precision measurement of the Casimir force from 0.1 to 0.9 µm", *Phys. Rev. Lett.* **81**, 4549 (1998).
- Bressi, G., Carugno, G., Onofrio, R. & Ruoso, G., "Measurement of the Casimir force between parallel metallic surfaces", *Phys. Rev. Lett.* **88**, 041804 (2002).
- Lambrecht, A. & Reynaud, S., "Casimir force between metallic mirrors", *Eur. Phys. J. D* **8**, 309 (2000). Source of the gold Drude parameters.
- Bordag, M., Mohideen, U. & Mostepanenko, V. M., "New developments in the Casimir effect", *Phys. Rep.* **353**, 1 (2001).
- Wilson, C. M. et al., "Observation of the dynamical Casimir effect in a superconducting circuit", *Nature* **479**, 376 (2011).
- Munday, J. N., Capasso, F. & Parsegian, V. A., "Measured long‑range repulsive Casimir–Lifshitz forces", *Nature* **457**, 170 (2009).
- Weinberg, S., "The cosmological constant problem", *Rev. Mod. Phys.* **61**, 1 (1989).
- Planck Collaboration (Aghanim, N. et al.), "Planck 2018 results. VI. Cosmological parameters", *Astron. Astrophys.* **641**, A6 (2020).
