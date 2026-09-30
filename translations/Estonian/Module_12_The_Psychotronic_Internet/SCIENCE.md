# 🔬 12. moodul — Teadus loo taga

> [Õppetund](readme.md) on jutustatud aastast 2420. See lehekülg on 2025. aasta reaalsuskontroll: mis on kindlakstehtud, kus loo väide murdub ja mis peaks olema tõsi, et see töötaks. Kõike siin saab kontrollida [laborikoodiga](../../../Module_12_The_Psychotronic_Internet/simulation.py).

## 2420. aasta väide ühes lauses

Inimmõtteid saab siduda otse, ilma telefonide või juhtmeteta, läbi planeedilaiuse „noosfääri“, mida võimendab „psühhotrooniline võrk“, nii et küsimustele vastatakse hetkega ja oskusi saab alla laadida sekunditega.

## Tase 1 — Mis on päris

**Ajud on elektrilised ja nende välju saab mõõta.** Neuronid toodavad voolusid, mille välju saab salvestada pea väljaspool: EEG (mikrovoltid peanahal) ja MEG (magnetväljad umbes 100 fT kuni 1 pT sensoritel mõne sentimeetri kaugusel allikatest, umbes $10^{-8}$ Maa väljast).

**Aju–arvuti liidesed on päris.** Implanteeritud elektroodimassiivid (näiteks BrainGate katsetes) lasevad halvatusega inimestel juhtida kursorit, robotkäsi ja teksti. Willett jt (2021) dekodeerisid kujuteldud käekirja umbes 90 tähemärki minutis ja hilisem töö dekodeeris üritatud kõnet umbes 62 sõna minutis (Willett jt, 2023). Need on meditsiiniseadmed, mis loevad signaale aju sisse või peale paigutatud elektroodidelt; nad ei jõua teiste inimeste ajudeni läbi õhu.

**Juhid varjestavad välju.** Muutuv väli, mis siseneb juhisse, laguneb naha sügavuse jooksul

$$\delta = \sqrt{\frac{2}{\mu\sigma\omega}} \;\propto\; f^{-1/2}.$$

Merevees ($\sigma \approx 4$ S/m), $\delta = 29$ m 76 Hz juures, USA mereväe ELF‑allveelaevasaatjate sagedusel, 4,6 m 3 kHz juures ja 0,25 m 1 MHz juures. 2,4 GHz juures on vee nihkevool suurem kui juhtivusvool ($\omega\varepsilon/\sigma \approx 2{,}7$), nii et vaja on üldvalemit, mis annab umbes 1 cm. Vases $\delta = 9{,}2$ mm 50 Hz juures ja 65 µm 1 MHz juures: 1 mm vaskplekk neeldub umbes 133 dB 1 MHz juures. Seetõttu töötavad Faraday puurid.

**Staatilised väljad varjestatakse samuti.** Juhis liiguvad laengud, kuni väli sees on null. Juhtiva sfääri jaoks ühtlases väljas $E_0$ on indutseeritud pinnalaeng $\sigma_s = 3\varepsilon_0E_0\cos\theta$. Labor ei eeldada vastust: see liidab Coulomb’i seadust üle selle pinnalaengu numbriliselt ja leiab, et kogu väli sees on alla $10^{-4}E_0$, samas kui väljaspool sobib see õpiku dipoollahendiga.

**Potentsiaalid on päris ja aine täpsel viisil.** Whittaker näitas 1903–1904, et lainevõrrandi lahendeid ja elektromagnetvälja ennast saab kirjutada skalaarfunktsioonide abil. See on õige matemaatika, aga see kirjeldab *samu* välju $\mathbf E$ ja $\mathbf B$, mitte uut tüüpi lainet. Üks koht, kus potentsiaalidel on otse vaadeldavad efektid, on Aharonov–Bohmi efekt (1959): elektron, mis möödub magnetvoo $\Phi$ piirkonnast, saab faasi

$$\Delta\varphi = \frac{e\Phi}{\hbar} = 2\pi\,\frac{\Phi}{h/e},\qquad h/e = 4.14\times10^{-15}\ \text{Wb},$$

isegi kui magnetväli selle teel on null. Tonomura jt (1986) kinnitasid seda väljaga, mis oli täielikult ümbritsetud ülijuhtivas kilbis. Efekt sõltub ainult ümbritsetud voost ümber suletud aasa ja järgib standardset kvant‑elektrodünaamikat.

**Inimkommunikatsiooni kiirused on mõõdetavad.** Üle 17 keele kannab kõne umbes 39 bitti sekundis (Coupé jt, 2019). Kirjalik inglise keel kannab umbes 1 bitti tähemärgi kohta, kui selle liiasus on arvesse võetud (Shannon, 1951).

