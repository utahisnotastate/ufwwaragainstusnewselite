# 🔬 模块 11 — 故事背后的科学

> [课程](readme.md)以 2420 年口吻讲述。本页是 2025 年现实核对：哪些已确立、故事主张在何处失效，以及它要成立必须满足什么。此处一切都可用[实验代码](../../../Module_11_Low_Energy_Transmutation/simulation.py)核验。

## 一句话中的 2420 主张

原子核可在室温被金属晶格、酶或细菌轻轻「重折叠」成其他元素，无需高能，因此金可以种植，核废料可以变成肥料。

## 第 1 层 — 哪些是真的

**嬗变是真实的。** 原子核确实变成其他元素：在恒星、反应堆、加速器与放射性衰变中。汞‑196 甚至可在反应堆中变成金：${}^{196}$Hg 俘获中子成为 ${}^{197}$Hg，再经电子俘获衰变为 ${}^{197}$Au。它有效，但产量极小、代价极大。

**Coulomb 墙。** 电荷 $Z_1e$、$Z_2e$ 的两核以能量 $Z_1Z_2e^2/(4\pi\varepsilon_0 r)$ 相互排斥，其中 $e^2/4\pi\varepsilon_0 = 1.44$ MeV·fm。在接触距离（$r \approx 1.2(A_1^{1/3}+A_2^{1/3})$ fm）那约为**两个氘核 0.48 MeV**、**质子与钾‑39 为 5.2 MeV**。室温给粒子约 $kT = 0.026$ eV：爬过去短约 2000 万倍。

**隧穿。** 量子力学让核穿过墙。对裸 Coulomb 墙概率是 Gamow 因子

$$P(E) = e^{-2\pi\eta} = \exp\!\left(-\sqrt{E_G/E}\right),\qquad \eta = Z_1Z_2\,\alpha\sqrt{\frac{\mu c^2}{2E}},\qquad E_G = 2\mu c^2\,(\pi\alpha Z_1Z_2)^2 .$$

对 D–D，$E_G = 0.986$ MeV（实验复现 Bosch 与 Hale 的常数 $\sqrt{E_G} = 31.40$ keV$^{1/2}$）。截面写为

$$\sigma(E) = \frac{S(E)}{E}\,e^{-\sqrt{E_G/E}},$$

其中天体物理 S 因子 $S(E)$ 缓慢变化：对两条主要 D–D 分支各约 55 keV·b。对热气体平均后，这在 2 到 10 keV 给出与已发表值约 25% 内吻合的 D–D 反应率（实验中的一项测试）。

**电子屏蔽是真实的开放研究问题。** 核周围的电子部分抵消其排斥。在小距离势看起来像 $e^2/r - U_e$，这把低能截面提升

$$f(E) \approx \exp\!\left(\pi\eta\,\frac{U_e}{E}\right)\qquad (U_e \ll E)$$

（Assenbaum, Langanke & Rolfs, 1987）。对氘气预期（绝热）值为 $U_e \approx 28$ eV。keV 能量束实验对载入金属的氘报告了大得多的值，数百 eV（例如钽中约 300 eV；Raiola et al., 2002）。这些值为何如此大仍在争论。

**能量簿记。** 核反应释放或吸收能量 $Q = (\sum m_\text{in} - \sum m_\text{out})c^2$。从测得质量：D + D → T + p 释放 4.03 MeV；D + D → ³He + n 释放 3.27 MeV（各约 50% 时间）；D + D → ⁴He + γ 释放 23.85 MeV 但约每 $10^7$ 次聚变才发生一次。K‑39 + p → Ca‑40 将释放 8.33 MeV。

## 第 2 层 — 主张在何处失效

**1. 室温隧穿数字。** 在 $E = kT = 0.026$ eV，裸 D–D Gamow 因子为 $10^{-2682}$。即便实验用 800 eV 屏蔽的 WKB 计算对热能量对给出 $10^{-24}$。对仅在已比屏蔽长度 $a = e^2/U_e \approx 1800$ fm 更近时才「看到」屏蔽益处。

**2. 乐观速率估计。** 实验计算 300 K 钯氘化物（PdD，$6.8\times10^{22}$ D/cm³）中的 D–D 聚变，把每对当作被 $U_e$ 屏蔽并计入快碰撞整个 Maxwell 尾。此模型故意慷慨：

| $U_e$ | 功率（W/cm³） |
|---|---|
| 0（裸） | $2\times10^{-254}$ |
| 28 eV（气） | $9\times10^{-101}$ |
| 300 eV | $7\times10^{-19}$ |
| 800 eV | $9\times10^{-4}$ |

$U_e$ ±10% 变化使结果改变约 260 倍，且 1 W/cm³ 需要 $U_e \approx 1050$ eV。因此答案完全取决于 keV 束屏蔽值是否适用于晶格中静止的室温氘核——无人证明。Koonin 与 Nauenberg（1989）计算 D₂ 分子中仅相距 0.74 Å 的两氘核以约每秒 $10^{-64}$ 聚变。

**3. 缺失的中子（决定性检验）。** 若热来自普通 D–D 聚变，一半反应会发射 2.45 MeV 中子。用上述 Q 值：

$$\frac{1\ \text{W}}{\tfrac12(4.03+3.27)\ \text{MeV}} = 1.7\times10^{12}\ \text{fusions/s} \;\Rightarrow\; 8.6\times10^{11}\ \text{neutrons/s per watt}.$$

