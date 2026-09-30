# 🔬 模块 8 — 故事背后的科学

> [课程](readme.md)以 2420 年口吻讲述。本页是 2025 年现实核对：哪些已确立、故事主张在何处失效，以及它要成立必须满足什么。此处一切都可用[实验代码](../../../Module_08_Instant_Travel/simulation.py)核验。

## 一句话中的 2420 主张

距离是幻觉：若你把身体调到目的地的「频率」，你在此消失并在零时间内出现在那里，没有速度限制，因为你跳过了空间而非穿越它。

## 第 1 层 — 哪些是真的

**广义相对论确实允许「移动空间而非移动你」——在纸上。** Miguel Alcubierre（1994）写下一种时空，其中平坦空间泡以任意速度 $v_s$ 被携带，甚至快于光速。在 $G = c = 1$ 的单位中：

$$ds^2 = -dt^2 + \big(dx - v_s f(r_s)\,dt\big)^2 + dy^2 + dz^2,$$

$$f(r) = \frac{\tanh\!\big(\sigma(r+R)\big) - \tanh\!\big(\sigma(r-R)\big)}{2\tanh(\sigma R)},$$

其中 $r_s$ 是距泡中心 $x_s(t)$ 的距离，$R$ 是泡半径，$1/\sigma$ 设定壁厚。内部 $f = 1$（乘客在自由落体中漂浮，不感到加速度），远处 $f \to 0$。

- **空间在前方收缩、在后方膨胀。** 切片中静止观测者体积元的膨胀（York 膨胀）为

$$\theta = v_s\,\frac{x - x_s}{r_s}\,\frac{df}{dr_s},$$

在泡前为负、在泡后为正，内部与远处为零。实验数值确认全部四项性质。

- **代价是负能量。** Einstein 方程告诉你制造此几何需要何种物质。对切片中静止观测者，能量密度为

$$T^{00} = -\frac{1}{8\pi}\,\frac{v_s^2\,(y^2+z^2)}{4\,r_s^2}\left(\frac{df}{dr_s}\right)^2 \;\le\; 0 .$$

它在非零处**处处为负**：违反弱能量条件。对全空间积分（实验数值完成，并对照蛮力三维求和核验）对薄壁给出

$$E \;\approx\; -\frac{v_s^2 R^2 \sigma}{36} \qquad (G=c=1),$$

因此能量账单随速度平方、泡大小平方增长，并与壁厚成反比。

- **负能量密度存在——一点点。** 两平行镜子相距 $d$ 时，量子真空能量密度 $u = -\pi^2\hbar c/(720\,d^4)$（Casimir, 1948）。由此产生的力已被测量（例如 Lamoreaux, 1997）。在 $d = 100$ nm，$u \approx -4$ J/m³。

- **「传送」在物理中是真实词——对信息，而非身体。** 量子传送（Bennett et al., 1993；Bouwmeester et al., 1997 首次演示）把粒子的量子*态*转移到已在目的地的另一粒子。它需要以光速或更慢发送的普通经典消息来完成工作。没有任何东西快于光，也没有物质被移动。

- **两个铃。** 共振交感是真实的，但第二个铃响是因为声波以约 343 m/s 跨房间携带能量。那是通过空气的缓慢、普通转移，不是跳跃。

## 第 2 层 — 主张在何处失效

**1. 量子不等式压碎墙壁。** 量子场论允许负能量，但只一点点，且只短暂。对平坦时空中的无质量标量场，用宽度 $t_0$ 的 Lorentz 权重平均能量密度的观测者总是发现（Ford & Roman）

$$\langle\rho\rangle \;\ge\; -\frac{3\hbar}{32\pi^2 c^3\,t_0^4}.$$

时间越短，允许的负能量越多，但界限按 $t_0^{-4}$ 收紧。Pfenning & Ford（1997）把这应用于 Alcubierre 泡，采样时间短于壁的曲率尺度，发现对 $v_s \sim c$ 壁最多约百个 Planck 长度厚，且总负能量随后远超可见宇宙质量。

实验用更简单捷径复现*数量级*：要求壁上最负的 $T^{00}$ 在 $t_0 = 0.1\,\Delta/c$（$\Delta$ = 壁厚）下尊重界限。对 $v_s = c$ 的 100 m 泡：

| 量 | 实验值 |
|---|---|
| 允许的最大壁厚 | $1.6\times10^{-33}$ m ≈ 98 Planck 长度 |
| 总负能量 | $\approx -4\times10^{79}$ J |
| 质量当量 | $\approx -5\times10^{62}$ kg（约 $10^{32}$ 个太阳） |

整个可观测宇宙的普通物质约 $10^{53}$ kg 量级。捷径比 Pfenning & Ford 的计算更粗，因此在 $v_s \sim c$ 仅信任其数量级，不信任其对速度的依赖。

**2. 即便「合理」的壁也不可及。** 忘掉量子不等式并允许 1 m 厚壁：实验给出总计约 −400 木星质量，峰值能量密度 $\approx -10^{42}$ J/m³。从 Casimir 板得到那需要相距约 $4\times10^{-18}$ m，大约比质子小 400 倍。最好的实验室负能量短超过 40 个数量级。

