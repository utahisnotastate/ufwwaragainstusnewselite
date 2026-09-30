# 🔬 モジュール6 — 物語の背後にある科学

> [レッスン](readme.md) は2420年の視点で語られます。このページは2025年の現実チェックです：何が確立されているか、物語の主張がどこで破綻するか、それが成り立つには何が真でなければならないか。ここにあるすべては [実験室コード](../../../Module_06_Language_of_Reality/simulation.py) で確認できます。

## 2420年の主張を一文で

自然のすべての形は「凍った音」である：バイオリンの弓が板上の砂を並べるように定在波が物質を並べるので、正しい音は物質を築き、溶かし、石を無重量にできる。

## レベル1 — 実在すること

**Chladni 図形は実在し、美しい物理学である。** Ernst Chladni（1787）は砂を載せた金属板を弓で弾き、砂が**節線** — 板が動かないところ — に集まることを見つけた。各音が異なる図形を与える。図形を決めるのは板の運動方程式である。

**太鼓の皮と板は異なる方程式に従う。** 張った膜（太鼓の皮）は波動（Helmholtz）方程式 $\nabla^2 w + k^2 w = 0$ に従う。辺長 $L$ の固定縁正方形膜の周波数は

$$f_{mn} = \frac{c}{2L}\sqrt{m^2+n^2}.$$

Chladni 板は薄く剛い**板**で、Kirchhoff の二重調和方程式

$$D\,\nabla^4 w - \rho h\,\omega^2 w = 0, \qquad D = \frac{E h^3}{12(1-\nu^2)}$$

に支配される。単純支持正方形板の厳密解は $\omega_{mn} = \sqrt{D/\rho h}\;\pi^2 (m^2+n^2)/L^2$ なので $f_{mn} \propto m^2 + n^2$ であり、$\sqrt{m^2+n^2}$ **ではない**。これは実在の検証可能な教訓：太鼓では (1,2) モードは基本波の $\sqrt{5/2} = 1.58$ 倍、板上では $5/2 = 2.5$ 倍。実験室は両方程式を数値的に解き（5点 Helmholtz ステンシルと13点二重調和ステンシル）、厳密結果と 0.5 % より良く一致し、期待どおり二次収束する。

2モードが同じ周波数をもつとき（例：正方形の (1,2) と (2,1)）、板は混合 $\sin m\pi x\,\sin n\pi y \pm \sin n\pi x\,\sin m\pi y$ で振動する。これらの混合が実 Chladni 図形の対角・環・星を生み、実験室は「−」混合が対角にちょうど節線をもつことを確認する。Chladni 自身の自由縁板は解くのが難しい（Leissa 1969 が古典結果を集める）。円板について **Chladni の法則** $f \approx C\,(m + 2n)^p$（$m$ 節直径、$n$ 節円、$p \approx 2$ が平板）は良い経験則である（Rossing 1982）。

**音は本当に小さな物体を押し、捕らえ、浮かせる。** 波長よりはるかに小さい粒子に定在波は定常**音響放射力**を及ぼす。Gor'kov（1962）はそれがポテンシャルから来ることを示した：

$$U = 2\pi R^3\left[\frac{f_1\,\langle p^2\rangle}{3\rho_0 c_0^2} - \frac{f_2\,\rho_0\langle v^2\rangle}{2}\right], \qquad \mathbf F = -\nabla U,$$

$$f_1 = 1 - \frac{\kappa_p}{\kappa_0}, \qquad f_2 = \frac{2(\rho_p-\rho_0)}{2\rho_p+\rho_0} .$$

$\mathbf F = -\nabla U$ なのでこの力は**保存力**である（このモジュールの初期草稿は非保存と呼び誤りだった）：閉経路で正味仕事はなく、粒子は $U$ の極小に落ち着く。1D 定在波 $p = p_0\cos kx\cos\omega t$ では $F = 4\pi\Phi\,kR^3 E_\text{ac}\sin 2kx$、コントラスト因子 $\Phi = f_1/3 + f_2/2$、エネルギー密度 $E_\text{ac} = p_0^2/4\rho_0 c_0^2$（Bruus 2012）。実験室は $U$ の数値勾配をこの式に対して確認し、波長にわたる正味仕事零を示し、粒子を漂わせる：

- 水中のポリスチレン（$\Phi = +0.22$）は**圧力節**に集まり、
- 水中の脂質滴（$\Phi = -0.07$）は**圧力腹**に集まる。

これが音響流体細胞選別機と**音響浮揚器**の原理である。Marzo et al.（2015）は 40 kHz 変換器アレイからホログラフィック音響ピンセットを作り、空気中でミリメートルビーズを浮かせ動かした。実験室は必要圧力を見積もる：フォームビーズで約 280 Pa（140 dB）、固体ポリスチレンで約 1.8 kPa（156 dB）。ビーズが 8.6 mm 波長より十分小さければサイズに依存しない。

