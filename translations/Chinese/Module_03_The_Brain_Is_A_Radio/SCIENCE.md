# 🔬 模块 3 — 故事背后的科学

> [课程](readme.md)以 2420 年口吻讲述。本页是 2025 年现实核对：哪些已确立、故事主张在何处失效，以及它要成立必须满足什么。此处一切都可用[实验代码](../../../Module_03_The_Brain_Is_A_Radio/simulation.py)核验。

## 一句话中的 2420 主张

大脑并不制造心灵，而是像调谐到「时间通道」广播的收音机那样接收它；光干扰该通道，两个调到同一频率的大脑共享思想。

## 第 1 层 — 哪些是真的

**大脑确实产生电节律。** Hans Berger 在 1920 年代记录了首个人类 EEG。头皮电极拾取约 10–100 µV 的电压，来自数百万同步放电的神经元。节律按常规频带划分（各实验室边界略有差异）：

| 频带 | 频率 | 通常关联 |
|---|---|---|
| delta | 0.5–4 Hz | 深睡眠 |
| theta | 4–8 Hz | 困倦、记忆任务 |
| alpha | 8–13 Hz | 放松觉醒、闭眼 |
| beta | 13–30 Hz | 积极思考、运动 |
| gamma | 30–80 Hz | 局部加工、注意 |

**「光压制信号」确有真实回声。** Berger 注意到睁眼时 alpha 节律缩小（「alpha 阻断」）。它也随脑力努力缩小，因此反映大脑在*做什么*，而非光子干扰隐藏通道。

**地球确实在嗡鸣。** 闪电（全球约每秒 50 次）敲响地面与电离层之间的腔。对半径 $R_E$ 的理想无损薄壳，模态为

$$f_n = \frac{c}{2\pi R_E}\sqrt{n(n+1)}, \qquad f_1 \approx 10.6\ \text{Hz}.$$

观测峰值约在 7.8、14.3、20.8、27.3 与 33.8 Hz，约为理想值的 75–80%，因为电离层是有损、不完美的镜子（Schumann 1952 年预言共振；Balser & Wagner 1960 年观测到）。7.83 Hz 基频恰好落在 theta/alpha 边界。

**大脑自身的场也很小。** 头外大脑磁场约 100 fT–1 pT（脑磁图 MEG）。Schumann 磁场也约 1 pT 量级。这就是为何 MEG 在磁屏蔽室中进行。

**测量节律与同步。** 实验实现标准工具：

- *Welch 功率谱* $S(f)$：对重叠加窗段的 Fourier 变换平方取平均。
- *频带功率*：$P_\text{band} = \int_{f_1}^{f_2} S(f)\,df$。对所有频率求和等于信号方差（测试核验此点）。
- *瞬时相位*：带通滤波，再取解析信号 $x(t) + i\,\mathcal{H}[x](t) = A(t)e^{i\phi(t)}$（Hilbert 变换）。
- *相位锁定值*（Lachaux et al., 1999）：$\text{PLV} = \left|\langle e^{i(\phi_1(t) - \phi_2(t))}\rangle_t\right|$，恒定相位差时为 1，无关相位时近 0。

「脑–脑同步」是超扫描研究中的真实发现，同时记录两人。但它多半因为两人同时看到、听到同样事物，而非信号在其间传递（Burgess, 2013）。

## 第 2 层 — 主张在何处失效

**1. 匹配频率不是耦合。** 7.83 Hz 的 1 pT 场在头大小回路（半径 7.5 cm）周围感应

$$\mathcal{E} = \pi r^2 \cdot 2\pi f B \approx 9\times10^{-13}\ \text{V}, \qquad E = \tfrac12 r\,\omega B \approx 2\times10^{-12}\ \text{V/m}.$$

约为 10 µV EEG 信号的 $10^{-7}$。可测量推动脑节律的经颅交流电刺激向脑内投入约 0.1–1 V/m：大约多 $10^{11}$ 倍。「调谐到 7.83 Hz」并不给出 Schumann 场能做任何事的机制。

**2. 不会失败的检验。** 「证明」脑–地共振的常见做法是把信号与完美 7.83 Hz 正弦比较。任何两个同频稳态信号都有恒定相位差，因此 PLV *由构造* 为 1。实验这样做得到 PLV = 1.000。然后提出正确问题：PLV 是否大于把两段记录滑动数秒后的值？对纯正弦，滑动不改变任何事，因此替代检验返回 p = 1：完全没有证据。

**3. 可能失败的检验。** 真实 Schumann 场不是完美正弦；闪电随机驱动它，相位游荡（品质因数 $Q \approx 4$）。实验模拟 EEG 与独立 Schumann 磁力计记录，再对 100 段合成记录做时间平移替代检验：

