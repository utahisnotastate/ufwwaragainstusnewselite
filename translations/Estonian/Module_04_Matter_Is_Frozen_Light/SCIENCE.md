# 🔬 4. moodul — Teadus loo taga

> [Õppetund](readme.md) on jutustatud aastast 2420. See lehekülg on 2025. aasta reaalsuskontroll: mis on kindlakstehtud, kus loo väide murdub ja mis peaks olema tõsi, et see töötaks. Kõike siin saab kontrollida [laborikoodiga](../../../Module_04_Matter_Is_Frozen_Light/simulation.py).

## 2420. aasta väide ühes lauses

Aine on valgus, mis on lõksus tillukeses pöörlevas silmuses (toruses), nii et elektron on ringis jooksev footon ja mass on lihtsalt „külmunud valgus“.

## Tase 1 — Mis on päris

**Mass ja energia on tõepoolest sama valuuta.** Einsteini $E = mc^2$ (1905) on üks füüsika kõige paremini testitud võrrandeid. Kui energia lahkub süsteemist, lahkub mass koos sellega:

| Protsess | Vabanenud energia | Kaduv mass |
|---|---|---|
| 1 kg kuiva puidu põletamine | $1.6\times10^{7}$ J | $1.8\times10^{-7}$ g ($2\times10^{-10}$ puidust) |
| 15‑kilotonnine lõhestuspomm | $6.3\times10^{13}$ J | 0.7 g |

Nii et õppetunni „palki põletades harutad sõlmi“ sisaldab midagi tõest: tuhk ja gaasid on tõepoolest kergemad $\Delta m = E/c^2$ võrra. Aga aatomid on kõik endiselt olemas. Ainult murdosa $10^{-10}$ massist läheb.

**Suurem osa sinu massist on tõepoolest energia, lihtsalt mitte valgus.** Prooton kaalub 938,27 MeV/c². Selle kolme valentskvargi puhkemassid (üles, üles, alla; umbes 2,2 + 2,2 + 4,7 MeV Particle Data Groupi skeemis) annavad kokku ainult umbes **1 %** sellest. Ülejäänu on kvarkide energia, mis liiguvad peaaegu valguse kiirusel, ja gluuonivälja energia, mis neid seob, kirjeldatud kvantkromodünaamika (QCD) abil. Võre‑QCD arvutab hadronite masse sellest mõne protsendi täpsusega (Dürr jt, 2008). Arvestades ka virtuaalsete „mere“ kvarkide (sealhulgas veidrate kvarkide) kvargimassi panust, tõuseb kvargimassi osa umbes 10 %‑ni, endiselt väike osa. Selles mõttes on „mass on peamiselt väljaenergia“ päris füüsika ja see on sügavam väide kui lugu teeb.

**Aine muutub tõepoolest valguseks ja valgus aineks.**

- *Aine → valgus.* Elektron ja positron annihileeruvad kaheks 511 keV footoniks. Haigla PET‑skannerid tuvastavad just neid footonipaare iga päev.
- *Valgus → aine.* Breit ja Wheeler (1934) arvutasid, et kaks footonit võivad teha elektron–positron paari, kui neil on koos piisavalt energiat. Energiatega $E_1, E_2$, mis kohtuvad nurga $\theta$ all, peab invariant $s = 2E_1E_2(1-\cos\theta)$ jõudma $(2m_ec^2)^2$:

$$E_1E_2(1-\cos\theta) \;\ge\; 2(m_ec^2)^2.$$

Pealtkokkupõrkel on kaks 511 keV footonit täpselt lävel. Üle selle on ristlõige

$$\sigma_{\gamma\gamma} = \frac{\pi r_e^2}{2}(1-\beta^2)\left[(3-\beta^4)\ln\frac{1+\beta}{1-\beta} - 2\beta(2-\beta^2)\right], \qquad \beta = \sqrt{1 - \frac{4m_e^2c^4}{s}},$$

kus $r_e$ on klassikaline elektroni raadius ja $\beta$ on iga leptoni kiirus massikeskme taustsüsteemis. See tipneb $1.70\times10^{-25}$ cm² $\approx 0.256\,\sigma_T$ lähedal $\beta = 0.70$. Labor kontrollib valemit sõltumatult: selle ülesehitamine Dirac’i (1930) pöördprotsessi $e^+e^-\to\gamma\gamma$ valemist, kasutades detailset tasakaalu $\sigma_{\gamma\gamma} = 2\beta^2\sigma_\text{ann}$, nõustub $10^{-13}$ täpsusega.

