# 🔬 模块 6 — 故事背后的科学

> [课程](readme.md)以 2420 年口吻讲述。本页是 2025 年现实核对：哪些已确立、故事主张在何处失效，以及它要成立必须满足什么。此处一切都可用[实验代码](../../../Module_06_Language_of_Reality/simulation.py)核验。

## 一句话中的 2420 主张

自然界的一切形状都是「冻结的声音」：驻波像提琴弓在板上安排沙子那样安排物质，因此正确的声音可以建造物质、溶解它，或使石头失重。

## 第 1 层 — 哪些是真的

**Chladni 图形是真实的，而且是美丽的物理。** Ernst Chladni（1787）用弓拉覆沙金属板，发现沙子沿**节线**聚集，那里板不动。每个音符给出不同图形。设定图形的是板的运动方程。

**鼓皮与板服从不同方程。** 张紧膜（鼓皮）服从波动（Helmholtz）方程 $\nabla^2 w + k^2 w = 0$。边长 $L$ 的固定边方膜频率为

$$f_{mn} = \frac{c}{2L}\sqrt{m^2+n^2}.$$

Chladni 板是薄而硬的**板**，由 Kirchhoff 双调和方程支配

$$D\,\nabla^4 w - \rho h\,\omega^2 w = 0, \qquad D = \frac{E h^3}{12(1-\nu^2)} .$$

对简支方板精确答案是 $\omega_{mn} = \sqrt{D/\rho h}\;\pi^2 (m^2+n^2)/L^2$，因此 $f_{mn} \propto m^2 + n^2$，**不是** $\sqrt{m^2+n^2}$。那是真实、可检验的课：在鼓上 (1,2) 模态位于基频的 $\sqrt{5/2} = 1.58$ 倍，在板上则为 $5/2 = 2.5$ 倍。实验数值求解两方程（5 点边界 Helmholtz 模板与 13 点双调和模板），以优于 0.5% 匹配精确结果，并具有预期的二阶收敛。

当两模态同频（例如方板上的 (1,2) 与 (2,1)）时，板以混合振动，$\sin m\pi x\,\sin n\pi y \pm \sin n\pi x\,\sin m\pi y$。这些混合产生真实 Chladni 图形的对角线、环与星；实验核验「−」混合恰在对角线上有节线。Chladni 自己的自由边板更难解（Leissa 1969 收集经典结果）。对圆板，**Chladni 定律** $f \approx C\,(m + 2n)^p$（$m$ 节直径，$n$ 节圆，$p \approx 2$ 对平板）是良好经验规则（Rossing 1982）。

**声音确实可以推、困与悬浮小物体。** 驻波对远小于波长的粒子施加稳态**声辐射力**。Gor'kov（1962）表明它来自势，

$$U = 2\pi R^3\left[\frac{f_1\,\langle p^2\rangle}{3\rho_0 c_0^2} - \frac{f_2\,\rho_0\langle v^2\rangle}{2}\right], \qquad \mathbf F = -\nabla U,$$

$$f_1 = 1 - \frac{\kappa_p}{\kappa_0}, \qquad f_2 = \frac{2(\rho_p-\rho_0)}{2\rho_p+\rho_0} .$$

因为 $\mathbf F = -\nabla U$，此力是**保守的**（本模块早期草稿称其为非保守，那是错的）：沿闭路径搬粒子净功为零，粒子落在 $U$ 的极小处。在一维驻波 $p = p_0\cos kx\cos\omega t$ 中变为 $F = 4\pi\Phi\,kR^3 E_\text{ac}\sin 2kx$，对比因子 $\Phi = f_1/3 + f_2/2$，能量密度 $E_\text{ac} = p_0^2/4\rho_0 c_0^2$（Bruus 2012）。实验核验 $U$ 的数值梯度与此公式，显示一波长上净功为零，并让粒子漂移：

- 水中聚苯乙烯（$\Phi = +0.22$）聚集在**压力节点**，
- 水中脂质液滴（$\Phi = -0.07$）聚集在**压力腹点**。

这是声流体细胞分选器与**声悬浮器**的工作原理。Marzo 等人（2015）用 40 kHz 换能器阵列建造全息声镊，在空气中悬浮并移动毫米珠。实验估计所需压力：泡沫珠约 280 Pa（140 dB），实心聚苯乙烯约 1.8 kPa（156 dB），只要珠远小于 8.6 mm 波长就与珠大小无关。

**雪花呈六边形有真实原因，但不是声音。** 普通冰（冰 Ih）具有由水分子间氢键几何设定的六方晶格。雪晶的六重形状来自该晶格以及蒸汽如何扩散到其上（Libbrecht 2005）。

## 第 2 层 — 主张在何处失效

**1. 图案尺度是波长。** 声音只能在半波长尺度上组织物质：空气中 40 kHz 为 4.3 mm。要安置单个原子（~0.1 nm）需要 0.2 nm 波长。实验说明为何不可能：

| 介质 | 所需频率 | 极限 |
|---|---|---|
| 固体（$c \approx 5$ km/s） | ~25 THz | 硅最高振动为 15.6 THz，晶格能携带的最短波是原子间距的两倍，0.47 nm。 |
| 空气 | ~1.7 × 10¹² Hz | 声音在分子平均自由程（~66 nm）以下不存在，将其封顶在近 5 GHz。 |

