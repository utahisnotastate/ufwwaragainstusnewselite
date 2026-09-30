# 2420 年代的「失落」课程 — 为人类讲解显而易见的物理学

[![tests](https://github.com/utahisnotastate/ufwwaragainstusnewselite/actions/workflows/tests.yml/badge.svg)](https://github.com/utahisnotastate/ufwwaragainstusnewselite/actions/workflows/tests.yml)

☕ 支持本项目：[ko-fi.com/utah23](https://ko-fi.com/utah23) · 我为什么做这个：[ABOUT.md](ABOUT.md)

十二个大想法，每个用三种方式讲授：

| 层级 | 文件 | 是什么 |
|---|---|---|
| 📖 **故事** | `readme.md` | 以 2420 年学校口吻写成的课，面向聪明的 8 岁孩子和好奇的成年人。围绕真实问题的科幻。 |
| 🔬 **科学** | `SCIENCE.md` | 2025 年现实核对：哪些已确立、故事主张在何处用数字失效、以及它要成立必须满足什么。附真实参考文献。 |
| 🧪 **实验** | `simulation.py` | 可运行的 Python，计算科学页中的每一个数字。对照教科书极限与已发表测量做过测试。 |

每个模块还保留设定内的 `PHYSICS_PROOF.md`：2420 档案自己的论证，明确标注为故事的一部分。

**为什么用这种格式？** 故事是钩子。它们提出孩子真正会问的问题：*空间真的是空的吗？引力为什么拉？我们能瞬间旅行吗？* 科学页诚实作答，包括「不行，而这是说明原因的计算。」弄清一个美丽想法在何处失效，比被告知它成立能学到更多物理。

实验代码仍在英文模块文件夹中（仓库根目录）。从本翻译目录运行时，请指向 `../../../Module_NN_Name/simulation.py`。

---

## 快速开始

```bash
python -m pip install -r requirements.txt
python Module_02_Gravity_Is_Pushing/simulation.py   # 运行一个实验（在仓库根目录）
python -m pytest                                    # 检查每一个实验
```

需要 Python 3.10+ 以及 NumPy 与 SciPy。不需要绘图库或网络连接。

---

## 模块索引

| # | 模块 | 2420 故事说…… | 实验计算什么 |
|---|---|---|---|
| 1 | 🌊 [真空海洋](Module_01_Zero_Point_Energy/readme.md) · [科学](Module_01_Zero_Point_Energy/SCIENCE.md) | 空间是可汲取免费能量的高压充盈场。 | Casimir 力（理想与真实金的 Lifshitz 理论）、为何闭循环净功为零。 |
| 2 | 📉 [引力是推](Module_02_Gravity_Is_Pushing/readme.md) · [科学](Module_02_Gravity_Is_Pushing/SCIENCE.md) | 质量相互遮蔽宇宙通量。 | Monte Carlo 遮蔽给出 1/r²，以及拖垮 Le Sage 引力的拖曳、加热与饱和问题。 |
| 3 | 📻 [大脑是收音机](Module_03_The_Brain_Is_A_Radio/readme.md) · [科学](Module_03_The_Brain_Is_A_Radio/SCIENCE.md) | 心灵是大脑调谐的信号。 | 真实 EEG 信号处理、Schumann 共振，以及如何用恰当零假设检验相位锁定。 |
| 4 | 🍩 [物质是冻结的光](Module_04_Matter_Is_Frozen_Light/readme.md) · [科学](Module_04_Matter_Is_Frozen_Light/SCIENCE.md) | 粒子是绕圈奔跑的光。 | Breit–Wheeler 对产生、Schwinger 场、质子质量从何而来，以及为何「光环」电子是同义反复。 |
| 5 | 🗺️ [时间是地图](Module_05_Time_Is_A_Map/readme.md) · [科学](Module_05_Time_Is_A_Map/SCIENCE.md) | 过去与未来是可造访的坐标。 | GPS 时钟修正、同时性的相对性、Kerr 能层与 Penrose 过程。 |
| 6 | 🔊 [现实的语言](Module_06_Language_of_Reality/readme.md) · [科学](Module_06_Language_of_Reality/SCIENCE.md) | 声音塑造物质。 | Chladni 板模态、声辐射力，以及为何声音无法安置原子。 |
| 7 | 🧬 [DNA 作为天线](Module_07_DNA_Antenna/readme.md) · [科学](Module_07_DNA_Antenna/SCIENCE.md) | DNA 从场接收指令。 | 螺旋天线理论 vs DNA 真实尺寸、细胞内 Debye 屏蔽、FRET 与 DNA 动力学。 |
| 8 | ⚡ [瞬间旅行](Module_08_Instant_Travel/readme.md) · [科学](Module_08_Instant_Travel/SCIENCE.md) | 折叠空间一步跨越。 | Alcubierre 曲速度规、其负能量账单，以及量子不等式极限。 |
| 9 | ⛈️ [天气工程](Module_09_Weather_Engineering/readme.md) · [科学](Module_09_Weather_Engineering/SCIENCE.md) | 用交叉波驾驭风暴。 | Köhler 液滴活化、离子诱导成核，以及机器与风暴之间的能量鸿沟。 |
| 10 | ⏳ [时间反转疗愈](Module_10_Time_Reversal_Healing/readme.md) · [科学](Module_10_Time_Reversal_Healing/SCIENCE.md) | 时间镜撤销疾病。 | 光学相位共轭及其极限、细胞膜电压，以及生命的熵预算。 |
| 11 | ⚗️ [沉淀黄金](Module_11_Low_Energy_Transmutation/readme.md) · [科学](Module_11_Low_Energy_Transmutation/SCIENCE.md) | 共振晶格使聚变变易。 | Coulomb 势垒、Gamow 隧穿、电子屏蔽，以及 1 W 聚变会产生的中子数。 |
| 12 | 🌐 [心灵电子互联网](Module_12_The_Psychotronic_Internet/readme.md) · [科学](Module_12_The_Psychotronic_Internet/SCIENCE.md) | 心灵经真空瞬间相连。 | 海水与 Faraday 笼中的趋肤深度、为何「标量」线圈并不辐射新东西，以及真实脑机接口带宽。 |

模块彼此递进，请从模块 1 开始。健康提示：此处没有任何内容是医疗建议（见模块 10）。

---

## 贡献

最有价值的贡献是**更正**：错误数字、夸大主张、缺失限定，或更好的参考文献。模块布局与代码、引用规则见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 意图

本课程用科幻让物理问题难以抗拒，再诚实作答。故事富有想象；科学页与代码力求正确。若你发现它们不正确之处，请开 issue。