**Katsed.** SLAC eksperiment E‑144 (Burke jt, 1997) tagasihajutas 527 nm laserit 46,6 GeV elektronidelt, et teha gammakiiri kuni 29,2 GeV, mis seejärel põrkasid sama intensiivse laseriga. Kinemaatika üksi ütleb, et vähemalt 4 laserfootonit tuli korraga neelata, nii et see oli *mittelineaarne, mitmefotoonne* Breit–Wheeler. STAR RHIC‑is (Adam jt, 2021) nägi $e^+e^-$ paare kuldtuumade lähedalt möödumise intensiivsetest elektromagnetväljadest, mis toimivad *kvaasi‑päris* footonite pilvedena. Kahe päris footonite kiire puhas kokkupõrge ei ole veel tehtud; ettepanekud on olemas (Pike jt, 2014).

**Paaride välja tõmbamine vaakumist.** Piisavalt tugev elektriväli saab paare otse luua. Skaala on see, kus väli annab elektronile selle puhkeenergia ühe Compton’i pikkuse jooksul (Sauter, Heisenberg–Euler, Schwinger):

$$E_\text{crit} = \frac{m_e^2c^3}{e\hbar} \approx 1.32\times10^{18}\ \text{V/m}, \qquad I_\text{crit} \approx 2.3\times10^{29}\ \text{W/cm}^2.$$

## Tase 2 — Kus väide murdub

**1. „Elektron on ringis jooksev footon“ saab oma ainsa edu tasuta.** Mudel (Williamson & van der Mark, 1997) asetab laengu $e$, mis liigub kiirusel $c$, silmusele raadiusega $r = \hbar/(m_ec) = 3.86\times10^{-13}$ m, redutseeritud Compton’i lainepikkus. Ringlev laeng omab magnetmomenti

$$\mu = I\cdot\pi r^2 = \frac{ec}{2\pi r}\,\pi r^2 = \frac{ecr}{2} = \frac{e\hbar}{2m_e} = \mu_B,$$

täpselt Bohri magneton. Aga $r$ valiti $m_e$‑st ja $\mu_B$ on *defineeritud* kui $e\hbar/2m_e$, nii et see on algebraline identiteet. Labor näitab, et sama retsept annab „õige magnetoni“ mis tahes massi jaoks, mille valid. See ei saa ebaõnnestuda, seega ei ennusta midagi.

**2. See jätab vahele selle, mida elektron tegelikult teeb.** Mõõdetud moment ei ole $\mu_B$, vaid $1.00115965218059\,\mu_B$ (Fan jt, 2023). Kvant‑elektrodünaamika ennustab selle lisatud 0,116 %:

$$a_e = \frac{g-2}{2} = \frac{1}{2}\frac{\alpha}{\pi} - 0.3285\left(\frac{\alpha}{\pi}\right)^2 + 1.1812\left(\frac{\alpha}{\pi}\right)^3 - 1.9122\left(\frac{\alpha}{\pi}\right)^4 + \dots$$

Labor kasutab $\alpha$‑d rubiidiumi aatomi‑tagasilöögi mõõtmistest (Morel jt, 2020), mis ei sõltu $g-2$‑st, nii et võrdlus ei ole ringikujuline:

| Mudel | ennustatud $g/2$ | kõrvalekalle |
|---|---|---|
| footonisilmus | 1 (täpselt) | $1.2\times10^{-3}$ |
| QED, 1 silmus (Schwingeri $\alpha/2\pi$) | 1.0011614 | $1.8\times10^{-6}$ |
| QED, 2 silmust | 1.001159637 | $1.5\times10^{-8}$ |
| QED, 3 silmust | 1.00115965223 | $5\times10^{-11}$ |
| QED, 4 silmust | 1.00115965218 | $5\times10^{-12}$ |

Järelejäänud $5\times10^{-12}$ on oodatav suurus terminitele, mida labor välja jätab (viiesilmuseline QED, raskemate müüonite ja tau’de silmused, hadroonilised ja nõrgad efektid). QED on umbes $10^{8}$ korda lähemal kui silmusmudel.

**3. Elektron on palju väiksem kui silmus.** Kõrgeenergia elektron–positron hajumine LEP‑is ei näita elektroni struktuuri märki alla umbes $10^{-18}$ m. Mudeli silmus on $4\times10^{5}$ korda suurem. Nii suur struktuur muudaks elektronide hajumist energiatel, mida sondeeriti aastakümneid tagasi.

