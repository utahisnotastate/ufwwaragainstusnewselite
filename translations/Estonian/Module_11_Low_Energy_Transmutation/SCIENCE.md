# 🔬 11. moodul — Teadus loo taga

> [Õppetund](readme.md) on jutustatud aastast 2420. See lehekülg on 2025. aasta reaalsuskontroll: mis on kindlakstehtud, kus loo väide murdub ja mis peaks olema tõsi, et see töötaks. Kõike siin saab kontrollida [laborikoodiga](../../../Module_11_Low_Energy_Transmutation/simulation.py).

## 2420. aasta väide ühes lauses

Tuumasid saab õrnalt „ümber voltida“ teisteks elementideks toatemperatuuril, metallvõrede, ensüümide või bakterite abil, ilma kõrgete energiateta, nii et kulda saab kasvatada ja tuumajäätmeid väetiseks muuta.

## Tase 1 — Mis on päris

**Transmutatsioon on päris.** Tuumad muutuvad teisteks elementideks: tähtedes, reaktorites, kiirendites ja radioaktiivses lagunemises. Elavhõbe‑196 saab isegi kullaks muuta reaktoris: $^{196}$Hg püüab neutroni, et saada $^{197}$Hg, mis laguneb elektronpüüdega $^{197}$Au‑ks. See töötab, aga toodab tillukesi koguseid suure hinnaga.

**Coulomb’i müür.** Kaks tuuma laengutega $Z_1e$, $Z_2e$ tõukuvad energiaga $Z_1Z_2e^2/(4\pi\varepsilon_0 r)$, kus $e^2/4\pi\varepsilon_0 = 1{,}44$ MeV·fm. Puutekaugusel ($r \approx 1{,}2(A_1^{1/3}+A_2^{1/3})$ fm) on see umbes **0,48 MeV kahe deutroni jaoks** ja **5,2 MeV prootoni ja kaalium‑39 jaoks**. Toatemperatuur annab osakestele umbes $kT = 0{,}026$ eV: umbes 20 miljonit korda liiga vähe, et üle ronida.

**Tunneldumine.** Kvantmehaanika laseb tuumadel läbi müüri tunnelda. Palja Coulomb’i müüri jaoks on tõenäosus Gamow’ tegur

$$P(E) = e^{-2\pi\eta} = \exp\!\left(-\sqrt{E_G/E}\right),\qquad \eta = Z_1Z_2\,\alpha\sqrt{\frac{\mu c^2}{2E}},\qquad E_G = 2\mu c^2\,(\pi\alpha Z_1Z_2)^2 .$$

D–D jaoks $E_G = 0{,}986$ MeV (labor taastoodab Boschi ja Hale’i konstandi $\sqrt{E_G} = 31{,}40$ keV$^{1/2}$). Ristlõiked kirjutatakse

$$\sigma(E) = \frac{S(E)}{E}\,e^{-\sqrt{E_G/E}},$$

kus astrofüüsikaline S‑tegur $S(E)$ muutub aeglaselt: umbes 55 keV·b kummagi peamise D–D harus. Keskmistatuna üle soojusgaasi annab see D–D reaktiivsuse umbes 25 % piires avaldatud väärtustest 2 kuni 10 keV (test laboris).

**Elektronide varjestus on päris ja avatud uurimisküsimus.** Elektronid tuumade ümber tühistavad osaliselt nende tõukumise. Väikestel kaugustel näeb potentsiaal välja nagu $e^2/r - U_e$, mis võimendab madala energia ristlõikeid

$$f(E) \approx \exp\!\left(\pi\eta\,\frac{U_e}{E}\right)\qquad (U_e \ll E)$$

(Assenbaum, Langanke & Rolfs, 1987). Deuteeriumgaasi jaoks on oodatav (adiabaatiline) väärtus $U_e \approx 28$ eV. Kiirekatsed keV energiatel deuteeriumil, mis on laaditud metallidesse, on teatanud palju suurematest väärtustest, mõnesaja eV (näiteks umbes 300 eV tantaalis; Raiola jt, 2002). Miks need väärtused nii suured on, on endiselt debatt.

**Energiaarvestus.** Tuumareaktsioonid vabastavad või neelavad energiat $Q = (\sum m_\text{in} - \sum m_\text{out})c^2$. Mõõdetud massidest: D + D → T + p vabastab 4,03 MeV; D + D → ³He + n vabastab 3,27 MeV (kumbki umbes 50 % ajast); D + D → ⁴He + γ vabastab 23,85 MeV, aga juhtub ainult umbes üks kord $10^7$ fusiooni kohta. K‑39 + p → Ca‑40 vabastaks 8,33 MeV.

## Tase 2 — Kus väide murdub

