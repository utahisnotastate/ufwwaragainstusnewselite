# 🔬 模块 4 — 故事背后的科学

> [课程](readme.md)以 2420 年口吻讲述。本页是 2025 年现实核对：哪些已确立、故事主张在何处失效，以及它要成立必须满足什么。此处一切都可用[实验代码](../../../Module_04_Matter_Is_Frozen_Light/simulation.py)核验。

## 一句话中的 2420 主张

物质是困在微小旋转环（环面）中的光，因此电子是绕圈奔跑的光子，质量只是「冻结的光」。

## 第 1 层 — 哪些是真的

**质量与能量确实是同一货币。** Einstein 的 $E = mc^2$（1905）是物理中检验最好的方程之一。每当能量离开系统，质量随之离开：

| 过程 | 释放能量 | 消失质量 |
|---|---|---|
| 燃烧 1 kg 干木 | $1.6\times10^{7}$ J | $1.8\times10^{-7}$ g（木材的 $2\times10^{-10}$） |
| 15 千吨裂变弹 | $6.3\times10^{13}$ J | 0.7 g |

因此课中「烧木头解开结」含有真实成分：灰与气体确实轻了 $\Delta m = E/c^2$。但原子仍都在。只有约 $10^{-10}$ 的质量离开。

**你的大部分质量确实是能量，只是不是光。** 质子重 938.27 MeV/c²。其三个价夸克（上、上、下；粒子数据组方案中约 2.2 + 2.2 + 4.7 MeV）静止质量合计仅约 **1%**。其余是接近光速运动的夸克能量与束缚它们的胶子场能量，由量子色动力学（QCD）描述。格点 QCD 由此以几个百分点精度计算强子质量（Dürr et al., 2008）。若也计入虚「海」夸克（含奇夸克）的夸克质量贡献，夸克质量份额升至约 10%，仍是小部分。就此而言「质量大多是场能」是真实物理，且比故事说得更深。

**物质确实变成光，光也变成物质。**

- *物质 → 光。* 电子与正电子湮灭为两个 511 keV 光子。医院 PET 扫描仪每天探测这些光子对。
- *光 → 物质。* Breit 与 Wheeler（1934）计算：若两光子携带足够能量，可产生电子–正电子对。能量 $E_1, E_2$ 以角 $\theta$ 相遇时，不变量 $s = 2E_1E_2(1-\cos\theta)$ 必须达到 $(2m_ec^2)^2$：

$$E_1E_2(1-\cos\theta) \;\ge\; 2(m_ec^2)^2.$$

对撞时，两个 511 keV 光子恰在阈值。之上截面为

$$\sigma_{\gamma\gamma} = \frac{\pi r_e^2}{2}(1-\beta^2)\left[(3-\beta^4)\ln\frac{1+\beta}{1-\beta} - 2\beta(2-\beta^2)\right], \qquad \beta = \sqrt{1 - \frac{4m_e^2c^4}{s}},$$

其中 $r_e$ 是经典电子半径，$\beta$ 是质心系中每个轻子的速度。峰值约在 $\beta = 0.70$ 处为 $1.70\times10^{-25}$ cm² $\approx 0.256\,\sigma_T$。实验独立核验公式：从 Dirac（1930）逆过程 $e^+e^-\to\gamma\gamma$ 用细致平衡 $\sigma_{\gamma\gamma} = 2\beta^2\sigma_\text{ann}$ 重建，吻合到 $10^{-13}$。

**实验。** SLAC 实验 E‑144（Burke et al., 1997）将 527 nm 激光背散射在 46.6 GeV 电子上产生最高 29.2 GeV 的伽马射线，再与同一强激光碰撞。仅从运动学至少需同时吸收 4 个激光光子，因而是*非线性、多光子* Breit–Wheeler。RHIC 的 STAR（Adam et al., 2021）看到金核近距离擦过时强电磁场产生的 $e^+e^-$ 对，场充当*准实*光子云。两束真实光子的干净碰撞尚未完成；有提案（Pike et al., 2014）。

**从真空拉出对。** 足够强的电场可直接产生对。尺度是场在一个 Compton 长度上给予电子其静止能量之处（Sauter, Heisenberg–Euler, Schwinger）：

$$E_\text{crit} = \frac{m_e^2c^3}{e\hbar} \approx 1.32\times10^{18}\ \text{V/m}, \qquad I_\text{crit} \approx 2.3\times10^{29}\ \text{W/cm}^2.$$

## 第 2 层 — 主张在何处失效

**1. 「电子是绕圈奔跑的光子」唯一成功是白送的。** 该模型（Williamson & van der Mark, 1997）把电荷 $e$ 以 $c$ 放在半径 $r = \hbar/(m_ec) = 3.86\times10^{-13}$ m 的环上，即约化 Compton 波长。环流电荷的磁矩为