**4. Muud asjad, mida mudel peab seletama, aga ei seleta.** Footonil puudub laeng, kust tuleb siis elektroni laeng $-e$? Footonil on spinn 1; elektronil spinn ½. Müüonil ja tau’l on täpselt sama laeng kui elektronil, aga erinevad massid. Ja ühel footonil, ükskõik kui energeetiline, on $s = 0$ ja see ei saa kunagi iseenesest massiivseks osakeseks; midagi muud (tuum, teine footon, tugev väli) on alati vaja. Valgus ei paindu ka iseenesest suletud silmuseks.

**5. Valgus ei ole praktiline aine allikas.** Kaks 2 eV päikesevalguse footonit jäävad paari lävest lühikeseks teguriga $6.5\times10^{10}$ $s$‑is; päikesevalguse footon vajaks partneriks 131 GeV gammakiirt. Paaride rebimine vaakumist väljaga on kontrollitud teguriga $e^{-\pi E_\text{crit}/E}$. Kõige intensiivsem laser seni, umbes $1.1\times10^{23}$ W/cm² (Yoon jt, 2021), jõuab $9\times10^{14}$ V/m $= 7\times10^{-4}\,E_\text{crit}$, andes teguri umbes $10^{-1983}$. (Päris laserimpulsid võnguvad ja on fokusseeritud, nii et täpne määr erineb, aga jääb täielikult tühiseks.)

**6. Miks asjad tunduvad tahked.** Mitte pöörleva valguse pärast. Aine on stabiilne ja kokkusurumatu, sest elektronid on fermionid: Pauli välistusprintsiip koos elektrostaatikaga hoiab aatomeid üksteisesse kokkuvarisemast (Dyson & Lenard, 1967; Lieb, 1976). Laeventilaatori pilt on kena, aga päris mehhanism on kvantstatistika.

## Tase 3 — Mis peaks olema tõsi

„Külmunud valguse“ elektroni mudel peaks läbima kõik need testid, millest igaühel on täpne mõõdetud sihtmärk:

- **Ennusta $a_e = 0.00115965218\ldots$** ilma sellele sobitatud parameetrita, nagu QED teeb $\alpha$‑st üksi.
- **Selgita laengut, spinni ½ ja kolme põlvkonda** (elektron, müüon, tau) ühe mehhanismiga ning ennusta nende massisuheteid (206,77 ja 3477,2). Standardmudel neid masse ka ei ennusta; need on avatud küsimus, nii et mudel, mis seda teeks, oleks suur avastus.
- **Näita struktuuri ~$10^{-13}$ m juures** elektronhajumises („vormitegur“). Praegused andmed välistavad selle rohkem kui viie suurusjärgu võrra.

Lähedased päris avatud küsimused: kahe päris footonite kiire esimene kokkupõrge üle Breit–Wheeleri läve; katsed, mis lähenevad Schwingeri väljale elektroni enda puhkesüsteemis (tugevavälja QED laserite ja kõrgeenergia elektronkiirtega); ja miks Higgsi haakumistel ning seega kvarkide ja leptonite massidel on need väärtused, mis neil on.

## Käivita labor

```bash
python Module_04_Matter_Is_Frozen_Light/simulation.py
python -m pytest tests/test_module_04.py
```

| Katse | Mida see näitab |
|---|---|
| `mass_defect`, `proton_valence_quark_fraction` | $E = mc^2$ keemilistel ja tuumaskaaladel; kvarkide puhkemassid on ~1 % prootonist. |
| `breit_wheeler_threshold`, `pair_beta`, `breit_wheeler_cross_section` | Valgus aineks: lävi ja ristlõige. |
| `breit_wheeler_from_annihilation`, `dirac_annihilation_cross_section` | Ristlõike sõltumatu kontroll detailse tasakaalu abil. |
| `compton_edge`, `min_laser_photons` | Miks SLAC E‑144 oli mitmefotoonne protsess. |
| `schwinger_field`, `schwinger_suppression_log10` | Kui kaugel on tänased laserid paaride rebimisest vaakumist. |
| `loop_magnetic_moment`, `toroidal_model_moment`, `qed_anomaly` | Footonisilmuse mudeli sisse ehitatud „edu“ ja selle möödalaskmine versus QED. |

## Proovi ise

