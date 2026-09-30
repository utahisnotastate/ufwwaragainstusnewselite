# 🔬 モジュール8 — 物語の背後にある科学

> [レッスン](readme.md) は2420年の視点で語られます。このページは2025年の現実チェックです：何が確立されているか、物語の主張がどこで破綻するか、それが成り立つには何が真でなければならないか。ここにあるすべては [実験室コード](../../../Module_08_Instant_Travel/simulation.py) で確認できます。

## 2420年の主張を一文で

距離は錯覚である：体を目的地の「周波数」に合わせればここで消え、零時間であそこに現れ、速度制限はない。空間を横切るのではなく飛ばしたからである。

## レベル1 — 実在すること

**一般相対論は「あなたではなく空間を動かす」ことを紙の上では許す。** Miguel Alcubierre（1994）は、平坦空間の泡が任意速度 $v_s$（光速より速くても）で運ばれる時空を書いた。$G = c = 1$ の単位で：

$$ds^2 = -dt^2 + \big(dx - v_s f(r_s)\,dt\big)^2 + dy^2 + dz^2,$$

$$f(r) = \frac{\tanh\!\big(\sigma(r+R)\big) - \tanh\!\big(\sigma(r-R)\big)}{2\tanh(\sigma R)},$$

ここで $r_s$ は泡中心 $x_s(t)$ からの距離、$R$ は泡半径、$1/\sigma$ が壁厚を決める。内側で $f = 1$（乗客は自由落下で加速を感じない）、遠くで $f \to 0$。

- **前方で空間が縮み、後方で伸びる。** スライスで静止する観測者の体積要素の膨張（York 膨張）は

$$\theta = v_s\,\frac{x - x_s}{r_s}\,\frac{df}{dr_s},$$

泡の前方で負、後方で正、内側と遠くで零。実験室は四性質すべてを数値確認する。

- **代償は負エネルギー。** Einstein 方程式は、この幾何を作るのにどんな物質が要るかを教える。スライスで静止する観測者についてエネルギー密度は

$$T^{00} = -\frac{1}{8\pi}\,\frac{v_s^2\,(y^2+z^2)}{4\,r_s^2}\left(\frac{df}{dr_s}\right)^2 \;\le\; 0 .$$

非零のところでは**どこでも負**：弱エネルギー条件の破れ。全空間積分（実験室は数値で行い、力任せ3D和と照合）は薄い壁で

$$E \;\approx\; -\frac{v_s^2 R^2 \sigma}{36} \qquad (G=c=1),$$

なのでエネルギー請求は速度の二乗、泡サイズの二乗で増え、壁厚に反比例する。

- **負エネルギー密度は少し存在する。** 距離 $d$ の平行鏡の間で量子真空はエネルギー密度 $u = -\pi^2\hbar c/(720\,d^4)$（Casimir, 1948）。結果の力は測定されている（例：Lamoreaux, 1997）。$d = 100$ nm で $u \approx -4$ J/m³。

- **「テレポーテーション」は物理学の実在語 — 体ではなく情報について。** 量子テレポーテーション（Bennett et al., 1993；Bouwmeester et al., 1997 が初実証）は粒子の量子*状態*を、すでに目的地にある別の粒子へ移す。仕事を終えるには光速以下で送られる普通の古典メッセージが要る。光より速く行くものはなく、物質は動かない。

- **2つの鐘。** 同調共鳴は実在するが、第二の鐘が鳴るのは音波が約 343 m/s で部屋を横切ってエネルギーを運ぶからである。遅い普通の空気経由転送であり、ジャンプではない。

## レベル2 — 主張が破綻するところ

**1. 量子不等式が壁を潰す。** 場の量子論は負エネルギーを許すが少しだけ、短時間だけ。平坦時空の質量なしスカラー場について、幅 $t_0$ の Lorentzian 重みでエネルギー密度を平均する観測者は常に（Ford & Roman）

$$\langle\rho\rangle \;\ge\; -\frac{3\hbar}{32\pi^2 c^3\,t_0^4}$$

を見つける。時間が短いほど負エネルギーは許されるが、束縛は $t_0^{-4}$ で締まる。Pfenning & Ford（1997）は壁の曲率尺度より短いサンプリング時間で Alcubierre 泡にこれを適用し、$v_s \sim c$ で壁は高々百プランク長程度しか厚くできず、そのときの総負エネルギーは可視宇宙の質量をはるかに超えることを見つけた。

