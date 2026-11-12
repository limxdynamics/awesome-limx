<p align="center"><img src="assets/banner_ja.png" alt="Awesome LimX" width="100%"></p>

<p align="center">
  <a href="README.md">English</a> | <a href="README_cn.md">中文</a> | <b>日本語</b> | <a href="README_ko.md">한국어</a>
</p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-CC0--1.0-2f6feb" alt="License: CC0-1.0"></a>
  <a href="https://github.com/limxdynamics/limxdynamics/blob/main/doc/wechat_qr.png"><img src="https://img.shields.io/badge/WeChat-Developer%20Community-07C160?logo=wechat&logoColor=white" alt="WeChat Community"></a>
</p>

> LimX のロボットと LimX SDK にまつわる **157** プロジェクト・提携を収録しています。うち **104** 件はオープンソースコードあり。論文、コード、データセット、チュートリアル、競技会の結果、産業応用を扱います。LimX 公式のオープンソースは [GitHub](https://github.com/limxdynamics) と [Hugging Face](https://huggingface.co/limxdynamics) をご覧ください。

**機種から探す**

| [**TRON1**](robots/TRON1_ja.md) | [**TRON2**](robots/TRON2_ja.md) | [**Oli**](robots/Oli_ja.md) | [**Luna**](robots/Luna_ja.md) | [**P1**](robots/P1_ja.md) | [**W1**](robots/W1_ja.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 90&nbsp;件 | 34&nbsp;件 | 27&nbsp;件 | 7&nbsp;件 | 5&nbsp;件 | 4&nbsp;件 |

## 目次

- [はじめる前に](#はじめる前に)
- [移動と全身制御](#移動と全身制御) — 50
  - [地形と知覚ロコモーション](#地形と知覚ロコモーション)
  - [強化学習の訓練と実機転移](#強化学習の訓練と実機転移)
  - [モデルベース制御](#モデルベース制御)
  - [モーショントラッキングとリターゲティング](#モーショントラッキングとリターゲティング)
- [知覚とナビゲーション](#知覚とナビゲーション) — 13
- [マニピュレーション](#マニピュレーション) — 11
- [エンボディドAI](#エンボディドai) — 9
- [ツール、シミュレーション、SDK](#ツールシミュレーションsdk) — 22
  - [学習フレームワーク](#学習フレームワーク)
  - [シミュレーションと環境](#シミュレーションと環境)
  - [デプロイと制御](#デプロイと制御)
  - [モデルとモーションデータ](#モデルとモーションデータ)
- [教育と競技会](#教育と競技会) — 18
- [産業応用](#産業応用) — 34
  - [導入事例と製品](#導入事例と製品)
  - [企業のオープンソース](#企業のオープンソース)
  - [商業公演とイベント](#商業公演とイベント)
  - [戦略提携](#戦略提携)
  - [地域パートナーと販売チャネル](#地域パートナーと販売チャネル)
  - [受賞と評価](#受賞と評価)
- [機種別](#機種別)
- [コントリビュート](#コントリビュート)

<sub>**コード** すぐ動かせる · **チュートリアル** 手順に沿って学べる · **論文** 読むもの · **報道** メディア報道や発表 · *sim* シミュレーションでのみ示された成果、それ以外は実機で動作 · **—** 特定の機種に限らない</sub>

## はじめる前に

以下の成果はすべて同じ 4 ステップの上に成り立っています。初めての方は順番に進めてください。ここに挙げたのは LimX 公式のリポジトリで、コミュニティのプロジェクトではありません。

| ステップ | 必要なもの | 入手先 |
|---|---|---|
| 1 · モデル | ロボットの URDF、MJCF、USD | [TRON1](https://github.com/limxdynamics/tron1-robot-description) · [TRON2](https://github.com/limxdynamics/tron2-robot-description) · [Oli](https://github.com/limxdynamics/humanoid-description) · [Luna](https://github.com/limxdynamics/luna-description) |
| 2 · インターフェース | 低レベル運動 SDK、ROS 2 | [limxsdk-lowlevel](https://github.com/limxdynamics/limxsdk-lowlevel) |
| 3 · 学習 | Isaac Lab、Isaac Gym、MuJoCo | [TRON1](https://github.com/limxdynamics/tron1-rl-isaaclab) · [TRON2](https://github.com/limxdynamics/tron2_rl_lab) · [Oli](https://github.com/limxdynamics/humanoid-rl-isaaclab) · [Luna](https://github.com/limxdynamics/luna-beyondmimic)<br>MuJoCo での sim-to-sim 検証：[TRON1](https://github.com/limxdynamics/tron1-mujoco-sim) · [TRON2](https://github.com/limxdynamics/tron2_mujoco_sim) · [Oli](https://github.com/limxdynamics/humanoid-mujoco-sim) |
| 4 · デプロイ | ONNX ランタイム、ROS 2、C++ | [TRON1](https://github.com/limxdynamics/tron1-rl-deploy-python) · [TRON2](https://github.com/limxdynamics/tron2_rl_deploy_python) · [Oli](https://github.com/limxdynamics/humanoid-rl-deploy-python) · Luna：デプロイ用リポジトリは未公開 |

**LimX のロボットで何か作りましたか？** このリストに追加できます —— [プロジェクトを投稿](https://github.com/limxdynamics/awesome-limx/issues/new?template=add-project.yml)（リンクだけで構いません）。先に[コントリビューションガイド](CONTRIBUTING.md)を読むこともできます。コードはご自身のリポジトリのままで構いません。

## 移動と全身制御

_50 件（4 グループ）：論文 20 · コード 30_

### 地形と知覚ロコモーション

| プロジェクト | 機種 | 作者 / 組織 | 年 | 種別 | リンク |
|---|---|---|---|---|---|
| <a id="p-ame-2"></a>**AME-2**：注意機構による地図エンコーディングで、まばらな足場でも俊敏かつ汎用的な知覚ロコモーション | `TRON1` | [ETH Zurich RSL](https://rsl.ethz.ch) | 2026 | 論文 | [プロジェクト](https://sites.google.com/leggedrobotics.com/ame-2)&nbsp;·&nbsp;[論文](https://arxiv.org/abs/2601.08485) |
| <a id="p-faststair"></a>**FastStair**：モデルベースの足場計画と強化学習を組み合わせ、階段を駆け上がる | `Oli` | HIT, LimX et al. | 2026 | 論文 | [プロジェクト](https://npcliu.github.io/FastStair)&nbsp;·&nbsp;[論文](https://arxiv.org/abs/2601.10365)&nbsp;·&nbsp;[動画](https://youtu.be/SoLBK7VEGDo) |
| <a id="p-steppingstonelocomotion"></a>**SteppingStoneLocomotion**：三段階の PPO カリキュラムで飛び石を渡る：まずブラインド、次に深度視覚、最後に状態推定器 | `TRON1`&nbsp;*sim* | [Yiyou6](https://github.com/Yiyou6) | 2026 | コード | [コード](https://github.com/Yiyou6/SteppingStoneLocomotion)&nbsp;·&nbsp;[動画](https://www.youtube.com/watch?v=vs608-L7kl0) |
| <a id="p-height-adjustable-wheel-legged-rl"></a>**Height-Adjustable Wheel-Legged RL**：ホイールフット TRON1 での地形適応と車高調整 | `TRON1` | 桂林電子科技大学、上海交通大学、浙江大学 | 2026 | 論文 | [論文](https://doi.org/10.1109/amc67705.2026.11435832) |
| <a id="p-reference-guided-stair-climbing"></a>**Reference-Guided Stair Climbing**：参照軌道に導かれた強化学習でホイールフット TRON1 が階段を走破、学士論文 | `TRON1`&nbsp;*sim* | ウプサラ大学 | 2026 | 論文 | [論文](http://urn.kb.se/resolve?urn=urn:nbn:se:uu:diva-594330) |
| <a id="p-ame-locomotion-tron2a"></a>**AME Locomotion for TRON2A**：Isaac Lab での AME 再現に TRON2A 脚式環境を追加 | `TRON2`&nbsp;*sim* | [possibleustc](https://github.com/possibleustc) | 2026 | コード | [コード](https://github.com/possibleustc/AME_Locomotion) |
| <a id="p-offline-visual-encoder-biped"></a>**Offline Visual Encoder for Biped Locomotion**：深度から高さへのエンコーダをオフライン学習して固定し、視覚ベースの歩行を学習 | `TRON1` | 華中科技大学 | 2026 | 論文 | [論文](https://doi.org/10.1109/access.2026.3686506) |
| <a id="p-barlowwalk"></a>**BarlowWalk**：Barlow Twins による自己教師ありの地形表現で地形適応ロコモーション | `TRON1`&nbsp;*sim* | HIT Shenzhen | 2025 | 論文 | [論文](https://arxiv.org/abs/2508.00939) |
| <a id="p-ctbc"></a>**CTBC**：接触をきっかけに階段を登るブラインド手法、ホイール付き二足が指示軌道から学習 | `TRON1` | Shanghai University, COWAROBOT | 2025 | 論文 | [プロジェクト](https://ctbc-for-wheeled-bipedal-robots.github.io/)&nbsp;·&nbsp;[論文](https://arxiv.org/abs/2509.02986) |
| <a id="p-ga-phl"></a>**GA-PHL**：足元の地形をリアルタイムに再構成し、歩容タイミングを適応させる知覚歩行 | `Oli` | USTC, LimX et al. | 2025 | 論文 | [プロジェクト](https://ga-phl.github.io/)&nbsp;·&nbsp;[論文](https://arxiv.org/abs/2512.07464) |
| <a id="p-lipm-guided-rl"></a>**LIPM-Guided RL**：線形倒立振子モデルに基づく報酬で、屋外でも安定し外乱に強い知覚歩行 | `TRON1` | SUSTech CLEAR Lab, HKUST et al. | 2025 | 論文 | [論文](https://arxiv.org/abs/2509.09106) |
| <a id="p-vmts"></a>**VMTS**：視覚を使う混合エキスパート型の教師・生徒 RL で多様な地形を歩行 | `P1` | Southeast University | 2025 | コード | [論文](https://arxiv.org/abs/2503.07049)&nbsp;·&nbsp;[コード](https://github.com/chenfu-user/VMTS) |

### 強化学習の訓練と実機転移

| プロジェクト | 機種 | 作者 / 組織 | 年 | 種別 | リンク |
|---|---|---|---|---|---|
| <a id="p-biped-rl-with-pathfinding"></a>**Biped RL with Pathfinding**：独自のゴールとそこへの経路探索を備えた Isaac Lab 学習環境 | `TRON1`&nbsp;*sim* | [shandilya1998](https://github.com/shandilya1998) | 2026 | コード | [コード](https://github.com/singhaman1750/biped-rl-isaaclab-iisc) |
| <a id="p-osram"></a>**OSRAM**：閉ループ系をオンラインでモデル化し、実機に残る追従誤差を補正 | `TRON1` | [Duke University](https://github.com/generalroboticslab) | 2026 | コード | [コード](https://github.com/generalroboticslab/OSRAM) |
| <a id="p-rl-tron1"></a>**TRON1 Teacher-Student RL**：ポイントフット版向けの教師・生徒構成による Isaac Lab 歩行学習 | `TRON1`&nbsp;*sim* | [Jiakang Ma](https://github.com/Jiakang-Ma) | 2026 | コード | [コード](https://github.com/Jiakang-Ma/rl-tron1) |
| <a id="p-tron1-sliding-analysis"></a>**TRON1 Sliding Analysis**：ホイールフットのポリシーがどの摩擦で横滑りし始めるかを、Isaac と MuJoCo で検証 | `TRON1`&nbsp;*sim* | [Shukashuki](https://github.com/Shukashuki) | 2026 | コード | [コード](https://github.com/Shukashuki/tron1-sliding-analysis) |
| <a id="p-vaps"></a>**VAPS**：宙返り中に続行・中止・安全な転倒を選び分け、実機で側方宙返りを実演 | `Oli` | TU Darmstadt, LimX et al. | 2026 | 論文 | [プロジェクト](https://vaps-r-al.github.io/)&nbsp;·&nbsp;[論文](https://arxiv.org/abs/2610.01397) |
| <a id="p-wf_tron1a-stand-still-policy"></a>**Wheel-Foot TRON1 Stand-Still Policy**：RL の報酬を調整し、速度ゼロ指令でホイールフット機が流れずに静止するようにした | `TRON1`&nbsp;*sim* | [F-Morry](https://github.com/F-Morry) | 2026 | コード | [コード](https://github.com/F-Morry/limx_rl) |
| <a id="p-where-to-learn"></a>**Where-to-Learn**：解析的方策勾配で on-policy 強化学習の探索先を導く | `TRON1` | ZJU, SUSTech | 2026 | 論文 | [プロジェクト](https://wheretolearn.github.io)&nbsp;·&nbsp;[論文](https://arxiv.org/abs/2603.27317)&nbsp;·&nbsp;[動画](https://www.youtube.com/watch?v=DztdUyh_LVk) |
| <a id="p-zetin-tron1-deploy"></a>**Zetin TRON1 Deploy**：チームのポリシーを MuJoCo とポイントフット・ソールフット実機に展開 | `TRON1` | [Chanjun Lee (UOS Zetin)](https://github.com/chanjun-nyam) | 2026 | コード | [コード](https://github.com/chanjun-nyam/Zetin-Humanoid-RL-Deploy) |
| <a id="p-sf_tron-ext-estimator"></a>**Sole-Foot TRON1 Disturbance Estimator**：深度知覚型の残差ポリシーに履歴ベースの外乱推定器を追加 | `TRON1`&nbsp;*sim* | [EVENWaterOne](https://github.com/EVENWaterOne) | 2026 | コード | [コード](https://github.com/EVENWaterOne/SF_TRON_Ext-estimator) |
| <a id="p-imfs"></a>**IMFS**：世界モデルで足置き位置を計画し、ソールフット TRON1 が追従（Isaac Gym） | `TRON1`&nbsp;*sim* | [Fleming-Sung](https://github.com/Fleming-Sung) | 2026 | コード | [コード](https://github.com/Fleming-Sung/imfs) |
| <a id="p-shape-your-body"></a>**Shape Your Body**：50 種の脚式ロボットで価値勾配による設計探索、TRON1 には専用の学習設定がある | `TRON1`&nbsp;*sim* | [nico-bohlinger](https://github.com/nico-bohlinger) | 2026 | コード | [コード](https://github.com/nico-bohlinger/shape-your-body) |
| <a id="p-model-based-gait-planning-rl"></a>**Model-Based Gait Planning RL**：3D-LIPM の参照歩容で手調整の歩容報酬を置き換えて RL 学習 | `TRON1` | ハルビン工業大学 | 2026 | 論文 | [論文](https://doi.org/10.1016/j.birob.2026.100338) |
| <a id="p-w1-parkour-legged-gym"></a>**W1 Parkour in legged_gym**：legged_gym で W1 ホイール脚四足のパルクールと追従環境を構築、ROS コントローラ付き | `W1`&nbsp;*sim* | [yiqiuqwq](https://github.com/yiqiuqwq) | 2026 | コード | [コード](https://github.com/yiqiuqwq/wheellegged_control) |
| <a id="p-him-pim-isaac-lab"></a>**HIM-PIM Isaac Lab**：Isaac Lab で HIM と PIM の歩行制御を比較、階段・斜面・外乱で検証 | `TRON1`&nbsp;*sim* | [DongyangLin](https://github.com/DongyangLin) | 2025 | コード | [コード](https://github.com/DongyangLin/HIM-PIM-isaaclab) |
| <a id="p-leggedrobotslab"></a>**LeggedRobotsLab**：Isaac Lab による歩行学習、MuJoCo の sim-to-sim と実機展開付き、Go1 と TRON1 に対応 | `TRON1`&nbsp;*sim* | [Guohua Zhang](https://github.com/guohua-zhang) | 2025 | コード | [コード](https://github.com/guohua-zhang/LeggedRobotsLab) |
| <a id="p-multi-loco"></a>**Multi-Loco**：1 つの拡散モデルのポリシーでポイントフットとホイールフットの両方を制御 | `TRON1` | SUSTech CLEAR Lab, LimX et al. | 2025 | コード | [プロジェクト](https://multi-loco.github.io)&nbsp;·&nbsp;[論文](https://arxiv.org/abs/2506.11470)&nbsp;·&nbsp;[コード](https://github.com/clearlab-sustech/multi_loco_isaacgym) |
| <a id="p-pvp"></a>**PvP**：固有感覚と特権状態の対比学習で、データ効率の高い全身制御 | `Oli` | PolyU, USTC et al. | 2025 | 論文 | [論文](https://arxiv.org/abs/2512.13093) |
| <a id="p-tron-camp-wheel-foot-deployment"></a>**TRON Camp Wheel-Foot Deployment**：TRON Camp 2025 向けにホイールフットのポリシーを調整し実機で動作 | `TRON1` | [Yitao Zeng](https://github.com/24zen0) | 2025 | コード | [コード](https://github.com/24zen0/Deployment_of_wheelfoot_tron) |
| <a id="p-ptrl"></a>**PTRL**：ロボット間で事前知識を転移して RL 学習時間を短縮、Go2 と TRON1 で実機検証 | `TRON1` | ハルビン工業大学（深圳）、蘇州大学 | 2025 | 論文 | [論文](https://arxiv.org/abs/2504.05629) |
| <a id="p-anybipe"></a>**AnyBipe**：言語モデルが二足ポリシーの報酬設計・学習・展開を導くエンドツーエンドの枠組み | `TRON1` | [SJTU](https://github.com/sjtu-mvasl-robotics) | 2024 | コード | [コード](https://github.com/sjtu-mvasl-robotics/AnyBipe) |
| <a id="p-cts"></a>**CTS**：教師ポリシーと生徒ポリシーを同時に学習する脚式ロコモーション RL | `P1` | SUSTech CLEAR Lab, ZJU-UIUC et al. | 2024 | 論文 | [プロジェクト](https://clearlab-sustech.github.io/concurrentTS/)&nbsp;·&nbsp;[論文](https://arxiv.org/abs/2405.10830) |

### モデルベース制御

| プロジェクト | 機種 | 作者 / 組織 | 年 | 種別 | リンク |
|---|---|---|---|---|---|
| <a id="p-learning-enhanced-pmp-mpc"></a>**Learning-Enhanced PMP-MPC**：ポントリャーギン最適化器と学習残差で重心 MPC を解き、MuJoCo で検証 | `TRON1`&nbsp;*sim* | [Markwcl2004](https://github.com/Markwcl2004) | 2026 | コード | [論文](https://doi.org/10.1109/ASCC70886.2026.11701800)&nbsp;·&nbsp;[コード](https://github.com/Markwcl2004/PMP_based_Bipedal_MPC) |
| <a id="p-whole-body-humanoid-mpc"></a>**Whole-Body Humanoid MPC**：人型の移動操作向け非線形全身 MPC、MuJoCo での 31 自由度 Oli の例付き | `Oli`&nbsp;*sim* | [Tianxing Liu](https://github.com/liuskywalkerjskd) | 2026 | コード | [コード](https://github.com/liuskywalkerjskd/humanoid_mpc) |
| <a id="p-terrain-aware-cfr-planning"></a>**Terrain-Aware CFR Planning**：凸実行可能領域による階段走破計画、W1 で 200 回中 200 回成功 | `W1` | SUSTech CLEAR Lab | 2026 | 論文 | [論文](https://doi.org/10.21203/rs.3.rs-10577407/v1) |
| <a id="p-power-bounded-inverted-pendulum"></a>**Power-Bounded Inverted Pendulum**：出力上限を考慮した二足の最高速度モデル、関節モーターのパラメータ再調整に使用 | `TRON1`&nbsp;*sim* | 浙江大学 | 2026 | 論文 | [論文](https://doi.org/10.1007/s10409-026-25928-x) |
| <a id="p-hierarchical-nmpc-stsmc"></a>**Hierarchical NMPC + STSMC**：階層型非線形 MPC とスーパーツイスティング・スライディングモード制御、不確かさのあるホイールフット TRON1 向け | `TRON1`&nbsp;*sim* | [pjmcconnellogue](https://github.com/pjmcconnellogue) | 2026 | コード | [コード](https://github.com/pjmcconnellogue/Hierarchical-Nonlinear-MPC-and-Super-Twisting-Sliding-Mode-Control-for-a-Wheeled-Biped-Robot-) |
| <a id="p-two-wheeled-robot-lqr"></a>**Two-Wheeled Robot LQR**：ホイールフット TRON1 の LQR と全身制御、卒業研究プロジェクト | `TRON1`&nbsp;*sim* | [alpttex19](https://github.com/alpttex19) | 2025 | コード | [コード](https://github.com/alpttex19/Two_Wheeled_Robot_LQR) |
| <a id="p-bipedal-mpc"></a>**Bipedal MPC**：凸 MPC と全身制御による MuJoCo での歩行、ROS 2 ベース | `TRON1`&nbsp;*sim* | [SUSTech CLEAR Lab](https://github.com/clearlab-sustech) | 2024 | コード | [コード](https://github.com/clearlab-sustech/Bipedal_MPC) |
| <a id="p-task-space-riccati-wbc"></a>**Task-Space Riccati WBC**：劣駆動脚ロボット向け、タスク空間 Riccati フィードバックによる全身制御 | `P1`&nbsp;*sim* | SUSTech, HKUST et al. | 2024 | 論文 | [論文](https://arxiv.org/abs/2404.00591) |

### モーショントラッキングとリターゲティング

| プロジェクト | 機種 | 作者 / 組織 | 年 | 種別 | リンク |
|---|---|---|---|---|---|
| <a id="p-any2any"></a>**Any2Any**：事前学習済みの全身モーショントラッキングを、少ない適応で新しいヒューマノイドへ移植 | `Oli` `Luna` | LimX | 2026 | コード | [論文](https://arxiv.org/abs/2605.23733)&nbsp;·&nbsp;[コード](https://github.com/Ming827/any2any_sonic2Oli) |
| <a id="p-chip-for-oli"></a>**CHIP for Oli**：適応コンプライアンス型モーショントラッキング CHIP の移植版、mjlab で学習 | `Oli`&nbsp;*sim* | [Matt14-mander](https://github.com/Matt14-mander) | 2026 | コード | [コード](https://github.com/Matt14-mander/chip-oli) |
| <a id="p-supermimic-for-oli"></a>**SuperMimic for Oli**：世界モデル型全身制御 SuperMimic の適用版、1 つのポリシーで 40 動作を追従 | `Oli`&nbsp;*sim* | [Tianxing Liu](https://github.com/liuskywalkerjskd) | 2026 | コード | [コード](https://github.com/liuskywalkerjskd/supermimic_oli) |
| <a id="p-tron1-wf-mimic"></a>**Wheel-Foot TRON1 Dance Mimic**：ホイールフット二足で人のダンスを模倣し、この形態でできる動作とできない動作を分析 | `TRON1`&nbsp;*sim* | [HUST-dolores](https://github.com/HUST-dolores) | 2026 | コード | [コード](https://github.com/HUST-dolores/tron1-wf-mimic) |
| <a id="p-robot-lab-srl-oli-mimic"></a>**Oli Mimic Tasks for robot_lab**：robot_lab の拡張、Isaac Lab に動作模倣の学習タスクを追加 | `Oli`&nbsp;*sim* | [song-hl](https://github.com/song-hl) | 2026 | コード | [コード](https://github.com/song-hl/robot_lab_srl) |
| <a id="p-robot-retargeter"></a>**Robot Retargeter**：SMPL-X や他ロボットの動作を人型にリターゲット、この機種の専用設定付き | `Oli`&nbsp;*sim* | [ccrpRepo](https://github.com/ccrpRepo) | 2026 | コード | [コード](https://github.com/ccrpRepo/robot_retargeter) |
| <a id="p-timo"></a>**Timo**：テキストから動作を生成する運動学を考慮したマルチモーダル拡散 Transformer、生成動作を Oli と Luna の実機で実行 | `Oli` `Luna` | LimX | 2026 | 論文 | [プロジェクト](https://kyfafyd.wang/projects/timo)&nbsp;·&nbsp;[論文](https://arxiv.org/abs/2609.30761) |
| <a id="p-hu-d03-rl-mjlab"></a>**Earlier-Generation Oli RL in mjlab**：HU_D03 モデル向けの歩行と動作模倣ポリシー、mjlab で学習（ベトナム語） | `Oli`&nbsp;*sim* | [KhanhPham248](https://github.com/KhanhPham248) | 2026 | コード | [コード](https://github.com/KhanhPham248/LimX_HU_D03_rl_mjlab) |
| <a id="p-multi-embodiment-retargeting"></a>**Multi-Embodiment Retargeting**：グラフ条件付き拡散モデルで、構造の異なるロボット間で同じ動作をリターゲット | `TRON1` `Oli`&nbsp;*sim* | SUSTech, HKUST et al. | 2025 | 論文 | [論文](https://arxiv.org/abs/2505.20857) |

## 知覚とナビゲーション

_13 件：論文 2 · コード 11_

| プロジェクト | 機種 | 作者 / 組織 | 年 | 種別 | リンク |
|---|---|---|---|---|---|
| <a id="p-tron1_navrl"></a>**TRON1 NavRL**：Isaac Lab で上位のナビゲーションポリシーだけを RL で学習し、既存の歩容ポリシーを再利用（韓国語） | `TRON1`&nbsp;*sim* | [jongbob1918](https://github.com/jongbob1918) | 2026 | コード | [コード](https://github.com/jongbob1918/tron1_navrl) |
| <a id="p-tron1-multi-floor-navigation"></a>**TRON1 Multi-floor Navigation**：平地走行、フロア切り替え、階段走行を一つのミッションに統合（韓国語） | `TRON1` | [justpastmarch](https://github.com/justpastmarch) | 2026 | コード | [コード](https://github.com/justpastmarch/TRON1_multifloor-navigation) |
| <a id="p-geometric-candidate-modes"></a>**Geometric Candidate Modes**：マルチモーダルなデモからナビゲーションを学習、シミュレーションで学習したポリシーを TRON1 に転移 | `TRON1` | オハイオ州立大学 | 2026 | 論文 | [論文](https://arxiv.org/abs/2610.20241) |
| <a id="p-ros2_gnss_waypoint_nav"></a>**GNSS Waypoint Navigation**：RTK GNSS、MID360、Nav2 による地図不要の屋外ウェイポイントナビゲーション、TRON1 ベースブリッジ付き | `TRON1` | [武漢大学 BRAIN Lab](https://github.com/Whu-BrainLab) | 2026 | コード | [コード](https://github.com/Whu-BrainLab/ros2_gnss_waypoint_nav) |
| <a id="p-lightnav-0"></a>**LightNav-0**：VLM ベースのナビゲーションスタック、MPC 追従と Web パネル付き、Go2 と TRON1 に対応 | `TRON1` | [Light Origins](https://github.com/lightorigins) | 2026 | コード | [論文](https://arxiv.org/abs/2608.30935)&nbsp;·&nbsp;[コード](https://github.com/lightorigins/LightNav-0)&nbsp;·&nbsp;[モデル](https://huggingface.co/LightOriginsHQ/LightNav-0) |
| <a id="p-gps-tron1"></a>**GPS-TRON1**：GNSS と FAST-LIO の融合測位による屋外ウェイポイント走行、局所的な衝突回避付き | `TRON1` | [potatoHu-a](https://github.com/potatoHu-a) | 2026 | コード | [コード](https://github.com/potatoHu-a/GPS-TRON1) |
| <a id="p-wf_tron1a-lidar-navigation"></a>**Wheel-Foot TRON1 LiDAR Odometry**：2D LiDAR の RF2O オドメトリで、車輪の空転や引っかかり時の車輪オドメトリ誤差を補正 | `TRON1` | [F-Morry](https://github.com/F-Morry) | 2026 | コード | [コード](https://github.com/F-Morry/limx_ws) |
| <a id="p-wave-go"></a>**WAVE-Go**：世界モデルによる行動適応で長距離ナビゲーション、Go2-W 実機と MuJoCo 上の Luna で検証 | `Luna`&nbsp;*sim* | BIT、HKU、LimX ほか | 2026 | コード | [論文](https://arxiv.org/abs/2609.18193)&nbsp;·&nbsp;[コード](https://github.com/vigorlee/wave-go) |
| <a id="p-tron-1-struzzo"></a>**TRON-1 Struzzo**：搭載した Jetson で自律走行するための Gazebo と ROS 2 環境 | `TRON1` | [enfff](https://github.com/enfff) | 2025 | コード | [コード](https://github.com/enfff/tron1-gazebo-ros2) |
| <a id="p-neupan-on-tron1"></a>**NeuPAN on TRON1**：A* による大域計画と NeuPAN のエンドツーエンド局所回避を組み合わせた ROS ナビゲーション | `TRON1` | [WikHClean](https://github.com/WikHClean) | 2025 | コード | [コード](https://github.com/WikHClean/-ROS1-NeuPAN-TRON1-) |
| <a id="p-3d-navigation-with-pct-planner"></a>**3D Navigation with PCT Planner**：Mid360 LiDAR と PCT プランナーで室内と階段を 3D ナビゲーション、実機で検証 | `TRON1` | [81578823](https://github.com/81578823) | 2025 | コード | [コード](https://github.com/81578823/3D_navigation_PCTplanner) |
| <a id="p-terrain-aware-lio-legged-wheel"></a>**Terrain-Aware LiDAR-Inertial Odometry**：地形を考慮した脚車輪ロボット向け LiDAR 慣性オドメトリ、ホイールフット TRON1 で屋外実験 | `TRON1` | 上海交通大学 | 2025 | 論文 | [論文](https://arxiv.org/abs/2509.26222) |
| <a id="p-eroam"></a>**EROAM**：イベントカメラによる回転オドメトリ、TRON1 で収録したシーケンスを含む | `TRON1` | [wlxing1901](https://github.com/wlxing1901) | 2024 | コード | [プロジェクト](https://wlxing1901.github.io/eroam/)&nbsp;·&nbsp;[論文](https://arxiv.org/abs/2411.11004)&nbsp;·&nbsp;[コード](https://github.com/wlxing1901/eroam)&nbsp;·&nbsp;[動画](https://youtu.be/8tF6b2VuvSM) |

## マニピュレーション

_11 件：論文 5 · コード 6_

| プロジェクト | 機種 | 作者 / 組織 | 年 | 種別 | リンク |
|---|---|---|---|---|---|
| <a id="p-cola-on-tron2"></a>**COLA on TRON2**：人とロボットの協調搬送 COLA を Unitree G1 から移植 | `TRON2`&nbsp;*sim* | [Matt14-mander](https://github.com/Matt14-mander) | 2026 | コード | [コード](https://github.com/Matt14-mander/COLA_TRON2) |
| <a id="p-holistic-loco-manipulation"></a>**Holistic Loco-Manipulation**：6 自由度の手先目標を、アーム付き TRON1 の脚と腕の動作に直接写像する RL 全身制御 | `TRON1` | ZJU-UIUC, LimX | 2026 | 論文 | [論文](https://arxiv.org/abs/2609.18930) |
| <a id="p-tron1-to-ur5e-bottle-transfer"></a>**TRON1-to-UR5e Bottle Transfer**：二足ロボットが瓶を受け渡し場所へ運び、UR5e アームが把持、MuJoCo で実装（韓国語） | `TRON1`&nbsp;*sim* | [Centaucyan](https://github.com/Centaucyan) | 2026 | コード | [コード](https://github.com/Centaucyan/Proj_Transferring_bottle_from_tron1_to_ur5e_in_mujoco_env) |
| <a id="p-cooperative-transportation"></a>**Cooperative Transportation**：2 台のロボットが 1 つの荷物を協調搬送、ホイールフット TRON1 と TRON2 の組に対応 | `TRON1` `TRON2`&nbsp;*sim* | [Matt14-mander](https://github.com/Matt14-mander) | 2026 | コード | [コード (TRON1)](https://github.com/Matt14-mander/Multiple_Humanoid_Cooperative_Transportation)&nbsp;·&nbsp;[コード (TRON2)](https://github.com/Matt14-mander/tron2-cooperative-carrying) |
| <a id="p-cwi"></a>**CWI**：モーキャプと指令を組み合わせた複合全身模倣で、歩きながらの操作を実現 | `Oli` | LimX, HKU et al. | 2026 | 論文 | [プロジェクト](https://cwi-ral.github.io/CWI-RAL-Webpage/)&nbsp;·&nbsp;[論文](https://arxiv.org/abs/2606.27676) |
| <a id="p-arm-tron"></a>**Arm-TRON**：3 種類の足先を換えられる片腕二足と、足先ごとの RL 全身制御 | `TRON1` | SUSTech, ZJU et al. | 2026 | 論文 | [論文](https://doi.org/10.1109/TMECH.2026.3727546) |
| <a id="p-mobile-pedipulation"></a>**Mobile Pedipulation**：階層型 NMPC でホイールフット TRON1 が車輪付きの脚で物体を押し動かす、RA-L | `TRON1` | ミシガン大学 | 2026 | 論文 | [論文](https://arxiv.org/abs/2606.19233) |
| <a id="p-tron2-vision-teleoperation"></a>**TRON2 Vision Teleoperation**：カメラで腕と手を追跡し、ORCA ハンド付き双腕ロボットを遠隔操作（スペイン語） | `TRON2`&nbsp;*sim* | [Aremanky](https://github.com/Aremanky) | 2026 | コード | [コード](https://github.com/Aremanky/Teleoperacion-tron-2) |
| <a id="p-umi-on-tron1"></a>**UMI on Tron1**：ARX5 アームで UMI の操作スキルを実機で実行 | `TRON1` | [Czy213hd](https://github.com/Czy213hd) | 2025 | コード | [コード](https://github.com/Czy213hd/umi-on-tron-lab) |
| <a id="p-quest-vr-teleop-for-oli"></a>**Quest VR Teleop for Oli**：Meta Quest で両腕・グリッパー・頭部を遠隔操作し、カメラ映像をヘッドセットに表示 | `Oli` | [MSTLE](https://github.com/MSTLE) | 2025 | コード | [コード](https://github.com/MSTLE/Limx_teleoperate-end_pose) |
| <a id="p-wheeled-quadrupedal-manipulator"></a>**Wheeled-Quadrupedal Manipulator**：ホイール付き四脚にアームを載せ、学習した制御器で手先の姿勢を追従 | `W1` | SUSTech CLEAR Lab, ZJU-UIUC et al. | 2024 | 論文 | [プロジェクト](https://clearlab-sustech.github.io/RFM_loco_mani/)&nbsp;·&nbsp;[論文](https://arxiv.org/abs/2412.03012) |

## エンボディドAI

_9 件：論文 2 · コード 7_

| プロジェクト | 機種 | 作者 / 組織 | 年 | 種別 | リンク |
|---|---|---|---|---|---|
| <a id="p-tron1-hermes-agent"></a>**Tron 1 Hermes Agent**：Mac 上で動く自己改善型ローカル AI エージェントが MuJoCo でロボットを操作 | `TRON1`&nbsp;*sim* | [justinsuo](https://github.com/justinsuo) | 2026 | コード | [コード](https://github.com/justinsuo/tron1-hermes-agent) |
| <a id="p-fluxvla-on-tron2"></a>**FluxVLA on TRON2**：FluxVLA 視覚言語行動モデルを自分のロボットで学習・展開 | `TRON2` | [emoPointer](https://github.com/emoPointer) | 2026 | コード | [コード](https://github.com/emoPointer/FluxVLA) |
| <a id="p-oli-voice-interaction"></a>**Oli Voice Interaction**：オフライン・オンライン音声認識、LLM 対話、動作指令を備えた ROS 2 音声システム | `Oli` | [zhilin2025](https://github.com/zhilin2025) | 2026 | コード | [コード](https://github.com/zhilin2025/oli_audio) |
| <a id="p-hwam"></a>**HWAM**：将来の状態と行動を同時に生成するヒューマノイド世界行動モデル | `Oli` | LimX | 2026 | 論文 | [プロジェクト](https://hwam.vercel.app/)&nbsp;·&nbsp;[論文](https://arxiv.org/abs/2610.12026) |
| <a id="p-acg-wam"></a>**ACG-WAM**：行動条件付きの幾何潜在表現を予測する世界行動モデル、多指ハンドで検証 | `TRON2` | BIT, LimX | 2026 | コード | [プロジェクト](https://RoboOpus.github.io/ACG-WAM)&nbsp;·&nbsp;[論文](https://arxiv.org/abs/2610.06965)&nbsp;·&nbsp;[コード](https://github.com/RoboOpus/ACG-WAM) |
| <a id="p-drifting-action-heads-for-gr00t-n17"></a>**GR00T Drifting Heads**：GR00T N1.7 の拡散アクションヘッドを 1 ステップの drifting ヘッドに置き換え、推論コストを削減 | `TRON2` | ZJU-UIUC, LimX | 2026 | 論文 | [論文](https://arxiv.org/abs/2609.18108) |
| <a id="p-tron2-garment-feeder"></a>**TRON2 Garment Feeder**：双腕で衣類を送り込むタスク向けに微調整した Pi0.5 ポリシー | `TRON2` | [voniu](https://huggingface.co/voniu) | 2026 | コード | [モデル](https://huggingface.co/voniu/tron2-garment-feeder-button-pi05) |
| <a id="p-tron2-lerobot-datasets"></a>**TRON2 LeRobot Datasets**：LeRobot 形式のピック＆プレース、衣類たたみ、注水データセットと、それで微調整した GR00T | `TRON2` | [trantor2nd](https://huggingface.co/trantor2nd) | 2026 | コード | [モデル](https://huggingface.co/models?author=trantor2nd&search=tron2)&nbsp;·&nbsp;[データセット](https://huggingface.co/datasets?author=trantor2nd&search=tron2) |
| <a id="p-troncamp-pi05-policies"></a>**TRONCamp Pi0.5 Policies**：TRONCamp の生け花と衣類たたみ課題向け Pi0.5 チェックポイント | `TRON2` | [toki1231](https://huggingface.co/toki1231) | 2026 | コード | [モデル](https://huggingface.co/toki1231) |

## ツール、シミュレーション、SDK

_ツール 22 件（4 グループ）_

### 学習フレームワーク

| プロジェクト | 機種 | 作者 / 組織 | 年 | リンク |
|---|---|---|---|---|
| <a id="p-tron1-isaac-lab-tasks"></a>**TRON1 Isaac Lab Tasks**：3 種類の足すべてに対応した Isaac Lab タスク、ジャンプを含む | `TRON1` | [HughWang-wzy](https://github.com/HughWang-wzy) | 2026 | [コード](https://github.com/HughWang-wzy/tron1-rl-isaaclab) |
| <a id="p-tron1-rl-mjlab"></a>**TRON1 RL on mjlab**：mjlab でホイールフット歩行を学習し ONNX を出力 | `TRON1` | [Xinchen Yao](https://github.com/hoscy) | 2025 | [コード](https://github.com/hoscy/tron1-rl-mjlab) |
| <a id="p-leggedgym-ex"></a>**LeggedGym-Ex**：Genesis、Isaac Gym、Isaac Sim 上の legged_gym | `TRON1` | [Yasen Jia](https://github.com/lupinjia) | 2024 | [コード](https://github.com/lupinjia/LeggedGym-Ex) |
| <a id="p-bipedal_locomotion_isaaclab"></a>**Bipedal Locomotion on Isaac Lab**：Isaac Lab で平地・不整地・階段の歩行を学習し、実機へ転移 | `TRON1` | [Andy-xiong6 (SUSTech)](https://github.com/Andy-xiong6) | 2024 | [コード](https://github.com/Andy-xiong6/bipedal_locomotion_isaaclab) |

### シミュレーションと環境

| プロジェクト | 機種 | 作者 / 組織 | 年 | リンク |
|---|---|---|---|---|
| <a id="p-tron2-wuji-bag-replay"></a>**TRON2 Wuji Hand Replay**：記録したロボットと Wuji ハンドの軌道を Isaac Sim で再生 | `TRON2` | [zengxiong111](https://github.com/zengxiong111) | 2026 | [コード](https://github.com/zengxiong111/tron2-wuji-bag-replay) |
| <a id="p-metalsim"></a>**MetalSim**：Apple シリコン向けシミュレーション・学習基盤、TRON1 専用モジュール付き：シミュレータ、制御器、実機ブリッジ | `TRON1` | [Aditya Pulipaka](https://github.com/pulipakaa24) | 2026 | [コード](https://github.com/pulipakaa24/MetalSim) |
| <a id="p-robot-sim-docker"></a>**Robot Sim Docker**：ROS 2 と LimX Gazebo、Isaac Lab、LeIsaac、MuJoCo を 1 台のホストでコンテナ実行 | `TRON1` | [Aklva](https://github.com/Aklva) | 2026 | [コード](https://github.com/Aklva/robot-sim-docker) |
| <a id="p-limx-robotics-mcp"></a>**LimX Robotics MCP Server**：AI エージェントが MuJoCo モデルの読み込み、関節制御、ポリシー実行を行える MCP サーバー | `TRON1` `Oli` | [sandraschi](https://github.com/sandraschi) | 2026 | [コード](https://github.com/sandraschi/limx-robotics-mcp) |
| <a id="p-tron_docker_sim"></a>**TRON Docker Sim**：ROS 2 の Gazebo シミュレーションをコンテナで動かし、GUI も転送 | `TRON1` | [The-RoboTUM](https://github.com/The-RoboTUM) | 2026 | [コード](https://github.com/The-RoboTUM/tron_docker_sim) |
| <a id="p-gewu-unity-rl-playground"></a>**Gewu (Unity RL Playground)**：Unity の強化学習プラットフォーム、TRON1 の歩行・走行・ジャンプのポリシー付き | `TRON1` | [loongOpen](https://github.com/loongOpen) | 2025 | [論文](https://arxiv.org/abs/2503.05146)&nbsp;·&nbsp;[コード](https://github.com/loongOpen/Unity-RL-Playground) |
| <a id="p-arc-bridge"></a>**ARC Bridge**：LCM でロボット制御器を MuJoCo シミュレータにつなぐブリッジ | `TRON1` | [UMich ARCaD Lab](https://github.com/ARCaD-Lab-UM) | 2024 | [コード](https://github.com/ARCaD-Lab-UM/arc-bridge) |

### デプロイと制御

| プロジェクト | 機種 | 作者 / 組織 | 年 | リンク |
|---|---|---|---|---|
| <a id="p-tron1_ctrl_ros2"></a>**TRON1 ROS 2 Control**：ロボットの WebSocket SDK をラップした ROS 2 制御パッケージ | `TRON1` | [Turing-zero](https://github.com/Turing-zero) | 2026 | [コード](https://github.com/Turing-zero/tron1_ctrl_ros2) |
| <a id="p-tron2_camera_calibration"></a>**TRON2 Camera Calibration**：頭部と手首カメラのキャリブレーションツール | `TRON2` | [zengxiong111](https://github.com/zengxiong111) | 2026 | [コード](https://github.com/zengxiong111/tron2_camera_calibration) |
| <a id="p-tron1_wheel_gui"></a>**TRON1 Wheel GUI**：Qt と ROS を組み合わせた操作パネルで、ノート PC からホイールフット実機を動かす | `TRON1` | [Yang Zhuqi](https://github.com/Y20-code-cpu) | 2026 | [コード](https://github.com/Y20-code-cpu/tron1_wheel_gui) |
| <a id="p-wf_tron1b_deploy"></a>**Wheel-Foot Depth Policy Deploy**：深度知覚型と非知覚型のホイールフットポリシーを Docker と ROS で sim-to-sim 検証 | `TRON1` | [Leixin Chang](https://github.com/Leixinjonaschang) | 2026 | [コード](https://github.com/Leixinjonaschang/wf_tron1b_deploy) |
| <a id="p-tron_deploy"></a>**TRON Deploy for Windows**：Windows 11 ノートにポイントフット SDK を入れてポリシーを実行 | `TRON1` | [candi4](https://github.com/candi4) | 2026 | [コード](https://github.com/candi4/Tron_Deploy) |
| <a id="p-multi-robot-camera-collector"></a>**Multi-Robot Camera Collector**：複数ロボットのカメラを切り替え、タスク段階ごとに画像を保存してデータ収集（中国語） | `TRON1` `TRON2` | [oalaaCN](https://github.com/oalaaCN) | 2026 | [コード](https://github.com/oalaaCN/multi_robot_camera_collector) |
| <a id="p-crl-humanoid-ros"></a>**CRL Humanoid ROS**：ETH チューリッヒの ROS 2 フレームワーク、シミュレーション・実機制御・RL 制御器を含み G1 と TRON1 に対応 | `TRON1` | [Jin Cheng (ETH Zurich CRL)](https://github.com/catachiii) | 2025 | [コード](https://github.com/catachiii/crl-humanoid-ros) |
| <a id="p-websocket_ros"></a>**TRON1 WebSocket-ROS Bridge**：ロボットの WebSocket API を ROS へつなぐ Docker ブリッジ、実機なしで試せる疑似ロボット付き | `TRON1` | [daweidavidwang](https://github.com/daweidavidwang) | 2025 | [コード](https://github.com/daweidavidwang/websocket_ros) |

### モデルとモーションデータ

| プロジェクト | 機種 | 作者 / 組織 | 年 | リンク |
|---|---|---|---|---|
| <a id="p-rimkit"></a>**RIMKit**：接触を考慮した人の動作のリターゲット、17 機種に対応しこの機種のモデルを同梱 | `Oli` | [Taemoon Jeong](https://github.com/tmjeong1103) | 2026 | [コード](https://github.com/tmjeong1103/RIMKit) |
| <a id="p-tron2_revo3_description"></a>**TRON2 with Revo3 Hands**：BrainCo Revo3 ハンドを装着した組立モデル、学習にそのまま使える | `TRON2` | [ENDLESS0321](https://github.com/ENDLESS0321) | 2026 | [コード](https://github.com/ENDLESS0321/tron2_revo3_description) |
| <a id="p-limx-3d-measurement-workbench"></a>**LimX 3D Measurement Workbench**：TRON 製品モデルを閲覧し、部品を探して寸法を測る Web ツール | `TRON1` `TRON2` | [voniu](https://github.com/voniu) | 2026 | [コード](https://github.com/voniu/limx-3d-measurement-workbench) |

## 教育と競技会

_18 件：論文 2 · コード 15 · チュートリアル 1_

| プロジェクト | 機種 | 作者 / 組織 | 年 | 種別 | リンク |
|---|---|---|---|---|---|
| <a id="p-atec-2026-simulation-challenge"></a>**ATEC 2026 Simulation Challenge**：ATEC 2026 ロボットシミュレーションチャレンジの公式スターターコード、機種ごとに部門あり | `TRON1` `TRON2`&nbsp;*sim* | [ATEC](https://github.com/atecup) | 2026 | コード | [コード](https://github.com/atecup/ATEC2026_Simulation_Challenge) |
| <a id="p-troncamp-2026-mani-solution"></a>**TRONCamp 2026 Mani Solution**：双腕 4 課題向けの ACT 解法、チェックポイントとデモデータを公開 | `TRON2`&nbsp;*sim* | [han-xudong](https://github.com/han-xudong) | 2026 | コード | [コード](https://github.com/han-xudong/troncamp-mani)&nbsp;·&nbsp;[モデル](https://huggingface.co/han-xudong/troncamp-mani-act)&nbsp;·&nbsp;[データセット](https://huggingface.co/datasets/han-xudong/troncamp-mani-dataset) |
| <a id="p-troncamp-2026-locomotion-solution"></a>**TRONCamp 2026 Locomotion Solution**：腕を固定したソールフット TRON2 の RL 歩行ポリシー、チェックポイントを公開 | `TRON2`&nbsp;*sim* | [han-xudong](https://github.com/han-xudong) | 2026 | コード | [コード](https://github.com/han-xudong/troncamp-locomotion)&nbsp;·&nbsp;[モデル](https://huggingface.co/han-xudong/troncamp-locomotion-rl) |
| <a id="p-study_tron1"></a>**TRON1 Study Notes**：ロボット SDK なしで Isaac Lab 学習を行うための環境構築メモと学習ログ | `TRON1`&nbsp;*sim* | [beamkeerati](https://github.com/beamkeerati) | 2026 | コード | [コード](https://github.com/beamkeerati/study_tron1) |
| <a id="p-openarm-mobile-manipulation-lab"></a>**OpenArm Mobile Manipulation Lab**：2 日間の MuJoCo・ROS 2 講座：OpenArm を二足または車輪台車に載せ、自然言語の指示で動かす（韓国語） | `TRON1`&nbsp;*sim* | [aha645](https://github.com/aha645) | 2026 | コード | [コード](https://github.com/aha645/openarms_llm_ex) |
| <a id="p-limx-tron1-learning"></a>**LimX Tron1 Learning**：Isaac Lab での学習を順を追って説明するインタラクティブガイド | `TRON1`&nbsp;*sim* | [jessiezhg](https://huggingface.co/jessiezhg) | 2026 | チュートリアル | [チュートリアル](https://huggingface.co/spaces/jessiezhg/LimX-Tron1-Learning) |
| <a id="p-zetin-robocup-2026"></a>**Zetin RoboCup 2026**：Isaac Lab でソールフット TRON1 のサッカーロボットに歩行・ボール追跡・シュートを学習（韓国語） | `TRON1`&nbsp;*sim* | [tae2yi](https://github.com/tae2yi) | 2026 | コード | [コード](https://github.com/tae2yi/Zetin_Robocup2026) |
| <a id="p-conducting-evaluation-with-oli"></a>**Conducting Evaluation System**：音楽教育向けの指揮動作の実演と評価システム、Oli のデジタルツインで実証 | `Oli`&nbsp;*sim* | 広東培正学院 | 2026 | 論文 | [論文](https://doi.org/10.1145/3806980.3807204) |
| <a id="p-every-embodied-troncamp-mani"></a>**Every Embodied: TRONCamp Mani**：Datawhale の具身 AI オープン講座、TRON2 双腕タスクを扱う TRONCamp Mani の章を収録（中国語） | `TRON2`&nbsp;*sim* | [Datawhale](https://github.com/datawhalechina) | 2026 | コード | [コード](https://github.com/datawhalechina/every-embodied/tree/main/15-Challenge%E7%AB%9E%E8%B5%9B/TRONCamp-Mani) |
| <a id="p-atec2026-logic-tars"></a>**ATEC 2026 Wheel-Legged Entry**：ATEC 2026 チャレンジ参加チームの強化学習訓練とシミュレーション配備 | `TRON1` `TRON2`&nbsp;*sim* | [Logic-TARS](https://github.com/Logic-TARS) | 2026 | コード | [コード](https://github.com/Logic-TARS/ATEC2026) |
| <a id="p-zetin-robocup-control"></a>**Zetin RoboCup Control**：RoboCup 2026 の試合用コード：TRON1 の下半身に自作の上半身とカメラを接続（韓国語） | `TRON1` | [newb-ops（ソウル市立大学 ZETIN）](https://github.com/newb-ops) | 2026 | コード | [コード](https://github.com/newb-ops/robocup-control-portfolio) |
| <a id="p-troncamp-mani-24zlha"></a>**TRONCamp Mani Solution 24ZlhA**：ACT とハードサンプルマイニング、マルチ GPU 学習、技術レポート付き。T4 のオンライン得点は 79/100 | `TRON2`&nbsp;*sim* | [upset666](https://github.com/upset666) | 2026 | コード | [コード](https://github.com/upset666/troncamp-mani-24ZlhA) |
| <a id="p-troncamp-mani-act-dp"></a>**TRONCamp Mani ACT + Diffusion Policy**：T1〜T3 は ACT、3 つのボウルを積む課題は Diffusion Policy、設計文書付き（中国語） | `TRON2`&nbsp;*sim* | [irvingskr](https://github.com/irvingskr) | 2026 | コード | [コード](https://github.com/irvingskr/troncamp-mani) |
| <a id="p-troncamp-mani-sormaker"></a>**TRONCamp Mani Solution SORMaker**：4 課題共通の ACT 学習・デプロイ手順、T3・T4 ポリシーの実行動画付き | `TRON2`&nbsp;*sim* | [SORMaker](https://github.com/SORMaker) | 2026 | コード | [コード](https://github.com/SORMaker/troncamp-mani) |
| <a id="p-hands-on-embodied-ai"></a>**Hands-on Embodied AI**：アルゴリズムから実機までのオープン講座、屋外 GNSS と Nav2 ナビゲーションを含む（中国語） | `TRON1` | [武漢大学 BRAIN Lab](https://github.com/Whu-BrainLab) | 2025 | コード | [コード](https://github.com/Whu-BrainLab/Embodied-AI-Tutorial)&nbsp;·&nbsp;[チュートリアル (zh)](https://mp.weixin.qq.com/s/YLKVi09hgImSuWUr_S6gJA) |
| <a id="p-canton-tower-robot-climbing-challenge"></a>**広州タワー ロボット登塔チャレンジ**：Oli が FastStair 手法で階段登りの優勝と最優秀精密制御賞を獲得 | `Oli` | LimX | 2025 | 論文 | [論文](https://arxiv.org/abs/2601.10365)&nbsp;·&nbsp;[結果 (zh)](https://www.sfccn.com/2026/1-1/5NMDE0NzNfMjA5MzM5NA.html) |
| <a id="p-rl-bipedal-locomotion"></a>**RL Bipedal Locomotion**：南方科技大学 ACR2025 授業課題：Isaac Lab での学習・再生・デプロイ | `TRON1`&nbsp;*sim* | [81578823 (SUSTech)](https://github.com/81578823) | 2025 | コード | [コード](https://github.com/81578823/RL_bipedal_locomotion_Isaaclab) |
| <a id="p-pointfootgym"></a>**pointfootGym**：南方科技大学 CLEAR Lab によるポイントフット学習テンプレート、Isaac Gym と legged_gym | `TRON1`&nbsp;*sim* | [Haokai Su (SUSTech CLEAR Lab)](https://github.com/SuDaxia-kai) | 2024 | コード | [コード](https://github.com/SuDaxia-kai/pointfootGym) |

## 産業応用

_34 件（6 グループ）_

このセクションは LimX が管理しています。公開報道、パートナーの発表、企業のオープンソースを収録し、各項目に出典リンクがあります。

### 導入事例と製品

| プロジェクト | 機種 | 作者 / 組織 | 年 | 種別 | リンク |
|---|---|---|---|---|---|
| <a id="p-tenniix-ultra-max"></a>**TENNIIX ULTRA MAX**：TRON2 ホイール脚を土台にしたテニスロボット、2026 ビリー・ジーン・キング・カップ ファイナルでプロと対戦 | `TRON2` | Enhanced Robotics (Tenniix) | 2026 | 報道 | [報道 (zh)](https://www.news.cn/sports/20260928/f1776d7ca75042568a5137e256fa9425/c.html) |
| <a id="p-zinova-tron2-construction"></a>**ZINOVA Tool Intelligence**：2 台の TRON2 が釘打ち機と鉄筋で縮小版のティルトアップ工法を実演 | `TRON2` | ZINOVA, RIC Robotics | 2026 | 報道 | [動画](https://www.youtube.com/watch?v=8KDxnT-4zl0)&nbsp;·&nbsp;[報道](https://www.equipmentworld.com/technology/article/15836367/zinova-limx-bring-toolwielding-robots-to-construction) |
| <a id="p-dongtu-domestic-architecture"></a>**国産電子アーキテクチャのヒューマノイド**：東土科技の Intewell OS と AUTBUS を搭載した Oli、LimX は東土主導のアーキテクチャ連盟にも参加 | `Oli` | 東土科技（Kyland） | 2026 | 報道 | [報道 (zh, WeChat)](http://mp.weixin.qq.com/s?__biz=Mzk0NDU5NjMwMA==&mid=2247495106&idx=1&sn=8b5ffd05d0615a0581d3b23a18f2d830&chksm=c20243eecd5be209a820feecab39fcb0480f5ec903b40f0d655db8f6225b378bd0e8f1db3a1a)&nbsp;·&nbsp;[報道 (zh, 21世紀経済報道)](https://m.21jingji.com/article/20260929/herald/af2d0b02d6e7593ed4a2af7d05a191b5.html)&nbsp;·&nbsp;[報道 (zh, 四川在線)](https://cbgc.scol.com.cn/news/8010385) |
| <a id="p-wuji-hand-2-pharmacy-demo"></a>**Wuji Hand 2 Pharmacy Demo**：WUJI TECH の Wuji Hand 2 を付けた TRON2 が生薬をつかみ、量り、挽き、包む | `TRON2` | WUJI TECH | 2026 | 報道 | [報道](https://robotstart.info/article/2026/08/26/382326.html) |
| <a id="p-d-robotics-rdk-s100-tron1"></a>**RDK S100 on TRON1**：ポイントフットの歩行ポリシーを D-Robotics RDK S100 の BPU に移植、公式応用事例 | `TRON1` | D-Robotics | 2025 | 報道 | [報道 (zh)](https://forum.d-robotics.cc/t/topic/28833) |

### 企業のオープンソース

| プロジェクト | 機種 | 作者 / 組織 | 年 | 種別 | リンク |
|---|---|---|---|---|---|
| <a id="p-xense-openpi-for-tron2"></a>**Xense OpenPI**：双腕操作向けの Pi0.5 学習設定とリアルタイム推論 | `TRON2` | [Xense Robotics](https://github.com/XenseRobotics-AI) | 2026 | コード | [コード](https://github.com/XenseRobotics-AI/xense-openpi) |
| <a id="p-crest-tron2-description"></a>**TRON2 Description, Crest edition**：SFYG アームの手首カメラマウントに合わせて調整したロボットモデル | `TRON2` | [Crest Robotics](https://github.com/Crest-Robotics) | 2026 | コード | [コード](https://github.com/Crest-Robotics/tron2-robot-description) |
| <a id="p-artefacts-tron1-nav2-newton"></a>**TRON1 Nav2 in Newton**：Newton 物理シミュレータでの Nav2 経路追従テスト | `TRON1`&nbsp;*sim* | [Artefacts](https://github.com/art-e-fact) | 2026 | コード | [コード](https://github.com/art-e-fact/tron-navigation-demo) |
| <a id="p-xense-pico4-teleoperator"></a>**LeRobot Pico4 Teleoperator**：LeRobot 用の PICO 4 双腕遠隔操作プラグイン、TRON2 に対応 | `TRON2` | [Xense Robotics](https://github.com/XenseRobotics-AI) | 2026 | コード | [コード](https://github.com/XenseRobotics-AI/lerobot-teleoperator-pico4) |
| <a id="p-safesentinel-sonic-for-oli"></a>**SONIC Training for Oli**：31 自由度モデルで GEAR-SONIC 全身制御を学習、PICO VR 遠隔操作対応 | `Oli`&nbsp;*sim* | [SafeSentinel](https://github.com/safe-sentinel-co) | 2026 | コード | [コード](https://github.com/safe-sentinel-co/hu_d04_sonic_setup) |
| <a id="p-anima-ros2-sim-net"></a>**ANIMA ROS 2 Simulation Network**：TRON1 二足モデルを同梱した ROS 2 と Gazebo のシミュレーションスタック | `TRON1`&nbsp;*sim* | [RobotFlow Labs](https://github.com/RobotFlow-Labs) | 2026 | コード | [コード](https://github.com/RobotFlow-Labs/anima-ros2-sim-net) |
| <a id="p-artefacts-tron1-workspace"></a>**TRON1 Artefacts Workspace**：Artefacts ロボットテスト基盤を使った ROS 2 と Gazebo のデモ | `TRON1`&nbsp;*sim* | [Artefacts](https://github.com/art-e-fact) | 2026 | コード | [コード](https://github.com/art-e-fact/tron1-artefacts) |
| <a id="p-openmind-om1-sim"></a>**OM1-sim**：ロボット OS「OM1」向け Isaac Sim 環境、ホイールフット TRON1・Go2・G1 に対応 | `TRON1`&nbsp;*sim* | [OpenMind](https://github.com/OpenMind) | 2026 | コード | [コード](https://github.com/OpenMind/OM1-sim) |
| <a id="p-phanthy-motus-driver"></a>**Phanthy Motus Drivers**：4Paradigm の具身 AI 基盤 Phanthy Motus のハードウェアドライバ、TRON2 双腕に対応 | `TRON2` | [4Paradigm](https://github.com/4paradigm) | 2026 | コード | [コード](https://github.com/4paradigm/phanthymotus-driver) |
| <a id="p-xense-tron2-pnp-dataset"></a>**Xense TRON2 Pick-and-Place Dataset**：触覚映像付きの遠隔操作 115 エピソード、Voxel51 が FiftyOne 形式でも公開 | `TRON2` | [Xense Robotics](https://huggingface.co/Xense) | 2026 | コード | [データセット](https://huggingface.co/datasets/Xense/tron2rt-pnp-0918)&nbsp;·&nbsp;[データセット (Voxel51)](https://huggingface.co/datasets/Voxel51/xense-tron2rt-pnp-115ep) |
| <a id="p-anima-ros2-bridge"></a>**ANIMA ROS 2 Bridge**：AI エージェントと ROS 2 ロボットをつなぐ DDS / WebSocket ブリッジ、LimX 機を自動識別し TRON1 モデルを同梱 | `TRON1`&nbsp;*sim* | [RobotFlow Labs](https://github.com/RobotFlow-Labs) | 2026 | コード | [コード](https://github.com/RobotFlow-Labs/anima-ros2-bridge) |
| <a id="p-cmriat-citadel"></a>**Citadel**：HDF5 の記録を LeRobot v2.1 に一括変換するロボットデータ管理ツール、例に TRON2 のデータを使用 | `TRON2` | [China Merchants Research Institute of Advanced Technology](https://github.com/cmriat) | 2026 | コード | [コード](https://github.com/cmriat/Citadel) |
| <a id="p-openmind-brainpack"></a>**OpenMind BrainPack**：TRON1、Unitree G1、Go2 に対応するモジュール式コンピュート・開発バックパック | `TRON1` | [OpenMind](https://github.com/OpenMind) | 2025 | コード | [コード](https://github.com/OpenMind/brainpack) |

### 商業公演とイベント

| プロジェクト | 機種 | 作者 / 組織 | 年 | 種別 | リンク |
|---|---|---|---|---|---|
| <a id="p-nio-gba-auto-show"></a>**粤港澳大湾区モーターショー NIO ブース**：NIO ブースで Oli と Luna がインタラクティブなデモ | `Oli` `Luna` | NIO | 2026 | 報道 | [報道 (zh)](https://news.ifeng.com/c/8vmGa3sP4u7) |
| <a id="p-kill-it-finale"></a>**「キル・イット」決勝**：デザイナー キム・ナラの優勝決勝ステージに Luna が登場、tvN | `Luna` | tvN、キム・ナラ | 2026 | 報道 | [報道 (ko)](https://isplus.com/article/view/isp202607290025) |
| <a id="p-taobao-influencer-festival"></a>**淘宝インフルエンサーフェスティバル**：上海で俳優 ミシェル・チェンと Luna がランウェイを歩行 | `Luna` | 淘宝 | 2026 | 報道 | [報道](https://interestingengineering.com/ai-robotics/video-china-humanoid-catwalk-taobao-festival) |
| <a id="p-luna-china-gt-opening"></a>**2026 CHINA GT opening ceremony**：5 台の Luna が CHINA GT 選手権の開幕式で自律型グループダンスを披露 | `Luna` | CHINA GT | 2026 | 報道 | [報道](https://robotstart.info/article/2026/09/18/382434.html) |

### 戦略提携

| プロジェクト | 機種 | 作者 / 組織 | 年 | 種別 | リンク |
|---|---|---|---|---|---|
| <a id="p-smartcube-partnership"></a>**SmartCube**：韓国の公式パートナー、工場やエネルギー施設の点検にヒューマノイドとデジタルツインを活用 | — | SmartCube（韓国） | 2026 | 報道 | [報道 (ko)](https://www.aipostkorea.com/news/articleView.html?idxno=12727) |
| <a id="p-guangyang-partnership"></a>**光洋股份**：一体型関節モジュールを共同開発、軸受・歯車・減速機・ドライバーを含む（サプライチェーン連携） | — | 光洋股份 | 2026 | 報道 | [報道 (zh, NBD)](https://www.nbd.com.cn/articles/2026-03-09/4285402.html)&nbsp;·&nbsp;[報道 (zh, 東方財富)](https://finance.eastmoney.com/a/202603093666208673.html) |
| <a id="p-nbpu-industry-college"></a>**Ningbo Polytechnic University**：エンボディド AI の共同産業学院、Oli を中核の教育プラットフォームに採用 | `Oli` | 寧波職業技術大学 | 2026 | 報道 | [報道 (zh)](https://www.nbpu.edu.cn/2026/0612/c2654a6462855/page.htm) |
| <a id="p-saic-beijing-joint-lab"></a>**上汽北京 共同ラボ**：自動車製造向けのエンボディドAI共同ラボ、LimX は SAIC 初のエンボディドAI戦略パートナー | — | 上汽北京 | 2025 | 報道 | [報道 (zh)](https://www.pingwest.com/a/306356) |

### 地域パートナーと販売チャネル

| プロジェクト | 機種 | 作者 / 組織 | 年 | 種別 | リンク |
|---|---|---|---|---|---|
| <a id="p-knoxlabs-data-collection"></a>**Knoxlabs**：米国で TRON2 と Oli のバンドルを販売、データ収集向け遠隔操作のセットアップを提供 | `TRON2` `Oli` | Knoxlabs | 2026 | 報道 | [報道](https://www.knoxlabs.com/blogs/articles/robot-teleoperation-data-collection-limx) |
| <a id="p-tron-kk-humanoid-si"></a>**トロン株式会社**：日本でヒューマノイドのシステムインテグレーションと Omniverse シミュレーションを提供、LimX を取り扱い | — | トロン株式会社 | 2026 | 報道 | [報道](https://tron.tokyo/en/service/limx-dynamics/) |
| <a id="p-robot-bank-japan"></a>**ロボットバンク**：TRON1、TRON2、Oli を日本国内で展開、現場導入を支援 | `TRON1` `TRON2` `Oli` | ロボットバンク | 2026 | 報道 | [報道](https://robotstart.info/article/2026/05/15/381891.html) |
| <a id="p-mybotshop-germany"></a>**MYBOTSHOP**：ドイツで P1 を販売・サポート、マニュアル、ROS 2 設定ガイド、修理サービスを提供 | `P1` | MYBOTSHOP GmbH（ドイツ） | 2026 | 報道 | [報道](https://www.docs.mybotshop.de/limx_p1.html) |
| <a id="p-synerex-korea"></a>**Synerex**：韓国の公式パートナー、Drone Show Korea 2025 で TRON1 を韓国初公開 | `TRON1` | Synerex（韓国） | 2025 | 報道 | [報道 (ko)](https://www.newswire.co.kr/newsRead.php?no=1005949) |
| <a id="p-r2c2-partnership"></a>**R2C2**：香港の公式デベロッパー兼販売代理店、強化学習ロボットを公共設備と点検業務に活用 | `W1` `P1` | R2C2 Limited（香港） | 2024 | 報道 | [発表 (LinkedIn)](https://www.linkedin.com/posts/limx-dynamics_robotics-partnership-innovation-activity-7211709457666310145-ddt9)&nbsp;·&nbsp;[発表 (X)](https://x.com/LimX_Dynamics/status/1806002749722820865) |

### 受賞と評価

| プロジェクト | 機種 | 作者 / 組織 | 年 | 種別 | リンク |
|---|---|---|---|---|---|
| <a id="p-ieee-spectrum-robot-of-the-month-tron1"></a>**IEEE Spectrum Robot of the Month**：TRON1 が IEEE Spectrum 誌の「Robot of the Month」に掲載 | `TRON1` | IEEE Spectrum | 2026 | 報道 | [報道](https://doi.org/10.1109/MSPEC.2026.11595926) |
| <a id="p-rbr50-2025-tron1"></a>**RBR50 ロボティクス・イノベーション・アワード 2025**：TRON1 がマルチモーダル二足の研究開発プラットフォームとして選出 | `TRON1` | The Robot Report | 2025 | 報道 | [結果](https://www.therobotreport.com/rbr50-company-2025/tron-1-multi-modal-biped-offers-a-unique-rd-platform/) |

## 機種別

機種ごとに専用ページがあり、その機種を使った項目をすべてまとめています： [TRON1](robots/TRON1_ja.md) · [TRON2](robots/TRON2_ja.md) · [Oli](robots/Oli_ja.md) · [Luna](robots/Luna_ja.md) · [P1](robots/P1_ja.md) · [W1](robots/W1_ja.md)

機種ごと・カテゴリごとの掲載数：

| 機種 | 合計 | 移動 | 知覚 | マニピュレーション | エンボディドAI | ツール | 教育 | 産業 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| [`TRON1`](robots/TRON1_ja.md) | **90** | 32 | 12 | 6 | 1 | 18 | 10 | 11 |
| [`TRON2`](robots/TRON2_ja.md) | **34** | 1 |  | 3 | 6 | 5 | 8 | 11 |
| [`Oli`](robots/Oli_ja.md) | **27** | 13 |  | 2 | 2 | 2 | 2 | 6 |
| [`Luna`](robots/Luna_ja.md) | **7** | 2 | 1 |  |  |  |  | 4 |
| [`P1`](robots/P1_ja.md) | **5** | 3 |  |  |  |  |  | 2 |
| [`W1`](robots/W1_ja.md) | **4** | 2 |  | 1 |  |  |  | 1 |

## コントリビュート

自薦も他薦も歓迎します。[投稿フォーム](https://github.com/limxdynamics/awesome-limx/issues/new?template=add-project.yml)、Pull Request、またはメール [opensource@limxdynamics.com](mailto:opensource@limxdynamics.com) でお送りください。英語・中国語・日本語・韓国語のどれでも構いません。収録基準は [CONTRIBUTING.md](CONTRIBUTING.md) をご覧ください。各カテゴリは年の新しい順に並んでいます。「種別」列は読者が得られるものを示します：すぐ動かせるもの（**コード**）、手順に沿って学べるもの（**チュートリアル**）、読むもの（**論文**）、メディア報道や発表（**報道**）。

掲載は LimX による推奨を意味するものではなく、権利はすべて原作者に帰属します。掲載の取り下げは、理由を問わずいつでも依頼できます。

提携・購入のお問い合わせは [opensource@limxdynamics.com](mailto:opensource@limxdynamics.com) まで。


## ライセンス

このリストは [CC0 1.0](LICENSE) で公開しています。リンク先のプロジェクトにはそれぞれのライセンスが適用されます。
