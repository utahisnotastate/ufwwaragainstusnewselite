# 🔬 3. moodul — Teadus loo taga

> [Õppetund](readme.md) on jutustatud aastast 2420. See lehekülg on 2025. aasta reaalsuskontroll: mis on kindlakstehtud, kus loo väide murdub ja mis peaks olema tõsi, et see töötaks. Kõike siin saab kontrollida [laborikoodiga](../../../Module_03_The_Brain_Is_A_Radio/simulation.py).

## 2420. aasta väide ühes lauses

Aju ei tee meelt, vaid võtab seda vastu nagu raadio, mis on häälestatud ülekandele „Aja kanalis“; valgus summutab selle kanali ja kaks samale sagedusele häälestatud aju jagavad mõtteid.

## Tase 1 — Mis on päris

**Ajud toodavad tõepoolest elektrilisi rütme.** Hans Berger salvestas esimese inimese EEG‑i 1920. aastatel. Peanaha elektroodid püüavad umbes 10–100 µV pingeid miljonitelt samm‑sammult tulistavatelt neuronitelt. Rütmid sortitakse tavapärastesse ribadesse (ääred varieeruvad laborite vahel veidi):

| Riba | Sagedus | Tüüpiliselt seotud |
|---|---|---|
| delta | 0.5–4 Hz | sügav uni |
| theta | 4–8 Hz | unisus, mälülesanded |
| alpha | 8–13 Hz | lõdvestunud ärkvelolek, silmad kinni |
| beta | 13–30 Hz | aktiivne mõtlemine, liikumine |
| gamma | 30–80 Hz | lokaalne töötlus, tähelepanu |

**On olemas päris kaja „valgus summutab signaali“.** Berger märkas, et alfa‑rütm kahaneb, kui silmad avad („alfa blokeerimine“). See kahaneb ka vaimse pingutusega, nii et see peegeldab seda, mida aju *teeb*, mitte footonite segamist peidetud kanaliga.

**Maa tõepoolest ümiseb.** Välgulöögid (umbes 50 sekundis maailmas) panavad resonantsi õõnsuse maa ja ionosfääri vahel. Ideaalne, kaotuseta peen kest raadiusega $R_E$ annab moodid

$$f_n = \frac{c}{2\pi R_E}\sqrt{n(n+1)}, \qquad f_1 \approx 10.6\ \text{Hz}.$$

Vaadeldud tipud on umbes 7,8, 14,3, 20,8, 27,3 ja 33,8 Hz, umbes 75–80 % ideaalväärtustest, sest ionosfäär on kaotusega, ebatäiuslik peegel (Schumann ennustas resonantsi 1952; Balser & Wagner vaatlesid seda 1960). Fundamentaal 7,83 Hz istub juhuslikult theta/alfa piiril.

**Aju enda väljad on samuti tillukesed.** Pea väljaspool on aju magnetväli umbes 100 fT–1 pT (magnetoentsefalograafia, MEG). Schumanni magnetväli on samuti suurusjärgus 1 pT. Seetõttu tehakse MEG magnetiliselt varjestatud ruumides.

**Rütmide ja sünkroonia mõõtmine.** Labor rakendab standardtööriistu:

- *Welchi võimsusspekter* $S(f)$: keskmista kattuvate aknastatud segmentide Fourier’ teisenduste ruudud.
- *Riba võimsus*: $P_\text{band} = \int_{f_1}^{f_2} S(f)\,df$. Kõigi sageduste üle summeerides võrdub see signaali dispersiooniga (testid kontrollivad seda).
- *Hetkefaas*: ribapääsfilter, seejärel analüütiline signaal $x(t) + i\,\mathcal{H}[x](t) = A(t)e^{i\phi(t)}$ Hilberti teisenduse kaudu.
- *Faasilukustusväärtus* (Lachaux jt, 1999): $\text{PLV} = \left|\langle e^{i(\phi_1(t) - \phi_2(t))}\rangle_t\right|$, mis on 1 konstantsel faasierinevusel ja lähedal 0‑le mitteseotud faaside korral.

„Aju‑aju sünkroonia“ on päris leid hüperskaneerimise uuringutes, kus kahte inimest salvestatakse korraga. Aga see tekib peamiselt seetõttu, et mõlemad näevad ja kuulevad samu asju samal ajal, mitte seetõttu, et nende vahel liigub signaal (Burgess, 2013).

## Tase 2 — Kus väide murdub

