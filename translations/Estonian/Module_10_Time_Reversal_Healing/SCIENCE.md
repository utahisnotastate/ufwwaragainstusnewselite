# 🔬 10. moodul — Teadus loo taga

> [Õppetund](readme.md) on jutustatud aastast 2420. See lehekülg on 2025. aasta reaalsuskontroll: mis on kindlakstehtud, kus loo väide murdub ja mis peaks olema tõsi, et see töötaks. Kõike siin saab kontrollida [laborikoodiga](../../../Module_10_Time_Reversal_Healing/simulation.py).

> ⚕️ **Tervisemärkus.** Midagi selles õppetunnis ei ole meditsiiniline nõuanne ega ravi. Ajatagasipööramise ravi tänapäeval ei eksisteeri. Kui oled haige või vigastatud, palun pöördu arsti poole; kirurgia ja ravimid päästavad elusid.

## 2420. aasta väide ühes lauses

„Faaskonjugaatpeegel“ saab salvestada haige või vananenud keha moonutatud „laine“, saata selle ajas tagasipööratuna tagasi ja nii tühistada kahju, taastades keha varasema, terve oleku.

## Tase 1 — Mis on päris

**Faaskonjugatsioon on päris optika.** 1972. aastal näitasid Zel'dovich ja kaastöötajad, et stimuleeritud Brillouini hajumisega peegeldunud valgus tuleb tagasi pööratud laine­frondiga: kiir, mis oli sisse tulles segamini aetud, harutatakse välja tulles lahti. Varsti pärast seda näitasid Hellwarth ja Yariv sama asja degeneerunud neljalainelise segamisega $\chi^{(3)}$ (Kerr‑tüüpi) mittelineaarses materjalis. Kui sissetulev väli on

$$E(\mathbf r, t) = \mathrm{Re}\big[A(\mathbf r)\,e^{i(kz-\omega t)}\big],$$

tagastab faaskonjugaatpeegel $A^*(\mathbf r)\,e^{i(-kz-\omega t)}$. Monokromaatse laine jaoks on see täpselt ajas tagasipööratud laine: iga kiir jälgib oma rada tagasi.

**Miks see moonutuse tühistab.** Peen aberreeriv kiht korrutab välja $e^{i\phi(x)}$‑ga. Pärast faaskonjugatsiooni kannab väli $e^{-i\phi(x)}$ ja sama kihi uuesti ületamine annab $e^{-i\phi}e^{+i\phi} = 1$. Vabaruumi levik on unitaarne, nii et see tühistatakse samamoodi. Labor saadab kiire läbi 2‑radiaanilise juhusliku faasiekraani ja tagasi: konjugaatpeegel tagastab algse kiire fideliidsusega $1{,}000000$, samas kui tavaline peegel tagastab fideliidsuse $0{,}0025$.

**Fokusseerimine läbi koe on päris uurimisvaldkond.** Bioloogiline kude hajutab valgust palju kordi. Yaqoob jt (2008) kasutasid optilist faaskonjugatsiooni, et tühistada hajumine läbi kanarindkoe lõikude („turbiditeedi summutamine“). Vellekoop ja Mosk (2007) fokusseerisid valgust *läbi* läbipaistmatu kihi, häälestades sisendkiire $N$ segmendi faase. Täielikult arenenud spekli jaoks on oodatav heleduse võit

$$\eta = \frac{\pi}{4}(N-1) + 1.$$

Labor taastoodab selle seaduse juhuslike ülekandemaatriksitega (näiteks $N = 1024$ annab $805$ ennustatud $804{,}5$ vastu). Neid meetodeid arendatakse kujutamiseks ja valguse kohaletoimetamiseks sügavale koesse.

**Bioelekter on päris, mõõdetav füüsika.** Iga rakk hoiab pinget üle oma membraani. Ühe iooniliigi jaoks on tasakaalu (Nernsti) potentsiaal

$$E_\text{ion} = \frac{RT}{zF}\ln\frac{[\text{ion}]_\text{out}}{[\text{ion}]_\text{in}},$$

mis annab $E_K = -89$ mV 37 °C juures $[K]_o = 5$ mM, $[K]_i = 140$ mM jaoks. Mitme iooniga seab puhkepinge Goldman–Hodgkin–Katzi võrrand:

$$V_m = \frac{RT}{F}\ln\frac{P_K[K]_o + P_{Na}[Na]_o + P_{Cl}[Cl]_i}{P_K[K]_i + P_{Na}[Na]_i + P_{Cl}[Cl]_o}.$$

Õpiku imetajaväärtustega saab labor $-67$ mV. Michael Levini rühm ja teised uurivad, kuidas nende pingete mustrid aitavad juhtida embrüonaalset arengut ja regeneratsiooni loomadel nagu konnad ja lamedad ussid (Levin, 2021). See on aktiivne põhiuuring, mitte teraapia.

