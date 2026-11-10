<p align="center"><img src="assets/banner_cn.png" alt="Awesome LimX" width="100%"></p>

<p align="center">
  <a href="README.md">English</a> | <b>中文</b> | <a href="README_ja.md">日本語</a> | <a href="README_ko.md">한국어</a>
</p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-CC0--1.0-2f6feb" alt="License: CC0-1.0"></a>
  <a href="https://github.com/limxdynamics/limxdynamics/blob/main/doc/wechat_qr.png"><img src="https://img.shields.io/badge/%E5%BE%AE%E4%BF%A1-%E5%BC%80%E5%8F%91%E8%80%85%E7%A4%BE%E5%8C%BA-07C160?logo=wechat&logoColor=white" alt="微信开发者社区"></a>
</p>

> 收录 **95** 个项目，其中 **61** 个有开源代码，都基于 LimX 机器人或 LimX SDK：论文、代码、数据集、教程、比赛成绩和行业应用。官方开源请见 [GitHub](https://github.com/limxdynamics) 和 [Hugging Face](https://huggingface.co/limxdynamics)。

## 目录

- [动手之前](#动手之前)
- [运动控制](#运动控制) — 32
  - [地形与感知行走](#地形与感知行走)
  - [强化学习训练与部署](#强化学习训练与部署)
  - [基于模型的控制](#基于模型的控制)
  - [动作跟踪与重定向](#动作跟踪与重定向)
- [感知与导航](#感知与导航) — 5
- [操作](#操作) — 9
- [具身智能](#具身智能) — 7
- [工具、仿真与 SDK](#工具仿真与-sdk) — 19
  - [训练框架](#训练框架)
  - [仿真与环境](#仿真与环境)
  - [部署与控制](#部署与控制)
  - [模型与动作数据](#模型与动作数据)
- [教学与竞赛](#教学与竞赛) — 9
- [行业应用](#行业应用) — 14
  - [落地与产品](#落地与产品)
  - [商业演出与活动](#商业演出与活动)
  - [战略合作](#战略合作)
  - [区域伙伴与渠道](#区域伙伴与渠道)
  - [奖项与认可](#奖项与认可)
- [按机型查找](#按机型查找): [TRON1](robots/TRON1_cn.md) · [TRON2](robots/TRON2_cn.md) · [Oli](robots/Oli_cn.md) · [Luna](robots/Luna_cn.md) · [P1](robots/P1_cn.md) · [W1](robots/W1_cn.md)
- [参与贡献](#参与贡献)

<sub>**代码** 可以直接跑 · **教程** 可以跟着学 · **论文** 可以阅读 · *仿真* 只在仿真中展示过，其余都在实机上运行过</sub>

## 动手之前

下面的条目都建立在这四步之上。刚开始的话，先按顺序走一遍——这些是我们自己维护的仓，不是社区项目。

| 步骤 | 需要什么 | 从哪拿 |
|---|---|---|
| 1 · 模型 | 机器人的 URDF、MJCF 和 USD | [TRON1](https://github.com/limxdynamics/tron1-robot-description) · [TRON2](https://github.com/limxdynamics/tron2-robot-description) · [Oli](https://github.com/limxdynamics/humanoid-description) · [Luna](https://github.com/limxdynamics/luna-description) |
| 2 · 接口 | 低层运动 SDK、ROS 2 | [limxsdk-lowlevel](https://github.com/limxdynamics/limxsdk-lowlevel) |
| 3 · 训练 | Isaac Lab、Isaac Gym、MuJoCo | [tron1-rl-isaaclab](https://github.com/limxdynamics/tron1-rl-isaaclab) · [tron2_rl_lab](https://github.com/limxdynamics/tron2_rl_lab) · [tron1-mujoco-sim](https://github.com/limxdynamics/tron1-mujoco-sim) |
| 4 · 部署 | ONNX 推理、ROS 2、C++ | [tron1-rl-deploy-python](https://github.com/limxdynamics/tron1-rl-deploy-python) · [humanoid-rl-deploy-python](https://github.com/limxdynamics/humanoid-rl-deploy-python) |

## 运动控制

_32 个条目，分 4 组：12 篇论文 · 20 个代码_

### 地形与感知行走

| 项目 | 机型 | 作者 / 机构 | 年份 | 类型 | 链接 |
|---|---|---|---|---|---|
| <a id="p-ame-2"></a>**AME-2**：敏捷感知运动 | `TRON1` | [苏黎世联邦理工 RSL](https://rsl.ethz.ch) | 2026 | 论文 | [主页](https://sites.google.com/leggedrobotics.com/ame-2)&nbsp;·&nbsp;[论文](https://arxiv.org/abs/2601.08485) |
| <a id="p-faststair"></a>**FastStair**：快速跑楼梯 | `Oli` | 哈工大、逐际动力等 | 2026 | 论文 | [主页](https://npcliu.github.io/FastStair)&nbsp;·&nbsp;[论文](https://arxiv.org/abs/2601.10365)&nbsp;·&nbsp;[视频](https://youtu.be/SoLBK7VEGDo) |
| <a id="p-steppingstonelocomotion"></a>**梅花桩行走**：跨越梅花桩，先盲走再加视觉 | `TRON1`&nbsp;*仿真* | [Yiyou6](https://github.com/Yiyou6) | 2026 | 代码 | [代码](https://github.com/Yiyou6/SteppingStoneLocomotion)&nbsp;·&nbsp;[视频](https://www.youtube.com/watch?v=vs608-L7kl0) |
| <a id="p-barlowwalk"></a>**BarlowWalk**：地形自适应运动 | `TRON1`&nbsp;*仿真* | 哈工大（深圳） | 2025 | 论文 | [论文](https://arxiv.org/abs/2508.00939) |
| <a id="p-ctbc"></a>**CTBC**：轮足盲爬台阶 | `TRON1` | 上海大学、酷哇机器人 | 2025 | 论文 | [主页](https://ctbc-for-wheeled-bipedal-robots.github.io/)&nbsp;·&nbsp;[论文](https://arxiv.org/abs/2509.02986) |
| <a id="p-ga-phl"></a>**GA-PHL**：步态自适应感知行走 | `Oli` | 中国科大、逐际动力等 | 2025 | 论文 | [主页](https://ga-phl.github.io/)&nbsp;·&nbsp;[论文](https://arxiv.org/abs/2512.07464) |
| <a id="p-lipm-guided-rl"></a>**LIPM 引导强化学习**：稳定的双足感知行走 | `TRON1` | 南科大 CLEAR 实验室、港科大等 | 2025 | 论文 | [论文](https://arxiv.org/abs/2509.09106) |
| <a id="p-vmts"></a>**VMTS**：视觉辅助多地形行走 | `P1` | 东南大学 | 2025 | 代码 | [论文](https://arxiv.org/abs/2503.07049)&nbsp;·&nbsp;[代码](https://github.com/chenfu-user/VMTS) |

### 强化学习训练与部署

| 项目 | 机型 | 作者 / 机构 | 年份 | 类型 | 链接 |
|---|---|---|---|---|---|
| <a id="p-osram"></a>**OSRAM**：在线 sim2real 自适应 | `TRON1` | [杜克大学](https://github.com/generalroboticslab) | 2026 | 代码 | [代码](https://github.com/generalroboticslab/OSRAM) |
| <a id="p-rl-tron1"></a>**rl-tron1**：Isaac Lab 师生训练框架 | `TRON1`&nbsp;*仿真* | [Jiakang Ma](https://github.com/Jiakang-Ma) | 2026 | 代码 | [代码](https://github.com/Jiakang-Ma/rl-tron1) |
| <a id="p-tron1-sliding-analysis"></a>**TRON1 打滑分析**：轮足漂移与摩擦迁移 | `TRON1`&nbsp;*仿真* | [Shukashuki](https://github.com/Shukashuki) | 2026 | 代码 | [代码](https://github.com/Shukashuki/tron1-sliding-analysis) |
| <a id="p-vaps"></a>**VAPS**：安全特技动作，实机侧空翻 | `Oli` | 达姆施塔特工业大学、逐际动力等 | 2026 | 论文 | [主页](https://vaps-r-al.github.io/)&nbsp;·&nbsp;[论文](https://arxiv.org/abs/2610.01397) |
| <a id="p-wf_tron1a-stand-still-policy"></a>**WF_TRON1A 静止站立**：原地静止站立的强化学习策略 | `TRON1`&nbsp;*仿真* | [F-Morry](https://github.com/F-Morry) | 2026 | 代码 | [代码](https://github.com/F-Morry/limx_rl) |
| <a id="p-where-to-learn"></a>**Where-to-Learn**：梯度引导的强化学习探索 | `TRON1` | 浙江大学、南方科技大学 | 2026 | 论文 | [主页](https://wheretolearn.github.io)&nbsp;·&nbsp;[论文](https://arxiv.org/abs/2603.27317)&nbsp;·&nbsp;[视频](https://www.youtube.com/watch?v=DztdUyh_LVk) |
| <a id="p-zetin-tron1-deploy"></a>**Zetin TRON1 部署**：sim2sim 与实机部署 | `TRON1` | [Chanjun Lee（首尔市立大学 Zetin）](https://github.com/chanjun-nyam) | 2026 | 代码 | [代码](https://github.com/chanjun-nyam/Zetin-Humanoid-RL-Deploy) |
| <a id="p-biped-rl-with-pathfinding"></a>**目标导向双足训练**：带路径规划的目标导向训练 | `TRON1`&nbsp;*仿真* | [shandilya1998](https://github.com/shandilya1998) | 2026 | 代码 | [代码](https://github.com/singhaman1750/biped-rl-isaaclab-iisc) |
| <a id="p-him-pim-isaac-lab"></a>**HIM-PIM Isaac Lab**：基于 HIM、PIM 的鲁棒运动控制 | `TRON1`&nbsp;*仿真* | [DongyangLin](https://github.com/DongyangLin) | 2025 | 代码 | [代码](https://github.com/DongyangLin/HIM-PIM-isaaclab) |
| <a id="p-leggedrobotslab"></a>**LeggedRobotsLab**：Go1 与 TRON1A 的 Isaac Lab 运动控制 | `TRON1`&nbsp;*仿真* | [Guohua Zhang](https://github.com/guohua-zhang) | 2025 | 代码 | [代码](https://github.com/guohua-zhang/LeggedRobotsLab) |
| <a id="p-multi-loco"></a>**Multi-Loco**：点足与轮足统一的扩散策略 | `TRON1` | 南科大 CLEAR 实验室、逐际动力等 | 2025 | 代码 | [主页](https://multi-loco.github.io)&nbsp;·&nbsp;[论文](https://arxiv.org/abs/2506.11470)&nbsp;·&nbsp;[代码](https://github.com/clearlab-sustech/multi_loco_isaacgym) |
| <a id="p-pvp"></a>**PvP**：高效的人形强化学习 | `Oli` | 香港理工、中国科大等 | 2025 | 论文 | [论文](https://arxiv.org/abs/2512.13093) |
| <a id="p-tron-camp-wheel-foot-deployment"></a>**TRON Camp 轮足部署**：轮足策略实机部署 | `TRON1` | [Yitao Zeng](https://github.com/24zen0) | 2025 | 代码 | [代码](https://github.com/24zen0/Deployment_of_wheelfoot_tron) |
| <a id="p-anybipe"></a>**AnyBipe**：大模型引导的双足训练与部署 | `TRON1` | [上海交通大学](https://github.com/sjtu-mvasl-robotics) | 2024 | 代码 | [代码](https://github.com/sjtu-mvasl-robotics/AnyBipe) |
| <a id="p-cts"></a>**CTS**：并行师生强化学习 | `P1` | 南科大 CLEAR 实验室、浙大-UIUC等 | 2024 | 论文 | [主页](https://clearlab-sustech.github.io/concurrentTS/)&nbsp;·&nbsp;[论文](https://arxiv.org/abs/2405.10830) |

### 基于模型的控制

| 项目 | 机型 | 作者 / 机构 | 年份 | 类型 | 链接 |
|---|---|---|---|---|---|
| <a id="p-whole-body-humanoid-mpc"></a>**人形全身 MPC**：31 自由度 Oli 上的全身非线性 MPC | `Oli`&nbsp;*仿真* | [Tianxing Liu](https://github.com/liuskywalkerjskd) | 2026 | 代码 | [代码](https://github.com/liuskywalkerjskd/humanoid_mpc) |
| <a id="p-learning-enhanced-pmp-mpc"></a>**学习增强的 PMP-MPC**：点足双足的学习增强 MPC | `TRON1`&nbsp;*仿真* | [Markwcl2004](https://github.com/Markwcl2004) | 2026 | 代码 | [论文](https://doi.org/10.1109/ASCC70886.2026.11701800)&nbsp;·&nbsp;[代码](https://github.com/Markwcl2004/PMP_based_Bipedal_MPC) |
| <a id="p-task-space-riccati-wbc"></a>**任务空间 Riccati 全身控制**：全身控制 | `P1`&nbsp;*仿真* | 南方科大、港科大等 | 2024 | 论文 | [论文](https://arxiv.org/abs/2404.00591) |
| <a id="p-bipedal-mpc"></a>**双足 MPC**：MuJoCo 中的 MPC 与全身控制 | `TRON1`&nbsp;*仿真* | [南方科技大学 CLEAR 实验室](https://github.com/clearlab-sustech) | 2024 | 代码 | [代码](https://github.com/clearlab-sustech/Bipedal_MPC) |

### 动作跟踪与重定向

| 项目 | 机型 | 作者 / 机构 | 年份 | 类型 | 链接 |
|---|---|---|---|---|---|
| <a id="p-any2any"></a>**Any2Any**：跨本体全身动作跟踪 | `Oli` `Luna` | 逐际动力 | 2026 | 代码 | [论文](https://arxiv.org/abs/2605.23733)&nbsp;·&nbsp;[代码](https://github.com/Ming827/any2any_sonic2Oli) |
| <a id="p-chip-for-oli"></a>**CHIP for Oli**：基于 mjlab 的自适应柔顺动作跟踪 | `Oli`&nbsp;*仿真* | [Matt14-mander](https://github.com/Matt14-mander) | 2026 | 代码 | [代码](https://github.com/Matt14-mander/chip-oli) |
| <a id="p-supermimic-for-oli"></a>**SuperMimic for Oli**：单策略跟踪 40 段动作 | `Oli`&nbsp;*仿真* | [Tianxing Liu](https://github.com/liuskywalkerjskd) | 2026 | 代码 | [代码](https://github.com/liuskywalkerjskd/supermimic_oli) |
| <a id="p-tron1-wf-mimic"></a>**TRON1 轮足舞蹈模仿**：舞蹈模仿与可行性分析 | `TRON1`&nbsp;*仿真* | [HUST-dolores](https://github.com/HUST-dolores) | 2026 | 代码 | [代码](https://github.com/HUST-dolores/tron1-wf-mimic) |
| <a id="p-multi-embodiment-retargeting"></a>**多本体动作重定向**：扩散模型动作重定向 | `TRON1` `Oli`&nbsp;*仿真* | 南方科大、港科大等 | 2025 | 论文 | [论文](https://arxiv.org/abs/2505.20857) |

## 感知与导航

_5 个条目，全部有代码_

| 项目 | 机型 | 作者 / 机构 | 年份 | 类型 | 链接 |
|---|---|---|---|---|---|
| <a id="p-gps-tron1"></a>**GPS-TRON1**：融合 FAST-LIO 的户外 GPS 导航 | `TRON1` | [potatoHu-a](https://github.com/potatoHu-a) | 2026 | 代码 | [代码](https://github.com/potatoHu-a/GPS-TRON1) |
| <a id="p-wf_tron1a-lidar-navigation"></a>**WF_TRON1A 激光导航**：激光里程计与导航 | `TRON1` | [F-Morry](https://github.com/F-Morry) | 2026 | 代码 | [代码](https://github.com/F-Morry/limx_ws) |
| <a id="p-tron-1-struzzo"></a>**TRON-1 Struzzo**：基于 Jetson 的自主导航 | `TRON1` | [enfff](https://github.com/enfff) | 2025 | 代码 | [代码](https://github.com/enfff/tron1-gazebo-ros2) |
| <a id="p-neupan-on-tron1"></a>**TRON1 上的 NeuPAN**：轮足上的 NeuPAN 端到端导航 | `TRON1` | [WikHClean](https://github.com/WikHClean) | 2025 | 代码 | [代码](https://github.com/WikHClean/-ROS1-NeuPAN-TRON1-) |
| <a id="p-3d-navigation-with-pct-planner"></a>**PCT 规划器 3D 导航**：楼梯 3D 导航 | `TRON1` | [81578823](https://github.com/81578823) | 2025 | 代码 | [代码](https://github.com/81578823/3D_navigation_PCTplanner) |

## 操作

_9 个条目：4 篇论文 · 5 个代码_

| 项目 | 机型 | 作者 / 机构 | 年份 | 类型 | 链接 |
|---|---|---|---|---|---|
| <a id="p-cola-on-tron2"></a>**COLA on TRON2**：人机协同搬运，TRON2 移植 | `TRON2`&nbsp;*仿真* | [Matt14-mander](https://github.com/Matt14-mander) | 2026 | 代码 | [代码](https://github.com/Matt14-mander/COLA_TRON2) |
| <a id="p-holistic-loco-manipulation"></a>**全身一体化移动操作**：TRON1 加机械臂 | `TRON1` | 浙大-UIUC、逐际动力 | 2026 | 论文 | [论文](https://arxiv.org/abs/2609.18930) |
| <a id="p-tron1-to-ur5e-bottle-transfer"></a>**TRON1 与 UR5e 交接水瓶**：ROS 2 与 MuJoCo | `TRON1`&nbsp;*仿真* | [Centaucyan](https://github.com/Centaucyan) | 2026 | 代码 | [代码](https://github.com/Centaucyan/Proj_Transferring_bottle_from_tron1_to_ur5e_in_mujoco_env) |
| <a id="p-cooperative-transportation"></a>**多机协同搬运**：两台轮足协同搬运 | `TRON1` `TRON2`&nbsp;*仿真* | [Matt14-mander](https://github.com/Matt14-mander) | 2026 | 代码 | [代码](https://github.com/Matt14-mander/Multiple_Humanoid_Cooperative_Transportation) |
| <a id="p-cwi"></a>**CWI**：全身模仿移动操作 | `Oli` | 逐际动力、港大等 | 2026 | 论文 | [主页](https://cwi-ral.github.io/CWI-RAL-Webpage/)&nbsp;·&nbsp;[论文](https://arxiv.org/abs/2606.27676) |
| <a id="p-arm-tron"></a>**Arm-TRON**：可变足型双足加机械臂 | `TRON1` | 南方科大、浙江大学等 | 2026 | 论文 | [论文](https://doi.org/10.1109/TMECH.2026.3727546) |
| <a id="p-umi-on-tron1"></a>**UMI on Tron1**：真机 TRON1 加 ARX5 机械臂部署 UMI 技能 | `TRON1` | [Czy213hd](https://github.com/Czy213hd) | 2025 | 代码 | [代码](https://github.com/Czy213hd/umi-on-tron-lab) |
| <a id="p-quest-vr-teleop-for-oli"></a>**Oli 的 Quest VR 遥操作**：Meta Quest 双臂与头部遥操作 | `Oli` | [MSTLE](https://github.com/MSTLE) | 2025 | 代码 | [代码](https://github.com/MSTLE/Limx_teleoperate-end_pose) |
| <a id="p-wheeled-quadrupedal-manipulator"></a>**轮足四足移动操作**：W1 加机械臂位姿跟踪 | `W1` | 南科大 CLEAR 实验室、浙大-UIUC等 | 2024 | 论文 | [主页](https://clearlab-sustech.github.io/RFM_loco_mani/)&nbsp;·&nbsp;[论文](https://arxiv.org/abs/2412.03012) |

## 具身智能

_7 个条目：2 篇论文 · 5 个代码_

| 项目 | 机型 | 作者 / 机构 | 年份 | 类型 | 链接 |
|---|---|---|---|---|---|
| <a id="p-fluxvla-on-tron2"></a>**在 TRON2 上部署 FluxVLA**：在自己的 TRON2 上训练部署 FluxVLA | `TRON2` | [emoPointer](https://github.com/emoPointer) | 2026 | 代码 | [代码](https://github.com/emoPointer/FluxVLA) |
| <a id="p-oli-voice-interaction"></a>**Oli 语音交互**：语音对话与动作控制 | `Oli` | [zhilin2025](https://github.com/zhilin2025) | 2026 | 代码 | [代码](https://github.com/zhilin2025/oli_audio) |
| <a id="p-hwam"></a>**HWAM**：人形世界动作模型 | `Oli` | 逐际动力 | 2026 | 论文 | [主页](https://hwam.vercel.app/)&nbsp;·&nbsp;[论文](https://arxiv.org/abs/2610.12026) |
| <a id="p-acg-wam"></a>**ACG-WAM**：灵巧手世界-动作模型 | `TRON2` | 北京理工大学、逐际动力 | 2026 | 代码 | [主页](https://RoboOpus.github.io/ACG-WAM)&nbsp;·&nbsp;[论文](https://arxiv.org/abs/2610.06965)&nbsp;·&nbsp;[代码](https://github.com/RoboOpus/ACG-WAM) |
| <a id="p-drifting-action-heads-for-gr00t-n17"></a>**GR00T 漂移动作头**：单步动作头 | `TRON2` | 浙大-UIUC、逐际动力 | 2026 | 论文 | [论文](https://arxiv.org/abs/2609.18108) |
| <a id="p-tron2-garment-feeder"></a>**TRON2 服装送料**：Pi0.5 策略 | `TRON2` | [voniu](https://huggingface.co/voniu) | 2026 | 代码 | [模型](https://huggingface.co/voniu/tron2-garment-feeder-button-pi05) |
| <a id="p-tron2-lerobot-datasets"></a>**TRON2 LeRobot 数据集**：数据集与 GR00T 微调模型 | `TRON2` | [trantor2nd](https://huggingface.co/trantor2nd) | 2026 | 代码 | [模型](https://huggingface.co/models?author=trantor2nd&search=tron2)&nbsp;·&nbsp;[数据集](https://huggingface.co/datasets?author=trantor2nd&search=tron2) |

## 工具、仿真与 SDK

_19 个工具，分 4 组_

### 训练框架

| 项目 | 机型 | 作者 / 机构 | 年份 | 链接 |
|---|---|---|---|---|
| <a id="p-tron1-isaac-lab-tasks"></a>**TRON1 Isaac Lab 任务集**：三种足型的 Isaac Lab 任务，含跳跃 | `TRON1` | [HughWang-wzy](https://github.com/HughWang-wzy) | 2026 | [代码](https://github.com/HughWang-wzy/tron1-rl-isaaclab) |
| <a id="p-tron1-rl-mjlab"></a>**tron1-rl-mjlab**：基于 mjlab 的轮足训练 | `TRON1` | [Xinchen Yao](https://github.com/hoscy) | 2025 | [代码](https://github.com/hoscy/tron1-rl-mjlab) |
| <a id="p-leggedgym-ex"></a>**LeggedGym-Ex**：支持 Genesis、Isaac Gym、Isaac Sim 的 legged_gym | `TRON1` | [Yasen Jia](https://github.com/lupinjia) | 2024 | [代码](https://github.com/lupinjia/LeggedGym-Ex) |
| <a id="p-bipedal_locomotion_isaaclab"></a>**bipedal_locomotion_isaaclab**：Isaac Lab 训练与实机部署 | `TRON1` | [Andy-xiong6（南方科大）](https://github.com/Andy-xiong6) | 2024 | [代码](https://github.com/Andy-xiong6/bipedal_locomotion_isaaclab) |

### 仿真与环境

| 项目 | 机型 | 作者 / 机构 | 年份 | 链接 |
|---|---|---|---|---|
| <a id="p-tron2-wuji-bag-replay"></a>**tron2-wuji-bag-replay**：在 Isaac Sim 中回放 TRON2 与 Wuji 灵巧手轨迹 | `TRON2` | [zengxiong111](https://github.com/zengxiong111) | 2026 | [代码](https://github.com/zengxiong111/tron2-wuji-bag-replay) |
| <a id="p-metalsim"></a>**MetalSim**：Apple 芯片仿真器，含 TRON1 场景 | `TRON1` | [Aditya Pulipaka](https://github.com/pulipakaa24) | 2026 | [代码](https://github.com/pulipakaa24/MetalSim) |
| <a id="p-robot-sim-docker"></a>**robot-sim-docker**：LimX Gazebo、Isaac Lab、MuJoCo 容器环境 | `TRON1` | [Aklva](https://github.com/Aklva) | 2026 | [代码](https://github.com/Aklva/robot-sim-docker) |
| <a id="p-limx-robotics-mcp"></a>**limx-robotics-mcp**：仿真与控制的 MCP 服务器 | `TRON1` `Oli` | [sandraschi](https://github.com/sandraschi) | 2026 | [代码](https://github.com/sandraschi/limx-robotics-mcp) |
| <a id="p-tron_docker_sim"></a>**tron_docker_sim**：Gazebo 仿真 Docker 环境 | `TRON1` | [The-RoboTUM](https://github.com/The-RoboTUM) | 2026 | [代码](https://github.com/The-RoboTUM/tron_docker_sim) |
| <a id="p-arc-bridge"></a>**ARC Bridge**：控制器到 MuJoCo 的桥接，支持 TRON1 | `TRON1` | [密歇根大学 ARCaD 实验室](https://github.com/ARCaD-Lab-UM) | 2024 | [代码](https://github.com/ARCaD-Lab-UM/arc-bridge) |

### 部署与控制

| 项目 | 机型 | 作者 / 机构 | 年份 | 链接 |
|---|---|---|---|---|
| <a id="p-tron2_camera_calibration"></a>**tron2_camera_calibration**：TRON2 头部与腕部相机标定工具 | `TRON2` | [zengxiong111](https://github.com/zengxiong111) | 2026 | [代码](https://github.com/zengxiong111/tron2_camera_calibration) |
| <a id="p-tron1_wheel_gui"></a>**tron1_wheel_gui**：实机 TRON1 的 Qt 控制面板 | `TRON1` | [Yang Zhuqi](https://github.com/Y20-code-cpu) | 2026 | [代码](https://github.com/Y20-code-cpu/tron1_wheel_gui) |
| <a id="p-wf_tron1b_deploy"></a>**wf_tron1b_deploy**：深度感知策略 sim2sim 部署 | `TRON1` | [Leixin Chang](https://github.com/Leixinjonaschang) | 2026 | [代码](https://github.com/Leixinjonaschang/wf_tron1b_deploy) |
| <a id="p-tron_deploy"></a>**Tron_Deploy**：在 Windows 上部署策略 | `TRON1` | [candi4](https://github.com/candi4) | 2026 | [代码](https://github.com/candi4/Tron_Deploy) |
| <a id="p-crl-humanoid-ros"></a>**CRL Humanoid ROS**：支持 G1 与 TRON1A 的 ROS 2 框架 | `TRON1` | [Jin Cheng（苏黎世联邦理工 CRL）](https://github.com/catachiii) | 2025 | [代码](https://github.com/catachiii/crl-humanoid-ros) |

### 模型与动作数据

| 项目 | 机型 | 作者 / 机构 | 年份 | 链接 |
|---|---|---|---|---|
| <a id="p-rimkit"></a>**RIMKit**：接触感知动作重定向，支持 Oli | `Oli` | [Taemoon Jeong](https://github.com/tmjeong1103) | 2026 | [代码](https://github.com/tmjeong1103/RIMKit) |
| <a id="p-tron2_revo3_description"></a>**tron2_revo3_description**：TRON2 加 BrainCo Revo3 灵巧手模型 | `TRON2` | [ENDLESS0321](https://github.com/ENDLESS0321) | 2026 | [代码](https://github.com/ENDLESS0321/tron2_revo3_description) |
| <a id="p-robot_descriptionspy"></a>**robot_descriptions.py**：一行代码加载 TRON1、TRON2、Oli、Luna 模型 | `TRON1` `TRON2` `Oli` `Luna` | [robot-descriptions](https://github.com/robot-descriptions) | 2026 | [代码](https://github.com/robot-descriptions/robot_descriptions.py) |
| <a id="p-limx-3d-measurement-workbench"></a>**limx-3d-measurement-workbench**：浏览 TRON 模型、测量尺寸 | `TRON1` `TRON2` | [voniu](https://github.com/voniu) | 2026 | [代码](https://github.com/voniu/limx-3d-measurement-workbench) |

## 教学与竞赛

_9 个条目：1 篇论文 · 7 个代码 · 1 个教程_

| 项目 | 机型 | 作者 / 机构 | 年份 | 类型 | 链接 |
|---|---|---|---|---|---|
| <a id="p-atec-2026-simulation-challenge"></a>**ATEC 2026 仿真挑战赛**：官方赛题，含 TRON1、TRON2A 赛道 | `TRON1` `TRON2`&nbsp;*仿真* | [ATEC](https://github.com/atecup) | 2026 | 代码 | [代码](https://github.com/atecup/ATEC2026_Simulation_Challenge) |
| <a id="p-troncamp-2026-mani-solution"></a>**TRONCamp 2026 操作赛方案**：ACT 双臂操作 | `TRON2`&nbsp;*仿真* | [han-xudong](https://github.com/han-xudong) | 2026 | 代码 | [代码](https://github.com/han-xudong/troncamp-mani) |
| <a id="p-troncamp-2026-locomotion-solution"></a>**TRONCamp 2026 运动赛方案**：SFYG TRON2A 强化学习策略 | `TRON2`&nbsp;*仿真* | [han-xudong](https://github.com/han-xudong) | 2026 | 代码 | [代码](https://github.com/han-xudong/troncamp-locomotion) |
| <a id="p-study_tron1"></a>**study_tron1**：环境搭建与学习笔记 | `TRON1`&nbsp;*仿真* | [beamkeerati](https://github.com/beamkeerati) | 2026 | 代码 | [代码](https://github.com/beamkeerati/study_tron1) |
| <a id="p-openarm-mobile-manipulation-lab"></a>**OpenArm 移动操作实训**：TRON1 加 OpenArm 双臂，大模型任务（韩语） | `TRON1`&nbsp;*仿真* | [aha645](https://github.com/aha645) | 2026 | 代码 | [代码](https://github.com/aha645/openarms_llm_ex) |
| <a id="p-limx-tron1-learning"></a>**LimX Tron1 Learning**：Isaac Lab 交互式教程 | `TRON1`&nbsp;*仿真* | [jessiezhg](https://huggingface.co/jessiezhg) | 2026 | 教程 | [教程](https://huggingface.co/spaces/jessiezhg/LimX-Tron1-Learning) |
| <a id="p-canton-tower-robot-climbing-challenge"></a>**广州塔机器人登高挑战赛**：冠军及最佳精准控制奖，采用 FastStair | `Oli` | 逐际动力 | 2025 | 论文 | [论文](https://arxiv.org/abs/2601.10365)&nbsp;·&nbsp;[成绩](https://www.sfccn.com/2026/1-1/5NMDE0NzNfMjA5MzM5NA.html) |
| <a id="p-rl-bipedal-locomotion"></a>**双足运动强化学习**：南方科大 ACR2025 课程项目 | `TRON1`&nbsp;*仿真* | [81578823（南方科大）](https://github.com/81578823) | 2025 | 代码 | [代码](https://github.com/81578823/RL_bipedal_locomotion_Isaaclab) |
| <a id="p-pointfootgym"></a>**pointfootGym**：Isaac Gym 课程模板 | `TRON1`&nbsp;*仿真* | [Haokai Su（南方科大 CLEAR 实验室）](https://github.com/SuDaxia-kai) | 2024 | 代码 | [代码](https://github.com/SuDaxia-kai/pointfootGym) |

## 行业应用

_14 个条目，分 5 组_

### 落地与产品

| 项目 | 机型 | 作者 / 机构 | 年份 | 类型 | 链接 |
|---|---|---|---|---|---|
| <a id="p-tenniix-ultra-max"></a>**TENNIIX ULTRA MAX**：以 TRON2 轮足为底盘的网球机器人，在 2026 比莉·简·金杯总决赛与职业选手对打 | `TRON2` | 英汉思动力（Tenniix） | 2026 | 论文 | [报道](https://www.news.cn/sports/20260928/f1776d7ca75042568a5137e256fa9425/c.html) |
| <a id="p-zinova-tron2-construction"></a>**ZINOVA Tool Intelligence**：两台 TRON2 用钉枪和钢筋完成缩比混凝土预制墙施工 | `TRON2` | ZINOVA、RIC Robotics | 2026 | 论文 | [视频](https://www.youtube.com/watch?v=8KDxnT-4zl0)&nbsp;·&nbsp;[报道](https://www.equipmentworld.com/technology/article/15836367/zinova-limx-bring-toolwielding-robots-to-construction) |
| <a id="p-dongtu-domestic-architecture"></a>**国产电子架构人形机器人**：Oli 搭载东土 Intewell 操作系统与 AUTBUS 总线，双方联合发布 | `Oli` | 东土科技 | 2026 | 论文 | [报道](http://mp.weixin.qq.com/s?__biz=Mzk0NDU5NjMwMA==&mid=2247495106&idx=1&sn=8b5ffd05d0615a0581d3b23a18f2d830&chksm=c20243eecd5be209a820feecab39fcb0480f5ec903b40f0d655db8f6225b378bd0e8f1db3a1a)&nbsp;·&nbsp;[报道](https://m.21jingji.com/article/20260929/herald/af2d0b02d6e7593ed4a2af7d05a191b5.html) |

### 商业演出与活动

| 项目 | 机型 | 作者 / 机构 | 年份 | 类型 | 链接 |
|---|---|---|---|---|---|
| <a id="p-nio-gba-auto-show"></a>**大湾区车展蔚来展台**：Oli 与 Luna 在蔚来展台做互动展示 | `Oli` `Luna` | 蔚来 | 2026 | 论文 | [报道](https://news.ifeng.com/c/8vmGa3sP4u7) |
| <a id="p-kill-it-finale"></a>**《Kill It》时装真人秀总决赛**：Luna 登上设计师金娜拉的夺冠决赛舞台（tvN） | `Luna` | tvN、金娜拉 | 2026 | 论文 | [报道](https://isplus.com/article/view/isp202607290025)&nbsp;·&nbsp;[报道](https://mikekalil.com/blog/the-rise-of-limx-dynamics/) |
| <a id="p-taobao-influencer-festival"></a>**淘宝达人节**：Luna 与演员陈意涵在上海同走 T 台 | `Luna` | 淘宝 | 2026 | 论文 | [报道](https://mikekalil.com/blog/limx-dynamics-luna-humanoid-robot/) |

### 战略合作

| 项目 | 机型 | 作者 / 机构 | 年份 | 类型 | 链接 |
|---|---|---|---|---|---|
| <a id="p-smartcube-partnership"></a>**SmartCube**：韩国官方合作伙伴，人形机器人用于工厂与能源现场巡检并接入数字孪生 | — | SmartCube（韩国） | 2026 | 论文 | [报道](https://www.aipostkorea.com/news/articleView.html?idxno=12727) |
| <a id="p-guangyang-partnership"></a>**光洋股份**：联合开发一体化关节模组，涵盖轴承、齿轮、减速机和驱动器（供应链合作） | — | 光洋股份 | 2026 | 论文 | [报道](https://www.nbd.com.cn/articles/2026-03-09/4285402.html)&nbsp;·&nbsp;[报道](https://finance.eastmoney.com/a/202603093666208673.html) |
| <a id="p-saic-beijing-joint-lab"></a>**上汽北京联合实验室**：面向汽车制造的具身智能联合实验室，逐际动力为上汽首家具身智能战略合作伙伴 | — | 上汽北京 | 2025 | 论文 | [报道](https://www.pingwest.com/a/306356) |

### 区域伙伴与渠道

| 项目 | 机型 | 作者 / 机构 | 年份 | 类型 | 链接 |
|---|---|---|---|---|---|
| <a id="p-knoxlabs-data-collection"></a>**Knoxlabs**：在美国销售 TRON2 与 Oli 套装，提供数据采集用遥操作部署 | `TRON2` `Oli` | Knoxlabs | 2026 | 论文 | [主页](https://www.knoxlabs.com/blogs/articles/robot-teleoperation-data-collection-limx) |
| <a id="p-tron-kk-humanoid-si"></a>**TRON K.K.**：在日本提供人形机器人系统集成与 Omniverse 仿真，合作品牌包括 LimX | — | TRON K.K.（日本） | 2026 | 论文 | [主页](https://tron.tokyo/en/service/limx-dynamics/) |
| <a id="p-synerex-korea"></a>**Synerex**：韩国官方合作伙伴，在 2025 韩国无人机展首次在韩展出 TRON1 | `TRON1` | Synerex（韩国） | 2025 | 论文 | [报道](https://www.newswire.co.kr/newsRead.php?no=1005949) |
| <a id="p-r2c2-partnership"></a>**R2C2**：香港官方开发者与分销商，把强化学习机器人用于公用设施与巡检 | `W1` `P1` | R2C2 Limited（香港） | 2024 | 论文 | [报道](https://www.linkedin.com/posts/limx-dynamics_robotics-partnership-innovation-activity-7211709457666310145-ddt9) |

### 奖项与认可

| 项目 | 机型 | 作者 / 机构 | 年份 | 类型 | 链接 |
|---|---|---|---|---|---|
| <a id="p-rbr50-2025-tron1"></a>**2025 RBR50 机器人创新奖**：TRON1 作为多形态双足研发平台入选 | `TRON1` | The Robot Report | 2025 | 论文 | [成绩](https://www.therobotreport.com/rbr50-company-2025/tron-1-multi-modal-biped-offers-a-unique-rd-platform/) |

## 按机型查找

每个机型都有单独页面，收录用到该机型的全部条目： [TRON1](robots/TRON1_cn.md) · [TRON2](robots/TRON2_cn.md) · [Oli](robots/Oli_cn.md) · [Luna](robots/Luna_cn.md) · [P1](robots/P1_cn.md) · [W1](robots/W1_cn.md)

各机型在每个分类中的条目数：

| 机型 | 合计 | 运动控制 | 感知与导航 | 操作 | 具身智能 | 工具 | 教学与竞赛 | 行业应用 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| [`TRON1`](robots/TRON1_cn.md) | **54** | 21 | 5 | 5 |  | 15 | 6 | 2 |
| [`TRON2`](robots/TRON2_cn.md) | **18** |  |  | 2 | 5 | 5 | 3 | 3 |
| [`Oli`](robots/Oli_cn.md) | **20** | 9 |  | 2 | 2 | 3 | 1 | 3 |
| [`Luna`](robots/Luna_cn.md) | **5** | 1 |  |  |  | 1 |  | 3 |
| [`P1`](robots/P1_cn.md) | **4** | 3 |  |  |  |  |  | 1 |
| [`W1`](robots/W1_cn.md) | **2** |  |  | 1 |  |  |  | 1 |

## 参与贡献

欢迎自荐，也欢迎推荐别人的工作：填写[提交表单](https://github.com/limxdynamics/awesome-limx/issues/new?template=add-project.yml)、提 Pull Request，或发邮件到 [opensource@limxdynamics.com](mailto:opensource@limxdynamics.com)。收录标准见 [CONTRIBUTING_cn.md](CONTRIBUTING_cn.md)。各分类内按时间从新到旧排列；「类型」列说明读者能拿到什么：可以直接跑的（**代码**）、可以跟着学的（**教程**），还是可以阅读的（**论文**）。

收录不代表逐际动力背书，权利归原作者所有。项目所有者可随时要求移除，无需说明理由。

合作采购请联系 [opensource@limxdynamics.com](mailto:opensource@limxdynamics.com)。


## 许可

本列表以 [CC0 1.0](LICENSE) 发布。被收录的项目仍适用其各自的许可证。