**雪の結晶が六角形なのは実在の理由によるが、音ではない。** 普通の氷（ice Ih）は水分子間の水素結合の幾何による六方格子をもつ。雪結晶の六回対称はその格子と蒸気の拡散の仕方から来る（Libbrecht 2005）。

## レベル2 — 主張が破綻するところ

**1. パターン尺度は波長である。** 音が物質を組織できるのは半波長の尺度まで：空気中 40 kHz で 4.3 mm。個々の原子（~0.1 nm）を置くには 0.2 nm 波長が要る。実験室はそれが不可能な理由を示す：

| 媒質 | 必要な周波数 | 限界 |
|---|---|---|
| 固体（$c \approx 5$ km/s） | ~25 THz | シリコンの最高振動は 15.6 THz、格子が運べる最短波は原子間隔の2倍、0.47 nm。 |
| 空気 | ~$1.7\times10^{12}$ Hz | 分子平均自由行程（~66 nm）以下で音は存在せず、約 5 GHz で頭打ち。 |

原子尺度で「音」（フォノン）は原子自身の揺れである。それらを置くテンプレートにはなれない。

**2. 振動は結合の上に乗り、結合を作らない。** シリコンの最高フォノンは 65 meV。結晶から原子1個を除くコストは 4.63 eV、約70倍。物質をまとめているのは電子の量子力学（化学結合）であり、持続する音ではない。

**3. 大きな石を歌で空に上げられない。** Gor'kov 式は波長よりはるかに小さい物体にしか適用されない。2 m のブロックには波長が数十メートル（約 17 Hz）要る。その周波数で花崗岩を支えるには圧力振幅 1.4 気圧：各周期の低圧半分が**真空以下**に落ちなければならず、空気にはできない。音響学で物体が「重いことを忘れる」ことはない。位相共役、または「時間反転音響」は実在する（Fink 1997）が、波を源に再集束する。重さを打ち消さない。

**4. 理論の名前は持たない。** 「Formon 理論」（Bearden）は物理学で**認知された理論ではない**：査読付き定式化も実験的支持もない。「時空を押すスカラー音」に物理学の対応物はない。縦波はただの普通の音（空気中の音はすべて縦）で、時空ではなく物質を押す。Hans Jenny の *Cymatics*（1967）は振動パターンの美しい写真記録だが、物質が「凍った音」であることを示さない。

## レベル3 — 何が真でなければならないか

「音で物質を築く」が比喩以上になるには、次がすべて必要：

- **配置する原子でできていない原子尺度波長の波。** 光と電子ビームはこれほど短い波長をもつ。だから光ピンセット、電子顕微鏡、走査プローブ「原子書き込み」が働き、音ではなく電磁気を通じて行う。
- **結合エネルギー（eV）に匹敵する量子あたりエネルギー。** そうでなければ波は直接結合を作ったり壊したりできない。音波量子は数十 meV が上限。
- **定量的予言。** 例えば結晶構造や石の重さを測定可能に変える特定周波数を研究室が試験できること。公表されていない。

本物の開かれた前線はより控えめでなお興奮する：多数粒子を一度に組む音響ホログラム、細胞・組織の音響操作、音と熱を操るよう設計されたフォノニック結晶。

## 実験室を実行

```bash
python Module_06_Language_of_Reality/simulation.py
python -m pytest tests/test_module_06.py
```

| 実験 | 示すこと |
|---|---|
| `membrane_frequencies`, `membrane_modes_fd` | 太鼓の皮：$f \propto \sqrt{m^2+n^2}$、有限差分で確認。 |
| `plate_frequencies`, `plate_modes_fd`, `biharmonic_simply_supported` | 板：$f \propto m^2+n^2$、13点二重調和で確認。 |
| `chladni_pattern` | 縮退モード混合とその節線（砂が集まるところ）。 |
| `gorkov_potential_1d`, `gorkov_force_1d`, `settle_positions` | 保存的放射力；正コントラストは節、負は腹へ。 |
| `levitation_pressure`, `spl_db` | 140–156 dB がビーズを浮かせる；石は「真空以下」圧力が要る。 |
| `atom_scale_sound`, `mean_free_path_air` | なぜ音が原子を配置できないか。 |

## 自分で試す

1. `biharmonic_simply_supported` でゴーストノード符号を $-1$ から $+1$ に変える。縁が「単純支持」から「固定」になる。$f_{21}/f_{11}$ はどうなるか？（固定板は実在の鐘やシンバルに近い。）
2. `chladni_pattern(1, 3, sign=+1)` と `sign=-1` を画像として描き（任意の描画ツール）、$|w|$ が小さいところを印せ。どちらが見たことのある Chladni 図形に近いか？
3. `levitation_pressure` で 150 dB で 1 mm 水滴を浮かせられる周波数を求めよ。滴はなお波長よりはるかに小さいか？
4. 音速約 18 km/s、最高フォノン約 1332 cm⁻¹ のダイヤモンドで `atom_scale_sound` を繰り返せ。「原子を置く」に近づくか？
5. 血漿中の赤血球の $\Phi$ を計算（近似密度と音速を調べよ）。節か腹か？

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
