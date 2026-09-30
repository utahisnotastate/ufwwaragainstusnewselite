# 🔬 モジュール12 — 物語の背後にある科学

> [レッスン](readme.md) は2420年の視点で語られます。このページは2025年の現実チェックです：何が確立されているか、物語の主張がどこで破綻するか、それが成り立つには何が真でなければならないか。ここにあるすべては [実験室コード](../../../Module_12_The_Psychotronic_Internet/simulation.py) で確認できます。

## 2420年の主張を一文で

人間の心は電話も線もなしに、「サイコトロニック格子」で増幅された惑星規模の「ノオスフェア」を通じて直接結ばれ、問いは瞬時に答えられ、技能は数秒でダウンロードできる。

## レベル1 — 実在すること

**脳は電気的で、その場は測定できる。** ニューロンは電流を生み、頭外で記録できる：EEG（頭皮でマイクロボルト）と MEG（源から数センチのセンサでおおよそ 100 fT〜1 pT の磁場、地球磁場の約 $10^{-8}$）。

**脳–コンピュータ・インターフェースは実在する。** 埋め込み電極アレイ（例：BrainGate 試験）は麻痺のある人にカーソル、ロボットアーム、テキストを制御させる。Willett et al.（2021）は想像手書きを約毎分90文字で復号し、後の研究は試みられた発話を約毎分62語で復号した（Willett et al., 2023）。これらは脳内または脳上に置かれた電極から信号を読む医療機器であり、空を通じて他人の脳に届かない。

**導体は場を遮蔽する。** 導体に入る変化する場は表皮深さ

$$\delta = \sqrt{\frac{2}{\mu\sigma\omega}} \;\propto\; f^{-1/2}$$

にわたって減衰する。海水（$\sigma \approx 4$ S/m）では、米海軍 ELF 潜水艦送信機の周波数 76 Hz で $\delta = 29$ m、3 kHz で 4.6 m、1 MHz で 0.25 m。2.4 GHz では水の変位電流が伝導電流より大きい（$\omega\varepsilon/\sigma \approx 2.7$）ので一般式が要り、約 1 cm を与える。銅では 50 Hz で $\delta = 9.2$ mm、1 MHz で 65 µm：1 mm 銅板は 1 MHz で約 133 dB 吸収する。だから Faraday ケージが働く。

**静電場も遮蔽される。** 導体では電荷が動き、内部の場が零になるまで続く。一様場 $E_0$ 中の導体球について、誘導表面電荷は $\sigma_s = 3\varepsilon_0E_0\cos\theta$。実験室は答えを仮定しない：その表面電荷にわたって Coulomb の法則を数値で足し、内部の総場が $10^{-4}E_0$ 未満で、外側は教科書の双極子解に合うことを見つける。

**ポテンシャルは実在し、精密な仕方で問題になる。** Whittaker は1903–1904年に波動方程式の解と電磁場自体をスカラー関数で書けることを示した。正しい数学だが、記述するのは*同じ*場 $\mathbf E$ と $\mathbf B$ であり、新しい波ではない。ポテンシャルが直接観測可能な効果をもつ唯一の場所は Aharonov–Bohm 効果（1959）：磁気フラックス $\Phi$ の領域を回る電子は位相

$$\Delta\varphi = \frac{e\Phi}{\hbar} = 2\pi\,\frac{\Phi}{h/e},\qquad h/e = 4.14\times10^{-15}\ \text{Wb}$$

を拾い、経路上の磁場が零でもそうである。Tonomura et al.（1986）は場を超伝導シールドに完全に閉じ込めて確認した。効果は閉ループ周りの囲まれたフラックスだけに依存し、標準量子電磁力学に従う。

**人間の通信速度は測定可能である。** 17言語にわたって、発話は約毎秒39ビットを運ぶ（Coupé et al., 2019）。書かれた英語は冗長性を数えるとおよそ文字あたり1ビットを運ぶ（Shannon, 1951）。

## レベル2 — 主張が破綻するところ

**1. 光より速く情報を運ぶものはない。** 「ピン！ 答えが瞬時に頭に浮かぶ」は実距離では不可能：

| リンク | 片道光遅延 |
|---|---|
| 地球–月 | 1.28 s |
| 地球–火星（最短〜最長） | 3.0〜22.3 分 |
| Proxima Centauri | 4.25 年 |

「火星の首都」の問いへの答えは往復で最短でも6〜45分後である。

**2. もつれはメッセージを送れない。** もつれた対について、実験室は Alice が任意軸に沿って測定した後の Bob の局所状態を計算し、常にちょうど $\tfrac12\mathbb 1$（差は $10^{-15}$ 未満）で、何もしないのと同じであることを見つける。相関は実在する（結果は確率 $\cos^2(\Delta\theta/2)$ で一致する）が、2つの記録を普通のチャンネルで比べたときだけ現れる。これが no‑communication 定理である。

**3. 脳の場は誰かに届くには弱すぎる。** 双極子場は $1/r^3$ で落ちる。源から約 4 cm で測った 1 pT 脳信号は 1 m で約 $6\times10^{-17}$ T、1 km で $6\times10^{-26}$ T、地球磁場より $10^{20}$ 倍以上弱い。最良の磁力計は遮蔽室と頭皮上のセンサを要する。

**4. 「スカラー」コイルは新しいものを放射しない。** 逆巻き（バイファイラ）コイルは2つの反対電流を駆動して場を打ち消す。実験室は近くに残るものと放射するものの両方を計算する：

- 軸上で、1ループの場は $z^{-3.00}$ で落ち；逆巻き対の残りは $z^{-4.00}$：普通のより高次の多重極。
- 遠くで、コイルが近いとき（$kd \ll 1$）対は1コイルの電力の $(kd)^2/5$ を放射する。$d = 0$ では放射はちょうど零。追加の「スカラー」波は現れず、ポテンシャルも打ち消すなら、Aharonov–Bohm その他の効果を残すものは何もない。

