# 🔬 模块 9 — 故事背后的科学

> [课程](readme.md)以 2420 年口吻讲述。本页是 2025 年现实核对：哪些已确立、故事主张在何处失效，以及它要成立必须满足什么。此处一切都可用[实验代码](../../../Module_09_Weather_Engineering/simulation.py)核验。

## 一句话中的 2420 主张

两束无害穿过地球的看不见「标量」（纵向）波可在天空任意处交叉，以创造瞬间热或冷口袋，这些口袋的网格以电的方式驾驭风暴与急流。

## 第 1 层 — 哪些是真的

**大气确实是电路。** 电离层相对地面约在 +250 kV。晴天这驱动微小向下电流，约 2 pA/m²，穿过弱导电空气，表面场约 100–130 V/m。全球雷暴充当保持其充电的电池。实验把这些典型值变成总量：

| 量 | 如何计算 | 实验值 |
|---|---|---|
| 总电流 | $J \times 4\pi R_\oplus^2$ | ≈ 1 kA |
| 功率 | $V_\text{ion} \times I$ | ≈ 250 MW |
| 地球表面电荷 | $\varepsilon_0 E \times 4\pi R_\oplus^2$（Gauss） | ≈ $5\times10^5$ C |
| 地面空气电导率 | $J/E$ | ≈ $2\times10^{-14}$ S/m |
| 无风暴时放电时间 | $\varepsilon_0/\sigma$ | ≈ 9 分钟 |

**电可以推动空气。** 强场中加速的离子拖着中性分子：这是「离子风」或电流体动力推力。对跨越间隙 $d$、离子迁移率为 $\mu$ 的电流 $I$，一维推力为 $T = I d/\mu$，因此每瓦推力 $T/P = d/(\mu V)$。MIT 用此原理飞行了无活动部件的 5 m 翼展飞机（Xu et al., 2018）。

**云在粒子上形成，理论精确说明何时。** 水不会在空气中所见湿度下自行凝结。它凝结在微小粒子（云凝结核）上，如海盐。Köhler 理论（1936）给出含盐质量 $m_s$、半径 $r$ 的溶液液滴上的平衡饱和比：

$$S(r) = a_w \exp\!\left(\frac{A}{r}\right) \;\approx\; 1 + \frac{A}{r} - \frac{B}{r^3}, \qquad A = \frac{2\sigma M_w}{R T \rho_w},\quad B = \frac{3\, i\, m_s M_w}{4\pi \rho_w M_s}.$$

曲率（Kelvin）项 $A/r$ 使小液滴蒸发；溶解盐（Raoult）项 $B/r^3$ 降低蒸汽压。曲线峰值在

$$r_c = \sqrt{3B/A}, \qquad S_c - 1 = \sqrt{\frac{4A^3}{27B}} \;\propto\; m_s^{-1/2}.$$

实验数值求完整表达式的峰值，并确认 $S_c - 1 \propto m_s^{-1/2}$ 与 $r_c \propto m_s^{1/2}$。对 NaCl（$i \approx 2$）给出：

| 干直径 | 临界过饱和度 | 交叉检验：用测得 κ = 1.28 的 κ‑Köhler |
|---|---|---|
| 20 nm | 1.14 % | 1.16 % |
| 50 nm | 0.29 % | 0.29 % |
| 100 nm | 0.10 % | 0.10 % |
| 200 nm | 0.036 % | 0.037 % |

峰值以下液滴是稳定的**霾**粒子。霾在远低于 100% 湿度时存在：盐晶在约 75% RH 溶解（潮解），实验从溶液水活度计算得 75.5%。仅当空气过饱和度超过 $S_c$ 时液滴无限生长并成为云滴（「活化」）。真实云很少超过约 1% 过饱和度，因此是粒子种群而非电压决定液滴在何处形成。

**离子确实帮助制造新粒子。** 电荷稳定小分子团簇。CERN CLOUD 实验（Kirkby et al., 2011）表明宇宙线电离可测地增加硫酸–氨粒子形成速率。那些粒子跨度纳米，必须生长数小时到数天才够大到播种云。

**人工降雨是真实但有限的。** 对山地上适合的冬云播撒碘化银已被直接观测到产生额外降雪（French et al., 2018）。在整季与区域尺度上效应小且难以统计证明。

**HAARP 是真实的。** 它是阿拉斯加的电离层研究设施，高频发射机功率 3.6 MW。它加热电离层小块，远高于天气（天气生活在最低 ~15 km）。对天气没有已证明效应。

**聚焦是真实的。** 放大镜制造热点因为它把大面积的光聚到小处。两束交叉波也在干涉处制造亮暗条纹。

## 第 2 层 — 主张在何处失效

