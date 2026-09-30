# 🔬 モジュール11 — 物語の背後にある科学

> [レッスン](readme.md) は2420年の視点で語られます。このページは2025年の現実チェックです：何が確立されているか、物語の主張がどこで破綻するか、それが成り立つには何が真でなければならないか。ここにあるすべては [実験室コード](../../../Module_11_Low_Energy_Transmutation/simulation.py) で確認できます。

## 2420年の主張を一文で

原子核は室温で金属格子、酵素、細菌によって穏やかに他の元素へ「折り直され」、高エネルギーは不要なので金を育て、核廃棄物を肥料に変えられる。

## レベル1 — 実在すること

**変換は実在する。** 原子核は他の元素に変わる：星の中、原子炉、加速器、放射性崩壊で。水銀‑196 でさえ原子炉で金にできる：$^{196}$Hg が中性子を捕獲して $^{197}$Hg になり、電子捕獲で $^{197}$Au に崩壊する。動くが、莫大なコストで微量しか出ない。

**Coulomb の壁。** 電荷 $Z_1e$、$Z_2e$ の2核はエネルギー $Z_1Z_2e^2/(4\pi\varepsilon_0 r)$ で反発し、$e^2/4\pi\varepsilon_0 = 1.44$ MeV·fm。接触距離（$r \approx 1.2(A_1^{1/3}+A_2^{1/3})$ fm）で約 **重陽子2個で 0.48 MeV**、**陽子とカリウム‑39 で 5.2 MeV**。室温は粒子に約 $kT = 0.026$ eV：登るには約2000万分の1足りない。

**トンネル。** 量子力学は核に壁をトンネルさせる。裸の Coulomb 壁について確率は Gamow 因子

$$P(E) = e^{-2\pi\eta} = \exp\!\left(-\sqrt{E_G/E}\right),\qquad \eta = Z_1Z_2\,\alpha\sqrt{\frac{\mu c^2}{2E}},\qquad E_G = 2\mu c^2\,(\pi\alpha Z_1Z_2)^2 .$$

D–D について $E_G = 0.986$ MeV（実験室は Bosch と Hale の定数 $\sqrt{E_G} = 31.40$ keV$^{1/2}$ を再現）。断面積は

$$\sigma(E) = \frac{S(E)}{E}\,e^{-\sqrt{E_G/E}}$$

と書かれ、天体物理学 S 因子 $S(E)$ はゆっくり変化する：主な D–D 分岐2つそれぞれ約 55 keV·b。熱気体で平均すると 2〜10 keV で公表値の約 25 % 以内の D–D 反応率を与える（実験室のテスト）。

**電子遮蔽は実在し、開かれた研究課題である。** 核周りの電子が反発を部分的に打ち消す。短距離ではポテンシャルは $e^2/r - U_e$ のように見え、低エネルギー断面積を

$$f(E) \approx \exp\!\left(\pi\eta\,\frac{U_e}{E}\right)\qquad (U_e \ll E)$$

で押し上げる（Assenbaum, Langanke & Rolfs, 1987）。重水素気体で期待（断熱）値は $U_e \approx 28$ eV。金属にロードした重水素への keV ビーム実験はずっと大きな値、数百 eV を報告した（例：タンタルで約 300 eV；Raiola et al., 2002）。なぜこれほど大きいかはなお議論中である。

**エネルギー簿記。** 核反応はエネルギー $Q = (\sum m_\text{in} - \sum m_\text{out})c^2$ を放出または吸収する。測定質量から：D + D → T + p は 4.03 MeV；D + D → ³He + n は 3.27 MeV（各約 50 %）；D + D → ⁴He + γ は 23.85 MeV だが約 $10^7$ 回に一度。K‑39 + p → Ca‑40 は 8.33 MeV を放出するはず。

## レベル2 — 主張が破綻するところ

