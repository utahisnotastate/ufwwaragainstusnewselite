# 🔬 7. moodul — Teadus loo taga

> [Õppetund](readme.md) on jutustatud aastast 2420. See lehekülg on 2025. aasta reaalsuskontroll: mis on kindlakstehtud, kus loo väide murdub ja mis peaks olema tõsi, et see töötaks. Kõike siin saab kontrollida [laborikoodiga](../../../Module_07_DNA_Antenna/simulation.py).

## 2420. aasta väide ühes lauses

DNA on spiraalikujuline antenn, mis võtab vastu juhiseid informatsiooniväljast, sealhulgas sinu enda mõtetest ja tunnetest, ning kirjutab keha ümber, et sellega sobida.

## Tase 1 — Mis on päris

**DNA kuju on täpselt teada.** B‑DNA, rakkudes leitud vorm, on paremakäeline kaksikheeliks (Watson & Crick 1953; Franklin & Gosling 1953) koos

- diameetriga umbes **2,0 nm**,
- tõusuga **0,34 nm** aluspaari kohta,
- umbes **10,5 aluspaari pöörde kohta** lahuses (34,3° keerd sammu kohta), nii et samm on **3,4–3,6 nm**.

See on lühikestel vahemaadel ka jäik: selle püsivuspikkus on füsioloogilises soolas umbes 50 nm.

**DNA suhestub tõepoolest valgusega, tugevalt, ultravioletses.** DNA neeldub kõige tugevamalt lähedal **260 nm** (4,77 eV footoni kohta). Igapäevane laborireegel „neeldumine 1 juures 260 nm tähendab 50 µg/mL kaksikahelalist DNA‑d“ annab umbes **6600 M⁻¹cm⁻¹ nukleotiidi kohta**. Kaksikheeliks neeldub umbes 30–40 % vähem kui samad alused vabade nukleotiididena (labor saab 39 % ligikaudsete õpiku nukleotiidiväärtustega). See **hüpokromism** juhtub, sest virnastatud alused haakuvad elektrooniliselt. Pärast UV‑ergastust saab ergastus jagada mitme virnastatud aluse vahel ja virnastamine kontrollib, kui kiiresti energia hajub (Crespo‑Hernández, Cohen & Kohler 2005). See on päris, kiire füüsika ja see aitab kaitsta DNA‑d UV‑kahjustuse eest. See töötab mõne aluse, mõne nanomeetri ulatuses.

**Energia saab DNA‑l hüpata, nanomeetrite ulatuses.** Försteri resonantsenergia ülekanne (FRET) liigutab ergastuse doonorvärvist aktseptorisse efektiivsusega

$$E = \frac{1}{1 + (r/R_0)^6},$$

kus $R_0$ on tüüpiliselt umbes 5 nm. DNA heeliksile paigutatud värvid 15 aluspaari kaugusel (5,1 nm) kannavad üle umbes poole oma energiast; 30 aluspaari juures umbes 1 %. See järsk $r^{-6}$ langus on põhjus, miks FRET‑i kasutatakse „spektroskoopilise joonlauana“ (Stryer & Haugland 1967), sageli DNA‑ga endaga joonlauana.

**DNA võngub ja „hingab“.** Peyrard–Bishopi mudel (1989) käsitleb iga aluspaari venitust $y_n$, mida hoiab Morse’i potentsiaal $V(y) = D\,(e^{-ay} - 1)^2$ (vesiniksidemed) ja mis on seotud naabritega virnastamisvedrudega:

$$H = \sum_n \left[\frac{p_n^2}{2m} + \frac{k}{2}(y_n - y_{n-1})^2 + D\,(e^{-a y_n} - 1)^2\right].$$

