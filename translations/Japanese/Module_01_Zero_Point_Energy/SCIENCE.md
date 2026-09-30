# 🔬 モジュール1 — 物語の背後にある科学

> [レッスン](readme.md) は2420年の視点で語られます。このページは2025年の現実チェックです：何が確立されているか、物語の主張がどこで破綻するか、それが成り立つには何が真でなければならないか。ここにあるすべては [実験室コード](../../../Module_01_Zero_Point_Energy/simulation.py) で確認できます。

## 2420年の主張を一文で

空っぽの空間は零点エネルギーの高圧「海」であり、エンジンはそこにバルブを開けるだけで無料の動力を得られる。

## レベル1 — 実在すること

**真空は「無」ではない。** 量子力学によれば、調和振動子は完全に静止できない：最低エネルギーは零ではなく $E_0 = \tfrac12\hbar\omega$ である。電磁場はそのような振動子の集まりで、モードごとに1つあるので、光子をすべて除いても各モードは $\tfrac12\hbar\omega$ を残す。この零点エネルギーは標準物理学の一部であり、測定可能な帰結をもつ（Lamb シフト、自然放出、および下記）。

**Casimir 効果。** 帯電していない平行な鏡を距離 $d$ だけ離す。内側では収まるモードだけが生き残り、外側ではすべてのモードがある。零点エネルギーの差が引力を与える。完全な鏡について（Casimir, 1948）：

$$\frac{E}{A} = -\frac{\pi^2\hbar c}{720\,d^3}, \qquad P = -\frac{\partial (E/A)}{\partial d} = -\frac{\pi^2\hbar c}{240\,d^4}.$$

実験室は CODATA 定数でこれを評価する：$d = 1\ \mu$m で $P \approx -1.30\times10^{-3}$ Pa、100 nm で $\approx -13$ Pa。1気圧に達するのは約 11 nm である。力は測定されている。まず Lamoreaux（1997、球–平板、0.6–6 µm）が説得力をもって示し、次いで Mohideen & Roy（1998）が AFM で、Bressi et al.（2002）が平行平板で測定した。

**実在の鏡。** 実在の金属はプラズマ周波数 $\omega_p$ より上では反射を止めるので、理想式は短距離で力を過大評価する。Lifshitz 理論（1956）が実材料を扱う。零温度で、同一の半空間2つについて、

$$\frac{E}{A} = \frac{\hbar}{4\pi^2}\int_0^\infty d\xi\int_0^\infty k\,dk \sum_{\mathrm{TE,TM}} \ln\!\left(1 - r^2 e^{-2\kappa d}\right), \qquad \kappa = \sqrt{k^2 + \xi^2/c^2},$$

Fresnel 係数は虚周波数 $i\xi$ で評価する：

$$r_{\mathrm{TE}} = \frac{\kappa - K}{\kappa + K},\qquad r_{\mathrm{TM}} = \frac{\varepsilon\kappa - K}{\varepsilon\kappa + K},\qquad K = \sqrt{k^2 + \varepsilon(i\xi)\,\xi^2/c^2}.$$

金について実験室は Drude モデル $\varepsilon(i\xi) = 1 + \omega_p^2/[\xi(\xi+\gamma)]$ を使い、$\hbar\omega_p = 9.0$ eV、$\hbar\gamma = 35$ meV とする。積分器は三通りで確認される：$r = 1$ では Casimir の閉じた形を $10^{-6}$ まで再現し、圧力は $-\partial(E/A)/\partial d$ に等しく、サブナノメートル隙間では非遅延 van der Waals 引力 $E/A \to -A_H/(12\pi d^2)$ になり、Hamaker 定数 $A_H \approx 2.1\times10^{-19}$ J が独立な一次元積分と 0.1 % で一致する。

| $d$ | 金 / 完全鏡 |
|---|---|
| 10 nm | 0.08 |
| 100 nm | 0.44 |
| 1 µm | 0.88 |
| 10 µm | 0.98 |

## レベル2 — 主張が破綻するところ

**1. 零点エネルギーは床であり、貯留層ではない。** それは場が取りうる*基底状態*のエネルギーである。エネルギーを取り出すことはより低い状態へ行くことであり、そんな状態はない。潜水艦の比喩はまさにここで失敗する：海水が流れ込めるのは潜水艦の内側がより低い圧力だからだ。真空の基底状態より「低い圧力」には何もなれない。

**2. Casimir 空洞は井戸ではなくばねである。** 力は位置だけに依存するので保存力である。板をくっつけて一度仕事を得られるが、引き離すときに同じ仕事を払う。実験室は閉サイクル（1 µm → 100 nm → 1 µm）で力を積分し、行きと帰りで異なるサンプリング格子を使い、答えが埋め込まれないようにする：

| 板（1 m²） | 近づくときの仕事 | 離すときの仕事 | 正味 |
|---|---|---|---|
| 完全鏡 | $+4.33\times10^{-7}$ J | $-4.33\times10^{-7}$ J | $\sim10^{-13}$ J（求積誤差、ストロークの $\sim10^{-6}$） |
| 金 | $+2.24\times10^{-7}$ J | $-2.24\times10^{-7}$ J | $\sim10^{-13}$ J |

片道の崩壊でも小さい。1 m² の完全鏡が 1 µm から 10 nm へ落ちると高々 $4.3\times10^{-4}$ J。単三電池は約 $10^4$ J を持つ。

