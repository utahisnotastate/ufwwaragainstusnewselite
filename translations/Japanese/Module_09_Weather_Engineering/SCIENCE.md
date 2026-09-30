# 🔬 モジュール9 — 物語の背後にある科学

> [レッスン](readme.md) は2420年の視点で語られます。このページは2025年の現実チェックです：何が確立されているか、物語の主張がどこで破綻するか、それが成り立つには何が真でなければならないか。ここにあるすべては [実験室コード](../../../Module_09_Weather_Engineering/simulation.py) で確認できます。

## 2420年の主張を一文で

地球を無害に通り抜ける2本の見えない「スカラー」（縦）ビームを空のどこでも交差させ、瞬時の熱・冷ポケットを作り、その格子が嵐とジェット気流を電気的に操る。

## レベル1 — 実在すること

**大気は本当に電気回路である。** 電離層は地面に対しておおよそ $+250$ kV にある。晴天では弱く導電する空気を通じて微小な下向き電流、約 $2$ pA/m² が流れ、地表電場は約 $100$–$130$ V/m。世界中の雷雨が充電を保つ電池として働く。実験室は典型値を合計に変える：

| 量 | 計算法 | 実験室の値 |
|---|---|---|
| 総電流 | $J \times 4\pi R_\oplus^2$ | ≈ 1 kA |
| 電力 | $V_\text{ion} \times I$ | ≈ 250 MW |
| 地球表面電荷 | $\varepsilon_0 E \times 4\pi R_\oplus^2$（Gauss） | ≈ $5\times10^5$ C |
| 地表の空気導電率 | $J/E$ | ≈ $2\times10^{-14}$ S/m |
| 嵐なしの放電時間 | $\varepsilon_0/\sigma$ | ≈ 9 分 |

**電気は空気を押せる。** 強場で加速されたイオンが中性分子を引きずる：これが「イオン風」または電気流体力学推力。電流 $I$ が隙間 $d$ をイオン移動度 $\mu$ で横切るとき、一次元推力は $T = I d/\mu$、ワットあたり推力は $T/P = d/(\mu V)$。MIT はこの原理で可動部なしの翼幅 5 m の飛行機を飛ばした（Xu et al., 2018）。

**雲は粒子の上にでき、理論はいつかを正確に言う。** 水は空気中の湿度だけでは自ら凝結しない。海塩などの微小粒子（雲凝結核）の上に凝結する。Köhler 理論（1936）は塩質量 $m_s$ を含む半径 $r$ の溶液滴上の平衡飽和比を与える：

$$S(r) = a_w \exp\!\left(\frac{A}{r}\right) \;\approx\; 1 + \frac{A}{r} - \frac{B}{r^3}, \qquad A = \frac{2\sigma M_w}{R T \rho_w},\quad B = \frac{3\, i\, m_s M_w}{4\pi \rho_w M_s}.$$

曲率（Kelvin）項 $A/r$ は小さな滴を蒸発させ、溶解塩（Raoult）項 $B/r^3$ は蒸気圧を下げる。曲線は

$$r_c = \sqrt{3B/A}, \qquad S_c - 1 = \sqrt{\frac{4A^3}{27B}} \;\propto\; m_s^{-1/2}$$

にピークをもつ。実験室は完全式のピークを数値で見つけ、$S_c - 1 \propto m_s^{-1/2}$、$r_c \propto m_s^{1/2}$ を確認する。NaCl（$i \approx 2$）について：

| 乾燥直径 | 臨界過飽和 | 照合：測定 κ = 1.28 の κ‑Köhler |
|---|---|---|
| 20 nm | 1.14 % | 1.16 % |
| 50 nm | 0.29 % | 0.29 % |
| 100 nm | 0.10 % | 0.10 % |
| 200 nm | 0.036 % | 0.037 % |

ピーク以下では滴は安定な**ヘイズ**粒子である。ヘイズは湿度 100 % より下でも存在する：塩結晶は約 75 % RH で溶解（潮解）し、実験室は溶液の水活性から 75.5 % を計算する。空気の過飽和が $S_c$ を超えて初めて滴は限りなく成長し雲滴になる（「活性化」）。実雲は約 1 % 過飽和をめったに超えず、だから電圧ではなく粒子集団がどこに滴ができるかを決める。

**イオンは新しい粒子を作る助けになる。** 電荷は小さな分子クラスターを安定化する。CERN CLOUD 実験（Kirkby et al., 2011）は宇宙線からの電離が硫酸–アンモニア粒子の形成率を測定可能に増やすことを示した。それらの粒子はナノメートル級で、雲を種にする大きさになるまで何時間〜何日も成長しなければならない。

