# 🔬 模块 10 — 故事背后的科学

> [课程](readme.md)以 2420 年口吻讲述。本页是 2025 年现实核对：哪些已确立、故事主张在何处失效，以及它要成立必须满足什么。此处一切都可用[实验代码](../../../Module_10_Time_Reversal_Healing/simulation.py)核验。

> ⚕️ **健康提示。** 本课中没有任何内容是医疗建议或治疗方法。时间反转疗愈今天并不存在。若你生病或受伤，请就医；手术与药物能挽救生命。

## 一句话中的 2420 主张

「相位共轭镜」可记录生病或衰老身体的失真「波」，时间反转地送回，从而撤销损伤，恢复身体更早的健康状态。

## 第 1 层 — 哪些是真的

**相位共轭是真实光学。** 1972 年 Zel'dovich 与合作者表明受激 Brillouin 散射反射的光带着波前反转回来：路上被搅乱的光束在路上被解扰。不久后，Hellwarth 与 Yariv 用 $\chi^{(3)}$（Kerr 型）非线性材料中的简并四波混频展示了同样的事。若入射场为

$$E(\mathbf r, t) = \mathrm{Re}\big[A(\mathbf r)\,e^{i(kz-\omega t)}\big],$$

相位共轭镜返回 $A^*(\mathbf r)\,e^{i(-kz-\omega t)}$。对单色波那恰是时间反转波：每条射线沿原路返回。

**为何那撤销失真。** 薄像差层把场乘以 $e^{i\phi(x)}$。相位共轭后场携带 $e^{-i\phi(x)}$，再次穿过同一层给出 $e^{-i\phi}e^{+i\phi} = 1$。自由空间传播是幺正的，因此以同样方式被撤销。实验把光束送过 2 弧度随机相位屏再回来：共轭镜以保真度 $1.000000$ 返回原光束，而普通镜子返回保真度 $0.0025$。

**穿过组织聚焦是真实研究领域。** 生物组织多次散射光。Yaqoob 等人（2008）用光学相位共轭撤销穿过鸡胸肉片的散射（「浊度抑制」）。Vellekoop 与 Mosk（2007）通过调节输入光束 $N$ 段的相位把光聚焦*穿过*不透明层。对充分发展的散斑，预期亮度增益为

$$\eta = \frac{\pi}{4}(N-1) + 1.$$

实验用随机传输矩阵复现此律（例如 $N = 1024$ 给出 805，对照预言 804.5）。这些方法正被开发用于深层组织成像与光投递。

**生物电是真实、可测量的物理。** 每个细胞在膜上保持电压。对一种离子，平衡（Nernst）电位为

$$E_\text{ion} = \frac{RT}{zF}\ln\frac{[\text{ion}]_\text{out}}{[\text{ion}]_\text{in}},$$

在 37 °C 对 $[K]_o = 5$ mM、$[K]_i = 140$ mM 给出 $E_K = -89$ mV。有几种离子时静息电压由 Goldman–Hodgkin–Katz 方程设定：

$$V_m = \frac{RT}{F}\ln\frac{P_K[K]_o + P_{Na}[Na]_o + P_{Cl}[Cl]_i}{P_K[K]_i + P_{Na}[Na]_i + P_{Cl}[Cl]_o}.$$

用教科书哺乳动物值实验得到 $-67$ mV。Michael Levin 的小组与其他人研究这些电压图案如何帮助引导青蛙与涡虫等动物的胚胎发育与再生（Levin, 2021）。这是活跃基础研究，不是疗法。

**生命一直合法地降低自身熵。** 静息人类释放约 100 W 热。每天，$8.6\times10^6$ J 以 310 K 离开身体，带走 $Q/T_\text{body} \approx 27{,}900$ J/K 的熵，并以 $Q/T_\text{room} \approx 29{,}500$ J/K 进入 293 K 房间。细胞通过以更大熵导出支付局部秩序来修复 DNA、替换蛋白质与愈合伤口。第二定律对身体加环境成立。

## 第 2 层 — 主张在何处失效

**1. 相位共轭镜反转波，不是物质。** 上述抵消有效是因为*同一*层被穿过两次。它反转光场；它不反转光穿过的原子。身体不是要被反射的波：其细胞、蛋白质与 DNA 是故事的镜子从不作用的物质。

**2. 介质在两次通过之间不得改变。** 若像差层改变，回程不再抵消第一次。对 rms 相位 $\sigma$、两次通过间相关 $\rho$ 的高斯相位屏，保真度为

$$F = e^{-2\sigma^2(1-\rho)}.$$

实验测得 $\rho = 0.99$ 时 $F = 0.92$，$\rho = 0.9$ 时 $0.44$，$\rho = 0.5$ 时约 $0$（理论 $0.92$、$0.45$、$0.02$）。活组织不断重排，体内光学实验必须在短窗口内（通常毫秒）校正。故事想「反转」*数十年*积累的变化，此时 $\rho \approx 0$ 且保真度为零。在散射组织模型中，组织移动前学到的校正给出增益 $0.92$：并不比完全不校正更好。

**3. 镜子必须捕获整个场。** 实验展示精确结果：介质不变时，保真度等于镜子截获的功率分数（差低于 $10^{-15}$）。逃逸的永远丢失。仅要在 800 nm 控制 1 cm² 组织上的光就需要约 $6\times10^{8}$ 个独立模式。故事中没有任何东西解释如何捕获身体中每个分子的「波」。

