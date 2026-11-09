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

Projects, papers, videos and competition results built on [LimX Dynamics](https://www.limxdynamics.com) robots (TRON1, TRON2, Oli, Luna) and the LimX SDK.

Every entry links to its original public source, so you can see for yourself what people have built with LimX hardware. A listing shows that the work used LimX hardware or software. It is not an endorsement by LimX Dynamics, and all rights stay with the project's owners.

## Contents

- [Locomotion & whole-body control](#locomotion--whole-body-control)
- [Perception & navigation](#perception--navigation)
- [Manipulation](#manipulation)
- [Embodied AI](#embodied-ai)
- [Tools, simulation & SDK](#tools-simulation--sdk)
- [Education & competitions](#education--competitions)
- [Industry deployments](#industry-deployments)
- [Submit a case](#submit-a-case)
- [Removal](#removal)

## Locomotion & whole-body control

_Walking, running, jumping, stair climbing, terrain traversal, motion tracking and whole-body control, learned or model-based._

- **[Where-to-Learn: analytical policy gradient directed exploration](https://wheretolearn.github.io)** — Used analytical policy gradients to guide on-policy RL exploration and transferred the resulting velocity-tracking policy to a real point-foot TRON1.<br>
  <sub>Zhejiang University, SUSTech · TRON1 · 2026 · [Paper](https://arxiv.org/abs/2603.27317) · [Video](https://www.youtube.com/watch?v=DztdUyh_LVk)</sub>
- **[AME-2: agile legged locomotion via attention-based neural map encoding](https://sites.google.com/leggedrobotics.com/ame-2)** — Trained a perceptive locomotion policy with attention-based map encoding and ran it on a real TRON1 biped as well as ANYmal-D.<br>
  <sub>ETH Zurich Robotic Systems Lab · TRON1 · 2026 · [Paper](https://arxiv.org/abs/2601.08485)</sub>
- **[PvP: proprioceptive-privileged contrastive representations](https://arxiv.org/abs/2512.13093)** — Used contrastive representations to make humanoid RL more data-efficient, evaluated on velocity tracking and motion imitation with Oli.<br>
  <sub>PolyU, USTC, LimX Dynamics et al. · Oli · 2025 · [Paper](https://arxiv.org/abs/2512.13093)</sub>
- **[Gait-adaptive perceptive humanoid locomotion](https://ga-phl.github.io/)** — Reconstructed the terrain under the robot in real time to adapt gait on stairs and rough ground, in simulation and on a real Oli.<br>
  <sub>USTC, LimX Dynamics et al. · Oli · 2025 · [Paper](https://arxiv.org/abs/2512.07464)</sub>
- **[LIPM-guided RL for stable and perceptive bipedal locomotion](https://arxiv.org/abs/2509.09106)** — Combined linear inverted pendulum guidance with RL and deployed the student policy on a point-foot TRON1 outdoors.<br>
  <sub>SUSTech, HKUST, HKU, ZJU-UIUC Institute, LimX Dynamics · TRON1 · 2025 · [Paper](https://arxiv.org/abs/2509.09106)</sub>
- **[CTBC: contact-triggered blind climbing for wheeled bipedal robots](https://ctbc-for-wheeled-bipedal-robots.github.io/)** — Trained blind curb and stair climbing triggered by wheel contact and deployed it on a wheel-legged TRON1.<br>
  <sub>Shanghai University, COWAROBOT · TRON1 · 2025 · [Paper](https://arxiv.org/abs/2509.02986)</sub>
- **[BarlowWalk: self-supervised representations for terrain-adaptive locomotion](https://arxiv.org/abs/2508.00939)** — Learned terrain-aware representations with Barlow Twins for locomotion and ran experiments on TRON1 in sole-foot mode.<br>
  <sub>Harbin Institute of Technology, Shenzhen · TRON1 · 2025 · [Paper](https://arxiv.org/abs/2508.00939)</sub>

## Perception & navigation

_Mapping, localization, path planning, obstacle avoidance and autonomous navigation._

_Nothing listed yet. [Submit a case](#submit-a-case)._

## Manipulation

_Grasping, mobile manipulation, teleoperation and arm control._

- **[Holistic whole-body loco-manipulation with a bipedal mobile manipulator](https://arxiv.org/abs/2609.18930)** — Learned coordinated walking and arm motion on a TRON1 biped fitted with an ARX L5 arm.<br>
  <sub>ZJU-UIUC Institute, LimX Dynamics · TRON1 · 2026 · [Paper](https://arxiv.org/abs/2609.18930)</sub>
- **[CWI: composite humanoid whole-body imitation for loco-manipulation](https://cwi-ral.github.io/CWI-RAL-Webpage/)** — Built a whole-body imitation system for loco-manipulation and deployed it on a full-size Oli.<br>
  <sub>LimX Dynamics, HKU, SUSTech, HKUST, ZJU-UIUC Institute · Oli · 2026 · [Paper](https://arxiv.org/abs/2606.27676)</sub>

## Embodied AI

_Vision-language-action models, LLM agents, imitation learning and foundation models running on LimX robots._

- **[TRON2 garment feeder Pi0.5 policy](https://huggingface.co/voniu/tron2-garment-feeder-button-pi05)** — Fine-tuned a Pi0.5 policy on 506 TRON2 episodes to place a garment into a feeder and press a button.<br>
  <sub>voniu · TRON2 · 2026</sub>
- **[TRON2 LeRobot datasets and GR00T fine-tunes](https://huggingface.co/trantor2nd)** — Published TRON2 datasets in LeRobot format for picking, sorting, pouring and cloth folding, and fine-tuned NVIDIA GR00T policies on them.<br>
  <sub>trantor2nd · TRON2 · 2026</sub>

## Tools, simulation & SDK

_Simulators, robot models, deployment pipelines, Docker images and libraries built on the LimX SDK._

_Nothing listed yet. [Submit a case](#submit-a-case)._

## Education & competitions

_Courses, teaching labs, student team projects and competition results._

- **[LimX Tron1 Learning](https://huggingface.co/spaces/jessiezhg/LimX-Tron1-Learning)** — An interactive guide, in Chinese, to training TRON1 locomotion policies with tron1-rl-isaaclab, from RL basics to the simulation setup.<br>
  <sub>jessiezhg · TRON1 · 2026</sub>
- **[RL bipedal locomotion with Isaac Lab](https://github.com/81578823/RL_bipedal_locomotion_Isaaclab)** — SUSTech ACR2025 course project: an Isaac Lab training setup for TRON1 point-foot, sole-foot and wheel-foot variants on flat, rough and stair terrain.<br>
  <sub>SUSTech · TRON1 · 2025 · [Code](https://github.com/81578823/RL_bipedal_locomotion_Isaaclab)</sub>

## Industry deployments

_Products and real-world deployments by companies. Listed only with the company's agreement._

_Nothing listed yet. [Submit a case](#submit-a-case)._

## Submit a case

Use the [submission form](https://github.com/limxdynamics/awesome-limx/issues/new?template=add-project.yml), open a pull request, or email [opensource@limxdynamics.com](mailto:opensource@limxdynamics.com). Self-nominations are welcome; your own description is better than our guess.

Each entry looks like this (example only, not a real project):

```markdown
- **[Stair climbing with learned locomotion](https://example.org/project)** — Trained a stair-climbing policy in simulation and deployed it on TRON1 without fine-tuning.<br>
  <sub>Example University · TRON1 · 2025 · [Paper](https://arxiv.org/abs/0000.00000) · [Code](https://github.com/owner/repo) · [Video](https://www.youtube.com/watch?v=...)</sub>
```

What we list:

1. **The work used LimX hardware or software**, on a real robot or in simulation with official LimX models, and a public source says so: the paper names the robot, the video shows it, or the README states it.
2. **There is a public link to the original source**: a code repository, a paper or project page, a video, or an official competition result.
3. **Company projects are listed only with the company's agreement.** We do not announce someone else's business relationship before they do.
4. **Links only.** We do not copy code, papers, videos or images.

Within each section, entries are listed newest first. See [CONTRIBUTING.md](CONTRIBUTING.md) for the full rules.

## Removal

Owners can ask to be removed at any time, for any reason, without explanation. Open an issue or email [opensource@limxdynamics.com](mailto:opensource@limxdynamics.com) and we will take the entry down.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, contributors have waived all copyright and related rights to this list. Linked projects keep their own licenses. See [LICENSE](LICENSE).
