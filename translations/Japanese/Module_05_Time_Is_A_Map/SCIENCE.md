# 🔬 モジュール5 — 物語の背後にある科学

> [レッスン](readme.md) は2420年の視点で語られます。このページは2025年の現実チェックです：何が確立されているか、物語の主張がどこで破綻するか、それが成り立つには何が真でなければならないか。ここにあるすべては [実験室コード](../../../Module_05_Time_Is_A_Map/simulation.py) で確認できます。

## 2420年の主張を一文で

過去・現在・未来は地図上の場所のように一緒に存在し、現実はフレームからフレームへ「点滅」し、時間旅行は地図の別の部分への位相シフトにすぎない。

## レベル1 — 実在すること

**時間は本当に四次元幾何の一部である。** 特殊相対論で、すべての観測者が一致する量は2事象間の時間でも距離でもなく、**Minkowski 間隔**

$$s^2 = -c^2\,\Delta t^2 + \Delta x^2 + \Delta y^2 + \Delta z^2 .$$

負の $s^2$（時間的）は一方が他方の原因になりうることを意味し、正の $s^2$（空間的）はどちらもなりえない。実験室は Lorentz 変換 $t' = \gamma\,(t - vx/c^2)$、$x' = \gamma\,(x - vt)$ が $s^2$ を不変に保つことを確認する。

**「今」は誰が問うかによる。** 同じ時刻 $t$ で距離 $L$ 離れた2事象は、速度 $v$ の観測者にとって時間で

$$\Delta t' = -\gamma\,\frac{vL}{c^2}$$

だけ分かれる。アンドロメダ銀河（$L \approx 250$ 万光年）では、単に 1.4 m/s で歩くだけで「今」と数えるアンドロメダ事象が約 **4日** ずれる（実験室が計算；例は Penrose の「アンドロメダ・パラドックス」）。この同時性の相対性が、多くの物理学の哲学者が**永遠主義** — すべての事象が等しく実在する「ブロック宇宙」観 — を擁護する理由である（Rietdijk 1966, Putnam 1967）。相対論の正当な解釈である。唯一ではなく、実験はライバルと区別できない。同じ予言をするからである。

**時計は本当に異なる速さで刻み、私たちは毎日補正する。** 座標時間に対する時計の速さは、弱場極限で

$$\frac{d\tau}{dt} \approx 1 + \frac{\Phi}{c^2} - \frac{v^2}{2c^2}, \qquad \Phi = -\frac{GM}{r}.$$

GPS 衛星（$a \approx 26\,562$ km、$v \approx 3.87$ km/s）を赤道上の時計と比べると、実験室は第一原理から計算する：

| 効果 | µs/日 |
|---|---|
| 高度での弱い重力（速く進む） | +45.7 |
| 軌道速度（遅く進む） | −7.2 |
| 地上時計自身の自転 | +0.1 |
| **正味** | **+38.5** |

公表値は通常 +45.9、−7.2、+38.6 µs/日；小さな差は地球の形と自転のモデル化から来る（IAU ジオイド定数 $L_G$ での交差確認は +38.58）。未補正なら測距誤差は約 11 km/日。相対論的時計ずれは原子時計を世界一周飛行しても直接測定された（Hafele & Keating 1972）。

**回転ブラックホールは時空を引きずる。** Boyer–Lindquist 座標の Kerr 計量（Kerr 1963）、$G = c = M = 1$ で

$$\Sigma = r^2 + a^2\cos^2\theta,\quad \Delta = r^2 - 2r + a^2,$$
$$g_{tt} = -\Big(1-\frac{2r}{\Sigma}\Big),\quad g_{t\phi} = -\frac{2ar\sin^2\theta}{\Sigma},\quad g_{\phi\phi} = \Big(r^2 + a^2 + \frac{2a^2 r\sin^2\theta}{\Sigma}\Big)\sin^2\theta .$$