Väikesed võnked moodustavad fonooniriba, $m\omega^2 = 2Da^2 + 4k\sin^2(q/2)$, terahertsi vahemikus. Labor kontrollib seda numbrilise Hessi vastu. Labor lahendab ka mudeli termodünaamika täpselt ülekande‑integraali meetodiga: aluspaarid avanevad temperatuuri tõustes veidi rohkem ja üle läve tulevad ahelad lahku (denaturatsioon ehk „sulamine“). Siin kasutatud illustreerivate harmoonilise virnastamise parameetritega juhtub see lähedal 490 K, hästi üle päris DNA 340–370 K. Dauxois, Peyrard & Bishop (1993) näitasid, et mittelineaarse virnastamise lisamine annab katsetes nähtava terava sulamise. Punkt on kvalitatiivne: DNA dünaamika on tavaline soojusfüüsika.

**Geene reguleerib keskkond, keemia kaudu.** Epigeneetilised märgid (DNA metülatsioon, histooni modifikatsioonid) muudavad, milliseid geene ekspresseeritakse. Nad reageerivad dieedile, hormoonidele ja kogemusele; rottidel näiteks muudab ema hool stressihormooni retseptori geeni metülatsiooni järglastes (Weaver jt 2004). Signaalid on molekulid: hormoonid, transkriptsioonifaktorid ja ensüümid.

**„Praht‑DNA“ kohta.** Umbes 1–2 % inimese genoomist kodeerib valke. Regulatoorsed elemendid (promootorid, enhanserid) ja mitte‑kodeerivad RNA‑d on päris ja olulised. ENCODE projekt (2012) teatas „biokeemilisest funktsioonist“ 80 % genoomile, aga see definitsioon luges mis tahes biokeemilist aktiivsust, näiteks üks kord transkribeerimist või valgu seondumist. Seda vaidlustati tugevalt, näiteks Graur jt (2013), kes väitsid, et funktsioon peaks tähendama midagi, mida valik säilitab. Genoomi osa evolutsioonilise piirangu all hinnatakse palju madalamaks.

## Tase 2 — Kus väide murdub

**1. Kui DNA oleks antenn, oleks see häälestatud röntgenile, mitte mõtetele ega biofootonitele.** Spiraalne antenn kiirgab piki oma telge (Krausi „aksiaalne mood“), kui selle ümbermõõt $C$ rahuldab $\tfrac34 < C/\lambda < \tfrac43$. B‑DNA jaoks $C = \pi \times 2{,}0\text{ nm} = 6{,}3$ nm, nii et

$$\lambda \approx 4{,}7\text{–}8{,}4\text{ nm} \quad (150\text{–}260\text{ eV}),$$

mis on äärmuslik ultravioletne või pehme röntgenvalgus ja see ioniseerib molekule. Eluskoest teatatud ülinõrk „biofootoni“ kiirgus (200–800 nm; vt Cifra & Pospíšil 2014) on **30–130 korda liiga pikk**. Selle sammunurk (30°) on ka väljaspool Krausi parimat vahemikku 12–14°. Peale selle ei ole DNA metalltraat: selle selgroog ei kanna vabu elektrone nii nagu antenn.

**2. Biofootoneid on juhiste kandmiseks palju liiga vähe.** Isegi helde 100 footonit sekundis cm² kohta, kõik suunatud DNA‑le, tabaks antud spiraalipööret umbes **üks kord iga 4400 aasta tagant**.

**3. Soolavesi varjestab ja neeldub.** Rakud on soolane vesi. 150 mM juures on **Debye’i varjestuspikkus**

$$\lambda_D = \sqrt{\frac{\varepsilon_r\varepsilon_0 k_B T}{2 N_A e^2 I}} \approx \frac{0.304}{\sqrt{I\,[\text{M}]}}\ \text{nm} \approx 0.78\text{ nm}.$$

Laengu elektrostaatiline väli on juba mõne miljondiku peal 10 nm kaugusel. Võnkuvad väljad pääsevad läbi, aga soolase vee Debye’i relaksatsioonimudel (juhtivus umbes 1,6 S/m) näitab, et mikrolained langevad $1/e$‑ni umbes **2,6 cm juures 1 GHz, 2,4 mm juures 10 GHz ja 0,24 mm juures 100 GHz**. 50 nm jäik DNA segment 1 GHz dipoolina omaks kiirgustakistust umbes $10^{-11}\ \Omega$, võrreldes umbes 50 Ω töötava antenniga. See on erakordselt kehv antenn.