**5. 遮蔽。** サイコトロニック信号が電磁なら、金属室、潜水艦、または数メートルの海水が、上の表皮深さが示すように切る。電磁でないなら、物語は新しい自然力を要し、どの実験も見ていない。

**6. 帯域。** 1 MB の飛行マニュアルを発話速度で移すと約57時間かかる。5秒でダウンロードするには $1.6\times10^6$ bit/s、発話の約4万倍が要る。今日の実 BCI は毎秒数ビットで走る。技能や記憶を脳に書き込む方法も知らない：それは膨大な数のニューロンにわたるシナプスを精密に変えることを要する。

**7. ノオスフェアは哲学であり物理学ではない。** Vernadsky と Teilhard de Chardin は「ノオスフェア」を人間の思考の成長する球とその惑星への影響に使った。社会と進化についての思慮深い考えであり、大気の測定された層ではない。蜂は通信するが物理信号を通じて：8の字ダンス、フェロモン、振動。

## レベル3 — 何が真でなければならないか

サイコトロニック・インターネットが存在するには、次をすべて示す必要がある。それぞれ検証可能：

- **脳から脳へ届く担体。** 試験：別々の Faraday 遮蔽室に送信者と受信者、ランダム目標メッセージ、盲検採点、事前登録解析、独立研究室での繰り返し。
- **光速の回避** — 相対論と因果律も覆す。試験：光が運べる前に到着するメッセージ。
- **記憶と技能の読み書きインターフェース：** 技能がシナプスにどう保存されるかを、別の脳に書き込めるほど理解すること。

**物語に近い本物の未解決：** BCI はどれだけ速く安全になれ、手術なしで作れるか？ 非侵襲法（EEG、MEG、光ポンピング磁力計、機能超音波）は脳の情報のどれだけを読めるか？ 「神経データ」のプライバシーと倫理規則は何か？

## 実験室を実行

```bash
python Module_12_The_Psychotronic_Internet/simulation.py
python -m pytest tests/test_module_12.py
```

| 実験 | 示すこと |
|---|---|
| `skin_depth`, `attenuation_length`, `shield_absorption_db` | 海水と金属は変化する場を遮る；$\delta \propto f^{-1/2}$。 |
| `conducting_sphere_field` | 誘導電荷にわたる Coulomb の法則の和が導体内で零場を与える。 |
| `antiparallel_pair_power`, `counterwound_axis_field` | 反対電流は普通の、より速く減衰する多重極を残し、新しい波ではない。 |
| `aharonov_bohm_phase` | ポテンシャルの実在の測定された効果。 |
| `light_delay`, `bob_state`, `same_outcome_probability` | 光速遅延；もつれは相関するが信号できない。 |
| `brain_field`, `bci_bits_per_second`, `transfer_time` | 脳の場がどれだけ弱いか、人間のデータ率がどれだけ遅いか。 |

## 自分で試す

1. 海水の表皮深さが 100 m になる周波数を求めよ。なぜ海軍の潜水艦無線は毎分数文字しか送れなかったか？
2. `bob_state` で Bell 状態を $(\lvert00\rangle + \lvert11\rangle)$ に小さな $\lvert01\rangle$ 混合を加えたもの（正規化）に置き換え。Alice の角度選択は今 Bob の状態を変えるか？
3. `antiparallel_pair_power` で、反対の 1 kHz コイル2つが単一コイルと同じだけ放射するには（km で）どれだけ離れる必要があるか？
4. 読書の情報率を調べよ。その速度ですべてのインターネットを読むのにどれだけかかるか？

## 参考文献

- Whittaker, E. T., "On the partial differential equations of mathematical physics", *Math. Ann.* **57**, 333 (1903).
- Whittaker, E. T., "On an expression of the electromagnetic field due to electrons by means of two scalar potential functions", *Proc. London Math. Soc.* **s2‑1**, 367 (1904).
- Aharonov, Y. & Bohm, D., "Significance of electromagnetic potentials in the quantum theory", *Phys. Rev.* **115**, 485 (1959).
- Tonomura, A. et al., "Evidence for Aharonov‑Bohm effect with magnetic field completely shielded from electron wave", *Phys. Rev. Lett.* **56**, 792 (1986).
- Ghirardi, G. C., Rimini, A. & Weber, T., "A general argument against superluminal transmission through the quantum mechanical measurement process", *Lett. Nuovo Cimento* **27**, 293 (1980).
- Nielsen, M. A. & Chuang, I. L., *Quantum Computation and Quantum Information*, Cambridge University Press (2000).
- Hämäläinen, M. et al., "Magnetoencephalography—theory, instrumentation, and applications to noninvasive studies of the working human brain", *Rev. Mod. Phys.* **65**, 413 (1993).
- Willett, F. R. et al., "High‑performance brain‑to‑text communication via handwriting", *Nature* **593**, 249 (2021).
- Willett, F. R. et al., "A high‑performance speech neuroprosthesis", *Nature* **620**, 1031 (2023).
- Coupé, C., Oh, Y. M., Dediu, D. & Pellegrino, F., "Different languages, similar encoding efficiency: Comparable information rates across the human communicative niche", *Science Advances* **5**, eaaw2594 (2019).
- Shannon, C. E., "Prediction and entropy of printed English", *Bell Syst. Tech. J.* **30**, 50 (1951).
- Vernadsky, V. I., "The biosphere and the noosphere", *American Scientist* **33**, 1 (1945).
- Teilhard de Chardin, P., *The Phenomenon of Man* (1955; English translation 1959).