| 情形 | p < 0.05 的比例 |
|---|---|
| 无耦合 | ≈ 5%（校准检验应有的假阳性率） |
| 内建弱耦合（EEG 功率的 0.5%） | ≈ 93% |
| 两路 EEG 共享一个 alpha 源 | 100% |
| 两路 EEG 独立 alpha 源 | ≈ 4% |

因为检验在耦合真实存在时能检出，它的「否」才有意义。这是任何脑–Schumann 耦合主张必须通过的标准。

**4. 光子猝灭。** 没有已发表、可重复的证据表明光抑制思想，或红外相机拍摄「类 tulpoid」精神形态。颅骨内部本已几乎黑暗，人们在明亮阳光下也能完美思考。眼睛的灵敏度曲线来自视网膜光色素的吸收光谱，可直接测量。

**5. 记忆作为来自过去的现场直播。** 这是可爱的意象，但证据坚决指向相反方向：

- 特定脑结构损伤移除特定能力。患者 H.M. 在手术切除两侧海马部分后失去形成新长时记忆的能力（Scoville & Milner, 1957）。
- 在小鼠中，学习期间活跃的特定神经元可被标记并稍后用光再激活，从而触发记忆（Liu et al., 2012）。
- 记忆被*重构*且可改变：问题措辞改变人们后来报告所见（Loftus & Palmer, 1974）。来自过去的现场直播不会被问题编辑。

家庭作业中的收音机类比（「歌曲仍在空气中」）做出可检验预测：某个其他接收器应能播放你的歌。从未找到这样的接收器。

**6. 量子脑（Orch‑OR）。** Hameroff 与 Penrose 提出神经元内微管中的量子叠加在约 25 ms 时标坍缩，并与意识相关。这是真实、已发表且有争议的假说。主要异议是时序：Tegmark（2000）估计此类叠加在 $10^{-13}$ s 或更短内退相干。实验计算鸿沟：

| 神经时标 | vs Tegmark 的 $10^{-13}$ s | vs 反驳估计 $10^{-4}$ s（Hagan et al., 2002） |
|---|---|---|
| 动作电位，1 ms | $10^{10}$ | $10^{1}$ |
| gamma 周期，25 ms | $10^{11}$ | $10^{2.4}$ |

即便最有利的已发表估计也不足。Orch‑OR 也不会使大脑成为*接收器*；它仍是大脑产生心灵的理论。

## 第 3 层 — 必须成立什么

要使大脑成为 Schumann 调谐接收器，下列必须出现。每一项都是清晰实验：

- **通过替代检验的耦合。** 与本地磁力计同时记录 EEG。预注册分析应发现其间 PLV 高于时间平移替代零假设，并在独立实验室重复。
- **场移除时耦合消失。** 在磁屏蔽室内重复，使 1 pT 场降低多个数量级。若「耦合」仍在，则并非来自 Schumann 场。
- **尺度正确的机制。** 神经组织中某物需对比已知可影响它的场弱约 $10^{11}$ 倍、且高于热噪声的场作出响应。
- **对「光子猝灭」：** 可重复、盲法实验，其中某种心理现象在黑暗中出现、在光中消失，且仅改变光水平。

真实开放问题仍在。意识如何从脑活动产生（「困难问题」）未解。量子效应是否在生物学中起任何功能作用正被积极研究。Orch‑OR 所依赖的引力相关波函数坍缩正在检验；一项地下实验排除了 Diósi–Penrose 模型最简单的无参数版本（Donadi et al., 2021）。

## 运行实验

```bash
python Module_03_The_Brain_Is_A_Radio/simulation.py
python Module_03_The_Brain_Is_A_Radio/simulation.py --data my_eeg.csv --fs 160 --channels 0 1
python -m pytest tests/test_module_03.py
```

| 实验 | 展示什么 |
|---|---|
| `schumann_frequency` | 理想腔模态（10.6、18.3，… Hz）vs 观测的 7.83、14.3，… Hz。 |
| `field_budget`, `induced_emf`, `induced_e_field` | Schumann 场在头外与大脑自身同量级，但在其内感应约 10⁻¹² V/m。 |
| `pink_noise`, `synthetic_eeg_pair`, `schumann_record` | 合成 EEG（1/f 背景加 alpha 爆发）与游荡相位的 Schumann 迹。 |
| `welch_psd`, `band_power`, `spectral_slope` | 标准 EEG 频谱分析。 |
| `plv`, `shift_surrogate_test`, `detection_rate` | 相位锁定、正弦对正弦陷阱，以及具有测得假阳性率与功效的校准检验。 |
| `decoherence_gap` | Orch‑OR 时序问题的数量级。 |
| `load_user_eeg` | 可选：你自己的记录为 `.csv` 或 `.npy`（样本 × 通道）。不使用网络。 |