**3. 超光速意味着因果可交换。** 若信号以速度 $u > c$ 在时间 $\Delta t$ 覆盖距离 $\Delta x$，以速度 $V$ 运动的观测者测得

$$\Delta t' = \gamma\,\Delta t\left(1 - \frac{uV}{c^2}\right),$$

对任何 $V > c^2/u$（完全普通的亚光速）为**负**。对 $u = 10c$，任何快于 $0.1c$ 运动的人都看到旅行者在离开前到达。两次这样的旅行可组合成在开始前返回的往返。Everett（1996）表明这特别适用于曲速驱动。对 $u \le c$ 实验找不到看到顺序反转的观测者。

**4. 「超光速物质波」什么都不携带。** 原「证明」依赖 de Broglie 波「在相位上有效超光速」。那部分为真：相速度 $v_p = c^2/v > c$。但粒子、其能量与任何消息以群速度 $v_g = d\omega/dk = v$ 运动，且 $v_p v_g = c^2$ 精确成立。对以 1 m/s 行走的 25 kg 儿童，实验给出 $v_p \approx 9\times10^{16}$ m/s 与 $v_g = 1.000$ m/s。

**5. 「匹配目的地共振并出现」没有物理基础。** 没有任何地点的测得性质像身体可调谐到的无线电频率那样工作，也没有已知机制因两物振动相似而移动物质。这是故事中纯属故事的部分。它是可爱意象；只是不是物理工作方式。每种把物质或信息从这里弄到那里的已知方式，要么至少花费光行时间（火箭、无线电、带经典消息的量子传送），要么像曲速泡那样仅存在于纸上并需要无人见过的物质。

**6. 旅行者的连续性。** 家庭作业答案（「你不是被传真，你是滑动」）是哲学立场，不是物理。量子传送在别处重建时*摧毁*原始态（不可克隆定理禁止保留两者），这比课所承认的更接近「传真」图景。

## 第 3 层 — 必须成立什么

- **逃避或不被量子不等式束缚的负能量源**，密度 $10^{40}$ J/m³ 或更高，在宏观区域上持续。任何远超 Casimir 效应的负能量密度实验室证据将是第一步。
- **绕过因果问题的方式。** 要么打破同时性相对性的优选参考系（被 Lorentz 不变性检验紧紧约束），要么禁止闭环的原理（Hawking 的时序保护猜想提出自然恰好如此做；尚未证明）。
- **更好的几何。** 研究已削减数字但未解决核心问题：
  - Van Den Broeck（1999）找到外表面很小、内部很大的泡，把总能量降到几个太阳质量，仍是天文尺度的负能量。
  - Lentz（2021）提出声称仅需正能量的超光速「孤子」；其他作者论证该主张不成立。
  - Bobrick & Martire（2021）给出一般框架并结论：**超光速**曲速驱动仍需负能量，而亚光速原则上可由正能量建造。
  - Fell & Heisenberg（2021）构造了由正能量源供能的亚光速曲速解。
- **可检验目标**：任何超过其采样时间量子不等式界限的负能量密度实验室观测；任何在光本可携带之前到达的信号，也将表现为精密检验中 Lorentz 不变性的违反。

## 运行实验

```bash
python Module_08_Instant_Travel/simulation.py
python -m pytest tests/test_module_08.py
```

| 实验 | 展示什么 |
|---|---|
| `shape_function`, `york_expansion` | 空间在泡前收缩、在泡后膨胀；内部与远处平坦。 |
| `energy_density` | $T^{00} \le 0$ 处处：弱能量条件被违反。 |
| `total_energy`, `total_energy_thin_wall` | 全部负能量的数值积分；按 $v_s^2 R^2/\Delta$ 标度。 |
| `qi_bound`, `max_wall_thickness_qi`, `warp_energy_budget` | 量子不等式迫使 Planck 薄壁与 $\sim10^{62}$ kg 负能量。 |
| `casimir_energy_density`, `casimir_gap_for` | 实验室负能量小许多数量级。 |
| `order_reversal_factor`, `reversing_frame_speed` | 超光速 + 相对论 = 对某些观测者结果在原因之前。 |
| `de_broglie_velocities` | 相速度超过 $c$，群速度（实际粒子）不超过。 |

## 自己动手

1. 用 `total_energy` 求在壁厚固定时把泡半径 $R$ 加倍总能量如何变化。从薄壁公式解释答案。
2. 把 `max_wall_thickness_qi` 中的 `sampling_fraction` 从 0.1 改为 0.5。壁厚与总能量变化多少？为何结论仍成立？
3. 用 `order_reversal_factor`，求看到以 $1.01c$ 发送的信号在离开前到达的最慢观测者。当 $u \to c$ 时发生什么？
4. 求给出 $v_s = 0.01c$ 时 1 km 壁能量密度的 Casimir 板间距。是否大于原子？
5. 计算到 Proxima Centauri（4.24 光年）的光行时间，并与 0.1c 探测器所需时间比较。

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
