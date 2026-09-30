# 🔬 Moduuli 7 — Tarinan takana oleva tiede

> [Oppitunti](readme.md) kerrotaan vuodesta 2420. Tämä sivu on vuoden 2025 todellisuustarkistus: mikä on vakiintunutta, missä tarinan väite pettää, ja mitä pitäisi olla totta, jotta se toimisi. Kaikki tässä voidaan tarkistaa [laboratoriokoodilla](../../../Module_07_DNA_Antenna/simulation.py).

## Vuoden 2420 väite yhdessä lauseessa

DNA on käämimäinen antenni, joka vastaanottaa ohjeita informaatiokentästä — myös omista ajatuksistasi ja tunteistasi — ja kirjoittaa kehon uudelleen vastaamaan niitä.

## Taso 1 — Mikä on totta

**DNA:n muoto tunnetaan tarkasti.** B‑DNA, soluissa esiintyvä muoto, on oikeakätinen kaksoiskierre (Watson & Crick 1953; Franklin & Gosling 1953), jolla on

- halkaisija noin **2,0 nm**,
- nousu **0,34 nm** emäsparia kohti,
- noin **10,5 emäsparia kierrosta kohti** liuoksessa (34,3° kiertoa askelta kohti), joten nousukorkeus on **3,4–3,6 nm**.

Se on myös jäykkä lyhyillä etäisyyksillä: sen persistenssipituus on noin 50 nm fysiologisessa suolapitoisuudessa.

**DNA todella vuorovaikuttaa valon kanssa, voimakkaasti, ultraviolettialueella.** DNA absorboi voimakkaimmin lähellä **260 nm** (4,77 eV fotonia kohti). Arkipäiväinen laboratorio‑ohje „absorbanssi 1 aallonpituudella 260 nm tarkoittaa 50 µg/mL kaksijuosteista DNA:ta“ antaa noin **6600 M⁻¹cm⁻¹ nukleotidia kohti**. Kaksoiskierre absorboi karkeasti 30–40 % vähemmän kuin samat emäkset vapaina nukleotideina (laboratorio saa 39 % käyttämällä likimääräisiä oppikirjan nukleotidiarvoja). Tämä **hypokromismi** syntyy, koska pinotut emäkset kytkeytyvät elektronisesti. UV‑virityksen jälkeen viritys voi jakautua usealle pinotulle emäkselle, ja pinoutuminen ohjaa, kuinka nopeasti energia hajoaa (Crespo‑Hernández, Cohen & Kohler 2005). Tämä on oikeaa, nopeaa fysiikkaa, ja se auttaa suojaamaan DNA:ta UV‑vaurioilta. Se toimii muutaman emäksen, muutaman nanometrin matkalla.

**Energia voi hypätä DNA:ta pitkin nanometrien matkalla.** Försterin resonanssienergiansiirto (FRET) siirtää virityksen luovuttajaväristä vastaanottajaan hyötysuhteella

$$E = \frac{1}{1 + (r/R_0)^6},$$

missä $R_0$ on tyypillisesti noin 5 nm. DNA‑kierteen varrelle sijoitetuilla väreillä 15 emäsparin (5,1 nm) etäisyydellä siirretään noin puolet energiasta; 30 emäsparilla osuus on noin 1 %. Tämä jyrkkä $r^{-6}$-lasku on syy, miksi FRET:iä käytetään „spektroskooppisena viivaimena“ (Stryer & Haugland 1967), usein DNA:ta itseään viivaimena käyttäen.

**DNA värähtelee ja „hengittää“.** Peyrard–Bishop‑malli (1989) käsittelee kutakin emäsparia venymänä $y_n$, jota pitää Morse‑potentiaali $V(y) = D\,(e^{-ay} - 1)^2$ (vetysidokset) ja joka on kytketty naapureihinsa pinoutumisjousilla:

$$H = \sum_n \left[\frac{p_n^2}{2m} + \frac{k}{2}(y_n - y_{n-1})^2 + D\,(e^{-a y_n} - 1)^2\right].$$

