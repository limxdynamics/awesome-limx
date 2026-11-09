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

收录基于[逐际动力（LimX Dynamics）](https://www.limxdynamics.com)机器人（TRON1、TRON2、Oli、Luna）和 LimX SDK 完成的开源项目、论文、视频和比赛成果。

每一条都链接到公开的原始出处，方便直接查看大家用 LimX 硬件做出了什么。收录只说明该工作使用了 LimX 的硬件或软件，不代表逐际动力为该项目背书，项目的一切权利归原作者所有。

## 目录

- [运动控制](#运动控制)
- [感知与导航](#感知与导航)
- [操作](#操作)
- [具身智能](#具身智能)
- [工具、仿真与 SDK](#工具仿真与-sdk)
- [教学与竞赛](#教学与竞赛)
- [行业应用](#行业应用)
- [提交案例](#提交案例)
- [移除收录](#移除收录)

## 运动控制

_行走、奔跑、跳跃、上下楼梯、复杂地形通过、动作跟踪和全身控制，强化学习或模型方法均可。_

- **[Where-to-Learn：解析策略梯度引导的探索](https://wheretolearn.github.io)** — 用解析策略梯度引导同策略强化学习的探索，把训练出的速度跟踪策略迁移到点足 TRON1 实机上。<br>
  <sub>浙江大学、南方科技大学 · TRON1 · 2026 · [论文](https://arxiv.org/abs/2603.27317) · [视频](https://www.youtube.com/watch?v=DztdUyh_LVk)</sub>
- **[AME-2：基于注意力地图编码的敏捷足式运动](https://sites.google.com/leggedrobotics.com/ame-2)** — 训练了基于注意力地图编码的感知运动策略，在 TRON1 双足和 ANYmal-D 实机上运行。<br>
  <sub>苏黎世联邦理工学院机器人系统实验室 · TRON1 · 2026 · [论文](https://arxiv.org/abs/2601.08485)</sub>
- **[PvP：本体感知-特权信息对比表征](https://arxiv.org/abs/2512.13093)** — 用对比表征提升人形机器人强化学习的数据效率，在 Oli 上评估了速度跟踪和动作模仿。<br>
  <sub>香港理工大学、中国科学技术大学、逐际动力等 · Oli · 2025 · [论文](https://arxiv.org/abs/2512.13093)</sub>
- **[步态自适应的人形感知运动](https://ga-phl.github.io/)** — 实时重建机器人脚下地形，在楼梯和崎岖路面上自适应调整步态，在仿真和 Oli 实机上验证。<br>
  <sub>中国科学技术大学、逐际动力等 · Oli · 2025 · [论文](https://arxiv.org/abs/2512.07464)</sub>
- **[LIPM 引导的双足稳定感知运动强化学习](https://arxiv.org/abs/2509.09106)** — 把线性倒立摆模型引导与强化学习结合，将学生策略部署到点足 TRON1 上进行户外行走。<br>
  <sub>南方科技大学、香港科技大学、香港大学、浙大-UIUC 联合学院、逐际动力 · TRON1 · 2025 · [论文](https://arxiv.org/abs/2509.09106)</sub>
- **[CTBC：轮式双足机器人的接触触发盲爬](https://ctbc-for-wheeled-bipedal-robots.github.io/)** — 训练由轮子接触触发的盲爬台阶、马路牙子策略，部署在轮足 TRON1 上。<br>
  <sub>上海大学、酷哇机器人 · TRON1 · 2025 · [论文](https://arxiv.org/abs/2509.02986)</sub>
- **[BarlowWalk：面向地形自适应运动的自监督表征](https://arxiv.org/abs/2508.00939)** — 用 Barlow Twins 学习地形感知表征用于运动控制，在双足（sole-foot）形态的 TRON1 上做实验。<br>
  <sub>哈尔滨工业大学（深圳） · TRON1 · 2025 · [论文](https://arxiv.org/abs/2508.00939)</sub>

## 感知与导航

_建图、定位、路径规划、避障和自主导航。_

_暂无收录，欢迎[提交案例](#提交案例)。_

## 操作

_抓取、移动操作、遥操作和机械臂控制。_

- **[双足移动操作机器人的全身一体化移动操作](https://arxiv.org/abs/2609.18930)** — 在加装 ARX L5 机械臂的 TRON1 双足上学习行走与机械臂动作的协同。<br>
  <sub>浙大-UIUC 联合学院、逐际动力 · TRON1 · 2026 · [论文](https://arxiv.org/abs/2609.18930)</sub>
- **[CWI：面向移动操作的人形全身组合模仿系统](https://cwi-ral.github.io/CWI-RAL-Webpage/)** — 搭建了用于移动操作的全身模仿系统，部署在全尺寸 Oli 上。<br>
  <sub>逐际动力、香港大学、南方科技大学、香港科技大学、浙大-UIUC 联合学院 · Oli · 2026 · [论文](https://arxiv.org/abs/2606.27676)</sub>

## 具身智能

_在 LimX 机器人上运行的视觉-语言-动作模型（VLA）、大模型智能体、模仿学习和基础模型。_

- **[TRON2 服装送料 Pi0.5 策略](https://huggingface.co/voniu/tron2-garment-feeder-button-pi05)** — 用 506 段 TRON2 数据微调 Pi0.5 策略，完成把衣物放进送料机并按下按钮的任务。<br>
  <sub>voniu · TRON2 · 2026</sub>
- **[TRON2 LeRobot 数据集与 GR00T 微调模型](https://huggingface.co/trantor2nd)** — 发布了抓取、分拣、倒水、叠衣等 TRON2 LeRobot 格式数据集，并在其上微调了 NVIDIA GR00T 策略。<br>
  <sub>trantor2nd · TRON2 · 2026</sub>

## 工具、仿真与 SDK

_仿真环境、机器人模型、部署流程、Docker 镜像，以及基于 LimX SDK 开发的库。_

_暂无收录，欢迎[提交案例](#提交案例)。_

## 教学与竞赛

_课程、教学实验室、学生团队项目和比赛成绩。_

- **[LimX Tron1 Learning](https://huggingface.co/spaces/jessiezhg/LimX-Tron1-Learning)** — 中文交互式教程，讲解如何用 tron1-rl-isaaclab 训练 TRON1 运动策略，从强化学习基础讲到仿真环境搭建。<br>
  <sub>jessiezhg · TRON1 · 2026</sub>
- **[基于 Isaac Lab 的双足运动强化学习](https://github.com/81578823/RL_bipedal_locomotion_Isaaclab)** — 南方科技大学 ACR2025 课程项目：基于 Isaac Lab 的 TRON1 训练框架，覆盖点足、双足、轮足三种形态和平地、崎岖、楼梯地形。<br>
  <sub>南方科技大学 · TRON1 · 2025 · [代码](https://github.com/81578823/RL_bipedal_locomotion_Isaaclab)</sub>

## 行业应用

_企业的产品和实际落地项目。须经该企业同意后才会收录。_

_暂无收录，欢迎[提交案例](#提交案例)。_

## 提交案例

可以填写[提交表单](https://github.com/limxdynamics/awesome-limx/issues/new?template=add-project.yml)、直接提 Pull Request，或发邮件到 [opensource@limxdynamics.com](mailto:opensource@limxdynamics.com)。欢迎自荐，你自己写的介绍比我们猜的更准确。

每条案例的格式如下（仅为示例，并非真实项目）：

```markdown
- **[基于强化学习的楼梯攀爬](https://example.org/project)** — 在仿真中训练楼梯攀爬策略，不经微调直接部署到 TRON1 实机。<br>
  <sub>示例大学 · TRON1 · 2025 · [论文](https://arxiv.org/abs/0000.00000) · [代码](https://github.com/owner/repo) · [视频](https://www.bilibili.com/video/...)</sub>
```

收录标准：

1. **使用了 LimX 的硬件或软件**，实机或基于 LimX 官方模型的仿真均可，并且有公开资料能说明这一点：论文写明了机器人型号、视频里能看到机器人，或仓库 README 中有说明。
2. **有公开的原始出处链接**：代码仓库、论文或项目主页、视频，或比赛官方公布的成绩。
3. **企业项目须经该企业同意后才收录。** 别人的商业合作关系，不由我们抢先公布。
4. **只放链接。** 不转载代码、论文、视频或图片。

各分类内按时间从新到旧排列。完整规则见 [CONTRIBUTING_cn.md](CONTRIBUTING_cn.md)。

## 移除收录

项目所有者可以随时要求移除，无需说明理由。提 Issue 或发邮件到 [opensource@limxdynamics.com](mailto:opensource@limxdynamics.com)，我们会下架该条目。

## 许可

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，贡献者已放弃本列表的全部著作权及相关权利。被收录的项目仍适用其各自的许可证。详见 [LICENSE](LICENSE)。
