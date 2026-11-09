<div align="center">

<a href="README.md"><img src="https://img.shields.io/badge/English-24292f?style=for-the-badge" alt="English"></a>&nbsp;&nbsp;<a href="README_cn.md"><img src="https://img.shields.io/badge/Chinese-24292f?style=for-the-badge" alt="Chinese"></a>

</div>

<p align="center"><img src="assets/banner_cn.png" alt="Awesome LimX" width="100%"></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-CC0--1.0-2f6feb" alt="License: CC0-1.0"></a>
  <a href="https://github.com/limxdynamics/limxdynamics/blob/main/doc/wechat_qr.png"><img src="https://img.shields.io/badge/%E5%BE%AE%E4%BF%A1-%E5%BC%80%E5%8F%91%E8%80%85%E7%A4%BE%E5%8C%BA-07C160?logo=wechat&logoColor=white" alt="微信开发者社区"></a>
</p>
<p align="center"><sub>合作采购请联系 <a href="mailto:opensource@limxdynamics.com">opensource@limxdynamics.com</a></sub></p>

基于[逐际动力（LimX Dynamics）](https://www.limxdynamics.com)机器人（TRON1、TRON2、Oli、Luna）和 LimX SDK 完成的开源项目、论文和比赛成果。

> 收录所有使用 LimX 硬件或软件的公开成果，包括高校、个人和逐际动力研究人员的工作；逐际动力官方发布的开源仓库请见 [GitHub](https://github.com/limxdynamics) 和 [Hugging Face](https://huggingface.co/limxdynamics)。每条都链接到公开原始出处，收录不代表逐际动力背书，权利归原作者所有。

**35 个项目，其中 13 个开源（🌟）**，覆盖 TRON1（18）、TRON2（5）、Oli（11）、Luna（1）、P1（3）、W1（1）。

## 目录

- [按机型查找](#按机型查找)
- [运动控制](#运动控制)（17）
- [操作](#操作)（6）
- [具身智能](#具身智能)（5）
- [工具、仿真与 SDK](#工具仿真与-sdk)（3）
- [教学与竞赛](#教学与竞赛)（4）
- [参与贡献](#参与贡献)

## 按机型查找

- **TRON1**（18）：[学习增强的 PMP-MPC](#p-learning-enhanced-pmp-mpc) · [Where-to-Learn](#p-where-to-learn) · [AME-2](#p-ame-2) · [LIPM 引导强化学习](#p-lipm-guided-rl) · [CTBC](#p-ctbc) · [BarlowWalk](#p-barlowwalk) · [多本体动作重定向](#p-multi-embodiment-retargeting) · [双足 MPC](#p-bipedal-mpc) · [全身一体化移动操作](#p-holistic-loco-manipulation) · [TRON1 与 UR5e 交接水瓶](#p-tron1-to-ur5e-bottle-transfer) · [多机协同搬运](#p-cooperative-transportation) · [Arm-TRON](#p-arm-tron) · [Tron_Deploy](#p-tron_deploy) · [limx-robotics-mcp](#p-limx-robotics-mcp) · [bipedal_locomotion_isaaclab](#p-bipedal_locomotion_isaaclab) · [LimX Tron1 Learning](#p-limx-tron1-learning) · [双足运动强化学习](#p-rl-bipedal-locomotion) · [pointfootGym](#p-pointfootgym)
- **TRON2**（5）：[多机协同搬运](#p-cooperative-transportation) · [ACG-WAM](#p-acg-wam) · [GR00T N1.7 单步漂移动作头](#p-drifting-action-heads-for-gr00t-n17) · [TRON2 服装送料](#p-tron2-garment-feeder) · [TRON2 LeRobot 数据集](#p-tron2-lerobot-datasets)
- **Oli**（11）：[SuperMimic for Oli](#p-supermimic-for-oli) · [VAPS](#p-vaps) · [Any2Any](#p-any2any) · [FastStair](#p-faststair) · [PvP](#p-pvp) · [GA-PHL](#p-ga-phl) · [多本体动作重定向](#p-multi-embodiment-retargeting) · [CWI](#p-cwi) · [HWAM](#p-hwam) · [limx-robotics-mcp](#p-limx-robotics-mcp) · [广州塔机器人登高挑战赛](#p-canton-tower-robot-climbing-challenge)
- **Luna**（1）：[Any2Any](#p-any2any)
- **P1**（3）：[VMTS](#p-vmts) · [CTS](#p-cts) · [任务空间 Riccati 全身控制](#p-task-space-riccati-wbc)
- **W1**（1）：[轮足四足移动操作](#p-wheeled-quadrupedal-manipulator)

## 运动控制

| 项目 | 机型 | 团队 | 年份 | 链接 |
|---|---|---|---|---|
| <a id="p-learning-enhanced-pmp-mpc"></a>🌟 **学习增强的 PMP-MPC**：点足双足的庞特里亚金 MPC，加入学习的动力学残差（ASCC 2026） | `TRON1` | Markwcl2004 | 2026 | [[论文](https://doi.org/10.1109/ASCC70886.2026.11701800)] [[代码](https://github.com/Markwcl2004/PMP_based_Bipedal_MPC)] |
| <a id="p-supermimic-for-oli"></a>🌟 **SuperMimic for Oli**：在 Isaac Lab / MuJoCo-Warp 中用一个策略让 31 自由度 Oli 跟踪 40 段 LAFAN1 动作 | `Oli` | Tianxing Liu | 2026 | [[代码](https://github.com/liuskywalkerjskd/supermimic_oli)] |
| <a id="p-vaps"></a>**VAPS**：可行性感知的策略选择，让人形机器人安全完成特技动作，在 Oli 实机上做侧空翻 | `Oli` | 达姆施塔特工业大学、逐际动力等 | 2026 | [[主页](https://vaps-r-al.github.io/)] [[论文](https://arxiv.org/abs/2610.01397)] |
| <a id="p-any2any"></a>**Any2Any**：人形全身动作跟踪的高效跨本体迁移 | `Oli` `Luna` | 逐际动力 | 2026 | [[论文](https://arxiv.org/abs/2605.23733)] |
| <a id="p-where-to-learn"></a>**Where-to-Learn**：解析策略梯度引导的同策略强化学习探索 | `TRON1` | 浙江大学、南方科技大学 | 2026 | [[主页](https://wheretolearn.github.io)] [[论文](https://arxiv.org/abs/2603.27317)] [[视频](https://www.youtube.com/watch?v=DztdUyh_LVk)] |
| <a id="p-faststair"></a>**FastStair**：让全尺寸人形机器人快速跑上楼梯 | `Oli` | 哈工大、逐际动力等 | 2026 | [[主页](https://npcliu.github.io/FastStair)] [[论文](https://arxiv.org/abs/2601.10365)] [[视频](https://youtu.be/SoLBK7VEGDo)] |
| <a id="p-ame-2"></a>**AME-2**：基于注意力地图编码的敏捷足式运动 | `TRON1` | 苏黎世联邦理工学院 | 2026 | [[主页](https://sites.google.com/leggedrobotics.com/ame-2)] [[论文](https://arxiv.org/abs/2601.08485)] |
| <a id="p-pvp"></a>**PvP**：基于本体-特权对比表征的高效人形机器人学习 | `Oli` | 香港理工、中国科大、逐际动力等 | 2025 | [[论文](https://arxiv.org/abs/2512.13093)] |
| <a id="p-ga-phl"></a>**GA-PHL**：实时地形重建的步态自适应人形感知运动 | `Oli` | 中国科大、逐际动力等 | 2025 | [[主页](https://ga-phl.github.io/)] [[论文](https://arxiv.org/abs/2512.07464)] |
| <a id="p-lipm-guided-rl"></a>**LIPM 引导强化学习**：点足双足的稳定感知运动 | `TRON1` | 南方科大、港科大、港大等 | 2025 | [[论文](https://arxiv.org/abs/2509.09106)] |
| <a id="p-ctbc"></a>**CTBC**：轮式双足机器人的接触触发盲爬 | `TRON1` | 上海大学、酷哇机器人 | 2025 | [[主页](https://ctbc-for-wheeled-bipedal-robots.github.io/)] [[论文](https://arxiv.org/abs/2509.02986)] |
| <a id="p-barlowwalk"></a>**BarlowWalk**：面向地形自适应运动的自监督表征 | `TRON1` | 哈工大（深圳） | 2025 | [[论文](https://arxiv.org/abs/2508.00939)] |
| <a id="p-multi-embodiment-retargeting"></a>**多本体动作重定向**：基于引导扩散模型，把动作重定向到 Oli、TRON1 等多种机器人 | `Oli` `TRON1` | 南方科大、港科大、浙大-UIUC 联合学院、逐际动力 | 2025 | [[论文](https://arxiv.org/abs/2505.20857)] |
| <a id="p-vmts"></a>**VMTS**：视觉辅助的师生强化学习，用于双足多地形运动，部署在 P1 上 | `P1` | 东南大学 | 2025 | [[论文](https://arxiv.org/abs/2503.07049)] |
| <a id="p-bipedal-mpc"></a>🌟 **双足 MPC**：MuJoCo 中的凸 MPC 与全身控制，基于 ROS 2 | `TRON1` | 南方科技大学 CLEAR 实验室 | 2024 | [[代码](https://github.com/clearlab-sustech/Bipedal_MPC)] |
| <a id="p-cts"></a>**CTS**：足式运动的并行师生强化学习，在点足 P1 上验证 | `P1` | 南方科大、浙大-UIUC 联合学院、逐际动力 | 2024 | [[主页](https://clearlab-sustech.github.io/concurrentTS/)] [[论文](https://arxiv.org/abs/2405.10830)] |
| <a id="p-task-space-riccati-wbc"></a>**任务空间 Riccati 全身控制**：欠驱动足式运动的全身控制，在 P1 仿真中验证 | `P1` | 南方科大、港科大、圣母大学 | 2024 | [[论文](https://arxiv.org/abs/2404.00591)] |

## 操作

| 项目 | 机型 | 团队 | 年份 | 链接 |
|---|---|---|---|---|
| <a id="p-holistic-loco-manipulation"></a>**全身一体化移动操作**：双足移动操作机器人（TRON1 加装机械臂） | `TRON1` | 浙大-UIUC 联合学院、逐际动力 | 2026 | [[论文](https://arxiv.org/abs/2609.18930)] |
| <a id="p-tron1-to-ur5e-bottle-transfer"></a>🌟 **TRON1 与 UR5e 交接水瓶**：TRON1 运送水瓶并对接，UR5e 用 MoveIt 2 抓取（MuJoCo、ROS 2） | `TRON1` | Centaucyan | 2026 | [[代码](https://github.com/Centaucyan/Proj_Transferring_bottle_from_tron1_to_ur5e_in_mujoco_env)] |
| <a id="p-cooperative-transportation"></a>🌟 **多机协同搬运**：两台带机械臂的轮足 TRON 在 MuJoCo 中协同搬运 | `TRON1` `TRON2` | Matt14-mander | 2026 | [[代码](https://github.com/Matt14-mander/Multiple_Humanoid_Cooperative_Transportation)] |
| <a id="p-cwi"></a>**CWI**：面向移动操作的人形全身组合模仿 | `Oli` | 逐际动力、港大、南方科大等 | 2026 | [[主页](https://cwi-ral.github.io/CWI-RAL-Webpage/)] [[论文](https://arxiv.org/abs/2606.27676)] |
| <a id="p-arm-tron"></a>**Arm-TRON**：点足、双足、轮足可切换的双足加机械臂平台上的全身移动操作（IEEE/ASME TMECH） | `TRON1` | 南方科大、浙江大学、逐际动力 | 2026 | [[论文](https://doi.org/10.1109/TMECH.2026.3727546)] |
| <a id="p-wheeled-quadrupedal-manipulator"></a>**轮足四足移动操作**：W1 加装 AIRBOT 机械臂，实现全向位姿跟踪的全身移动操作 | `W1` | 南方科大、浙大-UIUC 联合学院、逐际动力 | 2024 | [[论文](https://arxiv.org/abs/2412.03012)] |

## 具身智能

| 项目 | 机型 | 团队 | 年份 | 链接 |
|---|---|---|---|---|
| <a id="p-hwam"></a>**HWAM**：状态与动作联合生成的人形世界动作模型，在 31 自由度 Oli 上验证 | `Oli` | 逐际动力 | 2026 | [[主页](https://hwam.vercel.app/)] [[论文](https://arxiv.org/abs/2610.12026)] |
| <a id="p-acg-wam"></a>🌟 **ACG-WAM**：基于动作条件几何隐变量预测的世界-动作模型，在配 WUJI 灵巧手的 TRON2 上验证 | `TRON2` | 北京理工大学、逐际动力 | 2026 | [[主页](https://RoboOpus.github.io/ACG-WAM)] [[论文](https://arxiv.org/abs/2610.06965)] [[代码](https://github.com/RoboOpus/ACG-WAM)] |
| <a id="p-drifting-action-heads-for-gr00t-n17"></a>**GR00T N1.7 单步漂移动作头**：GR00T 的单步动作头，部署在 TRON2 实机上 | `TRON2` | 浙大-UIUC 联合学院、逐际动力 | 2026 | [[论文](https://arxiv.org/abs/2609.18108)] |
| <a id="p-tron2-garment-feeder"></a>🌟 **TRON2 服装送料**：在 506 段 TRON2 数据上微调的 Pi0.5 策略 | `TRON2` | voniu | 2026 | [[模型](https://huggingface.co/voniu/tron2-garment-feeder-button-pi05)] |
| <a id="p-tron2-lerobot-datasets"></a>🌟 **TRON2 LeRobot 数据集**：抓取、分拣、倒水、叠衣数据集及 GR00T 微调模型 | `TRON2` | trantor2nd | 2026 | [[数据集](https://huggingface.co/trantor2nd)] |

## 工具、仿真与 SDK

| 项目 | 机型 | 团队 | 年份 | 链接 |
|---|---|---|---|---|
| <a id="p-tron_deploy"></a>🌟 **Tron_Deploy**：从 Windows 11 笔记本向 TRON1 实机部署 ONNX 策略 | `TRON1` | candi4 | 2026 | [[代码](https://github.com/candi4/Tron_Deploy)] |
| <a id="p-limx-robotics-mcp"></a>🌟 **limx-robotics-mcp**：MCP 服务器，支持 MuJoCo 仿真、步态控制和策略推理 | `TRON1` `Oli` | sandraschi | 2026 | [[代码](https://github.com/sandraschi/limx-robotics-mcp)] |
| <a id="p-bipedal_locomotion_isaaclab"></a>🌟 **bipedal_locomotion_isaaclab**：基于 Isaac Lab 的平地、崎岖、楼梯地形训练，支持 sim2sim 和 sim2real | `TRON1` | 南方科技大学 | 2024 | [[代码](https://github.com/Andy-xiong6/bipedal_locomotion_isaaclab)] |

## 教学与竞赛

| 项目 | 机型 | 团队 | 年份 | 链接 |
|---|---|---|---|---|
| <a id="p-limx-tron1-learning"></a>**LimX Tron1 Learning**：用 Isaac Lab 训练 TRON1 的交互式教程 | `TRON1` | jessiezhg | 2026 | [[教程](https://huggingface.co/spaces/jessiezhg/LimX-Tron1-Learning)] |
| <a id="p-canton-tower-robot-climbing-challenge"></a>**广州塔机器人登高挑战赛**：冠军及最佳精准控制奖 | `Oli` | 逐际动力 | 2025 | [[成绩](https://www.sfccn.com/2026/1-1/5NMDE0NzNfMjA5MzM5NA.html)] [[论文](https://arxiv.org/abs/2601.10365)] |
| <a id="p-rl-bipedal-locomotion"></a>🌟 **双足运动强化学习**：南方科大 ACR2025 课程项目，基于 Isaac Lab | `TRON1` | 南方科技大学 | 2025 | [[代码](https://github.com/81578823/RL_bipedal_locomotion_Isaaclab)] |
| <a id="p-pointfootgym"></a>🌟 **pointfootGym**：点足机器人的 Isaac Gym / legged_gym 训练模板，用于南方科大 ACR 课程 | `TRON1` | 南方科技大学 CLEAR 实验室 | 2024 | [[代码](https://github.com/SuDaxia-kai/pointfootGym)] |

## 参与贡献

欢迎自荐，也欢迎推荐别人的工作。填写[提交表单](https://github.com/limxdynamics/awesome-limx/issues/new?template=add-project.yml)、提 Pull Request，或发邮件到 [opensource@limxdynamics.com](mailto:opensource@limxdynamics.com)。收录标准和格式见 [CONTRIBUTING_cn.md](CONTRIBUTING_cn.md)。

各分类内按时间从新到旧排列。感知与导航、行业应用等分类有了第一条收录后会出现在这里。

项目所有者可随时要求移除，无需说明理由：提 Issue 或发邮件即可。

## 许可

本列表以 [CC0 1.0](LICENSE) 发布。被收录的项目仍适用其各自的许可证。