$$\mu = I\cdot\pi r^2 = \frac{ec}{2\pi r}\,\pi r^2 = \frac{ecr}{2} = \frac{e\hbar}{2m_e} = \mu_B,$$

恰为 Bohr 磁子。但 $r$ 由 $m_e$ 选出，且 $\mu_B$ *定义为* $e\hbar/2m_e$，因此这是代数恒等式。实验表明同一配方对你选的任何质量都给出「正确磁子」。它不可能失败，因此什么都不预言。

**2. 它错过了电子实际所做的。** 测得磁矩不是 $\mu_B$ 而是 $1.00115965218059\,\mu_B$（Fan et al., 2023）。量子电动力学预言那额外的 0.116%：

$$a_e = \frac{g-2}{2} = \frac{1}{2}\frac{\alpha}{\pi} - 0.3285\left(\frac{\alpha}{\pi}\right)^2 + 1.1812\left(\frac{\alpha}{\pi}\right)^3 - 1.9122\left(\frac{\alpha}{\pi}\right)^4 + \dots$$

实验使用来自铷原子反冲测量的 $\alpha$（Morel et al., 2020），不依赖 $g-2$，因此比较不是循环的：

| 模型 | 预言 $g/2$ | 偏差 |
|---|---|---|
| 光子环 | 1（精确） | $1.2\times10^{-3}$ |
| QED，1 圈（Schwinger 的 $\alpha/2\pi$） | 1.0011614 | $1.8\times10^{-6}$ |
| QED，2 圈 | 1.001159637 | $1.5\times10^{-8}$ |
| QED，3 圈 | 1.00115965223 | $5\times10^{-11}$ |
| QED，4 圈 | 1.00115965218 | $5\times10^{-12}$ |

剩余的 $5\times10^{-12}$ 是实验未计入项的预期大小（五圈 QED、更重 μ 与 τ 的圈、强子与弱效应）。QED 比环模型近约 $10^{8}$ 倍。

**3. 电子远小于该环。** LEP 高能电子–正电子散射未显示电子结构，直至约 $10^{-18}$ m。模型的环大 $4\times10^{5}$ 倍。如此大的结构会在数十年前已探测的能量上改变电子散射。

**4. 模型必须解释却未解释的其他事。** 光子无电荷，电子的电荷 $-e$ 从何而来？光子自旋 1；电子自旋 ½。μ 与 τ 与电子电荷完全相同但质量不同。单个光子无论多高能都有 $s = 0$，绝不能独自变成有质量粒子；总需要别的东西（核、第二光子、强场）。光也不会自行弯成闭环。

**5. 光不是物质的实用来源。** 两个 2 eV 阳光光子在 $s$ 上距对阈值短 $6.5\times10^{10}$ 倍；阳光光子需要 131 GeV 伽马射线作伙伴。用场从真空撕开对由因子 $e^{-\pi E_\text{crit}/E}$ 控制。迄今最强激光约 $1.1\times10^{23}$ W/cm²（Yoon et al., 2021），达到 $9\times10^{14}$ V/m $= 7\times10^{-4}\,E_\text{crit}$，给出约 $10^{-1983}$ 的因子。（真实激光脉冲振荡且聚焦，精确速率不同，但仍完全可忽略。）

**6. 为何东西感觉固实。** 不是因为旋转的光。物质稳定且不可压缩，因为电子是费米子：Pauli 不相容原理与静电学一起阻止原子坍缩进彼此（Dyson & Lenard, 1967；Lieb, 1976）。吊扇图景是可爱意象，但真实机制是量子统计。

## 第 3 层 — 必须成立什么

电子的「冻结光」模型需通过下列全部检验，每一项都有精确测量目标：

- **预言 $a_e = 0.00115965218\ldots$** 且无对其拟合的参数，如 QED 仅从 $\alpha$ 所做。
- **用一种机制解释电荷、自旋 ½ 与三代**（电子、μ、τ），并预言其质量比（206.77 与 3477.2）。标准模型也不预言这些质量；它们是开放问题，因此若模型做到将是重大发现。
- **在电子散射中于 ~$10^{-13}$ m 显示结构**（「形状因子」）。现有数据以超过五个数量级排除这一点。

附近真实开放问题：两束真实光子在 Breit–Wheeler 阈值之上的首次碰撞；在电子自身静止系中逼近 Schwinger 场的实验（激光与高能电子束的强场 QED）；以及为何 Higgs 耦合——因而夸克与轻子质量——具有它们的值。

## 运行实验

```bash
python Module_04_Matter_Is_Frozen_Light/simulation.py
python -m pytest tests/test_module_04.py
```