**1. Sageduse sobitamine ei ole haakumine.** 1 pT väli 7,83 Hz juures indutseerib pea‑suuruse aasa (raadius 7,5 cm) ümber

$$\mathcal{E} = \pi r^2 \cdot 2\pi f B \approx 9\times10^{-13}\ \text{V}, \qquad E = \tfrac12 r\,\omega B \approx 2\times10^{-12}\ \text{V/m}.$$

See on umbes $10^{-7}$ 10 µV EEG‑signaalist. Transkraniaalne vahelduvvoolu stimulatsioon, mis suudab aju rütme mõõdetavalt nihutada, paneb ajusse umbes 0,1–1 V/m: umbes $10^{11}$ korda rohkem. „Häälestumine 7,83 Hz‑le“ ei anna mehhanismi, millega Schumanni väli midagi teeks.

**2. Test, mis ei saa ebaõnnestuda.** Levinud viis „näidata“ aju–Maa resonantsi on võrrelda signaali täiusliku 7,83 Hz siinusega. Mis tahes kaks püsivat signaali samal sagedusel omavad konstantset faasierinevust, nii et PLV on 1 *konstruktsioonist*. Labor teeb seda ja saab PLV = 1,000. Seejärel küsib õige küsimuse: kas PLV on suurem kui see, mille saaksid, kui kaks salvestist libistatakse mõne sekundi võrra välja? Puhta siinuse jaoks ei muuda libistamine midagi, nii et surrogaattest tagastab p = 1: üldse mitte tõendeid.

**3. Test, mis saab ebaõnnestuda.** Päris Schumanni väli ei ole täiuslik siinus; välk ajab seda juhuslikult, nii et faas uitab (kvaliteeditegur $Q \approx 4$). Labor simuleerib EEG‑i ja sõltumatut Schumanni magnetomeetri salvestist, seejärel käivitab aja‑nihke surrogaattesti 100 sünteetilisel salvestisel:

| Juhtum | Murdosa p < 0,05 korral |
|---|---|
| Haakumist pole | ≈ 5 % (valepositiivsete määr, mis kalibreeritud testil peaks olema) |
| Nõrk haakumine sisse ehitatud (0,5 % EEG võimsusest) | ≈ 93 % |
| Kaks EEG‑kanalit, mis jagavad üht alfa‑allikat | 100 % |
| Kaks EEG‑kanalit sõltumatute alfa‑allikatega | ≈ 4 % |

Kuna test tuvastab haakumise, kui see tõesti olemas on, tähendab selle „ei“ midagi. See on standard, millest peab läbima iga aju–Schumanni haakumise väide.

**4. Footonisummutus.** Puuduvad avaldatud, korratud tõendid, et valgus summutab mõtteid või et infrapunakaamerad pildistavad „tulpoidseid“ vaimseid vorme. Su kolju sisemus on juba peaaegu pime ja inimesed mõtlevad täiesti hästi eredas päikesevalguses. Silma tundlikkuskõver tuleb võrkkesta fotopigmentide neeldumisspektritest, mida mõõdetakse otse.

**5. Mälu kui otseülekanne minevikust.** See on armas pilt, aga tõendid osutavad kindlalt teisele poole:

- Kahjustused konkreetsetes aju struktuurides eemaldavad konkreetseid võimeid. Patsient H.M. kaotas võime moodustada uusi pikaajalisi mälestusi pärast operatsiooni, mis eemaldas osasid mõlemast hipokampusest (Scoville & Milner, 1957).
- Hiirtel saab õppimise ajal aktiivseid neuroneid märgistada ja hiljem valgusega uuesti aktiveerida, mis käivitab mälestuse (Liu jt, 2012).
- Mälestusi *rekonstrueeritakse* ja need võivad muutuda: küsimuse sõnastus muudab seda, mida inimesed hiljem teatavad näinud olevat (Loftus & Palmer, 1974). Otseülekanne minevikust ei oleks küsimuse poolt redigeeritud.

Koduülesande raadioanaloogia („laul on endiselt õhus“) teeb testitava ennustuse: mõni teine vastuvõtja peaks suutma sinu laulu mängida. Sellist vastuvõtjat ei ole kunagi leitud.

**6. Kvantaju (Orch‑OR).** Hameroff ja Penrose pakkusid, et kvantsuperpositsioonid mikrotuubulites neuronite sees varisevad umbes 25 ms ajaskaaladel ja et see on seotud teadvusega. See on päris, avaldatud ja vaidlustatud hüpotees. Peamine vastuväide on ajastus: Tegmark (2000) hindas, et sellised superpositsioonid dekoheeruvad $10^{-13}$ s või vähem. Labor arvutab lõhe:

| Neuraalne ajaskaala | vs Tegmarki $10^{-13}$ s | vs vastulause hinnang $10^{-4}$ s (Hagan jt, 2002) |
|---|---|---|
| aktsioonipotentsiaal, 1 ms | $10^{10}$ | $10^{1}$ |
| gamma‑tsükkel, 25 ms | $10^{11}$ | $10^{2.4}$ |

Isegi kõige soodsam avaldatud hinnang jääb lühikeseks. Orch‑OR ei teeks aju ka *vastuvõtjaks*; see on endiselt teooria ajuprotsessist, mis toodab meelt.

## Tase 3 — Mis peaks olema tõsi

Selleks et aju oleks Schumannile häälestatud vastuvõtja, peaksid need ilmuma. Igaüks on selge katse:

- **Haakumine, mis läbib surrogaattesti.** Salvesta EEG koos kohaliku magnetomeetriga. Eelregistreeritud analüüs peaks leidma nendevahelise PLV üle aja‑nihke surrogaatnulli, korduvalt sõltumatutes laborites.
- **Haakumine, mis kaob, kui väli eemaldatakse.** Korda magnetiliselt varjestatud ruumis, mis lõikab 1 pT välja suurusjärkude võrra. Kui „haakumine“ jääb, ei tule see Schumanni väljast.
- **Mehhanism õige suurusega.** Midagi neuraalkoel peaks vastama väljadele umbes $10^{11}$ korda nõrgematele kui need, mis teadaolevalt seda mõjutavad, ja üle soojusmüra.
- **„Footonisummutuse“ jaoks:** korratud, pimestatud katse, milles mõni vaimne nähtus ilmub pimeduses ja kaob valguses, kus ainus muudetud asi on valgustase.

Päris avatud küsimused jäävad. Kuidas teadvus tekib aju aktiivsusest („raske probleem“) on lahendamata. Kas kvantefektidel on bioloogias mingi funktsionaalne roll, uuritakse aktiivselt. Gravitatsiooniga seotud lainefunktsiooni varisemist, millest Orch‑OR sõltub, testitakse; maa‑alune katse välistas Diósi–Penrose’i mudeli lihtsaima parameetriteta versiooni (Donadi jt, 2021).

## Käivita labor

```bash
python Module_03_The_Brain_Is_A_Radio/simulation.py
python Module_03_The_Brain_Is_A_Radio/simulation.py --data my_eeg.csv --fs 160 --channels 0 1
python -m pytest tests/test_module_03.py
```

| Katse | Mida see näitab |
|---|---|
| `schumann_frequency` | Ideaalõõnsuse moodid (10,6, 18,3, … Hz) vs vaadeldud 7,83, 14,3, … Hz. |
| `field_budget`, `induced_emf`, `induced_e_field` | Schumanni väli on aju enda suuruses väljaspool pead, aga indutseerib ~10⁻¹² V/m selle sees. |
| `pink_noise`, `synthetic_eeg_pair`, `schumann_record` | Sünteetiline EEG (1/f taust pluss alfa‑pursked) ja uitava faasiga Schumanni jälg. |
| `welch_psd`, `band_power`, `spectral_slope` | Standardne EEG spektraalanalüüs. |
| `plv`, `shift_surrogate_test`, `detection_rate` | Faasilukustus, siinus‑vs‑siinus lõks ja kalibreeritud test mõõdetud valepositiivsete määra ning võimsusega. |
| `decoherence_gap` | Orch‑OR‑i ajastusprobleem suurusjärkudes. |
| `load_user_eeg` | Valikuline: sinu enda salvestis `.csv` või `.npy` (proovid × kanalid). Võrku ei kasutata. |

## Proovi ise