**1. 室温でのトンネル数。** $E = kT = 0.026$ eV で裸の D–D Gamow 因子は $10^{-2682}$。800 eV 遮蔽での実験室の WKB 計算でも熱エネルギーの対について $10^{-24}$。対が遮蔽の利益を「見る」のは遮蔽長 $a = e^2/U_e \approx 1800$ fm よりすでに近いときだけである。

**2. 楽観的な率見積もり。** 実験室は 300 K のパラジウム重水素化物（PdD、$6.8\times10^{22}$ D/cm³）中の D–D 融合を計算し、すべての対が $U_e$ で遮蔽され、速い衝突の Maxwell 尾全体を含める。このモデルは意図的に寛大：

| $U_e$ | 電力（W/cm³） |
|---|---|
| 0（裸） | $2\times10^{-254}$ |
| 28 eV（気体） | $9\times10^{-101}$ |
| 300 eV | $7\times10^{-19}$ |
| 800 eV | $9\times10^{-4}$ |

$U_e$ の ±10 % 変化で結果は約260倍変わり、1 W/cm³ には $U_e \approx 1050$ eV が要る。答えは keV ビーム遮蔽値が格子中の静止重陽子に当てはまるかに完全に依存し、誰も示していない。Koonin と Nauenberg（1989）は D₂ 分子中の2重陽子がわずか 0.74 Å 離れていても毎秒約 $10^{-64}$ で融合すると計算した。

**3. 欠けた中性子（決定的試験）。** 熱が普通の D–D 融合から来るなら、反応の半分が 2.45 MeV 中性子を出す。上の Q 値を使い：

$$\frac{1\ \text{W}}{\tfrac12(4.03+3.27)\ \text{MeV}} = 1.7\times10^{12}\ \text{fusions/s} \;\Rightarrow\; 8.6\times10^{11}\ \text{neutrons/s per watt}.$$

遮蔽なし 1 W 源から 1 m ではおよそ 10 Sv/時：約30分で典型的に致死線量。「死んだ大学院生」ジョークの起源である。中性子検出器は単一中性子を数えられるので、$10^{-12}$ W の D–D 融合でも測定可能である。冷たい核融合実験はワット級余剰熱を報告したが、これらの中性子・三重水素・ガンマ収量には似ても似つかなかった。だから熱は D–D 融合ではないか、核ではない。

**4. 1989年の主張は確認されなかった。** Fleischmann と Pons（1989）は重水中のパラジウム電極から余剰熱を報告した。多くの研究室が再現を試み、信頼してできなかった。Berlinguette et al.（2019）の多年プログラムは慎重な熱量測定で主な主張を再検討し、異常熱や核生成物の証拠を見つけず、途中で有用な材料科学を記した。

**5. 鶏と細菌。** 酵素は約 0.5 eV の化学エネルギーで働く（例：ATP 加水分解）。K‑39 + p → Ca‑40 障壁は 5.2 MeV、一千万倍高く、実験室の体温トンネル確率は $10^{-49515}$。Louis Kervran の生物学的変換主張は制御条件下で再現されていない。産卵鶏は食物と骨の特別な貯蔵からカルシウムを取り、カルシウム不足食では殻品質が落ちる。

**6. 「折りたたみ」は無料ではない。** 鉛‑208 を金‑197 に変えることは陽子3個と中性子8個を除くことを意味する。質量は原子あたり少なくとも 77 MeV、金1グラムあたり約 10 MWh（損失前）のコストを言う。核結合エネルギーが理由である：破片はまとまっており、ばらすにはエネルギーが要る。

## レベル3 — 何が真でなければならないか

室温変換が実在するには、次をすべて示す必要がある。それぞれ明確で検証可能な標的である：

