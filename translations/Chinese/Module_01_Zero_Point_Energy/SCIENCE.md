# 🔬 模块 1 — 故事背后的科学

> [课程](readme.md)以 2420 年口吻讲述。本页是 2025 年现实核对：哪些已确立、故事主张在何处失效，以及它要成立必须满足什么。此处一切都可用[实验代码](../../../Module_01_Zero_Point_Energy/simulation.py)核验。

## 一句话中的 2420 主张

空的空间是零点能量的高压「海洋」，引擎只需在其中打开阀门即可获得免费动力。

## 第 1 层 — 哪些是真的

**真空不是「什么都没有」。** 量子力学说谐振子永远不能完全静止：其最低能量是 $E_0 = \tfrac12\hbar\omega$，不是零。电磁场是此类振子的集合，每个模式一个，因此即使去掉每一个光子，每个模式仍保留其 $\tfrac12\hbar\omega$。这种零点能量是标准物理的一部分，并有可测量后果（Lamb 位移、自发辐射，以及下面这一项）。

**Casimir 效应。** 把两面平行的不带电镜子相距 $d$。只有能夹在其间的模式在内部存活，外部则存在所有模式。零点能量之差产生吸引。对完美镜子（Casimir, 1948）：

$$\frac{E}{A} = -\frac{\pi^2\hbar c}{720\,d^3}, \qquad P = -\frac{\partial (E/A)}{\partial d} = -\frac{\pi^2\hbar c}{240\,d^4}.$$

实验用 CODATA 常数计算这些：$d = 1\ \mu$m 时 $P \approx -1.30\times10^{-3}$ Pa，100 nm 时 $\approx -13$ Pa。大约到 11 nm 才达到一个大气压。该力已被测量：首先由 Lamoreaux（1997，球–板，0.6–6 µm）令人信服地测得，随后 Mohideen & Roy（1998）用 AFM，以及 Bressi 等人（2002）在平行板之间。

**真实镜子。** 真实金属在高于其等离子体频率 $\omega_p$ 的频率上停止反射，因此理想公式在短程高估了力。Lifshitz 理论（1956）处理真实材料。零温下，对两个相同半空间，

$$\frac{E}{A} = \frac{\hbar}{4\pi^2}\int_0^\infty d\xi\int_0^\infty k\,dk \sum_{\mathrm{TE,TM}} \ln\!\left(1 - r^2 e^{-2\kappa d}\right), \qquad \kappa = \sqrt{k^2 + \xi^2/c^2},$$

Fresnel 系数在虚频率 $i\xi$ 上求值：

$$r_{\mathrm{TE}} = \frac{\kappa - K}{\kappa + K},\qquad r_{\mathrm{TM}} = \frac{\varepsilon\kappa - K}{\varepsilon\kappa + K},\qquad K = \sqrt{k^2 + \varepsilon(i\xi)\,\xi^2/c^2}.$$

对金，实验使用 Drude 模型 $\varepsilon(i\xi) = 1 + \omega_p^2/[\xi(\xi+\gamma)]$，其中 $\hbar\omega_p = 9.0$ eV，$\hbar\gamma = 35$ meV。积分器以三种方式核验：当 $r = 1$ 时以 $10^{-6}$ 复现 Casimir 闭式；其压力等于 $-\partial(E/A)/\partial d$；在亚纳米间隙它变为非推迟 van der Waals 吸引，$E/A \to -A_H/(12\pi d^2)$，Hamaker 常数 $A_H \approx 2.1\times10^{-19}$ J，与独立一维积分在 0.1 % 内吻合。

| $d$ | 金 / 完美镜子 |
|---|---|
| 10 nm | 0.08 |
| 100 nm | 0.44 |
| 1 µm | 0.88 |
| 10 µm | 0.98 |

## 第 2 层 — 主张在何处失效

**1. 零点能量是地板，不是水库。** 它是*基态*的能量，场能处的最低态。抽取能量意味着进入更低态——并不存在。潜艇类比恰在此处失败：海水能涌入是因为潜艇内部压力更低。没有什么能比真空基态「压力更低」。

**2. Casimir 腔是弹簧，不是井。** 力只依赖位置，因而是保守力。让板吸合可一次性得功，但拉开必须付出同样的功。实验对闭循环（1 µm → 100 nm → 1 µm）积分力，两行程用不同采样网格，以免答案内建：

| 板（1 m²） | 合拢得功 | 拉开付功 | 净 |
|---|---|---|---|
| 完美镜子 | $+4.33\times10^{-7}$ J | $-4.33\times10^{-7}$ J | $\sim10^{-13}$ J（求积误差，约行程的 $\sim10^{-6}$） |
| 金 | $+2.24\times10^{-7}$ J | $-2.24\times10^{-7}$ J | $\sim10^{-13}$ J |

即便单向坍缩也很小。一平方米完美镜子从 1 µm 落到 10 nm 最多给出 $4.3\times10^{-4}$ J。一节 AA 电池约存 $10^4$ J。

