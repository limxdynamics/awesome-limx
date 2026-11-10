<p align="center"><img src="assets/banner_ko.png" alt="Awesome LimX" width="100%"></p>

<p align="center">
  <a href="README.md">English</a> | <a href="README_cn.md">中文</a> | <a href="README_ja.md">日本語</a> | <b>한국어</b>
</p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-CC0--1.0-2f6feb" alt="License: CC0-1.0"></a>
  <a href="https://github.com/limxdynamics/limxdynamics/blob/main/doc/wechat_qr.png"><img src="https://img.shields.io/badge/WeChat-Developer%20Community-07C160?logo=wechat&logoColor=white" alt="WeChat Community"></a>
</p>

> LimX 로봇과 LimX SDK로 만든 **95**개 프로젝트를 모았고, 그중 **61**개는 오픈소스 코드를 제공합니다. 논문, 코드, 데이터셋, 튜토리얼, 대회 결과, 산업 적용 사례를 다룹니다. LimX 공식 오픈소스는 [GitHub](https://github.com/limxdynamics)와 [Hugging Face](https://huggingface.co/limxdynamics)에서 확인하세요.

## 목차

- [시작하기 전에](#시작하기-전에)
- [보행 및 전신 제어](#보행-및-전신-제어) — 32
  - [지형 및 인지 기반 보행](#지형-및-인지-기반-보행)
  - [강화학습 훈련 및 실기 전이](#강화학습-훈련-및-실기-전이)
  - [모델 기반 제어](#모델-기반-제어)
  - [모션 트래킹 및 리타게팅](#모션-트래킹-및-리타게팅)
- [인지 및 내비게이션](#인지-및-내비게이션) — 5
- [매니퓰레이션](#매니퓰레이션) — 9
- [임바디드 AI](#임바디드-ai) — 7
- [도구, 시뮬레이션 및 SDK](#도구-시뮬레이션-및-sdk) — 19
  - [학습 프레임워크](#학습-프레임워크)
  - [시뮬레이션 및 환경](#시뮬레이션-및-환경)
  - [배포 및 제어](#배포-및-제어)
  - [모델 및 모션 데이터](#모델-및-모션-데이터)
- [교육 및 대회](#교육-및-대회) — 9
- [산업 적용](#산업-적용) — 14
  - [적용 사례 및 제품](#적용-사례-및-제품)
  - [상업 공연 및 이벤트](#상업-공연-및-이벤트)
  - [전략적 제휴](#전략적-제휴)
  - [지역 파트너 및 판매 채널](#지역-파트너-및-판매-채널)
  - [수상 및 인정](#수상-및-인정)
- [기종별](#기종별): [TRON1](robots/TRON1_ko.md) · [TRON2](robots/TRON2_ko.md) · [Oli](robots/Oli_ko.md) · [Luna](robots/Luna_ko.md) · [P1](robots/P1_ko.md) · [W1](robots/W1_ko.md)
- [기여하기](#기여하기)

<sub>**코드** 바로 실행 가능 · **튜토리얼** 따라 배울 수 있음 · **논문** 읽을거리 · *sim* 시뮬레이션에서만 보여준 성과, 나머지는 실제 로봇에서 동작</sub>

## 시작하기 전에

아래의 모든 성과는 같은 네 단계를 바탕으로 합니다. 처음이라면 순서대로 따라가세요. 여기 있는 것은 LimX 공식 저장소이며 커뮤니티 프로젝트가 아닙니다.

| 단계 | 필요한 것 | 받는 곳 |
|---|---|---|
| 1 · 모델 | 로봇의 URDF, MJCF, USD | [TRON1](https://github.com/limxdynamics/tron1-robot-description) · [TRON2](https://github.com/limxdynamics/tron2-robot-description) · [Oli](https://github.com/limxdynamics/humanoid-description) · [Luna](https://github.com/limxdynamics/luna-description) |
| 2 · 인터페이스 | 저수준 모션 SDK, ROS 2 | [limxsdk-lowlevel](https://github.com/limxdynamics/limxsdk-lowlevel) |
| 3 · 학습 | Isaac Lab, Isaac Gym, MuJoCo | [tron1-rl-isaaclab](https://github.com/limxdynamics/tron1-rl-isaaclab) · [tron2_rl_lab](https://github.com/limxdynamics/tron2_rl_lab) · [tron1-mujoco-sim](https://github.com/limxdynamics/tron1-mujoco-sim) |
| 4 · 배포 | ONNX 런타임, ROS 2, C++ | [tron1-rl-deploy-python](https://github.com/limxdynamics/tron1-rl-deploy-python) · [humanoid-rl-deploy-python](https://github.com/limxdynamics/humanoid-rl-deploy-python) |

## 보행 및 전신 제어

_32개 (4개 그룹): 논문 12 · 코드 20_

### 지형 및 인지 기반 보행

| 프로젝트 | 기종 | 저자 / 기관 | 연도 | 유형 | 링크 |
|---|---|---|---|---|---|
| <a id="p-ame-2"></a>**AME-2**: 민첩한 인지 기반 보행 | `TRON1` | [ETH Zurich RSL](https://rsl.ethz.ch) | 2026 | 논문 | [프로젝트](https://sites.google.com/leggedrobotics.com/ame-2)&nbsp;·&nbsp;[논문](https://arxiv.org/abs/2601.08485) |
| <a id="p-faststair"></a>**FastStair**: 계단 달려 오르기 | `Oli` | HIT, LimX et al. | 2026 | 논문 | [프로젝트](https://npcliu.github.io/FastStair)&nbsp;·&nbsp;[논문](https://arxiv.org/abs/2601.10365)&nbsp;·&nbsp;[영상](https://youtu.be/SoLBK7VEGDo) |
| <a id="p-steppingstonelocomotion"></a>**SteppingStoneLocomotion**: 징검다리 보행, 블라인드 후 비전 적용 | `TRON1`&nbsp;*sim* | [Yiyou6](https://github.com/Yiyou6) | 2026 | 코드 | [코드](https://github.com/Yiyou6/SteppingStoneLocomotion)&nbsp;·&nbsp;[영상](https://www.youtube.com/watch?v=vs608-L7kl0) |
| <a id="p-barlowwalk"></a>**BarlowWalk**: 지형 적응 보행 | `TRON1`&nbsp;*sim* | HIT Shenzhen | 2025 | 논문 | [논문](https://arxiv.org/abs/2508.00939) |
| <a id="p-ctbc"></a>**CTBC**: 바퀴로 하는 블라인드 계단 오르기 | `TRON1` | Shanghai University, COWAROBOT | 2025 | 논문 | [프로젝트](https://ctbc-for-wheeled-bipedal-robots.github.io/)&nbsp;·&nbsp;[논문](https://arxiv.org/abs/2509.02986) |
| <a id="p-ga-phl"></a>**GA-PHL**: 보행 패턴 적응형 인지 보행 | `Oli` | USTC, LimX et al. | 2025 | 논문 | [프로젝트](https://ga-phl.github.io/)&nbsp;·&nbsp;[논문](https://arxiv.org/abs/2512.07464) |
| <a id="p-lipm-guided-rl"></a>**LIPM-Guided RL**: 안정적인 인지 기반 이족 보행 | `TRON1` | SUSTech CLEAR Lab, HKUST et al. | 2025 | 논문 | [논문](https://arxiv.org/abs/2509.09106) |
| <a id="p-vmts"></a>**VMTS**: 비전 보조 다지형 보행 | `P1` | Southeast University | 2025 | 코드 | [논문](https://arxiv.org/abs/2503.07049)&nbsp;·&nbsp;[코드](https://github.com/chenfu-user/VMTS) |

### 강화학습 훈련 및 실기 전이

| 프로젝트 | 기종 | 저자 / 기관 | 연도 | 유형 | 링크 |
|---|---|---|---|---|---|
| <a id="p-biped-rl-with-pathfinding"></a>**Biped RL with Pathfinding**: 경로 탐색을 결합한 목표 조건부 학습 | `TRON1`&nbsp;*sim* | [shandilya1998](https://github.com/shandilya1998) | 2026 | 코드 | [코드](https://github.com/singhaman1750/biped-rl-isaaclab-iisc) |
| <a id="p-osram"></a>**OSRAM**: 온라인 sim-to-real 적응 | `TRON1` | [Duke University](https://github.com/generalroboticslab) | 2026 | 코드 | [코드](https://github.com/generalroboticslab/OSRAM) |
| <a id="p-rl-tron1"></a>**rl-tron1**: 교사-학생 방식 Isaac Lab 학습 | `TRON1`&nbsp;*sim* | [Jiakang Ma](https://github.com/Jiakang-Ma) | 2026 | 코드 | [코드](https://github.com/Jiakang-Ma/rl-tron1) |
| <a id="p-tron1-sliding-analysis"></a>**TRON1 Sliding Analysis**: 휠-풋 미끄러짐과 마찰 전이 | `TRON1`&nbsp;*sim* | [Shukashuki](https://github.com/Shukashuki) | 2026 | 코드 | [코드](https://github.com/Shukashuki/tron1-sliding-analysis) |
| <a id="p-vaps"></a>**VAPS**: 안전한 곡예 동작, 실기 옆돌기 | `Oli` | TU Darmstadt, LimX et al. | 2026 | 논문 | [프로젝트](https://vaps-r-al.github.io/)&nbsp;·&nbsp;[논문](https://arxiv.org/abs/2610.01397) |
| <a id="p-wf_tron1a-stand-still-policy"></a>**WF_TRON1A Stand-Still Policy**: 제자리 정지 서기 RL 정책 | `TRON1`&nbsp;*sim* | [F-Morry](https://github.com/F-Morry) | 2026 | 코드 | [코드](https://github.com/F-Morry/limx_rl) |
| <a id="p-where-to-learn"></a>**Where-to-Learn**: 그래디언트 유도 RL 탐색 | `TRON1` | ZJU, SUSTech | 2026 | 논문 | [프로젝트](https://wheretolearn.github.io)&nbsp;·&nbsp;[논문](https://arxiv.org/abs/2603.27317)&nbsp;·&nbsp;[영상](https://www.youtube.com/watch?v=DztdUyh_LVk) |
| <a id="p-zetin-tron1-deploy"></a>**Zetin TRON1 Deploy**: sim-to-sim 및 실기 배포 | `TRON1` | [Chanjun Lee (UOS Zetin)](https://github.com/chanjun-nyam) | 2026 | 코드 | [코드](https://github.com/chanjun-nyam/Zetin-Humanoid-RL-Deploy) |
| <a id="p-him-pim-isaac-lab"></a>**HIM-PIM Isaac Lab**: HIM과 PIM을 이용한 강건한 보행 | `TRON1`&nbsp;*sim* | [DongyangLin](https://github.com/DongyangLin) | 2025 | 코드 | [코드](https://github.com/DongyangLin/HIM-PIM-isaaclab) |
| <a id="p-leggedrobotslab"></a>**LeggedRobotsLab**: Go1과 TRON1A용 Isaac Lab 보행 | `TRON1`&nbsp;*sim* | [Guohua Zhang](https://github.com/guohua-zhang) | 2025 | 코드 | [코드](https://github.com/guohua-zhang/LeggedRobotsLab) |
| <a id="p-multi-loco"></a>**Multi-Loco**: 포인트풋과 휠풋을 하나의 확산 정책으로 | `TRON1` | SUSTech CLEAR Lab, LimX et al. | 2025 | 코드 | [프로젝트](https://multi-loco.github.io)&nbsp;·&nbsp;[논문](https://arxiv.org/abs/2506.11470)&nbsp;·&nbsp;[코드](https://github.com/clearlab-sustech/multi_loco_isaacgym) |
| <a id="p-pvp"></a>**PvP**: 데이터 효율적인 휴머노이드 RL | `Oli` | PolyU, USTC et al. | 2025 | 논문 | [논문](https://arxiv.org/abs/2512.13093) |
| <a id="p-tron-camp-wheel-foot-deployment"></a>**TRON Camp Wheel-Foot Deployment**: 휠풋 정책 실기 배포 | `TRON1` | [Yitao Zeng](https://github.com/24zen0) | 2025 | 코드 | [코드](https://github.com/24zen0/Deployment_of_wheelfoot_tron) |
| <a id="p-anybipe"></a>**AnyBipe**: LLM 기반 이족 로봇 학습 및 배포 | `TRON1` | [SJTU](https://github.com/sjtu-mvasl-robotics) | 2024 | 코드 | [코드](https://github.com/sjtu-mvasl-robotics/AnyBipe) |
| <a id="p-cts"></a>**CTS**: 동시 교사-학생 RL | `P1` | SUSTech CLEAR Lab, ZJU-UIUC et al. | 2024 | 논문 | [프로젝트](https://clearlab-sustech.github.io/concurrentTS/)&nbsp;·&nbsp;[논문](https://arxiv.org/abs/2405.10830) |

### 모델 기반 제어

| 프로젝트 | 기종 | 저자 / 기관 | 연도 | 유형 | 링크 |
|---|---|---|---|---|---|
| <a id="p-learning-enhanced-pmp-mpc"></a>**Learning-Enhanced PMP-MPC**: 포인트풋 이족 로봇용 학습 잔차 MPC | `TRON1`&nbsp;*sim* | [Markwcl2004](https://github.com/Markwcl2004) | 2026 | 코드 | [논문](https://doi.org/10.1109/ASCC70886.2026.11701800)&nbsp;·&nbsp;[코드](https://github.com/Markwcl2004/PMP_based_Bipedal_MPC) |
| <a id="p-whole-body-humanoid-mpc"></a>**Whole-Body Humanoid MPC**: 31자유도 Oli 비선형 전신 MPC | `Oli`&nbsp;*sim* | [Tianxing Liu](https://github.com/liuskywalkerjskd) | 2026 | 코드 | [코드](https://github.com/liuskywalkerjskd/humanoid_mpc) |
| <a id="p-bipedal-mpc"></a>**Bipedal MPC**: MuJoCo 기반 볼록 MPC와 WBC | `TRON1`&nbsp;*sim* | [SUSTech CLEAR Lab](https://github.com/clearlab-sustech) | 2024 | 코드 | [코드](https://github.com/clearlab-sustech/Bipedal_MPC) |
| <a id="p-task-space-riccati-wbc"></a>**Task-Space Riccati WBC**: 전신 제어 | `P1`&nbsp;*sim* | SUSTech, HKUST et al. | 2024 | 논문 | [논문](https://arxiv.org/abs/2404.00591) |

### 모션 트래킹 및 리타게팅

| 프로젝트 | 기종 | 저자 / 기관 | 연도 | 유형 | 링크 |
|---|---|---|---|---|---|
| <a id="p-any2any"></a>**Any2Any**: 기체 간 전신 모션 트래킹 | `Oli` `Luna` | LimX | 2026 | 코드 | [논문](https://arxiv.org/abs/2605.23733)&nbsp;·&nbsp;[코드](https://github.com/Ming827/any2any_sonic2Oli) |
| <a id="p-chip-for-oli"></a>**CHIP for Oli**: mjlab 기반 적응형 컴플라이언스 모션 트래킹 | `Oli`&nbsp;*sim* | [Matt14-mander](https://github.com/Matt14-mander) | 2026 | 코드 | [코드](https://github.com/Matt14-mander/chip-oli) |
| <a id="p-supermimic-for-oli"></a>**SuperMimic for Oli**: 하나의 정책으로 40개 동작 추종 | `Oli`&nbsp;*sim* | [Tianxing Liu](https://github.com/liuskywalkerjskd) | 2026 | 코드 | [코드](https://github.com/liuskywalkerjskd/supermimic_oli) |
| <a id="p-tron1-wf-mimic"></a>**TRON1 WF Mimic**: 댄스 모방과 실현 가능성 연구 | `TRON1`&nbsp;*sim* | [HUST-dolores](https://github.com/HUST-dolores) | 2026 | 코드 | [코드](https://github.com/HUST-dolores/tron1-wf-mimic) |
| <a id="p-multi-embodiment-retargeting"></a>**Multi-Embodiment Retargeting**: 확산 모델 기반 모션 리타게팅 | `TRON1` `Oli`&nbsp;*sim* | SUSTech, HKUST et al. | 2025 | 논문 | [논문](https://arxiv.org/abs/2505.20857) |

## 인지 및 내비게이션

_5개, 모두 코드 제공_

| 프로젝트 | 기종 | 저자 / 기관 | 연도 | 유형 | 링크 |
|---|---|---|---|---|---|
| <a id="p-gps-tron1"></a>**GPS-TRON1**: FAST-LIO 기반 실외 GPS 내비게이션 | `TRON1` | [potatoHu-a](https://github.com/potatoHu-a) | 2026 | 코드 | [코드](https://github.com/potatoHu-a/GPS-TRON1) |
| <a id="p-wf_tron1a-lidar-navigation"></a>**WF_TRON1A LiDAR Navigation**: LiDAR 오도메트리와 내비게이션 | `TRON1` | [F-Morry](https://github.com/F-Morry) | 2026 | 코드 | [코드](https://github.com/F-Morry/limx_ws) |
| <a id="p-tron-1-struzzo"></a>**TRON-1 Struzzo**: Jetson 기반 자율 내비게이션 | `TRON1` | [enfff](https://github.com/enfff) | 2025 | 코드 | [코드](https://github.com/enfff/tron1-gazebo-ros2) |
| <a id="p-neupan-on-tron1"></a>**NeuPAN on TRON1**: 바퀴 형태의 엔드투엔드 NeuPAN 내비게이션 | `TRON1` | [WikHClean](https://github.com/WikHClean) | 2025 | 코드 | [코드](https://github.com/WikHClean/-ROS1-NeuPAN-TRON1-) |
| <a id="p-3d-navigation-with-pct-planner"></a>**3D Navigation with PCT Planner**: 계단에서의 3D 내비게이션 | `TRON1` | [81578823](https://github.com/81578823) | 2025 | 코드 | [코드](https://github.com/81578823/3D_navigation_PCTplanner) |

## 매니퓰레이션

_9개: 논문 4 · 코드 5_

| 프로젝트 | 기종 | 저자 / 기관 | 연도 | 유형 | 링크 |
|---|---|---|---|---|---|
| <a id="p-cola-on-tron2"></a>**COLA on TRON2**: 사람-로봇 협동 운반, TRON2 이식 | `TRON2`&nbsp;*sim* | [Matt14-mander](https://github.com/Matt14-mander) | 2026 | 코드 | [코드](https://github.com/Matt14-mander/COLA_TRON2) |
| <a id="p-holistic-loco-manipulation"></a>**Holistic Loco-Manipulation**: 로봇팔을 단 TRON1 | `TRON1` | ZJU-UIUC, LimX | 2026 | 논문 | [논문](https://arxiv.org/abs/2609.18930) |
| <a id="p-tron1-to-ur5e-bottle-transfer"></a>**TRON1-to-UR5e Bottle Transfer**: ROS 2와 MuJoCo | `TRON1`&nbsp;*sim* | [Centaucyan](https://github.com/Centaucyan) | 2026 | 코드 | [코드](https://github.com/Centaucyan/Proj_Transferring_bottle_from_tron1_to_ur5e_in_mujoco_env) |
| <a id="p-cooperative-transportation"></a>**Cooperative Transportation**: 휠-레그 로봇 두 대가 짐을 운반 | `TRON1` `TRON2`&nbsp;*sim* | [Matt14-mander](https://github.com/Matt14-mander) | 2026 | 코드 | [코드](https://github.com/Matt14-mander/Multiple_Humanoid_Cooperative_Transportation) |
| <a id="p-cwi"></a>**CWI**: 로코-매니퓰레이션을 위한 전신 모방 | `Oli` | LimX, HKU et al. | 2026 | 논문 | [프로젝트](https://cwi-ral.github.io/CWI-RAL-Webpage/)&nbsp;·&nbsp;[논문](https://arxiv.org/abs/2606.27676) |
| <a id="p-arm-tron"></a>**Arm-TRON**: 로봇팔을 단 재구성형 이족 로봇 | `TRON1` | SUSTech, ZJU et al. | 2026 | 논문 | [논문](https://doi.org/10.1109/TMECH.2026.3727546) |
| <a id="p-umi-on-tron1"></a>**UMI on Tron1**: 실기 TRON1에서 ARX5 팔로 UMI 스킬 수행 | `TRON1` | [Czy213hd](https://github.com/Czy213hd) | 2025 | 코드 | [코드](https://github.com/Czy213hd/umi-on-tron-lab) |
| <a id="p-quest-vr-teleop-for-oli"></a>**Quest VR Teleop for Oli**: Meta Quest로 팔과 머리 원격 조종 | `Oli` | [MSTLE](https://github.com/MSTLE) | 2025 | 코드 | [코드](https://github.com/MSTLE/Limx_teleoperate-end_pose) |
| <a id="p-wheeled-quadrupedal-manipulator"></a>**Wheeled-Quadrupedal Manipulator**: 로봇팔을 단 W1, 자세 추종 | `W1` | SUSTech CLEAR Lab, ZJU-UIUC et al. | 2024 | 논문 | [프로젝트](https://clearlab-sustech.github.io/RFM_loco_mani/)&nbsp;·&nbsp;[논문](https://arxiv.org/abs/2412.03012) |

## 임바디드 AI

_7개: 논문 2 · 코드 5_

| 프로젝트 | 기종 | 저자 / 기관 | 연도 | 유형 | 링크 |
|---|---|---|---|---|---|
| <a id="p-fluxvla-on-tron2"></a>**FluxVLA on TRON2**: 내 TRON2에서 FluxVLA 학습 및 배포 | `TRON2` | [emoPointer](https://github.com/emoPointer) | 2026 | 코드 | [코드](https://github.com/emoPointer/FluxVLA) |
| <a id="p-oli-voice-interaction"></a>**Oli Voice Interaction**: 음성 대화와 동작 제어 | `Oli` | [zhilin2025](https://github.com/zhilin2025) | 2026 | 코드 | [코드](https://github.com/zhilin2025/oli_audio) |
| <a id="p-hwam"></a>**HWAM**: 휴머노이드 월드 액션 모델 | `Oli` | LimX | 2026 | 논문 | [프로젝트](https://hwam.vercel.app/)&nbsp;·&nbsp;[논문](https://arxiv.org/abs/2610.12026) |
| <a id="p-acg-wam"></a>**ACG-WAM**: 다관절 손을 쓰는 월드 액션 모델 | `TRON2` | BIT, LimX | 2026 | 코드 | [프로젝트](https://RoboOpus.github.io/ACG-WAM)&nbsp;·&nbsp;[논문](https://arxiv.org/abs/2610.06965)&nbsp;·&nbsp;[코드](https://github.com/RoboOpus/ACG-WAM) |
| <a id="p-drifting-action-heads-for-gr00t-n17"></a>**GR00T Drifting Heads**: 원스텝 액션 헤드 | `TRON2` | ZJU-UIUC, LimX | 2026 | 논문 | [논문](https://arxiv.org/abs/2609.18108) |
| <a id="p-tron2-garment-feeder"></a>**TRON2 Garment Feeder**: Pi0.5 정책 | `TRON2` | [voniu](https://huggingface.co/voniu) | 2026 | 코드 | [모델](https://huggingface.co/voniu/tron2-garment-feeder-button-pi05) |
| <a id="p-tron2-lerobot-datasets"></a>**TRON2 LeRobot Datasets**: 데이터셋과 GR00T 파인튜닝 모델 | `TRON2` | [trantor2nd](https://huggingface.co/trantor2nd) | 2026 | 코드 | [모델](https://huggingface.co/models?author=trantor2nd&search=tron2)&nbsp;·&nbsp;[데이터셋](https://huggingface.co/datasets?author=trantor2nd&search=tron2) |

## 도구, 시뮬레이션 및 SDK

_도구 19개 (4개 그룹)_

### 학습 프레임워크

| 프로젝트 | 기종 | 저자 / 기관 | 연도 | 링크 |
|---|---|---|---|---|
| <a id="p-tron1-isaac-lab-tasks"></a>**TRON1 Isaac Lab Tasks**: 세 가지 발 형태 전부를 위한 Isaac Lab 태스크, 점프 포함 | `TRON1` | [HughWang-wzy](https://github.com/HughWang-wzy) | 2026 | [코드](https://github.com/HughWang-wzy/tron1-rl-isaaclab) |
| <a id="p-tron1-rl-mjlab"></a>**tron1-rl-mjlab**: mjlab 기반 휠풋 학습 | `TRON1` | [Xinchen Yao](https://github.com/hoscy) | 2025 | [코드](https://github.com/hoscy/tron1-rl-mjlab) |
| <a id="p-leggedgym-ex"></a>**LeggedGym-Ex**: Genesis, Isaac Gym, Isaac Sim에서 돌아가는 legged_gym | `TRON1` | [Yasen Jia](https://github.com/lupinjia) | 2024 | [코드](https://github.com/lupinjia/LeggedGym-Ex) |
| <a id="p-bipedal_locomotion_isaaclab"></a>**bipedal_locomotion_isaaclab**: Isaac Lab 학습과 실기 전이 | `TRON1` | [Andy-xiong6 (SUSTech)](https://github.com/Andy-xiong6) | 2024 | [코드](https://github.com/Andy-xiong6/bipedal_locomotion_isaaclab) |

### 시뮬레이션 및 환경

| 프로젝트 | 기종 | 저자 / 기관 | 연도 | 링크 |
|---|---|---|---|---|
| <a id="p-tron2-wuji-bag-replay"></a>**tron2-wuji-bag-replay**: TRON2와 Wuji 핸드 궤적을 Isaac Sim에서 재생 | `TRON2` | [zengxiong111](https://github.com/zengxiong111) | 2026 | [코드](https://github.com/zengxiong111/tron2-wuji-bag-replay) |
| <a id="p-metalsim"></a>**MetalSim**: TRON1 장면을 포함한 Apple 실리콘용 시뮬레이터 | `TRON1` | [Aditya Pulipaka](https://github.com/pulipakaa24) | 2026 | [코드](https://github.com/pulipakaa24/MetalSim) |
| <a id="p-robot-sim-docker"></a>**robot-sim-docker**: LimX용 Gazebo, Isaac Lab, MuJoCo 컨테이너 | `TRON1` | [Aklva](https://github.com/Aklva) | 2026 | [코드](https://github.com/Aklva/robot-sim-docker) |
| <a id="p-limx-robotics-mcp"></a>**limx-robotics-mcp**: 시뮬레이션과 제어를 위한 MCP 서버 | `TRON1` `Oli` | [sandraschi](https://github.com/sandraschi) | 2026 | [코드](https://github.com/sandraschi/limx-robotics-mcp) |
| <a id="p-tron_docker_sim"></a>**tron_docker_sim**: Gazebo 시뮬레이션용 Docker 이미지 | `TRON1` | [The-RoboTUM](https://github.com/The-RoboTUM) | 2026 | [코드](https://github.com/The-RoboTUM/tron_docker_sim) |
| <a id="p-arc-bridge"></a>**ARC Bridge**: TRON1용 컨트롤러-MuJoCo 브리지 | `TRON1` | [UMich ARCaD Lab](https://github.com/ARCaD-Lab-UM) | 2024 | [코드](https://github.com/ARCaD-Lab-UM/arc-bridge) |

### 배포 및 제어

| 프로젝트 | 기종 | 저자 / 기관 | 연도 | 링크 |
|---|---|---|---|---|
| <a id="p-tron2_camera_calibration"></a>**tron2_camera_calibration**: TRON2 머리·손목 카메라 캘리브레이션 도구 | `TRON2` | [zengxiong111](https://github.com/zengxiong111) | 2026 | [코드](https://github.com/zengxiong111/tron2_camera_calibration) |
| <a id="p-tron1_wheel_gui"></a>**tron1_wheel_gui**: 실기 TRON1용 Qt 제어 패널 | `TRON1` | [Yang Zhuqi](https://github.com/Y20-code-cpu) | 2026 | [코드](https://github.com/Y20-code-cpu/tron1_wheel_gui) |
| <a id="p-wf_tron1b_deploy"></a>**wf_tron1b_deploy**: 깊이 인지 정책 sim-to-sim | `TRON1` | [Leixin Chang](https://github.com/Leixinjonaschang) | 2026 | [코드](https://github.com/Leixinjonaschang/wf_tron1b_deploy) |
| <a id="p-tron_deploy"></a>**Tron_Deploy**: Windows에서 정책 배포 | `TRON1` | [candi4](https://github.com/candi4) | 2026 | [코드](https://github.com/candi4/Tron_Deploy) |
| <a id="p-crl-humanoid-ros"></a>**CRL Humanoid ROS**: G1과 TRON1A용 ROS 2 프레임워크 | `TRON1` | [Jin Cheng (ETH Zurich CRL)](https://github.com/catachiii) | 2025 | [코드](https://github.com/catachiii/crl-humanoid-ros) |

### 모델 및 모션 데이터

| 프로젝트 | 기종 | 저자 / 기관 | 연도 | 링크 |
|---|---|---|---|---|
| <a id="p-rimkit"></a>**RIMKit**: 접촉 인식 리타게팅, Oli 지원 | `Oli` | [Taemoon Jeong](https://github.com/tmjeong1103) | 2026 | [코드](https://github.com/tmjeong1103/RIMKit) |
| <a id="p-tron2_revo3_description"></a>**tron2_revo3_description**: BrainCo Revo3 손을 단 TRON2 | `TRON2` | [ENDLESS0321](https://github.com/ENDLESS0321) | 2026 | [코드](https://github.com/ENDLESS0321/tron2_revo3_description) |
| <a id="p-robot_descriptionspy"></a>**robot_descriptions.py**: TRON1, TRON2, Oli, Luna 모델을 한 줄로 불러오기 | `TRON1` `TRON2` `Oli` `Luna` | [robot-descriptions](https://github.com/robot-descriptions) | 2026 | [코드](https://github.com/robot-descriptions/robot_descriptions.py) |
| <a id="p-limx-3d-measurement-workbench"></a>**limx-3d-measurement-workbench**: TRON 모델 탐색과 치수 측정 | `TRON1` `TRON2` | [voniu](https://github.com/voniu) | 2026 | [코드](https://github.com/voniu/limx-3d-measurement-workbench) |

## 교육 및 대회

_9개: 논문 1 · 코드 7 · 튜토리얼 1_

| 프로젝트 | 기종 | 저자 / 기관 | 연도 | 유형 | 링크 |
|---|---|---|---|---|---|
| <a id="p-atec-2026-simulation-challenge"></a>**ATEC 2026 Simulation Challenge**: TRON1·TRON2A 부문이 있는 공식 챌린지 | `TRON1` `TRON2`&nbsp;*sim* | [ATEC](https://github.com/atecup) | 2026 | 코드 | [코드](https://github.com/atecup/ATEC2026_Simulation_Challenge) |
| <a id="p-troncamp-2026-mani-solution"></a>**TRONCamp 2026 Mani Solution**: ACT 기반 양팔 매니퓰레이션 | `TRON2`&nbsp;*sim* | [han-xudong](https://github.com/han-xudong) | 2026 | 코드 | [코드](https://github.com/han-xudong/troncamp-mani) |
| <a id="p-troncamp-2026-locomotion-solution"></a>**TRONCamp 2026 Locomotion Solution**: SFYG TRON2A RL 정책 | `TRON2`&nbsp;*sim* | [han-xudong](https://github.com/han-xudong) | 2026 | 코드 | [코드](https://github.com/han-xudong/troncamp-locomotion) |
| <a id="p-study_tron1"></a>**study_tron1**: 환경 설정 노트와 학습 기록 | `TRON1`&nbsp;*sim* | [beamkeerati](https://github.com/beamkeerati) | 2026 | 코드 | [코드](https://github.com/beamkeerati/study_tron1) |
| <a id="p-openarm-mobile-manipulation-lab"></a>**OpenArm Mobile Manipulation Lab**: TRON1과 OpenArm, LLM 미션 (한국어) | `TRON1`&nbsp;*sim* | [aha645](https://github.com/aha645) | 2026 | 코드 | [코드](https://github.com/aha645/openarms_llm_ex) |
| <a id="p-limx-tron1-learning"></a>**LimX Tron1 Learning**: 인터랙티브 Isaac Lab 가이드 | `TRON1`&nbsp;*sim* | [jessiezhg](https://huggingface.co/jessiezhg) | 2026 | 튜토리얼 | [튜토리얼](https://huggingface.co/spaces/jessiezhg/LimX-Tron1-Learning) |
| <a id="p-canton-tower-robot-climbing-challenge"></a>**광저우타워 로봇 등반 챌린지**: 우승 및 최우수 정밀 제어상, FastStair 사용 | `Oli` | LimX | 2025 | 논문 | [논문](https://arxiv.org/abs/2601.10365)&nbsp;·&nbsp;[결과](https://www.sfccn.com/2026/1-1/5NMDE0NzNfMjA5MzM5NA.html) |
| <a id="p-rl-bipedal-locomotion"></a>**RL Bipedal Locomotion**: SUSTech ACR2025 수업 프로젝트 | `TRON1`&nbsp;*sim* | [81578823 (SUSTech)](https://github.com/81578823) | 2025 | 코드 | [코드](https://github.com/81578823/RL_bipedal_locomotion_Isaaclab) |
| <a id="p-pointfootgym"></a>**pointfootGym**: Isaac Gym 수업용 템플릿 | `TRON1`&nbsp;*sim* | [Haokai Su (SUSTech CLEAR Lab)](https://github.com/SuDaxia-kai) | 2024 | 코드 | [코드](https://github.com/SuDaxia-kai/pointfootGym) |

## 산업 적용

_14개 (5개 그룹)_

### 적용 사례 및 제품

| 프로젝트 | 기종 | 저자 / 기관 | 연도 | 유형 | 링크 |
|---|---|---|---|---|---|
| <a id="p-tenniix-ultra-max"></a>**TENNIIX ULTRA MAX**: TRON2 휠-레그를 기반으로 한 테니스 로봇, 2026 빌리 진 킹 컵 파이널에서 프로 선수와 대결 | `TRON2` | Enhanced Robotics (Tenniix) | 2026 | 논문 | [보도](https://www.news.cn/sports/20260928/f1776d7ca75042568a5137e256fa9425/c.html) |
| <a id="p-zinova-tron2-construction"></a>**ZINOVA Tool Intelligence**: TRON2 두 대가 네일건과 철근으로 축소판 틸트업 공정을 시연 | `TRON2` | ZINOVA, RIC Robotics | 2026 | 논문 | [영상](https://www.youtube.com/watch?v=8KDxnT-4zl0)&nbsp;·&nbsp;[보도](https://www.equipmentworld.com/technology/article/15836367/zinova-limx-bring-toolwielding-robots-to-construction) |
| <a id="p-dongtu-domestic-architecture"></a>**국산 전자 아키텍처 휴머노이드**: 둥투커지의 Intewell OS와 AUTBUS 버스를 탑재한 Oli, 공동 발표 | `Oli` | 둥투커지(Kyland) | 2026 | 논문 | [보도](http://mp.weixin.qq.com/s?__biz=Mzk0NDU5NjMwMA==&mid=2247495106&idx=1&sn=8b5ffd05d0615a0581d3b23a18f2d830&chksm=c20243eecd5be209a820feecab39fcb0480f5ec903b40f0d655db8f6225b378bd0e8f1db3a1a)&nbsp;·&nbsp;[보도](https://m.21jingji.com/article/20260929/herald/af2d0b02d6e7593ed4a2af7d05a191b5.html) |

### 상업 공연 및 이벤트

| 프로젝트 | 기종 | 저자 / 기관 | 연도 | 유형 | 링크 |
|---|---|---|---|---|---|
| <a id="p-nio-gba-auto-show"></a>**광둥·홍콩·마카오 모터쇼 NIO 부스**: NIO 부스에서 Oli와 Luna가 인터랙티브 시연 | `Oli` `Luna` | NIO | 2026 | 논문 | [보도](https://news.ifeng.com/c/8vmGa3sP4u7) |
| <a id="p-kill-it-finale"></a>**〈킬잇: 스타일 크리에이터 대전쟁〉 결승**: 디자이너 김나라의 우승 결승 무대에 Luna 출연, tvN | `Luna` | tvN, 김나라 | 2026 | 논문 | [보도](https://isplus.com/article/view/isp202607290025)&nbsp;·&nbsp;[보도](https://mikekalil.com/blog/the-rise-of-limx-dynamics/) |
| <a id="p-taobao-influencer-festival"></a>**타오바오 인플루언서 페스티벌**: 상하이에서 배우 천이한과 Luna가 런웨이 워킹 | `Luna` | 타오바오 | 2026 | 논문 | [보도](https://mikekalil.com/blog/limx-dynamics-luna-humanoid-robot/) |

### 전략적 제휴

| 프로젝트 | 기종 | 저자 / 기관 | 연도 | 유형 | 링크 |
|---|---|---|---|---|---|
| <a id="p-smartcube-partnership"></a>**스마트큐브**: 한국 공식 파트너, 공장·에너지 현장 점검에 휴머노이드와 디지털 트윈 활용 | — | 스마트큐브 | 2026 | 논문 | [보도](https://www.aipostkorea.com/news/articleView.html?idxno=12727) |
| <a id="p-guangyang-partnership"></a>**광양구펀**: 전략적 협력 협약 체결 | — | 광양구펀 | 2026 | 논문 | [보도](https://www.nbd.com.cn/articles/2026-03-09/4285402.html) |
| <a id="p-saic-beijing-joint-lab"></a>**상하이자동차 베이징 공동 연구소**: 자동차 제조를 위한 임바디드 AI 공동 연구소, LimX는 SAIC의 첫 임바디드 AI 전략 파트너 | — | SAIC 베이징 | 2025 | 논문 | [보도](https://www.pingwest.com/a/306356) |

### 지역 파트너 및 판매 채널

| 프로젝트 | 기종 | 저자 / 기관 | 연도 | 유형 | 링크 |
|---|---|---|---|---|---|
| <a id="p-knoxlabs-data-collection"></a>**Knoxlabs**: 미국에서 TRON2·Oli 번들 판매, 데이터 수집용 원격 조작 설정 제공 | `TRON2` `Oli` | Knoxlabs | 2026 | 논문 | [프로젝트](https://www.knoxlabs.com/blogs/articles/robot-teleoperation-data-collection-limx) |
| <a id="p-tron-kk-humanoid-si"></a>**TRON K.K.**: 일본에서 휴머노이드 시스템 통합과 Omniverse 시뮬레이션 제공, LimX 로봇 취급 | — | TRON K.K.(일본) | 2026 | 논문 | [프로젝트](https://tron.tokyo/en/service/limx-dynamics/) |
| <a id="p-synerex-korea"></a>**씨너렉스**: 한국 공식 파트너, 드론쇼코리아 2025에서 TRON1 국내 첫 공개 | `TRON1` | 씨너렉스 | 2025 | 논문 | [보도](https://www.newswire.co.kr/newsRead.php?no=1005949) |
| <a id="p-r2c2-partnership"></a>**R2C2**: 홍콩 공식 개발사 겸 유통사, 강화학습 로봇을 유틸리티·점검 업무에 활용 | `W1` `P1` | R2C2 Limited(홍콩) | 2024 | 논문 | [보도](https://www.linkedin.com/posts/limx-dynamics_robotics-partnership-innovation-activity-7211709457666310145-ddt9) |

### 수상 및 인정

| 프로젝트 | 기종 | 저자 / 기관 | 연도 | 유형 | 링크 |
|---|---|---|---|---|---|
| <a id="p-rbr50-2025-tron1"></a>**RBR50 로보틱스 혁신상 2025**: TRON1이 멀티모달 이족 R&D 플랫폼으로 선정 | `TRON1` | The Robot Report | 2025 | 논문 | [결과](https://www.therobotreport.com/rbr50-company-2025/tron-1-multi-modal-biped-offers-a-unique-rd-platform/) |

## 기종별

기종마다 전용 페이지가 있으며, 해당 기종을 사용한 항목을 모두 모았습니다: [TRON1](robots/TRON1_ko.md) · [TRON2](robots/TRON2_ko.md) · [Oli](robots/Oli_ko.md) · [Luna](robots/Luna_ko.md) · [P1](robots/P1_ko.md) · [W1](robots/W1_ko.md)

기종별·분류별 수록 개수:

| 기종 | 합계 | 보행 | 인지 | 매니퓰레이션 | 임바디드 AI | 도구 | 교육 | 산업 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| [`TRON1`](robots/TRON1_ko.md) | **54** | 21 | 5 | 5 |  | 15 | 6 | 2 |
| [`TRON2`](robots/TRON2_ko.md) | **18** |  |  | 2 | 5 | 5 | 3 | 3 |
| [`Oli`](robots/Oli_ko.md) | **20** | 9 |  | 2 | 2 | 3 | 1 | 3 |
| [`Luna`](robots/Luna_ko.md) | **5** | 1 |  |  |  | 1 |  | 3 |
| [`P1`](robots/P1_ko.md) | **4** | 3 |  |  |  |  |  | 1 |
| [`W1`](robots/W1_ko.md) | **2** |  |  | 1 |  |  |  | 1 |

## 기여하기

자기 추천과 타인 추천 모두 환영합니다. [제출 양식](https://github.com/limxdynamics/awesome-limx/issues/new?template=add-project.yml), Pull Request, 또는 이메일 [opensource@limxdynamics.com](mailto:opensource@limxdynamics.com)으로 보내 주세요. 영어, 중국어, 일본어, 한국어 모두 괜찮습니다. 수록 기준은 [CONTRIBUTING.md](CONTRIBUTING.md)를 참고하세요. 각 분류는 최신순으로 정렬되어 있습니다. '유형' 열은 독자가 얻을 수 있는 것을 나타냅니다: 바로 실행할 수 있는 것(**코드**), 따라 배울 수 있는 것(**튜토리얼**), 읽을 수 있는 것(**논문**).

수록은 LimX의 보증을 의미하지 않으며 모든 권리는 원저작자에게 있습니다. 소유자는 이유와 관계없이 언제든 삭제를 요청할 수 있습니다.

제휴 및 구매 문의는 [opensource@limxdynamics.com](mailto:opensource@limxdynamics.com)으로 연락해 주세요.


## 라이선스

이 목록은 [CC0 1.0](LICENSE)으로 공개됩니다. 링크된 프로젝트에는 각자의 라이선스가 적용됩니다.
