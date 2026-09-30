# 2420年代の「失われた」カリキュラム — 人間のための自明な物理学

[![tests](https://github.com/utahisnotastate/ufwwaragainstusnewselite/actions/workflows/tests.yml/badge.svg)](https://github.com/utahisnotastate/ufwwaragainstusnewselite/actions/workflows/tests.yml)

☕ このプロジェクトを支援する：[ko-fi.com/utah23](https://ko-fi.com/utah23) · なぜ作ったか：[ABOUT.md](ABOUT.md)

12の大きなアイデアを、それぞれ3つの層で教えます：

| 層 | ファイル | 内容 |
|---|---|---|
| 📖 **物語** | `readme.md` | 2420年の学校から届いたかのように書かれたレッスン。聡明な8歳児と好奇心旺盛な大人向け。実在の問いを軸にしたサイエンスフィクション。 |
| 🔬 **科学** | `SCIENCE.md` | 2025年の現実チェック：何が確立されているか、物語の主張がどこで破綻するか（数値つき）、それが成り立つには何が真でなければならないか。実在の文献つき。 |
| 🧪 **実験室** | `simulation.py` | 科学ページのすべての数値を計算する実行可能な Python。教科書の極限と公表された測定値に対してテスト済み。 |

各モジュールには作中文書の `PHYSICS_PROOF.md` も残っています：2420年アーカイブ自身の論証で、物語の一部として明確にラベル付けされています。

**なぜこの形式か？** 物語が引き込みます。子どもが本当に聞く問いを投げかけます：*宇宙は本当に空っぽ？ 重力はなぜ引く？ 瞬間移動はできる？* 科学ページは正直に答えます。「いいえ、そしてそれを示す計算はこれです」も含めて。美しいアイデアがどこで壊れるかを学ぶことは、「うまくいく」と教えられることより多くの物理学を教えます。

---

## クイックスタート

```bash
python -m pip install -r requirements.txt
python Module_02_Gravity_Is_Pushing/simulation.py   # 1つの実験室を実行
python -m pytest                                    # すべての実験室を確認
```

Python 3.10以上、NumPy と SciPy が必要です。描画ライブラリやインターネット接続は不要です。コマンドはリポジトリのルートから実行してください（実験室のコードは英語モジュール側にあります）。

---

## モジュール索引

| # | モジュール | 2420年の物語が言うこと… | 実験室が計算すること |
|---|---|---|---|
| 1 | 🌊 [真空の海](Module_01_Zero_Point_Energy/readme.md) · [科学](Module_01_Zero_Point_Energy/SCIENCE.md) | 空間は無料エネルギーを取り出せる高圧プレナムである。 | Casimir 力（理想と実在の金の Lifshitz 理論）、閉サイクルの正味仕事が零になる理由。 |
| 2 | 📉 [重力は押している](Module_02_Gravity_Is_Pushing/readme.md) · [科学](Module_02_Gravity_Is_Pushing/SCIENCE.md) | 質量は宇宙的フラックスから互いに影を落とす。 | Monte Carlo 遮蔽が 1/r² を与え、次いで Le Sage 重力を沈めた抗力・加熱・飽和の問題。 |
| 3 | 📻 [脳はラジオである](Module_03_The_Brain_Is_A_Radio/readme.md) · [科学](Module_03_The_Brain_Is_A_Radio/SCIENCE.md) | 心は脳が同調する信号である。 | 実在の EEG 信号処理、Schumann 共鳴、適切な帰無に対する位相同期の検定。 |
| 4 | 🍩 [物質は凍った光である](Module_04_Matter_Is_Frozen_Light/readme.md) · [科学](Module_04_Matter_Is_Frozen_Light/SCIENCE.md) | 粒子は円を走る光である。 | Breit–Wheeler 対生成、Schwinger 場、陽子質量の由来、「光のループ」電子がトートロジーである理由。 |
| 5 | 🗺️ [時間は地図である](Module_05_Time_Is_A_Map/readme.md) · [科学](Module_05_Time_Is_A_Map/SCIENCE.md) | 過去と未来は訪れることのできる座標である。 | GPS 時計補正、同時性の相対性、Kerr エルゴ球と Penrose 過程。 |
| 6 | 🔊 [現実の言語](Module_06_Language_of_Reality/readme.md) · [科学](Module_06_Language_of_Reality/SCIENCE.md) | 音が物質を形作る。 | Chladni 板のモード、音響放射力、音が原子を配置できない理由。 |
| 7 | 🧬 [DNAはアンテナである](Module_07_DNA_Antenna/readme.md) · [科学](Module_07_DNA_Antenna/SCIENCE.md) | DNA は場から指示を受け取る。 | ヘリカルアンテナ理論と DNA の実サイズ、細胞内の Debye 遮蔽、FRET と DNA ダイナミクス。 |
| 8 | ⚡ [瞬間移動](Module_08_Instant_Travel/readme.md) · [科学](Module_08_Instant_Travel/SCIENCE.md) | 空間を折りたたんで一歩で渡る。 | Alcubierre ワープ計量、負エネルギーの請求書、量子不等式の限界。 |
| 9 | ⛈️ [天候工学](Module_09_Weather_Engineering/readme.md) · [科学](Module_09_Weather_Engineering/SCIENCE.md) | 交差した波で嵐を操る。 | Köhler 液滴活性化、イオン誘起核生成、機械と嵐のエネルギーギャップ。 |
| 10 | ⏳ [時間反転ヒーリング](Module_10_Time_Reversal_Healing/readme.md) · [科学](Module_10_Time_Reversal_Healing/SCIENCE.md) | 時間鏡が病気を取り消す。 | 光学的位相共役とその限界、細胞膜電位、生命のエントロピー収支。 |
| 11 | ⚗️ [金の析出](Module_11_Low_Energy_Transmutation/readme.md) · [科学](Module_11_Low_Energy_Transmutation/SCIENCE.md) | 共鳴格子が核融合を容易にする。 | Coulomb 障壁、Gamow トンネル、電子遮蔽、1 W の核融合が出す中性子数。 |
| 12 | 🌐 [サイコトロニック・インターネット](Module_12_The_Psychotronic_Internet/readme.md) · [科学](Module_12_The_Psychotronic_Internet/SCIENCE.md) | 心は真空を通じて瞬時に結びつく。 | 海水と Faraday ケージの表皮深さ、「スカラー」コイルが新しいものを放射しない理由、実在の脳–コンピュータ・インターフェース帯域。 |

モジュールは互いに積み上がるので、モジュール1から始めてください。健康に関する注意：ここにあるものは医療アドバイスではありません（モジュール10を参照）。

---

## 翻訳

エストニア語、フィンランド語、ロシア語、日本語、中国語（簡体字）の**物語**版は [`translations/`](../README.md) にあります。科学ページと実験室が追加される前に作られたものもあり、まだ含まれていない言語もあります。この日本語フォルダは科学ページまで揃えています。実験室の Python は英語モジュール側を実行してください。

---

## 貢献

最も価値ある貢献は**訂正**です：誤った数値、欠けた注意書き、より良い文献。モジュール構成とコード・引用の規則は [CONTRIBUTING.md](CONTRIBUTING.md) を参照してください。

## 意図

このカリキュラムは、サイエンスフィクションで物理学の問いを抗いがたいものにし、それから正直に答えます。物語は想像的です。科学ページとコードは正確であることを目指します。そうでない箇所を見つけたら、issue を開いてください。