- **熱エネルギーで働く遮蔽。** eV 尺度に近づくエネルギーで金属中の低エネルギー D–D 収量を測り、格子中の静止重陽子に当てはまる約 1 keV 超の有効 $U_e$ を示す。
- **熱に合う核生成物。** 核熱の毎ジュールは正しい数の中性子、三重水素、³He、⁴He、またはガンマ線と共に来なければならない。同じランで測定し、盲検解析する。
- **分岐を変える機構。** 中性子がないなら、新しい物理学がエネルギーを速い粒子ではなく格子へ送り、事前に予言され次いで観測されなければならない。
- **独立複製** — 元の実験を設計しなかった研究室による、オープンデータ付き。

**本物の開かれた研究課題：** 金属中の測定遮蔽エネルギーがなぜこれほど大きいか；金属格子中の水素の振る舞い（水素貯蔵と脆化に重要）；恒星天体物理学のための低エネルギー核断面積（例：イタリア LUNA での地下測定）。

## 実験室を実行

```bash
python Module_11_Low_Energy_Transmutation/simulation.py
python -m pytest tests/test_module_11.py
```

| 実験 | 示すこと |
|---|---|
| `coulomb_barrier`, `gamow_energy`, `gamow_factor` | Coulomb 壁と裸トンネル確率、Bosch–Hale の $\sqrt{E_G}$ と照合。 |
| `wkb_exponent`, `screening_enhancement` | 遮蔽壁を通る数値 WKB トンネル；極限で解析的 Gamow と Assenbaum を再現。 |
| `dd_reactivity_cm3_s`, `fusion_power_density` | 熱 D–D 率（keV で公表値に一致）と PdD の楽観的室温見積もり。 |
| `q_value`, `neutrons_per_watt`, `dose_rate_sv_per_hour` | 測定質量からの Q 値と 1 W の D–D 融合が出す中性子束。 |
| `transmutation_cost_mev` | 鉛 → 金の最小エネルギーコスト。 |

## 自分で試す

1. `screening_needed` で 1 mW/cm³ を与える $U_e$ を求め、タンタルで測定された ~300 eV と比較せよ。
2. `fusion_power_density` の `temp_k` を 600 K に変える。温度を倍にすることは $U_e$ の 10 % 増加と比べどれだけ助けになるか？
3. 0.1 W 源から 3 m での中性子線量率を計算。水遮蔽はどれだけ厚く要るか？（水中の高速中性子の減衰長を調べよ。）
4. `q_value` で ¹²C + ¹²C → ²⁴Mg がエネルギーを放出するか確認し、`coulomb_barrier` と `gamow_energy` でなぜ大質量星の中だけで起きるか見よ。

## 参考文献

- Gamow, G., "Zur Quantentheorie des Atomkernes", *Z. Phys.* **51**, 204 (1928).
- Assenbaum, H. J., Langanke, K. & Rolfs, C., "Effects of electron screening on low‑energy fusion cross sections", *Z. Phys. A* **327**, 461 (1987).
- Bosch, H.‑S. & Hale, G. M., "Improved formulas for fusion cross‑sections and thermal reactivities", *Nucl. Fusion* **32**, 611 (1992).
- Raiola, F. et al., "Enhanced electron screening in d(d,p)t for deuterated Ta", *Eur. Phys. J. A* **13**, 377 (2002).
- Koonin, S. E. & Nauenberg, M., "Calculated fusion rates in isotopic hydrogen molecules", *Nature* **339**, 690 (1989).
- Fleischmann, M., Pons, S. & Hawkins, M., "Electrochemically induced nuclear fusion of deuterium", *J. Electroanal. Chem.* **261**, 301 (1989).
- Berlinguette, C. P. et al., "Revisiting the cold case of cold fusion", *Nature* **570**, 45 (2019).
- Wang, M. et al., "The AME 2020 atomic mass evaluation (II)", *Chinese Phys. C* **45**, 030003 (2021). Source of the atomic masses.
- ICRP Publication 74, *Conversion Coefficients for use in Radiological Protection against External Radiation* (1996). Source of the approximate neutron dose coefficient.
- Huba, J. D., *NRL Plasma Formulary* (Naval Research Laboratory, revised regularly). Tabulated D–D reactivities used in the tests.