- 地平面は $r_\pm = 1 \pm \sqrt{1-a^2}$。$a \le 1$ のときのみ存在。
- **エルゴ球**は $r_+$ と $r_\text{ergo} = 1 + \sqrt{1 - a^2\cos^2\theta}$（$g_{tt} = 0$）の間。内側では「静止」方向 $\partial_t$ が空間的になり：**どの観測者も静止できない**。すべてが穴と共に引きずられる。実験室は表面で $g_{tt}=0$、両側の符号を確認する。
- **Penrose 過程**（Penrose 1969）：粒子がエルゴ球内で分裂し、一片が負エネルギーで落ち、他方が元より多くのエネルギーで逃げる。実験室はエネルギーと角運動量保存を解き、教科書最大 $\eta = \tfrac12\big(\sqrt{2/r_+}-1\big)$ を回復する。$a = 1$ で **20.7 %**。
- 取り出せる総エネルギーは**既約質量**（Christodoulou 1970）$M_\text{irr} = \tfrac12\sqrt{r_+^2 + a^2}$ で決まる：極限穴で高々 $1 - M_\text{irr}/M = $ **29.3 %**。

## レベル2 — 主張が破綻するところ

**1. 「今」についての不一致は過去に届くことと同じではない。** 実験室は2対の事象を $0.99c$ までの199速度でブーストする。空間的対は50で順序が入れ替わる。原因と結果になりうる時間的対は**決して**入れ替わらない。相対論は互いに影響できない事象の順序について観測者の不一致を許す。効果を原因の前に見ることは許さない。

**2. 「時間は点滅」「時間旅行は位相シフト」には背後の物理学がない。** 理論は現実の正/負の「ティック」を予言せず、測定できる数を作らず、世界中で比べた時計は GPS 数値が示すように滑らかで予測可能な速さを示す。書かれたままでは検証できない。

**3. レッスンは2つの異なる考えを混ぜる。** ブロック宇宙（一つの固定四次元歴史）と「多世界」（Everett 1957；分岐する量子歴史）は別の解釈である。どちらもどの「リール」を再生するか選ぶことを含まない。「意識の光が虫に沿って毎秒何十億回も動く」は比喩であり物理機構ではない。

**4. 一般相対論が時間ループを*許す*ところでは、到達不能である。** 閉時間的曲線（CTC）は自らの過去に戻る時空の道である。CTC をもつ厳密解は存在する：Gödel の回転宇宙（1949）、van Stockum / Tipler の無限に長い回転円筒（Tipler 1974）、Kerr 解の内側（Carter 1968）。Kerr では軸周りのループは $g_{\phi\phi} < 0$ のところで時間的。実験室はすべてのスピンで $r$ を掃き、**$g_{\phi\phi} < 0$ は $r < 0$ のみ**を見つける。リング特異点を通ってのみ到達する領域；$a = 1$ の赤道で端はちょうど $r = -1$。このレッスンの初期草稿は、実験室が今テストする2つの誤りをしていた：

- $a = 1.2$ を使ったが、これは**地平面がまったくない**（裸の特異点で、自然では形成されないと期待される）、
- エルゴ球内で $\partial_t$ が空間的になることをタイムマシンと扱った。エルゴ球内で $g_{\phi\phi}$ はなお正：**フレーム引きずりであり CTC ではない**。

**5. 物理学は過去を守るように見える。** Hawking の**時系列保護予想**（1992）は、到達可能な領域で量子効果が CTC 形成を止めると提案する。予想であり定理ではないが、**CTC が我々の宇宙のどこかで物理的に実現可能だという証拠はない**。

## レベル3 — 何が真でなければならないか

「位相シフトによる時間旅行」が科学になるには、次のすべてを満たす必要がある：

- **到達可能な CTC 領域をもつ時空。** 既知の作り方（通過可能ワームホール、ワープ泡）はすべて古典エネルギー条件を破る負エネルギー密度の「エキゾチック」物質を要する（Morris, Thorne & Yurtsever 1988）。量子効果が十分許すかは未解決。
- **時系列保護の回避。** 量子重力の完全理論での計算が、タイムマシンの縁（「時系列地平面」）で真空が爆発しないことを示す必要がある。
- **「点滅」の測定可能な予言。** 例えば、標準物理学と食い違う原子時計比較の予測ノイズ床、離散性、周波数。物語が周波数を与えれば時計が探せる。
- **因果律との整合。** 祖父パラドックスの扱い（例：自己整合歴史の Novikov 原理）と、それについての検証可能な予言。