1. Päris andmed: laadi alla mõned käigud PhysioNet EEG Motor Movement/Imagery andmestikust (109 vabatahtlikku, 64 kanalit, 160 Hz, EDF‑vorming). Teisenda kaks kanalit CSV‑ks (näiteks MNE‑Pythoni teegiga) ja käivita labor `--data`‑ga. Võrdle silmad‑avatud ja silmad‑suletud baasjoone käike: kas alfa‑võimsus muutub nagu Berger leidis?
2. Oma andmetega arvuta PLV kahe *naaber*elektroodi ja kahe *kauge* elektroodi vahel. Miks on naabrid peaaegu alati „oluliselt lukustatud“? (Vihje: mahujuhtivus, kus üks allikas jõuab mõlema elektroodini.)
3. Rakenda faasijuhuslikustatud surrogaat (hoia ühe kanali Fourier’ amplituudid, juhuslikusta faasid) ja kasuta seda täiusliku 7,83 Hz siinusviite vastu. Näita, et seeki ei suuda eristada püsivat 7,83 Hz rütmi päris sünkroniseerimisest. Milline viite omadus paneb iga surrogaatmeetodi ebaõnnestuma?
4. Alanda `COUPLING_DEMO`, kuni `detection_rate` langeb umbes 50 %‑ni. Kuidas see võimsus muutub, kui kahekordistad salvestusaja?
5. Kasuta `induced_e_field`, et leida magnetväli 7,83 Hz juures, mis indutseeriks peas 0,1 V/m. Kuidas see võrdub MRI‑skanneri väljaga (mõned teslad, aga staatiline)?

## Viited

- Berger, H., "Über das Elektrenkephalogramm des Menschen", *Archiv für Psychiatrie und Nervenkrankheiten* **87**, 527 (1929).
- Schumann, W. O., "Über die strahlungslosen Eigenschwingungen einer leitenden Kugel, die von einer Luftschicht und einer Ionosphärenhülle umgeben ist", *Z. Naturforsch. A* **7**, 149 (1952).
- Balser, M. & Wagner, C. A., "Observations of Earth–ionosphere cavity resonances", *Nature* **188**, 638 (1960).
- Nickolaenko, A. P. & Hayakawa, M., *Resonances in the Earth–Ionosphere Cavity*, Kluwer (2002).
- Hämäläinen, M., Hari, R., Ilmoniemi, R. J., Knuutila, J. & Lounasmaa, O. V., "Magnetoencephalography — theory, instrumentation, and applications to noninvasive studies of the working human brain", *Rev. Mod. Phys.* **65**, 413 (1993).
- Lachaux, J.‑P., Rodriguez, E., Martinerie, J. & Varela, F. J., "Measuring phase synchrony in brain signals", *Hum. Brain Mapp.* **8**, 194 (1999).
- Theiler, J., Eubank, S., Longtin, A., Galdrikian, B. & Farmer, J. D., "Testing for nonlinearity in time series: the method of surrogate data", *Physica D* **58**, 77 (1992).
- Burgess, A. P., "On the interpretation of synchronization in EEG hyperscanning studies: a cautionary note", *Front. Hum. Neurosci.* **7**, 881 (2013).
- Schalk, G., McFarland, D. J., Hinterberger, T., Birbaumer, N. & Wolpaw, J. R., "BCI2000: a general‑purpose brain‑computer interface (BCI) system", *IEEE Trans. Biomed. Eng.* **51**(6), 1034 (2004). Source of the PhysioNet EEG Motor Movement/Imagery dataset.
- Goldberger, A. L. et al., "PhysioBank, PhysioToolkit, and PhysioNet", *Circulation* **101**(23), e215 (2000).
- Scoville, W. B. & Milner, B., "Loss of recent memory after bilateral hippocampal lesions", *J. Neurol. Neurosurg. Psychiatry* **20**, 11 (1957).
- Liu, X. et al., "Optogenetic stimulation of a hippocampal engram activates fear memory recall", *Nature* **484**, 381 (2012).
- Loftus, E. F. & Palmer, J. C., "Reconstruction of automobile destruction: an example of the interaction between language and memory", *J. Verbal Learn. Verbal Behav.* **13**, 585 (1974).
- Hameroff, S. & Penrose, R., "Orchestrated reduction of quantum coherence in brain microtubules: a model for consciousness", *Math. Comput. Simul.* **40**, 453 (1996).
- Hameroff, S. & Penrose, R., "Consciousness in the universe: a review of the 'Orch OR' theory", *Phys. Life Rev.* **11**, 39 (2014).
- Tegmark, M., "Importance of quantum decoherence in brain processes", *Phys. Rev. E* **61**, 4194 (2000).
- Hagan, S., Hameroff, S. R. & Tuszyński, J. A., "Quantum computation in brain microtubules: decoherence and biological feasibility", *Phys. Rev. E* **65**, 061901 (2002).
- Donadi, S. et al., "Underground test of gravity‑related wave function collapse", *Nat. Phys.* **17**, 74 (2021).
