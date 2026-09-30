# 🔬 模块 12 — 故事背后的科学

> [课程](readme.md)以 2420 年口吻讲述。本页是 2025 年现实核对：哪些已确立、故事主张在何处失效，以及它要成立必须满足什么。此处一切都可用[实验代码](../../../Module_12_The_Psychotronic_Internet/simulation.py)核验。

## 一句话中的 2420 主张

人类心灵可通过由「心灵电子网格」放大的行星级「Noosphere」直接相连，无需手机或电线，因而问题被瞬间回答，技能可在数秒内下载。

## 第 1 层 — 哪些是真的

**大脑是电的，其场可被测量。** 神经元产生电流，其场可在头外记录：EEG（头皮上微伏）与 MEG（距源数厘米处传感器约 100 fT 到 1 pT 的磁场，约为地磁场的 $10^{-8}$）。

**脑机接口是真实的。** 植入电极阵列（例如 BrainGate 试验）让瘫痪者控制光标、机器臂与文本。Willett 等人（2021）以约每分钟 90 字符解码想象书写，后来工作以约每分钟 62 词解码尝试言语（Willett et al., 2023）。这些是从置于脑内或脑上的电极读取信号的医疗装置；它们不通过空气到达他人大脑。

**导体屏蔽场。** 进入导体的变化场在趋肤深度上衰减

$$\delta = \sqrt{\frac{2}{\mu\sigma\omega}} \;\propto\; f^{-1/2}.$$

在海水中（$\sigma \approx 4$ S/m），美国海军 ELF 潜艇发射机频率 76 Hz 时 $\delta = 29$ m，3 kHz 时 4.6 m，1 MHz 时 0.25 m。在 2.4 GHz，水的位移电流大于传导电流（$\omega\varepsilon/\sigma \approx 2.7$），因此需要一般公式并给出约 1 cm。在铜中，50 Hz 时 $\delta = 9.2$ mm，1 MHz 时 65 µm：1 mm 铜片在 1 MHz 吸收约 133 dB。这就是为何 Faraday 笼有效。

**静场也被屏蔽。** 在导体中，电荷移动直到内部场为零。对均匀场 $E_0$ 中的导电球，感应表面电荷为 $\sigma_s = 3\varepsilon_0E_0\cos\theta$。实验不假设答案：它对该表面电荷数值累加 Coulomb 定律，发现内部总场低于 $10^{-4}E_0$，而外部匹配教科书偶极解。

**势是真实的，且以精确方式重要。** Whittaker 在 1903–1904 年表明波动方程的解以及电磁场本身可用标量函数写出。那是正确数学，但它描述*同一*场 $\mathbf E$ 与 $\mathbf B$，不是新波种。势有直接可观测效应的一处是 Aharonov–Bohm 效应（1959）：绕磁通量 $\Phi$ 区域经过的电子获得相位

$$\Delta\varphi = \frac{e\Phi}{\hbar} = 2\pi\,\frac{\Phi}{h/e},\qquad h/e = 4.14\times10^{-15}\ \text{Wb},$$

即便其路径上磁场为零。Tonomura 等人（1986）在场被完全封闭于超导屏蔽中时确认了它。效应仅依赖闭环周围的封闭通量，并遵循标准量子电动力学。

**人类通信速率可测量。** 跨 17 种语言，言语约携带每秒 39 比特（Coupé et al., 2019）。书面英语在计入冗余后约每字符 1 比特（Shannon, 1951）。

## 第 2 层 — 主张在何处失效

**1. 没有任何东西比光更快携带信息。** 「叮！答案瞬间弹入你的心灵」在真实距离上不可能：

| 链路 | 单向光延迟 |
|---|---|
| 地球–月球 | 1.28 s |
| 地球–火星（最近到最远） | 3.0 到 22.3 分钟 |
| Proxima Centauri | 4.25 年 |

「火星首都」问题最早在往返 6 到 45 分钟后得到答案。

**2. 纠缠不能发送消息。** 对纠缠对，实验计算 Alice 沿任意轴测量后 Bob 的局域态，发现它总是精确 $\tfrac12\mathbb 1$（差低于 $10^{-15}$），与她什么都不做相同。关联是真实的（结果以概率 $\cos^2(\Delta\theta/2)$ 一致），但它们仅在两记录经普通信道比较时出现。这是无通信定理。

**3. 脑场远太弱，无法到达任何人。** 偶极场按 $1/r^3$ 下降。在距源约 4 cm 测得的 1 pT 脑信号在 1 m 处约 $6\times10^{-17}$ T，在 1 km 处约 $6\times10^{-26}$ T，比地磁场弱超过 $10^{20}$ 倍。最好的磁力计需要屏蔽室与头皮上的传感器。

**4. 「标量」线圈不辐射任何新东西。** 反绕（双线）线圈驱动两反向电流使场抵消。实验计算近处剩余与远处辐射：

- 在轴上，单环场按 $z^{-3.00}$ 下降；反绕对的剩余按 $z^{-4.00}$ 下降：普通更高多极。
- 远处，线圈靠近（$kd \ll 1$）时对辐射单线圈功率的 $(kd)^2/5$。对 $d = 0$ 辐射精确为零。不出现额外「标量」波，若势也抵消，则没有留下可产生 Aharonov–Bohm 或其他效应的东西。

