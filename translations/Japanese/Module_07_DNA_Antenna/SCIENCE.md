# 🔬 モジュール7 — 物語の背後にある科学

> [レッスン](readme.md) は2420年の視点で語られます。このページは2025年の現実チェックです：何が確立されているか、物語の主張がどこで破綻するか、それが成り立つには何が真でなければならないか。ここにあるすべては [実験室コード](../../../Module_07_DNA_Antenna/simulation.py) で確認できます。

## 2420年の主張を一文で

DNA はコイル形アンテナで、情報場 — 自分の思考や感情も含む — から指示を受け取り、体をそれに合わせて書き換える。

## レベル1 — 実在すること

**DNA の形は精密に知られている。** 細胞内の B‑DNA は右巻き二重らせん（Watson & Crick 1953；Franklin & Gosling 1953）で

- 直径約 **2.0 nm**、
- 塩基対あたりの上昇 **0.34 nm**、
- 溶液中で約 **10.5 塩基対/ターン**（ステップあたり 34.3° ねじれ）、ピッチ **3.4–3.6 nm**。

短距離では剛い：生理塩濃度で持続長は約 50 nm。

**DNA は本当に光と強く相互作用する — 紫外で。** DNA は **260 nm**（光子あたり 4.77 eV）付近で最も強く吸収する。日常の研究室ルール「260 nm で吸光度1は二本鎖 DNA 50 µg/mL」は約 **6600 M⁻¹cm⁻¹ per nucleotide** を与える。二重らせんは同じ塩基が遊離ヌクレオチドのときよりおよそ 30–40 % 少なく吸収する（実験室は教科書的近似値で 39 %）。この**低色素性**は積み重なった塩基が電子的に結合するからである。UV 励起後、励起は数塩基にわたって共有され、積み重ねがエネルギー消散の速さを制御する（Crespo‑Hernández, Cohen & Kohler 2005）。これは実在の速い物理学で、UV 損傷から DNA を守る助けになる。数塩基、数ナノメートルの範囲で働く。

**エネルギーは DNA に沿ってナノメートル規模で跳べる。** Förster 共鳴エネルギー移動（FRET）はドナー色素からアクセプターへ効率

$$E = \frac{1}{1 + (r/R_0)^6}$$

で励起を移す。$R_0$ は典型的に約 5 nm。DNA らせんに沿って置くと、15 塩基対離れる（5.1 nm）とエネルギーの約半分が移り、30 塩基対では約 1 %。この急な $r^{-6}$ 減衰が FRET を「分光定規」にする理由である（Stryer & Haugland 1967）。しばしば DNA 自体が定規になる。

**DNA は振動し「呼吸」する。** Peyrard–Bishop モデル（1989）は各塩基対を Morse ポテンシャル $V(y) = D\,(e^{-ay} - 1)^2$（水素結合）で保たれ、隣と積み重ねばねで結合した伸び $y_n$ として扱う：

$$H = \sum_n \left[\frac{p_n^2}{2m} + \frac{k}{2}(y_n - y_{n-1})^2 + D\,(e^{-a y_n} - 1)^2\right].$$

小振動はフォノン帯 $m\omega^2 = 2Da^2 + 4k\sin^2(q/2)$ をテラヘルツ域に作る。実験室は数値 Hessian と照合する。また転送積分でモデルの熱力学を厳密に解く：温度が上がると塩基対は少し開き、閾値を超えると鎖が分かれる（変性、「融解」）。ここでの例示的調和積み重ねパラメータでは約 490 K で起き、実 DNA の 340–370 K より高い。Dauxois, Peyrard & Bishop（1993）は非線形積み重ねを加えると実験で見られる鋭い融解が得られることを示した。要点は定性的：DNA のダイナミクスは普通の熱物理学である。

**遺伝子は環境により化学を通じて調節される。** エピジェネティックマーク（DNA メチル化、ヒストン修飾）はどの遺伝子が発現するかを変える。食事、ホルモン、経験に応答する；ラットでは例えば母性ケアが子孫のストレスホルモン受容体遺伝子のメチル化を変える（Weaver et al. 2004）。信号は分子：ホルモン、転写因子、酵素である。

**「ジャンク DNA」について。** ヒトゲノムの約 1–2 % がタンパク質をコードする。調節要素（プロモーター、エンハンサー）と非コード RNA は実在で重要である。ENCODE プロジェクト（2012）はゲノムの 80 % に「生化学的機能」を報告したが、その定義は一度転写されることやタンパク質に結合されることなど任意の生化学活性を数えた。強く論争され、例えば Graur et al.（2013）は機能は選択が保存するものを意味すべきだと論じた。進化的制約下にあるゲノムの割合ははるかに低いと見積もられる。

## レベル2 — 主張が破綻するところ

**1. DNA がアンテナなら、思考やバイオフォトンではなく X 線に同調する。** ヘリカルアンテナは円周 $C$ が $\tfrac34 < C/\lambda < \tfrac43$ を満たすとき軸方向に放射する（Kraus の「軸モード」）。B‑DNA では $C = \pi \times 2.0\text{ nm} = 6.3$ nm なので

$$\lambda \approx 4.7\text{–}8.4\text{ nm} \quad (150\text{–}260\text{ eV}),$$

これは極端紫外または軟 X 線で、分子をイオン化する。生体組織から報告される超弱「バイオフォトン」放射（200–800 nm；Cifra & Pospíšil 2014 参照）は **30–130 倍長すぎる**。ピッチ角（30°）も Kraus の最良範囲 12–14° の外である。その上 DNA は金属線ではない：骨格はアンテナのように自由電子を運ばない。

