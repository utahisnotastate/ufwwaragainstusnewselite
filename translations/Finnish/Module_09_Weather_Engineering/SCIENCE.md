# 🔬 Moduuli 9 — Tarinan takana oleva tiede

> [Oppitunti](readme.md) kerrotaan vuodesta 2420. Tämä sivu on vuoden 2025 todellisuustarkistus: mikä on vakiintunutta, missä tarinan väite pettää, ja mitä pitäisi olla totta, jotta se toimisi. Kaikki tässä voidaan tarkistaa [laboratoriokoodilla](../../../Module_09_Weather_Engineering/simulation.py).

## Vuoden 2420 väite yhdessä lauseessa

Kaksi näkymätöntä „skalaari“‑ (pitkittäistä) sädettä, jotka kulkevat harmittomasti Maan läpi, voidaan risteyttää missä tahansa taivaalla synnyttämään välittömiä kuumia tai kylmiä taskuja, ja näiden taskujen ruudukko ohjaa myrskyjä ja suihkuvirtausta sähköisesti.

## Taso 1 — Mikä on totta

**Ilmakehä todella on sähköinen piiri.** Ionosfääri istuu karkeasti $+250$ kV:ssa suhteessa maahan. Kauniilla säällä tämä ajaa pienen alaspäin suuntautuvan virran, noin $2$ pA/m², heikosti johtavan ilman läpi, pintakentällä noin $100$–$130$ V/m. Maailman ukkosmyrskyt toimivat akkuna, joka pitää sen ladattuna. Laboratorio muuntaa nämä tyypilliset arvot kokonaissummiksi:

| Suure | Miten se lasketaan | Laboratorion arvo |
|---|---|---|
| Kokonaisvirta | $J \times 4\pi R_\oplus^2$ | ≈ 1 kA |
| Teho | $V_\text{ion} \times I$ | ≈ 250 MW |
| Maan pintavaraus | $\varepsilon_0 E \times 4\pi R_\oplus^2$ (Gauss) | ≈ $5\times10^5$ C |
| Ilman johtavuus maassa | $J/E$ | ≈ $2\times10^{-14}$ S/m |
| Purkausaika ilman myrskyjä | $\varepsilon_0/\sigma$ | ≈ 9 minuuttia |

**Sähkö voi työntää ilmaa.** Voimakkaassa kentässä kiihdytetyt ionit raahaavat neutraaleja molekyylejä mukanaan: tämä on „ionituuli“ eli elektrohydrodynaaminen työntö. Virralle $I$, joka ylittää raon $d$ ionin liikkuvuudella $\mu$, yksiulotteinen työntö on $T = I d/\mu$, joten työntö wattia kohti on $T/P = d/(\mu V)$. MIT lensi 5 m:n siipivälin lentokonetta ilman liikkuvia osia tällä periaatteella (Xu et al., 2018).

**Pilvet muodostuvat hiukkasille, ja teoria sanoo tarkalleen milloin.** Vesi ei tiivisty itsestään ilman kosteuksissa. Se tiivistyy pienille hiukkasille (pilven tiivistymisytimet), kuten merisuolalle. Köhlerin teoria (1936) antaa tasapainokylläisyyssuhteen liuospisaralle säteellä $r$, joka sisältää suolamassan $m_s$:

$$S(r) = a_w \exp\!\left(\frac{A}{r}\right) \;\approx\; 1 + \frac{A}{r} - \frac{B}{r^3}, \qquad A = \frac{2\sigma M_w}{R T \rho_w},\quad B = \frac{3\, i\, m_s M_w}{4\pi \rho_w M_s}.$$

Kaarevuustermi (Kelvin) $A/r$ saa pienet pisarat haihtumaan; liuennut suola (Raoult) $B/r^3$ alentaa höyrynpainetta. Käyrällä on huippu kohdassa

$$r_c = \sqrt{3B/A}, \qquad S_c - 1 = \sqrt{\frac{4A^3}{27B}} \;\propto\; m_s^{-1/2}.$$

Laboratorio löytää täyden lausekkeen huipun numeerisesti ja vahvistaa $S_c - 1 \propto m_s^{-1/2}$ ja $r_c \propto m_s^{1/2}$. NaCl:lle ($i \approx 2$) se antaa:

| Kuiva halkaisija | Kriittinen ylikylläisyys | Ristivalvonta: κ‑Köhler mitatulla κ = 1,28 |
|---|---|---|
| 20 nm | 1,14 % | 1,16 % |
| 50 nm | 0,29 % | 0,29 % |
| 100 nm | 0,10 % | 0,10 % |
| 200 nm | 0,036 % | 0,037 % |

Huipun alapuolella pisara on vakaa **utu**‑hiukkanen. Utua on selvästi alle 100 %:n kosteudessa: suolakide liukenee (delikvesoi) noin 75 % RH:ssa, ja laboratorio laskee 75,5 % liuoksen veden aktiivisuudesta. Vain kun ilman ylikylläisyys ylittää $S_c$:n, pisara kasvaa rajatta ja muuttuu pilvipisaraksi („aktivoituminen“). Oikeat pilvet ylittävät harvoin noin 1 %:n ylikylläisyyden, siksi hiukkaspopulaatio, ei jännite, päättää missä pisarat muodostuvat.

**Ionit todella auttavat tekemään uusia hiukkasia.** Varaus vakauttaa pieniä molekyyliklustereita. CERN:n CLOUD‑koe (Kirkby et al., 2011) osoitti, että kosmisen säteilyn ionisaatio lisää mitattavasti nopeutta, jolla rikkihappo–ammoniakki‑hiukkasia muodostuu. Nuo hiukkaset ovat nanometrien kokoisia ja niiden täytyy kasvaa tunteja tai päiviä ennen kuin ne ovat tarpeeksi suuria siementämään pilviä.

**Pilvisiementäminen on totta mutta vaatimatonta.** Hopeajodidin siementäminen sopivissa talvipilvissä vuorilla on suoraan havaittu tuottavan ylimääräistä lumisadetta (French et al., 2018). Kokonaisten vuodenaikojen ja alueiden yli vaikutus on pieni ja vaikea todistaa tilastollisesti.

**HAARP on totta.** Se on ionosfääritutkimuslaitos Alaskassa, jonka korkeataajuuslähettimellä on 3,6 MW tehoa. Se lämmittää pieniä ionosfäärin laikkuja, kauas sään yläpuolella (sää elää alimmassa ~15 km:ssä). Säävaikutusta ei ole osoitettu.

**Kohdentaminen on totta.** Suurennuslasi tekee kuuman pisteen, koska se kerää valoa suuresta alueesta pieneen. Kaksi risteävää sädettä tekevät myös kirkkaita ja tummia juovia siellä, missä ne interferoivat.

## Taso 2 — Missä väite pettää

**1. Tyhjässä avaruudessa ei ole pitkittäisiä radioaaltoja.** Tyhjiössä Gaussin laki kuuluu $\nabla\cdot\mathbf E = 0$. Aallolle $\mathbf E_0 e^{i\mathbf k\cdot\mathbf x}$ se tarkoittaa $\mathbf k\cdot\mathbf E_0 = 0$: kentän on oltava kohtisuorassa kulkusuuntaan. Potentiaalien „skalaari“‑ ja pitkittäisosat voidaan muuttaa mittamuunnoksella ilman, että mikään mitattava kenttä muuttuu, eivätkä ne kanna energiaa. Whittaker (1903) osoitti, että kentät voidaan *kirjoittaa* kahden skalaarifunktion avulla. Tämä on tavallisen sähkömagnetismin matemaattinen uudelleenkirjoitus, ei uusi aaltolaji. Pitkittäisiä sähkökenttäaaltoja on olemassa plasmaissa (Langmuir‑aallot), mutta ne tarvitsevat plasman olemassaolon eivätkä kulje kiven tai valtameren läpi.

**2. Radioaallot eivät kulje Maan läpi.** Johtimet absorboivat sähkömagneettisia aaltoja ihosyvyyden $\delta \approx \sqrt{2/(\omega\mu_0\sigma)}$ sisällä. Laboratorio käyttää tarkkaa kaavaa:

| Taajuus | Merivesi ($\sigma$ = 4 S/m) | Kivi ($\sigma$ = 10⁻³ S/m) |
|---|---|---|
| 10 Hz | 80 m | 5 km |
| 1 kHz | 8 m | 500 m |
| 1 MHz | 0,25 m | 21 m |

1000 km:n kiven jälkeen jopa 10 Hz:n aalto säilyttää murto‑osan $e^{-199} \approx 10^{-87}$ amplitudistaan. Siksi sukellusveneisiin otetaan yhteyttä erittäin matalilla taajuuksilla ja valtavilla antenneilla, ja silloinkin vain lähellä pintaa.

**3. Risteävät säteet siirtävät energiaa; ne eivät voi luoda sitä eivätkä poistaa sitä.** Missä kaksi koherenttia sädettä intensiteeteillä $I_1$ ja $I_2$ limittäin, aika‑keskiarvoistettu intensiteetti on

$$I = I_1 + I_2 + 2\sqrt{I_1 I_2}\cos\Delta\phi .$$

Tummat juovat ovat aina pareina kirkkaiden kanssa, ja keskiarvo kuvion yli on täsmälleen $I_1 + I_2$. Laboratorio tarkistaa molemmat. „Kylmä moodi“, jossa risteyskohta imee lämmön ilmasta, tarvitsisi negatiivisen intensiteetin. Ilman jäähdyttäminen tarkoittaa sen lämmön pumppaamista jonnekin muualle, mikä vaatii työtä ja joutuu dumppaamaan vielä muuta lämpöä lähelle (termodynamiikan toinen pääsääntö). Suurennuslasi ei myöskään voi tehdä kylmää pistettä.

**4. Sää on valtavan paljon voimakkaampi kuin mikään sähköinen vipu.** Säää ajaa auringonvalo ($\approx 1{,}2\times10^{17}$ W Maan absorboimana) ja latenttilämpö, joka vapautuu vesihöyryn tiivistyessä:

| Energian lähde tai nielu | Laboratorion arvo |
|---|---|
| Yksi ukkosmyrsky (2 cm sadetta 5 km:n säteellä) | ≈ $4\times10^{15}$ J |
| Keskimääräinen hurrikaani (1,5 cm/vrk sadetta 665 km:n säteellä, NOAA:n menetelmä) | ≈ $6\times10^{14}$ W |
| Ilman lämmittäminen 100 km × 100 km vain 1 K | ≈ $10^{17}$ J |
| Koko globaali sähköpiiri | ≈ $2{,}5\times10^{8}$ W |
| HAARP‑lähetin | $3{,}6\times10^{6}$ W |
| Suuri maahan sijoitettu ioniryhmä (100 kV × 1 mA) | 100 W |

Teholla 100 W 1 K:n lämmitys veisi noin 30 miljoonaa vuotta. Vaikka kaikki HAARP:n teho absorboituisi alailmakehään (se ei absorboidu), se veisi noin 900 vuotta. Hurrikaani ylittää ioniryhmän tehon kertoimella noin $6\times10^{12}$. Tuon ryhmän ionituuli on työntö noin 0,25 N, 25 g:n esineen paino, sovellettuna sääjärjestelmiin, joissa on miljardeja tonneja liikkuvaa ilmaa.

**5. Ionit eivät voi tehdä pilviä suoraan.** Thomsonin teoria pisaran muodostumisesta varaukselle lisää sähköstaattisen termin puhtaan vesipisaran klassiseen vapaaseen energiaan:

$$\Delta G(r) = -\tfrac43\pi r^3 n_l k T\ln S \;+\; 4\pi r^2\sigma \;+\; \frac{q^2}{8\pi\varepsilon_0}\left(1-\frac{1}{\varepsilon_r}\right)\left(\frac1r - \frac1{r_0}\right).$$

