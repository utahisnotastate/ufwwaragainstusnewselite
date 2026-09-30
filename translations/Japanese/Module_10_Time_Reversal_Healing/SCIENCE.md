# 🔬 モジュール10 — 物語の背後にある科学

> [レッスン](readme.md) は2420年の視点で語られます。このページは2025年の現実チェックです：何が確立されているか、物語の主張がどこで破綻するか、それが成り立つには何が真でなければならないか。ここにあるすべては [実験室コード](../../../Module_10_Time_Reversal_Healing/simulation.py) で確認できます。

> ⚕️ **健康に関する注意。** このレッスンの内容は医療アドバイスでも治療法でもありません。時間反転ヒーリングは今日存在しません。病気や怪我をしている場合は医師に相談してください。手術と薬は命を救います。

## 2420年の主張を一文で

「位相共役鏡」は病気や老化した体の歪んだ「波」を記録し、時間反転して送り返し、損傷を取り消して体の以前の健康状態を復元できる。

## レベル1 — 実在すること

**位相共役は実在の光学である。** 1972年、Zel'dovich らは誘導 Brillouin 散乱で反射された光が波面反転して戻ることを示した：行きで乱れたビームが帰りで乱れを解く。その後 Hellwarth と Yariv は $\chi^{(3)}$（Kerr 型）非線形材料での縮退四波混合で同じことを示した。入射場が

$$E(\mathbf r, t) = \mathrm{Re}\big[A(\mathbf r)\,e^{i(kz-\omega t)}\big]$$

なら、位相共役鏡は $A^*(\mathbf r)\,e^{i(-kz-\omega t)}$ を返す。単色波ではそれは正確に時間反転波：すべての光線が道をたどり直す。

**なぜそれが歪みを取り消すか。** 薄い収差層は場に $e^{i\phi(x)}$ を掛ける。位相共役後、場は $e^{-i\phi(x)}$ を帯び、同じ層を再び横切ると $e^{-i\phi}e^{+i\phi} = 1$。自由空間伝播はユニタリなので同じように取り消される。実験室はビームを 2 ラジアンのランダム位相スクリーン往復させる：共役鏡は忠実度 $1.000000$ で元のビームを返し、普通の鏡は忠実度 $0.0025$ を返す。

**組織を通す集束は実在の研究分野である。** 生体組織は光を何度も散乱する。Yaqoob et al.（2008）は光学的位相共役で鶏胸肉切片の散乱を解いた（「濁度抑制」）。Vellekoop と Mosk（2007）は入力ビームの $N$ セグメントの位相を調整して不透明層*を通して*光を集束した。十分発達したスペックルについて、期待される明るさ利得は

$$\eta = \frac{\pi}{4}(N-1) + 1.$$

実験室はランダム透過行列でこの法則を再現する（例：$N = 1024$ で予測 $804.5$ に対し $805$）。これらの方法は組織深部での撮像と光送達のために開発中である。

**生体電気は実在の測定可能な物理学である。** すべての細胞は膜を横切る電圧を保つ。1イオン種について平衡（Nernst）電位は

$$E_\text{ion} = \frac{RT}{zF}\ln\frac{[\text{ion}]_\text{out}}{[\text{ion}]_\text{in}}$$

で、$[K]_o = 5$ mM、$[K]_i = 140$ mM、37 °C で $E_K = -89$ mV。複数イオンでは静止電圧は Goldman–Hodgkin–Katz 方程式で決まる：

$$V_m = \frac{RT}{F}\ln\frac{P_K[K]_o + P_{Na}[Na]_o + P_{Cl}[Cl]_i}{P_K[K]_i + P_{Na}[Na]_i + P_{Cl}[Cl]_o}.$$

教科書的哺乳類値で実験室は $-67$ mV を得る。Michael Levin のグループらはこれらの電圧パターンがカエルや扁形動物などの胚発生と再生をどう導くかを研究する（Levin, 2021）。これは活発な基礎研究であり治療法ではない。