**2. バイオフォトンは指示を運ぶには少なすぎる。** 寛大に毎秒毎 cm² 100 光子、すべて DNA 向けとしても、与えられたらせんターンに当たるのは約 **4400 年に一度**。

**3. 塩水は遮蔽し吸収する。** 細胞は塩水である。150 mM で **Debye 遮蔽長**は

$$\lambda_D = \sqrt{\frac{\varepsilon_r\varepsilon_0 k_B T}{2 N_A e^2 I}} \approx \frac{0.304}{\sqrt{I\,[\text{M}]}}\ \text{nm} \approx 0.78\text{ nm}.$$

電荷の静電場は 10 nm 先ですでに百万分の数まで落ちる。振動場は通るが、塩水の Debye 緩和モデル（導電率約 1.6 S/m）はマイクロ波が $1/e$ に落ちる距離を示す：約 **1 GHz で 2.6 cm、10 GHz で 2.4 mm、100 GHz で 0.24 mm**。50 nm の剛 DNA 断片が 1 GHz 双極子として働くと放射抵抗は約 $10^{-11}\ \Omega$、実用アンテナの約 50 Ω と比べて極めて悪いアンテナである。

**4. 電波光子は化学を行うには弱すぎる。** 1 GHz 光子は体温で $1.5\times10^{-4}\,k_BT$ を運ぶ。分子は毎ピコ秒それより何千倍も揺さぶられる。だから UV（260 nm で光子あたり 178 $k_BT$）は DNA を傷つけ、電波は傷つけない。

**5. 「ファントムリーフ」と「分裂促進放射線」の話。** コロナ放電（Kirlian）写真の制御研究は、像が水分・圧力・露光条件に強く依存することを見つけた（Pehek, Kyler & Faust 1976）。「ファントムリーフ」は確立された効果ではない。Gurwitsch の分裂促進放射線と Kaznacheyev の「細胞病原性転送」主張は独立複製で確立されなかった。

**6. DNA が場から「形態形成指示」を受け取る証拠はない。** 体が形を取る仕方は詳細に研究され、遺伝子、タンパク質、信号分子の勾配、細胞間の機械・電気的手がかりを通じて働く。感情は本当に神経・ホルモン・免疫系を通じて体に影響でき、エピジェネティクスはその物語の一部である。しかしメッセンジャーは分子であり放送ではない。

## レベル3 — 何が真でなければならないか

「DNA はアンテナ」を科学仮説にするには、次をすべて示す必要がある：

- **塩水で働く受信機。** 組織を貫通し*かつ* 2 nm らせんに結合する信号周波数、または遮蔽と熱雑音で洗い流されない機構（例：分子共鳴）。測定可能な試験：細胞培養で遺伝子発現を変える特定周波数、用量反応曲線、盲検、独立複製。
- **信号あたり十分なエネルギー。** DNA 化学を変えるには事象あたり電子ボルト付近のエネルギー、または $k_BT$ 雑音に勝ちながら微小信号を大きな応答に変える細胞内増幅器が要る。
- **「場からの情報」の担体。** 物語は測定可能な強度と予測スペクトルをもつ名前付き物理場を必要とする。書かれたままでは確認できる数を予言しない。

付近の未解決は実在で興味深い：電荷が DNA に沿ってどれだけ運べるか（積み重ね塩基間のホッピングで数ナノメートル）、UV エネルギーが積み重ね塩基間でどう共有されるか、DNA「呼吸」がタンパク質の読み取りをどう助けるか、非コードゲノムのどれだけが重要か。

## 実験室を実行

```bash
python Module_07_DNA_Antenna/simulation.py
python -m pytest tests/test_module_07.py
```

| 実験 | 示すこと |
|---|---|
| `b_dna_geometry`, `helical_antenna_band`, `biophoton_mismatch` | DNA サイズのらせんは ~6 nm（EUV/軟 X 線）に同調、バイオフォトンより 30–130×短い。 |
| `photon_hits_per_turn` | バイオフォトン束は分子尺度で極めて小さい。 |
| `uv_absorption` | 260 nm でヌクレオチドあたり ~6600 M⁻¹cm⁻¹、積み重ねから ~39 % 低色素性。 |
| `fret_efficiency`, `fret_along_dna` | DNA 沿いのエネルギー移動：~15 bp で 50 %、30 bp で ~1 %。 |
| `pb_mode_frequencies_numeric`, `pb_dispersion`, `pb_transfer_integral` | Peyrard–Bishop 振動（THz）と熱的開口・変性。 |
| `debye_length`, `water_permittivity`, `field_penetration_depth` | 0.78 nm 遮蔽；マイクロ波は mm–cm で吸収。 |
| `short_dipole_radiation_resistance`, `rf_photon_vs_thermal` | DNA は絶望的な RF アンテナ；電波光子 ≪ $k_BT$。 |

## 自分で試す

1. `debye_length` で遮蔽長が 1 µm に達する塩濃度を求めよ。生きた細胞はその純度の水で生きられるか？
2. `fret_along_dna` の `R0_nm` を 3 nm と 7 nm に変える。50 % 点は何塩基対動くか？
3. `pb_transfer_integral` で `D` を倍にする。`pb_denaturation_temperature` の解離温度はどう変わるか？ $\sqrt{kD}$ でスケールする `pb_continuum_estimate` と比較せよ。
4. 1細胞のヒトゲノムは約 $6.4\times10^9$ 塩基対（両コピー）。`RISE_NM` で1細胞の DNA 全長を求めよ。真空中の直線半波双極子ならどの周波数に同調し、その周波数は塩水でどれだけ進むか（`field_penetration_depth`）？
5. `rf_photon_vs_thermal` が体温で1になる周波数を求めよ。スペクトルのどの部分か？

## 参考文献

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
