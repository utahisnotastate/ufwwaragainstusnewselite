# 🔬 6. moodul — Teadus loo taga

> [Õppetund](readme.md) on jutustatud aastast 2420. See lehekülg on 2025. aasta reaalsuskontroll: mis on kindlakstehtud, kus loo väide murdub ja mis peaks olema tõsi, et see töötaks. Kõike siin saab kontrollida [laborikoodiga](../../../Module_06_Language_of_Reality/simulation.py).

## 2420. aasta väide ühes lauses

Kõik looduse kujundid on „külmunud heli“: seisulaine korrastab ainet nii, nagu viiulipoogen korrastab liiva plaadil, nii et õige heli võib ainet ehitada, lahustada või teha kivi kaalutuks.

## Tase 1 — Mis on päris

**Chladni figuurid on päris ja need on ilus füüsika.** Ernst Chladni (1787) mängis poogeniga liivaga kaetud metallplaate ja leidis, et liiv koguneb **sõlmjoonte** äärde, kus plaat ei liigu. Iga noot annab erineva figuuri. Figuurid seab paika plaadi liikumisvõrrand.

**Trumi nahk ja plaat alluvad erinevatele võrranditele.** Venitatud membraan (trumi nahk) allub laine (Helmholtzi) võrrandile, $\nabla^2 w + k^2 w = 0$. Fikseeritud servaga ruutmembraanil küljega $L$ on sagedused

$$f_{mn} = \frac{c}{2L}\sqrt{m^2+n^2}.$$

Chladni plaat on peen, jäik **plaat**, mida juhib Kirchhoffi biharmooniline võrrand

$$D\,\nabla^4 w - \rho h\,\omega^2 w = 0, \qquad D = \frac{E h^3}{12(1-\nu^2)} .$$

Lihtsalt toetatud ruutplaadi jaoks on täpne vastus $\omega_{mn} = \sqrt{D/\rho h}\;\pi^2 (m^2+n^2)/L^2$, nii et $f_{mn} \propto m^2 + n^2$, **mitte** $\sqrt{m^2+n^2}$. See on päris, testitav õppetund: (1,2) mood istub trummil $\sqrt{5/2} = 1{,}58$ korda fundamentaalist, aga plaadil $5/2 = 2{,}5$ korda. Labor lahendab mõlemad võrrandid numbriliselt (5‑punktiline Helmholtz ja 13‑punktiline biharmooniline šabloon) ning sobib täpsete tulemustega paremini kui 0,5 %, oodatava teise järgu konvergentsiga.

Kui kahel moodil on sama sagedus (näiteks (1,2) ja (2,1) ruudul), võngub plaat segus, $\sin m\pi x\,\sin n\pi y \pm \sin n\pi x\,\sin m\pi y$. Need segud tekitavad päris Chladni figuuride diagonaale, rõngaid ja tähti; labor kontrollib, et „−“ segul on sõlmjoon täpselt diagonaalil. Chladni enda vaba‑servaga plaate on raskem lahendada (Leissa 1969 kogub klassikalised tulemused). Ringplaatide jaoks on **Chladni seadus** $f \approx C\,(m + 2n)^p$, kus $m$ on sõlm‑diameetrite arv, $n$ sõlmringide arv ja $p \approx 2$ lamedatele plaatidele, hea empiiriline reegel (Rossing 1982).

**Heli suudab tõepoolest lükata, lõksustada ja levitada väikseid objekte.** Seisulaine avaldab osakesele, mis on lainepikkusest palju väiksem, püsivat **akustilist kiirgusjõudu**. Gor'kov (1962) näitas, et see tuleb potentsiaalist,

$$U = 2\pi R^3\left[\frac{f_1\,\langle p^2\rangle}{3\rho_0 c_0^2} - \frac{f_2\,\rho_0\langle v^2\rangle}{2}\right], \qquad \mathbf F = -\nabla U,$$

$$f_1 = 1 - \frac{\kappa_p}{\kappa_0}, \qquad f_2 = \frac{2(\rho_p-\rho_0)}{2\rho_p+\rho_0} .$$