物語で生き残る部分は実在で驚くべき：時間は四次元幾何の方向、「今」は普遍ではない、高さ・速度の違う時計は正確に予測可能な量だけ食い違い、回転ブラックホールは原理上取り出せるエネルギーを蓄える。

## 実験室を実行

```bash
python Module_05_Time_Is_A_Map/simulation.py
python -m pytest tests/test_module_05.py
```

| 実験 | 示すこと |
|---|---|
| `lorentz_boost`, `interval`, `simultaneity_shift` | $s^2$ は不変；「今」は速度でずれる；時間的順序は決して反転しない。 |
| `gps_clock_rates` | +45.7 / −7.2 / +38.5 µs/日、$GM$、$c$、軌道から計算。 |
| `kerr_metric`, `horizons`, `ergosurface`, `static_observer_norm` | 地平面、エルゴ球、なぜ内側で静止できないか。 |
| `penrose_gain`, `penrose_max_efficiency_*`, `irreducible_mass` | $a = 1$ で分裂あたり 20.7 %、合計 29.3 %。 |
| `ctc_scan` | Kerr の閉時間的曲線は $r < 0$ のみ。 |

## 自分で試す

1. `simultaneity_shift` でアンドロメダの「今」が1年ずれる速度を求めよ。$c$ の何分か？
2. `gps_clock_rates` の `A_GPS` を変え、重力と速度効果がちょうど打ち消し合う（正味ずれ零）軌道半径を求め、$\tfrac32 R_\text{Earth}$ と比較せよ。
3. $r_+$ と 2 の間で `penrose_gain(0.9, r)` を描き、利得が零になるところとなぜエルゴ面に合うか。
4. いくつかのスピンで `ctc_scan(a, theta=0.3)` を実行。赤道から外れて CTC 領域が $r > 0$ に来るか？
5. `horizons(1.2)` を試し、初期草稿の $a = 1.2$ ブラックホールがなぜブラックホールでなかったかを一文で説明せよ。

## 参考文献

- Kerr, R. P., "Gravitational field of a spinning mass as an example of algebraically special metrics", *Phys. Rev. Lett.* **11**, 237 (1963).
- Boyer, R. H. & Lindquist, R. W., "Maximal analytic extension of the Kerr metric", *J. Math. Phys.* **8**, 265 (1967).
- Carter, B., "Global structure of the Kerr family of gravitational fields", *Phys. Rev.* **174**, 1559 (1968).
- Penrose, R., "Gravitational collapse: the role of general relativity", *Riv. Nuovo Cimento* **1**, 252 (1969).
- Christodoulou, D., "Reversible and irreversible transformations in black‑hole physics", *Phys. Rev. Lett.* **25**, 1596 (1970).
- Gödel, K., "An example of a new type of cosmological solutions of Einstein's field equations of gravitation", *Rev. Mod. Phys.* **21**, 447 (1949).
- Tipler, F. J., "Rotating cylinders and the possibility of global causality violation", *Phys. Rev. D* **9**, 2203 (1974).
- Morris, M. S., Thorne, K. S. & Yurtsever, U., "Wormholes, time machines, and the weak energy condition", *Phys. Rev. Lett.* **61**, 1446 (1988).
- Hawking, S. W., "Chronology protection conjecture", *Phys. Rev. D* **46**, 603 (1992).
- Ashby, N., "Relativity in the Global Positioning System", *Living Rev. Relativ.* **6**, 1 (2003).
- Hafele, J. C. & Keating, R. E., "Around‑the‑world atomic clocks", *Science* **177**, 166 and 168 (1972).
- Putnam, H., "Time and physical geometry", *J. Philos.* **64**, 240 (1967). Rietdijk, C. W., "A rigorous proof of determinism derived from the special theory of relativity", *Philos. Sci.* **33**, 341 (1966).
- Penrose, R., *The Emperor's New Mind*, Oxford University Press (1989). The Andromeda example.
- Everett, H., "'Relative state' formulation of quantum mechanics", *Rev. Mod. Phys.* **29**, 454 (1957).