距无屏蔽 1 W 源 1 m 处约每小时 10 Sv：大约半小时典型致死剂量。这是「死研究生」笑话的来源。中子探测器可计数单个中子，因此即便 $10^{-12}$ W 的 D–D 聚变也可测量。冷聚变实验报告瓦级超额热却远无这些中子、氚或伽马产额。因此要么热不是 D–D 聚变，要么不是核的。

**4. 1989 年主张未被确认。** Fleischmann 与 Pons（1989）报告重水中钯电极的超额热。许多实验室试图重复且无法可靠做到。Berlinguette 等人（2019）多年计划以仔细量热重新审视主要主张，未发现异常热或核产物证据，同时沿途记下有用材料科学。

**5. 鸡与细菌。** 酶以约 0.5 eV 化学能量工作（例如 ATP 水解）。K‑39 + p → Ca‑40 势垒为 5.2 MeV，高一千万倍，实验在体温的隧穿概率为 $10^{-49515}$。Louis Kervran 的生物嬗变主张未在受控条件下被重复。产蛋母鸡从食物与骨中特殊储备吸取钙；在缺钙饮食上壳质量下降。

**6. 「折叠」不是免费的。** 把铅‑208 变成金‑197意味着移除 3 个质子与 8 个中子。质量说这至少每原子花费 77 MeV，每克金约 10 MWh，尚未计任何损失。核结合能是原因：碎片被聚在一起，拆开要花费能量。

## 第 3 层 — 必须成立什么

要使室温嬗变真实，下列全部必须被展示。每一项都是清晰、可检验目标：

- **在热能工作的屏蔽。** 在接近 eV 尺度能量测量金属中低能 D–D 产额，并展示适用于晶格中静止氘核的有效 $U_e$ 高于约 1 keV。
- **匹配热的核产物。** 每一焦耳核热必须伴随正确数量的中子、氚、³He、⁴He 或伽马射线。在同一次运行中测量它们，盲法分析。
- **改变分支比的机制。** 若没有中子，某种新物理必须把能量送入晶格而非快粒子，且必须事先预言然后观测。
- **独立重复**，由未设计原实验的实验室进行，开放数据。

**真实开放研究问题：** 为何金属中测得屏蔽能如此大；氢在金属晶格中如何行为（对储氢与脆化重要）；以及恒星天体物理的低能核截面，在地下深处测量（例如意大利 LUNA）。

## 运行实验

```bash
python Module_11_Low_Energy_Transmutation/simulation.py
python -m pytest tests/test_module_11.py
```

| 实验 | 展示什么 |
|---|---|
| `coulomb_barrier`, `gamow_energy`, `gamow_factor` | Coulomb 墙与裸隧穿概率，对照 Bosch–Hale 的 $\sqrt{E_G}$ 核验。 |
| `wkb_exponent`, `screening_enhancement` | 穿过屏蔽墙的数值 WKB 隧穿；在极限中复现解析 Gamow 与 Assenbaum 结果。 |
| `dd_reactivity_cm3_s`, `fusion_power_density` | 热 D–D 速率（在 keV 匹配已发表值）与对 PdD 的乐观室温估计。 |
| `q_value`, `neutrons_per_watt`, `dose_rate_sv_per_hour` | 来自测得质量的 Q 值与 1 W D–D 聚变将产生的中子通量。 |
| `transmutation_cost_mev` | 铅 → 金的最小能量代价。 |

## 自己动手

1. 用 `screening_needed` 求给出 1 mW/cm³ 的 $U_e$，并与钽中测得的 ~300 eV 比较。
2. 把 `fusion_power_density` 中的 `temp_k` 改为 600 K。温度加倍相比 $U_e$ 增加 10% 帮助多少？
3. 计算距 0.1 W 源 3 m 处的中子剂量率。水屏蔽需多厚？（查阅快中子在水中的衰减长度。）
4. 用 `q_value` 核验 ¹²C + ¹²C → ²⁴Mg 是否释放能量，再用 `coulomb_barrier` 与 `gamow_energy` 看为何它仅发生在大质量恒星内部。

## 参考文献

- Gamow, G., "Zur Quantentheorie des Atomkernes", *Z. Phys.* **51**, 204 (1928).
- Assenbaum, H. J., Langanke, K. & Rolfs, C., "Effects of electron screening on low‑energy fusion cross sections", *Z. Phys. A* **327**, 461 (1987).
- Bosch, H.‑S. & Hale, G. M., "Improved formulas for fusion cross‑sections and thermal reactivities", *Nucl. Fusion* **32**, 611 (1992).
- Raiola, F. et al., "Enhanced electron screening in d(d,p)t for deuterated Ta", *Eur. Phys. J. A* **13**, 377 (2002).
- Koonin, S. E. & Nauenberg, M., "Calculated fusion rates in isotopic hydrogen molecules", *Nature* **339**, 690 (1989).
- Fleischmann, M., Pons, S. & Hawkins, M., "Electrochemically induced nuclear fusion of deuterium", *J. Electroanal. Chem.* **261**, 301 (1989).
- Berlinguette, C. P. et al., "Revisiting the cold case of cold fusion", *Nature* **570**, 45 (2019).
- Wang, M. et al., "The AME 2020 atomic mass evaluation (II)", *Chinese Phys. C* **45**, 030003 (2021). Source of the atomic masses.
- ICRP Publication 74, *Conversion Coefficients for use in Radiological Protection against External Radiation* (1996). Source of the approximate neutron dose coefficient.
- Huba, J. D., *NRL Plasma Formulary* (Naval Research Laboratory, revised regularly). Tabulated D–D reactivities used in the tests.
