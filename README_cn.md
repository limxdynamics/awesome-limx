<p align="center"><img src="assets/banner_cn.png" alt="Awesome LimX" width="100%"></p>

<p align="center">
  <a href="README.md">English</a> | <b>中文</b> | <a href="README_ja.md">日本語</a> | <a href="README_ko.md">한국어</a>
</p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-CC0--1.0-2f6feb" alt="License: CC0-1.0"></a>
  <a href="https://github.com/limxdynamics/limxdynamics/blob/main/doc/wechat_qr.png"><img src="https://img.shields.io/badge/%E5%BE%AE%E4%BF%A1-%E5%BC%80%E5%8F%91%E8%80%85%E7%A4%BE%E5%8C%BA-07C160?logo=wechat&logoColor=white" alt="微信开发者社区"></a>
</p>

> 收录 **161** 个项目与合作，其中 **107** 个有开源代码，都围绕 LimX 机器人或 LimX SDK：论文、代码、数据集、教程、比赛成绩和行业应用。官方开源请见 [GitHub](https://github.com/limxdynamics) 和 [Hugging Face](https://huggingface.co/limxdynamics)。

**按机型直达**

| [**TRON1**](robots/TRON1_cn.md) | [**TRON2**](robots/TRON2_cn.md) | [**Oli**](robots/Oli_cn.md) | [**Luna**](robots/Luna_cn.md) | [**P1**](robots/P1_cn.md) | [**W1**](robots/W1_cn.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 92&nbsp;条 | 35&nbsp;条 | 30&nbsp;条 | 8&nbsp;条 | 5&nbsp;条 | 4&nbsp;条 |

## 目录

- [动手之前](#动手之前)
- [运动控制](#运动控制) — 51
  - [地形与感知行走](#地形与感知行走)
  - [强化学习训练与部署](#强化学习训练与部署)
  - [基于模型的控制](#基于模型的控制)
  - [动作跟踪与重定向](#动作跟踪与重定向)
- [感知与导航](#感知与导航) — 14
- [操作](#操作) — 11
- [具身智能](#具身智能) — 9
- [工具、仿真与 SDK](#工具仿真与-sdk) — 24
  - [训练框架](#训练框架)
  - [仿真与环境](#仿真与环境)
  - [部署与控制](#部署与控制)
  - [模型与动作数据](#模型与动作数据)
- [教学与竞赛](#教学与竞赛) — 18
- [行业应用](#行业应用) — 34
  - [落地与产品](#落地与产品)
  - [企业开源项目](#企业开源项目)
  - [商业演出与活动](#商业演出与活动)
  - [战略合作](#战略合作)
  - [区域伙伴与渠道](#区域伙伴与渠道)
  - [奖项与认可](#奖项与认可)
- [按机型查找](#按机型查找)
- [参与贡献](#参与贡献)

<sub>**代码** 可以直接跑 · **教程** 可以跟着学 · **论文** 可以阅读 · **报道** 媒体报道或公告 · *仿真* 只在仿真中展示过，其余都在实机上运行过 · **—** 不针对具体机型</sub>

## 动手之前

下面的条目都建立在这四步之上。刚开始的话，先按顺序走一遍——这些是 LimX 的官方仓库，不是社区项目。

| 步骤 | 需要什么 | 从哪拿 |
|---|---|---|
| 1 · 模型 | 机器人的 URDF、MJCF 和 USD | [TRON1](https://github.com/limxdynamics/tron1-robot-description) · [TRON2](https://github.com/limxdynamics/tron2-robot-description) · [Oli](https://github.com/limxdynamics/humanoid-description) · [Luna](https://github.com/limxdynamics/luna-description) |
| 2 · 接口 | 低层运动 SDK、ROS 2 | [limxsdk-lowlevel](https://github.com/limxdynamics/limxsdk-lowlevel) |
| 3 · 训练 | Isaac Lab、Isaac Gym、MuJoCo | [TRON1](https://github.com/limxdynamics/tron1-rl-isaaclab) · [TRON2](https://github.com/limxdynamics/tron2_rl_lab) · [Oli](https://github.com/limxdynamics/humanoid-rl-isaaclab) · [Luna](https://github.com/limxdynamics/luna-beyondmimic)<br>MuJoCo 仿真验证：[TRON1](https://github.com/limxdynamics/tron1-mujoco-sim) · [TRON2](https://github.com/limxdynamics/tron2_mujoco_sim) · [Oli](https://github.com/limxdynamics/humanoid-mujoco-sim) |
| 4 · 部署 | ONNX 推理、ROS 2、C++ | [TRON1](https://github.com/limxdynamics/tron1-rl-deploy-python) · [TRON2](https://github.com/limxdynamics/tron2_rl_deploy_python) · [Oli](https://github.com/limxdynamics/humanoid-rl-deploy-python) · Luna：暂未公开部署仓库 |

**用 LimX 机器人做出过东西？** 欢迎加到这个清单里 —— [提交项目](https://github.com/limxdynamics/awesome-limx/issues/new?template=add-project.yml)（给个链接就够了），或先看[贡献说明](CONTRIBUTING_cn.md)。只放链接，代码留在你自己的仓里。

## 运动控制

_51 个条目，分 4 组：20 篇论文 · 31 个代码_

### 地形与感知行走

| 项目 | 机型 | 作者 / 机构 | 年份 | 类型 | 链接 |
|---|---|---|---|---|---|
| <a id="p-ame-2"></a>**AME-2**：基于注意力的地图编码，实现稀疏落脚点地形上敏捷、可泛化的感知运动 | `TRON1` | [苏黎世联邦理工 RSL](https://rsl.ethz.ch) | 2026 | 论文 | [主页](https://sites.google.com/leggedrobotics.com/ame-2)&nbsp;·&nbsp;[论文](https://arxiv.org/abs/2601.08485) |
| <a id="p-faststair"></a>**FastStair**：把基于模型的落脚点规划与强化学习结合，学会快速跑上楼梯 | `Oli` | 哈工大、逐际动力等 | 2026 | 论文 | [主页](https://npcliu.github.io/FastStair)&nbsp;·&nbsp;[论文](https://arxiv.org/abs/2601.10365)&nbsp;·&nbsp;[视频](https://youtu.be/SoLBK7VEGDo) |
| <a id="p-steppingstonelocomotion"></a>**梅花桩行走**：三阶段 PPO 课程学习走过梅花桩：先盲走，再加深度视觉，最后用状态估计器 | `TRON1`&nbsp;*仿真* | [Yiyou6](https://github.com/Yiyou6) | 2026 | 代码 | [代码](https://github.com/Yiyou6/SteppingStoneLocomotion)&nbsp;·&nbsp;[视频](https://www.youtube.com/watch?v=vs608-L7kl0) |
| <a id="p-height-adjustable-wheel-legged-rl"></a>**Height-Adjustable Wheel-Legged RL**：轮足 TRON1 的地形适应与机身高度调节 | `TRON1` | 桂林电子科大、上海交大、浙大 | 2026 | 论文 | [论文](https://doi.org/10.1109/amc67705.2026.11435832) |
| <a id="p-reference-guided-stair-climbing"></a>**Reference-Guided Stair Climbing**：参考轨迹引导的强化学习，让轮足 TRON1 上楼梯，本科毕业论文 | `TRON1`&nbsp;*仿真* | 乌普萨拉大学 | 2026 | 论文 | [论文](http://urn.kb.se/resolve?urn=urn:nbn:se:uu:diva-594330) |
| <a id="p-ame-locomotion-tron2a"></a>**AME Locomotion for TRON2A**：在 Isaac Lab 中复现 AME，并新增 TRON2A 双足环境 | `TRON2`&nbsp;*仿真* | [possibleustc](https://github.com/possibleustc) | 2026 | 代码 | [代码](https://github.com/possibleustc/AME_Locomotion) |
| <a id="p-offline-visual-encoder-biped"></a>**Offline Visual Encoder for Biped Locomotion**：基于视觉的运动控制，深度到高度图编码器离线训练后冻结用于策略学习 | `TRON1` | 华中科技大学 | 2026 | 论文 | [论文](https://doi.org/10.1109/access.2026.3686506) |
| <a id="p-barlowwalk"></a>**BarlowWalk**：用 Barlow Twins 自监督学习地形表征，实现地形自适应运动 | `TRON1`&nbsp;*仿真* | 哈工大（深圳） | 2025 | 论文 | [论文](https://arxiv.org/abs/2508.00939) |
| <a id="p-ctbc"></a>**CTBC**：接触触发的盲爬楼梯方法，让轮足双足机器人从指令轨迹中学习上台阶 | `TRON1` | 上海大学、酷哇机器人 | 2025 | 论文 | [主页](https://ctbc-for-wheeled-bipedal-robots.github.io/)&nbsp;·&nbsp;[论文](https://arxiv.org/abs/2509.02986) |
| <a id="p-ga-phl"></a>**GA-PHL**：实时重建机器人脚下地形并据此调整步态节奏的感知行走 | `Oli` | 中国科大、逐际动力等 | 2025 | 论文 | [主页](https://ga-phl.github.io/)&nbsp;·&nbsp;[论文](https://arxiv.org/abs/2512.07464) |
| <a id="p-lipm-guided-rl"></a>**LIPM 引导强化学习**：借鉴线性倒立摆模型设计奖励，实现户外稳定、抗扰的感知行走 | `TRON1` | 南科大 CLEAR 实验室、港科大等 | 2025 | 论文 | [论文](https://arxiv.org/abs/2509.09106) |
| <a id="p-vmts"></a>**VMTS**：带视觉的混合专家师生强化学习，让双足机器人走过多种地形 | `P1` | 东南大学 | 2025 | 代码 | [论文](https://arxiv.org/abs/2503.07049)&nbsp;·&nbsp;[代码](https://github.com/chenfu-user/VMTS) |

### 强化学习训练与部署

| 项目 | 机型 | 作者 / 机构 | 年份 | 类型 | 链接 |
|---|---|---|---|---|---|
| <a id="p-osram"></a>**OSRAM**：在线建模闭环系统，在实机上修正 sim2real 后残留的跟踪误差 | `TRON1` | [杜克大学](https://github.com/generalroboticslab) | 2026 | 代码 | [代码](https://github.com/generalroboticslab/OSRAM) |
| <a id="p-rl-tron1"></a>**TRON1 Teacher-Student RL**：面向点足版本的 Isaac Lab 运动训练框架，采用师生结构 | `TRON1`&nbsp;*仿真* | [Jiakang Ma](https://github.com/Jiakang-Ma) | 2026 | 代码 | [代码](https://github.com/Jiakang-Ma/rl-tron1) |
| <a id="p-tron1-sliding-analysis"></a>**TRON1 打滑分析**：分析轮足策略在哪些地面摩擦下开始侧滑，并在 Isaac 与 MuJoCo 中交叉验证 | `TRON1`&nbsp;*仿真* | [Shukashuki](https://github.com/Shukashuki) | 2026 | 代码 | [代码](https://github.com/Shukashuki/tron1-sliding-analysis) |
| <a id="p-vaps"></a>**VAPS**：在翻跟头时选择继续、中止或安全倒地，实机完成侧空翻 | `Oli` | 达姆施塔特工业大学、逐际动力等 | 2026 | 论文 | [主页](https://vaps-r-al.github.io/)&nbsp;·&nbsp;[论文](https://arxiv.org/abs/2610.01397) |
| <a id="p-wf_tron1a-stand-still-policy"></a>**Wheel-Foot TRON1 Stand-Still Policy**：调整强化学习奖励，让轮足机器人在零速度指令下真正静止而不漂移 | `TRON1`&nbsp;*仿真* | [F-Morry](https://github.com/F-Morry) | 2026 | 代码 | [代码](https://github.com/F-Morry/limx_rl) |
| <a id="p-where-to-learn"></a>**Where-to-Learn**：用解析策略梯度引导 on-policy 强化学习的探索方向 | `TRON1` | 浙江大学、南方科技大学 | 2026 | 论文 | [主页](https://wheretolearn.github.io)&nbsp;·&nbsp;[论文](https://arxiv.org/abs/2603.27317)&nbsp;·&nbsp;[视频](https://www.youtube.com/watch?v=DztdUyh_LVk) |
| <a id="p-zetin-tron1-deploy"></a>**Zetin TRON1 部署**：把团队训练的策略部署到 MuJoCo 及点足、双足实机上 | `TRON1` | [Chanjun Lee（首尔市立大学 Zetin）](https://github.com/chanjun-nyam) | 2026 | 代码 | [代码](https://github.com/chanjun-nyam/Zetin-Humanoid-RL-Deploy) |
| <a id="p-biped-rl-with-pathfinding"></a>**目标导向双足训练**：带自定义目标和寻路功能的 Isaac Lab 训练环境 | `TRON1`&nbsp;*仿真* | [shandilya1998](https://github.com/shandilya1998) | 2026 | 代码 | [代码](https://github.com/singhaman1750/biped-rl-isaaclab-iisc) |
| <a id="p-sf_tron-ext-estimator"></a>**Sole-Foot TRON1 Disturbance Estimator**：在深度感知残差策略上加入基于历史的扰动估计器 | `TRON1`&nbsp;*仿真* | [EVENWaterOne](https://github.com/EVENWaterOne) | 2026 | 代码 | [代码](https://github.com/EVENWaterOne/SF_TRON_Ext-estimator) |
| <a id="p-imfs"></a>**IMFS**：在 Isaac Gym 中用世界模型规划落脚点，双足 TRON1 跟踪落脚点 | `TRON1`&nbsp;*仿真* | [Fleming-Sung](https://github.com/Fleming-Sung) | 2026 | 代码 | [代码](https://github.com/Fleming-Sung/imfs) |
| <a id="p-shape-your-body"></a>**Shape Your Body**：在 50 款足式机器人上做价值梯度构型搜索，TRON1 有专门的训练配置 | `TRON1`&nbsp;*仿真* | [nico-bohlinger](https://github.com/nico-bohlinger) | 2026 | 代码 | [代码](https://github.com/nico-bohlinger/shape-your-body) |
| <a id="p-model-based-gait-planning-rl"></a>**Model-Based Gait Planning RL**：用 3D-LIPM 参考步态代替手调步态奖励进行强化学习训练 | `TRON1` | 哈尔滨工业大学 | 2026 | 论文 | [论文](https://doi.org/10.1016/j.birob.2026.100338) |
| <a id="p-w1-parkour-legged-gym"></a>**W1 Parkour in legged_gym**：在 legged_gym 中为 W1 轮腿四足搭建跑酷与跟踪训练环境，附 ROS 控制器 | `W1`&nbsp;*仿真* | [yiqiuqwq](https://github.com/yiqiuqwq) | 2026 | 代码 | [代码](https://github.com/yiqiuqwq/wheellegged_control) |
| <a id="p-him-pim-isaac-lab"></a>**HIM-PIM Isaac Lab**：在 Isaac Lab 中对比 HIM 与 PIM 两种运动控制，测试楼梯、斜坡和外力扰动 | `TRON1`&nbsp;*仿真* | [DongyangLin](https://github.com/DongyangLin) | 2025 | 代码 | [代码](https://github.com/DongyangLin/HIM-PIM-isaaclab) |
| <a id="p-leggedrobotslab"></a>**LeggedRobotsLab**：基于 Isaac Lab 的运动训练，含 MuJoCo sim2sim 和实机部署，支持 Go1 与 TRON1 | `TRON1`&nbsp;*仿真* | [Guohua Zhang](https://github.com/guohua-zhang) | 2025 | 代码 | [代码](https://github.com/guohua-zhang/LeggedRobotsLab) |
| <a id="p-multi-loco"></a>**Multi-Loco**：用一个扩散模型策略同时控制点足和轮足机器人 | `TRON1` | 南科大 CLEAR 实验室、逐际动力等 | 2025 | 代码 | [主页](https://multi-loco.github.io)&nbsp;·&nbsp;[论文](https://arxiv.org/abs/2506.11470)&nbsp;·&nbsp;[代码](https://github.com/clearlab-sustech/multi_loco_isaacgym) |
| <a id="p-pvp"></a>**PvP**：在本体感知与特权状态之间做对比学习，提高全身控制的数据效率 | `Oli` | 香港理工、中国科大等 | 2025 | 论文 | [论文](https://arxiv.org/abs/2512.13093) |
| <a id="p-tron-camp-wheel-foot-deployment"></a>**TRON Camp 轮足部署**：为 2025 年 TRON Camp 调整轮足策略并部署到实机 | `TRON1` | [Yitao Zeng](https://github.com/24zen0) | 2025 | 代码 | [代码](https://github.com/24zen0/Deployment_of_wheelfoot_tron) |
| <a id="p-ptrl"></a>**PTRL**：在机器人之间迁移先验以缩短强化学习训练时间，在 Go2 和 TRON1 上实测 | `TRON1` | 哈工大（深圳）、苏州大学 | 2025 | 论文 | [论文](https://arxiv.org/abs/2504.05629) |
| <a id="p-anybipe"></a>**AnyBipe**：端到端框架，由大语言模型指导双足策略的奖励设计、训练和部署 | `TRON1` | [上海交通大学](https://github.com/sjtu-mvasl-robotics) | 2024 | 代码 | [代码](https://github.com/sjtu-mvasl-robotics/AnyBipe) |
| <a id="p-cts"></a>**CTS**：教师策略与学生策略同时训练的足式运动强化学习 | `P1` | 南科大 CLEAR 实验室、浙大-UIUC等 | 2024 | 论文 | [主页](https://clearlab-sustech.github.io/concurrentTS/)&nbsp;·&nbsp;[论文](https://arxiv.org/abs/2405.10830) |

### 基于模型的控制

| 项目 | 机型 | 作者 / 机构 | 年份 | 类型 | 链接 |
|---|---|---|---|---|---|
| <a id="p-whole-body-humanoid-mpc"></a>**人形全身 MPC**：面向人形移动操作的非线性全身 MPC，提供 MuJoCo 中 31 自由度 Oli 示例 | `Oli`&nbsp;*仿真* | [Tianxing Liu](https://github.com/liuskywalkerjskd) | 2026 | 代码 | [代码](https://github.com/liuskywalkerjskd/humanoid_mpc) |
| <a id="p-learning-enhanced-pmp-mpc"></a>**学习增强的 PMP-MPC**：用庞特里亚金优化器加学习残差求解质心 MPC，在 MuJoCo 中验证 | `TRON1`&nbsp;*仿真* | [Markwcl2004](https://github.com/Markwcl2004) | 2026 | 代码 | [论文](https://doi.org/10.1109/ASCC70886.2026.11701800)&nbsp;·&nbsp;[代码](https://github.com/Markwcl2004/PMP_based_Bipedal_MPC) |
| <a id="p-terrain-aware-cfr-planning"></a>**Terrain-Aware CFR Planning**：凸可行域规划上下楼梯，W1 实测 200 次全部通过 | `W1` | 南科大 CLEAR 实验室 | 2026 | 论文 | [论文](https://doi.org/10.21203/rs.3.rs-10577407/v1) |
| <a id="p-power-bounded-inverted-pendulum"></a>**Power-Bounded Inverted Pendulum**：考虑功率上限的双足最高速度模型，并据此重新整定关节电机参数 | `TRON1`&nbsp;*仿真* | 浙江大学 | 2026 | 论文 | [论文](https://doi.org/10.1007/s10409-026-25928-x) |
| <a id="p-hierarchical-nmpc-stsmc"></a>**Hierarchical NMPC + STSMC**：分层非线性 MPC 加超螺旋滑模控制，应对轮足 TRON1 的不确定性 | `TRON1`&nbsp;*仿真* | [pjmcconnellogue](https://github.com/pjmcconnellogue) | 2026 | 代码 | [代码](https://github.com/pjmcconnellogue/Hierarchical-Nonlinear-MPC-and-Super-Twisting-Sliding-Mode-Control-for-a-Wheeled-Biped-Robot-) |
| <a id="p-two-wheeled-robot-lqr"></a>**Two-Wheeled Robot LQR**：轮足 TRON1 的 LQR 与全身控制，毕业论文项目 | `TRON1`&nbsp;*仿真* | [alpttex19](https://github.com/alpttex19) | 2025 | 代码 | [代码](https://github.com/alpttex19/Two_Wheeled_Robot_LQR) |
| <a id="p-task-space-riccati-wbc"></a>**任务空间 Riccati 全身控制**：基于任务空间 Riccati 反馈的欠驱动足式机器人全身控制 | `P1`&nbsp;*仿真* | 南方科大、港科大等 | 2024 | 论文 | [论文](https://arxiv.org/abs/2404.00591) |
| <a id="p-bipedal-mpc"></a>**双足 MPC**：在 MuJoCo 中用凸 MPC 加全身控制实现行走，基于 ROS 2 | `TRON1`&nbsp;*仿真* | [南方科技大学 CLEAR 实验室](https://github.com/clearlab-sustech) | 2024 | 代码 | [代码](https://github.com/clearlab-sustech/Bipedal_MPC) |

### 动作跟踪与重定向

| 项目 | 机型 | 作者 / 机构 | 年份 | 类型 | 链接 |
|---|---|---|---|---|---|
| <a id="p-any2any"></a>**Any2Any**：把预训练的全身动作跟踪模型以少量适配迁移到新的人形机器人 | `Oli` `Luna` | 逐际动力 | 2026 | 代码 | [论文](https://arxiv.org/abs/2605.23733)&nbsp;·&nbsp;[代码](https://github.com/Ming827/any2any_sonic2Oli) |
| <a id="p-chip-for-oli"></a>**CHIP for Oli**：CHIP 自适应柔顺动作跟踪任务的移植版，在 mjlab 上训练 | `Oli`&nbsp;*仿真* | [Matt14-mander](https://github.com/Matt14-mander) | 2026 | 代码 | [代码](https://github.com/Matt14-mander/chip-oli) |
| <a id="p-supermimic-for-oli"></a>**SuperMimic for Oli**：SuperMimic 世界模型全身控制的适配版，单个策略跟踪 40 段动作 | `Oli`&nbsp;*仿真* | [Tianxing Liu](https://github.com/liuskywalkerjskd) | 2026 | 代码 | [代码](https://github.com/liuskywalkerjskd/supermimic_oli) |
| <a id="p-tron1-wf-mimic"></a>**Wheel-Foot TRON1 Dance Mimic**：在轮足双足上模仿人类舞蹈，并分析这种形态能做和做不了哪些动作 | `TRON1`&nbsp;*仿真* | [HUST-dolores](https://github.com/HUST-dolores) | 2026 | 代码 | [代码](https://github.com/HUST-dolores/tron1-wf-mimic) |
| <a id="p-robot-lab-srl-oli-mimic"></a>**Oli Mimic Tasks for robot_lab**：robot_lab 扩展，在 Isaac Lab 中加入动作模仿训练任务 | `Oli`&nbsp;*仿真* | [song-hl](https://github.com/song-hl) | 2026 | 代码 | [代码](https://github.com/song-hl/robot_lab_srl) |
| <a id="p-robot-retargeter"></a>**Robot Retargeter**：把 SMPL-X 或其他机器人的动作重定向到人形机器人，带该机型的专用配置 | `Oli`&nbsp;*仿真* | [ccrpRepo](https://github.com/ccrpRepo) | 2026 | 代码 | [代码](https://github.com/ccrpRepo/robot_retargeter) |
| <a id="p-timo"></a>**Timo**：面向文本生成动作的运动学感知多模态扩散 Transformer，生成的动作重定向后在 Oli 和 Luna 实机上执行 | `Oli` `Luna` | 逐际动力 | 2026 | 论文 | [主页](https://kyfafyd.wang/projects/timo)&nbsp;·&nbsp;[论文](https://arxiv.org/abs/2609.30761) |
| <a id="p-hu-d03-rl-mjlab"></a>**Earlier-Generation Oli RL in mjlab**：面向 HU_D03 型号的行走与动作模仿策略，在 mjlab 中训练（越南语） | `Oli`&nbsp;*仿真* | [KhanhPham248](https://github.com/KhanhPham248) | 2026 | 代码 | [代码](https://github.com/KhanhPham248/LimX_HU_D03_rl_mjlab) |
| <a id="p-robodance"></a>**RoboDance**：把网络舞蹈视频重定向到含 Oli 在内的 12 款人形机器人，在 MuJoCo 中渲染 | `Oli`&nbsp;*仿真* | [junyuan-fang](https://github.com/junyuan-fang) | 2026 | 代码 | [代码](https://github.com/junyuan-fang/robodance) |
| <a id="p-multi-embodiment-retargeting"></a>**多本体动作重定向**：以图结构为条件的扩散模型，把同一段动作重定向到结构不同的机器人上 | `TRON1` `Oli`&nbsp;*仿真* | 南方科大、港科大等 | 2025 | 论文 | [论文](https://arxiv.org/abs/2505.20857) |

## 感知与导航

_14 个条目：3 篇论文 · 11 个代码_

| 项目 | 机型 | 作者 / 机构 | 年份 | 类型 | 链接 |
|---|---|---|---|---|---|
| <a id="p-tron1_navrl"></a>**TRON1 NavRL**：在 Isaac Lab 中只用强化学习训练上层导航策略，底层沿用现有步态策略（韩语） | `TRON1`&nbsp;*仿真* | [jongbob1918](https://github.com/jongbob1918) | 2026 | 代码 | [代码](https://github.com/jongbob1918/tron1_navrl) |
| <a id="p-tron1-multi-floor-navigation"></a>**TRON1 Multi-floor Navigation**：把平地行驶、换层和上下楼梯合成一个任务（韩语） | `TRON1` | [justpastmarch](https://github.com/justpastmarch) | 2026 | 代码 | [代码](https://github.com/justpastmarch/TRON1_multifloor-navigation) |
| <a id="p-geometric-candidate-modes"></a>**Geometric Candidate Modes**：从多模态示范中学习导航，仿真训练的策略迁移到 TRON1 | `TRON1` | 俄亥俄州立大学 | 2026 | 论文 | [论文](https://arxiv.org/abs/2610.20241) |
| <a id="p-ros2_gnss_waypoint_nav"></a>**GNSS Waypoint Navigation**：基于 RTK GNSS、MID360 与 Nav2 的免建图室外航点导航，含 TRON1 底盘桥接 | `TRON1` | [武汉大学 BRAIN 实验室](https://github.com/Whu-BrainLab) | 2026 | 代码 | [代码](https://github.com/Whu-BrainLab/ros2_gnss_waypoint_nav) |
| <a id="p-lightnav-0"></a>**LightNav-0**：基于 VLM 的导航栈，含 MPC 路径跟踪与网页控制面板，适配 Go2 和 TRON1 | `TRON1` | [Light Origins](https://github.com/lightorigins) | 2026 | 代码 | [论文](https://arxiv.org/abs/2608.30935)&nbsp;·&nbsp;[代码](https://github.com/lightorigins/LightNav-0)&nbsp;·&nbsp;[模型](https://huggingface.co/LightOriginsHQ/LightNav-0) |
| <a id="p-gps-tron1"></a>**GPS-TRON1**：基于 GNSS 与 FAST-LIO 融合定位的户外航点导航，带局部防碰撞 | `TRON1` | [potatoHu-a](https://github.com/potatoHu-a) | 2026 | 代码 | [代码](https://github.com/potatoHu-a/GPS-TRON1) |
| <a id="p-wf_tron1a-lidar-navigation"></a>**Wheel-Foot TRON1 LiDAR Odometry**：外接二维激光雷达，用 RF2O 激光里程计修正单轮打滑或卡住时的轮式里程计误差 | `TRON1` | [F-Morry](https://github.com/F-Morry) | 2026 | 代码 | [代码](https://github.com/F-Morry/limx_ws) |
| <a id="p-wave-go"></a>**WAVE-Go**：世界模型动作适配的长距离导航，Go2-W 实机验证，并在 MuJoCo 中迁移到 Luna | `Luna`&nbsp;*仿真* | 北理工、港大、逐际动力等 | 2026 | 代码 | [论文](https://arxiv.org/abs/2609.18193)&nbsp;·&nbsp;[代码](https://github.com/vigorlee/wave-go) |
| <a id="p-hourglass-cross-embodiment-planning"></a>**Hourglass**：基于与机体无关的世界模型做跨机体运动规划，TRON1 是七款训练机器人之一 | `TRON1`&nbsp;*仿真* | 南洋理工大学 | 2026 | 论文 | [论文](https://arxiv.org/abs/2610.41330) |
| <a id="p-tron-1-struzzo"></a>**TRON-1 Struzzo**：用机载 Jetson 做自主导航的 Gazebo 与 ROS 2 工程 | `TRON1` | [enfff](https://github.com/enfff) | 2025 | 代码 | [代码](https://github.com/enfff/tron1-gazebo-ros2) |
| <a id="p-neupan-on-tron1"></a>**TRON1 上的 NeuPAN**：ROS 导航：A* 全局规划，NeuPAN 端到端局部避障 | `TRON1` | [WikHClean](https://github.com/WikHClean) | 2025 | 代码 | [代码](https://github.com/WikHClean/-ROS1-NeuPAN-TRON1-) |
| <a id="p-3d-navigation-with-pct-planner"></a>**PCT 规划器 3D 导航**：用 Mid360 激光雷达和 PCT 规划器在室内和楼梯上做三维导航，实机验证 | `TRON1` | [81578823](https://github.com/81578823) | 2025 | 代码 | [代码](https://github.com/81578823/3D_navigation_PCTplanner) |
| <a id="p-terrain-aware-lio-legged-wheel"></a>**Terrain-Aware LiDAR-Inertial Odometry**：面向轮足机器人的地形感知激光惯性里程计，在轮足 TRON1 上做室外实验 | `TRON1` | 上海交通大学 | 2025 | 论文 | [论文](https://arxiv.org/abs/2509.26222) |
| <a id="p-eroam"></a>**EROAM**：事件相机旋转里程计，数据集含在 TRON1 上采集的序列 | `TRON1` | [wlxing1901](https://github.com/wlxing1901) | 2024 | 代码 | [主页](https://wlxing1901.github.io/eroam/)&nbsp;·&nbsp;[论文](https://arxiv.org/abs/2411.11004)&nbsp;·&nbsp;[代码](https://github.com/wlxing1901/eroam)&nbsp;·&nbsp;[视频](https://youtu.be/8tF6b2VuvSM) |

## 操作

_11 个条目：5 篇论文 · 6 个代码_

| 项目 | 机型 | 作者 / 机构 | 年份 | 类型 | 链接 |
|---|---|---|---|---|---|
| <a id="p-cola-on-tron2"></a>**COLA on TRON2**：把 COLA 人机协同搬运从 Unitree G1 移植过来 | `TRON2`&nbsp;*仿真* | [Matt14-mander](https://github.com/Matt14-mander) | 2026 | 代码 | [代码](https://github.com/Matt14-mander/COLA_TRON2) |
| <a id="p-holistic-loco-manipulation"></a>**全身一体化移动操作**：强化学习全身控制器，把 6 自由度末端目标直接映射为加装机械臂的 TRON1 的腿臂动作 | `TRON1` | 浙大-UIUC、逐际动力 | 2026 | 论文 | [论文](https://arxiv.org/abs/2609.18930) |
| <a id="p-tron1-to-ur5e-bottle-transfer"></a>**TRON1 与 UR5e 交接水瓶**：双足机器人把瓶子送到交接区，再由 UR5e 机械臂抓取，基于 MuJoCo（韩语） | `TRON1`&nbsp;*仿真* | [Centaucyan](https://github.com/Centaucyan) | 2026 | 代码 | [代码](https://github.com/Centaucyan/Proj_Transferring_bottle_from_tron1_to_ur5e_in_mujoco_env) |
| <a id="p-cooperative-transportation"></a>**多机协同搬运**：两台机器人协同搬运同一物体，支持轮足 TRON1 和 TRON2 两种组合 | `TRON1` `TRON2`&nbsp;*仿真* | [Matt14-mander](https://github.com/Matt14-mander) | 2026 | 代码 | [代码 (TRON1)](https://github.com/Matt14-mander/Multiple_Humanoid_Cooperative_Transportation)&nbsp;·&nbsp;[代码 (TRON2)](https://github.com/Matt14-mander/tron2-cooperative-carrying) |
| <a id="p-cwi"></a>**CWI**：把动捕数据与指令结合的复合全身模仿系统，用于边走边操作 | `Oli` | 逐际动力、港大等 | 2026 | 论文 | [主页](https://cwi-ral.github.io/CWI-RAL-Webpage/)&nbsp;·&nbsp;[论文](https://arxiv.org/abs/2606.27676) |
| <a id="p-arm-tron"></a>**Arm-TRON**：单臂双足平台，可换三种足端，并为每种足端训练强化学习全身控制 | `TRON1` | 南方科大、浙江大学等 | 2026 | 论文 | [论文](https://doi.org/10.1109/TMECH.2026.3727546) |
| <a id="p-mobile-pedipulation"></a>**Mobile Pedipulation**：分层 NMPC 让轮足 TRON1 用轮腿推移物体，RA-L 论文 | `TRON1` | 密歇根大学 | 2026 | 论文 | [论文](https://arxiv.org/abs/2606.19233) |
| <a id="p-tron2-vision-teleoperation"></a>**TRON2 Vision Teleoperation**：用相机跟踪手臂和手，遥操作装有 ORCA 灵巧手的双臂机器人（西班牙语） | `TRON2`&nbsp;*仿真* | [Aremanky](https://github.com/Aremanky) | 2026 | 代码 | [代码](https://github.com/Aremanky/Teleoperacion-tron-2) |
| <a id="p-umi-on-tron1"></a>**UMI on Tron1**：用 ARX5 机械臂运行 UMI 操作技能，实机验证 | `TRON1` | [Czy213hd](https://github.com/Czy213hd) | 2025 | 代码 | [代码](https://github.com/Czy213hd/umi-on-tron-lab) |
| <a id="p-quest-vr-teleop-for-oli"></a>**Oli 的 Quest VR 遥操作**：用 Meta Quest 遥操作双臂、夹爪和头部，机器人相机画面实时回传头显 | `Oli` | [MSTLE](https://github.com/MSTLE) | 2025 | 代码 | [代码](https://github.com/MSTLE/Limx_teleoperate-end_pose) |
| <a id="p-wheeled-quadrupedal-manipulator"></a>**轮足四足移动操作**：在轮足四足机器人上加装机械臂，用学习控制器跟踪末端位姿 | `W1` | 南科大 CLEAR 实验室、浙大-UIUC等 | 2024 | 论文 | [主页](https://clearlab-sustech.github.io/RFM_loco_mani/)&nbsp;·&nbsp;[论文](https://arxiv.org/abs/2412.03012) |

## 具身智能

_9 个条目：2 篇论文 · 7 个代码_

| 项目 | 机型 | 作者 / 机构 | 年份 | 类型 | 链接 |
|---|---|---|---|---|---|
| <a id="p-tron1-hermes-agent"></a>**Tron 1 Hermes Agent**：在 Mac 上运行的自我改进本地 AI 智能体，在 MuJoCo 中驱动机器人 | `TRON1`&nbsp;*仿真* | [justinsuo](https://github.com/justinsuo) | 2026 | 代码 | [代码](https://github.com/justinsuo/tron1-hermes-agent) |
| <a id="p-fluxvla-on-tron2"></a>**在 TRON2 上部署 FluxVLA**：在自己的机器人上训练并部署 FluxVLA 视觉-语言-动作模型 | `TRON2` | [emoPointer](https://github.com/emoPointer) | 2026 | 代码 | [代码](https://github.com/emoPointer/FluxVLA) |
| <a id="p-oli-voice-interaction"></a>**Oli 语音交互**：ROS 2 语音交互：离线与在线语音识别、大模型对话和动作指令 | `Oli` | [zhilin2025](https://github.com/zhilin2025) | 2026 | 代码 | [代码](https://github.com/zhilin2025/oli_audio) |
| <a id="p-hwam"></a>**HWAM**：联合生成未来状态与动作的人形世界动作模型 | `Oli` | 逐际动力 | 2026 | 论文 | [主页](https://hwam.vercel.app/)&nbsp;·&nbsp;[论文](https://arxiv.org/abs/2610.12026) |
| <a id="p-acg-wam"></a>**ACG-WAM**：预测动作条件几何隐变量的世界-动作模型，在灵巧手上验证 | `TRON2` | 北京理工大学、逐际动力 | 2026 | 代码 | [主页](https://RoboOpus.github.io/ACG-WAM)&nbsp;·&nbsp;[论文](https://arxiv.org/abs/2610.06965)&nbsp;·&nbsp;[代码](https://github.com/RoboOpus/ACG-WAM) |
| <a id="p-drifting-action-heads-for-gr00t-n17"></a>**GR00T 漂移动作头**：把 GR00T N1.7 的扩散动作头换成单步 drifting 头，降低推理开销 | `TRON2` | 浙大-UIUC、逐际动力 | 2026 | 论文 | [论文](https://arxiv.org/abs/2609.18108) |
| <a id="p-tron2-garment-feeder"></a>**TRON2 服装送料**：为双臂送布任务微调的 Pi0.5 策略 | `TRON2` | [voniu](https://huggingface.co/voniu) | 2026 | 代码 | [模型](https://huggingface.co/voniu/tron2-garment-feeder-button-pi05) |
| <a id="p-tron2-lerobot-datasets"></a>**TRON2 LeRobot 数据集**：LeRobot 格式的抓放、叠衣、倒水数据集，以及基于它们微调的 GR00T 模型 | `TRON2` | [trantor2nd](https://huggingface.co/trantor2nd) | 2026 | 代码 | [模型](https://huggingface.co/models?author=trantor2nd&search=tron2)&nbsp;·&nbsp;[数据集](https://huggingface.co/datasets?author=trantor2nd&search=tron2) |
| <a id="p-troncamp-pi05-policies"></a>**TRONCamp Pi0.5 Policies**：TRONCamp 中插花和叠衣任务的 Pi0.5 模型权重 | `TRON2` | [toki1231](https://huggingface.co/toki1231) | 2026 | 代码 | [模型](https://huggingface.co/toki1231) |

## 工具、仿真与 SDK

_24 个工具，分 4 组_

### 训练框架

| 项目 | 机型 | 作者 / 机构 | 年份 | 链接 |
|---|---|---|---|---|
| <a id="p-tron1-isaac-lab-tasks"></a>**TRON1 Isaac Lab 任务集**：三种足型的 Isaac Lab 任务，含跳跃 | `TRON1` | [HughWang-wzy](https://github.com/HughWang-wzy) | 2026 | [代码](https://github.com/HughWang-wzy/tron1-rl-isaaclab) |
| <a id="p-tron1-rl-mjlab"></a>**TRON1 RL on mjlab**：在 mjlab 上训练轮足运动策略并导出 ONNX | `TRON1` | [Xinchen Yao](https://github.com/hoscy) | 2025 | [代码](https://github.com/hoscy/tron1-rl-mjlab) |
| <a id="p-leggedgym-ex"></a>**LeggedGym-Ex**：支持 Genesis、Isaac Gym、Isaac Sim 的 legged_gym | `TRON1` | [Yasen Jia](https://github.com/lupinjia) | 2024 | [代码](https://github.com/lupinjia/LeggedGym-Ex) |
| <a id="p-bipedal_locomotion_isaaclab"></a>**Bipedal Locomotion on Isaac Lab**：在 Isaac Lab 中训练平地、崎岖和楼梯地形行走，并部署到实机 | `TRON1` | [Andy-xiong6（南方科大）](https://github.com/Andy-xiong6) | 2024 | [代码](https://github.com/Andy-xiong6/bipedal_locomotion_isaaclab) |

### 仿真与环境

| 项目 | 机型 | 作者 / 机构 | 年份 | 链接 |
|---|---|---|---|---|
| <a id="p-tron2-wuji-bag-replay"></a>**TRON2 Wuji Hand Replay**：在 Isaac Sim 中回放机器人与 Wuji 灵巧手的录制轨迹 | `TRON2` | [zengxiong111](https://github.com/zengxiong111) | 2026 | [代码](https://github.com/zengxiong111/tron2-wuji-bag-replay) |
| <a id="p-metalsim"></a>**MetalSim**：面向 Apple 芯片 GPU 的机器人仿真与学习框架，对齐 Isaac Lab 任务，含 TRON1 场景 | `TRON1` | [Aditya Pulipaka](https://github.com/pulipakaa24) | 2026 | [代码](https://github.com/pulipakaa24/MetalSim) |
| <a id="p-robot-sim-docker"></a>**Robot Sim Docker**：在一台主机上用容器运行 ROS 2 与 LimX Gazebo、Isaac Lab、LeIsaac 和 MuJoCo | `TRON1` | [Aklva](https://github.com/Aklva) | 2026 | [代码](https://github.com/Aklva/robot-sim-docker) |
| <a id="p-limx-robotics-mcp"></a>**LimX Robotics MCP Server**：MCP 服务器，让 AI 智能体加载 MuJoCo 模型、控制关节并运行策略 | `TRON1` `Oli` | [sandraschi](https://github.com/sandraschi) | 2026 | [代码](https://github.com/sandraschi/limx-robotics-mcp) |
| <a id="p-tron_docker_sim"></a>**TRON Docker Sim**：在容器里运行 ROS 2 Gazebo 仿真，支持图形界面转发 | `TRON1` | [The-RoboTUM](https://github.com/The-RoboTUM) | 2026 | [代码](https://github.com/The-RoboTUM/tron_docker_sim) |
| <a id="p-roqsim"></a>**roqsim**：插件式 MuJoCo 仿真框架，内置人形机器人包含 Oli | `Oli` | [cps-test-lab](https://github.com/cps-test-lab) | 2026 | [代码](https://github.com/cps-test-lab/roqsim) |
| <a id="p-gewu-unity-rl-playground"></a>**Gewu (Unity RL Playground)**：Unity 强化学习训练平台，自带 TRON1 行走、轮行和跳跃策略 | `TRON1` | [loongOpen](https://github.com/loongOpen) | 2025 | [论文](https://arxiv.org/abs/2503.05146)&nbsp;·&nbsp;[代码](https://github.com/loongOpen/Unity-RL-Playground) |
| <a id="p-arc-bridge"></a>**ARC Bridge**：通过 LCM 把机器人控制器接到 MuJoCo 仿真器的桥接工具 | `TRON1` | [密歇根大学 ARCaD 实验室](https://github.com/ARCaD-Lab-UM) | 2024 | [代码](https://github.com/ARCaD-Lab-UM/arc-bridge) |

### 部署与控制

| 项目 | 机型 | 作者 / 机构 | 年份 | 链接 |
|---|---|---|---|---|
| <a id="p-tron1_ctrl_ros2"></a>**TRON1 ROS 2 Control**：封装机器人 WebSocket SDK 的 ROS 2 控制包 | `TRON1` | [Turing-zero](https://github.com/Turing-zero) | 2026 | [代码](https://github.com/Turing-zero/tron1_ctrl_ros2) |
| <a id="p-tron2_camera_calibration"></a>**TRON2 Camera Calibration**：机器人头部与腕部相机的标定工具 | `TRON2` | [zengxiong111](https://github.com/zengxiong111) | 2026 | [代码](https://github.com/zengxiong111/tron2_camera_calibration) |
| <a id="p-tron1_wheel_gui"></a>**TRON1 Wheel GUI**：Qt 与 ROS 结合的控制面板，从笔记本控制轮足实机运动 | `TRON1` | [Yang Zhuqi](https://github.com/Y20-code-cpu) | 2026 | [代码](https://github.com/Y20-code-cpu/tron1_wheel_gui) |
| <a id="p-wf_tron1b_deploy"></a>**Wheel-Foot Depth Policy Deploy**：轮足深度感知与非感知策略的 sim2sim 测试，基于 Docker 和 ROS | `TRON1` | [Leixin Chang](https://github.com/Leixinjonaschang) | 2026 | [代码](https://github.com/Leixinjonaschang/wf_tron1b_deploy) |
| <a id="p-tron_deploy"></a>**TRON Deploy for Windows**：在 Windows 11 笔记本上安装点足 SDK 并运行策略 | `TRON1` | [candi4](https://github.com/candi4) | 2026 | [代码](https://github.com/candi4/Tron_Deploy) |
| <a id="p-multi-robot-camera-collector"></a>**Multi-Robot Camera Collector**：在多台机器人相机间切换，按任务阶段保存画面用于数据采集 | `TRON1` `TRON2` | [oalaaCN](https://github.com/oalaaCN) | 2026 | [代码](https://github.com/oalaaCN/multi_robot_camera_collector) |
| <a id="p-crl-humanoid-ros"></a>**CRL Humanoid ROS**：苏黎世联邦理工的 ROS 2 框架，涵盖仿真、硬件控制和强化学习控制器，支持 G1 与 TRON1 | `TRON1` | [Jin Cheng（苏黎世联邦理工 CRL）](https://github.com/catachiii) | 2025 | [代码](https://github.com/catachiii/crl-humanoid-ros) |
| <a id="p-websocket_ros"></a>**TRON1 WebSocket-ROS Bridge**：把机器人 WebSocket 接口桥接到 ROS 的 Docker 方案，带模拟机器人，无实机也能测试 | `TRON1` | [daweidavidwang](https://github.com/daweidavidwang) | 2025 | [代码](https://github.com/daweidavidwang/websocket_ros) |

### 模型与动作数据

| 项目 | 机型 | 作者 / 机构 | 年份 | 链接 |
|---|---|---|---|---|
| <a id="p-rimkit"></a>**RIMKit**：接触感知的人体动作重定向，支持 17 款人形机器人，含该机型模型 | `Oli` | [Taemoon Jeong](https://github.com/tmjeong1103) | 2026 | [代码](https://github.com/tmjeong1103/RIMKit) |
| <a id="p-tron2_revo3_description"></a>**TRON2 with Revo3 Hands**：装配 BrainCo Revo3 灵巧手的整机模型，可直接用于训练 | `TRON2` | [ENDLESS0321](https://github.com/ENDLESS0321) | 2026 | [代码](https://github.com/ENDLESS0321/tron2_revo3_description) |
| <a id="p-robot_descriptionspy"></a>**robot_descriptions.py**：一行代码加载 TRON1、TRON2、Oli、Luna 模型 | `TRON1` `TRON2` `Oli` `Luna` | [robot-descriptions](https://github.com/robot-descriptions) | 2026 | [代码](https://github.com/robot-descriptions/robot_descriptions.py) |
| <a id="p-limx-3d-measurement-workbench"></a>**LimX 3D Measurement Workbench**：网页工具：浏览 TRON 产品模型、定位零件并测量尺寸 | `TRON1` `TRON2` | [voniu](https://github.com/voniu) | 2026 | [代码](https://github.com/voniu/limx-3d-measurement-workbench) |

## 教学与竞赛

_18 个条目：2 篇论文 · 15 个代码 · 1 个教程_

| 项目 | 机型 | 作者 / 机构 | 年份 | 类型 | 链接 |
|---|---|---|---|---|---|
| <a id="p-atec-2026-simulation-challenge"></a>**ATEC 2026 仿真挑战赛**：ATEC 2026 机器人仿真挑战赛官方入门代码，各机型分设赛道 | `TRON1` `TRON2`&nbsp;*仿真* | [ATEC](https://github.com/atecup) | 2026 | 代码 | [代码](https://github.com/atecup/ATEC2026_Simulation_Challenge) |
| <a id="p-troncamp-2026-mani-solution"></a>**TRONCamp 2026 操作赛方案**：四个双臂任务的 ACT 方案，公开了模型权重和示范数据 | `TRON2`&nbsp;*仿真* | [han-xudong](https://github.com/han-xudong) | 2026 | 代码 | [代码](https://github.com/han-xudong/troncamp-mani)&nbsp;·&nbsp;[模型](https://huggingface.co/han-xudong/troncamp-mani-act)&nbsp;·&nbsp;[数据集](https://huggingface.co/datasets/han-xudong/troncamp-mani-dataset) |
| <a id="p-troncamp-2026-locomotion-solution"></a>**TRONCamp 2026 运动赛方案**：锁臂双足 TRON2 的强化学习运动策略，公开了模型权重 | `TRON2`&nbsp;*仿真* | [han-xudong](https://github.com/han-xudong) | 2026 | 代码 | [代码](https://github.com/han-xudong/troncamp-locomotion)&nbsp;·&nbsp;[模型](https://huggingface.co/han-xudong/troncamp-locomotion-rl) |
| <a id="p-study_tron1"></a>**TRON1 Study Notes**：在不装机器人 SDK 的情况下用 Isaac Lab 训练的环境搭建笔记与学习日志 | `TRON1`&nbsp;*仿真* | [beamkeerati](https://github.com/beamkeerati) | 2026 | 代码 | [代码](https://github.com/beamkeerati/study_tron1) |
| <a id="p-openarm-mobile-manipulation-lab"></a>**OpenArm 移动操作实训**：两天的 MuJoCo 与 ROS 2 课程：把 OpenArm 装在双足或轮式底盘上，按自然语言任务执行（韩语） | `TRON1`&nbsp;*仿真* | [aha645](https://github.com/aha645) | 2026 | 代码 | [代码](https://github.com/aha645/openarms_llm_ex) |
| <a id="p-limx-tron1-learning"></a>**LimX Tron1 Learning**：交互式教程，一步步讲解 Isaac Lab 训练流程 | `TRON1`&nbsp;*仿真* | [jessiezhg](https://huggingface.co/jessiezhg) | 2026 | 教程 | [教程](https://huggingface.co/spaces/jessiezhg/LimX-Tron1-Learning) |
| <a id="p-zetin-robocup-2026"></a>**Zetin RoboCup 2026**：在 Isaac Lab 中训练双足 TRON1 足球机器人的行走、追球和射门（韩语） | `TRON1`&nbsp;*仿真* | [tae2yi](https://github.com/tae2yi) | 2026 | 代码 | [代码](https://github.com/tae2yi/Zetin_Robocup2026) |
| <a id="p-conducting-evaluation-with-oli"></a>**Conducting Evaluation System**：面向音乐教学的指挥动作示范与评分系统，在 Oli 数字孪生上展示 | `Oli`&nbsp;*仿真* | 广东培正学院 | 2026 | 论文 | [论文](https://doi.org/10.1145/3806980.3807204) |
| <a id="p-every-embodied-troncamp-mani"></a>**Every Embodied: TRONCamp Mani**：Datawhale 具身智能开源教程，含 TRONCamp Mani 赛事章节，讲 TRON2 双臂操作任务 | `TRON2`&nbsp;*仿真* | [Datawhale](https://github.com/datawhalechina) | 2026 | 代码 | [代码](https://github.com/datawhalechina/every-embodied/tree/main/15-Challenge%E7%AB%9E%E8%B5%9B/TRONCamp-Mani) |
| <a id="p-atec2026-logic-tars"></a>**ATEC 2026 Wheel-Legged Entry**：参赛队伍在 ATEC 2026 挑战赛中的强化学习训练与仿真部署工程 | `TRON1` `TRON2`&nbsp;*仿真* | [Logic-TARS](https://github.com/Logic-TARS) | 2026 | 代码 | [代码](https://github.com/Logic-TARS/ATEC2026) |
| <a id="p-zetin-robocup-control"></a>**Zetin RoboCup Control**：RoboCup 2026 比赛代码：TRON1 下肢加自制上身和相机（韩语） | `TRON1` | [newb-ops（首尔市立大学 ZETIN）](https://github.com/newb-ops) | 2026 | 代码 | [代码](https://github.com/newb-ops/robocup-control-portfolio) |
| <a id="p-troncamp-mani-24zlha"></a>**TRONCamp Mani Solution 24ZlhA**：ACT 加困难样本挖掘与多卡训练，附技术报告；T4 线上得分 79/100 | `TRON2`&nbsp;*仿真* | [upset666](https://github.com/upset666) | 2026 | 代码 | [代码](https://github.com/upset666/troncamp-mani-24ZlhA) |
| <a id="p-troncamp-mani-act-dp"></a>**TRONCamp Mani ACT + Diffusion Policy**：T1 到 T3 用 ACT，三碗堆叠任务改用 Diffusion Policy，附技术设计文档 | `TRON2`&nbsp;*仿真* | [irvingskr](https://github.com/irvingskr) | 2026 | 代码 | [代码](https://github.com/irvingskr/troncamp-mani) |
| <a id="p-troncamp-mani-sormaker"></a>**TRONCamp Mani Solution SORMaker**：四个任务统一的 ACT 训练与部署流程，附 T3、T4 策略的运行视频 | `TRON2`&nbsp;*仿真* | [SORMaker](https://github.com/SORMaker) | 2026 | 代码 | [代码](https://github.com/SORMaker/troncamp-mani) |
| <a id="p-hands-on-embodied-ai"></a>**动手做具身智能**：从算法到实机的开放课程，包含户外 GNSS 与 Nav2 导航实践 | `TRON1` | [武汉大学 BRAIN 实验室](https://github.com/Whu-BrainLab) | 2025 | 代码 | [代码](https://github.com/Whu-BrainLab/Embodied-AI-Tutorial)&nbsp;·&nbsp;[教程](https://mp.weixin.qq.com/s/YLKVi09hgImSuWUr_S6gJA) |
| <a id="p-canton-tower-robot-climbing-challenge"></a>**广州塔机器人登高挑战赛**：Oli 凭借 FastStair 方法获得登塔赛冠军和最佳精准控制奖 | `Oli` | 逐际动力 | 2025 | 论文 | [论文](https://arxiv.org/abs/2601.10365)&nbsp;·&nbsp;[成绩](https://www.sfccn.com/2026/1-1/5NMDE0NzNfMjA5MzM5NA.html) |
| <a id="p-rl-bipedal-locomotion"></a>**双足运动强化学习**：南科大 ACR2025 课程项目：Isaac Lab 训练、回放与部署 | `TRON1`&nbsp;*仿真* | [81578823（南方科大）](https://github.com/81578823) | 2025 | 代码 | [代码](https://github.com/81578823/RL_bipedal_locomotion_Isaaclab) |
| <a id="p-pointfootgym"></a>**pointfootGym**：南科大 CLEAR 实验室的点足机器人训练模板，基于 Isaac Gym 与 legged_gym | `TRON1`&nbsp;*仿真* | [Haokai Su（南方科大 CLEAR 实验室）](https://github.com/SuDaxia-kai) | 2024 | 代码 | [代码](https://github.com/SuDaxia-kai/pointfootGym) |

## 行业应用

_34 个条目，分 6 组_

本节由 LimX 维护，收录公开报道、合作方公告和企业开源项目，每条都附有来源链接。

### 落地与产品

| 项目 | 机型 | 作者 / 机构 | 年份 | 类型 | 链接 |
|---|---|---|---|---|---|
| <a id="p-tenniix-ultra-max"></a>**TENNIIX ULTRA MAX**：以 TRON2 轮足为底盘的网球机器人，在 2026 比莉·简·金杯总决赛与职业选手对打 | `TRON2` | 英汉思动力（Tenniix） | 2026 | 报道 | [报道](https://www.news.cn/sports/20260928/f1776d7ca75042568a5137e256fa9425/c.html) |
| <a id="p-zinova-tron2-construction"></a>**ZINOVA Tool Intelligence**：两台 TRON2 用钉枪和钢筋完成缩比混凝土预制墙施工 | `TRON2` | ZINOVA、RIC Robotics | 2026 | 报道 | [视频](https://www.youtube.com/watch?v=8KDxnT-4zl0)&nbsp;·&nbsp;[报道](https://www.equipmentworld.com/technology/article/15836367/zinova-limx-bring-toolwielding-robots-to-construction) |
| <a id="p-dongtu-domestic-architecture"></a>**国产电子架构人形机器人**：Oli 搭载东土 Intewell 操作系统与 AUTBUS 总线；逐际同时加入东土发起的电子架构联盟 | `Oli` | 东土科技 | 2026 | 报道 | [报道 (微信公众号)](http://mp.weixin.qq.com/s?__biz=Mzk0NDU5NjMwMA==&mid=2247495106&idx=1&sn=8b5ffd05d0615a0581d3b23a18f2d830&chksm=c20243eecd5be209a820feecab39fcb0480f5ec903b40f0d655db8f6225b378bd0e8f1db3a1a)&nbsp;·&nbsp;[报道 (21世纪经济报道)](https://m.21jingji.com/article/20260929/herald/af2d0b02d6e7593ed4a2af7d05a191b5.html)&nbsp;·&nbsp;[报道 (四川在线)](https://cbgc.scol.com.cn/news/8010385) |
| <a id="p-wuji-hand-2-pharmacy-demo"></a>**Wuji Hand 2 Pharmacy Demo**：装配舞肌科技 Wuji Hand 2 的 TRON2 完成中药抓取、称量、研磨和包装 | `TRON2` | WUJI TECH | 2026 | 报道 | [报道 (ja)](https://robotstart.info/article/2026/08/26/382326.html) |
| <a id="p-d-robotics-rdk-s100-tron1"></a>**RDK S100 on TRON1**：点足运控模型迁移到地瓜机器人 RDK S100 的 BPU 上运行，列为官方应用案例 | `TRON1` | 地瓜机器人 | 2025 | 报道 | [报道](https://forum.d-robotics.cc/t/topic/28833) |

### 企业开源项目

| 项目 | 机型 | 作者 / 机构 | 年份 | 类型 | 链接 |
|---|---|---|---|---|---|
| <a id="p-xense-openpi-for-tron2"></a>**Xense OpenPI**：面向双臂操作的 Pi0.5 训练配置与实时推理 | `TRON2` | [他山科技 Xense](https://github.com/XenseRobotics-AI) | 2026 | 代码 | [代码](https://github.com/XenseRobotics-AI/xense-openpi) |
| <a id="p-crest-tron2-description"></a>**TRON2 Description, Crest edition**：为 SFYG 手臂腕部相机支架调整过的机器人模型 | `TRON2` | [Crest Robotics](https://github.com/Crest-Robotics) | 2026 | 代码 | [代码](https://github.com/Crest-Robotics/tron2-robot-description) |
| <a id="p-artefacts-tron1-nav2-newton"></a>**TRON1 Nav2 in Newton**：在 Newton 物理仿真器中进行 Nav2 路径跟随测试 | `TRON1`&nbsp;*仿真* | [Artefacts（日本）](https://github.com/art-e-fact) | 2026 | 代码 | [代码](https://github.com/art-e-fact/tron-navigation-demo) |
| <a id="p-xense-pico4-teleoperator"></a>**LeRobot Pico4 Teleoperator**：LeRobot 的 PICO 4 双臂遥操作插件，支持 TRON2 | `TRON2` | [他山科技 Xense](https://github.com/XenseRobotics-AI) | 2026 | 代码 | [代码](https://github.com/XenseRobotics-AI/lerobot-teleoperator-pico4) |
| <a id="p-safesentinel-sonic-for-oli"></a>**SONIC Training for Oli**：在 31 自由度型号上训练 GEAR-SONIC 全身控制，支持 PICO VR 遥操作 | `Oli`&nbsp;*仿真* | [SafeSentinel](https://github.com/safe-sentinel-co) | 2026 | 代码 | [代码](https://github.com/safe-sentinel-co/hu_d04_sonic_setup) |
| <a id="p-anima-ros2-sim-net"></a>**ANIMA ROS 2 Simulation Network**：ROS 2 与 Gazebo 仿真栈，内置 TRON1 双足模型 | `TRON1`&nbsp;*仿真* | [RobotFlow Labs](https://github.com/RobotFlow-Labs) | 2026 | 代码 | [代码](https://github.com/RobotFlow-Labs/anima-ros2-sim-net) |
| <a id="p-artefacts-tron1-workspace"></a>**TRON1 Artefacts Workspace**：基于 Artefacts 机器人测试平台的 ROS 2 与 Gazebo 演示 | `TRON1`&nbsp;*仿真* | [Artefacts（日本）](https://github.com/art-e-fact) | 2026 | 代码 | [代码](https://github.com/art-e-fact/tron1-artefacts) |
| <a id="p-openmind-om1-sim"></a>**OM1-sim**：OM1 机器人操作系统的 Isaac Sim 仿真环境，支持轮足 TRON1、Go2 和 G1 | `TRON1`&nbsp;*仿真* | [OpenMind](https://github.com/OpenMind) | 2026 | 代码 | [代码](https://github.com/OpenMind/OM1-sim) |
| <a id="p-phanthy-motus-driver"></a>**Phanthy Motus Drivers**：第四范式 Phanthy Motus 具身智能平台的硬件驱动，支持 TRON2 双臂 | `TRON2` | [第四范式](https://github.com/4paradigm) | 2026 | 代码 | [代码](https://github.com/4paradigm/phanthymotus-driver) |
| <a id="p-xense-tron2-pnp-dataset"></a>**Xense TRON2 Pick-and-Place Dataset**：115 条遥操作数据，带触觉视频；Voxel51 另以 FiftyOne 格式转发 | `TRON2` | [他山科技 Xense](https://huggingface.co/Xense) | 2026 | 代码 | [数据集](https://huggingface.co/datasets/Xense/tron2rt-pnp-0918)&nbsp;·&nbsp;[数据集 (Voxel51)](https://huggingface.co/datasets/Voxel51/xense-tron2rt-pnp-115ep) |
| <a id="p-anima-ros2-bridge"></a>**ANIMA ROS 2 Bridge**：AI 智能体到 ROS 2 机器人的 DDS / WebSocket 桥接，可自动识别 LimX 机器人并内置 TRON1 模型 | `TRON1`&nbsp;*仿真* | [RobotFlow Labs](https://github.com/RobotFlow-Labs) | 2026 | 代码 | [代码](https://github.com/RobotFlow-Labs/anima-ros2-bridge) |
| <a id="p-cmriat-citadel"></a>**Citadel**：机器人数据管理工具，把 HDF5 录制数据批量转换为 LeRobot v2.1，示例使用 TRON2 采集的数据 | `TRON2` | [招商局先进技术研究院](https://github.com/cmriat) | 2026 | 代码 | [代码](https://github.com/cmriat/Citadel) |
| <a id="p-openmind-brainpack"></a>**OpenMind BrainPack**：模块化计算与开发背包，适配 TRON1、Unitree G1 和 Go2 | `TRON1` | [OpenMind](https://github.com/OpenMind) | 2025 | 代码 | [代码](https://github.com/OpenMind/brainpack) |

### 商业演出与活动

| 项目 | 机型 | 作者 / 机构 | 年份 | 类型 | 链接 |
|---|---|---|---|---|---|
| <a id="p-nio-gba-auto-show"></a>**大湾区车展蔚来展台**：Oli 与 Luna 在蔚来展台做互动展示 | `Oli` `Luna` | 蔚来 | 2026 | 报道 | [报道](https://news.ifeng.com/c/8vmGa3sP4u7) |
| <a id="p-kill-it-finale"></a>**《Kill It》时装真人秀总决赛**：Luna 登上设计师金娜拉的夺冠决赛舞台（tvN） | `Luna` | tvN、金娜拉 | 2026 | 报道 | [报道 (ko)](https://isplus.com/article/view/isp202607290025) |
| <a id="p-taobao-influencer-festival"></a>**淘宝达人节**：Luna 与演员陈意涵在上海同走 T 台 | `Luna` | 淘宝 | 2026 | 报道 | [报道](https://interestingengineering.com/ai-robotics/video-china-humanoid-catwalk-taobao-festival) |
| <a id="p-luna-china-gt-opening"></a>**2026 CHINA GT opening ceremony**：5 台 Luna 在 CHINA GT 中国超级跑车锦标赛开幕式上表演自主编队舞蹈 | `Luna` | CHINA GT | 2026 | 报道 | [报道 (ja)](https://robotstart.info/article/2026/09/18/382434.html) |

### 战略合作

| 项目 | 机型 | 作者 / 机构 | 年份 | 类型 | 链接 |
|---|---|---|---|---|---|
| <a id="p-smartcube-partnership"></a>**SmartCube**：韩国官方合作伙伴，人形机器人用于工厂与能源现场巡检并接入数字孪生 | — | SmartCube（韩国） | 2026 | 报道 | [报道 (ko)](https://www.aipostkorea.com/news/articleView.html?idxno=12727) |
| <a id="p-guangyang-partnership"></a>**光洋股份**：联合开发一体化关节模组，涵盖轴承、齿轮、减速机和驱动器（供应链合作） | — | 光洋股份 | 2026 | 报道 | [报道 (每日经济新闻)](https://www.nbd.com.cn/articles/2026-03-09/4285402.html)&nbsp;·&nbsp;[报道 (东方财富)](https://finance.eastmoney.com/a/202603093666208673.html) |
| <a id="p-nbpu-industry-college"></a>**Ningbo Polytechnic University**：共建具身智能产业学院，以 Oli 作为核心教学平台 | `Oli` | 宁波职业技术大学 | 2026 | 报道 | [报道](https://www.nbpu.edu.cn/2026/0612/c2654a6462855/page.htm) |
| <a id="p-saic-beijing-joint-lab"></a>**上汽北京联合实验室**：面向汽车制造的具身智能联合实验室，逐际动力为上汽首家具身智能战略合作伙伴 | — | 上汽北京 | 2025 | 报道 | [报道](https://www.pingwest.com/a/306356) |

### 区域伙伴与渠道

| 项目 | 机型 | 作者 / 机构 | 年份 | 类型 | 链接 |
|---|---|---|---|---|---|
| <a id="p-knoxlabs-data-collection"></a>**Knoxlabs**：在美国销售 TRON2 与 Oli 套装，提供数据采集用遥操作部署 | `TRON2` `Oli` | Knoxlabs | 2026 | 报道 | [报道](https://www.knoxlabs.com/blogs/articles/robot-teleoperation-data-collection-limx) |
| <a id="p-tron-kk-humanoid-si"></a>**TRON K.K.**：在日本提供人形机器人系统集成与 Omniverse 仿真，合作品牌包括 LimX | — | TRON K.K.（日本） | 2026 | 报道 | [报道 (ja)](https://tron.tokyo/en/service/limx-dynamics/) |
| <a id="p-robot-bank-japan"></a>**Robot Bank**：在日本推出 TRON1、TRON2 和 Oli，并提供现场部署支持 | `TRON1` `TRON2` `Oli` | Robot Bank（日本） | 2026 | 报道 | [报道 (ja)](https://robotstart.info/article/2026/05/15/381891.html) |
| <a id="p-mybotshop-germany"></a>**MYBOTSHOP**：在德国销售并支持 P1，提供使用手册、ROS 2 配置指南和返修服务 | `P1` | MYBOTSHOP GmbH（德国） | 2026 | 报道 | [报道](https://www.docs.mybotshop.de/limx_p1.html) |
| <a id="p-synerex-korea"></a>**Synerex**：韩国官方合作伙伴，在 2025 韩国无人机展首次在韩展出 TRON1 | `TRON1` | Synerex（韩国） | 2025 | 报道 | [报道 (ko)](https://www.newswire.co.kr/newsRead.php?no=1005949) |
| <a id="p-r2c2-partnership"></a>**R2C2**：香港官方开发者与分销商，把强化学习机器人用于公用设施与巡检 | `W1` `P1` | R2C2 Limited（香港） | 2024 | 报道 | [公告 (LinkedIn)](https://www.linkedin.com/posts/limx-dynamics_robotics-partnership-innovation-activity-7211709457666310145-ddt9)&nbsp;·&nbsp;[公告 (X)](https://x.com/LimX_Dynamics/status/1806002749722820865) |

### 奖项与认可

| 项目 | 机型 | 作者 / 机构 | 年份 | 类型 | 链接 |
|---|---|---|---|---|---|
| <a id="p-ieee-spectrum-robot-of-the-month-tron1"></a>**IEEE Spectrum Robot of the Month**：TRON1 入选 IEEE Spectrum 杂志“月度机器人”栏目 | `TRON1` | IEEE Spectrum | 2026 | 报道 | [报道](https://doi.org/10.1109/MSPEC.2026.11595926) |
| <a id="p-rbr50-2025-tron1"></a>**2025 RBR50 机器人创新奖**：TRON1 作为多形态双足研发平台入选 | `TRON1` | The Robot Report | 2025 | 报道 | [成绩](https://www.therobotreport.com/rbr50-company-2025/tron-1-multi-modal-biped-offers-a-unique-rd-platform/) |

## 按机型查找

每个机型都有单独页面，收录用到该机型的全部条目： [TRON1](robots/TRON1_cn.md) · [TRON2](robots/TRON2_cn.md) · [Oli](robots/Oli_cn.md) · [Luna](robots/Luna_cn.md) · [P1](robots/P1_cn.md) · [W1](robots/W1_cn.md)

各机型在每个分类中的条目数：

| 机型 | 合计 | 运动控制 | 感知与导航 | 操作 | 具身智能 | 工具 | 教学与竞赛 | 行业应用 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| [`TRON1`](robots/TRON1_cn.md) | **92** | 32 | 13 | 6 | 1 | 19 | 10 | 11 |
| [`TRON2`](robots/TRON2_cn.md) | **35** | 1 |  | 3 | 6 | 6 | 8 | 11 |
| [`Oli`](robots/Oli_cn.md) | **30** | 14 |  | 2 | 2 | 4 | 2 | 6 |
| [`Luna`](robots/Luna_cn.md) | **8** | 2 | 1 |  |  | 1 |  | 4 |
| [`P1`](robots/P1_cn.md) | **5** | 3 |  |  |  |  |  | 2 |
| [`W1`](robots/W1_cn.md) | **4** | 2 |  | 1 |  |  |  | 1 |

## 参与贡献

欢迎自荐，也欢迎推荐别人的工作：填写[提交表单](https://github.com/limxdynamics/awesome-limx/issues/new?template=add-project.yml)、提 Pull Request，或发邮件到 [opensource@limxdynamics.com](mailto:opensource@limxdynamics.com)。收录标准见 [CONTRIBUTING_cn.md](CONTRIBUTING_cn.md)。各分类内按年份从新到旧排列；「类型」列说明读者能拿到什么：可以直接跑的（**代码**）、可以跟着学的（**教程**）、可以阅读的（**论文**），还是媒体报道或公告（**报道**）。

收录不代表逐际动力背书，权利归原作者所有。项目所有者可随时要求移除，无需说明理由。

合作采购请联系 [opensource@limxdynamics.com](mailto:opensource@limxdynamics.com)。


## 许可

本列表以 [CC0 1.0](LICENSE) 发布。被收录的项目仍适用其各自的许可证。