**1. Tunneldumisnumbrid toatemperatuuril.** Juures $E = kT = 0{,}026$ eV on paljas D–D Gamow’ tegur $10^{-2682}$. Isegi labori WKB arvutus 800 eV varjestusega annab $10^{-24}$ paarile soojusenergial. Paar „näeb“ varjestuse kasu alles siis, kui on juba lähemal kui varjestuspikkus, $a = e^2/U_e \approx 1800$ fm.

**2. Optimistlik kiiruse hinnang.** Labor arvutab D–D fusiooni pallaadiumdeuteeriidis (PdD, $6{,}8\times10^{22}$ D/cm³) 300 K juures, käsitledes iga paari varjestatuna $U_e$‑ga ja hõlmates kogu Maxwelli saba kiiretest põrgetest. See mudel on tahtlikult helde:

| $U_e$ | Võimsus (W/cm³) |
|---|---|
| 0 (paljas) | $2\times10^{-254}$ |
| 28 eV (gaas) | $9\times10^{-101}$ |
| 300 eV | $7\times10^{-19}$ |
| 800 eV | $9\times10^{-4}$ |

Tulemus muutub teguriga umbes 260 ±10 % muutuse korral $U_e$‑s ja 1 W/cm³ vajaks $U_e \approx 1050$ eV. Nii et vastus sõltub täielikult sellest, kas keV‑kiire varjestusväärtused kehtivad toatemperatuuri deutronitele, mida keegi ei ole näidanud. Koonin ja Nauenberg (1989) arvutasid, et kaks deutronit D₂ molekulis, ainult 0,74 Å kaugusel, fuseeruvad umbes $10^{-64}$ sekundis.

**3. Puuduvad neutronid (otsustav test).** Kui soojus tuleks tavalisest D–D fusioonist, kiirgaks pool reaktsioonidest 2,45 MeV neutroni. Kasutades ülaltoodud Q‑väärtusi:

$$\frac{1\ \text{W}}{\tfrac12(4.03+3.27)\ \text{MeV}} = 1.7\times10^{12}\ \text{fusions/s} \;\Rightarrow\; 8.6\times10^{11}\ \text{neutrons/s per watt}.$$

1 m kaugusel varjestamata 1 W allikast on see umbes 10 Sv tunnis: tüüpiliselt letaalne doos umbes poole tunniga. See on „surnud magistrandi“ nalja päritolu. Neutrondetektorid suudavad lugeda üksikuid neutroneid, nii et isegi $10^{-12}$ W D–D fusiooni on mõõdetav. Külma fusiooni katsed teatasid vati‑taseme ülejääksoojusest ilma millegi sarnase neutroni‑, triitiumi‑ või gammatoodanguta. Nii et kas soojus ei ole D–D fusioon või see ei ole tuumaline.

**4. 1989. aasta väiteid ei kinnitatud.** Fleischmann ja Pons (1989) teatasid ülejääksoojusest pallaadiumelektroodidelt raskes vees. Paljud laborid üritasid seda korrata ega suutnud seda usaldusväärselt teha. Mitmeaastane programm Berlinguette jt (2019) poolt uuris peamisi väiteid hoolika kalorimeetriaga ega leidnud tõendeid anomaalse soojuse ega tuumaproduktide kohta, märkides samal ajal kasulikku materjaliteadust.

**5. Kanad ja bakterid.** Ensüümid töötavad keemiliste energiatega umbes 0,5 eV (näiteks ATP hüdrolüüs). K‑39 + p → Ca‑40 barjäär on 5,2 MeV, kümme miljonit korda kõrgem, ja labori tunneldumistõenäosus kehatemperatuuril on $10^{-49515}$. Louis Kervrani bioloogilise transmutatsiooni väiteid ei ole kontrollitud tingimustes korratud. Munemiskanad ammutavad kaltsiumi toidust ja erilise reservi oma luudest; kaltsiumivaesel dieedil langeb koore kvaliteet.

**6. „Voltimine“ ei ole tasuta.** Plii‑208 muutmine kuld‑197‑ks tähendab 3 prootoni ja 8 neutroni eemaldamist. Massid ütlevad, et see maksab vähemalt 77 MeV aatomi kohta, umbes 10 MWh grammi kulla kohta, enne mis tahes kadusid. Tuumade sidumisenergia on põhjus: tükke hoitakse koos ja nende lahutamine maksab energiat.

## Tase 3 — Mis peaks olema tõsi

Selleks et toatemperatuuri transmutatsioon oleks päris, peaksid kõik need olema näidatud. Igaüks on selge, testitav sihtmärk:

- **Varjestus, mis töötab soojusenergiatel.** Mõõda madala energia D–D saagiseid metallides energiatel, mis lähenevad eV skaalale, ja näita efektiivset $U_e$ üle umbes 1 keV, mis kehtib deutronitele puhkeolekus võres.
- **Tuumaproduktid, mis sobivad soojusega.** Iga džaul tuumasoojust peab tulema õige arvu neutronite, triitiumi, ³He, ⁴He või gammakiirtega. Mõõda neid samas käigus, pimeda analüüsiga.
- **Mehhanism, mis muudab harusid.** Kui neutroneid pole, peab uus füüsika saatma energia võresse kiirete osakeste asemel ja seda peab ette ennustama ning seejärel vaatlema.
- **Sõltumatu kordamine** laborite poolt, mis ei kavandanud algset katset, avatud andmetega.

**Avatud uurimisküsimused, mis on päris:** miks on mõõdetud varjestusenergiad metallides nii suured; kuidas käitub vesinik metallvõredes (oluline vesinikusäilituse ja rabeduse jaoks); ja madala energia tuumaristlõiked täheastrofüüsika jaoks, mõõdetud sügaval maa all (näiteks LUNA Itaalias).

## Käivita labor

```bash
python Module_11_Low_Energy_Transmutation/simulation.py
python -m pytest tests/test_module_11.py
```

| Katse | Mida see näitab |
|---|---|
| `coulomb_barrier`, `gamow_energy`, `gamow_factor` | Coulomb’i müür ja paljas tunneldumistõenäosus, kontrollitud Bosch–Hale’i $\sqrt{E_G}$ vastu. |
| `wkb_exponent`, `screening_enhancement` | Numbriline WKB tunneldumine läbi varjestatud müüri; taastoodab analüütilisi Gamow’ ja Assenbaumi tulemusi nende piirides. |
| `dd_reactivity_cm3_s`, `fusion_power_density` | Soojuslikud D–D kiirused (sobivad avaldatud väärtustega keV juures) ja optimistlik toatemperatuuri hinnang PdD jaoks. |
| `q_value`, `neutrons_per_watt`, `dose_rate_sv_per_hour` | Q‑väärtused mõõdetud massidest ja neutronivoog, mida 1 W D–D fusiooni toodaks. |
| `transmutation_cost_mev` | Plii → kuld minimaalne energiakulu. |

## Proovi ise

1. Kasuta `screening_needed`, et leida $U_e$, mis annaks 1 mW/cm³, ja võrdle seda ~300 eV‑ga, mida mõõdeti tantaalis.
2. Muuda `temp_k` funktsioonis `fusion_power_density` 600 K‑ks. Kui palju aitab temperatuuri kahekordistamine võrreldes 10 % tõusuga $U_e$‑s?
3. Arvuta neutronidoosi määr 3 m kaugusel 0,1 W allikast. Kui paks peaks olema veekaitse? (Otsi kiirete neutronite summutuspikkust vees.)
4. Kasuta `q_value`, et kontrollida, kas ¹²C + ¹²C → ²⁴Mg vabastab energiat, seejärel kasuta `coulomb_barrier` ja `gamow_energy`, et näha, miks see juhtub ainult massiivsete tähtede sees.

## Viited

- Gamow, G., "Zur Quantentheorie des Atomkernes", *Z. Phys.* **51**, 204 (1928).
- Assenbaum, H. J., Langanke, K. & Rolfs, C., "Effects of electron screening on low‑energy fusion cross sections", *Z. Phys. A* **327**, 461 (1987).
- Bosch, H.‑S. & Hale, G. M., "Improved formulas for fusion cross‑sections and thermal reactivities", *Nucl. Fusion* **32**, 611 (1992).
- Raiola, F. et al., "Enhanced electron screening in d(d,p)t for deuterated Ta", *Eur. Phys. J. A* **13**, 377 (2002).
- Koonin, S. E. & Nauenberg, M., "Calculated fusion rates in isotopic hydrogen molecules", *Nature* **339**, 690 (1989).
- Fleischmann, M., Pons, S. & Hawkins, M., "Electrochemically induced nuclear fusion of deuterium", *J. Electroanal. Chem.* **261**, 301 (1989).
- Berlinguette, C. P. et al., "Revisiting the cold case of cold fusion", *Nature* **570**, 45 (2019).
- Wang, M. et al., "The AME 2020 atomic mass evaluation (II)", *Chinese Phys. C* **45**, 030003 (2021). Source of the atomic masses.
- ICRP Publication 74, *Conversion Coefficients for use in Radiological Protection against External Radiation* (1996). Source of the approximate neutron dose coefficient.
- Huba, J. D., *NRL Plasma Formulary* (Naval Research Laboratory, revised regularly). Tabulated D–D reactivities used in the tests.