Kun $S \le 1$, bulkkitermi on positiivinen, joten $\Delta G$:llä ei ole maksimia eikä kriittistä sädettä ole olemassa: pisarat eivät koskaan kasva, varauksella tai ilman. Kun $S > 1$, varaus alentaa estettä, mutta laboratorio löytää, että este putoaa vain ~60 kT:hen (karkeasti yksi pisara cm³:tä kohti sekunnissa) arvoilla $S \approx 4{,}1$ neutraaleille klustereille ja $S \approx 2{,}5$ yhdellä alkeisvarauksella. C. T. R. Wilsonin 1890‑luvun pilvikammiot löysivät samanlaisen luvun: ionit laukaisevat pisaroita vain muutaman sadan prosentin ylikylläisyyksissä. Realistisella $S = 1{,}01$:llä este on yli $10^6$ kT. Oikeassa ilmassa suola ja muut hiukkaset aktivoituvat alle 1 %:n ylikylläisyydessä, kauan ennen kuin ionit merkitsevät. (Jatkumoteoria on karkea vain muutaman molekyylin klustereille; järjestys, ei tarkat numerot, on kestävä.)

**6. Maahan sijoitetut ionisaattorit sateelle.** Useat kaupalliset hankkeet ovat väittäneet sateen lisäämistä maahan sijoitettujen ionisaattoriryhmien avulla. Tähän mennessä julkaistu näyttö on heikkoa ja kiistanalaista: pieniä väitettyjä vaikutuksia, ei riippumattomia satunnaistettuja kokeita, eikä hyväksyttyä mekanismia, joka veisi ylimääräisistä ioneista ylimääräiseen sateeseen realistisissa ylikylläisyyksissä.

**7. „Ilmaseinä yhtä kova kuin betoni.“** Vakiopaineessa ilman jäähdyttäminen 30 K nostaa sen tiheyttä vain noin 10 % ($\rho \propto 1/T$). Mikään lämpötilan muutos ei saa ilmaa käyttäytymään kuin kiinteä aine ohjukselle.

## Taso 3 — Mitä pitäisi olla totta

- **Uusi, pitkän kantaman kenttä**, joka etenee kiven ja valtameren läpi mitättömällä häviöllä, ei ole tavallinen sähkömagneettinen aalto, ja kytkeytyy voimakkaasti ilmaan. Se näkyisi myös sähkömagnetismin tarkkuustesteissä. Fotoni, jolla on pieni massa, omaisi pitkittäisen moodin, mutta laboratorion ja astrofysiikan ylärajat fotonin massalle ovat poikkeuksellisen pieniä (Particle Data Group listaa rajoja luokkaa $10^{-18}$ eV).
- **Energianlähde, joka vastaa säätä**: vähintään $10^{15}$–$10^{17}$ J tapahtumaa kohti, toimitettuna tunneissa. Se on 1 GW:n voimalaitoksen koko tuotanto päivistä vuosiin, ja se pitäisi säteillä taivaalle lämmittämättä mitään matkalla.
- **Testattavat kohteet**: kontrolloitu, satunnaistettu koe, jossa laite (ionisaattoriryhmä, säde tai muu) tuottaa tilastollisesti merkitsevän muutoksen sademäärässä tai paineessa verrattuna käsittelemättömiin kontrollipäiviin, toistettuna riippumattomien ryhmien toimesta. Se on pilvisiementämiseen sovellettu standardi, ja syy miksi sen mitattuja vaikutuksia kuvataan vaatimattomiksi.
- **Avoimet kysymykset, jotka ovat oikeaa tiedettä**: kuinka paljon kosmisen säteilyn ionit vaikuttavat pilvipeitteeseen (CLOUD:n tulokset viittaavat siihen, että vaikutus nykypäivän ilmastoon on pieni); miten globaali sähköpiiri reagoi muuttuvaan ukkostoimintaan; miten tehdä EHD‑propulsiosta tehokkaampaa.

## Aja laboratorio

```bash
python Module_09_Weather_Engineering/simulation.py
python -m pytest tests/test_module_09.py
```

