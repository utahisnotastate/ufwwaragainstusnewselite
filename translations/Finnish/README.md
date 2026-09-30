# 2420-luvun „kadonnut“ opetussuunnitelma — ilmeinen fysiikka ihmisille

[![tests](https://github.com/utahisnotastate/ufwwaragainstusnewselite/actions/workflows/tests.yml/badge.svg)](https://github.com/utahisnotastate/ufwwaragainstusnewselite/actions/workflows/tests.yml)

☕ Tue projektia: [ko-fi.com/utah23](https://ko-fi.com/utah23) · Miksi tein tämän: [ABOUT.md](ABOUT.md)

Kaksitoista suurta ideaa, jokainen opetettu kolmella tavalla:

| Kerros | Tiedosto | Mitä se on |
|---|---|---|
| 📖 **Tarina** | `readme.md` | Oppitunti ikään kuin vuoden 2420 koulusta — teräville 8‑vuotiaille ja uteliaille aikuisille. Tieteisfiktiota oikean kysymyksen ympärillä. |
| 🔬 **Tiede** | `SCIENCE.md` | Vuoden 2025 todellisuustarkistus: mikä on vakiintunutta, missä tarinan väite pettää (lukujen kanssa), ja mitä pitäisi olla totta, jotta se toimisi. Oikeilla viitteillä. |
| 🧪 **Laboratorio** | `simulation.py` | Ajettava Python, joka laskee jokaisen luvun tiedesivulla. Testattu oppikirjarajoja ja julkaistuja mittauksia vasten. *(Laboratoriot elävät englanninkielisen repon juuressa — ei käännöskansiossa.)* |

Jokainen moduuli säilyttää myös maailmansisäisen `PHYSICS_PROOF.md`-tiedoston: vuoden 2420 arkiston oman argumentin, selvästi merkittynä osaksi tarinaa.

**Miksi tämä muoto?** Tarinat ovat koukku. Ne kysyvät kysymyksiä, joita lapset oikeasti kysyvät: *Onko avaruus todella tyhjä? Miksi painovoima vetää? Voisimmeko matkustaa hetkessä?* Tiedesivut vastaavat rehellisesti — myös „ei, ja tässä on lasku, joka näyttää miksi.“ Oppiminen siitä, missä kaunis idea pettää, opettaa enemmän fysiikkaa kuin väite, että se toimii.

---

## Pika-aloitus

Laboratoriot ajetaan repon juuresta (englanninkieliset polut):

```bash
python -m pip install -r requirements.txt
python Module_02_Gravity_Is_Pushing/simulation.py   # aja yksi laboratorio
python -m pytest                                    # tarkista kaikki laboratoriot
```

Vaatii Python 3.10+:n sekä NumPyn ja SciPyn. Piirtokirjastoa tai internetyhteyttä ei tarvita.

---

## Moduuli-indeksi

| # | Moduuli | Vuoden 2420 tarina sanoo… | Mitä laboratorio laskee |
|---|---|---|---|
| 1 | 🌊 [Tyhjiömeri](Module_01_Zero_Point_Energy/readme.md) · [tiede](Module_01_Zero_Point_Energy/SCIENCE.md) | Avaruus on korkeapaineinen pleenum, josta voi napata ilmaista energiaa. | Casimir-voima (ideaali ja Lifshitz-teoria oikealle kullalle); miksi suljettu kierto antaa nollan nettotyön. |
| 2 | 📉 [Painovoima työntää](Module_02_Gravity_Is_Pushing/readme.md) · [tiede](Module_02_Gravity_Is_Pushing/SCIENCE.md) | Massat varjostavat toisiaan kosmiselta vuolta. | Monte Carlo -varjostus antaa 1/r²:n; sitten veto, kuumeneminen ja kyllästyminen, jotka upottivat Le Sagen painovoiman. |
| 3 | 📻 [Aivot ovat radio](Module_03_The_Brain_Is_A_Radio/readme.md) · [tiede](Module_03_The_Brain_Is_A_Radio/SCIENCE.md) | Mieli on signaali, johon aivot virittyvät. | Oikea EEG-signaalinkäsittely, Schumann-resonanssit ja vaihekytkennän testaus kunnollista nollaa vasten. |
| 4 | 🍩 [Aine on jäätynyttä valoa](Module_04_Matter_Is_Frozen_Light/readme.md) · [tiede](Module_04_Matter_Is_Frozen_Light/SCIENCE.md) | Hiukkaset ovat ympyrässä juoksevaa valoa. | Breit–Wheeler-parien luonti, Schwinger-kenttä, mistä protonin massa tulee, ja miksi „valosilmukka“-elektroni on tautologia. |
| 5 | 🗺️ [Aika on kartta](Module_05_Time_Is_A_Map/readme.md) · [tiede](Module_05_Time_Is_A_Map/SCIENCE.md) | Menneisyys ja tulevaisuus ovat koordinaatteja, joissa voi vierailla. | GPS-kellokorjaukset, samanaikaisuuden suhteellisuus, Kerrin ergosfäärit ja Penrose-prosessi. |
| 6 | 🔊 [Todellisuuden kieli](Module_06_Language_of_Reality/readme.md) · [tiede](Module_06_Language_of_Reality/SCIENCE.md) | Ääni muovaa ainetta. | Chladni-levyjen moodit, akustiset säteilyvoimat ja miksi ääni ei voi sijoittaa atomeja. |
| 7 | 🧬 [DNA antennina](Module_07_DNA_Antenna/readme.md) · [tiede](Module_07_DNA_Antenna/SCIENCE.md) | DNA vastaanottaa ohjeita kentästä. | Kierreantenniteoria vs DNA:n todellinen koko, Debye-seulonta solussa, FRET ja DNA:n dynamiikka. |
| 8 | ⚡ [Hetkellinen matkustaminen](Module_08_Instant_Travel/readme.md) · [tiede](Module_08_Instant_Travel/SCIENCE.md) | Taita avaruus ja astu yli. | Alcubierren warp-metriikka, sen negatiivisen energian lasku ja kvanttiepäyhtälörajoitukset. |
| 9 | ⛈️ [Säätekniikka](Module_09_Weather_Engineering/readme.md) · [tiede](Module_09_Weather_Engineering/SCIENCE.md) | Ohjaa myrskyjä ristikkäisillä aalloilla. | Köhlerin pisara-aktivaatio, ioni-indusoitu nukleaatio ja energiaero koneiden ja myrskyjen välillä. |
| 10 | ⏳ [Ajan kääntäminen parantamiseen](Module_10_Time_Reversal_Healing/readme.md) · [tiede](Module_10_Time_Reversal_Healing/SCIENCE.md) | Aikapeili kumoaa sairauden. | Optinen vaihekonjugaatio ja sen rajat, solukalvojännitteet ja elämän entropiabudjetti. |
| 11 | ⚗️ [Kullan saostaminen](Module_11_Low_Energy_Transmutation/readme.md) · [tiede](Module_11_Low_Energy_Transmutation/SCIENCE.md) | Resonanssihilat tekevät fuusiosta helppoa. | Coulombin esteet, Gamow-tunnelointi, elektroniseulonta ja neutronimäärä, jonka 1 W fuusiota tuottaisi. |
| 12 | 🌐 [Psykotroninen internet](Module_12_The_Psychotronic_Internet/readme.md) · [tiede](Module_12_The_Psychotronic_Internet/SCIENCE.md) | Mielet linkittyvät hetkessä tyhjiön kautta. | Tunkeutumissyvyys merivedessä ja Faraday-häkeissä, miksi „skalaari“-kelat eivät säteile mitään uutta, ja oikeat aivo–tietokone-liitäntöjen kaistanleveydet. |

Moduulit rakentuvat toistensa päälle, joten aloita moduulista 1. Terveysmuistutus: mikään tässä ei ole lääketieteellistä neuvontaa (ks. moduuli 10).

---

## Osallistuminen

Korjaukset ovat arvokkain panos: väärä luku, puuttuva varoitus, parempi viite. Katso [CONTRIBUTING.md](CONTRIBUTING.md) moduulirakenteesta sekä koodin ja viittausten säännöistä.

## Tarkoitus

Tämä opetussuunnitelma käyttää tieteisfiktiota tekemään fysiikkakysymyksistä vastustamattomia — ja vastaa niihin sitten rehellisesti. Tarinat ovat mielikuvituksellisia; tiedesivut ja koodi pyrkivät olemaan oikein. Jos löydät kohdan, jossa ne eivät ole, avaa issue.