Pienet värähtelyt muodostavat fononivyön, $m\omega^2 = 2Da^2 + 4k\sin^2(q/2)$, terahertsialueella. Laboratorio tarkistaa tämän numeerista Hessen matriisia vasten. Laboratorio ratkaisee myös mallin termodynamiikan tarkasti siirtymäintegraalimenetelmällä: emäsparit avautuvat hieman enemmän lämpötilan noustessa, ja kynnyksen yläpuolella juosteet irtoavat (denaturaatio eli „sulaminen“). Tässä käytetyillä havainnollistavilla harmonisen pinoutumisen parametreilla se tapahtuu lähellä 490 K:ta, selvästi yli oikean DNA:n 340–370 K:n. Dauxois, Peyrard & Bishop (1993) osoittivat, että epälineaarisen pinoutumisen lisääminen antaa kokeissa nähdyn terävän sulamisen. Asia on laadullinen: DNA:n dynamiikka on tavallista lämpöfysiikkaa.

**Geenejä säätelee ympäristö kemian kautta.** Epigeneettiset merkit (DNA‑metylaatio, histonimodifikaatiot) muuttavat, mitkä geenit ilmentyvät. Ne reagoivat ruokavalioon, hormoneihin ja kokemukseen; rotilla esimerkiksi äidinhoiva muuttaa stressihormonireseptorigeenin metylaatiota jälkeläisissä (Weaver et al. 2004). Signaalit ovat molekyylejä: hormoneja, transkriptiotekijöitä ja entsyymejä.

**„Roska‑DNA:sta“.** Noin 1–2 % ihmisen genomista koodaa proteiineja. Sääntelyelementit (promoottorit, tehostajat) ja ei‑koodaavat RNA:t ovat tosia ja tärkeitä. ENCODE‑projekti (2012) raportoi „biokemiallista funktiota“ 80 %:lle genomista, mutta tuo määritelmä laski mukaan minkä tahansa biokemiallisen aktiivisuuden, kuten kertaluontoisen transkription tai proteiinin sitoutumisen. Sitä kiistettiin voimakkaasti, esimerkiksi Graur et al. (2013), jotka väittivät, että funktion pitäisi tarkoittaa jotain, mitä valinta säilyttää. Evolutiivisen rajoitteen alaisen genomin osuuden arvioidaan olevan paljon pienempi.

## Taso 2 — Missä väite pettää

**1. Jos DNA olisi antenni, se olisi viritetty röntgensäteisiin, ei ajatuksiin tai biofotoneihin.** Kierreantenni säteilee akselinsa suuntaan (Krausin „aksiaalitila“), kun sen ympärysmitta $C$ täyttää $\tfrac34 < C/\lambda < \tfrac43$. B‑DNA:lle $C = \pi \times 2{,}0\text{ nm} = 6{,}3$ nm, joten

$$\lambda \approx 4.7\text{–}8.4\text{ nm} \quad (150\text{–}260\text{ eV}),$$

mikä on äärimmäistä ultraviolettia tai pehmeää röntgensäteilyä, ja se ionisoi molekyylejä. Elävästä kudoksesta raportoitu ultraheikko „biofotoni“‑emissio (200–800 nm; ks. Cifra & Pospíšil 2014) on **30–130 kertaa liian pitkä**. Sen nousukulma (30°) on myös Krausin parhaan alueen 12–14° ulkopuolella. Lisäksi DNA ei ole metallilanka: sen runko ei kuljeta vapaita elektroneja antennin tavoin.

**2. Biofotoneita on aivan liian vähän ohjeiden kantamiseen.** Jopa antelias 100 fotonia sekunnissa neliösenttimetriä kohti, kaikki DNA:lle suunnattuna, osuisi annettuun kierrokseen noin **kerran 4400 vuodessa**.

**3. Suolavesi peittää ja absorboi.** Solut ovat suolaista vettä. Pitoisuudessa 150 mM **Debye‑seulontapituus** on

$$\lambda_D = \sqrt{\frac{\varepsilon_r\varepsilon_0 k_B T}{2 N_A e^2 I}} \approx \frac{0.304}{\sqrt{I\,[\text{M}]}}\ \text{nm} \approx 0.78\text{ nm}.$$

Varauksen sähkökenttä on jo muutamia miljoonasosia 10 nm:n päässä. Värähtelevät kentät pääsevät läpi, mutta suolaveden Debye‑relaatiomalli (johtavuus noin 1,6 S/m) näyttää, että mikroaallot putoavat arvoon $1/e$ noin **2,6 cm:ssä 1 GHz:llä, 2,4 mm:ssä 10 GHz:llä ja 0,24 mm:ssä 100 GHz:llä**. 50 nm:n jäykkä DNA‑segmentti 1 GHz:n dipolina toimisi säteilyvastuksella noin $10^{-11}\ \Omega$, verrattuna noin 50 Ω:iin toimivalle antennille. Se on poikkeuksellisen huono antenni.