| Koe | Mitä se näyttää |
|---|---|
| `global_circuit` | Maan kauniin sään piirin virta, teho, varaus ja johtavuus. |
| `saturation_ratio`, `critical_point`, `equilibrium_radius` | Köhlerin teoria: utu alle 100 % RH, aktivoituminen $S_c$:n yläpuolella, $S_c - 1 \propto m_s^{-1/2}$. |
| `deliquescence_rh` | Miksi suolakiteet liukenevat ~75 % RH:ssa (ja miksi ideaaliliuosvastaus on liian korkea). |
| `thomson_free_energy`, `nucleation_barrier`, `saturation_for_barrier` | Ionit alentavat nukleaatioestettä, mutta vain ylikylläisyyksissä kauas oikeiden pilvien yli. |
| `ion_wind_thrust`, `thrust_per_power` | Ionituuli on totta mutta tuottaa pieniä voimia. |
| `rain_latent_heat`, `hurricane_heat_power`, `column_heating_energy` | Sään energiabudjetti vs. jokainen sähköinen vipu. |
| `crossed_beams`, `skin_depth` | Interferenssi uudelleenjakaa energiaa; radioaallot kuolevat metreissä kilometreihin maassa ja meressä. |

## Kokeile itse

1. Käytä `critical_point`-funktiota löytääksesi kuivan NaCl‑halkaisijan, joka aktivoituu täsmälleen 0,5 %:n ylikylläisyydessä. Tarkista sitten vastauksesi funktiolla `kappa_critical_saturation`.
2. Piirrä `saturation_ratio` 50 nm:n hiukkaselle kuivasta säteestä 10 µm:iin (käytä mitä tahansa piirtotyökalua). Merkitse utuhaara, huippu ja aktivoitunut haara.
3. Muuta `eps_r` funktiossa `thomson_free_energy` arvosta 80 arvoon 1. Mitä tapahtuu varauksen hyödylle, ja miksi?
4. Kuinka monta 1 GW:n voimalaitosta, käyden yhden päivän, tarvittaisiin labin ukkosmyrskyn latenttilämmön vastaamiseen?
5. Käyttäen `skin_depth`-funktiota, löydä taajuus, jossa aalto menettää vain puolet amplitudistaan 100 m:ssä merivettä. Kuinka pitkä antenni tuolle taajuudelle pitäisi olla (ota neljännesaaltopituus)?

## Viitteet

- Köhler, H., "The nucleus in and the growth of hygroscopic droplets", *Trans. Faraday Soc.* **32**, 1152 (1936).
- Petters, M. D. & Kreidenweis, S. M., "A single parameter representation of hygroscopic growth and cloud condensation nucleus activity", *Atmos. Chem. Phys.* **7**, 1961 (2007).
- Pruppacher, H. R. & Klett, J. D., *Microphysics of Clouds and Precipitation*, 2nd ed., Kluwer (1997). Köhler and Thomson theory, ion‑induced nucleation.
- Rogers, R. R. & Yau, M. K., *A Short Course in Cloud Physics*, 3rd ed., Pergamon (1989).
- Seinfeld, J. H. & Pandis, S. N., *Atmospheric Chemistry and Physics*, 3rd ed., Wiley (2016). Deliquescence and CCN activation.
- Robinson, R. A. & Stokes, R. H., *Electrolyte Solutions*, 2nd ed., Butterworths (1959). Osmotic coefficients of NaCl solutions.
- Kirkby, J. et al., "Role of sulphuric acid, ammonia and galactic cosmic rays in atmospheric aerosol nucleation", *Nature* **476**, 429 (2011).
- Rycroft, M. J., Israelsson, S. & Price, C., "The global atmospheric electric circuit, solar activity and climate change", *J. Atmos. Sol.‑Terr. Phys.* **62**, 1563 (2000).
- Xu, H. et al., "Flight of an aeroplane with solid‑state propulsion", *Nature* **563**, 532 (2018).
- French, J. R. et al., "Precipitation formation from orographic cloud seeding", *Proc. Natl. Acad. Sci. USA* **115**, 1168 (2018).
- Whittaker, E. T., "On the partial differential equations of mathematical physics", *Math. Ann.* **57**, 333 (1903).
- Jackson, J. D., *Classical Electrodynamics*, 3rd ed., Wiley (1999). Transversality of vacuum waves, skin depth.
- Kopp, G. & Lean, J. L., "A new, lower value of total solar irradiance: Evidence and climate significance", *Geophys. Res. Lett.* **38**, L01706 (2011).
- NOAA Atlantic Oceanographic and Meteorological Laboratory, Hurricane Research Division, *Hurricane FAQ* ("How much energy does a hurricane release?"). Source of the rainfall‑based heat‑release method.
