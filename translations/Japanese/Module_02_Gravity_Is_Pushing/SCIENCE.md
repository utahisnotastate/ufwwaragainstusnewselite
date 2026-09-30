# 🔬 モジュール2 — 物語の背後にある科学

> [レッスン](readme.md) は2420年の視点で語られます。このページは2025年の現実チェックです：何が確立されているか、物語の主張がどこで破綻するか、それが成り立つには何が真でなければならないか。ここにあるすべては [実験室コード](../../../Module_02_Gravity_Is_Pushing/simulation.py) で確認できます。

## 2420年の主張を一文で

重力は引きではない：空間は速く等方的なフラックスで満ち、2つの質量が互いにそれから影を落とすので、不均衡なフラックスがそれらを押し合わせる。

## レベル1 — 実在すること

この考えには実名と長い歴史がある：**Le Sage 重力**（Nicolas Fatio de Duillier, 1690；Georges‑Louis Le Sage, 1748）。Kelvin、Maxwell、Poincaré が真剣に扱い、幾何は正しい：

- 小さな物体は、距離 $d$ にある半径 $R$ の第二の物体を、半角 $\theta_0$ の円錐を覆う円盤として見る（$\sin\theta_0 = R/d$）。
- 光線があらゆる方向から均等に来るなら、その円錐から欠ける運動量は

$$F \;\propto\; \tfrac12\int_{\cos\theta_0}^{1} u\,du \;=\; \frac{1-\cos^2\theta_0}{4} \;=\; \frac{R^2}{4d^2}.$$

これは**純粋な幾何からの逆二乗則**である。実験室は200万本のランダム光線を投げ、遮られたものを数えて確認する；力の法則は入れていない。

エネルギー密度 $u$ のフラックスが $c$ で動き、各物体が質量に比例する断面積 $\sigma = h\,m$ を吸収するなら、

$$F = \frac{u\,\sigma_1\sigma_2}{4\pi r^2} = \frac{u\,h^2}{4\pi}\,\frac{m_1 m_2}{r^2}, \qquad\text{なので Newton に合わせるには}\qquad u = \frac{4\pi G}{h^2}.$$

## レベル2 — 主張が破綻するところ

物理学者が Le Sage 重力を捨てたのは三つの問題のためである。三つとも実験室では意見ではなく数値として現れる。

**1. 飽和（質量比例）。** 影が質量とともに増えるのは、物体がほぼ透明なあいだだけである。光学半径 $\tau = \mu R$ の一様球について、吸収分数は

$$f(\tau) = 1 - \frac{1-(1+2\tau)e^{-2\tau}}{2\tau^2} \;\xrightarrow{\tau\ll 1}\; \tfrac43\tau.$$

$\tau = 1$ ですでに影は「質量に比例」値の 53 % にしかならない。実在の重力は質量に $10^{13}$ 分の1より良く比例し（MICROSCOPE 等価原理試験）、測定可能な自己遮蔽を示さない（月レーザー測距）。

**2. 抗力。** 速度 $v$ で等方フラックス中を動く物体は、後ろより前からより多く当たる。吸収体について力は $F = \tfrac43\,\sigma u\,v/c$。$u$ を $G$ で固定すると、地球の軌道速度は時間

$$t_\text{decay} = \frac{3\,h\,c}{16\pi G}$$

で減衰する。

**3. 加熱。** 吸収されたフラックスは吸収されたエネルギー：$P = \sigma u c = 4\pi G\,m\,c/h$。

**ジレンマ。** 小さな $h$ は地球を透明に保つ（問題1には良い）が、軌道は一瞬の何分の一で止まり、地球は約 $10^{45}$ W を吸収する。大きな $h$ は抗力を抑えるが、地球は不透明になり重力は質量に比例しなくなる。実験室の `test_no_coefficient_escapes_both_drag_and_saturation` は $h$ の30桁を掃き、うまくいく値がないことを見つける。Richard Feynman は *The Feynman Lectures on Physics*（Vol. I, §7‑7）で同じ議論をする。

元のレッスンの「抗力の反駁」— 一定速度の定常フラックスは抗力を生まない — は生き残らない。抗力はフラックスが加速することからではなく、物体がフラックス中を*動く*ことから来る。

## レベル3 — 何が真でなければならないか

押し重力モデルを救うには、次をすべて同時に必要とする。それぞれ明確で検証可能な標的である：

- **運動量は運ぶがエネルギーは物質に入れないフラックス**、または吸収したものを正確に再放射するので加熱がない。しかし再放射は影を埋め力を殺す。それが Maxwell の異議（1875）である。
- **動く物体で抗力が消えること。** フラックスが量子真空のように Lorentz 不変であることを要するが、Lorentz 不変な真空には押す*元*となる静止系がなく、正味の影の力も出ない。
- **微小で測定可能な偏差**：第三の物体の後ろで重力がわずかに弱まること（食の「遮蔽」、Majorana が 1920 年に、後に食重力測定で探され、確認された効果なし）と、非常に密な物体での質量比例の小さな破れ。

現代物理学は重力を時空の曲率（一般相対論）として記述し、これまでのすべての試験に合格している。重力波（LIGO, 2015）とブラックホール撮像（EHT, 2019）も含む。押しモデルはそれらすべてを再現しなければならない。

## 実験室を実行

```bash
python Module_02_Gravity_Is_Pushing/simulation.py
python -m pytest tests/test_module_02.py
```

| 実験 | 示すこと |
|---|---|
| `shadow_force` | Monte Carlo 光線計数が、力の法則なしで $1/d^2$ を与える。 |
| `absorbed_fraction`, `mass_proportionality` | 物体が不透明になると影は質量を追わなくなる。 |
| `drag_and_heating` | $G$ を再現するようフラックスを調えると、抗力・加熱と飽和の二者択一を強いられる。 |

## 自分で試す

1. `shadow_force` で `R2` を変える。Monte Carlo 結果が単純な $R^2/4d^2$ 則と一致しなくなる距離はどこか、なぜか？
2. `absorbed_fraction` を使い、影が「質量に比例」より 1 % 弱くなる光学半径を求めよ。
3. 月（$7.35\times10^{22}$ kg、地球周り 1.02 km/s）について `drag_and_heating` をやり直せ。ジレンマは楽になるか？
4. MICROSCOPE の結果（Touboul et al., 2022）を調べ、その上限を試験質量の最大許容光学半径に換算せよ。

## 参考文献

- Feynman, Leighton & Sands, *The Feynman Lectures on Physics*, Vol. I, §7‑7 "What is gravity?" (1963).
- Edwards, M. R. (ed.), *Pushing Gravity: New Perspectives on Le Sage's Theory of Gravitation*, Apeiron (2002). A sympathetic collection that also sets out the historical objections.
- Poincaré, H., *Science and Method*, Book III (1908). The heating objection.
- Maxwell, J. C., "Atom", *Encyclopaedia Britannica*, 9th ed. (1875). The re‑emission objection.
- Touboul, P. et al., "MICROSCOPE mission: final results of the test of the equivalence principle", *Phys. Rev. Lett.* **129**, 121102 (2022).
- Abbott, B. P. et al. (LIGO/Virgo), "Observation of gravitational waves from a binary black hole merger", *Phys. Rev. Lett.* **116**, 061102 (2016).