**4. Radiofotonit ovat liian heikkoja tekemään kemiaa.** 1 GHz:n fotoni kantaa $1{,}5\times10^{-4}\,k_BT$ kehon lämpötilassa. Molekyylejä tömistää tuhansia kertoja enemmän energiaa joka pikosekunti. Siksi UV (178 $k_BT$ fotonia kohti 260 nm:llä) vaurioittaa DNA:ta ja radio ei.

**5. „Aavelehti“‑ ja „mitogeneettinen säteily“‑tarinat.** Koronapurkaus‑ (Kirlian‑) valokuvauksen kontrolloidut tutkimukset havaitsivat, että kuvat riippuvat voimakkaasti kosteudesta, paineesta ja valotusehdoista (Pehek, Kyler & Faust 1976). „Aavelehti“ ei ole vakiintunut vaikutus. Gurwitschin mitogeneettistä säteilyä ja Kaznatšejevin „sytopaattisen siirron“ väitteitä ei ole vakiinnuttanut riippumaton toisto.

**6. Ei ole näyttöä siitä, että DNA vastaanottaisi „morfogeneettisiä ohjeita“ kentästä.** Se, miten kehot saavat muotonsa, tutkitaan yksityiskohtaisesti, ja se toimii geenien, proteiinien, signaalimolekyyligradienttien sekä solujen välisten mekaanisten ja sähköisten vihjeiden kautta. Tunteesi voivat todella vaikuttaa kehoosi hermojen, hormonien ja immuunijärjestelmän kautta, ja epigenetiikka on osa sitä tarinaa. Mutta sanansaattajat ovat molekyylejä, eivät lähetystä.

## Taso 3 — Mitä pitäisi olla totta

Jotta „DNA antennina“ olisi tieteellinen hypoteesi, jonkun pitäisi osoittaa kaikki nämä:

- **Vastaanotin, joka toimii suolavedessä.** Joko signaalitaajuus, joka läpäisee kudoksen *ja* kytkeytyy 2 nm:n kierteeseen, tai mekanismi (esimerkiksi molekyyliresonanssi), jota seulonta ja lämpökohina eivät pese pois. Mitattava testi: tietty taajuus, joka muuttaa geenien ilmentymistä soluviljelmässä, annos–vaste‑käyrällä, sokkoutuksella ja riippumattomalla toistolla.
- **Riittävästi energiaa signaalia kohti.** DNA‑kemian muuttaminen tarvitsee energioita lähellä elektronivolttia tapahtumaa kohti, tai vahvistimen solun sisällä, joka muuttaa pienen signaalin suureksi vasteeksi voittaen $k_BT$-kohinan.
- **Kantaja „kentän informaatiolle“.** Tarina tarvitsee nimetyn fysikaalisen kentän mittattavalla voimakkuudella ja ennustetulla spektrillä. Sellaisenaan se ei ennusta yhtään lukua, jota voisi tarkistaa.

Läheiset avoimet kysymykset ovat tosia ja kiinnostavia: kuinka kauas varaus voi kulkea DNA:ta pitkin (muutamia nanometrejä, hyppien pinottujen emästen välillä), miten UV‑energia jaetaan pinottujen emästen kesken, miten DNA:n „hengitys“ auttaa proteiineja lukemaan sitä, ja kuinka paljon ei‑koodaavasta genomista merkitsee.

## Aja laboratorio

```bash
python Module_07_DNA_Antenna/simulation.py
python -m pytest tests/test_module_07.py
```

| Koe | Mitä se näyttää |
|---|---|
| `b_dna_geometry`, `helical_antenna_band`, `biophoton_mismatch` | DNA‑kokoinen kierre olisi viritetty ~6 nm:iin (EUV/pehmeä röntgen), 30–130× lyhyempi kuin biofotoni. |
| `photon_hits_per_turn` | Biofotonivuot ovat mitättömän pieniä molekyylimitassa. |
| `uv_absorption` | ~6600 M⁻¹cm⁻¹ nukleotidia kohti 260 nm:llä ja ~39 % hypokromismi pinoutumisesta. |
| `fret_efficiency`, `fret_along_dna` | Energiansiirto DNA:ta pitkin: 50 % ~15 bp:ssä, ~1 % 30 bp:ssä. |
| `pb_mode_frequencies_numeric`, `pb_dispersion`, `pb_transfer_integral` | Peyrard–Bishop‑värähtelyt (THz) sekä lämpöavautuminen ja denaturaatio. |
| `debye_length`, `water_permittivity`, `field_penetration_depth` | 0,78 nm:n seulonta; mikroaallot absorboituvat mm–cm:ssä. |
| `short_dipole_radiation_resistance`, `rf_photon_vs_thermal` | DNA on toivoton RF‑antenni; radiofotoni ≪ $k_BT$. |