1. Kui energeetiline peab gammakiir olema, et teha paare kosmilisel mikrolaine taustal (tüüpiline footonienergia umbes $6\times10^{-4}$ eV)? Seetõttu on Universum läbipaistmatu kõrgeima energia gammakiirtele.
2. Kasuta `toroidal_model_moment` müüoni massiga ja võrdle mõõdetud müüoni anomaaliaga $a_\mu \approx 0.00116592$. Kas silmusmudel teeb müüoni jaoks midagi paremini?
3. Arvuta 30 kg lapse puhkeenergia `mass_defect`‑iga vastupidi ($E = mc^2$). Mitu 15‑kilotonnist pommi see on? Miks midagi sellist kunagi iseenesest ei juhtu? (Vihje: millised säilivad suurused peaksid kaduma?)
4. Joonista `breit_wheeler_cross_section` vastu $s/(2m_ec^2)^2$ ja kontrolli kõrgeenergia vormi $\sigma \approx \frac{4\pi r_e^2 m_e^2c^4}{s}\left[\ln\frac{s}{m_e^2c^4} - 1\right]$.
5. Asenda `ALPHA_RB` tseesiumi väärtusega $\alpha^{-1} = 137.035999046$ (Parker jt, 2018). Kui palju liigub 4‑silmuseline ennustus võrreldes mõõtemääramatusega $1.3\times10^{-13}$ $g/2$‑s?

## Viited

- Einstein, A., "Ist die Trägheit eines Körpers von seinem Energieinhalt abhängig?", *Ann. Phys.* **18**, 639 (1905).
- Breit, G. & Wheeler, J. A., "Collision of two light quanta", *Phys. Rev.* **46**, 1087 (1934).
- Dirac, P. A. M., "On the annihilation of electrons and protons", *Proc. Camb. Phil. Soc.* **26**, 361 (1930).
- Schwinger, J., "On quantum‑electrodynamics and the magnetic moment of the electron", *Phys. Rev.* **73**, 416 (1948).
- Schwinger, J., "On gauge invariance and vacuum polarization", *Phys. Rev.* **82**, 664 (1951).
- Burke, D. L. et al., "Positron production in multiphoton light‑by‑light scattering", *Phys. Rev. Lett.* **79**, 1626 (1997).
- Adam, J. et al. (STAR Collaboration), "Measurement of e⁺e⁻ momentum and angular distributions from linearly polarized photon collisions", *Phys. Rev. Lett.* **127**, 052302 (2021).
- Pike, O. J., Mackenroth, F., Hill, E. G. & Rose, S. J., "A photon–photon collider in a vacuum hohlraum", *Nat. Photon.* **8**, 434 (2014).
- Yoon, J. W. et al., "Realization of laser intensity over 10²³ W/cm²", *Optica* **8**, 630 (2021).
- Williamson, J. G. & van der Mark, M. B., "Is the electron a photon with toroidal topology?", *Ann. Fond. Louis de Broglie* **22**, 133 (1997).
- Fan, X., Myers, T. G., Sukra, B. A. D. & Gabrielse, G., "Measurement of the electron magnetic moment", *Phys. Rev. Lett.* **130**, 071801 (2023).
- Morel, L., Yao, Z., Cladé, P. & Guellati‑Khélifa, S., "Determination of the fine‑structure constant with an accuracy of 81 parts per trillion", *Nature* **588**, 61 (2020).
- Parker, R. H., Yu, C., Zhong, W., Estey, B. & Müller, H., "Measurement of the fine‑structure constant as a test of the Standard Model", *Science* **360**, 191 (2018).
- Laporta, S. & Remiddi, E., "The analytical value of the electron (g−2) at order α³ in QED", *Phys. Lett. B* **379**, 283 (1996).
- Laporta, S., "High‑precision calculation of the 4‑loop contribution to the electron g‑2 in QED", *Phys. Lett. B* **772**, 232 (2017).
- Workman, R. L. et al. (Particle Data Group), "Review of Particle Physics", *Prog. Theor. Exp. Phys.* **2022**, 083C01 (2022).
- Dürr, S. et al., "Ab initio determination of light hadron masses", *Science* **322**, 1224 (2008).
- Dyson, F. J. & Lenard, A., "Stability of matter. I", *J. Math. Phys.* **8**, 423 (1967).
- Lieb, E. H., "The stability of matter", *Rev. Mod. Phys.* **48**, 553 (1976).
