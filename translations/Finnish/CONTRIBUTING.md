# Osallistuminen

Kiitos avusta. Arvokkaimmat panokset ovat **korjauksia**: väärä luku, liioiteltu väite, puuttuva varoitus tai parempi viite.

## Moduulin rakenne

Jokainen `Module_NN_Name/`-kansio sisältää:

| Tiedosto | Rooli | Säännöt |
|---|---|---|
| `readme.md` | 📖 Vuoden 2420 tarinaoppitunti | Alkaa otsikolla ja „Tarinatila“-bannerilla, sitten `Oppitunnin otsikko`, `Lähde`, `Käsite` -kohdat ja numeroidut osiot. Kuvitteellista, mutta ei koskaan kehota lukijaa ohittamaan oikeaa lääketieteellistä hoitoa. |
| `PHYSICS_PROOF.md` | 📜 Maailmansisäinen argumentti | Alkaa „Maailmansisäinen asiakirja“ -bannerilla. Osiot: 8‑vuotiaalle, Aihe, Aksioomi, Mekanismi, Todistus/Johtopäätös. |
| `SCIENCE.md` | 🔬 Vuoden 2025 todellisuustarkistus | Osiot: Vuoden 2420 väite yhdessä lauseessa · Taso 1 — Mikä on totta · Taso 2 — Missä väite pettää · Taso 3 — Mitä pitäisi olla totta · Aja laboratorio · Kokeile itse · Viitteet. |
| `simulation.py` | 🧪 Laboratorio | Itsenäinen; vain NumPy ja SciPy; tuotavat puhtaat funktiot sekä `main()`-raportti. |

Testit ovat kansiossa `tests/test_module_NN.py` ja lataavat laboratorion yhteisellä `sim`-fixtuurilla (aseta tiedoston alkuun `FOLDER = "Module_NN_Name"`).

## Säännöt laboratoriokoodille

1. **Ei kehämäistä varmistusta.** Älä koskaan johda parametria vastauksesta ja sitten „vahvista“ vastausta. Jos tulos on taattu rakenteesta, sano se kommentissa äläkä esitä sitä todisteena.
2. **Ei kovakoodattuja tuomioita.** Jokainen tulostettu johtopäätös on laskettava.
3. **Näytä missä se pettää.** Jokainen laboratorio sisältää ainakin yhden laskun, joka testaa tarinan väitettä mittausta vasten — ei vain niitä osia, jotka pitävät paikkansa.
4. **Testien täytyy voida epäonnistua.** Tarkista analyyttiset rajat, skaalauslait ja julkaistut arvot — ei arvoja, jotka koodi kopioi itsestään.
5. Pidä jokainen testitiedosto alle muutamassa sekunnissa.

## Säännöt viittauksille

- Viittaa vain lähteisiin, jotka olet tarkistanut: tekijät, vuosi, lehti, nide ja sivu.
- Suosi primäärisiä artikkeleita ja vakiokirjoja. Kiistanalaisessa väitteessä viittaa molempiin puoliin.
- Sano „ei näyttöä“ selvästi ja ystävällisesti, kun se on tiedon tila.

## Ennen pull requestin avaamista

```bash
python -m pip install -r requirements.txt
python -m pytest
```

Jos muutat englanninkielistä oppituntia, mainitse se pull requestissa, jotta käännökset voidaan päivittää.

**Huom:** Käännöskansiot (kuten tämä) sisältävät tarinat, maailmansisäiset todistukset ja `SCIENCE.md`-sivut. Laboratoriot (`simulation.py`) pysyvät englanninkielisen repon juuressa — älä kopioi niitä käännöksiin. Laboratoriolinkit osoittavat juureen polulla `../../../Module_NN_Name/simulation.py`.
