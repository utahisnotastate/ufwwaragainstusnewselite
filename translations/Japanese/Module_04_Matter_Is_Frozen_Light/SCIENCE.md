# 🔬 モジュール4 — 物語の背後にある科学

> [レッスン](readme.md) は2420年の視点で語られます。このページは2025年の現実チェックです：何が確立されているか、物語の主張がどこで破綻するか、それが成り立つには何が真でなければならないか。ここにあるすべては [実験室コード](../../../Module_04_Matter_Is_Frozen_Light/simulation.py) で確認できます。

## 2420年の主張を一文で

物質は小さな回転ループ（トーラス）に閉じ込められた光であり、電子は円を走る光子で、質量はただの「凍った光」である。

## レベル1 — 実在すること

**質量とエネルギーは本当に同じ通貨である。** Einstein の $E = mc^2$（1905）は物理学で最もよく検証された式の一つである。系からエネルギーが出ると、質量も一緒に出る：

| 過程 | 放出エネルギー | 消える質量 |
|---|---|---|
| 乾燥木材 1 kg の燃焼 | $1.6\times10^{7}$ J | $1.8\times10^{-7}$ g（木材の $2\times10^{-10}$） |
| 15キロトン核分裂爆弾 | $6.3\times10^{13}$ J | 0.7 g |

だからレッスンの「丸太を燃やすと結び目が解ける」には真実がある：灰と気体は本当に $\Delta m = E/c^2$ だけ軽い。しかし原子はすべて残っている。質量の $10^{-10}$ だけが行く。

**あなたの質量のほとんどは本当にエネルギーだが、光ではない。** 陽子は 938.27 MeV/c²。3つの価クォーク（up, up, down；Particle Data Group で約 2.2 + 2.2 + 4.7 MeV）の静止質量は合計約 **1 %** しかない。残りは光速近くで動くクォークとそれらを結ぶグルーオン場のエネルギーで、量子色力学（QCD）が記述する。格子 QCD はハドロン質量を数パーセント精度で計算する（Dürr et al., 2008）。仮想「海」クォークのクォーク質量寄与も数えると（ストレンジも含む）クォーク質量の分け前はおおよそ 10 % に上がるが、なお小さい。「質量のほとんどは場のエネルギー」はその意味で実在の物理学であり、物語より深い主張である。

**物質は本当に光になり、光は物質になる。**

- *物質 → 光。* 電子と陽電子が対消滅して 2 本の 511 keV 光子になる。病院の PET スキャナは毎日まさにこの光子対を検出する。
- *光 → 物質。* Breit と Wheeler（1934）は、2光子が十分なエネルギーを持てば電子–陽電子対を作れると計算した。エネルギー $E_1, E_2$ が角 $\theta$ で出会うとき、不変量 $s = 2E_1E_2(1-\cos\theta)$ が $(2m_ec^2)^2$ に達する必要がある：

$$E_1E_2(1-\cos\theta) \;\ge\; 2(m_ec^2)^2.$$

正面衝突では 2 本の 511 keV 光子がちょうど閾値。それより上での断面積は

$$\sigma_{\gamma\gamma} = \frac{\pi r_e^2}{2}(1-\beta^2)\left[(3-\beta^4)\ln\frac{1+\beta}{1-\beta} - 2\beta(2-\beta^2)\right], \qquad \beta = \sqrt{1 - \frac{4m_e^2c^4}{s}},$$

ここで $r_e$ は古典電子半径、$\beta$ は重心系での各レプトン速度。$\beta = 0.70$ 付近でピーク $1.70\times10^{-25}$ cm² $\approx 0.256\,\sigma_T$。実験室は式を独立に確認する：逆過程 $e^+e^-\to\gamma\gamma$ の Dirac（1930）式から詳細釣り合い $\sigma_{\gamma\gamma} = 2\beta^2\sigma_\text{ann}$ で再構築すると $10^{-13}$ で一致する。

**実験。** SLAC 実験 E‑144（Burke et al., 1997）は 46.6 GeV 電子に 527 nm レーザーを後方散乱させ最大 29.2 GeV のガンマ線を作り、同じ強いレーザーと衝突させた。運動学だけで、少なくとも4個のレーザー光子が同時吸収されたので、これは*非線形・多光子* Breit–Wheeler だった。RHIC の STAR（Adam et al., 2021）は接近する金原子核の強い電磁場からの $e^+e^-$ 対を見たが、これは*準実*光子の雲として働く。実光子ビーム同士のきれいな衝突はまだ行われておらず、提案がある（Pike et al., 2014）。

**真空から対を引き出す。** 十分強い電場は対を直接作れる。尺度は、場が1 Compton 長で電子に静止エネルギーを与えるところ（Sauter, Heisenberg–Euler, Schwinger）：

$$E_\text{crit} = \frac{m_e^2c^3}{e\hbar} \approx 1.32\times10^{18}\ \text{V/m}, \qquad I_\text{crit} \approx 2.3\times10^{29}\ \text{W/cm}^2.$$

## レベル2 — 主張が破綻するところ