**生命は自分のエントロピーを常に合法的に下げる。** 安静時のヒトは約 100 W の熱を放出する。1日あたり $8.6\times10^6$ J が 310 K の体から出て、エントロピー $Q/T_\text{body} \approx 27{,}900$ J/K を運び出し、293 K の部屋に $Q/T_\text{room} \approx 29{,}500$ J/K として入る。細胞は局所秩序を、より大きなエントロピー輸出で払いながら DNA を修復し、タンパク質を置き換え、傷を治す。第二法則は体＋周囲で成り立つ。

## レベル2 — 主張が破綻するところ

**1. 位相共役鏡は波を反転し、物質を反転しない。** 上の打ち消しは*同じ*層を二度横切るから働く。光場を反転する；光が通った原子を反転しない。体は反射される波ではない：細胞、タンパク質、DNA は物語の鏡が作用しない物質である。

**2. 媒質は往復の間に変わってはならない。** 収差層が変わると帰りは行きを打ち消さない。rms 位相 $\sigma$、往復間相関 $\rho$ の Gauss 位相スクリーンについて忠実度は

$$F = e^{-2\sigma^2(1-\rho)}.$$

実験室は $\rho = 0.99$ で $F = 0.92$、$\rho = 0.9$ で $0.44$、$\rho = 0.5$ で約 $0$ を測る（理論 $0.92$、$0.45$、$0.02$）。生きた組織は絶えず再配置し、生体内光学実験は短い窓（典型的にミリ秒）内で補正しなければならない。物語は*何十年*かけて蓄積した変化を「反転」したいが、$\rho \approx 0$ で忠実度は零である。散乱組織モデルでは、組織が動く前に学んだ補正の利得は $0.92$：補正なしと変わらない。

**3. 鏡は場全体を捕らえなければならない。** 実験室は厳密結果を示す：変わらない媒質で、忠実度は鏡が遮るパワーの割合に等しい（差は $10^{-15}$ 未満）。逃げるものは永遠に失われる。組織 1 cm² だけでも 800 nm で光を制御するには約 $6\times10^{8}$ の独立モードが要る。物語は体のすべての分子の「波」をどう捕らえるかを説明しない。

**4. 「時間チャンネル」に保存された「若いパターン」はない。** 物理学に再生を待つ体の過去状態の記録はない。20歳の細胞配置の情報は、上で述べた同じエントロピー輸出として熱で環境に散らばった。エネルギーは限界ではない（100 W は原理上 Landauer 限界 $kT\ln 2$ で毎秒約 $3\times10^{22}$ ビットの消去を払える）。欠けているのは情報と、すべての分子に作用する機構である。

**5. 「Priore マシン」。** Antoine Priore は1960–70年代フランスで電磁装置を作り、動物の腫瘍や感染への効果を報告した。結果は独立に複製・検証されず、装置は受け入れられた治療法ではない。

**6. 手術と医学は「コンピュータをハンマーで叩く」ではない。** 現代医学は物理学と化学の上に厚く建てられ、働く：ワクチン、抗生物質、麻酔、手術は何百万もの命を救う。レッスンの対比はフィクションの一部である。

## レベル3 — 何が真でなければならないか

「時間反転ヒーリング」が存在するには、次がすべて成り立たなければならない。それぞれ具体的な標的である：

- **体の状態の物理的担体**で「反射」できるもの。試験：体外の場が細胞分解能で組織構造を符号化し測定できることを示す。
- **過去状態の保存記録。** 試験：事前の写真や試料なしに、今日の測定から検証可能な以前の状態（例：古い傷跡パターン）を回復する。
- **返された波を再配置された分子に変える機構** — 既知の化学に合い、組織を焼かないやり方で。
- **時間にわたるコヒーレンス。** どんな「反転」も、体がミリ秒〜年の時間尺度で変わるにもかかわらず働かねばならないが、それは上で示したように共役忠実度を壊す。

**物語の精神により近い本物の未解決：**

