# 🔬 モジュール3 — 物語の背後にある科学

> [レッスン](readme.md) は2420年の視点で語られます。このページは2025年の現実チェックです：何が確立されているか、物語の主張がどこで破綻するか、それが成り立つには何が真でなければならないか。ここにあるすべては [実験室コード](../../../Module_03_The_Brain_Is_A_Radio/simulation.py) で確認できます。

## 2420年の主張を一文で

脳は心を作るのではなく受信する。ラジオが「時間チャンネル」の放送に同調するように；光がそのチャンネルを妨害し、同じ周波数に同調した2つの脳は思考を共有する。

## レベル1 — 実在すること

**脳は本当に電気的リズムを出す。** Hans Berger は1920年代に最初のヒト EEG を記録した。頭皮電極は、歩調を合わせて発火する数百万のニューロンから約 10–100 µV の電圧を拾う。リズムは慣例の帯域に分けられる（境界は研究室で少し異なる）：

| 帯域 | 周波数 | 典型的に関連すること |
|---|---|---|
| delta | 0.5–4 Hz | 深い睡眠 |
| theta | 4–8 Hz | 眠気、記憶課題 |
| alpha | 8–13 Hz | リラックスした覚醒、閉眼 |
| beta | 13–30 Hz | 積極的思考、運動 |
| gamma | 30–80 Hz | 局所処理、注意 |

**「光が信号を消す」の本当の反響がある。** Berger は目を開けるとアルファリズムが縮むことに気づいた（「アルファ遮断」）。精神的努力でも縮むので、隠れたチャンネルへの光子干渉ではなく、脳が*していること*を反映する。

**地球は本当に唸る。** 雷（世界で毎秒約50回）が地面と電離層の空洞を鳴らす。半径 $R_E$ の理想的で損失のない薄い殻について、モードは

$$f_n = \frac{c}{2\pi R_E}\sqrt{n(n+1)}, \qquad f_1 \approx 10.6\ \text{Hz}.$$

観測ピークは約 7.8、14.3、20.8、27.3、33.8 Hz で、理想値のおよそ 75–80 % である。電離層が損失のある不完全な鏡だからだ（Schumann が1952年に共鳴を予言；Balser & Wagner が1960年に観測）。7.83 Hz の基本波はたまたま theta/alpha 境界にある。

**脳自身の場も微小である。** 頭の外で脳の磁場は約 100 fT–1 pT（脳磁図、MEG）。Schumann 磁場も 1 pT のオーダーである。だから MEG は磁気遮蔽室で行われる。

**リズムと同期の測定。** 実験室は標準ツールを実装する：

- *Welch パワースペクトル* $S(f)$：重なり合う窓付きセグメントの Fourier 変換の二乗平均。
- *帯域パワー*：$P_\text{band} = \int_{f_1}^{f_2} S(f)\,df$。全周波数で足すと信号の分散に等しい（テストが確認）。
- *瞬時位相*：帯域通過フィルタ後、Hilbert 変換で解析信号 $x(t) + i\,\mathcal{H}[x](t) = A(t)e^{i\phi(t)}$。
- *位相同期値*（Lachaux et al., 1999）：$\text{PLV} = \left|\langle e^{i(\phi_1(t) - \phi_2(t))}\rangle_t\right|$。一定の位相差なら1、無関係なら0付近。

「脳–脳同期」はハイパースキャン研究の実在の知見だが、主に両者が同時に同じものを見聞きするから生じ、信号が間を渡るからではない（Burgess, 2013）。

## レベル2 — 主張が破綻するところ

**1. 周波数の一致は結合ではない。** 7.83 Hz、1 pT の場が頭サイズのループ（半径 7.5 cm）に誘導するのは

$$\mathcal{E} = \pi r^2 \cdot 2\pi f B \approx 9\times10^{-13}\ \text{V}, \qquad E = \tfrac12 r\,\omega B \approx 2\times10^{-12}\ \text{V/m}.$$

これは 10 µV EEG 信号の約 $10^{-7}$。脳リズムを測定可能に押せる経頭蓋交流刺激は脳に約 0.1–1 V/m を入れる：約 $10^{11}$ 倍多い。「7.83 Hz に同調」は Schumann 場が何かをする機構を与えない。

**2. 失敗できない検定。** 脳–地球共鳴を「示す」よくある方法は、信号を完全な 7.83 Hz 正弦と比較することだ。同じ周波数の定常信号は一定の位相差をもつので、PLV は*構成上*1である。実験室はこれを行い PLV = 1.000 を得る。次いで正しい問いを立てる：数秒ずらした記録同士の PLV より大きいか？ 純粋正弦ではずらしは何も変えないので、代理検定は p = 1：証拠なし。

**3. 失敗できる検定。** 実在の Schumann 場は完全正弦ではない；雷がランダムに駆動するので位相がさまよう（品質係数 $Q \approx 4$）。実験室は EEG と独立な Schumann 磁力計記録をシミュレートし、100の合成記録で時間ずらし代理検定を行う：

