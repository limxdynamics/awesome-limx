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

> 每条都链接到公开原始出处。收录仅说明该工作使用了 LimX 硬件或软件，不代表逐际动力背书，权利归原作者所有。

## 目录

- [运动控制](#运动控制)（9）
- [操作](#操作)（4）
- [具身智能](#具身智能)（2）
- [工具、仿真与 SDK](#工具仿真与-sdk)（3）
- [教学与竞赛](#教学与竞赛)（3）
- [参与贡献](#参与贡献)

## 运动控制

| 项目 | 机型 | 团队 | 年份 | 链接 |
|---|---|---|---|---|
| **学习增强的 PMP-MPC**：点足双足的庞特里亚金 MPC，加入学习的动力学残差（ASCC 2026） | `TRON1` | Markwcl2004 | 2026 | [[论文](https://doi.org/10.1109/ASCC70886.2026.11701800)] [[代码](https://github.com/Markwcl2004/PMP_based_Bipedal_MPC)] |
| **Where-to-Learn**：解析策略梯度引导的同策略强化学习探索 | `TRON1` | 浙江大学、南方科技大学 | 2026 | [[主页](https://wheretolearn.github.io)] [[论文](https://arxiv.org/abs/2603.27317)] [[视频](https://www.youtube.com/watch?v=DztdUyh_LVk)] |
| **AME-2**：基于注意力地图编码的敏捷足式运动 | `TRON1` | 苏黎世联邦理工学院 | 2026 | [[主页](https://sites.google.com/leggedrobotics.com/ame-2)] [[论文](https://arxiv.org/abs/2601.08485)] |
| **PvP**：基于本体-特权对比表征的高效人形机器人学习 | `Oli` | 香港理工、中国科大、逐际动力等 | 2025 | [[论文](https://arxiv.org/abs/2512.13093)] |
| **GA-PHL**：实时地形重建的步态自适应人形感知运动 | `Oli` | 中国科大、逐际动力等 | 2025 | [[主页](https://ga-phl.github.io/)] [[论文](https://arxiv.org/abs/2512.07464)] |
| **LIPM 引导强化学习**：点足双足的稳定感知运动 | `TRON1` | 南方科大、港科大、港大等 | 2025 | [[论文](https://arxiv.org/abs/2509.09106)] |
| **CTBC**：轮式双足机器人的接触触发盲爬 | `TRON1` | 上海大学 | 2025 | [[主页](https://ctbc-for-wheeled-bipedal-robots.github.io/)] [[论文](https://arxiv.org/abs/2509.02986)] |
| **BarlowWalk**：面向地形自适应运动的自监督表征 | `TRON1` | 哈工大（深圳） | 2025 | [[论文](https://arxiv.org/abs/2508.00939)] |
| **双足 MPC**：MuJoCo 中的凸 MPC 与全身控制，基于 ROS 2 | `TRON1` | 南方科技大学 CLEAR 实验室 | 2024 | [[代码](https://github.com/clearlab-sustech/Bipedal_MPC)] |

## 操作

| 项目 | 机型 | 团队 | 年份 | 链接 |
|---|---|---|---|---|
| **全身一体化移动操作**：双足移动操作机器人（TRON1 加装机械臂） | `TRON1` | 浙大-UIUC 联合学院、逐际动力 | 2026 | [[论文](https://arxiv.org/abs/2609.18930)] |
| **TRON1 与 UR5e 交接水瓶**：TRON1 运送水瓶并对接，UR5e 用 MoveIt 2 抓取（MuJoCo、ROS 2） | `TRON1` | Centaucyan | 2026 | [[代码](https://github.com/Centaucyan/Proj_Transferring_bottle_from_tron1_to_ur5e_in_mujoco_env)] |
| **多机协同搬运**：两台带机械臂的轮足 TRON 在 MuJoCo 中协同搬运 | `TRON1` `TRON2` | Matt14-mander | 2026 | [[代码](https://github.com/Matt14-mander/Multiple_Humanoid_Cooperative_Transportation)] |
| **CWI**：面向移动操作的人形全身组合模仿 | `Oli` | 逐际动力、港大、南方科大等 | 2026 | [[主页](https://cwi-ral.github.io/CWI-RAL-Webpage/)] [[论文](https://arxiv.org/abs/2606.27676)] |

## 具身智能

| 项目 | 机型 | 团队 | 年份 | 链接 |
|---|---|---|---|---|
| **TRON2 服装送料**：在 506 段 TRON2 数据上微调的 Pi0.5 策略 | `TRON2` | voniu | 2026 | [[模型](https://huggingface.co/voniu/tron2-garment-feeder-button-pi05)] |
| **TRON2 LeRobot 数据集**：抓取、分拣、倒水、叠衣数据集及 GR00T 微调模型 | `TRON2` | trantor2nd | 2026 | [[数据集](https://huggingface.co/trantor2nd)] |

## 工具、仿真与 SDK

| 项目 | 机型 | 团队 | 年份 | 链接 |
|---|---|---|---|---|
| **Tron_Deploy**：从 Windows 11 笔记本向 TRON1 实机部署 ONNX 策略 | `TRON1` | candi4 | 2026 | [[代码](https://github.com/candi4/Tron_Deploy)] |
| **limx-robotics-mcp**：MCP 服务器，支持 MuJoCo 仿真、步态控制和策略推理 | `TRON1` `Oli` | sandraschi | 2026 | [[代码](https://github.com/sandraschi/limx-robotics-mcp)] |
| **bipedal_locomotion_isaaclab**：基于 Isaac Lab 的平地、崎岖、楼梯地形训练，支持 sim2sim 和 sim2real | `TRON1` | 南方科技大学 | 2024 | [[代码](https://github.com/Andy-xiong6/bipedal_locomotion_isaaclab)] |

## 教学与竞赛

| 项目 | 机型 | 团队 | 年份 | 链接 |
|---|---|---|---|---|
| **LimX Tron1 Learning**：用 Isaac Lab 训练 TRON1 的交互式教程 | `TRON1` | jessiezhg | 2026 | [[教程](https://huggingface.co/spaces/jessiezhg/LimX-Tron1-Learning)] |
| **双足运动强化学习**：南方科大 ACR2025 课程项目，基于 Isaac Lab | `TRON1` | 南方科技大学 | 2025 | [[代码](https://github.com/81578823/RL_bipedal_locomotion_Isaaclab)] |
| **pointfootGym**：点足机器人的 Isaac Gym / legged_gym 训练模板，用于南方科大 ACR 课程 | `TRON1` | 南方科技大学 CLEAR 实验室 | 2024 | [[代码](https://github.com/SuDaxia-kai/pointfootGym)] |

## 参与贡献

欢迎自荐，也欢迎推荐别人的工作。填写[提交表单](https://github.com/limxdynamics/awesome-limx/issues/new?template=add-project.yml)、提 Pull Request，或发邮件到 [opensource@limxdynamics.com](mailto:opensource@limxdynamics.com)。收录标准和格式见 [CONTRIBUTING_cn.md](CONTRIBUTING_cn.md)。

各分类内按时间从新到旧排列。感知与导航、行业应用等分类有了第一条收录后会出现在这里。

项目所有者可随时要求移除，无需说明理由：提 Issue 或发邮件即可。

## 许可

本列表以 [CC0 1.0](LICENSE) 发布。被收录的项目仍适用其各自的许可证。