**5. 屏蔽。** 若心灵电子信号是电磁的，金属房间、潜艇或数米海水将切断它，如上趋肤深度所示。若它不是电磁的，故事需要自然的新力，没有任何实验见过。

**6. 带宽。** 1 MB 飞行手册以言语速度传输约需 57 小时。在 5 s 内下载它需要 $1.6\times10^6$ bit/s，约为言语速率的 40,000 倍。当今真实 BCI 以每秒数比特运行。我们也不知道如何把技能或记忆写入大脑：那将要求精确改变巨大数量神经元上的突触。

**7. Noosphere 是哲学，不是物理。** Vernadsky 与 Teilhard de Chardin 用「noosphere」表示人类思想的增长球层及其对行星的影响。那是关于社会与进化的深思想法，不是大气的测得层。蜜蜂确实通信，但通过物理信号：摇摆舞、信息素与振动。

## 第 3 层 — 必须成立什么

要使心灵电子互联网存在，下列全部必须被展示。每一项都可检验：

- **从脑到脑到达的载体。** 检验：发送者与接收者在分开的 Faraday 屏蔽室中，随机目标消息，盲法评分与预注册分析，由独立实验室重复。
- **绕过光速的方式**，那也将推翻相对论与因果律。检验：在光本可携带之前到达的消息。
- **记忆与技能的读写接口**：充分理解技能如何储存在突触中，足以将其写入不同大脑。

**接近故事的真实开放问题：** BCI 能多快、多安全，能否无需手术？非侵入方法（EEG、MEG、光泵磁力计、功能超声）能读取多少脑信息？「神经数据」的隐私与伦理规则是什么？

## 运行实验

```bash
python Module_12_The_Psychotronic_Internet/simulation.py
python -m pytest tests/test_module_12.py
```

| 实验 | 展示什么 |
|---|---|
| `skin_depth`, `attenuation_length`, `shield_absorption_db` | 海水与金属阻挡变化场；$\delta \propto f^{-1/2}$。 |
| `conducting_sphere_field` | 对感应电荷累加 Coulomb 定律给出导体内零场。 |
| `antiparallel_pair_power`, `counterwound_axis_field` | 反向电流留下普通、更快衰减的多极，不是新波。 |
| `aharonov_bohm_phase` | 势的真实、已测量效应。 |
| `light_delay`, `bob_state`, `same_outcome_probability` | 光速延迟；纠缠关联但不能发信号。 |
| `brain_field`, `bci_bits_per_second`, `transfer_time` | 脑场多弱以及人类数据速率多慢。 |

## 自己动手

1. 求海水趋肤深度为 100 m 的频率。为何海军潜艇无线电每分钟仅发送几个字符？
2. 在 `bob_state` 中把 Bell 态替换为 $(\lvert00\rangle + \lvert11\rangle)$ 加小的 $\lvert01\rangle$ 混合（归一化它）。Alice 对角度的选择现在是否改变 Bob 的态？
3. 用 `antiparallel_pair_power`，两反向 1 kHz 线圈必须相距多远（以 km）才能辐射与单线圈一样多？
4. 查阅阅读的信息速率。以该速率读完互联网上一切需要多久？

## 参考文献

- Whittaker, E. T., "On the partial differential equations of mathematical physics", *Math. Ann.* **57**, 333 (1903).
- Whittaker, E. T., "On an expression of the electromagnetic field due to electrons by means of two scalar potential functions", *Proc. London Math. Soc.* **s2‑1**, 367 (1904).
- Aharonov, Y. & Bohm, D., "Significance of electromagnetic potentials in the quantum theory", *Phys. Rev.* **115**, 485 (1959).
- Tonomura, A. et al., "Evidence for Aharonov‑Bohm effect with magnetic field completely shielded from electron wave", *Phys. Rev. Lett.* **56**, 792 (1986).
- Ghirardi, G. C., Rimini, A. & Weber, T., "A general argument against superluminal transmission through the quantum mechanical measurement process", *Lett. Nuovo Cimento* **27**, 293 (1980).
- Nielsen, M. A. & Chuang, I. L., *Quantum Computation and Quantum Information*, Cambridge University Press (2000).
- Hämäläinen, M. et al., "Magnetoencephalography—theory, instrumentation, and applications to noninvasive studies of the working human brain", *Rev. Mod. Phys.* **65**, 413 (1993).
- Willett, F. R. et al., "High‑performance brain‑to‑text communication via handwriting", *Nature* **593**, 249 (2021).
- Willett, F. R. et al., "A high‑performance speech neuroprosthesis", *Nature* **620**, 1031 (2023).
- Coupé, C., Oh, Y. M., Dediu, D. & Pellegrino, F., "Different languages, similar encoding efficiency: Comparable information rates across the human communicative niche", *Science Advances* **5**, eaaw2594 (2019).
- Shannon, C. E., "Prediction and entropy of printed English", *Bell Syst. Tech. J.* **30**, 50 (1951).
- Vernadsky, V. I., "The biosphere and the noosphere", *American Scientist* **33**, 1 (1945).
- Teilhard de Chardin, P., *The Phenomenon of Man* (1955; English translation 1959).