| 場合 | p < 0.05 の割合 |
|---|---|
| 結合なし | ≈ 5 %（校正された検定が持つべき偽陽性率） |
| 弱い結合を内蔵（EEG パワーの 0.5 %） | ≈ 93 % |
| 1つのアルファ源を共有する2 EEG チャンネル | 100 % |
| 独立アルファ源の2 EEG チャンネル | ≈ 4 % |

本当に結合があるときに検出するので、「否」には意味がある。脳–Schumann 結合の主張が通るべき標準である。

**4. 光子消音。** 光が思考を抑える、赤外カメラが「トゥルポイド」心的形態を撮る、という公表され複製された証拠はない。頭蓋の内側はすでにほぼ暗く、人は明るい日光の下でも完璧に考える。眼の感度曲線は網膜の光色素の吸収スペクトルから来、直接測定されている。

**5. 過去からの生放送としての記憶。** 美しい像だが、証拠ははっきり逆を指す：

- 特定の脳構造の損傷は特定の能力を奪う。患者 H.M. は両側海馬の一部を手術で取り除いた後、新しい長期記憶を作れなくなった（Scoville & Milner, 1957）。
- マウスでは、学習中に活動した特定ニューロンをタグ付けし、後で光で再活性化すると記憶が誘発される（Liu et al., 2012）。
- 記憶は*再構成*され変わりうる：質問の言い回しが後で見た報告を変える（Loftus & Palmer, 1974）。過去からの生放送は質問で編集されない。

宿題のラジオ比喩（「歌はまだ空中にある」）は検証可能な予言をする：別の受信機があなたの歌を再生できるはずだ。そんな受信機は見つかっていない。

**6. 量子脳（Orch‑OR）。** Hameroff と Penrose は、ニューロン内微小管の量子重ね合わせが約 25 ms で崩壊し、それが意識と結びつくと提案した。実在の、公表された、論争中の仮説である。主な異議はタイミング：Tegmark（2000）はそうした重ね合わせが $10^{-13}$ s 以下で脱コヒーレンスすると見積もった。実験室はそのギャップを計算する：

| 神経時間尺度 | vs Tegmark の $10^{-13}$ s | vs 反論見積もり $10^{-4}$ s（Hagan et al., 2002） |
|---|---|---|
| 活動電位、1 ms | $10^{10}$ | $10^{1}$ |
| ガンマ周期、25 ms | $10^{11}$ | $10^{2.4}$ |

最も好意的な公表見積もりでも足りない。Orch‑OR は脳を*受信機*にもしない；なお脳が心を作る理論である。

## レベル3 — 何が真でなければならないか

脳が Schumann 同調受信機であるには、次が現れなければならない。それぞれ明確な実験である：

- **代理検定を通る結合。** EEG を局所磁力計と同時記録。事前登録解析が時間ずらし代理帰無を上回る PLV を見つけ、独立研究室で繰り返されること。
- **場を除くと消える結合。** 磁気遮蔽室で繰り返し、1 pT 場を桁違いに切る。「結合」が生き残るなら Schumann 場から来ていない。
- **正しい大きさの機構。** 神経組織の何かが、影響を与えると知られる場の約 $10^{11}$ 倍弱く、熱雑音を上回って応答する必要。
- **「光子消音」について：** 暗所で現れ明所で消える精神現象の、複製された盲検実験。変えたのは光レベルだけ。

本物の未解決問題は残る。意識が脳活動からどう生じるか（「ハード問題」）は未解決。量子効果が生物学で機能的役割を果たすかは活発に研究されている。Orch‑OR が依る重力関連波動関数崩壊は試験中；地下実験が Diósi–Penrose モデルの最も単純なパラメータフリー版を排除した（Donadi et al., 2021）。

## 実験室を実行

```bash
python Module_03_The_Brain_Is_A_Radio/simulation.py
python Module_03_The_Brain_Is_A_Radio/simulation.py --data my_eeg.csv --fs 160 --channels 0 1
python -m pytest tests/test_module_03.py
```

| 実験 | 示すこと |
|---|---|
| `schumann_frequency` | 理想空洞モード（10.6, 18.3, … Hz）対観測 7.83, 14.3, … Hz。 |
| `field_budget`, `induced_emf`, `induced_e_field` | Schumann 場は頭外で脳自身の大きさだが、内部では ~10⁻¹² V/m を誘導。 |
| `pink_noise`, `synthetic_eeg_pair`, `schumann_record` | 合成 EEG（1/f 背景＋アルファバースト）と位相さまよう Schumann 痕跡。 |
| `welch_psd`, `band_power`, `spectral_slope` | 標準 EEG スペクトル解析。 |
| `plv`, `shift_surrogate_test`, `detection_rate` | 位相同期、正弦対正弦の罠、偽陽性率と検出力を測った校正検定。 |
| `decoherence_gap` | Orch‑OR のタイミング問題（桁）。 |
| `load_user_eeg` | 任意：自分の記録を `.csv` または `.npy`（試料 × チャンネル）。ネットワーク不使用。 |

