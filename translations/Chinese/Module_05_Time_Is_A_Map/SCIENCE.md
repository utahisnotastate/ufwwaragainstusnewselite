# 🔬 模块 5 — 故事背后的科学

> [课程](readme.md)以 2420 年口吻讲述。本页是 2025 年现实核对：哪些已确立、故事主张在何处失效，以及它要成立必须满足什么。此处一切都可用[实验代码](../../../Module_05_Time_Is_A_Map/simulation.py)核验。

## 一句话中的 2420 主张

过去、现在与未来像地图上的地点同时存在，现实「帧帧闪烁」，时间旅行只是把相位移到地图的不同部分。

## 第 1 层 — 哪些是真的

**时间确实是四维几何的一部分。** 在狭义相对论中，每位观测者都同意的量不是两事件之间的时间或距离，而是 **Minkowski 间隔**

$$s^2 = -c^2\,\Delta t^2 + \Delta x^2 + \Delta y^2 + \Delta z^2 .$$

负的 $s^2$（类时）意味着一事件可导致另一；正的 $s^2$（类空）意味着都不能。实验核验 Lorentz 变换 $t' = \gamma\,(t - vx/c^2)$，$x' = \gamma\,(x - vt)$ 使 $s^2$ 不变。

**「现在」取决于谁在问。** 同一时间 $t$ 但相距 $L$ 的两事件，对以 $v$ 运动的观测者在时间上分开

$$\Delta t' = -\gamma\,\frac{vL}{c^2}.$$

对仙女座星系（$L \approx 250$ 万光年），仅以 1.4 m/s 行走就把哪些仙女座事件算作「现在」移动约 **4 天**（实验计算此例；即 Penrose 的「仙女座佯谬」）。这种同时性的相对性是许多物理哲学家捍卫 **永恒主义**——所有事件同等真实的「块宇宙」观点——的原因（Rietdijk 1966，Putnam 1967）。它是相对论的合法诠释。不是唯一一种，且无实验能区分它与对手，因为它们做出相同预言。

**时钟确实以不同速率滴答，我们每天为此修正。** 时钟相对坐标时间的速率，在弱场极限下为

$$\frac{d\tau}{dt} \approx 1 + \frac{\Phi}{c^2} - \frac{v^2}{2c^2}, \qquad \Phi = -\frac{GM}{r}.$$

对 GPS 卫星（$a \approx 26\,562$ km，$v \approx 3.87$ km/s）相对赤道上的时钟，实验从第一原理计算：

| 效应 | µs/天 |
|---|---|
| 高度上更弱引力（走快） | +45.7 |
| 轨道速度（走慢） | −7.2 |
| 地面时钟自身自转 | +0.1 |
| **净** | **+38.5** |

已发表数字常引为 +45.9、−7.2 与 +38.6 µs/天；小差异来自地球形状与自转的建模（实验用 IAU 大地水准面常数 $L_G$ 交叉检验给出 +38.58）。不修正则每天测距误差约 11 km。相对论时钟偏移也通过环球飞行原子钟直接测量（Hafele & Keating 1972）。

**旋转黑洞拖曳时空。** Kerr 度规（Kerr 1963）在 Boyer–Lindquist 坐标中，取 $G = c = M = 1$，有

$$\Sigma = r^2 + a^2\cos^2\theta,\quad \Delta = r^2 - 2r + a^2,$$
$$g_{tt} = -\Big(1-\frac{2r}{\Sigma}\Big),\quad g_{t\phi} = -\frac{2ar\sin^2\theta}{\Sigma},\quad g_{\phi\phi} = \Big(r^2 + a^2 + \frac{2a^2 r\sin^2\theta}{\Sigma}\Big)\sin^2\theta .$$

- 视界在 $r_\pm = 1 \pm \sqrt{1-a^2}$，仅当 $a \le 1$ 存在。
- **能层**位于 $r_+$ 与 $r_\text{ergo} = 1 + \sqrt{1 - a^2\cos^2\theta}$ 之间，那里 $g_{tt} = 0$。其内「静止」方向 $\partial_t$ 变为类空：**没有任何观测者能保持静止**，一切被洞拖着转。实验核验该表面上 $g_{tt}=0$，以及两侧 $g_{tt}$ 的符号。
- **Penrose 过程**（Penrose 1969）：粒子在能层内分裂，一块以负能量落入，另一块带着比原来更多的能量逃逸。实验求解此分裂的能量与角动量守恒，并复现教科书最大值 $\eta = \tfrac12\big(\sqrt{2/r_+}-1\big)$，对 $a = 1$ 为 **20.7%**。
- 可提取总能量由 **不可约质量**（Christodoulou 1970）设定，$M_\text{irr} = \tfrac12\sqrt{r_+^2 + a^2}$：对极端洞最多 $1 - M_\text{irr}/M = $ **29.3%**。

## 第 2 层 — 主张在何处失效