## Tase 2 — Kus väide murdub

**1. Miski ei kanna infot valgusest kiiremini.** „PING! Vastus ilmub su meelde silmapilkselt“ ei ole võimalik üle päris vahemaade:

| Ühendus | Ühesuunaline valguse viivitus |
|---|---|
| Maa–Kuu | 1.28 s |
| Maa–Marss (lähimast kaugeimani) | 3.0 kuni 22.3 min |
| Proxima Centauri | 4.25 aastat |

„Marsi pealinna“ küsimus saab vastuse kõige varem 6 kuni 45 minutit hiljem, ringreisina.

**2. Põimumine ei saa sõnumeid saata.** Põimunud paari jaoks arvutab labor Bobi lokaalse oleku pärast seda, kui Alice mõõdab mööda mis tahes telge, ja leiab, et see on alati täpselt $\tfrac12\mathbb 1$ (erinevus alla $10^{-15}$), sama nagu kui ta midagi ei teeks. Korrelatsioonid on päris (nende tulemused nõustuvad tõenäosusega $\cos^2(\Delta\theta/2)$), aga nad ilmuvad ainult siis, kui kaks salvestist võrreldakse tavalise kanali kaudu. See on no‑communication teoreem.

**3. Aju väljad on kellegi teiseni jõudmiseks palju liiga nõrgad.** Dipoolväli langeb kui $1/r^3$. 1 pT aju signaal, mis on mõõdetud umbes 4 cm kaugusel allikast, on umbes $6\times10^{-17}$ T 1 m juures ja $6\times10^{-26}$ T 1 km juures, rohkem kui $10^{20}$ korda nõrgem kui Maa väli. Parimad magnetomeetrid vajavad varjestatud ruume ja sensoreid peanahal.

**4. „Skalaar“‑poolid ei kiirga midagi uut.** Vastu‑keeratud (bifilaarne) pool juhib kahte vastupidist voolu, nii et väljad tühistuvad. Labor arvutab nii selle, mis jääb lähedale, kui ka selle, mis kiirgub:

- Teljel langeb ühe aasa väli kui $z^{-3{,}00}$; vastu‑keeratud paari jäänuk langeb kui $z^{-4{,}00}$: tavaline kõrgem multipool.
- Kaugel kiirgab paar $(kd)^2/5$ ühe pooli võimsusest, kui poolid on lähestikku ($kd \ll 1$). $d = 0$ korral on kiirgus täpselt null. Lisaks „skalaarlaine“ ei ilmu ja kui potentsiaalid ka tühistuvad, ei jää midagi, millel oleks efekt, Aharonov–Bohm või muu.

**5. Varjestus.** Kui psühhotrooniline signaal oleks elektromagnetiline, lõikaks metallruum, allveelaev või mõned meetrit merevett selle ära, nagu ülaltoodud naha sügavused näitavad. Kui see ei ole elektromagnetiline, vajab lugu uut loodusjõudu, mida ükski katse ei ole näinud.

**6. Ribalaius.** 1 MB lennujuhend kõne kiirusel võtab ülekandeks umbes 57 tundi. Selle allalaadimine 5 s jooksul vajaks $1{,}6\times10^6$ bitti/s, umbes 40 000 korda kõne kiirusest. Päris BCI‑d täna jooksevad mõne biti sekundis. Me ei tea ka, kuidas oskusi või mälestusi ajusse kirjutada: see nõuaks sünapsite täpset muutmist üle tohutu arvu neuronite.

**7. Noosfäär on filosoofia, mitte füüsika.** Vernadski ja Teilhard de Chardin kasutasid „noosfääri“ kasvava inimõtte sfääri ja selle mõju planeedile jaoks. See on mõtlik idee ühiskonna ja evolutsiooni kohta, mitte mõõdetud atmosfäärikiht. Mesilased suhtlevad tõepoolest, aga füüsikaliste signaalide kaudu: vibutustants, feromoonid ja vibratsioonid.

## Tase 3 — Mis peaks olema tõsi

Selleks et psühhotrooniline internet eksisteeriks, peaksid kõik need olema näidatud. Igaüks on testitav:

- **Kandja, mis jõuab ajust ajusse.** Test: saatja ja vastuvõtja eraldi Faraday‑varjestatud ruumides, juhuslike sihtsõnumitega, pimeda skoorimise ja eelregistreeritud analüüsiga, korduvalt sõltumatute laborite poolt.
- **Tee ümber valguse kiiruse**, mis kukutaks ka relatiivsusteooria ja põhjuslikkuse. Test: sõnum, mis saabub enne, kui valgus oleks saanud selle kanda.
- **Loe–kirjuta liides mälestustele ja oskustele**: arusaamine, kuidas oskus on sünapsites salvestatud, piisavalt hästi, et kirjutada see teise ajusse.