Kuna $\mathbf F = -\nabla U$, on see jõud **konservatiivne** (selle mooduli varasem mustand nimetas seda mitte‑konservatiivseks, mis oli vale): suletud teel osakese kandmine ei tee netotööd ja osakesed settivad $U$ miinimumidesse. 1D seisulaines $p = p_0\cos kx\cos\omega t$ muutub see $F = 4\pi\Phi\,kR^3 E_\text{ac}\sin 2kx$, kontrastiteguriga $\Phi = f_1/3 + f_2/2$ ja energiatihedusega $E_\text{ac} = p_0^2/4\rho_0 c_0^2$ (Bruus 2012). Labor kontrollib $U$ numbrilist gradienti selle valemi vastu, näitab null netoöö üle lainepikkuse ja laseb osakestel triivida:

- polüstüreen vees ($\Phi = +0{,}22$) koguneb **rõhusõlmedesse**,
- lipiidipiisk vees ($\Phi = -0{,}07$) koguneb **rõhuantinoodidesse**.

See on akustiliste vedeliku‑rakusorteerijate ja **akustiliste levitatorite** tööpõhimõte. Marzo jt (2015) ehitasid holograafilised akustilised pintsetid 40 kHz transducerite massiividest, mis levitavad ja liigutavad millimeetrilisi helmeid õhus. Labor hindab vajalikku rõhku: umbes 280 Pa (140 dB) vahthelmeste jaoks ja umbes 1,8 kPa (156 dB) tahke polüstüreeni jaoks, sõltumata helme suurusest seni, kuni helm on 8,6 mm lainepikkusest palju väiksem.

**Lumehelbed on kuusnurksed päris põhjusel, aga see ei ole heli.** Tavalisel jääl (jää Ih) on kuusnurkne kristallvõre, mille seab veemolekulide vesiniksidemete geomeetria. Lumekristalli kuuekordne kuju tuleb sellest võrest ja sellest, kuidas aur sellele difundeerub (Libbrecht 2005).

## Tase 2 — Kus väide murdub

**1. Mustri skaala on lainepikkus.** Heli saab ainet korrastada ainult poole lainepikkuse skaalal: 4,3 mm 40 kHz juures õhus. Üksikute aatomite (~0,1 nm) paigutamiseks vajaksid 0,2 nm lainepikkust. Labor näitab, miks see on võimatu:

| Keskkond | Vajalik sagedus | Piir |
|---|---|---|
| Tahkis ($c \approx 5$ km/s) | ~25 THz | Räni kõrgeim võnge on 15,6 THz ja lühim laine, mida võre kannab, on kaks aatomivahet, 0,47 nm. |
| Õhk | ~1,7 × 10¹² Hz | Heli ei eksisteeri allpool molekulaarset vaba teepikkust (~66 nm), mis piirab selle ~5 GHz lähedale. |

Aatomiskaalal on „heli“ (fonoonid) aatomid ise, mis värisevad. See ei saa olla mall, mis neid paigutab.

**2. Vibratsioonid sõidavad sidemetel; nad ei tee neid.** Räni kõrgeim fonoon kannab 65 meV. Ühe aatomi eemaldamine kristallist maksab 4,63 eV, umbes 70 korda rohkem. Mis ainet koos hoiab, on elektronide kvantmehaanika (keemilised sidemed), mitte ülalhoidv toon.

**3. Suuri kive ei saa õhku laulda.** Gor'kovi valem kehtib ainult objektidele, mis on lainepikkusest palju väiksemad. 2 m ploki jaoks peab lainepikkus olema kümneid meetreid (umbes 17 Hz). Graniidi hoidmine sellel sagedusel vajab rõhuamplituudi 1,4 atmosfääri: iga tsükli madala rõhu pool peaks langema **alla vaakumi**, mida õhk ei suuda. Miski akustikas ei pane objekti „unustama, et ta on raske“. Faaskonjugatsioon ehk „ajas tagasipööratud akustika“ on päris (Fink 1997), aga see fokusseerib lained tagasi nende allikale. See ei tühista kaalu.