**Elu alandab oma entroopiat kogu aeg, legaalselt.** Puhkav inimene vabastab umbes 100 W soojust. Päevas lahkub kehast 310 K juures $8{,}6\times10^6$ J, kandes välja $Q/T_\text{body} \approx 27\,900$ J/K entroopiat, ja siseneb 293 K ruumi kui $Q/T_\text{room} \approx 29\,500$ J/K. Rakud parandavad DNA‑d, asendavad valke ja ravivad haavu, makstes lokaalse korra eest suurema entroopiaekspordiga. Teine seadus kehtib kehale pluss ümbrusele.

## Tase 2 — Kus väide murdub

**1. Faaskonjugaatpeegel pöörab laine, mitte ainet.** Ülalolev tühistamine töötab, sest *sama* kihti ületatakse kaks korda. See pöörab valgusvälja; see ei pööra aatomeid, millest valgus läbi läks. Keha ei ole peegeldamiseks laine: selle rakud, valgud ja DNA on aine, millele loo peegel kunagi ei mõju.

**2. Keskkond ei tohi käikude vahel muutuda.** Kui aberreeriv kiht muutub, ei tühista tagasitee enam esimest. Gaussi faasiekraanide jaoks rms‑faasiga $\sigma$ ja korrelatsiooniga $\rho$ käikude vahel on fideliidsus

$$F = e^{-2\sigma^2(1-\rho)}.$$

Labor mõõdab $F = 0{,}92$ juures $\rho = 0{,}99$, $0{,}44$ juures $\rho = 0{,}9$ ja umbes $0$ juures $\rho = 0{,}5$ (teooria $0{,}92$, $0{,}45$, $0{,}02$). Eluskude korraldab end pidevalt ümber ja in‑vivo optilised katsed peavad korrigeerima lühikeste akende jooksul (tüüpiliselt millisekundid). Lugu tahab „pöörata“ muutusi, mis on kogunenud *aastakümnete* jooksul, kui $\rho \approx 0$ ja fideliidsus on null. Hajutava koe mudelis annab enne koe liikumist õpitud korrektsioon võidu $0{,}92$: mitte parem kui korrektsiooni üldse mitte.

**3. Peegel peab püüdma kogu välja.** Labor näitab täpset tulemust: muutumatu keskkonna korral võrdub fideliidsus võimsuse murdosaga, mille peegel kinni püüab (erinevus alla $10^{-15}$). Mis iganes põgeneb, on igaveseks kadunud. Ainult 1 cm² koe valguse kontrollimiseks 800 nm juures vajaksid umbes $6\times10^{8}$ sõltumatut moodi. Miski loos ei selgita, kuidas püüda iga molekuli „laine“ kehas.

**4. Puudub „noor muster“, mis on salvestatud „Aja kanalisse“.** Füüsikal puudub salvestis keha mineviku olekust, mida ootaks taasesitus. Info selle kohta, kuidas su rakud olid 20‑aastaselt paigutatud, on hajutatud keskkonda soojusena, sama entroopiaeksport nagu ülal. Energia ei ole piir (100 W võiks põhimõtteliselt maksta umbes $3\times10^{22}$ biti kustutamise eest sekundis Landaueri piiril $kT\ln 2$). Puudu on info ja mehhanism, mis mõjuks igale molekulile.

**5. „Priore masin“.** Antoine Priore ehitas Prantsusmaal 1960.–70. aastatel elektromagnetseadmeid ja teatas mõjudest kasvajatele ja nakkustele loomadel. Tulemusi ei korratud ega valideeritud sõltumatult ning seadmed ei ole aktsepteeritud ravi.

**6. Kirurgia ja meditsiin ei ole „arvuti haamriga löömine“.** Moodne meditsiin on tugevalt ehitatud füüsikale ja keemiale ning see töötab: vaktsiinid, antibiootikumid, anesteesia ja kirurgia päästavad palju miljoneid elusid. Õppetunni vastandus on osa fiktsioonist.

## Tase 3 — Mis peaks olema tõsi

Selleks et „ajatagasipööramise ravi“ eksisteeriks, peaksid kõik need kehtima. Igaüks on konkreetne sihtmärk:

- **Füüsikaline kandja keha olekule**, mida saab „peegeldada“. Test: näita, et mõni väli väljaspool keha kodeerib koe struktuuri rakulise eraldusvõimega ja seda saab mõõta.
- **Salvestatud mineviku oleku salvestis.** Test: taasta kontrollitav varasem olek (näiteks vana armi muster) tänasest mõõtmisest, ilma varasemate fotode või proovideta.
- **Mehhanism, mis muudab tagastatud laine ümberkorraldatud molekulideks**, viisidel, mis sobivad teadaoleva keemiaga ega küpseta kude.
- **Koherentsus ajas.** Mis tahes „pööramine“ peaks töötama, kuigi keha muutub millisekundite‑kuni‑aastate ajaskaaladel, mis hävitab konjugatsioonifideliidsuse nagu ülal näidatud.