## 自己动手

1. 真实数据：下载 PhysioNet EEG Motor Movement/Imagery 数据集的若干次运行（109 名志愿者，64 通道，160 Hz，EDF 格式）。把两通道转为 CSV（例如用 MNE‑Python 库）并用 `--data` 运行实验。比较睁眼与闭眼基线：alpha 功率是否如 Berger 所见变化？
2. 用你自己的数据，计算两*相邻*电极与两*远处*电极之间的 PLV。为何邻居几乎总是「显著锁定」？（提示：容积传导，一个源到达两个电极。）
3. 实现相位随机化替代（保留一通道的 Fourier 振幅，随机化其相位），并用它对抗完美 7.83 Hz 正弦参考。说明它同样无法区分稳态 7.83 Hz 节律与真实夹带。参考的何种性质使每种替代方法失败？
4. 降低 `COUPLING_DEMO` 直至 `detection_rate` 落到约 50%。若把记录长度加倍，该功效如何变化？
5. 用 `induced_e_field` 求在头内感应 0.1 V/m 所需的 7.83 Hz 磁场。与 MRI 扫描仪的场（数特斯拉，但是静场）相比如何？

## 参考文献

- Berger, H., "Über das Elektrenkephalogramm des Menschen", *Archiv für Psychiatrie und Nervenkrankheiten* **87**, 527 (1929).
- Schumann, W. O., "Über die strahlungslosen Eigenschwingungen einer leitenden Kugel, die von einer Luftschicht und einer Ionosphärenhülle umgeben ist", *Z. Naturforsch. A* **7**, 149 (1952).
- Balser, M. & Wagner, C. A., "Observations of Earth–ionosphere cavity resonances", *Nature* **188**, 638 (1960).
- Nickolaenko, A. P. & Hayakawa, M., *Resonances in the Earth–Ionosphere Cavity*, Kluwer (2002).
- Hämäläinen, M., Hari, R., Ilmoniemi, R. J., Knuutila, J. & Lounasmaa, O. V., "Magnetoencephalography — theory, instrumentation, and applications to noninvasive studies of the working human brain", *Rev. Mod. Phys.* **65**, 413 (1993).
- Lachaux, J.‑P., Rodriguez, E., Martinerie, J. & Varela, F. J., "Measuring phase synchrony in brain signals", *Hum. Brain Mapp.* **8**, 194 (1999).
- Theiler, J., Eubank, S., Longtin, A., Galdrikian, B. & Farmer, J. D., "Testing for nonlinearity in time series: the method of surrogate data", *Physica D* **58**, 77 (1992).
- Burgess, A. P., "On the interpretation of synchronization in EEG hyperscanning studies: a cautionary note", *Front. Hum. Neurosci.* **7**, 881 (2013).
- Schalk, G., McFarland, D. J., Hinterberger, T., Birbaumer, N. & Wolpaw, J. R., "BCI2000: a general‑purpose brain‑computer interface (BCI) system", *IEEE Trans. Biomed. Eng.* **51**(6), 1034 (2004). Source of the PhysioNet EEG Motor Movement/Imagery dataset.
- Goldberger, A. L. et al., "PhysioBank, PhysioToolkit, and PhysioNet", *Circulation* **101**(23), e215 (2000).
- Scoville, W. B. & Milner, B., "Loss of recent memory after bilateral hippocampal lesions", *J. Neurol. Neurosurg. Psychiatry* **20**, 11 (1957).
- Liu, X. et al., "Optogenetic stimulation of a hippocampal engram activates fear memory recall", *Nature* **484**, 381 (2012).
- Loftus, E. F. & Palmer, J. C., "Reconstruction of automobile destruction: an example of the interaction between language and memory", *J. Verbal Learn. Verbal Behav.* **13**, 585 (1974).
- Hameroff, S. & Penrose, R., "Orchestrated reduction of quantum coherence in brain microtubules: a model for consciousness", *Math. Comput. Simul.* **40**, 453 (1996).
- Hameroff, S. & Penrose, R., "Consciousness in the universe: a review of the 'Orch OR' theory", *Phys. Life Rev.* **11**, 39 (2014).
- Tegmark, M., "Importance of quantum decoherence in brain processes", *Phys. Rev. E* **61**, 4194 (2000).
- Hagan, S., Hameroff, S. R. & Tuszyński, J. A., "Quantum computation in brain microtubules: decoherence and biological feasibility", *Phys. Rev. E* **65**, 061901 (2002).
- Donadi, S. et al., "Underground test of gravity‑related wave function collapse", *Nat. Phys.* **17**, 74 (2021).
