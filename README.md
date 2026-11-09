<div align="center">

<a href="README.md"><img src="https://img.shields.io/badge/English-24292f?style=for-the-badge" alt="English"></a>&nbsp;&nbsp;<a href="README_cn.md"><img src="https://img.shields.io/badge/Chinese-24292f?style=for-the-badge" alt="Chinese"></a>

</div>

<p align="center"><img src="assets/banner.png" alt="Awesome LimX" width="100%"></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-CC0--1.0-2f6feb" alt="License: CC0-1.0"></a>
  <a href="https://github.com/limxdynamics/limxdynamics/blob/main/doc/wechat_qr.png"><img src="https://img.shields.io/badge/WeChat-Developer%20Community-07C160?logo=wechat&logoColor=white" alt="WeChat Community"></a>
</p>
<p align="center"><sub>For partnership and procurement inquiries, contact <a href="mailto:opensource@limxdynamics.com">opensource@limxdynamics.com</a></sub></p>

Open-source projects, papers and competition results built on [LimX Dynamics](https://www.limxdynamics.com) robots (TRON1, TRON2, Oli, Luna) and the LimX SDK.

> This list covers public work that uses LimX hardware or software, by universities, individuals and LimX researchers alike. LimX's own open-source releases live on [GitHub](https://github.com/limxdynamics) and [Hugging Face](https://huggingface.co/limxdynamics). Every entry links to its original source; a listing is not an endorsement, and all rights stay with the owners.

**31 projects, 12 open source (🌟)**, covering TRON1 (17), TRON2 (3), Oli (10), Luna (1), P1 (3), W1 (1).

## Contents

- [By robot](#by-robot)
- [Locomotion & whole-body control](#locomotion--whole-body-control) (16)
- [Manipulation](#manipulation) (5)
- [Embodied AI](#embodied-ai) (3)
- [Tools, simulation & SDK](#tools-simulation--sdk) (3)
- [Education & competitions](#education--competitions) (4)
- [Contributing](#contributing)

## By robot

- **TRON1** (17): [Learning-Enhanced PMP-MPC](#p-learning-enhanced-pmp-mpc) · [Where-to-Learn](#p-where-to-learn) · [AME-2](#p-ame-2) · [LIPM-Guided RL](#p-lipm-guided-rl) · [CTBC](#p-ctbc) · [BarlowWalk](#p-barlowwalk) · [Multi-Embodiment Retargeting](#p-multi-embodiment-retargeting) · [Bipedal MPC](#p-bipedal-mpc) · [Holistic Loco-Manipulation](#p-holistic-loco-manipulation) · [TRON1-to-UR5e Bottle Transfer](#p-tron1-to-ur5e-bottle-transfer) · [Cooperative Transportation](#p-cooperative-transportation) · [Tron_Deploy](#p-tron_deploy) · [limx-robotics-mcp](#p-limx-robotics-mcp) · [bipedal_locomotion_isaaclab](#p-bipedal_locomotion_isaaclab) · [LimX Tron1 Learning](#p-limx-tron1-learning) · [RL Bipedal Locomotion](#p-rl-bipedal-locomotion) · [pointfootGym](#p-pointfootgym)
- **TRON2** (3): [Cooperative Transportation](#p-cooperative-transportation) · [TRON2 Garment Feeder](#p-tron2-garment-feeder) · [TRON2 LeRobot Datasets](#p-tron2-lerobot-datasets)
- **Oli** (10): [SuperMimic for Oli](#p-supermimic-for-oli) · [Any2Any](#p-any2any) · [FastStair](#p-faststair) · [PvP](#p-pvp) · [GA-PHL](#p-ga-phl) · [Multi-Embodiment Retargeting](#p-multi-embodiment-retargeting) · [CWI](#p-cwi) · [HWAM](#p-hwam) · [limx-robotics-mcp](#p-limx-robotics-mcp) · [Canton Tower Robot Climbing Challenge](#p-canton-tower-robot-climbing-challenge)
- **Luna** (1): [Any2Any](#p-any2any)
- **P1** (3): [VMTS](#p-vmts) · [CTS](#p-cts) · [Task-Space Riccati WBC](#p-task-space-riccati-wbc)
- **W1** (1): [Wheeled-Quadrupedal Manipulator](#p-wheeled-quadrupedal-manipulator)

## Locomotion & whole-body control

| Project | Robot | Team | Year | Links |
|---|---|---|---|---|
| <a id="p-learning-enhanced-pmp-mpc"></a>🌟 **Learning-Enhanced PMP-MPC**: Pontryagin-based MPC with a learned dynamics residual for a point-foot biped (ASCC 2026) | `TRON1` | Markwcl2004 | 2026 | [[paper](https://doi.org/10.1109/ASCC70886.2026.11701800)] [[code](https://github.com/Markwcl2004/PMP_based_Bipedal_MPC)] |
| <a id="p-supermimic-for-oli"></a>🌟 **SuperMimic for Oli**: one policy tracking 40 LAFAN1 motions on a 31-DoF Oli in Isaac Lab / MuJoCo-Warp | `Oli` | Tianxing Liu | 2026 | [[code](https://github.com/liuskywalkerjskd/supermimic_oli)] |
| <a id="p-any2any"></a>**Any2Any**: efficient cross-embodiment transfer for humanoid whole-body tracking | `Oli` `Luna` | LimX | 2026 | [[paper](https://arxiv.org/abs/2605.23733)] |
| <a id="p-where-to-learn"></a>**Where-to-Learn**: analytical policy gradient directed exploration for on-policy RL | `TRON1` | ZJU, SUSTech | 2026 | [[project](https://wheretolearn.github.io)] [[paper](https://arxiv.org/abs/2603.27317)] [[video](https://www.youtube.com/watch?v=DztdUyh_LVk)] |
| <a id="p-faststair"></a>**FastStair**: learning to run up stairs on a full-size humanoid | `Oli` | HIT, LimX et al. | 2026 | [[project](https://npcliu.github.io/FastStair)] [[paper](https://arxiv.org/abs/2601.10365)] [[video](https://youtu.be/SoLBK7VEGDo)] |
| <a id="p-ame-2"></a>**AME-2**: agile legged locomotion via attention-based neural map encoding | `TRON1` | ETH Zurich | 2026 | [[project](https://sites.google.com/leggedrobotics.com/ame-2)] [[paper](https://arxiv.org/abs/2601.08485)] |
| <a id="p-pvp"></a>**PvP**: data-efficient humanoid learning with proprioceptive-privileged contrastive representations | `Oli` | PolyU, USTC, LimX et al. | 2025 | [[paper](https://arxiv.org/abs/2512.13093)] |
| <a id="p-ga-phl"></a>**GA-PHL**: gait-adaptive perceptive humanoid locomotion with real-time terrain reconstruction | `Oli` | USTC, LimX et al. | 2025 | [[project](https://ga-phl.github.io/)] [[paper](https://arxiv.org/abs/2512.07464)] |
| <a id="p-lipm-guided-rl"></a>**LIPM-Guided RL**: stable and perceptive locomotion for point-foot bipeds | `TRON1` | SUSTech, HKUST, HKU et al. | 2025 | [[paper](https://arxiv.org/abs/2509.09106)] |
| <a id="p-ctbc"></a>**CTBC**: contact-triggered blind climbing for wheeled bipedal robots | `TRON1` | Shanghai University, COWAROBOT | 2025 | [[project](https://ctbc-for-wheeled-bipedal-robots.github.io/)] [[paper](https://arxiv.org/abs/2509.02986)] |
| <a id="p-barlowwalk"></a>**BarlowWalk**: self-supervised representations for terrain-adaptive locomotion | `TRON1` | HIT Shenzhen | 2025 | [[paper](https://arxiv.org/abs/2508.00939)] |
| <a id="p-multi-embodiment-retargeting"></a>**Multi-Embodiment Retargeting**: motion retargeting to Oli, TRON1 and other robots via a guided diffusion model | `Oli` `TRON1` | SUSTech, HKUST, ZJU-UIUC, LimX | 2025 | [[paper](https://arxiv.org/abs/2505.20857)] |
| <a id="p-vmts"></a>**VMTS**: vision-assisted teacher-student RL for multi-terrain bipedal locomotion, deployed on P1 | `P1` | Southeast University | 2025 | [[paper](https://arxiv.org/abs/2503.07049)] |
| <a id="p-bipedal-mpc"></a>🌟 **Bipedal MPC**: convex MPC and whole-body control in MuJoCo with ROS 2 | `TRON1` | SUSTech CLEAR Lab | 2024 | [[code](https://github.com/clearlab-sustech/Bipedal_MPC)] |
| <a id="p-cts"></a>**CTS**: concurrent teacher-student RL for legged locomotion, tested on the point-foot P1 | `P1` | SUSTech, ZJU-UIUC, LimX | 2024 | [[project](https://clearlab-sustech.github.io/concurrentTS/)] [[paper](https://arxiv.org/abs/2405.10830)] |
| <a id="p-task-space-riccati-wbc"></a>**Task-Space Riccati WBC**: whole-body control for underactuated legged locomotion, tested on P1 in simulation | `P1` | SUSTech, HKUST, Notre Dame | 2024 | [[paper](https://arxiv.org/abs/2404.00591)] |

## Manipulation

| Project | Robot | Team | Year | Links |
|---|---|---|---|---|
| <a id="p-holistic-loco-manipulation"></a>**Holistic Loco-Manipulation**: whole-body loco-manipulation with a bipedal mobile manipulator (TRON1 + arm) | `TRON1` | ZJU-UIUC, LimX | 2026 | [[paper](https://arxiv.org/abs/2609.18930)] |
| <a id="p-tron1-to-ur5e-bottle-transfer"></a>🌟 **TRON1-to-UR5e Bottle Transfer**: TRON1 docks with a load of bottles, then a UR5e picks them with MoveIt 2 (MuJoCo, ROS 2) | `TRON1` | Centaucyan | 2026 | [[code](https://github.com/Centaucyan/Proj_Transferring_bottle_from_tron1_to_ur5e_in_mujoco_env)] |
| <a id="p-cooperative-transportation"></a>🌟 **Cooperative Transportation**: two wheel-legged TRONs with arms carrying a payload together in MuJoCo | `TRON1` `TRON2` | Matt14-mander | 2026 | [[code](https://github.com/Matt14-mander/Multiple_Humanoid_Cooperative_Transportation)] |
| <a id="p-cwi"></a>**CWI**: composite humanoid whole-body imitation for loco-manipulation | `Oli` | LimX, HKU, SUSTech et al. | 2026 | [[project](https://cwi-ral.github.io/CWI-RAL-Webpage/)] [[paper](https://arxiv.org/abs/2606.27676)] |
| <a id="p-wheeled-quadrupedal-manipulator"></a>**Wheeled-Quadrupedal Manipulator**: whole-body loco-manipulation for omni-directional pose tracking on W1 with an AIRBOT arm | `W1` | SUSTech, ZJU-UIUC, LimX | 2024 | [[paper](https://arxiv.org/abs/2412.03012)] |

## Embodied AI

| Project | Robot | Team | Year | Links |
|---|---|---|---|---|
| <a id="p-hwam"></a>**HWAM**: humanoid world action model with joint state-action generation, on a 31-DoF Oli | `Oli` | LimX | 2026 | [[project](https://hwam.vercel.app/)] [[paper](https://arxiv.org/abs/2610.12026)] |
| <a id="p-tron2-garment-feeder"></a>🌟 **TRON2 Garment Feeder**: Pi0.5 policy fine-tuned on 506 TRON2 episodes | `TRON2` | voniu | 2026 | [[model](https://huggingface.co/voniu/tron2-garment-feeder-button-pi05)] |
| <a id="p-tron2-lerobot-datasets"></a>🌟 **TRON2 LeRobot Datasets**: pick, sort, pour and fold datasets, with GR00T fine-tunes | `TRON2` | trantor2nd | 2026 | [[dataset](https://huggingface.co/trantor2nd)] |

## Tools, simulation & SDK

| Project | Robot | Team | Year | Links |
|---|---|---|---|---|
| <a id="p-tron_deploy"></a>🌟 **Tron_Deploy**: deploying ONNX policies to a real TRON1 from a Windows 11 laptop | `TRON1` | candi4 | 2026 | [[code](https://github.com/candi4/Tron_Deploy)] |
| <a id="p-limx-robotics-mcp"></a>🌟 **limx-robotics-mcp**: MCP server for MuJoCo simulation, gait control and policy inference | `TRON1` `Oli` | sandraschi | 2026 | [[code](https://github.com/sandraschi/limx-robotics-mcp)] |
| <a id="p-bipedal_locomotion_isaaclab"></a>🌟 **bipedal_locomotion_isaaclab**: Isaac Lab training for flat, rough and stair terrain, with sim-to-sim and sim-to-real | `TRON1` | SUSTech | 2024 | [[code](https://github.com/Andy-xiong6/bipedal_locomotion_isaaclab)] |

## Education & competitions

| Project | Robot | Team | Year | Links |
|---|---|---|---|---|
| <a id="p-limx-tron1-learning"></a>**LimX Tron1 Learning**: interactive guide to training TRON1 with Isaac Lab (Chinese) | `TRON1` | jessiezhg | 2026 | [[tutorial](https://huggingface.co/spaces/jessiezhg/LimX-Tron1-Learning)] |
| <a id="p-canton-tower-robot-climbing-challenge"></a>**Canton Tower Robot Climbing Challenge**: champion and best precision control award | `Oli` | LimX | 2025 | [[result](https://www.sfccn.com/2026/1-1/5NMDE0NzNfMjA5MzM5NA.html)] [[paper](https://arxiv.org/abs/2601.10365)] |
| <a id="p-rl-bipedal-locomotion"></a>🌟 **RL Bipedal Locomotion**: SUSTech ACR2025 course project on Isaac Lab | `TRON1` | SUSTech | 2025 | [[code](https://github.com/81578823/RL_bipedal_locomotion_Isaaclab)] |
| <a id="p-pointfootgym"></a>🌟 **pointfootGym**: Isaac Gym and legged_gym template for point-foot robots, used in SUSTech's ACR course | `TRON1` | SUSTech CLEAR Lab | 2024 | [[code](https://github.com/SuDaxia-kai/pointfootGym)] |

## Contributing

Self-nominations and suggestions are welcome. Use the [submission form](https://github.com/limxdynamics/awesome-limx/issues/new?template=add-project.yml), open a pull request, or email [opensource@limxdynamics.com](mailto:opensource@limxdynamics.com). See [CONTRIBUTING.md](CONTRIBUTING.md) for the criteria and format.

Entries are listed newest first within each section. Other sections, such as perception & navigation and industry deployments, will appear once they have their first entry.

Owners can ask to be removed at any time, for any reason: open an issue or send an email.

## License

This list is released under [CC0 1.0](LICENSE). Linked projects keep their own licenses.
