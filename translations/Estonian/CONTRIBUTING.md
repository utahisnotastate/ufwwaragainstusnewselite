# Kaastöö

Aitäh abi eest. Kõige väärtuslikumad panused on **parandused**: vale number, ülepakutud väide, puuduv mööndus või parem viide.

## Mooduli paigutus

Iga `Module_NN_Name/` kaust sisaldab:

| Fail | Roll | Reeglid |
|---|---|---|
| `readme.md` | 📖 2420. aasta looõppetund | Algab pealkirja ja „Loorežiimi“ ribaga, seejärel `Õppetunni pealkiri`, `Allikas`, `Mõiste` täpid ja nummerdatud sektsioonid. Kujutlusvõimeline, aga ei ütle kunagi lugejale, et jätaks päris arstiabi vahele. |
| `PHYSICS_PROOF.md` | 📜 Universumisisene argument | Algab „Universumisisese dokumendi“ ribaga. Sektsioonid: 8‑aastasele, Teema, Aksioom, Mehhanism, Tõestus/Järeldus. |
| `SCIENCE.md` | 🔬 2025. aasta reaalsuskontroll | Sektsioonid: 2420. aasta väide ühes lauses · Tase 1 — Mis on päris · Tase 2 — Kus väide murdub · Tase 3 — Mis peaks olema tõsi · Käivita labor · Proovi ise · Viited. |
| `simulation.py` | 🧪 Labor | Iseseisev; ainult NumPy ja SciPy; imporditavad puhtad funktsioonid pluss `main()` aruanne. |

Testid elavad failides `tests/test_module_NN.py` ja laadivad labori jagatud `sim` fixture’iga (sea faili ülaosas `FOLDER = "Module_NN_Name"`).

Tõlked elavad kaustas `translations/`; laborid (`simulation.py`) jäävad ingliskeelsesse juurkausta ega kuulu tõlkekausta kopeerimisele.

## Reeglid laborikoodile

1. **Ei ringikujulisele kontrollile.** Ära kunagi tuletata parameetrit vastusest ja siis „kinnita“ vastust. Kui tulemus on konstruktsioonist garanteeritud, ütle seda kommentaariga ja ära esita seda tõendina.
2. **Ei kõvakodeeritud otsustele.** Iga trükitud järeldus peab olema arvutatud.
3. **Näita, kus see murdub.** Iga labor sisaldab vähemalt ühte arvutust, mis testib loo väidet mõõtmise vastu, mitte ainult osi, mis on tõesed.
4. **Testid peavad saama ebaõnnestuda.** Kontrolli analüütilisi piire, skaleerimisseadusi ja avaldatud väärtusi, mitte väärtusi, mille kood iseendast kopeeris.
5. Hoia iga testifail mõne sekundi piires.

## Reeglid viidetele

- Viita ainult allikaid, mida oled kontrollinud: autorid, aasta, ajakiri, köide ja lehekülg.
- Eelista esmaseid artikleid ja standardõpikuid. Vaidlustatud väide peaks viitama mõlemale poolele.
- Ütle „tõendeid pole“ selgelt ja lahkel toonil seal, kus see on teadmiste seis.

## Enne pull request’i avamist

```bash
python -m pip install -r requirements.txt
python -m pytest
```

Kui muudad ingliskeelset õppetundi, maini seda pull request’is, et tõlkeid saaks uuendada.