**4. Raadiofootonid on keemia jaoks liiga nõrgad.** 1 GHz footon kannab $1{,}5\times10^{-4}\,k_BT$ kehatemperatuuril. Molekule tõukab iga pikosekundi tuhandeid kordi rohkem energiat. Seetõttu kahjustab UV (178 $k_BT$ footoni kohta 260 nm juures) DNA‑d ja raadio mitte.

**5. „Fantoomlehe“ ja „mitogeneetilise kiirguse“ lood.** Koroonalahenduse (Kirliani) fotograafia kontrollitud uuringud leidsid, et pildid sõltuvad tugevalt niiskusest, rõhust ja säritusest (Pehek, Kyler & Faust 1976). „Fantoomleht“ ei ole kindlakstehtud efekt. Gurwitschi mitogeneetiline kiirgus ja Kaznatšejevi „tsütopaatilise ülekande“ väited ei saanud sõltumatut kordamist.

**6. Puuduvad tõendid, et DNA võtab vastu „morfogeneetilisi juhiseid“ väljast.** Kuidas kehad kuju võtavad, uuritakse detailselt ja see töötab geenide, valkude, signaalmolekulide gradientide ning rakkudevaheliste mehaaniliste ja elektriliste vihjete kaudu. Sinu tunded võivad tõepoolest keha mõjutada, närvide, hormoonide ja immuunsüsteemi kaudu, ja epigeneetika on osa sellest loost. Aga käskjalad on molekulid, mitte ülekanne.

## Tase 3 — Mis peaks olema tõsi

Selleks et „DNA kui antenn“ oleks teaduslik hüpotees, peaks keegi näitama kõiki neid:

- **Vastuvõtja, mis töötab soolases vees.** Kas signaalisagedus, mis tungib koesse *ja* haakub 2 nm heeliksiga, või mehhanism (näiteks molekulaarne resonants), mida varjestus ja soojusmüra ei uhu välja. Mõõdetav test: kindel sagedus, mis muudab geeniekspressiooni rakukultuuris, koos doos–vastus kõveraga, pimestamise ja sõltumatu kordamisega.
- **Piisavalt energiat signaali kohta.** DNA keemia muutmine vajab energiat lähedal elektronvoldile sündmuse kohta või võimendit rakus, mis muudab tillukese signaali suureks vastuseks, ületades $k_BT$ müra.
- **Kandja „info väljast“ jaoks.** Lugu vajab nimetatud füüsikalist välja mõõdetava tugevuse ja ennustatud spektriga. Nagu kirjutatud, ei ennusta see ühtegi arvu, mida saaks kontrollida.

Lähedased avatud küsimused on päris ja huvitavad: kui kaugele saab laeng DNA‑l liikuda (mõned nanomeetrid, hüpates virnastatud aluste vahel), kuidas UV‑energia jagatakse virnastatud aluste vahel, kuidas DNA „hingamine“ aitab valkudel seda lugeda ja kui palju mitte‑kodeerivast genoomist loeb.

## Käivita labor

```bash
python Module_07_DNA_Antenna/simulation.py
python -m pytest tests/test_module_07.py
```

| Katse | Mida see näitab |
|---|---|
| `b_dna_geometry`, `helical_antenna_band`, `biophoton_mismatch` | DNA‑suurune heeliks oleks häälestatud ~6 nm (EUV/pehme röntgen), 30–130× lühem kui biofootonid. |
| `photon_hits_per_turn` | Biofootonite voogud on molekulaarsel skaalal kaduvväikesed. |
| `uv_absorption` | ~6600 M⁻¹cm⁻¹ nukleotiidi kohta 260 nm juures ja ~39 % hüpokromism virnastamisest. |
| `fret_efficiency`, `fret_along_dna` | Energiaülekanne DNA‑l: 50 % ~15 bp juures, ~1 % 30 bp juures. |
| `pb_mode_frequencies_numeric`, `pb_dispersion`, `pb_transfer_integral` | Peyrard–Bishopi võnked (THz) ning soojuslik avanemine ja denaturatsioon. |
| `debye_length`, `water_permittivity`, `field_penetration_depth` | 0,78 nm varjestus; mikrolained neelduvad mm–cm piires. |
| `short_dipole_radiation_resistance`, `rf_photon_vs_thermal` | DNA on lootusetu RF‑antenn; raadiofootonid on ≪ $k_BT$. |

