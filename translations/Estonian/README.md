# 2420. aastate „kadunud“ õppekava — ilmselge füüsika inimestele

[![tests](https://github.com/utahisnotastate/ufwwaragainstusnewselite/actions/workflows/tests.yml/badge.svg)](https://github.com/utahisnotastate/ufwwaragainstusnewselite/actions/workflows/tests.yml)

☕ Toeta projekti: [ko-fi.com/utah23](https://ko-fi.com/utah23) · Miks ma selle tegin: [ABOUT.md](ABOUT.md)

Kaksteist suurt ideed, igaüks õpetatud kolmel viisil:

| Kiht | Fail | Mis see on |
|---|---|---|
| 📖 **Lugu** | `readme.md` | Õppetund, mis on kirjutatud nii, nagu oleks see 2420. aasta koolist, teravmeelsetele 8‑aastastele ja uudishimulikele täiskasvanutele. Ulme, mis on üles ehitatud päris küsimuse ümber. |
| 🔬 **Teadus** | `SCIENCE.md` | 2025. aasta reaalsuskontroll: mis on kindlakstehtud, kus loo väide murdub (numbritega) ja mis peaks olema tõsi, et see töötaks. Päris viidetega. |
| 🧪 **Labor** | `simulation.py` | Käivitatav Python, mis arvutab iga numbri teaduslehel. Testitud õpiku piiride ja avaldatud mõõtmiste vastu. |

Iga moodul säilitab ka universumisisese `PHYSICS_PROOF.md`: 2420. aasta arhiivi enda argumendi, selgelt märgistatud loo osana.

**Miks selline vorm?** Lood on konks. Need küsivad küsimusi, mida lapsed tegelikult küsivad: *Kas ruum on tõesti tühi? Miks gravitatsioon tõmbab? Kas saaksime hetkega reisida?* Teaduslehed vastavad ausalt, sealhulgas „ei, ja siin on arvutus, mis näitab miks“. Õppimine, kus ilus idee murdub, õpetab rohkem füüsikat kui väide, et see töötab.

---

## Kiirstart

```bash
python -m pip install -r requirements.txt
python Module_02_Gravity_Is_Pushing/simulation.py   # käivita üks labor
python -m pytest                                    # kontrolli iga laborit
```

Vajab Python 3.10+ koos NumPy ja SciPy‑ga. Joonistusraamatukogu ega internetiühendust ei ole vaja.

Laborid (`simulation.py`) asuvad hoidla juurkaustas inglise keeles; käivita need sealt, mitte tõlkekaustast.

---

## Moodulite register

| # | Moodul | 2420. aasta lugu ütleb… | Mida labor arvutab |
|---|---|---|---|
| 1 | 🌊 [Vaakumookean](Module_01_Zero_Point_Energy/readme.md) · [teadus](Module_01_Zero_Point_Energy/SCIENCE.md) | Ruum on kõrgsurve‑pleenum, millest saab ammutada tasuta energiat. | Casimiri jõud (ideaalne ja Lifshitzi teooria päris kulla jaoks), miks suletud tsükkel annab null netoöö. |
| 2 | 📉 [Gravitatsioon lükkab](Module_02_Gravity_Is_Pushing/readme.md) · [teadus](Module_02_Gravity_Is_Pushing/SCIENCE.md) | Massid varjavad teineteist kosmilise voo eest. | Monte Carlo varjestus annab 1/r², seejärel takistus, kuumenemine ja küllastumine, mis uputasid Le Sage’i gravitatsiooni. |
| 3 | 📻 [Aju on raadio](Module_03_The_Brain_Is_A_Radio/readme.md) · [teadus](Module_03_The_Brain_Is_A_Radio/SCIENCE.md) | Meel on signaal, millesse aju häälestub. | Päris EEG‑signaalitöötlus, Schumanni resonantsid ja faasilukustuse testimine õige nulliga. |
| 4 | 🍩 [Aine on külmunud valgus](Module_04_Matter_Is_Frozen_Light/readme.md) · [teadus](Module_04_Matter_Is_Frozen_Light/SCIENCE.md) | Osakesed on ringis jooksev valgus. | Breit–Wheeleri paaride teke, Schwingeri väli, kust tuleb prootoni mass, ja miks „valgussilmuse“ elektron on tautoloogia. |
| 5 | 🗺️ [Aeg on kaart](Module_05_Time_Is_A_Map/readme.md) · [teadus](Module_05_Time_Is_A_Map/SCIENCE.md) | Minevik ja tulevik on koordinaadid, mida saab külastada. | GPS‑kella korrektsioonid, samaaegsuse relatiivsus, Kerri ergosphere’id ja Penrose’i protsess. |
| 6 | 🔊 [Reaalsuse keel](Module_06_Language_of_Reality/readme.md) · [teadus](Module_06_Language_of_Reality/SCIENCE.md) | Heli vormib ainet. | Chladni plaadi moodid, akustilised kiirgusjõud ja miks heli ei saa aatomeid paigutada. |
| 7 | 🧬 [DNA kui antenn](Module_07_DNA_Antenna/readme.md) · [teadus](Module_07_DNA_Antenna/SCIENCE.md) | DNA saab juhiseid väljast. | Spiraalse antenni teooria vs DNA tegelik suurus, Debye’i varjestus rakus, FRET ja DNA dünaamika. |
| 8 | ⚡ [Hetkeline reisimine](Module_08_Instant_Travel/readme.md) · [teadus](Module_08_Instant_Travel/SCIENCE.md) | Murra ruum kokku ja astu üle. | Alcubierre’i warp‑meetrika, selle negatiivse energia arve ja kvant‑ebavõrdsuste piirid. |
| 9 | ⛈️ [Ilmatehnoloogia](Module_09_Weather_Engineering/readme.md) · [teadus](Module_09_Weather_Engineering/SCIENCE.md) | Juhi torme ristatud lainetega. | Köhleri tilkade aktiveerumine, ioonide indutseeritud nukleatsioon ja energiavahe masinate ning tormide vahel. |
| 10 | ⏳ [Ajatagasipööramise ravi](Module_10_Time_Reversal_Healing/readme.md) · [teadus](Module_10_Time_Reversal_Healing/SCIENCE.md) | Ajapeegel tühistab haiguse. | Optiline faasikonjugatsioon ja selle piirid, rakumembraani pinged ning elu entroopiabilanss. |
| 11 | ⚗️ [Kulla sadestamine](Module_11_Low_Energy_Transmutation/readme.md) · [teadus](Module_11_Low_Energy_Transmutation/SCIENCE.md) | Resonantsed võred teevad fusiooni lihtsaks. | Coulomb’i barjäärid, Gamow’ tunneldumine, elektronide varjestus ja neutronite arv, mida annaks 1 W fusiooni. |
| 12 | 🌐 [Psühhotrooniline internet](Module_12_The_Psychotronic_Internet/readme.md) · [teadus](Module_12_The_Psychotronic_Internet/SCIENCE.md) | Meeled ühenduvad hetkega läbi vaakumi. | Nahasügavus merevees ja Faraday puurides, miks „skalaar“‑poolid midagi uut ei kiirga, ja päris aju–arvuti liidese ribalaiused. |

Moodulid ehituvad üksteise peale, seega alusta 1. moodulist. Tervisemärkus: midagi siin ei ole meditsiiniline nõuanne (vt 10. moodul).

---

## Tõlked

Eesti, soome, vene, jaapani ja hiina (lihtsustatud) lood elavad kaustas [`translations/`](../README.md). Õed‑kaustad (soome, vene, jaapani, hiina) võivad olla erinevas valmiduses. Laborid jäävad ingliskeelsesse juurkausta; käivita need hoidla juurest.

---

## Kaastöö

Kõige väärtuslikum panus on parandus: vale number, puuduv mööndus, parem viide. Vt [CONTRIBUTING.md](CONTRIBUTING.md) mooduli paigutuse ning koodi ja viidete reeglite kohta.

## Eesmärk

See õppekava kasutab ulmet, et teha füüsikaküsimused vastupandamatuks, ja vastab neile seejärel ausalt. Lood on kujutlusvõimelised; teaduslehed ja kood püüavad olla õiged. Kui leiad koha, kus nad ei ole, ava palun päring (issue).