**1. 「電子は円を走る光子」の唯一の成功はタダである。** モデル（Williamson & van der Mark, 1997）は電荷 $e$ が $c$ で半径 $r = \hbar/(m_ec) = 3.86\times10^{-13}$ m（換算 Compton 波長）のループ上を動くとする。周回電荷の磁気モーメントは

$$\mu = I\cdot\pi r^2 = \frac{ec}{2\pi r}\,\pi r^2 = \frac{ecr}{2} = \frac{e\hbar}{2m_e} = \mu_B,$$

ちょうど Bohr 磁子。しかし $r$ は $m_e$ から選ばれ、$\mu_B$ は $e\hbar/2m_e$ と*定義*されるので代数的恒等式である。実験室は同じレシピが任意の質量で「正しい磁子」を出すことを示す。失敗できないので何も予言しない。

**2. 電子が実際にすることを外す。** 測定モーメントは $\mu_B$ ではなく $1.00115965218059\,\mu_B$（Fan et al., 2023）。量子電磁力学はその余分な 0.116 % を予言する：

$$a_e = \frac{g-2}{2} = \frac{1}{2}\frac{\alpha}{\pi} - 0.3285\left(\frac{\alpha}{\pi}\right)^2 + 1.1812\left(\frac{\alpha}{\pi}\right)^3 - 1.9122\left(\frac{\alpha}{\pi}\right)^4 + \dots$$

実験室はルビジウム原子反跳測定の $\alpha$（Morel et al., 2020）を使い、$g-2$ に依存しないので比較は循環していない：

| モデル | 予言 $g/2$ | ずれ |
|---|---|---|
| 光子ループ | 1（正確） | $1.2\times10^{-3}$ |
| QED、1ループ（Schwinger の $\alpha/2\pi$） | 1.0011614 | $1.8\times10^{-6}$ |
| QED、2ループ | 1.001159637 | $1.5\times10^{-8}$ |
| QED、3ループ | 1.00115965223 | $5\times10^{-11}$ |
| QED、4ループ | 1.00115965218 | $5\times10^{-12}$ |

残る $5\times10^{-12}$ は実験室が省く項の予想サイズ（5ループ QED、重いミューオン・タウのループ、ハドロン・弱効果）。QED はループモデルより約 $10^{8}$ 倍近い。

**3. 電子はループよりはるかに小さい。** LEP の高エネルギー電子–陽電子散乱は約 $10^{-18}$ m まで電子構造の兆候を示さない。モデルのループは $4\times10^{5}$ 倍大きい。それほど大きな構造は、何十年も前に探られたエネルギーでの散乱を変えるはずだ。

**4. モデルが説明すべきだがしないこと。** 光子に電荷はないので、電子の電荷 $-e$ はどこから？ 光子はスピン1、電子はスピン½。ミューオンとタウは電子と同じ電荷で質量が違う。そして単一光子はどれほど高エネルギーでも $s = 0$ で、それだけでは質量粒子になれない；常に何か他のもの（原子核、第二の光子、強場）が要る。光が自ら閉ループに曲がることもない。

**5. 光は実用的な物質源ではない。** 2 eV の太陽光光子2つは対閾値に $s$ で $6.5\times10^{10}$ 倍足りない；太陽光光子の相手には 131 GeV ガンマ線が要る。場で真空から対を裂くのは因子 $e^{-\pi E_\text{crit}/E}$ で支配される。これまでの最強レーザー、約 $1.1\times10^{23}$ W/cm²（Yoon et al., 2021）は $9\times10^{14}$ V/m $= 7\times10^{-4}\,E_\text{crit}$ に達し、因子は約 $10^{-1983}$。（実レーザーは振動し焦点があるので精密率は違うが、まったく無視できるまま。）

**6. なぜものが固体に感じるか。** 回転する光のせいではない。物質が安定で非圧縮なのは電子がフェルミオンだから：Pauli 排他原理と静電気が原子の相互崩壊を防ぐ（Dyson & Lenard, 1967；Lieb, 1976）。天井扇の絵は良いが、実機構は量子統計である。

## レベル3 — 何が真でなければならないか

電子の「凍った光」モデルは、精密な測定標的をもつ次のすべてを通る必要がある：

- **$a_e = 0.00115965218\ldots$ を予言する** — それに合わせたパラメータなしで、QED が $\alpha$ だけでするように。
- **電荷、スピン½、三世代**（電子、ミューオン、タウ）を一つの機構で説明し、質量比（206.77 と 3477.2）を予言する。標準模型もこれらの質量は予言しない；未解決なので、できたモデルは大発見になる。
- **~$10^{-13}$ m の構造を**電子散乱で示す（「形状因子」）。現データは5桁以上でこれを排除する。

付近の本物の未解決：Breit–Wheeler 閾値を超える実光子ビーム同士の初衝突；電子自身の静止系で Schwinger 場に近づく実験（レーザーと高エネルギー電子ビームの強場 QED）；Higgs 結合、したがってクォーク・レプトン質量がなぜその値か。

## 実験室を実行

```bash
python Module_04_Matter_Is_Frozen_Light/simulation.py
python -m pytest tests/test_module_04.py
```

