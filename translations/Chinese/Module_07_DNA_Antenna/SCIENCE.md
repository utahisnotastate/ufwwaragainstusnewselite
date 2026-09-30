# 🔬 模块 7 — 故事背后的科学

> [课程](readme.md)以 2420 年口吻讲述。本页是 2025 年现实核对：哪些已确立、故事主张在何处失效，以及它要成立必须满足什么。此处一切都可用[实验代码](../../../Module_07_DNA_Antenna/simulation.py)核验。

## 一句话中的 2420 主张

DNA 是线圈形天线，从信息场——包括你自己的思想与感受——接收指令，并重写身体以匹配。

## 第 1 层 — 哪些是真的

**DNA 的形状被精确已知。** B‑DNA（细胞中的形式）是右手双螺旋（Watson & Crick 1953；Franklin & Gosling 1953），具有

- 直径约 **2.0 nm**，
- 每碱基对上升 **0.34 nm**，
- 溶液中约 **每圈 10.5 碱基对**（每步扭转 34.3°），因此螺距 **3.4–3.6 nm**。

它在短距离上也僵硬：生理盐中持续长度约 50 nm。

**DNA 确实强烈与光相互作用，在紫外。** DNA 在约 **260 nm**（每光子 4.77 eV）吸收最强。日常实验室规则「260 nm 吸光度为 1 意味着 50 µg/mL 双链 DNA」给出约 **每核苷酸 6600 M⁻¹cm⁻¹**。双螺旋比相同碱基作为游离核苷酸约少吸收 30–40%（实验用近似教科书核苷酸值得到 39%）。这种**减色性**因为堆叠碱基电子耦合。UV 激发后，激发可在若干堆叠碱基间共享，堆叠控制能量耗散有多快（Crespo‑Hernández, Cohen & Kohler 2005）。这是真实、快速的物理，并帮助保护 DNA 免受 UV 损伤。它作用于几个碱基、几个纳米。

**能量可沿 DNA 跳跃，跨越纳米。** Förster 共振能量转移（FRET）以效率

$$E = \frac{1}{1 + (r/R_0)^6}$$

把激发从供体染料移到受体，其中 $R_0$ 通常约 5 nm。沿 DNA 螺旋放置时，相距 15 碱基对（5.1 nm）的染料转移约一半能量；30 碱基对处约 1%。这种陡峭的 $r^{-6}$ 衰减是为何 FRET 被用作「光谱尺」（Stryer & Haugland 1967），常以 DNA 本身为尺。

**DNA 振动并「呼吸」。** Peyrard–Bishop 模型（1989）把每个碱基对当作由 Morse 势 $V(y) = D\,(e^{-ay} - 1)^2$（氢键）保持的拉伸 $y_n$，并通过堆叠弹簧与邻居耦合：

$$H = \sum_n \left[\frac{p_n^2}{2m} + \frac{k}{2}(y_n - y_{n-1})^2 + D\,(e^{-a y_n} - 1)^2\right].$$

小振荡形成声子带，$m\omega^2 = 2Da^2 + 4k\sin^2(q/2)$，在太赫兹范围。实验对照数值 Hessian 核验。实验也用转移积分方法精确求解模型热力学：温度上升时碱基对略微更多地打开，超过阈值后链分开（变性或「熔融」）。用此处说明性的谐堆叠参数，那发生在近 490 K，远高于真实 DNA 的 340–370 K。Dauxois, Peyrard & Bishop（1993）表明加入非线性堆叠给出实验所见的尖锐熔融。要点是定性的：DNA 的动力学是普通热物理。

**基因通过化学被环境调控。** 表观遗传标记（DNA 甲基化、组蛋白修饰）改变哪些基因表达。它们响应饮食、激素与经历；例如在大鼠中，母爱改变后代应激激素受体基因的甲基化（Weaver et al. 2004）。信号是分子：激素、转录因子与酶。

**关于「垃圾 DNA」。** 人类基因组约 1–2% 编码蛋白质。调控元件（启动子、增强子）与非编码 RNA 真实且重要。ENCODE 项目（2012）报告基因组 80% 有「生化功能」，但该定义计入任何生化活动，如被转录一次或被蛋白结合。它受到强烈争议，例如 Graur 等人（2013）主张功能应意味着选择所保存的东西。处于进化约束下的基因组份额估计远更低。

## 第 2 层 — 主张在何处失效

