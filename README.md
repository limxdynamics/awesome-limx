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

Public work that uses LimX hardware or software: papers, open-source code, datasets, tutorials and competition results. LimX's own open-source releases live on [GitHub](https://github.com/limxdynamics) and [Hugging Face](https://huggingface.co/limxdynamics).

**43** projects · **21** open source 🌟 | [Locomotion & whole-body control](#locomotion--whole-body-control) 19 · [Manipulation](#manipulation) 6 · [Embodied AI](#embodied-ai) 5 · [Tools, simulation & SDK](#tools-simulation--sdk) 8 · [Education & competitions](#education--competitions) 5 · [Contributing](#contributing)

<details>
<summary><b>By robot</b>: TRON1 26 · TRON2 7 · Oli 12 · Luna 2 · P1 3 · W1 1</summary>

- **TRON1**: [TRON1 Sliding Analysis](#p-tron1-sliding-analysis) · [Learning-Enhanced PMP-MPC](#p-learning-enhanced-pmp-mpc) · [TRON1 WF Mimic](#p-tron1-wf-mimic) · [Where-to-Learn](#p-where-to-learn) · [AME-2](#p-ame-2) · [LIPM-Guided RL](#p-lipm-guided-rl) · [CTBC](#p-ctbc) · [BarlowWalk](#p-barlowwalk) · [Multi-Embodiment Retargeting](#p-multi-embodiment-retargeting) · [Bipedal MPC](#p-bipedal-mpc) · [Holistic Loco-Manipulation](#p-holistic-loco-manipulation) · [TRON1-to-UR5e Bottle Transfer](#p-tron1-to-ur5e-bottle-transfer) · [Cooperative Transportation](#p-cooperative-transportation) · [Arm-TRON](#p-arm-tron) · [robot_descriptions.py](#p-robot_descriptionspy) · [wf_tron1b_deploy](#p-wf_tron1b_deploy) · [Tron_Deploy](#p-tron_deploy) · [limx-3d-measurement-workbench](#p-limx-3d-measurement-workbench) · [limx-robotics-mcp](#p-limx-robotics-mcp) · [tron_docker_sim](#p-tron_docker_sim) · [tron1-rl-mjlab](#p-tron1-rl-mjlab) · [bipedal_locomotion_isaaclab](#p-bipedal_locomotion_isaaclab) · [OpenArm Mobile Manipulation Lab](#p-openarm-mobile-manipulation-lab) · [LimX Tron1 Learning](#p-limx-tron1-learning) · [RL Bipedal Locomotion](#p-rl-bipedal-locomotion) · [pointfootGym](#p-pointfootgym)
- **TRON2**: [Cooperative Transportation](#p-cooperative-transportation) · [ACG-WAM](#p-acg-wam) · [GR00T Drifting Heads](#p-drifting-action-heads-for-gr00t-n17) · [TRON2 Garment Feeder](#p-tron2-garment-feeder) · [TRON2 LeRobot Datasets](#p-tron2-lerobot-datasets) · [robot_descriptions.py](#p-robot_descriptionspy) · [limx-3d-measurement-workbench](#p-limx-3d-measurement-workbench)
- **Oli**: [SuperMimic for Oli](#p-supermimic-for-oli) · [VAPS](#p-vaps) · [Any2Any](#p-any2any) · [FastStair](#p-faststair) · [PvP](#p-pvp) · [GA-PHL](#p-ga-phl) · [Multi-Embodiment Retargeting](#p-multi-embodiment-retargeting) · [CWI](#p-cwi) · [HWAM](#p-hwam) · [robot_descriptions.py](#p-robot_descriptionspy) · [limx-robotics-mcp](#p-limx-robotics-mcp) · [Canton Tower Robot Climbing Challenge](#p-canton-tower-robot-climbing-challenge)
- **Luna**: [Any2Any](#p-any2any) · [robot_descriptions.py](#p-robot_descriptionspy)
- **P1**: [VMTS](#p-vmts) · [CTS](#p-cts) · [Task-Space Riccati WBC](#p-task-space-riccati-wbc)
- **W1**: [Wheeled-Quadrupedal Manipulator](#p-wheeled-quadrupedal-manipulator)

</details>

## Locomotion & whole-body control

| Project | Robot | Team | Year | Links |
|---|---|---|---|---|
| <a id="p-tron1-sliding-analysis"></a>🌟 **TRON1 Sliding Analysis**: wheel-foot drift and friction transfer (sim) | `TRON1` | Shukashuki | 2026 | [[code](https://github.com/Shukashuki/tron1-sliding-analysis)] |
| <a id="p-learning-enhanced-pmp-mpc"></a>🌟 **Learning-Enhanced PMP-MPC**: learned-residual MPC for a point-foot biped | `TRON1` | Markwcl2004 | 2026 | [[paper](https://doi.org/10.1109/ASCC70886.2026.11701800)] [[code](https://github.com/Markwcl2004/PMP_based_Bipedal_MPC)] |
| <a id="p-supermimic-for-oli"></a>🌟 **SuperMimic for Oli**: one policy tracking 40 motions (sim) | `Oli` | Tianxing Liu | 2026 | [[code](https://github.com/liuskywalkerjskd/supermimic_oli)] |
| <a id="p-vaps"></a>**VAPS**: safe acrobatics, real side flips | `Oli` | TU Darmstadt, LimX et al. | 2026 | [[project](https://vaps-r-al.github.io/)] [[paper](https://arxiv.org/abs/2610.01397)] |
| <a id="p-tron1-wf-mimic"></a>🌟 **TRON1 WF Mimic**: dance imitation and feasibility study (sim) | `TRON1` | HUST-dolores | 2026 | [[code](https://github.com/HUST-dolores/tron1-wf-mimic)] |
| <a id="p-any2any"></a>**Any2Any**: cross-embodiment whole-body tracking | `Oli` `Luna` | LimX | 2026 | [[paper](https://arxiv.org/abs/2605.23733)] |
| <a id="p-where-to-learn"></a>**Where-to-Learn**: gradient-guided RL exploration | `TRON1` | ZJU, SUSTech | 2026 | [[project](https://wheretolearn.github.io)] [[paper](https://arxiv.org/abs/2603.27317)] [[video](https://www.youtube.com/watch?v=DztdUyh_LVk)] |
| <a id="p-faststair"></a>**FastStair**: running up stairs | `Oli` | HIT, LimX et al. | 2026 | [[project](https://npcliu.github.io/FastStair)] [[paper](https://arxiv.org/abs/2601.10365)] [[video](https://youtu.be/SoLBK7VEGDo)] |
| <a id="p-ame-2"></a>**AME-2**: agile perceptive locomotion | `TRON1` | ETH Zurich | 2026 | [[project](https://sites.google.com/leggedrobotics.com/ame-2)] [[paper](https://arxiv.org/abs/2601.08485)] |
| <a id="p-pvp"></a>**PvP**: data-efficient humanoid RL | `Oli` | PolyU, USTC et al. | 2025 | [[paper](https://arxiv.org/abs/2512.13093)] |
| <a id="p-ga-phl"></a>**GA-PHL**: gait-adaptive perceptive walking | `Oli` | USTC, LimX et al. | 2025 | [[project](https://ga-phl.github.io/)] [[paper](https://arxiv.org/abs/2512.07464)] |
| <a id="p-lipm-guided-rl"></a>**LIPM-Guided RL**: stable perceptive biped walking | `TRON1` | SUSTech, HKUST et al. | 2025 | [[paper](https://arxiv.org/abs/2509.09106)] |
| <a id="p-ctbc"></a>**CTBC**: blind stair climbing on wheels | `TRON1` | Shanghai University, COWAROBOT | 2025 | [[project](https://ctbc-for-wheeled-bipedal-robots.github.io/)] [[paper](https://arxiv.org/abs/2509.02986)] |
| <a id="p-barlowwalk"></a>**BarlowWalk**: terrain-adaptive locomotion | `TRON1` | HIT Shenzhen | 2025 | [[paper](https://arxiv.org/abs/2508.00939)] |
| <a id="p-multi-embodiment-retargeting"></a>**Multi-Embodiment Retargeting**: diffusion-based motion retargeting | `Oli` `TRON1` | SUSTech, HKUST et al. | 2025 | [[paper](https://arxiv.org/abs/2505.20857)] |
| <a id="p-vmts"></a>**VMTS**: vision-assisted multi-terrain walking | `P1` | Southeast University | 2025 | [[paper](https://arxiv.org/abs/2503.07049)] |
| <a id="p-bipedal-mpc"></a>🌟 **Bipedal MPC**: convex MPC and WBC in MuJoCo | `TRON1` | SUSTech CLEAR Lab | 2024 | [[code](https://github.com/clearlab-sustech/Bipedal_MPC)] |
| <a id="p-cts"></a>**CTS**: concurrent teacher-student RL | `P1` | SUSTech, ZJU-UIUC et al. | 2024 | [[project](https://clearlab-sustech.github.io/concurrentTS/)] [[paper](https://arxiv.org/abs/2405.10830)] |
| <a id="p-task-space-riccati-wbc"></a>**Task-Space Riccati WBC**: whole-body control (sim) | `P1` | SUSTech, HKUST et al. | 2024 | [[paper](https://arxiv.org/abs/2404.00591)] |

## Manipulation

| Project | Robot | Team | Year | Links |
|---|---|---|---|---|
| <a id="p-holistic-loco-manipulation"></a>**Holistic Loco-Manipulation**: TRON1 with an arm | `TRON1` | ZJU-UIUC, LimX | 2026 | [[paper](https://arxiv.org/abs/2609.18930)] |
| <a id="p-tron1-to-ur5e-bottle-transfer"></a>🌟 **TRON1-to-UR5e Bottle Transfer**: ROS 2 and MuJoCo (sim) | `TRON1` | Centaucyan | 2026 | [[code](https://github.com/Centaucyan/Proj_Transferring_bottle_from_tron1_to_ur5e_in_mujoco_env)] |
| <a id="p-cooperative-transportation"></a>🌟 **Cooperative Transportation**: two wheel-legged robots carry a load (sim) | `TRON1` `TRON2` | Matt14-mander | 2026 | [[code](https://github.com/Matt14-mander/Multiple_Humanoid_Cooperative_Transportation)] |
| <a id="p-cwi"></a>**CWI**: whole-body imitation for loco-manipulation | `Oli` | LimX, HKU et al. | 2026 | [[project](https://cwi-ral.github.io/CWI-RAL-Webpage/)] [[paper](https://arxiv.org/abs/2606.27676)] |
| <a id="p-arm-tron"></a>**Arm-TRON**: reconfigurable biped with an arm | `TRON1` | SUSTech, ZJU et al. | 2026 | [[paper](https://doi.org/10.1109/TMECH.2026.3727546)] |
| <a id="p-wheeled-quadrupedal-manipulator"></a>**Wheeled-Quadrupedal Manipulator**: W1 with an arm, pose tracking | `W1` | SUSTech, ZJU-UIUC et al. | 2024 | [[paper](https://arxiv.org/abs/2412.03012)] |

## Embodied AI

| Project | Robot | Team | Year | Links |
|---|---|---|---|---|
| <a id="p-hwam"></a>**HWAM**: humanoid world action model | `Oli` | LimX | 2026 | [[project](https://hwam.vercel.app/)] [[paper](https://arxiv.org/abs/2610.12026)] |
| <a id="p-acg-wam"></a>🌟 **ACG-WAM**: world-action model with dexterous hands | `TRON2` | BIT, LimX | 2026 | [[project](https://RoboOpus.github.io/ACG-WAM)] [[paper](https://arxiv.org/abs/2610.06965)] [[code](https://github.com/RoboOpus/ACG-WAM)] |
| <a id="p-drifting-action-heads-for-gr00t-n17"></a>**GR00T Drifting Heads**: one-step action heads | `TRON2` | ZJU-UIUC, LimX | 2026 | [[paper](https://arxiv.org/abs/2609.18108)] |
| <a id="p-tron2-garment-feeder"></a>🌟 **TRON2 Garment Feeder**: Pi0.5 policy | `TRON2` | voniu | 2026 | [[model](https://huggingface.co/voniu/tron2-garment-feeder-button-pi05)] |
| <a id="p-tron2-lerobot-datasets"></a>🌟 **TRON2 LeRobot Datasets**: datasets and GR00T fine-tunes | `TRON2` | trantor2nd | 2026 | [[dataset](https://huggingface.co/trantor2nd)] |

## Tools, simulation & SDK

| Project | Robot | Team | Year | Links |
|---|---|---|---|---|
| <a id="p-robot_descriptionspy"></a>🌟 **robot_descriptions.py**: load TRON1, TRON2, Oli, Luna models in one line | `TRON1` `TRON2` `Oli` `Luna` | robot-descriptions | 2026 | [[code](https://github.com/robot-descriptions/robot_descriptions.py)] |
| <a id="p-wf_tron1b_deploy"></a>🌟 **wf_tron1b_deploy**: depth-perceptive policy sim-to-sim | `TRON1` | Leixin Chang | 2026 | [[code](https://github.com/Leixinjonaschang/wf_tron1b_deploy)] |
| <a id="p-tron_deploy"></a>🌟 **Tron_Deploy**: deploy policies from Windows | `TRON1` | candi4 | 2026 | [[code](https://github.com/candi4/Tron_Deploy)] |
| <a id="p-limx-3d-measurement-workbench"></a>🌟 **limx-3d-measurement-workbench**: browse TRON models, measure dimensions | `TRON1` `TRON2` | voniu | 2026 | [[code](https://github.com/voniu/limx-3d-measurement-workbench)] |
| <a id="p-limx-robotics-mcp"></a>🌟 **limx-robotics-mcp**: MCP server for sim and control | `TRON1` `Oli` | sandraschi | 2026 | [[code](https://github.com/sandraschi/limx-robotics-mcp)] |
| <a id="p-tron_docker_sim"></a>🌟 **tron_docker_sim**: Docker image for Gazebo sim | `TRON1` | The-RoboTUM | 2026 | [[code](https://github.com/The-RoboTUM/tron_docker_sim)] |
| <a id="p-tron1-rl-mjlab"></a>🌟 **tron1-rl-mjlab**: wheel-foot training on mjlab | `TRON1` | Xinchen Yao | 2025 | [[code](https://github.com/hoscy/tron1-rl-mjlab)] |
| <a id="p-bipedal_locomotion_isaaclab"></a>🌟 **bipedal_locomotion_isaaclab**: Isaac Lab training, sim-to-real | `TRON1` | SUSTech | 2024 | [[code](https://github.com/Andy-xiong6/bipedal_locomotion_isaaclab)] |

## Education & competitions

| Project | Robot | Team | Year | Links |
|---|---|---|---|---|
| <a id="p-openarm-mobile-manipulation-lab"></a>🌟 **OpenArm Mobile Manipulation Lab**: TRON1 + OpenArm, LLM missions (sim, Korean) | `TRON1` | aha645 | 2026 | [[code](https://github.com/aha645/openarms_llm_ex)] |
| <a id="p-limx-tron1-learning"></a>**LimX Tron1 Learning**: interactive Isaac Lab guide | `TRON1` | jessiezhg | 2026 | [[tutorial](https://huggingface.co/spaces/jessiezhg/LimX-Tron1-Learning)] |
| <a id="p-canton-tower-robot-climbing-challenge"></a>**Canton Tower Robot Climbing Challenge**: champion, best precision control | `Oli` | LimX | 2025 | [[result](https://www.sfccn.com/2026/1-1/5NMDE0NzNfMjA5MzM5NA.html)] [[paper](https://arxiv.org/abs/2601.10365)] |
| <a id="p-rl-bipedal-locomotion"></a>🌟 **RL Bipedal Locomotion**: SUSTech ACR2025 course project | `TRON1` | SUSTech | 2025 | [[code](https://github.com/81578823/RL_bipedal_locomotion_Isaaclab)] |
| <a id="p-pointfootgym"></a>🌟 **pointfootGym**: Isaac Gym course template | `TRON1` | SUSTech CLEAR Lab | 2024 | [[code](https://github.com/SuDaxia-kai/pointfootGym)] |

## Contributing

Self-nominations and suggestions are welcome: use the [submission form](https://github.com/limxdynamics/awesome-limx/issues/new?template=add-project.yml), open a pull request, or email [opensource@limxdynamics.com](mailto:opensource@limxdynamics.com). See [CONTRIBUTING.md](CONTRIBUTING.md) for the criteria. Entries are newest first within each section; 🌟 marks entries with code, a model or a dataset.

A listing is not an endorsement, and all rights stay with the owners. Owners can ask to be removed at any time, for any reason.

## License

This list is released under [CC0 1.0](LICENSE). Linked projects keep their own licenses.