| 実験 | 示すこと |
|---|---|
| `mass_defect`, `proton_valence_quark_fraction` | 化学・核尺度での $E = mc^2$；クォーク静止質量は陽子の ~1 %。 |
| `breit_wheeler_threshold`, `pair_beta`, `breit_wheeler_cross_section` | 光から物質：閾値と断面積。 |
| `breit_wheeler_from_annihilation`, `dirac_annihilation_cross_section` | 詳細釣り合いによる断面積の独立チェック。 |
| `compton_edge`, `min_laser_photons` | なぜ SLAC E‑144 が多光子過程だったか。 |
| `schwinger_field`, `schwinger_suppression_log10` | 今日のレーザーが真空から対を裂くのにどれだけ遠いか。 |
| `loop_magnetic_moment`, `toroidal_model_moment`, `qed_anomaly` | 光子ループモデルの内蔵「成功」とその外れ対 QED。 |

## 自分で試す

1. 宇宙マイクロ波背景（典型光子エネルギー約 $6\times10^{-4}$ eV）で対を作るにはガンマ線はどれだけ高エネルギーか？ これが宇宙が最高エネルギーガンマ線に不透明な理由である。
2. ミューオン質量で `toroidal_model_moment` を使い、測定ミューオン異常 $a_\mu \approx 0.00116592$ と比較。ループモデルはミューオンで良くなるか？
3. 30 kg の子どもの静止エネルギーを `mass_defect` の逆（$E = mc^2$）で計算。15キロトン爆弾何個分か？ なぜそんなことは独りでに起きないか？（ヒント：どの保存量が消えなければならないか？）
4. `breit_wheeler_cross_section` を $s/(2m_ec^2)^2$ に対して描き、高エネルギー形 $\sigma \approx \frac{4\pi r_e^2 m_e^2c^4}{s}\left[\ln\frac{s}{m_e^2c^4} - 1\right]$ を確認せよ。
5. `ALPHA_RB` をセシウム値 $\alpha^{-1} = 137.035999046$（Parker et al., 2018）に置き換え。4ループ予言はどれだけ動き、$g/2$ の測定不確かさ $1.3\times10^{-13}$ と比べると？

## 参考文献

- Einstein, A., "Ist die Trägheit eines Körpers von seinem Energieinhalt abhängig?", *Ann. Phys.* **18**, 639 (1905).
- Breit, G. & Wheeler, J. A., "Collision of two light quanta", *Phys. Rev.* **46**, 1087 (1934).
- Dirac, P. A. M., "On the annihilation of electrons and protons", *Proc. Camb. Phil. Soc.* **26**, 361 (1930).
- Schwinger, J., "On quantum‑electrodynamics and the magnetic moment of the electron", *Phys. Rev.* **73**, 416 (1948).
- Schwinger, J., "On gauge invariance and vacuum polarization", *Phys. Rev.* **82**, 664 (1951).
- Burke, D. L. et al., "Positron production in multiphoton light‑by‑light scattering", *Phys. Rev. Lett.* **79**, 1626 (1997).
- Adam, J. et al. (STAR Collaboration), "Measurement of e⁺e⁻ momentum and angular distributions from linearly polarized photon collisions", *Phys. Rev. Lett.* **127**, 052302 (2021).
- Pike, O. J., Mackenroth, F., Hill, E. G. & Rose, S. J., "A photon–photon collider in a vacuum hohlraum", *Nat. Photon.* **8**, 434 (2014).
- Yoon, J. W. et al., "Realization of laser intensity over 10²³ W/cm²", *Optica* **8**, 630 (2021).
- Williamson, J. G. & van der Mark, M. B., "Is the electron a photon with toroidal topology?", *Ann. Fond. Louis de Broglie* **22**, 133 (1997).
- Fan, X., Myers, T. G., Sukra, B. A. D. & Gabrielse, G., "Measurement of the electron magnetic moment", *Phys. Rev. Lett.* **130**, 071801 (2023).
- Morel, L., Yao, Z., Cladé, P. & Guellati‑Khélifa, S., "Determination of the fine‑structure constant with an accuracy of 81 parts per trillion", *Nature* **588**, 61 (2020).
- Parker, R. H., Yu, C., Zhong, W., Estey, B. & Müller, H., "Measurement of the fine‑structure constant as a test of the Standard Model", *Science* **360**, 191 (2018).
- Laporta, S. & Remiddi, E., "The analytical value of the electron (g−2) at order α³ in QED", *Phys. Lett. B* **379**, 283 (1996).
- Laporta, S., "High‑precision calculation of the 4‑loop contribution to the electron g‑2 in QED", *Phys. Lett. B* **772**, 232 (2017).
- Workman, R. L. et al. (Particle Data Group), "Review of Particle Physics", *Prog. Theor. Exp. Phys.* **2022**, 083C01 (2022).
- Dürr, S. et al., "Ab initio determination of light hadron masses", *Science* **322**, 1224 (2008).
- Dyson, F. J. & Lenard, A., "Stability of matter. I", *J. Math. Phys.* **8**, 423 (1967).
- Lieb, E. H., "The stability of matter", *Rev. Mod. Phys.* **48**, 553 (1976).