**雲播種は実在するが控えめである。** 山岳上の適した冬雲へのヨウ化銀播種は追加降雪を直接観測されている（French et al., 2018）。季節・地域全体では効果は小さく統計的証明が難しい。

**HAARP は実在する。** アラスカの電離層研究施設で、高周波送信機の電力は 3.6 MW。電離層の小さなパッチを加熱し、天気よりはるかに上にある（天気は最低 ~15 km に住む）。天気への実証された効果はない。

**集束は実在する。** 虫眼鏡が热点を作るのは大きな面積の光を小さな点に集めるからである。交差する2ビームも干渉で明暗の縞を作る。

## レベル2 — 主張が破綻するところ

**1. 真空中に縦電波はない。** 真空で Gauss の法則は $\nabla\cdot\mathbf E = 0$。波 $\mathbf E_0 e^{i\mathbf k\cdot\mathbf x}$ では $\mathbf k\cdot\mathbf E_0 = 0$：場は進行方向に垂直でなければならない。ポテンシャルの「スカラー」・縦部分はゲージ変換で変えられ、測定可能な場を変えず、エネルギーを運ばない。Whittaker（1903）は場を2つのスカラー関数で*書ける*ことを示した。これは普通の電磁気の数学的書き換えであり、新しい波ではない。縦電気波はプラズマ内には存在する（Langmuir 波）が、プラズマが要り、岩や海を横切らない。

**2. 電波は地球を通り抜けない。** 導体は電磁波を表皮深さ $\delta \approx \sqrt{2/(\omega\mu_0\sigma)}$ 以内で吸収する。実験室は厳密式を使う：

| 周波数 | 海水（$\sigma$ = 4 S/m） | 岩（$\sigma$ = 10⁻³ S/m） |
|---|---|---|
| 10 Hz | 80 m | 5 km |
| 1 kHz | 8 m | 500 m |
| 1 MHz | 0.25 m | 21 m |

岩 1000 km の後、10 Hz 波でも振幅の $e^{-199} \approx 10^{-87}$ しか残らない。だから潜水艦は超低周波と巨大アンテナで連絡され、それでも表面付近だけである。

**3. 交差ビームはエネルギーを動かす；作ったり消したりできない。** 強度 $I_1$、$I_2$ の2つのコヒーレントビームが重なるところの時間平均強度は

$$I = I_1 + I_2 + 2\sqrt{I_1 I_2}\cos\Delta\phi .$$

暗い縞は常に明るい縞と対になり、パターン平均はちょうど $I_1 + I_2$。実験室は両方を確認する。交点が空気から熱を吸う「冷モード」には負の強度が要る。空気を冷やすことは熱を他所へポンプすることであり、仕事が要り、近くにより多くの熱を捨てなければならない（熱力学第二法則）。虫眼鏡も冷点は作れない。

**4. 天気はどんな電気レバーよりはるかに強力である。** 天気は太陽光（地球が吸収する $\approx 1.2\times10^{17}$ W）と水蒸気凝結の潜熱で駆動される：

| エネルギー源または吸い込み | 実験室の値 |
|---|---|
| 雷雨1つ（半径 5 km に雨 2 cm） | ≈ $4\times10^{15}$ J |
| 平均ハリケーン（半径 665 km に 1.5 cm/日の雨、NOAA 法） | ≈ $6\times10^{14}$ W |
| 100 km × 100 km の空気をわずか 1 K 温める | ≈ $10^{17}$ J |
| 地球電気回路全体 | ≈ $2.5\times10^{8}$ W |
| HAARP 送信機 | $3.6\times10^{6}$ W |
| 大きな地上イオンアレイ（100 kV × 1 mA） | 100 W |

100 W では 1 K 昇温に約3000万年。HAARP の全電力が下層大気に吸収されても（実際はされない）約900年。ハリケーンはイオンアレイを約 $6\times10^{12}$ 倍上回る。そのアレイのイオン風は約 0.25 N の押し — 25 g の重さ — を、何十億トンもの動く空気を含む天気系に当てる。

**5. イオンは直接雲を作れない。** 電荷上の滴形成の Thomson 理論は純水滴の古典自由エネルギーに静電項を加える：

$$\Delta G(r) = -\tfrac43\pi r^3 n_l k T\ln S \;+\; 4\pi r^2\sigma \;+\; \frac{q^2}{8\pi\varepsilon_0}\left(1-\frac{1}{\varepsilon_r}\right)\left(\frac1r - \frac1{r_0}\right).$$