**1. 若 DNA 是天线，它将调谐到 X 射线，而非思想或生物光子。** 螺旋天线沿其轴辐射（Kraus 的「轴向模式」）当周长 $C$ 满足 $\tfrac34 < C/\lambda < \tfrac43$。对 B‑DNA，$C = \pi \times 2.0\text{ nm} = 6.3$ nm，因此

$$\lambda \approx 4.7\text{–}8.4\text{ nm} \quad (150\text{–}260\text{ eV}),$$

这是极紫外或软 X 射线，并使分子电离。从活组织报告的超弱「生物光子」发射（200–800 nm；见 Cifra & Pospíšil 2014）**长 30–130 倍**。其螺距角（30°）也在 Kraus 最佳范围 12–14° 之外。此外，DNA 不是金属线：其骨架不像天线那样携带自由电子。

**2. 生物光子太少，无法携带指令。** 即便慷慨的每秒每 cm² 100 光子，全部瞄准 DNA，击中给定螺旋圈约 **每 4400 年一次**。

**3. 盐水屏蔽并吸收。** 细胞是咸水。在 150 mM 时 **Debye 屏蔽长度**为

$$\lambda_D = \sqrt{\frac{\varepsilon_r\varepsilon_0 k_B T}{2 N_A e^2 I}} \approx \frac{0.304}{\sqrt{I\,[\text{M}]}}\ \text{nm} \approx 0.78\text{ nm}.$$

电荷的静电场在 10 nm 外已降到百万分之几。振荡场确实穿过，但盐水（电导率约 1.6 S/m）的 Debye 弛豫模型显示微波在 **1 GHz 约 2.6 cm、10 GHz 约 2.4 mm、100 GHz 约 0.24 mm** 内降到 $1/e$。作为 1 GHz 偶极的 50 nm 僵硬 DNA 段辐射电阻约 $10^{-11}\ \Omega$，而工作天线约 50 Ω。它是极其糟糕的天线。

**4. 无线电光子太弱，无法做化学。** 1 GHz 光子在体温携带 $1.5\times10^{-4}\,k_BT$。分子每皮秒被数千倍更多能量推挤。这就是为何 UV（260 nm 每光子 178 $k_BT$）损伤 DNA 而无线电不。

**5. 「幽灵叶片」与「促有丝分裂辐射」故事。** 对电晕放电（Kirlian）摄影的受控研究发现图像强烈依赖湿度、压力与曝光条件（Pehek, Kyler & Faust 1976）。「幽灵叶片」不是已确立效应。Gurwitsch 的促有丝分裂辐射与 Kaznacheyev 的「细胞病变转移」主张未被独立重复确立。

**6. 没有证据表明 DNA 从场接收「形态发生指令」。** 身体如何成形被详细研究，并通过基因、蛋白质、信号分子梯度以及细胞间机械与电线索工作。你的感受确实可以通过神经、激素与免疫系统影响身体，表观遗传是该故事的一部分。但信使是分子，不是广播。

## 第 3 层 — 必须成立什么

要使「DNA 作为天线」成为科学假说，某人需要展示下列全部：

- **在盐水中工作的接收器。** 要么穿透组织*并*耦合到 2 nm 螺旋的信号频率，要么不被屏蔽与热噪声冲刷掉的机制（例如分子共振）。可测量检验：在细胞培养中改变基因表达的特定频率，带剂量–响应曲线、盲法与独立重复。
- **每信号足够能量。** 改变 DNA 化学需要每事件近电子伏特的能量，或细胞内把微弱信号放大为大响应同时战胜 $k_BT$ 噪声的放大器。
- **「来自场的信息」的载体。** 故事需要具有可测强度与预言光谱的命名物理场。按字面写，它不预言任何可核验的数字。

附近开放问题真实且有趣：电荷沿 DNA 能走多远（几个纳米，在堆叠碱基间跳跃）、UV 能量如何在堆叠碱基间共享、DNA「呼吸」如何帮助蛋白质读取它，以及非编码基因组有多少重要。

## 运行实验

```bash
python Module_07_DNA_Antenna/simulation.py
python -m pytest tests/test_module_07.py
```