実験室はより単純な近道で*桁*を再現する：壁上の最も負の $T^{00}$ が $t_0 = 0.1\,\Delta/c$（$\Delta$ = 壁厚）の束縛を守ることを要求する。100 m 泡、$v_s = c$ で：

| 量 | 実験室の値 |
|---|---|
| 許される最大壁厚 | $1.6\times10^{-33}$ m ≈ 98 プランク長 |
| 総負エネルギー | $\approx -4\times10^{79}$ J |
| 質量換算 | $\approx -5\times10^{62}$ kg（約 $10^{32}$ 太陽） |

観測可能宇宙の普通の物質は $10^{53}$ kg のオーダー。近道は Pfenning & Ford より粗いので、$v_s \sim c$ での桁だけを信じ、速度依存は信じない。

**2. 「妥当な」壁でも到達不能。** 量子不等式を忘れ 1 m 厚の壁を許す：実験室は合計約 −400 木星質量、ピークエネルギー密度 $\approx -10^{42}$ J/m³。Casimir 板からそれを得るには約 $4\times10^{-18}$ m 間隔 — 陽子の約400倍小さい — が要る。最良の研究室負エネルギーは40桁以上足りない。

**3. 光より速いことは原因と結果が入れ替わりうる。** 信号が距離 $\Delta x$ を時間 $\Delta t$ で速度 $u > c$ で覆うなら、速度 $V$ の観測者は

$$\Delta t' = \gamma\,\Delta t\left(1 - \frac{uV}{c^2}\right)$$

を測り、$V > c^2/u$ — 完全に普通の亜光速 — で**負**になる。$u = 10c$ では $0.1c$ より速く動く誰でも旅行者が出発前に到着するのを見る。そのような2旅を組み合わせると出発前に戻る往復になる。Everett（1996）はこれがワープドライブに特に当てはまると示した。$u \le c$ では実験室は順序逆転を見る観測者を見つけない。

**4. 「超光速物質波」は何も運ばない。** 元の証明は de Broglie 波が「位相で実効的に超光速」であることによる。その部分は正しい：位相速度は $v_p = c^2/v > c$。しかし粒子、そのエネルギー、メッセージは群速度 $v_g = d\omega/dk = v$ で動き、$v_p v_g = c^2$ ちょうどである。1 m/s で歩く 25 kg の子どもについて実験室は $v_p \approx 9\times10^{16}$ m/s、$v_g = 1.000$ m/s を与える。

**5. 「目的地の共鳴に合わせて現れる」に物理的基盤はない。** 場所の測定可能な性質で体が同調できるラジオ周波数のように働くものはなく、2つが似て振動するから物質を動かす既知機構もない。物語のこの部分は純粋な物語である。美しい像だが、物理学の働き方ではない。物質や情報をここからあそこへ運ぶ既知の方法はすべて、少なくとも光伝播時間かかる（ロケット、電波、古典メッセージ付き量子テレポーテーション）か、ワープ泡のように紙の上だけに存在し、誰も見たことのない物質を要する。

**6. 旅行者の連続性。** 宿題の答え（「ファックスされない、滑る」）は哲学的立場であり物理学ではない。量子テレポーテーションは元の状態を*破壊*しながら他所で再創造する（no‑cloning 定理が両方の保持を禁じる）ので、レッスンが認めるより「ファックス」像に近い。

## レベル3 — 何が真でなければならないか

- **量子不等式を逃れるか束縛されない負エネルギー源**、密度 $10^{40}$ J/m³ 以上を巨視的領域で持続。Casimir 効果をはるかに超える負エネルギー密度の研究室証拠が第一歩。
- **因果問題の回避。** 同時性の相対性を破る優先参照系（Lorentz 不変性試験で強く制約）か、閉ループを禁じる原理（Hawking の時系列保護予想は自然がまさにそうすると提案する；未証明）。
- **より良い幾何。** 研究は数を削ったが核心問題は残る：
  - Van Den Broeck（1999）は外側が小さく内側が大きい泡を見つけ、総エネルギーを数太陽質量に下げたが、なお天文規模の負エネルギーである。
  - Lentz（2021）は正エネルギーだけを要すると主張する超光速「ソリトン」を提案；他の著者はこの主張が持たないと論じた。
  - Bobrick & Martire（2021）は一般枠組みを与え、**超光速**ワープはなお負エネルギーを要し、亜光速は原理上正エネルギーから作れると結論した。
  - Fell & Heisenberg（2021）は正エネルギーで源付けされた亜光速ワープ解を構成した。