## 自分で試す

1. 実データ：PhysioNet EEG Motor Movement/Imagery データセットの数ランをダウンロード（109名、64ch、160 Hz、EDF）。2チャンネルを CSV に変換（例：MNE‑Python）し `--data` で実験室を実行。開眼・閉眼ベースラインを比較：Berger の発見どおりアルファパワーは変わるか？
2. 自分のデータで、隣接電極と遠い電極の PLV を計算。なぜ隣接はほぼ常に「有意にロック」か？（ヒント：体積伝導 — 1つの源が両電極に届く。）
3. 位相ランダム化代理を実装し（1チャンネルの Fourier 振幅を保ち位相を乱す）、完全な 7.83 Hz 正弦参照に対して使え。それも定常 7.83 Hz リズムと真の引き込みを区別できないことを示せ。参照のどの性質がすべての代理法を失敗させるか？
4. `COUPLING_DEMO` を下げ、`detection_rate` が約 50 % になるまで。記録長を倍にするとその検出力はどう変わるか？
5. `induced_e_field` で、頭に 0.1 V/m を誘導する 7.83 Hz 磁場を求めよ。MRI スキャナの場（数テスラだが静的）と比べると？

## 参考文献

- Berger, H., "Über das Elektrenkephalogramm des Menschen", *Archiv für Psychiatrie und Nervenkrankheiten* **87**, 527 (1929).
- Schumann, W. O., "Über die strahlungslosen Eigenschwingungen einer leitenden Kugel, die von einer Luftschicht und einer Ionosphärenhülle umgeben ist", *Z. Naturforsch. A* **7**, 149 (1952).
- Balser, M. & Wagner, C. A., "Observations of Earth–ionosphere cavity resonances", *Nature* **188**, 638 (1960).
- Nickolaenko, A. P. & Hayakawa, M., *Resonances in the Earth–Ionosphere Cavity*, Kluwer (2002).
- Hämäläinen, M., Hari, R., Ilmoniemi, R. J., Knuutila, J. & Lounasmaa, O. V., "Magnetoencephalography — theory, instrumentation, and applications to noninvasive studies of the working human brain", *Rev. Mod. Phys.* **65**, 413 (1993).
- Lachaux, J.‑P., Rodriguez, E., Martinerie, J. & Varela, F. J., "Measuring phase synchrony in brain signals", *Hum. Brain Mapp.* **8**, 194 (1999).
- Theiler, J., Eubank, S., Longtin, A., Galdrikian, B. & Farmer, J. D., "Testing for nonlinearity in time series: the method of surrogate data", *Physica D* **58**, 77 (1992).
- Burgess, A. P., "On the interpretation of synchronization in EEG hyperscanning studies: a cautionary note", *Front. Hum. Neurosci.* **7**, 881 (2013).
- Schalk, G., McFarland, D. J., Hinterberger, T., Birbaumer, N. & Wolpaw, J. R., "BCI2000: a general‑purpose brain‑computer interface (BCI) system", *IEEE Trans. Biomed. Eng.* **51**(6), 1034 (2004). Source of the PhysioNet EEG Motor Movement/Imagery dataset.
- Goldberger, A. L. et al., "PhysioBank, PhysioToolkit, and PhysioNet", *Circulation* **101**(23), e215 (2000).
- Scoville, W. B. & Milner, B., "Loss of recent memory after bilateral hippocampal lesions", *J. Neurol. Neurosurg. Psychiatry* **20**, 11 (1957).
- Liu, X. et al., "Optogenetic stimulation of a hippocampal engram activates fear memory recall", *Nature* **484**, 381 (2012).
- Loftus, E. F. & Palmer, J. C., "Reconstruction of automobile destruction: an example of the interaction between language and memory", *J. Verbal Learn. Verbal Behav.* **13**, 585 (1974).
- Hameroff, S. & Penrose, R., "Orchestrated reduction of quantum coherence in brain microtubules: a model for consciousness", *Math. Comput. Simul.* **40**, 453 (1996).
- Hameroff, S. & Penrose, R., "Consciousness in the universe: a review of the 'Orch OR' theory", *Phys. Life Rev.* **11**, 39 (2014).
- Tegmark, M., "Importance of quantum decoherence in brain processes", *Phys. Rev. E* **61**, 4194 (2000).
- Hagan, S., Hameroff, S. R. & Tuszyński, J. A., "Quantum computation in brain microtubules: decoherence and biological feasibility", *Phys. Rev. E* **65**, 061901 (2002).
- Donadi, S. et al., "Underground test of gravity‑related wave function collapse", *Nat. Phys.* **17**, 74 (2021).