**1. 对「现在」意见不一不等于到达过去。** 实验把两对事件通过 199 个速度提升到 $0.99c$。类空对在其中 50 个中交换顺序。可互为因果的类时对**从不**交换。相对论允许观测者对不能相互影响的事件顺序意见不一。它从不让任何人在原因之前看到结果。

**2. 「时间是闪烁」与「时间旅行是相位移」背后没有物理。** 没有任何理论预言现实的正/负「滴答」，该想法不产生可测量的数字，且全球比较的时钟显示平滑、可预言的速率，如上述 GPS 数字。按字面写，主张不可检验。

**3. 课把两个不同想法混在一起。** 块宇宙（一段固定四维历史）与「多世界」（Everett 1957；分支量子历史）是分开的诠释。两者都不包括选择播放哪卷「胶片」。「意识之光每秒沿蠕虫移动数十亿次」是隐喻，不是物理机制。

**4. 广义相对论*确实*允许时间环之处，远不可及。** 闭合类时曲线（CTC）是穿过时空回到自身过去的路径。带 CTC 的精确解存在：Gödel 旋转宇宙（1949）、van Stockum 与 Tipler 无限长旋转圆柱（Tipler 1974），以及 Kerr 解内部（Carter 1968）。在 Kerr 中，绕轴的环在 $g_{\phi\phi} < 0$ 处为类时。实验对每一自旋扫描 $r$，发现 **$g_{\phi\phi} < 0$ 仅在 $r < 0$**，该区域仅能穿过环奇点到达；对 $a = 1$ 在赤道其边缘恰在 $r = -1$。本课早期草稿有两处错误，实验现在对照检验：

- 它用了 $a = 1.2$，**根本没有视界**（裸奇点，预期不在自然中形成），以及
- 它把能层内 $\partial_t$ 变为类空当作时间机器。能层内 $g_{\phi\phi}$ 仍为正：那是**参考系拖曳，不是 CTC**。

**5. 物理似乎保护过去。** Hawking 的 **时序保护猜想**（1992）提出量子效应阻止在我们能到达的任何区域形成 CTC。它是猜想而非定理，但**没有证据表明 CTC 在我们宇宙任何地方物理可实现**。

## 第 3 层 — 必须成立什么

要使「通过相位移时间旅行」成为科学，它需要满足下列全部：

- **具有可达 CTC 区域的时空。** 每种已知建造方式（可穿越虫洞、曲速泡）都需要负能量密度的「奇异」物质，违反经典能量条件（Morris, Thorne & Yurtsever 1988）。量子效应是否允许足够多仍是开放问题。
- **绕过时序保护的方式。** 完整量子引力理论中的计算必须表明真空不在时间机器边缘（「时序视界」）爆炸。
- **「闪烁」的可测量预言。** 例如原子钟比较中预言的噪声底、离散性或频率，与标准物理不符。若故事给出频率，时钟可以寻找它。
- **与因果律一致。** 理论必须处理祖父悖论，例如通过自洽历史（Novikov 原理），并对其做出可检验预言。

故事中幸存的部分真实且惊人：时间是四维几何中的一个方向，「现在」不普遍，不同高度与速度的时钟以精确、可预言的量分歧，旋转黑洞储存原则上可提取的能量。

## 运行实验

```bash
python Module_05_Time_Is_A_Map/simulation.py
python -m pytest tests/test_module_05.py
```

| 实验 | 展示什么 |
|---|---|
| `lorentz_boost`, `interval`, `simultaneity_shift` | $s^2$ 不变；「现在」随速度移动；类时顺序从不翻转。 |
| `gps_clock_rates` | +45.7 / −7.2 / +38.5 µs/天，由 $GM$、$c$ 与轨道计算。 |
| `kerr_metric`, `horizons`, `ergosurface`, `static_observer_norm` | 视界、能层，以及为何其内无法静止。 |
| `penrose_gain`, `penrose_max_efficiency_*`, `irreducible_mass` | 对 $a = 1$ 每次分裂 20.7%，总计 29.3%。 |
| `ctc_scan` | Kerr 的闭合类时曲线仅存在于 $r < 0$。 |

## 自己动手

1. 用 `simultaneity_shift` 求仙女座「现在」移动一年所需速度。那是 $c$ 的多少分之几？
2. 改变 `gps_clock_rates` 中的 `A_GPS`，求引力与速度效应恰好抵消（净偏移为零）的轨道半径。与 $\tfrac32 R_\text{Earth}$ 比较。
3. 对 $r$ 在 $r_+$ 与 2 之间画出 `penrose_gain(0.9, r)`。增益在何处降为零，为何与能层表面匹配？
4. 对几种自旋运行 `ctc_scan(a, theta=0.3)`。离开赤道是否曾把 CTC 区域带到 $r > 0$？
5. 试 `horizons(1.2)`。用一句话解释为何早期草稿的 $a = 1.2$ 黑洞不是黑洞。

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
