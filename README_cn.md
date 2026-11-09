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

收录所有使用 LimX 硬件或软件的公开成果：论文、开源代码、数据集、教程和比赛成绩。官方开源仓库请见 [GitHub](https://github.com/limxdynamics) 和 [Hugging Face](https://huggingface.co/limxdynamics)。

**42** 个项目 · **20** 个开源 🌟 ｜ [运动控制](#运动控制) 19 · [操作](#操作) 6 · [具身智能](#具身智能) 5 · [工具、仿真与 SDK](#工具仿真与-sdk) 7 · [教学与竞赛](#教学与竞赛) 5 · [参与贡献](#参与贡献)

<details>
<summary><b>按机型查找</b>：TRON1 25 · TRON2 6 · Oli 11 · Luna 1 · P1 3 · W1 1</summary>

- **TRON1**：[TRON1 打滑分析](#p-tron1-sliding-analysis) · [学习增强的 PMP-MPC](#p-learning-enhanced-pmp-mpc) · [TRON1 轮足舞蹈模仿](#p-tron1-wf-mimic) · [Where-to-Learn](#p-where-to-learn) · [AME-2](#p-ame-2) · [LIPM 引导强化学习](#p-lipm-guided-rl) · [CTBC](#p-ctbc) · [BarlowWalk](#p-barlowwalk) · [多本体动作重定向](#p-multi-embodiment-retargeting) · [双足 MPC](#p-bipedal-mpc) · [全身一体化移动操作](#p-holistic-loco-manipulation) · [TRON1 与 UR5e 交接水瓶](#p-tron1-to-ur5e-bottle-transfer) · [多机协同搬运](#p-cooperative-transportation) · [Arm-TRON](#p-arm-tron) · [wf_tron1b_deploy](#p-wf_tron1b_deploy) · [Tron_Deploy](#p-tron_deploy) · [limx-3d-measurement-workbench](#p-limx-3d-measurement-workbench) · [limx-robotics-mcp](#p-limx-robotics-mcp) · [tron_docker_sim](#p-tron_docker_sim) · [tron1-rl-mjlab](#p-tron1-rl-mjlab) · [bipedal_locomotion_isaaclab](#p-bipedal_locomotion_isaaclab) · [OpenArm 移动操作实训](#p-openarm-mobile-manipulation-lab) · [LimX Tron1 Learning](#p-limx-tron1-learning) · [双足运动强化学习](#p-rl-bipedal-locomotion) · [pointfootGym](#p-pointfootgym)
- **TRON2**：[多机协同搬运](#p-cooperative-transportation) · [ACG-WAM](#p-acg-wam) · [GR00T 漂移动作头](#p-drifting-action-heads-for-gr00t-n17) · [TRON2 服装送料](#p-tron2-garment-feeder) · [TRON2 LeRobot 数据集](#p-tron2-lerobot-datasets) · [limx-3d-measurement-workbench](#p-limx-3d-measurement-workbench)
- **Oli**：[SuperMimic for Oli](#p-supermimic-for-oli) · [VAPS](#p-vaps) · [Any2Any](#p-any2any) · [FastStair](#p-faststair) · [PvP](#p-pvp) · [GA-PHL](#p-ga-phl) · [多本体动作重定向](#p-multi-embodiment-retargeting) · [CWI](#p-cwi) · [HWAM](#p-hwam) · [limx-robotics-mcp](#p-limx-robotics-mcp) · [广州塔机器人登高挑战赛](#p-canton-tower-robot-climbing-challenge)
- **Luna**：[Any2Any](#p-any2any)
- **P1**：[VMTS](#p-vmts) · [CTS](#p-cts) · [任务空间 Riccati 全身控制](#p-task-space-riccati-wbc)
- **W1**：[轮足四足移动操作](#p-wheeled-quadrupedal-manipulator)

</details>

## 运动控制

| 项目 | 机型 | 团队 | 年份 | 链接 |
|---|---|---|---|---|
| <a id="p-tron1-sliding-analysis"></a>🌟 **TRON1 打滑分析**：轮足漂移与摩擦迁移（仿真） | `TRON1` | Shukashuki | 2026 | [[代码](https://github.com/Shukashuki/tron1-sliding-analysis)] |
| <a id="p-learning-enhanced-pmp-mpc"></a>🌟 **学习增强的 PMP-MPC**：点足双足的学习增强 MPC | `TRON1` | Markwcl2004 | 2026 | [[论文](https://doi.org/10.1109/ASCC70886.2026.11701800)] [[代码](https://github.com/Markwcl2004/PMP_based_Bipedal_MPC)] |
| <a id="p-supermimic-for-oli"></a>🌟 **SuperMimic for Oli**：单策略跟踪 40 段动作（仿真） | `Oli` | Tianxing Liu | 2026 | [[代码](https://github.com/liuskywalkerjskd/supermimic_oli)] |
| <a id="p-vaps"></a>**VAPS**：安全特技动作，实机侧空翻 | `Oli` | 达姆施塔特工业大学、逐际动力等 | 2026 | [[主页](https://vaps-r-al.github.io/)] [[论文](https://arxiv.org/abs/2610.01397)] |
| <a id="p-tron1-wf-mimic"></a>🌟 **TRON1 轮足舞蹈模仿**：舞蹈模仿与可行性分析（仿真） | `TRON1` | HUST-dolores | 2026 | [[代码](https://github.com/HUST-dolores/tron1-wf-mimic)] |
| <a id="p-any2any"></a>**Any2Any**：跨本体全身动作跟踪 | `Oli` `Luna` | 逐际动力 | 2026 | [[论文](https://arxiv.org/abs/2605.23733)] |
| <a id="p-where-to-learn"></a>**Where-to-Learn**：梯度引导的强化学习探索 | `TRON1` | 浙江大学、南方科技大学 | 2026 | [[主页](https://wheretolearn.github.io)] [[论文](https://arxiv.org/abs/2603.27317)] [[视频](https://www.youtube.com/watch?v=DztdUyh_LVk)] |
| <a id="p-faststair"></a>**FastStair**：快速跑楼梯 | `Oli` | 哈工大、逐际动力等 | 2026 | [[主页](https://npcliu.github.io/FastStair)] [[论文](https://arxiv.org/abs/2601.10365)] [[视频](https://youtu.be/SoLBK7VEGDo)] |
| <a id="p-ame-2"></a>**AME-2**：敏捷感知运动 | `TRON1` | 苏黎世联邦理工学院 | 2026 | [[主页](https://sites.google.com/leggedrobotics.com/ame-2)] [[论文](https://arxiv.org/abs/2601.08485)] |
| <a id="p-pvp"></a>**PvP**：高效的人形强化学习 | `Oli` | 香港理工、中国科大等 | 2025 | [[论文](https://arxiv.org/abs/2512.13093)] |
| <a id="p-ga-phl"></a>**GA-PHL**：步态自适应感知行走 | `Oli` | 中国科大、逐际动力等 | 2025 | [[主页](https://ga-phl.github.io/)] [[论文](https://arxiv.org/abs/2512.07464)] |
| <a id="p-lipm-guided-rl"></a>**LIPM 引导强化学习**：稳定的双足感知行走 | `TRON1` | 南方科大、港科大等 | 2025 | [[论文](https://arxiv.org/abs/2509.09106)] |
| <a id="p-ctbc"></a>**CTBC**：轮足盲爬台阶 | `TRON1` | 上海大学、酷哇机器人 | 2025 | [[主页](https://ctbc-for-wheeled-bipedal-robots.github.io/)] [[论文](https://arxiv.org/abs/2509.02986)] |
| <a id="p-barlowwalk"></a>**BarlowWalk**：地形自适应运动 | `TRON1` | 哈工大（深圳） | 2025 | [[论文](https://arxiv.org/abs/2508.00939)] |
| <a id="p-multi-embodiment-retargeting"></a>**多本体动作重定向**：扩散模型动作重定向 | `Oli` `TRON1` | 南方科大、港科大等 | 2025 | [[论文](https://arxiv.org/abs/2505.20857)] |
| <a id="p-vmts"></a>**VMTS**：视觉辅助多地形行走 | `P1` | 东南大学 | 2025 | [[论文](https://arxiv.org/abs/2503.07049)] |
| <a id="p-bipedal-mpc"></a>🌟 **双足 MPC**：MuJoCo 中的 MPC 与全身控制 | `TRON1` | 南方科技大学 CLEAR 实验室 | 2024 | [[代码](https://github.com/clearlab-sustech/Bipedal_MPC)] |
| <a id="p-cts"></a>**CTS**：并行师生强化学习 | `P1` | 南方科大、浙大-UIUC等 | 2024 | [[主页](https://clearlab-sustech.github.io/concurrentTS/)] [[论文](https://arxiv.org/abs/2405.10830)] |
| <a id="p-task-space-riccati-wbc"></a>**任务空间 Riccati 全身控制**：全身控制（仿真） | `P1` | 南方科大、港科大等 | 2024 | [[论文](https://arxiv.org/abs/2404.00591)] |

## 操作

| 项目 | 机型 | 团队 | 年份 | 链接 |
|---|---|---|---|---|
| <a id="p-holistic-loco-manipulation"></a>**全身一体化移动操作**：TRON1 加机械臂 | `TRON1` | 浙大-UIUC、逐际动力 | 2026 | [[论文](https://arxiv.org/abs/2609.18930)] |
| <a id="p-tron1-to-ur5e-bottle-transfer"></a>🌟 **TRON1 与 UR5e 交接水瓶**：ROS 2 与 MuJoCo（仿真） | `TRON1` | Centaucyan | 2026 | [[代码](https://github.com/Centaucyan/Proj_Transferring_bottle_from_tron1_to_ur5e_in_mujoco_env)] |
| <a id="p-cooperative-transportation"></a>🌟 **多机协同搬运**：两台轮足协同搬运（仿真） | `TRON1` `TRON2` | Matt14-mander | 2026 | [[代码](https://github.com/Matt14-mander/Multiple_Humanoid_Cooperative_Transportation)] |
| <a id="p-cwi"></a>**CWI**：全身模仿移动操作 | `Oli` | 逐际动力、港大等 | 2026 | [[主页](https://cwi-ral.github.io/CWI-RAL-Webpage/)] [[论文](https://arxiv.org/abs/2606.27676)] |
| <a id="p-arm-tron"></a>**Arm-TRON**：可变足型双足加机械臂 | `TRON1` | 南方科大、浙江大学等 | 2026 | [[论文](https://doi.org/10.1109/TMECH.2026.3727546)] |
| <a id="p-wheeled-quadrupedal-manipulator"></a>**轮足四足移动操作**：W1 加机械臂位姿跟踪 | `W1` | 南方科大、浙大-UIUC等 | 2024 | [[论文](https://arxiv.org/abs/2412.03012)] |

## 具身智能

| 项目 | 机型 | 团队 | 年份 | 链接 |
|---|---|---|---|---|
| <a id="p-hwam"></a>**HWAM**：人形世界动作模型 | `Oli` | 逐际动力 | 2026 | [[主页](https://hwam.vercel.app/)] [[论文](https://arxiv.org/abs/2610.12026)] |
| <a id="p-acg-wam"></a>🌟 **ACG-WAM**：灵巧手世界-动作模型 | `TRON2` | 北京理工大学、逐际动力 | 2026 | [[主页](https://RoboOpus.github.io/ACG-WAM)] [[论文](https://arxiv.org/abs/2610.06965)] [[代码](https://github.com/RoboOpus/ACG-WAM)] |
| <a id="p-drifting-action-heads-for-gr00t-n17"></a>**GR00T 漂移动作头**：单步动作头 | `TRON2` | 浙大-UIUC、逐际动力 | 2026 | [[论文](https://arxiv.org/abs/2609.18108)] |
| <a id="p-tron2-garment-feeder"></a>🌟 **TRON2 服装送料**：Pi0.5 策略 | `TRON2` | voniu | 2026 | [[模型](https://huggingface.co/voniu/tron2-garment-feeder-button-pi05)] |
| <a id="p-tron2-lerobot-datasets"></a>🌟 **TRON2 LeRobot 数据集**：数据集与 GR00T 微调模型 | `TRON2` | trantor2nd | 2026 | [[数据集](https://huggingface.co/trantor2nd)] |

## 工具、仿真与 SDK

| 项目 | 机型 | 团队 | 年份 | 链接 |
|---|---|---|---|---|
| <a id="p-wf_tron1b_deploy"></a>🌟 **wf_tron1b_deploy**：深度感知策略 sim2sim 部署 | `TRON1` | Leixin Chang | 2026 | [[代码](https://github.com/Leixinjonaschang/wf_tron1b_deploy)] |
| <a id="p-tron_deploy"></a>🌟 **Tron_Deploy**：在 Windows 上部署策略 | `TRON1` | candi4 | 2026 | [[代码](https://github.com/candi4/Tron_Deploy)] |
| <a id="p-limx-3d-measurement-workbench"></a>🌟 **limx-3d-measurement-workbench**：浏览 TRON 模型、测量尺寸 | `TRON1` `TRON2` | voniu | 2026 | [[代码](https://github.com/voniu/limx-3d-measurement-workbench)] |
| <a id="p-limx-robotics-mcp"></a>🌟 **limx-robotics-mcp**：仿真与控制的 MCP 服务器 | `TRON1` `Oli` | sandraschi | 2026 | [[代码](https://github.com/sandraschi/limx-robotics-mcp)] |
| <a id="p-tron_docker_sim"></a>🌟 **tron_docker_sim**：Gazebo 仿真 Docker 环境 | `TRON1` | The-RoboTUM | 2026 | [[代码](https://github.com/The-RoboTUM/tron_docker_sim)] |
| <a id="p-tron1-rl-mjlab"></a>🌟 **tron1-rl-mjlab**：基于 mjlab 的轮足训练 | `TRON1` | Xinchen Yao | 2025 | [[代码](https://github.com/hoscy/tron1-rl-mjlab)] |
| <a id="p-bipedal_locomotion_isaaclab"></a>🌟 **bipedal_locomotion_isaaclab**：Isaac Lab 训练与实机部署 | `TRON1` | 南方科技大学 | 2024 | [[代码](https://github.com/Andy-xiong6/bipedal_locomotion_isaaclab)] |

## 教学与竞赛

| 项目 | 机型 | 团队 | 年份 | 链接 |
|---|---|---|---|---|
| <a id="p-openarm-mobile-manipulation-lab"></a>🌟 **OpenArm 移动操作实训**：TRON1 加 OpenArm 双臂，大模型任务（仿真，韩语） | `TRON1` | aha645 | 2026 | [[代码](https://github.com/aha645/openarms_llm_ex)] |
| <a id="p-limx-tron1-learning"></a>**LimX Tron1 Learning**：Isaac Lab 交互式教程 | `TRON1` | jessiezhg | 2026 | [[教程](https://huggingface.co/spaces/jessiezhg/LimX-Tron1-Learning)] |
| <a id="p-canton-tower-robot-climbing-challenge"></a>**广州塔机器人登高挑战赛**：冠军、最佳精准控制奖 | `Oli` | 逐际动力 | 2025 | [[成绩](https://www.sfccn.com/2026/1-1/5NMDE0NzNfMjA5MzM5NA.html)] [[论文](https://arxiv.org/abs/2601.10365)] |
| <a id="p-rl-bipedal-locomotion"></a>🌟 **双足运动强化学习**：南方科大 ACR2025 课程项目 | `TRON1` | 南方科技大学 | 2025 | [[代码](https://github.com/81578823/RL_bipedal_locomotion_Isaaclab)] |
| <a id="p-pointfootgym"></a>🌟 **pointfootGym**：Isaac Gym 课程模板 | `TRON1` | 南方科技大学 CLEAR 实验室 | 2024 | [[代码](https://github.com/SuDaxia-kai/pointfootGym)] |

## 参与贡献

欢迎自荐，也欢迎推荐别人的工作：填写[提交表单](https://github.com/limxdynamics/awesome-limx/issues/new?template=add-project.yml)、提 Pull Request，或发邮件到 [opensource@limxdynamics.com](mailto:opensource@limxdynamics.com)。收录标准见 [CONTRIBUTING_cn.md](CONTRIBUTING_cn.md)。各分类内按时间从新到旧排列；🌟 表示提供了代码、模型或数据集。

收录不代表逐际动力背书，权利归原作者所有。项目所有者可随时要求移除，无需说明理由。

## 许可

本列表以 [CC0 1.0](LICENSE) 发布。被收录的项目仍适用其各自的许可证。