**1. 空的空间中没有纵向无线电波。** 在真空中 Gauss 定律写为 $\nabla\cdot\mathbf E = 0$。对波 $\mathbf E_0 e^{i\mathbf k\cdot\mathbf x}$ 这意味着 $\mathbf k\cdot\mathbf E_0 = 0$：场必须垂直于传播方向。势的「标量」与纵向部分可由规范变换改变而不改变任何可测场，且它们不携带能量。Whittaker（1903）表明场可用两个标量函数*写出*。这是普通电磁学的数学改写，不是新波种。纵电波确实存在于等离子体内部（Langmuir 波），但它们需要等离子体存在，且不穿越岩石或海洋。

**2. 无线电波不穿过地球。** 导体在趋肤深度 $\delta \approx \sqrt{2/(\omega\mu_0\sigma)}$ 内吸收电磁波。实验使用精确公式：

| 频率 | 海水（$\sigma$ = 4 S/m） | 岩石（$\sigma$ = 10⁻³ S/m） |
|---|---|---|
| 10 Hz | 80 m | 5 km |
| 1 kHz | 8 m | 500 m |
| 1 MHz | 0.25 m | 21 m |

穿过 1000 km 岩石后，即便 10 Hz 波也只保留振幅的 $e^{-199} \approx 10^{-87}$。这就是为何用极低频与巨大天线联系潜艇，即便如此也仅在近表面。

**3. 交叉波束移动能量；它不能创造或移除能量。** 两相干波束强度 $I_1$ 与 $I_2$ 重叠处，时间平均强度为

$$I = I_1 + I_2 + 2\sqrt{I_1 I_2}\cos\Delta\phi .$$

暗条纹总与亮条纹成对，图案平均恰为 $I_1 + I_2$。实验核验两者。交叉点从空气吸热的「冷模式」将需要负强度。冷却空气意味着把热泵到别处，这需要做功并必须在附近倾倒更多热（热力学第二定律）。放大镜也不能制造冷点。

**4. 天气远比任何电杠杆强大。** 天气由阳光（地球吸收 ≈ $1.2\times10^{17}$ W）与水汽凝结释放的潜热驱动：

| 能源或汇 | 实验值 |
|---|---|
| 一场雷暴（半径 5 km 上 2 cm 雨） | ≈ $4\times10^{15}$ J |
| 平均飓风（半径 665 km 上每天 1.5 cm 雨，NOAA 方法） | ≈ $6\times10^{14}$ W |
| 仅把 100 km × 100 km 上空空气加热 1 K | ≈ $10^{17}$ J |
| 整个全球电路 | ≈ $2.5\times10^{8}$ W |
| HAARP 发射机 | $3.6\times10^{6}$ W |
| 大型地面离子阵列（100 kV × 1 mA） | 100 W |

以 100 W，1 K 加热约需 3000 万年。即便 HAARP 全部功率被低层大气吸收（并非如此），也约需 900 年。飓风功率超过离子阵列约 $6\times10^{12}$ 倍。该阵列的离子风是约 0.25 N 的推力，25 g 物体的重量，施加于含数十亿吨运动空气的天气系统。

**5. 离子不能直接造云。** Thomson 在电荷上形成液滴的理论向纯水液滴经典自由能加入静电项：

$$\Delta G(r) = -\tfrac43\pi r^3 n_l k T\ln S \;+\; 4\pi r^2\sigma \;+\; \frac{q^2}{8\pi\varepsilon_0}\left(1-\frac{1}{\varepsilon_r}\right)\left(\frac1r - \frac1{r_0}\right).$$

对 $S \le 1$ 体项为正，因此 $\Delta G$ 无最大值也无临界半径：液滴从不生长，带电与否。对 $S > 1$ 电荷降低势垒，但实验发现势垒仅在中性团簇 $S \approx 4.1$、带一个基本电荷 $S \approx 2.5$ 时降到 ~60 kT（大约每 cm³ 每秒一个液滴）。C. T. R. Wilson 1890 年代云室发现同类数字：离子仅在几百百分比过饱和度触发液滴。在现实的 $S = 1.01$ 势垒超过 $10^6$ kT。在真实空气中，盐与其他粒子在不到 1% 过饱和度活化，远早于离子起作用。（连续体理论对仅几个分子的团簇粗糙；排序而非精确数字稳健。）

**6. 地面离子器造雨。** 若干商业项目声称地面离子器阵列增强降雨。迄今发表的证据薄弱且有争议：声称效应小、无独立随机试验，且无可接受机制从额外离子在现实过饱和度下得到额外雨。

**7. 「硬如混凝土的空气墙」。** 在恒压下，把空气冷却 30 K 仅使其密度升高约 10%（$\rho \propto 1/T$）。没有任何温度变化使空气对导弹表现得像固体。

## 第 3 层 — 必须成立什么