| 实验 | 展示什么 |
|---|---|
| `b_dna_geometry`, `helical_antenna_band`, `biophoton_mismatch` | DNA 大小的螺旋将调谐到 ~6 nm（EUV/软 X 射线），比生物光子短 30–130×。 |
| `photon_hits_per_turn` | 生物光子通量在分子尺度上微不足道。 |
| `uv_absorption` | 260 nm 每核苷酸 ~6600 M⁻¹cm⁻¹，堆叠减色性 ~39%。 |
| `fret_efficiency`, `fret_along_dna` | 沿 DNA 的能量转移：~15 bp 处 50%，30 bp 处 ~1%。 |
| `pb_mode_frequencies_numeric`, `pb_dispersion`, `pb_transfer_integral` | Peyrard–Bishop 振动（THz）与热打开及变性。 |
| `debye_length`, `water_permittivity`, `field_penetration_depth` | 0.78 nm 屏蔽；微波在 mm–cm 内被吸收。 |
| `short_dipole_radiation_resistance`, `rf_photon_vs_thermal` | DNA 是无望的 RF 天线；无线电光子 ≪ $k_BT$。 |

## 自己动手

1. 用 `debye_length` 求屏蔽长度达到 1 µm 的盐浓度。活细胞能在那么纯的水中存活吗？
2. 把 `fret_along_dna` 中的 `R0_nm` 改为 3 nm 与 7 nm。50% 点移动多少碱基对？
3. 在 `pb_transfer_integral` 中加倍 `D`。来自 `pb_denaturation_temperature` 的解链温度如何变化？与按 $\sqrt{kD}$ 标度的 `pb_continuum_estimate` 比较。
4. 一个细胞中人类基因组约 $6.4\times10^9$ 碱基对（两份拷贝）。用 `RISE_NM` 求一个细胞中 DNA 总长度。若它是真空中的直半波偶极，将调谐到何频率，该频率在盐水中传播多远（`field_penetration_depth`）？
5. 求体温下 `rf_photon_vs_thermal` 等于 1 的频率。那是光谱的哪一部分？

## 参考文献

- Watson, J. D. & Crick, F. H. C., "Molecular structure of nucleic acids", *Nature* **171**, 737 (1953).
- Franklin, R. E. & Gosling, R. G., "Molecular configuration in sodium thymonucleate", *Nature* **171**, 740 (1953).
- Kraus, J. D., *Antennas*, 2nd ed., McGraw‑Hill (1988). Helical antenna modes.
- Crespo‑Hernández, C. E., Cohen, B. & Kohler, B., "Base stacking controls excited‑state dynamics in A·T DNA", *Nature* **436**, 1141 (2005).
- Cavaluzzi, M. J. & Borer, P. N., "Revised UV extinction coefficients for nucleoside‑5′‑monophosphates and unpaired DNA and RNA", *Nucleic Acids Res.* **32**, e13 (2004).
- Förster, T., "Zwischenmolekulare Energiewanderung und Fluoreszenz", *Ann. Phys.* **437**, 55 (1948).
- Stryer, L. & Haugland, R. P., "Energy transfer: a spectroscopic ruler", *Proc. Natl. Acad. Sci. USA* **58**, 719 (1967).
- Peyrard, M. & Bishop, A. R., "Statistical mechanics of a nonlinear model for DNA denaturation", *Phys. Rev. Lett.* **62**, 2755 (1989).
- Dauxois, T., Peyrard, M. & Bishop, A. R., "Entropy‑driven DNA denaturation", *Phys. Rev. E* **47**, R44 (1993).
- Israelachvili, J. N., *Intermolecular and Surface Forces*, 3rd ed., Academic Press (2011). Debye length.
- Kaatze, U., "Complex permittivity of water as a function of frequency and temperature", *J. Chem. Eng. Data* **34**, 371 (1989).
- Cifra, M. & Pospíšil, P., "Ultra‑weak photon emission from biological samples: definition, mechanisms, properties, detection and applications", *J. Photochem. Photobiol. B* **139**, 2 (2014).
- Pehek, J. O., Kyler, H. J. & Faust, D. L., "Image modulation in corona discharge photography", *Science* **194**, 263 (1976).
- Weaver, I. C. G. et al., "Epigenetic programming by maternal behavior", *Nat. Neurosci.* **7**, 847 (2004).
- ENCODE Project Consortium, "An integrated encyclopedia of DNA elements in the human genome", *Nature* **489**, 57 (2012).
- Graur, D. et al., "On the immortality of television sets: 'function' in the human genome according to the evolution‑free gospel of ENCODE", *Genome Biol. Evol.* **5**, 578 (2013).