## Proovi ise

1. Kasuta `debye_length`, et leida soolakontsentratsioon, millel varjestuspikkus jõuaks 1 µm‑ni. Kas elusrakk saaks nii puhtas vees ellu jääda?
2. Muuda `R0_nm` funktsioonis `fret_along_dna` 3 nm‑ks ja 7 nm‑ks. Mitu aluspaari liigub 50 % punkt?
3. Funktsioonis `pb_transfer_integral` kahekordista `D`. Kuidas muutub sidumise temperatuur `pb_denaturation_temperature`‑st? Võrdle `pb_continuum_estimate`‑iga, mis skaleerub kui $\sqrt{kD}$.
4. Inimese genoom ühes rakus on umbes $6{,}4\times10^9$ aluspaari (mõlemad koopiad). Kasuta `RISE_NM`, et leida DNA kogupikkus ühes rakus. Kui see oleks sirge pool‑laine dipool vaakumis, millisele sagedusele oleks see häälestatud ja kui kaugele see sagedus soolases vees reisiks (`field_penetration_depth`)?
5. Leia sagedus, kus `rf_photon_vs_thermal` võrdub 1 kehatemperatuuril. Milline spektri osa see on?

## Viited

- Watson, J. D. & Crick, F. H. C., "Molecular structure of nucleic acids", *Nature* **171**, 737 (1953).
- Franklin, R. E. & Gosling, R. G., "Molecular configuration in sodium thymonucleate", *Nature* **171**, 740 (1953).
- Kraus, J. D., *Antennas*, 2nd ed., McGraw‑Hill (1988). Helical antenna modes.
- Crespo‑Hernández, C. E., Cohen, B. & Kohler, B., "Base stacking controls excited‑state dynamics in A·T DNA", *Nature* **436**, 1141 (2005).
- Cavaluzzi, M. J. & Borer, P. N., "Revised UV extinction coefficients for nucleoside‑5′‑monophosphates and unpaired DNA and RNA", *Nucleic Acids Res.* **32**, e13 (2004).
- Förster, T., "Zwischenmolekulare Energiewanderung und Fluoreszenz", *Ann. Phys.* **437**, 55 (1948).
- Stryer, L. & Haugland, R. P., "Energy transfer: a spectroscopic ruler", *Proc. Natl. Acad. Sci. USA* **58**, 719 (1967).
- Peyrard, M. & Bishop, A. R., "Statistical mechanics of a nonlinear model for DNA denaturation", *Phys. Rev. Lett.* **62**, 2755 (1989).
- Dauxois, T., Peyrard, M. & Bishop, A. R., "Entropy‑driven DNA denaturation", *Phys. Rev. E* **47**, R44 (1993).
- Israelachvili, J. N., *Intermolecular and Surface Forces*, 3rd ed., Academic Press (2011). Debye length.
- Kaatze, U., "Complex permittivity of water as a function of frequency and temperature", *J. Chem. Eng. Data* **34**, 371 (1989).
- Cifra, M. & Pospíšil, P., "Ultra‑weak photon emission from biological samples: definition, mechanisms, properties, detection and applications", *J. Photochem. Photobiol. B* **139**, 2 (2014).
- Pehek, J. O., Kyler, H. J. & Faust, D. L., "Image modulation in corona discharge photography", *Science* **194**, 263 (1976).
- Weaver, I. C. G. et al., "Epigenetic programming by maternal behavior", *Nat. Neurosci.* **7**, 847 (2004).
- ENCODE Project Consortium, "An integrated encyclopedia of DNA elements in the human genome", *Nature* **489**, 57 (2012).
- Graur, D. et al., "On the immortality of television sets: 'function' in the human genome according to the evolution‑free gospel of ENCODE", *Genome Biol. Evol.* **5**, 578 (2013).