**4. Teooria nimed ei pea vastu.** „Formoni teooria“ (Bearden) **ei ole füüsikas tunnustatud teooria**: sellel puudub eelretsenseeritud formulatsioon või eksperimentaalne tugi. „Skalaarheli, mis lükkab aegruumi“ ei oma füüsikas vastet. Pikilained on lihtsalt tavaline heli (õhus on kogu heli pikilaine) ja need lükkavad ainet, mitte aegruumi. Hans Jenny *Cymatics* (1967) on armas fotograafiline salvestis vibratsioonimustritest, aga see ei näita, et aine on „külmunud heli“.

## Tase 3 — Mis peaks olema tõsi

Selleks et „aine ehitamine heliga“ oleks rohkem kui metafoor, peaksid kõik need olema tõsi:

- **Laine aatomiskaala lainepikkusega, mis ei ole tehtud aatomitest, mida see korrastab.** Valgusel ja elektronkiirtel on nii lühikesed lainepikkused. Seetõttu töötavad optilised pintsetid, elektronmikroskoobid ja skaneeriv‑sondi „aatomikirjutamine“ — ja nad teevad seda elektromagnetismi, mitte heli kaudu.
- **Energia kvandi kohta võrreldav sidemeenergiatega (eV).** Alles siis saaks laine sidemeid otse teha või murda. Heli kvandid tipnevad kümnetes meV.
- **Kvantitatiivne ennustus.** Näiteks kindel sagedus, mis mõõdetavalt muudab kristalli struktuuri või kivi kaalu, mida labor saaks seejärel testida. Ühtegi ei ole avaldatud.

Päris, avatud piirid on tagasihoidlikumad ja endiselt põnevad: akustilised hologrammid, mis koguvad palju osakesi korraga, rakkude ja kudede akustiline manipuleerimine ning foonilised kristallid, mis on projekteeritud heli ja soojuse juhtimiseks.

## Käivita labor

```bash
python Module_06_Language_of_Reality/simulation.py
python -m pytest tests/test_module_06.py
```

| Katse | Mida see näitab |
|---|---|
| `membrane_frequencies`, `membrane_modes_fd` | Trumi nahk: $f \propto \sqrt{m^2+n^2}$, kinnitatud lõplike diferentside lahendiga. |
| `plate_frequencies`, `plate_modes_fd`, `biharmonic_simply_supported` | Plaat: $f \propto m^2+n^2$, kinnitatud 13‑punktilise biharmoonilise lahendiga. |
| `chladni_pattern` | Degeneerunud moodisegud ja nende sõlmjooned (kuhu liiv koguneb). |
| `gorkov_potential_1d`, `gorkov_force_1d`, `settle_positions` | Konservatiivne kiirgusjõud; positiivne kontrast läheb sõlmedesse, negatiivne antinoodidesse. |
| `levitation_pressure`, `spl_db` | 140–156 dB levitab helmeid; kivi vajab „alla‑vaakumi“ rõhke. |
| `atom_scale_sound`, `mean_free_path_air` | Miks heli ei saa aatomeid paigutada. |

## Proovi ise

1. Funktsioonis `biharmonic_simply_supported` muuda ghost‑sõlme märk $-1$‑st $+1$‑ks. See muudab servad „lihtsalt toetatud“‑st „klambriks“. Mis juhtub $f_{21}/f_{11}$‑ga? (Klambitud plaadid on lähemal päris kelladele ja taldrikutele.)
2. Joonista `chladni_pattern(1, 3, sign=+1)` ja `sign=-1` piltidena ning märgi, kus $|w|$ on väike. Milline näeb rohkem välja nagu Chladni figuur, mida oled näinud?
3. Kasuta `levitation_pressure`, et leida sagedus, millel 1 mm veepiiska saab levitada 150 dB‑ga. Kas piisk on endiselt lainepikkusest palju väiksem?
4. Korda `atom_scale_sound` teemandi jaoks, mille helikiirus on umbes 18 km/s ja kõrgeim fonoon umbes 1332 cm⁻¹. Kas see jõuab lähemale „aatomite paigutamisele“?
5. Arvuta $\Phi$ punaste vereliblede jaoks plasmas (otsi ligikaudsed tihedused ja helikiirused). Kas nad lähevad sõlmedesse või antinoodidesse?

## Viited

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
