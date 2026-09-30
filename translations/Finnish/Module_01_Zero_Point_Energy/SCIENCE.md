# 🔬 Moduuli 1 — Tarinan takana oleva tiede

> [Oppitunti](readme.md) kerrotaan vuodesta 2420. Tämä sivu on vuoden 2025 todellisuustarkistus: mikä on vakiintunutta, missä tarinan väite pettää, ja mitä pitäisi olla totta, jotta se toimisi. Kaikki tässä voidaan tarkistaa [laboratoriokoodilla](../../../Module_01_Zero_Point_Energy/simulation.py).

## Vuoden 2420 väite yhdessä lauseessa

Tyhjä avaruus on korkeapaineinen nollapistenergian „meri“, ja moottorin tarvitsee vain avata siihen venttiili saadakseen ilmaista tehoa.

## Taso 1 — Mikä on totta

**Tyhjiö ei ole „ei mitään“.** Kvanttimekaniikka sanoo, ettei harmoninen oskillaattori voi koskaan olla täysin paikallaan: sen alin energia on $E_0 = \tfrac12\hbar\omega$, ei nolla. Sähkömagneettinen kenttä on kokoelma tällaisia oskillaattoreita, yksi moodia kohti, joten vaikka jokainen fotoni poistettaisiin, jokainen moodi säilyttää $\tfrac12\hbar\omega$:nsa. Tämä nollapistenergia kuuluu standardifysiikkaan, ja sillä on mitattavia seurauksia (Lamb-siirtymä, spontaani emissio ja alla oleva).

**Casimir-ilmiö.** Aseta kaksi rinnakkaista varaamatonta peiliä etäisyydelle $d$. Niiden väliin mahtuvat vain sinne sopivat moodit, kun taas ulkopuolella kaikki moodit ovat olemassa. Nollapistenergian ero antaa vetovoiman. Täydellisille peileille (Casimir, 1948):

$$\frac{E}{A} = -\frac{\pi^2\hbar c}{720\,d^3}, \qquad P = -\frac{\partial (E/A)}{\partial d} = -\frac{\pi^2\hbar c}{240\,d^4}.$$

Laboratorio arvioi nämä CODATA-vakioilla: $P \approx -1.30\times10^{-3}$ Pa etäisyydellä $d = 1\ \mu$m ja $\approx -13$ Pa etäisyydellä 100 nm. Yhteen ilmakehään päästään vasta noin 11 nm:ssä. Voima on mitattu, ensin vakuuttavasti Lamoreaux’n toimesta (1997, pallo–levy, 0,6–6 µm), sitten AFM:llä Mohideen & Roy (1998) ja rinnakkaislevyillä Bressi et al. (2002).

**Oikeat peilit.** Oikeat metallit lakkaavat heijastamasta plasma taajuutensa $\omega_p$ yläpuolella, joten ideaalikaava yliarvioi voiman lyhyillä etäisyyksillä. Lifshitzin teoria (1956) käsittelee oikeita materiaaleja. Nollalämpötilassa kahdelle identtiselle puolitasolle

$$\frac{E}{A} = \frac{\hbar}{4\pi^2}\int_0^\infty d\xi\int_0^\infty k\,dk \sum_{\mathrm{TE,TM}} \ln\!\left(1 - r^2 e^{-2\kappa d}\right), \qquad \kappa = \sqrt{k^2 + \xi^2/c^2},$$

Fresnel-kertoimilla imaginäärisellä taajuudella $i\xi$:

$$r_{\mathrm{TE}} = \frac{\kappa - K}{\kappa + K},\qquad r_{\mathrm{TM}} = \frac{\varepsilon\kappa - K}{\varepsilon\kappa + K},\qquad K = \sqrt{k^2 + \varepsilon(i\xi)\,\xi^2/c^2}.$$

Kullalle laboratorio käyttää Drude-mallia $\varepsilon(i\xi) = 1 + \omega_p^2/[\xi(\xi+\gamma)]$ arvoilla $\hbar\omega_p = 9.0$ eV ja $\hbar\gamma = 35$ meV. Integraattori tarkistetaan kolmella tavalla: $r = 1$ toistaa Casimirin suljetut muodot tarkkuudella $10^{-6}$; paine on $-\partial(E/A)/\partial d$; ja subnanometrin raoilla se muuttuu ei-retardoiduksi van der Waals -vetovoimaksi, $E/A \to -A_H/(12\pi d^2)$, Hamaker-vakiolla $A_H \approx 2.1\times10^{-19}$ J, joka vastaa riippumatonta yksiulotteista integraalia 0,1 %:iin.

| $d$ | kulta / täydellinen peili |
|---|---|
| 10 nm | 0.08 |
| 100 nm | 0.44 |
| 1 µm | 0.88 |
| 10 µm | 0.98 |

## Taso 2 — Missä väite pettää

**1. Nollapistenergia on lattia, ei säiliö.** Se on *perustilan* energia, alin tila jossa kenttä voi olla. Energian ottaminen tarkoittaisi siirtymistä alempaan tilaan — eikä sellaista ole. Sukellusvertaus pettää juuri tässä: merivesi voi virrata sisään, koska sukellusveneen sisäpuoli on matalammassa paineessa. Mikään ei voi olla „matalammassa paineessa“ kuin tyhjiön perustila.