| 实验 | 展示什么 |
|---|---|
| `mass_defect`, `proton_valence_quark_fraction` | 化学与核尺度上的 $E = mc^2$；夸克静止质量约为质子的 ~1%。 |
| `breit_wheeler_threshold`, `pair_beta`, `breit_wheeler_cross_section` | 光变物质：阈值与截面。 |
| `breit_wheeler_from_annihilation`, `dirac_annihilation_cross_section` | 用细致平衡独立核验截面。 |
| `compton_edge`, `min_laser_photons` | 为何 SLAC E‑144 是多光子过程。 |
| `schwinger_field`, `schwinger_suppression_log10` | 当今激光距从真空撕开对有多远。 |
| `loop_magnetic_moment`, `toroidal_model_moment`, `qed_anomaly` | 光子环模型内建「成功」及其失误，对照 QED。 |

## 自己动手

1. 伽马射线需多高能才能在宇宙微波背景（典型光子能量约 $6\times10^{-4}$ eV）上产生对？这就是为何宇宙对最高能伽马射线不透明。
2. 用 μ 质量调用 `toroidal_model_moment`，并与测得的 μ 反常 $a_\mu \approx 0.00116592$ 比较。环模型对 μ 是否更好？
3. 用 `mass_defect` 反向（$E = mc^2$）计算 30 kg 儿童的静止能量。那是多少个 15 千吨炸弹？为何这类事从不自行发生？（提示：哪些守恒量必须消失？）
4. 相对 $s/(2m_ec^2)^2$ 画出 `breit_wheeler_cross_section`，并核验高能形式 $\sigma \approx \frac{4\pi r_e^2 m_e^2c^4}{s}\left[\ln\frac{s}{m_e^2c^4} - 1\right]$。
5. 用铯值 $\alpha^{-1} = 137.035999046$（Parker et al., 2018）替换 `ALPHA_RB`。4 圈预言移动多少，对照 $g/2$ 测量不确定度 $1.3\times10^{-13}$？

## 参考文献

- Einstein, A., "Ist die Trägheit eines Körpers von seinem Energieinhalt abhängig?", *Ann. Phys.* **18**, 639 (1905).
- Breit, G. & Wheeler, J. A., "Collision of two light quanta", *Phys. Rev.* **46**, 1087 (1934).
- Dirac, P. A. M., "On the annihilation of electrons and protons", *Proc. Camb. Phil. Soc.* **26**, 361 (1930).
- Schwinger, J., "On quantum‑electrodynamics and the magnetic moment of the electron", *Phys. Rev.* **73**, 416 (1948).
- Schwinger, J., "On gauge invariance and vacuum polarization", *Phys. Rev.* **82**, 664 (1951).
- Burke, D. L. et al., "Positron production in multiphoton light‑by‑light scattering", *Phys. Rev. Lett.* **79**, 1626 (1997).
- Adam, J. et al. (STAR Collaboration), "Measurement of e⁺e⁻ momentum and angular distributions from linearly polarized photon collisions", *Phys. Rev. Lett.* **127**, 052302 (2021).
- Pike, O. J., Mackenroth, F., Hill, E. G. & Rose, S. J., "A photon–photon collider in a vacuum hohlraum", *Nat. Photon.* **8**, 434 (2014).
- Yoon, J. W. et al., "Realization of laser intensity over 10²³ W/cm²", *Optica* **8**, 630 (2021).
- Williamson, J. G. & van der Mark, M. B., "Is the electron a photon with toroidal topology?", *Ann. Fond. Louis de Broglie* **22**, 133 (1997).
- Fan, X., Myers, T. G., Sukra, B. A. D. & Gabrielse, G., "Measurement of the electron magnetic moment", *Phys. Rev. Lett.* **130**, 071801 (2023).
- Morel, L., Yao, Z., Cladé, P. & Guellati‑Khélifa, S., "Determination of the fine‑structure constant with an accuracy of 81 parts per trillion", *Nature* **588**, 61 (2020).
- Parker, R. H., Yu, C., Zhong, W., Estey, B. & Müller, H., "Measurement of the fine‑structure constant as a test of the Standard Model", *Science* **360**, 191 (2018).
- Laporta, S. & Remiddi, E., "The analytical value of the electron (g−2) at order α³ in QED", *Phys. Lett. B* **379**, 283 (1996).
- Laporta, S., "High‑precision calculation of the 4‑loop contribution to the electron g‑2 in QED", *Phys. Lett. B* **772**, 232 (2017).
- Workman, R. L. et al. (Particle Data Group), "Review of Particle Physics", *Prog. Theor. Exp. Phys.* **2022**, 083C01 (2022).
- Dürr, S. et al., "Ab initio determination of light hadron masses", *Science* **322**, 1224 (2008).
- Dyson, F. J. & Lenard, A., "Stability of matter. I", *J. Math. Phys.* **8**, 423 (1967).
- Lieb, E. H., "The stability of matter", *Rev. Mod. Phys.* **48**, 553 (1976).