## Kokeile itse

1. Käytä `debye_length`-funktiota löytääksesi suolapitoisuuden, jossa seulontapituus yltäisi 1 µm:iin. Voisiko elävä solu selvitä noin puhtaassa vedessä?
2. Muuta `R0_nm` funktiossa `fret_along_dna` arvoihin 3 nm ja 7 nm. Kuinka monta emäsparia 50 %:n piste siirtyy?
3. Funktiossa `pb_transfer_integral` kaksinkertaista `D`. Miten irtoamislämpötila funktiosta `pb_denaturation_temperature` muuttuu? Vertaa `pb_continuum_estimate`-funktioon, joka skaalautuu kuten $\sqrt{kD}$.
4. Ihmisen genomi yhdessä solussa on noin $6{,}4\times10^9$ emäsparia (molemmat kopiot). Käytä `RISE_NM`-arvoa löytääksesi DNA:n kokonaispituuden yhdessä solussa. Jos se olisi suora puoliaaltopituinen dipoli tyhjiössä, mille taajuudelle se olisi viritetty, ja kuinka kauas tuo taajuus kulkisi suolavedessä (`field_penetration_depth`)?
5. Etsi taajuus, jossa `rf_photon_vs_thermal` on yhtä suuri kuin 1 kehon lämpötilassa. Minkä spektrin osa se on?

## Viitteet

- Watson, J. D. & Crick, F. H. C., "Molecular structure of nucleic acids", *Nature* **171**, 737 (1953).
- Franklin, R. E. & Gosling, R. G., "Molecular configuration in sodium thymonucleate", *Nature* **171**, 740 (1953).
- Kraus, J. D., *Antennas*, 2nd ed., McGraw‑Hill (1988). Helical antenna modes.
- Crespo‑Hernández, C. E., Cohen, B. & Kohler, B., "Base stacking controls excited‑state dynamics in A·T DNA", *Nature* **436**, 1141 (2005).
- Cavaluzzi, M. J. & Borer, P. N., "Revised UV extinction coefficients for nucleoside‑5′‑monophosphates and unpaired DNA and RNA", *Nucleic Acids Res.* **32**, e13 (2004).
- Förster, T., "Zwischenmolekulare Energiewanderung und Fluoreszenz", *Ann. Phys.* **437**, 55 (1948).
- Stryer, L. & Haugland, R. P., "Energy transfer: a spectroscopic ruler", *Proc. Natl. Acad. Sci. USA* **58**, 719 (1967).
- Peyrard, M. & Bishop, A. R., "Statistical mechanics of a nonlinear model for DNA denaturation", *Phys. Rev. Lett.* **62**, 2755 (1989).
- Dauxois, T., Peyrard, M. & Bishop, A. R., "Entropy‑driven DNA denaturation", *Phys. Rev. E* **47**, R44 (1993).
- Israelachvili, J. N., *Intermolecular and Surface Forces*, 3rd ed., Academic Press (2011). Debye length.
- Kaatze, U., "Complex permittivity of water as a function of frequency and temperature", *J. Chem. Eng. Data* **34**, 371 (1989).
- Cifra, M. & Pospíšil, P., "Ultra‑weak photon emission from biological samples: definition, mechanisms, properties, detection and applications", *J. Photochem. Photobiol. B* **139**, 2 (2014).
- Pehek, J. O., Kyler, H. J. & Faust, D. L., "Image modulation in corona discharge photography", *Science* **194**, 263 (1976).
- Weaver, I. C. G. et al., "Epigenetic programming by maternal behavior", *Nat. Neurosci.* **7**, 847 (2004).
- ENCODE Project Consortium, "An integrated encyclopedia of DNA elements in the human genome", *Nature* **489**, 57 (2012).
- Graur, D. et al., "On the immortality of television sets: 'function' in the human genome according to the evolution‑free gospel of ENCODE", *Genome Biol. Evol.* **5**, 578 (2013).