**2. Casimir-ontelo on jousi, ei kaivo.** Voima riippuu vain asemasta, joten se on konservatiivinen. Voit saada työn kerran antamalla levyjen napsahtaa yhteen, mutta joudut maksamaan saman työn vetääksesi ne erilleen. Laboratorio integroi voiman suljetun kierron ympäri (1 µm → 100 nm → 1 µm) käyttäen eri näytteenottoruudukoita kahdelle iskulle, jotta vastaus ei ole rakennettu sisään:

| Levyt (1 m²) | saatu työ sisäänpäin | maksettu työ ulospäin | netto |
|---|---|---|---|
| täydelliset peilit | $+4.33\times10^{-7}$ J | $-4.33\times10^{-7}$ J | $\sim10^{-13}$ J (kvadratuurivirhe, $\sim10^{-6}$ iskusta) |
| kulta | $+2.24\times10^{-7}$ J | $-2.24\times10^{-7}$ J | $\sim10^{-13}$ J |

Jopa yksisuuntainen romahtaminen on pieni. Neliömetri täydellisiä peilejä putoamassa 1 µm:stä 10 nm:iin antaa enintään $4.3\times10^{-4}$ J. AA-paristo sisältää noin $10^4$ J.

**3. Liikkuvat peilit tekevät valoa, mutta energia tulee moottorista.** Dynaaminen Casimir-ilmiö on todellinen. Wilson et al. (2011) moduloivat suprajohtavan piirin tehollista pituutta gigahertsitaajuuksilla ja havaitsivat fotonipareja tyhjiöstä. Jokaisen parin energia summautuu yhteen pumpun kvanttiin ($\hbar\omega_1 + \hbar\omega_2 = \hbar\omega_\text{drive}$), joten ulostuleva teho tulee pumpusta. Se on tapa *muuntaa* energiaa, ei löytää sitä.

**4. „10⁹⁵ g/cm³“ -meri on ristiriidassa painovoiman kanssa.** Tarinan luku tulee Planck-tiheydestä $c^5/(\hbar G^2) \approx 5\times10^{96}$ kg/m³ $\approx 5\times10^{93}$ g/cm³, joka saadaan summaamalla $\tfrac12\hbar\omega$ moodeihin Planck-pituuteen asti. Energia gravitoi, ja tyhjiöenergia, jonka universumin laajeneminen todella näyttää (pimeä energia), on vain

$$\rho_\Lambda c^2 = \Omega_\Lambda\,\frac{3H_0^2c^2}{8\pi G} \approx 5\times10^{-10}\ \text{J/m}^3.$$

Naiivi arvio, $\hbar c\,k_\text{max}^4/(16\pi^2)$ arvolla $k_\text{max} = 1/\ell_P$, on noin $3\times10^{111}$ J/m³. Se on **~10¹²¹** kertaa liikaa — *kosmologisen vakion ongelma* (Weinberg, 1989). Tämä on avoin ongelma, mutta se osoittaa päinvastaiseen suuntaan kuin tarina: mitä tyhjiö tekeekään, se ei toimi kuin valtava säiliö.

**5. Tyhjiö ei työnnä kuten vesi.** Lorentz-invariantilla tyhjiöenergialla on paine $p = -\rho c^2$, jännitys eikä murskaava paine. Sama joka kehyksessä ja suunnassa — ei gradienttia, ja vain gradientti antaa voiman. Casimir-voima syntyy, koska levyt muuttavat moodirakennetta, ja se katoaa kun levyt poistetaan.

Maailmansisäinen „todistus“ sanoo myös, että Fermin heikon vuorovaikutuksen teoria epäonnistuu korkeilla energioilla „jos avaruuden panosta ei huomioida“. Fermi-teoria kyllä murtuu (muutaman sadan GeV:n kohdilla). Se korjattiin sähköheikolla teorialla, jonka ennustamat W- ja Z-bosonit löydettiin CERNissä 1983 — ei tyhjiöenergian ottamisella.

## Taso 3 — Mitä pitäisi olla totta

Jotta tyhjiömoottori toimisi, ainakin yksi näistä pitäisi löytää. Jokainen on testattavissa:

- **Tila tyhjiön alapuolella.** Mikä tahansa järjestelmä, joka antaa nettotyön „tyhjiöstä“ suljetussa kierrossa, olisi alempienergiatila kuin perustila. Tarkkuus-Casimir-kokeet mittaavat voimia 1 %:n tasolla. Kierto, joka palauttaa nettotyön, näkyisi hystereesisilmukkana voima vs. etäisyys -kuvassa. Sellaista ei ole nähty.
- **Ei-konservatiiviset Casimir-voimat.** Voima, joka riippuisi liikkeen suunnasta (ei vain asemasta) nollalämpötilassa, olisi uutta fysiikkaa. Kitkamainen „kvanttikitka“ sivuttain liukuvien pintojen välillä on ennustettu mutta pieni, ja sekin ottaa energian *liikkeestä*.
- **Kosmologisen vakion ongelman ratkaisu, joka jättää valtavan käyttökelpoisen energian.** Ehdokasratkaisut (supersymmetriset kumoamiset, antropinen valinta, muokattu painovoima) tekevät tehollisesta tyhjiöenergiasta pienen. Mikään ei tee siitä suurta ja saavutettavaa.