**Päris avatud küsimused loo lähedal:** Kui kiireks ja kui ohutuks saavad BCI‑d saada ning kas neid saab teha ilma operatsioonita? Kui palju aju infost saavad mitte‑invasiivsed meetodid (EEG, MEG, optiliselt pumbatud magnetomeetrid, funktsionaalne ultraheli) lugeda? Millised on privaatsuse ja eetika reeglid „neuraalandmete“ jaoks?

## Käivita labor

```bash
python Module_12_The_Psychotronic_Internet/simulation.py
python -m pytest tests/test_module_12.py
```

| Katse | Mida see näitab |
|---|---|
| `skin_depth`, `attenuation_length`, `shield_absorption_db` | Merevesi ja metall blokeerivad muutuvaid välju; $\delta \propto f^{-1/2}$. |
| `conducting_sphere_field` | Coulomb’i seaduse summeerimine üle indutseeritud laengu annab null välja juhi sees. |
| `antiparallel_pair_power`, `counterwound_axis_field` | Vastupidised voolud jätavad tavalise, kiiremini langeva multipooli, mitte uue laine. |
| `aharonov_bohm_phase` | Potentsiaalide päris, mõõdetud efekt. |
| `light_delay`, `bob_state`, `same_outcome_probability` | Valguskiiruse viivitused; põimumine korreleerib, aga ei saa signaalida. |
| `brain_field`, `bci_bits_per_second`, `transfer_time` | Kui nõrgad on aju väljad ja kui aeglased on inimandmete kiirused. |

## Proovi ise

1. Leia sagedus, millel merevee naha sügavus on 100 m. Miks saatis mereväe allveelaevaraadio ainult mõned tähemärgid minutis?
2. Funktsioonis `bob_state` asenda Belli olek $(\lvert00\rangle + \lvert11\rangle)$ pluss väikese $\lvert01\rangle$ seguga (normaliseeri). Kas Alice’i nurga valik muudab nüüd Bobi olekut?
3. Kasutades `antiparallel_pair_power`, kui kaugel peavad kaks vastupidist 1 kHz pooli olema (km‑des), enne kui nad kiirgavad sama palju kui üksik pool?
4. Otsi üles lugemise info‑kiirus. Kui kaua võtaks kogu interneti lugemine sellel kiirusel?

## Viited

- Whittaker, E. T., "On the partial differential equations of mathematical physics", *Math. Ann.* **57**, 333 (1903).
- Whittaker, E. T., "On an expression of the electromagnetic field due to electrons by means of two scalar potential functions", *Proc. London Math. Soc.* **s2‑1**, 367 (1904).
- Aharonov, Y. & Bohm, D., "Significance of electromagnetic potentials in the quantum theory", *Phys. Rev.* **115**, 485 (1959).
- Tonomura, A. et al., "Evidence for Aharonov‑Bohm effect with magnetic field completely shielded from electron wave", *Phys. Rev. Lett.* **56**, 792 (1986).
- Ghirardi, G. C., Rimini, A. & Weber, T., "A general argument against superluminal transmission through the quantum mechanical measurement process", *Lett. Nuovo Cimento* **27**, 293 (1980).
- Nielsen, M. A. & Chuang, I. L., *Quantum Computation and Quantum Information*, Cambridge University Press (2000).
- Hämäläinen, M. et al., "Magnetoencephalography—theory, instrumentation, and applications to noninvasive studies of the working human brain", *Rev. Mod. Phys.* **65**, 413 (1993).
- Willett, F. R. et al., "High‑performance brain‑to‑text communication via handwriting", *Nature* **593**, 249 (2021).
- Willett, F. R. et al., "A high‑performance speech neuroprosthesis", *Nature* **620**, 1031 (2023).
- Coupé, C., Oh, Y. M., Dediu, D. & Pellegrino, F., "Different languages, similar encoding efficiency: Comparable information rates across the human communicative niche", *Science Advances* **5**, eaaw2594 (2019).
- Shannon, C. E., "Prediction and entropy of printed English", *Bell Syst. Tech. J.* **30**, 50 (1951).
- Vernadsky, V. I., "The biosphere and the noosphere", *American Scientist* **33**, 1 (1945).
- Teilhard de Chardin, P., *The Phenomenon of Man* (1955; English translation 1959).