- **検証可能な標的**：そのサンプリング時間の量子不等式束縛を超える負エネルギー密度の研究室観測；光が運べる前に到着する信号（精密試験で Lorentz 不変性の破れとしても現れる）。

## 実験室を実行

```bash
python Module_08_Instant_Travel/simulation.py
python -m pytest tests/test_module_08.py
```

| 実験 | 示すこと |
|---|---|
| `shape_function`, `york_expansion` | 空間は泡の前方で収縮、後方で膨張；内側と遠くは平坦。 |
| `energy_density` | どこでも $T^{00} \le 0$：弱エネルギー条件が破れる。 |
| `total_energy`, `total_energy_thin_wall` | すべての負エネルギーの数値積分；$v_s^2 R^2/\Delta$ でスケール。 |
| `qi_bound`, `max_wall_thickness_qi`, `warp_energy_budget` | 量子不等式がプランク薄壁と $\sim10^{62}$ kg の負エネルギーを強制。 |
| `casimir_energy_density`, `casimir_gap_for` | 研究室負エネルギーは何桁も小さすぎる。 |
| `order_reversal_factor`, `reversing_frame_speed` | 超光速＋相対論＝一部の観測者で結果が原因の前。 |
| `de_broglie_velocities` | 位相速度は $c$ を超えるが、群速度（実際の粒子）は超えない。 |

## 自分で試す

1. `total_energy` で壁厚を固定して泡半径 $R$ を倍にしたとき総エネルギーがどう変わるか求め、薄壁公式から説明せよ。
2. `max_wall_thickness_qi` の `sampling_fraction` を 0.1 から 0.5 に変える。壁厚と総エネルギーはどれだけ変わるか？ なぜ結論は生き残るか？
3. `order_reversal_factor` で $1.01c$ で送られた信号が出発前に到着すると見る最も遅い観測者を求めよ。$u \to c$ で何が起きるか？
4. $v_s = 0.01c$ の 1 km 壁のエネルギー密度を与える Casimir 板間隔を求めよ。原子より大きいか？
5. Proxima Centauri（4.24 光年）への光伝播時間を計算し、0.1c 探査機の所要時間と比較せよ。

## 参考文献

- Alcubierre, M., "The warp drive: hyper‑fast travel within general relativity", *Class. Quantum Grav.* **11**, L73 (1994).
- Ford, L. H. & Roman, T. A., "Averaged energy conditions and quantum inequalities", *Phys. Rev. D* **51**, 4277 (1995).
- Ford, L. H. & Roman, T. A., "Restrictions on negative energy density in flat spacetime", *Phys. Rev. D* **55**, 2082 (1997).
- Pfenning, M. J. & Ford, L. H., "The unphysical nature of 'warp drive'", *Class. Quantum Grav.* **14**, 1743 (1997).
- Everett, A. E., "Warp drive and causality", *Phys. Rev. D* **53**, 7365 (1996).
- Van Den Broeck, C., "A 'warp drive' with more reasonable total energy requirements", *Class. Quantum Grav.* **16**, 3973 (1999).
- Lentz, E. W., "Breaking the warp barrier: hyper‑fast solitons in Einstein–Maxwell‑plasma theory", *Class. Quantum Grav.* **38**, 075015 (2021).
- Bobrick, A. & Martire, G., "Introducing physical warp drives", *Class. Quantum Grav.* **38**, 105009 (2021).
- Fell, S. D. B. & Heisenberg, L., "Positive energy warp drive from hidden geometric structures", *Class. Quantum Grav.* **38**, 155020 (2021).
- Casimir, H. B. G., "On the attraction between two perfectly conducting plates", *Proc. K. Ned. Akad. Wet.* **51**, 793 (1948).
- Lamoreaux, S. K., "Demonstration of the Casimir force in the 0.6 to 6 μm range", *Phys. Rev. Lett.* **78**, 5 (1997).
- Hawking, S. W., "Chronology protection conjecture", *Phys. Rev. D* **46**, 603 (1992).
- Bennett, C. H. et al., "Teleporting an unknown quantum state via dual classical and Einstein–Podolsky–Rosen channels", *Phys. Rev. Lett.* **70**, 1895 (1993).
- Bouwmeester, D. et al., "Experimental quantum teleportation", *Nature* **390**, 575 (1997).
