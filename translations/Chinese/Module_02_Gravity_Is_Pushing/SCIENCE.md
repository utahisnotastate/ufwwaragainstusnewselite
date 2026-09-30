# 🔬 模块 2 — 故事背后的科学

> [课程](readme.md)以 2420 年口吻讲述。本页是 2025 年现实核对：哪些已确立、故事主张在何处失效，以及它要成立必须满足什么。此处一切都可用[实验代码](../../../Module_02_Gravity_Is_Pushing/simulation.py)核验。

## 一句话中的 2420 主张

引力不是拉：空间充满快速、各向同性的通量，两个质量相互遮蔽它，因此不平衡的通量把它们推到一起。

## 第 1 层 — 哪些是真的

这个想法有真实名称与漫长历史：**Le Sage 引力**（Nicolas Fatio de Duillier, 1690；Georges‑Louis Le Sage, 1748）。Kelvin、Maxwell 与 Poincaré 曾认真对待它，几何是正确的：

- 一个小物体把距离 $d$ 处半径为 $R$ 的第二物体看成覆盖半角 $\theta_0$ 的圆锥盘，其中 $\sin\theta_0 = R/d$。
- 若射线从每一方向均等到来，来自该锥的缺失动量为

$$F \;\propto\; \tfrac12\int_{\cos\theta_0}^{1} u\,du \;=\; \frac{1-\cos^2\theta_0}{4} \;=\; \frac{R^2}{4d^2}.$$

那是**纯几何得出的反平方律**。实验通过抛掷两百万条随机射线并计数被挡者确认；并未预先植入力律。

能量密度为 $u$、以 $c$ 运动的通量，若每个物体吸收与质量成正比的截面 $\sigma = h\,m$，则给出

$$F = \frac{u\,\sigma_1\sigma_2}{4\pi r^2} = \frac{u\,h^2}{4\pi}\,\frac{m_1 m_2}{r^2}, \qquad\text{因此匹配 Newton 需要}\qquad u = \frac{4\pi G}{h^2}.$$

## 第 2 层 — 主张在何处失效

物理学家放弃 Le Sage 引力是因为三个问题。三者都在实验中以数字而非意见出现。

**1. 饱和（质量比例性）。** 影子仅在物体近乎透明时随质量增长。对光学半径 $\tau = \mu R$ 的均匀球，吸收分数为

$$f(\tau) = 1 - \frac{1-(1+2\tau)e^{-2\tau}}{2\tau^2} \;\xrightarrow{\tau\ll 1}\; \tfrac43\tau.$$

在 $\tau = 1$ 时影子已仅为「与质量成正比」值的 53%。真实引力与质量成正比优于 $10^{13}$ 分之一（MICROSCOPE 等效原理检验），且无可测自遮蔽（月球激光测距）。

**2. 拖曳。** 以 $v$ 穿过各向同性通量的物体从前比从后撞到更多。对吸收体力为 $F = \tfrac43\,\sigma u\,v/c$。用 $G$ 固定 $u$ 后，地球轨道速度会在时间

$$t_\text{decay} = \frac{3\,h\,c}{16\pi G}$$

内衰减。

**3. 加热。** 吸收的通量是吸收的能量：$P = \sigma u c = 4\pi G\,m\,c/h$。

**两难。** 小的 $h$ 使地球保持透明（对问题 1 有利），但轨道在不到一秒内停止，且地球吸收约 $10^{45}$ W。大的 $h$ 驯服拖曳，但地球不透明，引力不再随质量标度。实验测试 `test_no_coefficient_escapes_both_drag_and_saturation` 扫过 $h$ 的 30 个数量级，找不到可用值。Richard Feynman 在 *The Feynman Lectures on Physics*（Vol. I, §7‑7）中作了同样论证。

原课对拖曳的「反驳」——匀速稳态通量不产生拖曳——不能成立。拖曳来自*物体*穿过通量的运动，而非通量加速。

## 第 3 层 — 必须成立什么

要拯救推式引力模型，你需要同时具备下列全部。每一项都是清晰、可检验的目标：

- **把动量但不把能量带入物质的通量**，或精确再发射所吸收的，因而无加热。但再发射填满影子并杀死力。那是 Maxwell 的异议（1875）。
- **对运动物体消失的拖曳。** 这要求通量 Lorentz 不变，像量子真空，但 Lorentz 不变真空没有可推*自*的静止系，根本不给出净影子力。
- **微小、可测偏差**：第三物体后方引力略弱（日食「遮蔽」，Majorana 1920 及后来的日食重力测量搜索过，无确认效应），以及极致密物体中质量比例性的微小违反。

现代物理把引力描述为时空曲率（广义相对论），迄今通过每一项检验，包括引力波（LIGO, 2015）与黑洞成像（EHT, 2019）。推式模型也必须再现所有这些。

## 运行实验

```bash
python Module_02_Gravity_Is_Pushing/simulation.py
python -m pytest tests/test_module_02.py
```

| 实验 | 展示什么 |
|---|---|
| `shadow_force` | Monte Carlo 射线计数给出 $1/d^2$，未植入力律。 |
| `absorbed_fraction`, `mass_proportionality` | 物体变得不透明后影子不再跟踪质量。 |
| `drag_and_heating` | 调节通量以复现 $G$ 迫使在拖曳/加热与饱和之间二选一。 |

## 自己动手

1. 在 `shadow_force` 中改变 `R2`。Monte Carlo 结果在何距离停止匹配简单的 $R^2/4d^2$ 律，为什么？
2. 用 `absorbed_fraction`，求影子比「与质量成正比」弱 1% 时的光学半径。
3. 对月球（7.35 × 10²² kg，绕地 1.02 km/s）重做 `drag_and_heating`。两难是否更容易？
4. 查阅 MICROSCOPE 结果（Touboul et al., 2022）。将其界限换算为测试质量允许的最大光学半径。

## 参考文献

- Feynman, Leighton & Sands, *The Feynman Lectures on Physics*, Vol. I, §7‑7 "What is gravity?" (1963).
- Edwards, M. R. (ed.), *Pushing Gravity: New Perspectives on Le Sage's Theory of Gravitation*, Apeiron (2002). A sympathetic collection that also sets out the historical objections.
- Poincaré, H., *Science and Method*, Book III (1908). The heating objection.
- Maxwell, J. C., "Atom", *Encyclopaedia Britannica*, 9th ed. (1875). The re‑emission objection.
- Touboul, P. et al., "MICROSCOPE mission: final results of the test of the equivalence principle", *Phys. Rev. Lett.* **129**, 121102 (2022).
- Abbott, B. P. et al. (LIGO/Virgo), "Observation of gravitational waves from a binary black hole merger", *Phys. Rev. Lett.* **116**, 061102 (2016).