- **新的长程场**，以可忽略损耗穿过岩石与海洋传播，不是普通电磁波，并强烈耦合空气。它也将出现在电磁学精密检验中。具有微小质量的光子会有纵向模式，但对光子质量的实验室与天体物理上限极其小（粒子数据组列出约 $10^{-18}$ eV 量级界限）。
- **匹配天气的能源**：每事件至少 $10^{15}$–$10^{17}$ J，在数小时内送达。那是 1 GW 电站运行数天到数年的全部输出，必须射入天空而不在途中加热任何东西。
- **可检验目标**：受控、随机实验，其中装置（离子器阵列、波束或其他）相对未处理对照日在降雨或气压上产生统计显著变化，并由独立组重复。那是应用于人工降雨的标准，也是其测得效应被描述为有限的原因。
- **真实科学的开放问题**：宇宙线离子对云量影响多少（CLOUD 结果表明对当今气候效应小）；全球电路如何响应变化的雷暴活动；如何使 EHD 推进更高效。

## 运行实验

```bash
python Module_09_Weather_Engineering/simulation.py
python -m pytest tests/test_module_09.py
```

| 实验 | 展示什么 |
|---|---|
| `global_circuit` | 地球晴天电路的电流、功率、电荷与电导率。 |
| `saturation_ratio`, `critical_point`, `equilibrium_radius` | Köhler 理论：100% RH 以下为霾，$S_c$ 以上活化，$S_c - 1 \propto m_s^{-1/2}$。 |
| `deliquescence_rh` | 为何盐晶在 ~75% RH 溶解（以及为何理想溶液答案过高）。 |
| `thomson_free_energy`, `nucleation_barrier`, `saturation_for_barrier` | 离子降低成核势垒，但仅在远超真实云的过饱和度。 |
| `ion_wind_thrust`, `thrust_per_power` | 离子风真实但产生微小力。 |
| `rain_latent_heat`, `hurricane_heat_power`, `column_heating_energy` | 天气能量预算 vs 每一电杠杆。 |
| `crossed_beams`, `skin_depth` | 干涉重新分配能量；无线电波在地与海中数米到数公里内消亡。 |

## 自己动手

1. 用 `critical_point` 求恰在 0.5% 过饱和度活化的干 NaCl 直径。再用 `kappa_critical_saturation` 核验答案。
2. 对 50 nm 粒子从干半径到 10 μm 画出 `saturation_ratio`。标出霾支、峰值与活化支。
3. 把 `thomson_free_energy` 中的 `eps_r` 从 80 改为 1。电荷的益处发生什么，为什么？
4. 多少座 1 GW 电站运行一天才能匹配实验雷暴的潜热？
5. 用 `skin_depth` 求波在 100 m 海水中仅损失一半振幅的频率。该频率天线需多长（取四分之一波长）？

## 参考文献

- Köhler, H., "The nucleus in and the growth of hygroscopic droplets", *Trans. Faraday Soc.* **32**, 1152 (1936).
- Petters, M. D. & Kreidenweis, S. M., "A single parameter representation of hygroscopic growth and cloud condensation nucleus activity", *Atmos. Chem. Phys.* **7**, 1961 (2007).
- Pruppacher, H. R. & Klett, J. D., *Microphysics of Clouds and Precipitation*, 2nd ed., Kluwer (1997). Köhler and Thomson theory, ion‑induced nucleation.
- Rogers, R. R. & Yau, M. K., *A Short Course in Cloud Physics*, 3rd ed., Pergamon (1989).
- Seinfeld, J. H. & Pandis, S. N., *Atmospheric Chemistry and Physics*, 3rd ed., Wiley (2016). Deliquescence and CCN activation.
- Robinson, R. A. & Stokes, R. H., *Electrolyte Solutions*, 2nd ed., Butterworths (1959). Osmotic coefficients of NaCl solutions.
- Kirkby, J. et al., "Role of sulphuric acid, ammonia and galactic cosmic rays in atmospheric aerosol nucleation", *Nature* **476**, 429 (2011).
- Rycroft, M. J., Israelsson, S. & Price, C., "The global atmospheric electric circuit, solar activity and climate change", *J. Atmos. Sol.‑Terr. Phys.* **62**, 1563 (2000).
- Xu, H. et al., "Flight of an aeroplane with solid‑state propulsion", *Nature* **563**, 532 (2018).
- French, J. R. et al., "Precipitation formation from orographic cloud seeding", *Proc. Natl. Acad. Sci. USA* **115**, 1168 (2018).
- Whittaker, E. T., "On the partial differential equations of mathematical physics", *Math. Ann.* **57**, 333 (1903).
- Jackson, J. D., *Classical Electrodynamics*, 3rd ed., Wiley (1999). Transversality of vacuum waves, skin depth.
- Kopp, G. & Lean, J. L., "A new, lower value of total solar irradiance: Evidence and climate significance", *Geophys. Res. Lett.* **38**, L01706 (2011).
- NOAA Atlantic Oceanographic and Meteorological Laboratory, Hurricane Research Division, *Hurricane FAQ* ("How much energy does a hurricane release?"). Source of the rainfall‑based heat‑release method.