**3. 動く鏡は光を作るが、エネルギーはモーターから来る。** 動的 Casimir 効果は実在する。Wilson et al.（2011）は超伝導回路の有効長をギガヘルツで変調し、真空から光子対を検出した。各対のエネルギーは駆動の1量子に足し上がる（$\hbar\omega_1 + \hbar\omega_2 = \hbar\omega_\text{drive}$）ので、出力はポンプから来る。エネルギーを*変換*する方法であり、見つける方法ではない。

**4. 「10⁹⁵ g/cm³」の海は重力と矛盾する。** 物語の数はプランク密度 $c^5/(\hbar G^2) \approx 5\times10^{96}$ kg/m³ $\approx 5\times10^{93}$ g/cm³ から来る。これはプランク長まで $\tfrac12\hbar\omega$ を足し合わせたものだ。エネルギーは重力を生み、宇宙膨張が実際に示す真空エネルギー（ダークエネルギー）はわずか

$$\rho_\Lambda c^2 = \Omega_\Lambda\,\frac{3H_0^2c^2}{8\pi G} \approx 5\times10^{-10}\ \text{J/m}^3.$$

素朴な見積もり $\hbar c\,k_\text{max}^4/(16\pi^2)$（$k_\text{max} = 1/\ell_P$）は約 $3\times10^{111}$ J/m³ である。これは **~10¹²¹** の不一致、*宇宙定数問題*（Weinberg, 1989）である。未解決だが、物語とは逆を指す：真空が何をしていようと、巨大な貯留層のようには振る舞わない。

**5. 真空は水のように押さない。** Lorentz 不変な真空エネルギーは圧力 $p = -\rho c^2$ — 押し潰す圧力ではなく張力 — をもつ。すべての慣性系・すべての方向で同じで、勾配がなく、力を与えるのは勾配だけである。Casimir 力があるのは板がモード構造を変えるからで、板を取り除けば消える。

作中の「証明」はまた、Fermi の弱い相互作用理論が高エネルギーで「空間の寄与を無視すると」破綻すると言う。Fermi 理論は実際に破綻する（数百 GeV 付近）。それは電弱理論によって修復され、予言された W と Z ボソンは 1983 年に CERN で見つかった — 真空エネルギー抽出によってではない。

## レベル3 — 何が真でなければならないか

真空エンジンが動くには、少なくとも次のどれかが発見されなければならない。それぞれ検証可能である：

- **真空より下の状態。** 閉サイクルで「真空」から正味エネルギーを出す系は、基底状態より低いエネルギー状態になる。精密 Casimir 実験は力を 1 % レベルで測る。正味仕事を返すサイクルは、力対距離のヒステリシスとして現れるはずだ。見つかっていない。
- **非保存的 Casimir 力。** 零温度で運動方向に依存する力（位置だけではない）は新しい物理学である。横滑りする「量子摩擦」は予言されるが微小で、なお運動*から*エネルギーを取る。
- **巨大で利用可能なエネルギーを残す宇宙定数問題の解決。** 候補（超対称性による相殺、人間原理的選択、修正重力）は有効真空エネルギーを小さくする。大きくて取り出せるようにするものはない。

残る本物で興味深い未解決問題：観測される真空エネルギーがなぜこれほど小さいが零ではないか；Casimir 力を実用ナノマシン向けに斥力にできるか（一部の媒質では可能：Munday, Capasso & Parsegian, *Nature* **457**, 170 (2009)）；温度と材料応答がマイクロメートル尺度でどう組み合わさるか、なお活発な議論である。

## 実験室を実行

```bash
python Module_01_Zero_Point_Energy/simulation.py
python -m pytest tests/test_module_01.py
```

| 実験 | 示すこと |
|---|---|
| `casimir_pressure_ideal`, `casimir_energy_ideal` | Casimir の閉じた形：真空は本当に押すが、強く押すのはナノメートルだけ。 |
| `lifshitz_pressure`, `lifshitz_energy`, `gold_reduction_factor` | 虚周波数積分による実在の金板；理想より弱く、マイクロメートルで近づく。 |
| `hamaker_constant` | 短距離（van der Waals）極限の独立チェック。 |
| `closed_cycle_work`, `one_shot_energy` | 閉サイクルの正味仕事は零；片道崩壊は微小で繰り返し不能。 |
| `planck_density`, `naive_vacuum_energy_density`, `observed_dark_energy_density`, `cosmological_constant_gap` | 素朴な「海」と重力が測るものの間の ~10¹²¹ ギャップ。 |

## 自分で試す

1. `GOLD_PLASMA_EV` をアルミニウムの ≈ 12.5 eV に変える。100 nm での金/理想比はどう変わり、なぜ高いプラズマ周波数が助けになるか？
2. `casimir_pressure_ideal` を使い、Casimir 圧が鏡上の太陽光圧（約 9 µPa）と等しくなる間隔を求めよ。
3. ごまかしサイクルを設計してみよ：近づくときは理想則、離すときは金則の圧力関数を `closed_cycle_work` に渡す。正味仕事が出る — 100 nm で板の材料を入れ替える物理過程は何か、そのコストは何か説明せよ。
4. `naive_vacuum_energy_density` で、素朴見積もりが観測ダークエネルギー密度に合うカットオフ $k_\text{max}$ は何か？ 長さに換算せよ。（数十マイクロメートル、ミリメートルの一部になるはずで、これが亜ミリメートル重力試験が興味深い理由の一つである。）

## 参考文献

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