**4. 没有储存在「时间通道」中的「年轻图案」。** 物理没有等待重播的身体过去状态记录。你细胞在 20 岁时如何排列的信息已作为热散入环境，即上述同一熵导出。能量不是极限（100 W 原则上可在 Landauer 极限 $kT\ln 2$ 支付每秒擦除约 $3\times10^{22}$ 比特）。缺少的是信息与作用于每个分子的机制。

**5. 「Priore 机器」。** Antoine Priore 在 1960–70 年代法国建造电磁装置，并报告对动物肿瘤与感染的效应。结果从未被独立重复或验证，装置不是公认治疗。

**6. 手术与医学不是「用锤子敲计算机」。** 现代医学大量建立在物理与化学之上，并且有效：疫苗、抗生素、麻醉与手术挽救数百万生命。课中的对比是虚构的一部分。

## 第 3 层 — 必须成立什么

要使「时间反转疗愈」存在，下列全部必须成立。每一项都是具体目标：

- **身体状态的物理载体**，可被「反射」。检验：表明身体外某场以细胞分辨率编码组织结构并可被测量。
- **过去状态的存储记录。** 检验：从今天的测量恢复可验证的更早状态（例如旧疤痕图案），无先前照片或样本。
- **把返回波变成重排分子的机制**，方式匹配已知化学且不把组织煮熟。
- **时间上的相干。** 任何「反转」必须在身体以毫秒到年时标变化时仍工作，而这如上所示摧毁共轭保真度。

**更接近故事精神的真实开放问题：**

- 波前整形与光学相位共轭能把聚焦、成像与光投递在活组织深处推多远？
- 生物电信号能否用于驾驭动物再生，并稍后安全用于人类？（早期研究；无批准疗法。）
- 什么设定身体自身修复的极限，生物学（例如干细胞与再生医学）能否扩展它？

## 运行实验

```bash
python Module_10_Time_Reversal_Healing/simulation.py
python -m pytest tests/test_module_10.py
```

| 实验 | 展示什么 |
|---|---|
| `round_trip` | 相位共轭精确取消随机像差；普通镜子不能。 |
| `round_trip(rho=...)`, `decorrelation_fidelity_theory` | 若介质在两次通过间改变，保真度按 $e^{-2\sigma^2(1-\rho)}$ 下降。 |
| `round_trip(aperture=...)` | 保真度等于镜子捕获的场分数。 |
| `wavefront_shaping_enhancement`, `vellekoop_mosk_theory` | 穿过散射介质聚焦遵循 $\tfrac{\pi}{4}(N-1)+1$，介质改变则丢失。 |
| `nernst`, `ghk_voltage` | 来自离子浓度的真实膜电压（静息约 $-67$ mV）。 |
| `entropy_budget`, `landauer_bits_per_second` | 生命通过导出更多降低局部熵；第二定律总体上成立。 |

## 自己动手

1. 在 `round_trip` 中把 `rms_rad` 从 2 升到 4。介质变化必须多慢（$\rho$ 必须多接近 1）才能保持 90% 保真度？对照 $e^{-2\sigma^2(1-\rho)}$ 核验。
2. 用 `with_changes` 求静息电压达到 $-55$ mV 的细胞外钾水平。（医生因此密切关注血钾。）
3. 用仅*部分*改变的介质运行 `wavefront_shaping_enhancement`：把新旧传输矩阵混合为 $\sqrt{\rho}\,t_\text{old} + \sqrt{1-\rho}\,t_\text{new}$。增益如何随 $\rho$ 下降？
4. 对 35 °C 房间重做 `entropy_budget`。净熵产生发生什么，为何热环境使散热更难？

## 参考文献

- Zel'dovich, B. Ya., Popovichev, V. I., Ragul'skii, V. V. & Faizullov, F. S., "Connection between the wave fronts of the reflected and exciting light in stimulated Mandel'shtam‑Brillouin scattering", *JETP Lett.* **15**, 109 (1972).
- Hellwarth, R. W., "Generation of time‑reversed wave fronts by nonlinear refraction", *J. Opt. Soc. Am.* **67**, 1 (1977).
- Yariv, A., "Phase conjugate optics and real‑time holography", *IEEE J. Quantum Electron.* **14**, 650 (1978).
- Vellekoop, I. M. & Mosk, A. P., "Focusing coherent light through opaque strongly scattering media", *Opt. Lett.* **32**, 2309 (2007).
- Yaqoob, Z., Psaltis, D., Feld, M. S. & Yang, C., "Optical phase conjugation for turbidity suppression in biological samples", *Nature Photonics* **2**, 110 (2008).
- Goldman, D. E., "Potential, impedance, and rectification in membranes", *J. Gen. Physiol.* **27**, 37 (1943).
- Hodgkin, A. L. & Katz, B., "The effect of sodium ions on the electrical activity of the giant axon of the squid", *J. Physiol.* **108**, 37 (1949).
- Levin, M., "Bioelectric signaling: Reprogrammable circuits underlying embryogenesis, regeneration, and cancer", *Cell* **184**, 1971 (2021).
- Landauer, R., "Irreversibility and heat generation in the computing process", *IBM J. Res. Dev.* **5**, 183 (1961).