**3. 运动镜子造光，但能量来自电机。** 动态 Casimir 效应是真实的。Wilson 等人（2011）以吉赫兹频率调制超导电路的有效长度，并探测到来自真空的光子对。每对能量之和等于驱动的一个量子（$\hbar\omega_1 + \hbar\omega_2 = \hbar\omega_\text{drive}$），因此输出功率来自泵。这是*转换*能量的方式，不是发现能量。

**4. 「10⁹⁵ g/cm³」海洋与引力矛盾。** 故事中的数字来自 Planck 密度 $c^5/(\hbar G^2) \approx 5\times10^{96}$ kg/m³ $\approx 5\times10^{93}$ g/cm³，即把 $\tfrac12\hbar\omega$ 对模式求和到 Planck 长度。能量有引力，而宇宙膨胀实际显示的真空能量（暗能量）仅为

$$\rho_\Lambda c^2 = \Omega_\Lambda\,\frac{3H_0^2c^2}{8\pi G} \approx 5\times10^{-10}\ \text{J/m}^3.$$

朴素估计 $\hbar c\,k_\text{max}^4/(16\pi^2)$（$k_\text{max} = 1/\ell_P$）约为 $3\times10^{111}$ J/m³。这是 **~10¹²¹** 的失配，即*宇宙学常数问题*（Weinberg, 1989）。这是开放问题，但指向与故事相反的方向：无论真空做什么，它都不像巨大水库。

**5. 真空不像水那样推。** Lorentz 不变的真空能量具有压力 $p = -\rho c^2$，是张力而非压碎压力。在每一参考系、每一方向都相同，它没有梯度，而只有梯度才产生力。Casimir 力存在是因为板改变了模式结构；板移走后它消失。

设定内「证明」还说：若忽略空间贡献，Fermi 弱相互作用理论在高能失效。Fermi 理论确实失效（约几百 GeV）。它被电弱理论修复，其预言的 W 与 Z 玻色子于 1983 年在 CERN 发现，并非靠抽取真空能量。

## 第 3 层 — 必须成立什么

要使真空引擎工作，至少下列之一必须被发现。每一项都可检验：

- **低于真空的态。** 任何在闭循环中从「真空」得到净能量的系统，都会是比基态更低的能量态。精密 Casimir 实验以约 1 % 水平测力。返回净功的循环会表现为力–距离的滞后环。从未见过。
- **非保守 Casimir 力。** 零温下依赖运动方向（而不只是位置）的力将是新物理。侧面滑动表面之间类摩擦的「量子摩擦」有预言但极小，且仍从运动中*取走*能量。
- **宇宙学常数问题的解法留下巨大可用能量。** 候选解（超对称抵消、人择选择、修正引力）使有效真空能量变小。没有一个使其既大又可达。

仍然真实且有趣的开放问题：为何观测到的真空能量如此之小却非零；Casimir 力能否为实用纳米机器做成排斥（在某些介质中可以：Munday, Capasso & Parsegian, *Nature* **457**, 170 (2009)）；以及温度与材料响应在微米尺度如何结合——仍是活跃争论。

## 运行实验

```bash
python Module_01_Zero_Point_Energy/simulation.py
python -m pytest tests/test_module_01.py
```

| 实验 | 展示什么 |
|---|---|
| `casimir_pressure_ideal`, `casimir_energy_ideal` | Casimir 闭式：真空确实推，仅在纳米尺度很强。 |
| `lifshitz_pressure`, `lifshitz_energy`, `gold_reduction_factor` | 对虚频率数值积分得到真实金板；弱于理想，在微米处趋近。 |
| `hamaker_constant` | 短程（van der Waals）极限的独立核验。 |
| `closed_cycle_work`, `one_shot_energy` | 闭循环净功为零；单向坍缩给出微小、不可重复的能量。 |
| `planck_density`, `naive_vacuum_energy_density`, `observed_dark_energy_density`, `cosmological_constant_gap` | 朴素「海洋」与引力所测之间约 10¹²¹ 的鸿沟。 |

## 自己动手

1. 把 `GOLD_PLASMA_EV` 改成铝的 ≈ 12.5 eV。100 nm 处金/理想比值如何变化，为何更高等离子体频率有帮助？
2. 用 `casimir_pressure_ideal`，求 Casimir 压力等于阳光压在镜子上（约 9 µPa）时的间距。
3. 试设计作弊循环：传给 `closed_cycle_work` 的压力函数，合拢时用理想律、拉开时用金律。你会得到净功——现在解释何种物理过程必须在 100 nm 处交换板的材料，以及代价是什么。
4. 在 `naive_vacuum_energy_density` 中，何种截止 $k_\text{max}$ 会使朴素估计匹配观测暗能量密度？换算成长度。（应得数十微米，毫米的几分之一——这也是亚毫米引力检验有趣的原因之一。）

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