**Päris avatud küsimused, mis on loo vaimule lähemal:**

- Kui kaugele saavad laine­frondi kujundamine ja optiline faaskonjugatsioon lükata fokusseerimist, kujutamist ja valguse kohaletoimetamist sügavale eluskude?
- Kas bioelektrilisi signaale saab kasutada regeneratsiooni juhtimiseks loomadel ja hiljem ohutult inimestel? (Varajane uuring; heakskiidetud teraapiaid pole.)
- Mis seab keha enda parandamise piirid ja kas bioloogia (näiteks tüviraku‑ ja regeneratiivmeditsiin) saab seda laiendada?

## Käivita labor

```bash
python Module_10_Time_Reversal_Healing/simulation.py
python -m pytest tests/test_module_10.py
```

| Katse | Mida see näitab |
|---|---|
| `round_trip` | Faaskonjugatsioon tühistab juhusliku aberratsiooni täpselt; tavaline peegel mitte. |
| `round_trip(rho=...)`, `decorrelation_fidelity_theory` | Kui keskkond muutub käikude vahel, langeb fideliidsus kui $e^{-2\sigma^2(1-\rho)}$. |
| `round_trip(aperture=...)` | Fideliidsus võrdub välja murdosaga, mille peegel püüab. |
| `wavefront_shaping_enhancement`, `vellekoop_mosk_theory` | Fokusseerimine läbi hajutava meediumi järgib $\tfrac{\pi}{4}(N-1)+1$ ja kaob, kui meedium muutub. |
| `nernst`, `ghk_voltage` | Päris membraanipinged ioonkontsentratsioonidest (umbes $-67$ mV puhkeolekus). |
| `entropy_budget`, `landauer_bits_per_second` | Elu alandab lokaalset entroopiat, eksportides rohkem; teine seadus kehtib üldiselt. |

## Proovi ise

1. Funktsioonis `round_trip` tõsta `rms_rad` 2‑st 4‑ks. Kui palju aeglasemalt saab meedium muutuda (kui lähedal 1‑le peab $\rho$ olema), et hoida 90 % fideliidsust? Kontrolli $e^{-2\sigma^2(1-\rho)}$ vastu.
2. Kasuta `with_changes`, et leida ekstratsellulaarne kaaliumitase, millel puhkepinge jõuab $-55$ mV‑ni. (Arstid jälgivad vere kaaliumi just seetõttu.)
3. Käivita `wavefront_shaping_enhancement` meediumiga, mis muutub ainult *osaliselt*: sega vana ja uus ülekandemaatriks kui $\sqrt{\rho}\,t_\text{old} + \sqrt{1-\rho}\,t_\text{new}$. Kuidas võit langeb $\rho$‑ga?
4. Tee `entropy_budget` uuesti ruumi jaoks 35 °C juures. Mis juhtub neto entroopiaproduktsiooniga ja miks raskendavad kuumad keskkonnad soojuse eraldamist?

## Viited

- Zel'dovich, B. Ya., Popovichev, V. I., Ragul'skii, V. V. & Faizullov, F. S., "Connection between the wave fronts of the reflected and exciting light in stimulated Mandel'shtam‑Brillouin scattering", *JETP Lett.* **15**, 109 (1972).
- Hellwarth, R. W., "Generation of time‑reversed wave fronts by nonlinear refraction", *J. Opt. Soc. Am.* **67**, 1 (1977).
- Yariv, A., "Phase conjugate optics and real‑time holography", *IEEE J. Quantum Electron.* **14**, 650 (1978).
- Vellekoop, I. M. & Mosk, A. P., "Focusing coherent light through opaque strongly scattering media", *Opt. Lett.* **32**, 2309 (2007).
- Yaqoob, Z., Psaltis, D., Feld, M. S. & Yang, C., "Optical phase conjugation for turbidity suppression in biological samples", *Nature Photonics* **2**, 110 (2008).
- Goldman, D. E., "Potential, impedance, and rectification in membranes", *J. Gen. Physiol.* **27**, 37 (1943).
- Hodgkin, A. L. & Katz, B., "The effect of sodium ions on the electrical activity of the giant axon of the squid", *J. Physiol.* **108**, 37 (1949).
- Levin, M., "Bioelectric signaling: Reprogrammable circuits underlying embryogenesis, regeneration, and cancer", *Cell* **184**, 1971 (2021).
- Landauer, R., "Irreversibility and heat generation in the computing process", *IBM J. Res. Dev.* **5**, 183 (1961).