$S \le 1$ ではバルク項が正なので $\Delta G$ に最大がなく臨界半径もない：帯電していても滴は成長しない。$S > 1$ では電荷が障壁を下げるが、実験室は障壁が ~60 kT（およそ 1 滴/cm³/秒）まで落ちるのが中性クラスターで $S \approx 4.1$、素電荷1で $S \approx 2.5$ だと見つける。1890年代の C. T. R. Wilson の雲箱は同種の数を見つけた：イオンが滴を誘発するのは過飽和が数百パーセントのときだけ。現実的な $S = 1.01$ では障壁は $10^6$ kT 超。実空気では塩その他の粒子が 1 % 未満の過飽和で活性化し、イオンが問題になるはるか前である。（数分子のクラスターでは連続体理論は粗い；順序は桁ではなく堅牢。）

**6. 雨のための地上イオナイザー。** いくつかの商業プロジェクトが地上イオナイザーアレイからの雨増強を主張した。これまで公表された証拠は弱く論争中：主張される小さな効果、独立ランダム化試験なし、現実的過飽和で余分イオンから余分雨へ至る受け入れられた機構なし。

**7. 「コンクリートのように硬い空気の壁。」** 定圧で空気を 30 K 冷やすと密度は約 10 % しか上がらない（$\rho \propto 1/T$）。どんな温度変化もミサイルに対して空気を固体のように振る舞わせない。

## レベル3 — 何が真でなければならないか

- **新しい長距離場**が岩と海を無視できる損失で伝播し、普通の電磁波ではなく、空気に強く結合する。精密電磁気試験にも現れるはず。微小質量の光子は縦モードをもつが、光子質量の研究室・天体物理学上限は極めて小さい（Particle Data Group は $10^{-18}$ eV オーダーの束縛を列挙）。
- **天気に見合うエネルギー源**：事象あたり少なくとも $10^{15}$–$10^{17}$ J を何時間で届ける。それは 1 GW 発電所が数日〜数年走る全出力であり、途中で何も温めずに空へビームしなければならない。
- **検証可能な標的**：装置（イオナイザーアレイ、ビームその他）が未処理対照日と比べ雨や気圧の統計的有意な変化を生む制御ランダム化実験で、独立グループが複製。それが雲播種に適用される標準であり、測定効果が控えめと記述される理由である。
- **本物の科学の未解決**：宇宙線イオンが雲量にどれだけ影響するか（CLOUD の結果は今日の気候への効果が小さいことを示唆）；全球電気回路が変化する雷雨活動にどう応答するか；EHD 推進をより効率的にする方法。

## 実験室を実行

```bash
python Module_09_Weather_Engineering/simulation.py
python -m pytest tests/test_module_09.py
```

| 実験 | 示すこと |
|---|---|
| `global_circuit` | 地球晴天回路の電流、電力、電荷、導電率。 |
| `saturation_ratio`, `critical_point`, `equilibrium_radius` | Köhler 理論：100 % RH 以下でヘイズ、$S_c$ 超で活性化、$S_c - 1 \propto m_s^{-1/2}$。 |
| `deliquescence_rh` | なぜ塩結晶が ~75 % RH で溶けるか（理想溶液答えが高すぎる理由）。 |
| `thomson_free_energy`, `nucleation_barrier`, `saturation_for_barrier` | イオンは核生成障壁を下げるが、実雲をはるかに超える過飽和でのみ。 |
| `ion_wind_thrust`, `thrust_per_power` | イオン風は実在するが微小な力を生む。 |
| `rain_latent_heat`, `hurricane_heat_power`, `column_heating_energy` | 天気のエネルギー収支対あらゆる電気レバー。 |
| `crossed_beams`, `skin_depth` | 干渉はエネルギーを再配分；電波は地中・海でメートル〜キロメートルで死ぬ。 |

## 自分で試す

1. `critical_point` でちょうど 0.5 % 過飽和で活性化する乾燥 NaCl 直径を求め、`kappa_critical_saturation` で答えを確認せよ。
2. 50 nm 粒子について乾燥半径から 10 μm まで `saturation_ratio` を描き（任意の描画ツール）、ヘイズ枝、ピーク、活性化枝を印せ。
3. `thomson_free_energy` の `eps_r` を 80 から 1 に変える。電荷の利益はどうなり、なぜか？
4. 実験室の雷雨の潜熱に見合うには、1 GW 発電所が1日走って何基要るか？
5. `skin_depth` で海水 100 m で振幅が半分しか失われない周波数を求めよ。その周波数のアンテナはどれだけ長いか（四分の一波長）？

## 参考文献

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