- 波面整形と光学的位相共役は生きた組織深部での集束・撮像・光送達をどこまで押し進められるか？
- 生体電気信号は動物の再生を操り、後にヒトで安全に使えるか？（初期研究；承認療法なし。）
- 体自身の修復の限界を何が決め、生物学（例：幹細胞・再生医療）はそれを延ばせるか？

## 実験室を実行

```bash
python Module_10_Time_Reversal_Healing/simulation.py
python -m pytest tests/test_module_10.py
```

| 実験 | 示すこと |
|---|---|
| `round_trip` | 位相共役はランダム収差を正確に打ち消す；普通の鏡はしない。 |
| `round_trip(rho=...)`, `decorrelation_fidelity_theory` | 媒質が往復間で変わると忠実度は $e^{-2\sigma^2(1-\rho)}$ で落ちる。 |
| `round_trip(aperture=...)` | 忠実度は鏡が捕らえる場の割合に等しい。 |
| `wavefront_shaping_enhancement`, `vellekoop_mosk_theory` | 散乱媒質を通す集束は $\tfrac{\pi}{4}(N-1)+1$ に従い、媒質が変わると失われる。 |
| `nernst`, `ghk_voltage` | イオン濃度からの実膜電圧（静止で約 $-67$ mV）。 |
| `entropy_budget`, `landauer_bits_per_second` | 生命はより多く輸出して局所エントロピーを下げる；第二法則は全体で成り立つ。 |

## 自分で試す

1. `round_trip` で `rms_rad` を 2 から 4 に上げる。90 % 忠実度を保つには媒質はどれだけゆっくりしか変われないか（$\rho$ は1にどれだけ近くなければならないか）？ $e^{-2\sigma^2(1-\rho)}$ と照合せよ。
2. `with_changes` で静止電圧が $-55$ mV に達する細胞外カリウムレベルを求めよ。（医師が血中カリウムを注意深く見る理由。）
3. 媒質が*部分的に*だけ変わる `wavefront_shaping_enhancement` を実行：古い透過行列と新しいものを $\sqrt{\rho}\,t_\text{old} + \sqrt{1-\rho}\,t_\text{new}$ として混ぜる。利得は $\rho$ でどう落ちるか？
4. 部屋 35 °C で `entropy_budget` をやり直せ。正味エントロピー生成はどうなり、なぜ暑い環境では熱を捨てにくいか？

## 参考文献

- Zel'dovich, B. Ya., Popovichev, V. I., Ragul'skii, V. V. & Faizullov, F. S., "Connection between the wave fronts of the reflected and exciting light in stimulated Mandel'shtam‑Brillouin scattering", *JETP Lett.* **15**, 109 (1972).
- Hellwarth, R. W., "Generation of time‑reversed wave fronts by nonlinear refraction", *J. Opt. Soc. Am.* **67**, 1 (1977).
- Yariv, A., "Phase conjugate optics and real‑time holography", *IEEE J. Quantum Electron.* **14**, 650 (1978).
- Vellekoop, I. M. & Mosk, A. P., "Focusing coherent light through opaque strongly scattering media", *Opt. Lett.* **32**, 2309 (2007).
- Yaqoob, Z., Psaltis, D., Feld, M. S. & Yang, C., "Optical phase conjugation for turbidity suppression in biological samples", *Nature Photonics* **2**, 110 (2008).
- Goldman, D. E., "Potential, impedance, and rectification in membranes", *J. Gen. Physiol.* **27**, 37 (1943).
- Hodgkin, A. L. & Katz, B., "The effect of sodium ions on the electrical activity of the giant axon of the squid", *J. Physiol.* **108**, 37 (1949).
- Levin, M., "Bioelectric signaling: Reprogrammable circuits underlying embryogenesis, regeneration, and cancer", *Cell* **184**, 1971 (2021).
- Landauer, R., "Irreversibility and heat generation in the computing process", *IBM J. Res. Dev.* **5**, 183 (1961).