Avoimia kysymyksiä, jotka ovat oikeasti kiinnostavia: miksi havaittu tyhjiöenergia on niin pieni mutta ei nolla; voidaanko Casimir-voimia tehdä hylkiviksi käytännön nanokoneille (voidaan joissain väliaineissa: Munday, Capasso & Parsegian, *Nature* **457**, 170 (2009)); ja miten lämpötila ja materiaalin vaste yhdistyvät mikrometriskaalalla — edelleen aktiivinen keskustelu.

## Aja laboratorio

```bash
python Module_01_Zero_Point_Energy/simulation.py
python -m pytest tests/test_module_01.py
```

| Koe | Mitä se näyttää |
|---|---|
| `casimir_pressure_ideal`, `casimir_energy_ideal` | Casimirin suljetut muodot: tyhjiö todella työntää, voimakkaasti vain nanometreissä. |
| `lifshitz_pressure`, `lifshitz_energy`, `gold_reduction_factor` | Oikeat kultalevyt numeerisella integraatiolla imaginäärisen taajuuden yli; heikompi kuin ideaali, lähestyy sitä mikrometreissä. |
| `hamaker_constant` | Riippumaton tarkistus lyhyen kantaman (van der Waals) rajalle. |
| `closed_cycle_work`, `one_shot_energy` | Suljettu kierto antaa nollan nettotyön; yksisuuntainen romahtaminen antaa pienen, ei-toistettavan energian. |
| `planck_density`, `naive_vacuum_energy_density`, `observed_dark_energy_density`, `cosmological_constant_gap` | ~10¹²¹:n kuilu naiivin „meren“ ja painovoiman mittauksen välillä. |

## Kokeile itse

1. Vaihda `GOLD_PLASMA_EV` alumiinin ≈ 12,5 eV:iin. Miten kulta/ideaali -suhde 100 nm:ssä muuttuu, ja miksi korkeampi plasma taajuus auttaa?
2. Käytä `casimir_pressure_ideal`-funktiota löytääksesi etäisyyden, jossa Casimir-paine vastaa auringonvalon painetta peiliin (noin 9 µPa).
3. Yritä suunnitella huijauskierto: anna `closed_cycle_work`-funktiolle painefunktio, joka on ideaalilaki sisäänpäin ja kultalaki ulospäin. Saat nettotyön — selitä nyt, minkä fysikaalisen prosessin pitäisi vaihtaa levyjen materiaalia 100 nm:ssä, ja mitä se maksaisi.
4. Funktiossa `naive_vacuum_energy_density`, millä katkaisulla $k_\text{max}$ naiivi arvio vastaisi havaittua pimeän energian tiheyttä? Muunna se pituudeksi. (Pitäisi saada kymmeniä mikrometrejä, murto-osa millimetristä — yksi syy miksi painovoiman submillimetritestit ovat kiinnostavia.)

## Viitteet

- Casimir, H. B. G., "On the attraction between two perfectly conducting plates", *Proc. K. Ned. Akad. Wet.* **51**, 793 (1948).
- Lifshitz, E. M., "The theory of molecular attractive forces between solids", *Sov. Phys. JETP* **2**, 73 (1956).
- Lamoreaux, S. K., "Demonstration of the Casimir force in the 0.6 to 6 µm range", *Phys. Rev. Lett.* **78**, 5 (1997).
- Mohideen, U. & Roy, A., "Precision measurement of the Casimir force from 0.1 to 0.9 µm", *Phys. Rev. Lett.* **81**, 4549 (1998).
- Bressi, G., Carugno, G., Onofrio, R. & Ruoso, G., "Measurement of the Casimir force between parallel metallic surfaces", *Phys. Rev. Lett.* **88**, 041804 (2002).
- Lambrecht, A. & Reynaud, S., "Casimir force between metallic mirrors", *Eur. Phys. J. D* **8**, 309 (2000). Source of the gold Drude parameters.
- Bordag, M., Mohideen, U. & Mostepanenko, V. M., "New developments in the Casimir effect", *Phys. Rep.* **353**, 1 (2001).
- Wilson, C. M. et al., "Observation of the dynamical Casimir effect in a superconducting circuit", *Nature* **479**, 376 (2011).
- Munday, J. N., Capasso, F. & Parsegian, V. A., "Measured long‑range repulsive Casimir–Lifshitz forces", *Nature* **457**, 170 (2009).
- Weinberg, S., "The cosmological constant problem", *Rev. Mod. Phys.* **61**, 1 (1989).
- Planck Collaboration (Aghanim, N. et al.), "Planck 2018 results. VI. Cosmological parameters", *Astron. Astrophys.* **641**, A6 (2020).