在原子尺度，「声音」（声子）就是原子本身在抖动。它不能成为安置它们的模板。

**2. 振动骑在键上；它们不制造键。** 硅最高声子携带 65 meV。从晶体移除一个原子花费 4.63 eV，约 70 倍。把物质聚在一起的是电子的量子力学（化学键），不是持续的音调。

**3. 大石头不能被唱到空中。** Gor'kov 公式仅适用于远小于波长的物体。对 2 m 块，波长必须为数十米（约 17 Hz）。在该频率托起花岗岩需要 1.4 大气压的压力振幅：每周期低压半周必须落到**真空以下**，空气做不到。声学中没有任何东西使物体「忘记自己很重」。相位共轭或「时间反转声学」是真实的（Fink 1997），但它把波重新聚焦回源。它不取消重量。

**4. 理论名称站不住。** 「Formon 理论」（Bearden）**不是物理中公认的理论**：没有同行评议表述或实验支持。「推动时空的标量声音」在物理中没有对应物。纵波就是普通声音（在空气中所有声音都是纵波），它们推动物质，不是时空。Hans Jenny 的 *Cymatics*（1967）是振动图案的可爱摄影记录，但不表明物质是「冻结的声音」。

## 第 3 层 — 必须成立什么

要使「用声音建造物质」不止是隐喻，需要下列全部：

- **具有原子尺度波长、且不是由它所安排的原子构成的波。** 光与电子束确实有如此短的波长。这就是为何光镊、电子显微镜与扫描探针「写原子」有效，它们通过电磁学而非声音做到。
- **每个量子的能量可与键能（eV）相比。** 只有那时波才能直接制造或打断键。声音量子上限为数十 meV。
- **定量预言。** 例如可测量改变晶体结构或石头重量的特定频率，实验室随后可检验。从未发表过。

真实、开放的前沿更谦逊且仍令人兴奋：一次组装许多粒子的声全息、细胞与组织的声操控，以及工程化引导声音与热的声子晶体。

## 运行实验

```bash
python Module_06_Language_of_Reality/simulation.py
python -m pytest tests/test_module_06.py
```

| 实验 | 展示什么 |
|---|---|
| `membrane_frequencies`, `membrane_modes_fd` | 鼓皮：$f \propto \sqrt{m^2+n^2}$，由有限差分求解确认。 |
| `plate_frequencies`, `plate_modes_fd`, `biharmonic_simply_supported` | 板：$f \propto m^2+n^2$，由 13 点双调和求解确认。 |
| `chladni_pattern` | 简并模态混合及其节线（沙子聚集处）。 |
| `gorkov_potential_1d`, `gorkov_force_1d`, `settle_positions` | 保守辐射力；正对比去节点，负对比去腹点。 |
| `levitation_pressure`, `spl_db` | 140–156 dB 悬浮珠；石头需要「真空以下」压力。 |
| `atom_scale_sound`, `mean_free_path_air` | 为何声音无法安置原子。 |

## 自己动手

1. 在 `biharmonic_simply_supported` 中把鬼节点符号从 $-1$ 改为 $+1$。这把边从「简支」变为「固支」。$f_{21}/f_{11}$ 发生什么？（固支板更接近真实铃与钹。）
2. 把 `chladni_pattern(1, 3, sign=+1)` 与 `sign=-1` 画成图像并标出 $|w|$ 小处。哪一个更像你见过的 Chladni 图形？
3. 用 `levitation_pressure` 求以 150 dB 悬浮 1 mm 水滴的频率。液滴是否仍远小于波长？
4. 对金刚石重做 `atom_scale_sound`（声速约 18 km/s，最高声子约 1332 cm⁻¹）。是否更接近「安置原子」？
5. 计算血浆中红细胞的 $\Phi$（查阅近似密度与声速）。它们会去节点还是腹点？

## 参考文献

- Chladni, E. F. F., *Entdeckungen über die Theorie des Klanges*, Leipzig (1787).
- Leissa, A. W., *Vibration of Plates*, NASA SP‑160 (1969).
- Fletcher, N. H. & Rossing, T. D., *The Physics of Musical Instruments*, 2nd ed., Springer (1998). Plate modes and Chladni patterns.
- Rossing, T. D., "Chladni's law for vibrating plates", *Am. J. Phys.* **50**, 271 (1982).
- Gor'kov, L. P., "On the forces acting on a small particle in an acoustical field in an ideal fluid", *Sov. Phys. Dokl.* **6**, 773 (1962).
- Bruus, H., "Acoustofluidics 7: The acoustic radiation force on small particles", *Lab Chip* **12**, 1014 (2012).
- Marzo, A. et al., "Holographic acoustic elements for manipulation of levitated objects", *Nat. Commun.* **6**, 8661 (2015).
- Fink, M., "Time reversed acoustics", *Physics Today* **50**(3), 34 (1997).
- Libbrecht, K. G., "The physics of snow crystals", *Rep. Prog. Phys.* **68**, 855 (2005).
- Kittel, C., *Introduction to Solid State Physics*, 8th ed., Wiley (2005). Cohesive energies and phonons.
- Jenny, H., *Kymatik / Cymatics*, Basilius Presse (1967).
