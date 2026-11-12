<p align="center"><img src="assets/banner_ko.png" alt="Awesome LimX" width="100%"></p>

<p align="center">
  <a href="README.md">English</a> | <a href="README_cn.md">中文</a> | <a href="README_ja.md">日本語</a> | <b>한국어</b>
</p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-CC0--1.0-2f6feb" alt="License: CC0-1.0"></a>
  <a href="https://github.com/limxdynamics/limxdynamics/blob/main/doc/wechat_qr.png"><img src="https://img.shields.io/badge/WeChat-Developer%20Community-07C160?logo=wechat&logoColor=white" alt="WeChat Community"></a>
</p>

> LimX 로봇과 LimX SDK 관련 **157**개 프로젝트와 협력 사례를 모았고, 그중 **104**개는 오픈소스 코드를 제공합니다. 논문, 코드, 데이터셋, 튜토리얼, 대회 결과, 산업 적용 사례를 다룹니다. LimX 공식 오픈소스는 [GitHub](https://github.com/limxdynamics)와 [Hugging Face](https://huggingface.co/limxdynamics)에서 확인하세요.

**기종별로 찾기**

| [**TRON1**](robots/TRON1_ko.md) | [**TRON2**](robots/TRON2_ko.md) | [**Oli**](robots/Oli_ko.md) | [**Luna**](robots/Luna_ko.md) | [**P1**](robots/P1_ko.md) | [**W1**](robots/W1_ko.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 90개 | 34개 | 27개 | 7개 | 5개 | 4개 |

## 목차

- [시작하기 전에](#시작하기-전에)
- [보행 및 전신 제어](#보행-및-전신-제어) — 50
  - [지형 및 인지 기반 보행](#지형-및-인지-기반-보행)
  - [강화학습 훈련 및 실기 전이](#강화학습-훈련-및-실기-전이)
  - [모델 기반 제어](#모델-기반-제어)
  - [모션 트래킹 및 리타게팅](#모션-트래킹-및-리타게팅)
- [인지 및 내비게이션](#인지-및-내비게이션) — 13
- [매니퓰레이션](#매니퓰레이션) — 11
- [임바디드 AI](#임바디드-ai) — 9
- [도구, 시뮬레이션 및 SDK](#도구-시뮬레이션-및-sdk) — 22
  - [학습 프레임워크](#학습-프레임워크)
  - [시뮬레이션 및 환경](#시뮬레이션-및-환경)
  - [배포 및 제어](#배포-및-제어)
  - [모델 및 모션 데이터](#모델-및-모션-데이터)
- [교육 및 대회](#교육-및-대회) — 18
- [산업 적용](#산업-적용) — 34
  - [적용 사례 및 제품](#적용-사례-및-제품)
  - [기업 오픈소스](#기업-오픈소스)
  - [상업 공연 및 이벤트](#상업-공연-및-이벤트)
  - [전략적 제휴](#전략적-제휴)
  - [지역 파트너 및 판매 채널](#지역-파트너-및-판매-채널)
  - [수상 및 인정](#수상-및-인정)
- [기종별](#기종별)
- [기여하기](#기여하기)

<sub>**코드** 바로 실행 가능 · **튜토리얼** 따라 배울 수 있음 · **논문** 읽을거리 · **보도** 언론 보도나 발표 · *sim* 시뮬레이션에서만 보여준 성과, 나머지는 실제 로봇에서 동작 · **—** 특정 기종에 한정되지 않음</sub>

## 시작하기 전에

아래의 모든 성과는 같은 네 단계를 바탕으로 합니다. 처음이라면 순서대로 따라가세요. 여기 있는 것은 LimX 공식 저장소이며 커뮤니티 프로젝트가 아닙니다.

| 단계 | 필요한 것 | 받는 곳 |
|---|---|---|
| 1 · 모델 | 로봇의 URDF, MJCF, USD | [TRON1](https://github.com/limxdynamics/tron1-robot-description) · [TRON2](https://github.com/limxdynamics/tron2-robot-description) · [Oli](https://github.com/limxdynamics/humanoid-description) · [Luna](https://github.com/limxdynamics/luna-description) |
| 2 · 인터페이스 | 저수준 모션 SDK, ROS 2 | [limxsdk-lowlevel](https://github.com/limxdynamics/limxsdk-lowlevel) |
| 3 · 학습 | Isaac Lab, Isaac Gym, MuJoCo | [TRON1](https://github.com/limxdynamics/tron1-rl-isaaclab) · [TRON2](https://github.com/limxdynamics/tron2_rl_lab) · [Oli](https://github.com/limxdynamics/humanoid-rl-isaaclab) · [Luna](https://github.com/limxdynamics/luna-beyondmimic)<br>MuJoCo sim-to-sim 검증: [TRON1](https://github.com/limxdynamics/tron1-mujoco-sim) · [TRON2](https://github.com/limxdynamics/tron2_mujoco_sim) · [Oli](https://github.com/limxdynamics/humanoid-mujoco-sim) |
| 4 · 배포 | ONNX 런타임, ROS 2, C++ | [TRON1](https://github.com/limxdynamics/tron1-rl-deploy-python) · [TRON2](https://github.com/limxdynamics/tron2_rl_deploy_python) · [Oli](https://github.com/limxdynamics/humanoid-rl-deploy-python) · Luna: 배포 저장소 아직 미공개 |

**LimX 로봇으로 무언가 만들었나요?** 이 목록에 추가할 수 있습니다 —— [프로젝트 제출](https://github.com/limxdynamics/awesome-limx/issues/new?template=add-project.yml)(링크만 있으면 됩니다). 먼저 [기여 안내](CONTRIBUTING.md)를 읽어도 좋습니다. 코드는 원래 저장소에 그대로 두시면 됩니다.

## 보행 및 전신 제어

_51개 (4개 그룹): 논문 20 · 코드 31_

### 지형 및 인지 기반 보행

| 프로젝트 | 기종 | 저자 / 기관 | 연도 | 유형 | 링크 |
|---|---|---|---|---|---|
| <a id="p-ame-2"></a>**AME-2**: 어텐션 기반 지도 인코딩으로 드문 발판에서도 민첩하고 일반화된 인지 보행 | `TRON1` | [ETH Zurich RSL](https://rsl.ethz.ch) | 2026 | 논문 | [프로젝트](https://sites.google.com/leggedrobotics.com/ame-2)&nbsp;·&nbsp;[논문](https://arxiv.org/abs/2601.08485) |
| <a id="p-faststair"></a>**FastStair**: 모델 기반 발판 계획과 강화학습을 결합해 계단을 달려 오름 | `Oli` | HIT, LimX et al. | 2026 | 논문 | [프로젝트](https://npcliu.github.io/FastStair)&nbsp;·&nbsp;[논문](https://arxiv.org/abs/2601.10365)&nbsp;·&nbsp;[영상](https://youtu.be/SoLBK7VEGDo) |
| <a id="p-steppingstonelocomotion"></a>**SteppingStoneLocomotion**: 3단계 PPO 커리큘럼으로 징검돌 건너기: 블라인드, 깊이 시각, 상태 추정기 순서 | `TRON1`&nbsp;*sim* | [Yiyou6](https://github.com/Yiyou6) | 2026 | 코드 | [코드](https://github.com/Yiyou6/SteppingStoneLocomotion)&nbsp;·&nbsp;[영상](https://www.youtube.com/watch?v=vs608-L7kl0) |
| <a id="p-height-adjustable-wheel-legged-rl"></a>**Height-Adjustable Wheel-Legged RL**: 휠풋 TRON1의 지형 적응과 차체 높이 조절 | `TRON1` | 구이린전자과기대, 상하이교통대, 저장대 | 2026 | 논문 | [논문](https://doi.org/10.1109/amc67705.2026.11435832) |
| <a id="p-reference-guided-stair-climbing"></a>**Reference-Guided Stair Climbing**: 참조 궤적 유도 강화학습으로 휠풋 TRON1 계단 주행, 학사 논문 | `TRON1`&nbsp;*sim* | 웁살라 대학교 | 2026 | 논문 | [논문](http://urn.kb.se/resolve?urn=urn:nbn:se:uu:diva-594330) |
| <a id="p-ame-locomotion-tron2a"></a>**AME Locomotion for TRON2A**: Isaac Lab AME 재현에 TRON2A 족형 환경 추가 | `TRON2`&nbsp;*sim* | [possibleustc](https://github.com/possibleustc) | 2026 | 코드 | [코드](https://github.com/possibleustc/AME_Locomotion) |
| <a id="p-offline-visual-encoder-biped"></a>**Offline Visual Encoder for Biped Locomotion**: 깊이→높이 인코더를 오프라인 학습 후 고정해 시각 기반 보행을 학습 | `TRON1` | 화중과기대학교 | 2026 | 논문 | [논문](https://doi.org/10.1109/access.2026.3686506) |
| <a id="p-barlowwalk"></a>**BarlowWalk**: Barlow Twins 자기지도 지형 표현으로 지형 적응 보행 | `TRON1`&nbsp;*sim* | HIT Shenzhen | 2025 | 논문 | [논문](https://arxiv.org/abs/2508.00939) |
| <a id="p-ctbc"></a>**CTBC**: 접촉을 계기로 계단을 오르는 블라인드 방법, 휠 이족이 지시 궤적으로 학습 | `TRON1` | Shanghai University, COWAROBOT | 2025 | 논문 | [프로젝트](https://ctbc-for-wheeled-bipedal-robots.github.io/)&nbsp;·&nbsp;[논문](https://arxiv.org/abs/2509.02986) |
| <a id="p-ga-phl"></a>**GA-PHL**: 발밑 지형을 실시간으로 재구성해 보행 타이밍을 조절하는 인지 보행 | `Oli` | USTC, LimX et al. | 2025 | 논문 | [프로젝트](https://ga-phl.github.io/)&nbsp;·&nbsp;[논문](https://arxiv.org/abs/2512.07464) |
| <a id="p-lipm-guided-rl"></a>**LIPM-Guided RL**: 선형 역진자 모델에서 착안한 보상으로 실외에서도 안정적이고 외란에 강한 인지 보행 | `TRON1` | SUSTech CLEAR Lab, HKUST et al. | 2025 | 논문 | [논문](https://arxiv.org/abs/2509.09106) |
| <a id="p-vmts"></a>**VMTS**: 시각을 쓰는 전문가 혼합 교사-학생 RL로 다양한 지형을 보행 | `P1` | Southeast University | 2025 | 코드 | [논문](https://arxiv.org/abs/2503.07049)&nbsp;·&nbsp;[코드](https://github.com/chenfu-user/VMTS) |

### 강화학습 훈련 및 실기 전이

| 프로젝트 | 기종 | 저자 / 기관 | 연도 | 유형 | 링크 |
|---|---|---|---|---|---|
| <a id="p-biped-rl-with-pathfinding"></a>**Biped RL with Pathfinding**: 사용자 정의 목표와 경로 탐색을 갖춘 Isaac Lab 학습 환경 | `TRON1`&nbsp;*sim* | [shandilya1998](https://github.com/shandilya1998) | 2026 | 코드 | [코드](https://github.com/singhaman1750/biped-rl-isaaclab-iisc) |
| <a id="p-osram"></a>**OSRAM**: 폐루프 시스템을 온라인으로 모델링해 실기에 남는 추종 오차를 보정 | `TRON1` | [Duke University](https://github.com/generalroboticslab) | 2026 | 코드 | [코드](https://github.com/generalroboticslab/OSRAM) |
| <a id="p-rl-tron1"></a>**TRON1 Teacher-Student RL**: 포인트풋 버전용 교사-학생 구조 Isaac Lab 보행 학습 | `TRON1`&nbsp;*sim* | [Jiakang Ma](https://github.com/Jiakang-Ma) | 2026 | 코드 | [코드](https://github.com/Jiakang-Ma/rl-tron1) |
| <a id="p-tron1-sliding-analysis"></a>**TRON1 Sliding Analysis**: 휠풋 정책이 어떤 마찰에서 미끄러지기 시작하는지 Isaac과 MuJoCo로 검증 | `TRON1`&nbsp;*sim* | [Shukashuki](https://github.com/Shukashuki) | 2026 | 코드 | [코드](https://github.com/Shukashuki/tron1-sliding-analysis) |
| <a id="p-vaps"></a>**VAPS**: 공중제비 중 계속·중단·안전 낙하를 선택, 실기로 옆돌기 시연 | `Oli` | TU Darmstadt, LimX et al. | 2026 | 논문 | [프로젝트](https://vaps-r-al.github.io/)&nbsp;·&nbsp;[논문](https://arxiv.org/abs/2610.01397) |
| <a id="p-wf_tron1a-stand-still-policy"></a>**Wheel-Foot TRON1 Stand-Still Policy**: RL 보상을 조정해 속도 0 명령에서 휠풋 로봇이 흘러가지 않고 정지하도록 함 | `TRON1`&nbsp;*sim* | [F-Morry](https://github.com/F-Morry) | 2026 | 코드 | [코드](https://github.com/F-Morry/limx_rl) |
| <a id="p-where-to-learn"></a>**Where-to-Learn**: 해석적 정책 그래디언트로 온폴리시 강화학습의 탐색 방향을 유도 | `TRON1` | ZJU, SUSTech | 2026 | 논문 | [프로젝트](https://wheretolearn.github.io)&nbsp;·&nbsp;[논문](https://arxiv.org/abs/2603.27317)&nbsp;·&nbsp;[영상](https://www.youtube.com/watch?v=DztdUyh_LVk) |
| <a id="p-zetin-tron1-deploy"></a>**Zetin TRON1 Deploy**: 팀의 정책을 MuJoCo와 포인트풋·솔풋 실기에 배포 | `TRON1` | [Chanjun Lee (UOS Zetin)](https://github.com/chanjun-nyam) | 2026 | 코드 | [코드](https://github.com/chanjun-nyam/Zetin-Humanoid-RL-Deploy) |
| <a id="p-sf_tron-ext-estimator"></a>**Sole-Foot TRON1 Disturbance Estimator**: 깊이 인지 잔차 정책에 이력 기반 외란 추정기를 추가 | `TRON1`&nbsp;*sim* | [EVENWaterOne](https://github.com/EVENWaterOne) | 2026 | 코드 | [코드](https://github.com/EVENWaterOne/SF_TRON_Ext-estimator) |
| <a id="p-imfs"></a>**IMFS**: 월드 모델로 발 디딤 위치를 계획하고 솔풋 TRON1이 추종 (Isaac Gym) | `TRON1`&nbsp;*sim* | [Fleming-Sung](https://github.com/Fleming-Sung) | 2026 | 코드 | [코드](https://github.com/Fleming-Sung/imfs) |
| <a id="p-shape-your-body"></a>**Shape Your Body**: 족형 로봇 50종 대상 가치 기울기 설계 탐색, TRON1 전용 학습 설정 포함 | `TRON1`&nbsp;*sim* | [nico-bohlinger](https://github.com/nico-bohlinger) | 2026 | 코드 | [코드](https://github.com/nico-bohlinger/shape-your-body) |
| <a id="p-model-based-gait-planning-rl"></a>**Model-Based Gait Planning RL**: 3D-LIPM 참조 보행으로 수작업 보행 보상을 대체해 RL 학습 | `TRON1` | 하얼빈 공업대학교 | 2026 | 논문 | [논문](https://doi.org/10.1016/j.birob.2026.100338) |
| <a id="p-w1-parkour-legged-gym"></a>**W1 Parkour in legged_gym**: legged_gym에서 W1 휠-레그 사족용 파쿠르·추종 환경 구축, ROS 컨트롤러 포함 | `W1`&nbsp;*sim* | [yiqiuqwq](https://github.com/yiqiuqwq) | 2026 | 코드 | [코드](https://github.com/yiqiuqwq/wheellegged_control) |
| <a id="p-him-pim-isaac-lab"></a>**HIM-PIM Isaac Lab**: Isaac Lab에서 HIM과 PIM 보행 제어를 비교, 계단·경사·외란으로 검증 | `TRON1`&nbsp;*sim* | [DongyangLin](https://github.com/DongyangLin) | 2025 | 코드 | [코드](https://github.com/DongyangLin/HIM-PIM-isaaclab) |
| <a id="p-leggedrobotslab"></a>**LeggedRobotsLab**: Isaac Lab 보행 학습, MuJoCo sim-to-sim과 실기 배포 포함, Go1과 TRON1 지원 | `TRON1`&nbsp;*sim* | [Guohua Zhang](https://github.com/guohua-zhang) | 2025 | 코드 | [코드](https://github.com/guohua-zhang/LeggedRobotsLab) |
| <a id="p-multi-loco"></a>**Multi-Loco**: 하나의 확산 모델 정책으로 포인트풋과 휠풋 로봇을 모두 제어 | `TRON1` | SUSTech CLEAR Lab, LimX et al. | 2025 | 코드 | [프로젝트](https://multi-loco.github.io)&nbsp;·&nbsp;[논문](https://arxiv.org/abs/2506.11470)&nbsp;·&nbsp;[코드](https://github.com/clearlab-sustech/multi_loco_isaacgym) |
| <a id="p-pvp"></a>**PvP**: 고유감각과 특권 상태 간 대조 학습으로 데이터 효율적인 전신 제어 | `Oli` | PolyU, USTC et al. | 2025 | 논문 | [논문](https://arxiv.org/abs/2512.13093) |
| <a id="p-tron-camp-wheel-foot-deployment"></a>**TRON Camp Wheel-Foot Deployment**: TRON Camp 2025를 위해 휠풋 정책을 조정해 실기에서 구동 | `TRON1` | [Yitao Zeng](https://github.com/24zen0) | 2025 | 코드 | [코드](https://github.com/24zen0/Deployment_of_wheelfoot_tron) |
| <a id="p-ptrl"></a>**PTRL**: 로봇 간 사전 지식 전이로 RL 학습 시간 단축, Go2와 TRON1에서 실기 검증 | `TRON1` | 하얼빈공대(선전), 쑤저우대 | 2025 | 논문 | [논문](https://arxiv.org/abs/2504.05629) |
| <a id="p-anybipe"></a>**AnyBipe**: 언어 모델이 이족 정책의 보상 설계·학습·배포를 이끄는 엔드투엔드 프레임워크 | `TRON1` | [SJTU](https://github.com/sjtu-mvasl-robotics) | 2024 | 코드 | [코드](https://github.com/sjtu-mvasl-robotics/AnyBipe) |
| <a id="p-cts"></a>**CTS**: 교사·학생 정책을 동시에 학습하는 족형 보행 강화학습 | `P1` | SUSTech CLEAR Lab, ZJU-UIUC et al. | 2024 | 논문 | [프로젝트](https://clearlab-sustech.github.io/concurrentTS/)&nbsp;·&nbsp;[논문](https://arxiv.org/abs/2405.10830) |

### 모델 기반 제어

| 프로젝트 | 기종 | 저자 / 기관 | 연도 | 유형 | 링크 |
|---|---|---|---|---|---|
| <a id="p-learning-enhanced-pmp-mpc"></a>**Learning-Enhanced PMP-MPC**: 폰트랴긴 최적화기와 학습 잔차로 무게중심 MPC를 풀고 MuJoCo에서 검증 | `TRON1`&nbsp;*sim* | [Markwcl2004](https://github.com/Markwcl2004) | 2026 | 코드 | [논문](https://doi.org/10.1109/ASCC70886.2026.11701800)&nbsp;·&nbsp;[코드](https://github.com/Markwcl2004/PMP_based_Bipedal_MPC) |
| <a id="p-whole-body-humanoid-mpc"></a>**Whole-Body Humanoid MPC**: 휴머노이드 이동 조작용 비선형 전신 MPC, MuJoCo 31자유도 Oli 예제 포함 | `Oli`&nbsp;*sim* | [Tianxing Liu](https://github.com/liuskywalkerjskd) | 2026 | 코드 | [코드](https://github.com/liuskywalkerjskd/humanoid_mpc) |
| <a id="p-terrain-aware-cfr-planning"></a>**Terrain-Aware CFR Planning**: 볼록 가능 영역 기반 계단 주행 계획, W1에서 200회 중 200회 성공 | `W1` | SUSTech CLEAR Lab | 2026 | 논문 | [논문](https://doi.org/10.21203/rs.3.rs-10577407/v1) |
| <a id="p-power-bounded-inverted-pendulum"></a>**Power-Bounded Inverted Pendulum**: 출력 한계를 고려한 이족 최고 속도 모델, 관절 모터 파라미터 재조정에 사용 | `TRON1`&nbsp;*sim* | 저장대학교 | 2026 | 논문 | [논문](https://doi.org/10.1007/s10409-026-25928-x) |
| <a id="p-hierarchical-nmpc-stsmc"></a>**Hierarchical NMPC + STSMC**: 계층형 비선형 MPC와 슈퍼 트위스팅 슬라이딩 모드 제어, 불확실성 하의 휠풋 TRON1 | `TRON1`&nbsp;*sim* | [pjmcconnellogue](https://github.com/pjmcconnellogue) | 2026 | 코드 | [코드](https://github.com/pjmcconnellogue/Hierarchical-Nonlinear-MPC-and-Super-Twisting-Sliding-Mode-Control-for-a-Wheeled-Biped-Robot-) |
| <a id="p-two-wheeled-robot-lqr"></a>**Two-Wheeled Robot LQR**: 휠풋 TRON1의 LQR 및 전신 제어, 졸업 논문 프로젝트 | `TRON1`&nbsp;*sim* | [alpttex19](https://github.com/alpttex19) | 2025 | 코드 | [코드](https://github.com/alpttex19/Two_Wheeled_Robot_LQR) |
| <a id="p-bipedal-mpc"></a>**Bipedal MPC**: 볼록 MPC와 전신 제어로 MuJoCo에서 보행, ROS 2 기반 | `TRON1`&nbsp;*sim* | [SUSTech CLEAR Lab](https://github.com/clearlab-sustech) | 2024 | 코드 | [코드](https://github.com/clearlab-sustech/Bipedal_MPC) |
| <a id="p-task-space-riccati-wbc"></a>**Task-Space Riccati WBC**: 저구동 족형 로봇을 위한 태스크 공간 Riccati 피드백 전신 제어 | `P1`&nbsp;*sim* | SUSTech, HKUST et al. | 2024 | 논문 | [논문](https://arxiv.org/abs/2404.00591) |

### 모션 트래킹 및 리타게팅

| 프로젝트 | 기종 | 저자 / 기관 | 연도 | 유형 | 링크 |
|---|---|---|---|---|---|
| <a id="p-any2any"></a>**Any2Any**: 사전학습된 전신 모션 트래킹 모델을 적은 적응으로 새 휴머노이드에 이전 | `Oli` `Luna` | LimX | 2026 | 코드 | [논문](https://arxiv.org/abs/2605.23733)&nbsp;·&nbsp;[코드](https://github.com/Ming827/any2any_sonic2Oli) |
| <a id="p-chip-for-oli"></a>**CHIP for Oli**: 적응형 컴플라이언스 모션 트래킹 CHIP 이식판, mjlab에서 학습 | `Oli`&nbsp;*sim* | [Matt14-mander](https://github.com/Matt14-mander) | 2026 | 코드 | [코드](https://github.com/Matt14-mander/chip-oli) |
| <a id="p-supermimic-for-oli"></a>**SuperMimic for Oli**: 월드 모델 전신 제어 SuperMimic 적용판, 정책 하나로 40개 동작 추종 | `Oli`&nbsp;*sim* | [Tianxing Liu](https://github.com/liuskywalkerjskd) | 2026 | 코드 | [코드](https://github.com/liuskywalkerjskd/supermimic_oli) |
| <a id="p-tron1-wf-mimic"></a>**Wheel-Foot TRON1 Dance Mimic**: 휠풋 이족으로 사람의 춤을 모방하고 이 형태로 가능한 동작과 불가능한 동작을 분석 | `TRON1`&nbsp;*sim* | [HUST-dolores](https://github.com/HUST-dolores) | 2026 | 코드 | [코드](https://github.com/HUST-dolores/tron1-wf-mimic) |
| <a id="p-robot-lab-srl-oli-mimic"></a>**Oli Mimic Tasks for robot_lab**: robot_lab 확장, Isaac Lab에 동작 모방 학습 과제 추가 | `Oli`&nbsp;*sim* | [song-hl](https://github.com/song-hl) | 2026 | 코드 | [코드](https://github.com/song-hl/robot_lab_srl) |
| <a id="p-robot-retargeter"></a>**Robot Retargeter**: SMPL-X나 다른 로봇의 동작을 휴머노이드로 리타게팅, 이 기종 전용 설정 포함 | `Oli`&nbsp;*sim* | [ccrpRepo](https://github.com/ccrpRepo) | 2026 | 코드 | [코드](https://github.com/ccrpRepo/robot_retargeter) |
| <a id="p-timo"></a>**Timo**: 텍스트-투-모션용 운동학 인지 멀티모달 확산 트랜스포머, 생성 동작을 리타게팅해 Oli와 Luna 실기에서 실행 | `Oli` `Luna` | LimX | 2026 | 논문 | [프로젝트](https://kyfafyd.wang/projects/timo)&nbsp;·&nbsp;[논문](https://arxiv.org/abs/2609.30761) |
| <a id="p-hu-d03-rl-mjlab"></a>**Earlier-Generation Oli RL in mjlab**: HU_D03 모델용 보행·동작 모방 정책, mjlab에서 학습 (베트남어) | `Oli`&nbsp;*sim* | [KhanhPham248](https://github.com/KhanhPham248) | 2026 | 코드 | [코드](https://github.com/KhanhPham248/LimX_HU_D03_rl_mjlab) |
| <a id="p-multi-embodiment-retargeting"></a>**Multi-Embodiment Retargeting**: 그래프 조건부 확산 모델로 구조가 다른 로봇들에 같은 동작을 리타게팅 | `TRON1` `Oli`&nbsp;*sim* | SUSTech, HKUST et al. | 2025 | 논문 | [논문](https://arxiv.org/abs/2505.20857) |

## 인지 및 내비게이션

_14개: 논문 3 · 코드 11_

| 프로젝트 | 기종 | 저자 / 기관 | 연도 | 유형 | 링크 |
|---|---|---|---|---|---|
| <a id="p-tron1_navrl"></a>**TRON1 NavRL**: Isaac Lab에서 상위 내비게이션 정책만 RL로 학습하고 기존 보행 정책을 재사용 | `TRON1`&nbsp;*sim* | [jongbob1918](https://github.com/jongbob1918) | 2026 | 코드 | [코드](https://github.com/jongbob1918/tron1_navrl) |
| <a id="p-tron1-multi-floor-navigation"></a>**TRON1 Multi-floor Navigation**: 평면 주행, 층 전환, 계단 주행을 하나의 미션으로 운영 (한국어) | `TRON1` | [justpastmarch](https://github.com/justpastmarch) | 2026 | 코드 | [코드](https://github.com/justpastmarch/TRON1_multifloor-navigation) |
| <a id="p-geometric-candidate-modes"></a>**Geometric Candidate Modes**: 멀티모달 시연으로 내비게이션 학습, 시뮬레이션에서 학습한 정책을 TRON1에 전이 | `TRON1` | 오하이오 주립대학교 | 2026 | 논문 | [논문](https://arxiv.org/abs/2610.20241) |
| <a id="p-ros2_gnss_waypoint_nav"></a>**GNSS Waypoint Navigation**: RTK GNSS, MID360, Nav2 기반 지도 없는 실외 웨이포인트 내비게이션, TRON1 베이스 브리지 포함 | `TRON1` | [우한대학교 BRAIN Lab](https://github.com/Whu-BrainLab) | 2026 | 코드 | [코드](https://github.com/Whu-BrainLab/ros2_gnss_waypoint_nav) |
| <a id="p-lightnav-0"></a>**LightNav-0**: VLM 기반 내비게이션 스택, MPC 추종과 웹 패널 포함, Go2와 TRON1 지원 | `TRON1` | [Light Origins](https://github.com/lightorigins) | 2026 | 코드 | [논문](https://arxiv.org/abs/2608.30935)&nbsp;·&nbsp;[코드](https://github.com/lightorigins/LightNav-0)&nbsp;·&nbsp;[모델](https://huggingface.co/LightOriginsHQ/LightNav-0) |
| <a id="p-gps-tron1"></a>**GPS-TRON1**: GNSS와 FAST-LIO 융합 측위 기반 실외 웨이포인트 주행, 국소 충돌 회피 포함 | `TRON1` | [potatoHu-a](https://github.com/potatoHu-a) | 2026 | 코드 | [코드](https://github.com/potatoHu-a/GPS-TRON1) |
| <a id="p-wf_tron1a-lidar-navigation"></a>**Wheel-Foot TRON1 LiDAR Odometry**: 2D LiDAR RF2O 오도메트리로 바퀴 미끄러짐·걸림 시 휠 오도메트리 오차를 보정 | `TRON1` | [F-Morry](https://github.com/F-Morry) | 2026 | 코드 | [코드](https://github.com/F-Morry/limx_ws) |
| <a id="p-wave-go"></a>**WAVE-Go**: 월드 모델 행동 적응 기반 장거리 내비게이션, Go2-W 실기와 MuJoCo의 Luna로 검증 | `Luna`&nbsp;*sim* | BIT, HKU, LimX 외 | 2026 | 코드 | [논문](https://arxiv.org/abs/2609.18193)&nbsp;·&nbsp;[코드](https://github.com/vigorlee/wave-go) |
| <a id="p-tron-1-struzzo"></a>**TRON-1 Struzzo**: 탑재 Jetson으로 자율 주행하는 Gazebo·ROS 2 환경 | `TRON1` | [enfff](https://github.com/enfff) | 2025 | 코드 | [코드](https://github.com/enfff/tron1-gazebo-ros2) |
| <a id="p-neupan-on-tron1"></a>**NeuPAN on TRON1**: A* 전역 계획과 NeuPAN 엔드투엔드 국소 회피를 결합한 ROS 내비게이션 | `TRON1` | [WikHClean](https://github.com/WikHClean) | 2025 | 코드 | [코드](https://github.com/WikHClean/-ROS1-NeuPAN-TRON1-) |
| <a id="p-3d-navigation-with-pct-planner"></a>**3D Navigation with PCT Planner**: Mid360 LiDAR와 PCT 플래너로 실내와 계단을 3D 내비게이션, 실기 검증 | `TRON1` | [81578823](https://github.com/81578823) | 2025 | 코드 | [코드](https://github.com/81578823/3D_navigation_PCTplanner) |
| <a id="p-terrain-aware-lio-legged-wheel"></a>**Terrain-Aware LiDAR-Inertial Odometry**: 지형을 고려한 휠-레그 로봇용 LiDAR 관성 오도메트리, 휠풋 TRON1으로 실외 실험 | `TRON1` | 상하이 교통대학교 | 2025 | 논문 | [논문](https://arxiv.org/abs/2509.26222) |
| <a id="p-eroam"></a>**EROAM**: 이벤트 카메라 회전 오도메트리, TRON1에서 수집한 시퀀스 포함 | `TRON1` | [wlxing1901](https://github.com/wlxing1901) | 2024 | 코드 | [프로젝트](https://wlxing1901.github.io/eroam/)&nbsp;·&nbsp;[논문](https://arxiv.org/abs/2411.11004)&nbsp;·&nbsp;[코드](https://github.com/wlxing1901/eroam)&nbsp;·&nbsp;[영상](https://youtu.be/8tF6b2VuvSM) |

## 매니퓰레이션

_11개: 논문 5 · 코드 6_

| 프로젝트 | 기종 | 저자 / 기관 | 연도 | 유형 | 링크 |
|---|---|---|---|---|---|
| <a id="p-cola-on-tron2"></a>**COLA on TRON2**: 사람-로봇 협동 운반 COLA를 Unitree G1에서 이식 | `TRON2`&nbsp;*sim* | [Matt14-mander](https://github.com/Matt14-mander) | 2026 | 코드 | [코드](https://github.com/Matt14-mander/COLA_TRON2) |
| <a id="p-holistic-loco-manipulation"></a>**Holistic Loco-Manipulation**: 6자유도 말단 목표를 로봇팔을 단 TRON1의 다리·팔 동작으로 직접 매핑하는 RL 전신 제어기 | `TRON1` | ZJU-UIUC, LimX | 2026 | 논문 | [논문](https://arxiv.org/abs/2609.18930) |
| <a id="p-tron1-to-ur5e-bottle-transfer"></a>**TRON1-to-UR5e Bottle Transfer**: 이족 로봇이 병을 인계 구역으로 옮기면 UR5e 팔이 집음, MuJoCo 기반 | `TRON1`&nbsp;*sim* | [Centaucyan](https://github.com/Centaucyan) | 2026 | 코드 | [코드](https://github.com/Centaucyan/Proj_Transferring_bottle_from_tron1_to_ur5e_in_mujoco_env) |
| <a id="p-cooperative-transportation"></a>**Cooperative Transportation**: 로봇 두 대가 하나의 짐을 함께 운반, 휠풋 TRON1과 TRON2 조합 지원 | `TRON1` `TRON2`&nbsp;*sim* | [Matt14-mander](https://github.com/Matt14-mander) | 2026 | 코드 | [코드 (TRON1)](https://github.com/Matt14-mander/Multiple_Humanoid_Cooperative_Transportation)&nbsp;·&nbsp;[코드 (TRON2)](https://github.com/Matt14-mander/tron2-cooperative-carrying) |
| <a id="p-cwi"></a>**CWI**: 모캡과 명령을 결합한 복합 전신 모방으로 걸으면서 조작 | `Oli` | LimX, HKU et al. | 2026 | 논문 | [프로젝트](https://cwi-ral.github.io/CWI-RAL-Webpage/)&nbsp;·&nbsp;[논문](https://arxiv.org/abs/2606.27676) |
| <a id="p-arm-tron"></a>**Arm-TRON**: 세 가지 발 형태를 바꿀 수 있는 외팔 이족과 형태별 RL 전신 제어 | `TRON1` | SUSTech, ZJU et al. | 2026 | 논문 | [논문](https://doi.org/10.1109/TMECH.2026.3727546) |
| <a id="p-mobile-pedipulation"></a>**Mobile Pedipulation**: 계층형 NMPC로 휠풋 TRON1이 바퀴 달린 다리로 물체를 밀어 옮김, RA-L | `TRON1` | 미시간 대학교 | 2026 | 논문 | [논문](https://arxiv.org/abs/2606.19233) |
| <a id="p-tron2-vision-teleoperation"></a>**TRON2 Vision Teleoperation**: 카메라로 팔과 손을 추적해 ORCA 핸드를 단 양팔 로봇을 원격 조작 (스페인어) | `TRON2`&nbsp;*sim* | [Aremanky](https://github.com/Aremanky) | 2026 | 코드 | [코드](https://github.com/Aremanky/Teleoperacion-tron-2) |
| <a id="p-umi-on-tron1"></a>**UMI on Tron1**: ARX5 팔로 UMI 조작 기술을 실기에서 실행 | `TRON1` | [Czy213hd](https://github.com/Czy213hd) | 2025 | 코드 | [코드](https://github.com/Czy213hd/umi-on-tron-lab) |
| <a id="p-quest-vr-teleop-for-oli"></a>**Quest VR Teleop for Oli**: Meta Quest로 양팔·그리퍼·머리를 원격 조작, 카메라 영상을 헤드셋에 실시간 표시 | `Oli` | [MSTLE](https://github.com/MSTLE) | 2025 | 코드 | [코드](https://github.com/MSTLE/Limx_teleoperate-end_pose) |
| <a id="p-wheeled-quadrupedal-manipulator"></a>**Wheeled-Quadrupedal Manipulator**: 휠 사족에 팔을 달고 학습한 제어기로 말단 자세를 추종 | `W1` | SUSTech CLEAR Lab, ZJU-UIUC et al. | 2024 | 논문 | [프로젝트](https://clearlab-sustech.github.io/RFM_loco_mani/)&nbsp;·&nbsp;[논문](https://arxiv.org/abs/2412.03012) |

## 임바디드 AI

_9개: 논문 2 · 코드 7_

| 프로젝트 | 기종 | 저자 / 기관 | 연도 | 유형 | 링크 |
|---|---|---|---|---|---|
| <a id="p-tron1-hermes-agent"></a>**Tron 1 Hermes Agent**: Mac에서 도는 자기 개선형 로컬 AI 에이전트가 MuJoCo에서 로봇을 조종 | `TRON1`&nbsp;*sim* | [justinsuo](https://github.com/justinsuo) | 2026 | 코드 | [코드](https://github.com/justinsuo/tron1-hermes-agent) |
| <a id="p-fluxvla-on-tron2"></a>**FluxVLA on TRON2**: FluxVLA 시각-언어-행동 모델을 자신의 로봇에서 학습·배포 | `TRON2` | [emoPointer](https://github.com/emoPointer) | 2026 | 코드 | [코드](https://github.com/emoPointer/FluxVLA) |
| <a id="p-oli-voice-interaction"></a>**Oli Voice Interaction**: 오프라인·온라인 음성 인식, LLM 대화, 동작 명령을 갖춘 ROS 2 음성 시스템 | `Oli` | [zhilin2025](https://github.com/zhilin2025) | 2026 | 코드 | [코드](https://github.com/zhilin2025/oli_audio) |
| <a id="p-hwam"></a>**HWAM**: 미래 상태와 행동을 함께 생성하는 휴머노이드 월드 액션 모델 | `Oli` | LimX | 2026 | 논문 | [프로젝트](https://hwam.vercel.app/)&nbsp;·&nbsp;[논문](https://arxiv.org/abs/2610.12026) |
| <a id="p-acg-wam"></a>**ACG-WAM**: 행동 조건부 기하 잠재 표현을 예측하는 월드 액션 모델, 다관절 손으로 검증 | `TRON2` | BIT, LimX | 2026 | 코드 | [프로젝트](https://RoboOpus.github.io/ACG-WAM)&nbsp;·&nbsp;[논문](https://arxiv.org/abs/2610.06965)&nbsp;·&nbsp;[코드](https://github.com/RoboOpus/ACG-WAM) |
| <a id="p-drifting-action-heads-for-gr00t-n17"></a>**GR00T Drifting Heads**: GR00T N1.7의 확산 액션 헤드를 원스텝 drifting 헤드로 바꿔 추론 비용 절감 | `TRON2` | ZJU-UIUC, LimX | 2026 | 논문 | [논문](https://arxiv.org/abs/2609.18108) |
| <a id="p-tron2-garment-feeder"></a>**TRON2 Garment Feeder**: 양팔 의류 투입 작업용으로 미세조정한 Pi0.5 정책 | `TRON2` | [voniu](https://huggingface.co/voniu) | 2026 | 코드 | [모델](https://huggingface.co/voniu/tron2-garment-feeder-button-pi05) |
| <a id="p-tron2-lerobot-datasets"></a>**TRON2 LeRobot Datasets**: LeRobot 형식의 집기·놓기, 옷 개기, 물 따르기 데이터셋과 이를 이용해 미세조정한 GR00T | `TRON2` | [trantor2nd](https://huggingface.co/trantor2nd) | 2026 | 코드 | [모델](https://huggingface.co/models?author=trantor2nd&search=tron2)&nbsp;·&nbsp;[데이터셋](https://huggingface.co/datasets?author=trantor2nd&search=tron2) |
| <a id="p-troncamp-pi05-policies"></a>**TRONCamp Pi0.5 Policies**: TRONCamp 꽃꽂이·옷 개기 과제용 Pi0.5 체크포인트 | `TRON2` | [toki1231](https://huggingface.co/toki1231) | 2026 | 코드 | [모델](https://huggingface.co/toki1231) |

## 도구, 시뮬레이션 및 SDK

_도구 24개 (4개 그룹)_

### 학습 프레임워크

| 프로젝트 | 기종 | 저자 / 기관 | 연도 | 링크 |
|---|---|---|---|---|
| <a id="p-tron1-isaac-lab-tasks"></a>**TRON1 Isaac Lab Tasks**: 세 가지 발 형태 전부를 위한 Isaac Lab 태스크, 점프 포함 | `TRON1` | [HughWang-wzy](https://github.com/HughWang-wzy) | 2026 | [코드](https://github.com/HughWang-wzy/tron1-rl-isaaclab) |
| <a id="p-tron1-rl-mjlab"></a>**TRON1 RL on mjlab**: mjlab에서 휠풋 보행을 학습하고 ONNX로 내보내기 | `TRON1` | [Xinchen Yao](https://github.com/hoscy) | 2025 | [코드](https://github.com/hoscy/tron1-rl-mjlab) |
| <a id="p-leggedgym-ex"></a>**LeggedGym-Ex**: Genesis, Isaac Gym, Isaac Sim에서 돌아가는 legged_gym | `TRON1` | [Yasen Jia](https://github.com/lupinjia) | 2024 | [코드](https://github.com/lupinjia/LeggedGym-Ex) |
| <a id="p-bipedal_locomotion_isaaclab"></a>**Bipedal Locomotion on Isaac Lab**: Isaac Lab에서 평지·험지·계단 보행을 학습하고 실기로 전이 | `TRON1` | [Andy-xiong6 (SUSTech)](https://github.com/Andy-xiong6) | 2024 | [코드](https://github.com/Andy-xiong6/bipedal_locomotion_isaaclab) |

### 시뮬레이션 및 환경

| 프로젝트 | 기종 | 저자 / 기관 | 연도 | 링크 |
|---|---|---|---|---|
| <a id="p-tron2-wuji-bag-replay"></a>**TRON2 Wuji Hand Replay**: 녹화한 로봇과 Wuji 핸드 궤적을 Isaac Sim에서 재생 | `TRON2` | [zengxiong111](https://github.com/zengxiong111) | 2026 | [코드](https://github.com/zengxiong111/tron2-wuji-bag-replay) |
| <a id="p-metalsim"></a>**MetalSim**: Apple 실리콘용 시뮬레이션·학습 스택, TRON1 전용 모듈 포함: 시뮬레이터, 제어기, 실기 브리지 | `TRON1` | [Aditya Pulipaka](https://github.com/pulipakaa24) | 2026 | [코드](https://github.com/pulipakaa24/MetalSim) |
| <a id="p-robot-sim-docker"></a>**Robot Sim Docker**: ROS 2와 LimX Gazebo, Isaac Lab, LeIsaac, MuJoCo를 한 호스트에서 컨테이너로 실행 | `TRON1` | [Aklva](https://github.com/Aklva) | 2026 | [코드](https://github.com/Aklva/robot-sim-docker) |
| <a id="p-limx-robotics-mcp"></a>**LimX Robotics MCP Server**: AI 에이전트가 MuJoCo 모델 로드, 관절 제어, 정책 실행을 할 수 있는 MCP 서버 | `TRON1` `Oli` | [sandraschi](https://github.com/sandraschi) | 2026 | [코드](https://github.com/sandraschi/limx-robotics-mcp) |
| <a id="p-tron_docker_sim"></a>**TRON Docker Sim**: ROS 2 Gazebo 시뮬레이션을 컨테이너에서 실행, GUI 포워딩 지원 | `TRON1` | [The-RoboTUM](https://github.com/The-RoboTUM) | 2026 | [코드](https://github.com/The-RoboTUM/tron_docker_sim) |
| <a id="p-gewu-unity-rl-playground"></a>**Gewu (Unity RL Playground)**: Unity 강화학습 플랫폼, TRON1 보행·주행·점프 정책 포함 | `TRON1` | [loongOpen](https://github.com/loongOpen) | 2025 | [논문](https://arxiv.org/abs/2503.05146)&nbsp;·&nbsp;[코드](https://github.com/loongOpen/Unity-RL-Playground) |
| <a id="p-arc-bridge"></a>**ARC Bridge**: LCM으로 로봇 제어기를 MuJoCo 시뮬레이터에 연결하는 브리지 | `TRON1` | [UMich ARCaD Lab](https://github.com/ARCaD-Lab-UM) | 2024 | [코드](https://github.com/ARCaD-Lab-UM/arc-bridge) |

### 배포 및 제어

| 프로젝트 | 기종 | 저자 / 기관 | 연도 | 링크 |
|---|---|---|---|---|
| <a id="p-tron1_ctrl_ros2"></a>**TRON1 ROS 2 Control**: 로봇 WebSocket SDK를 감싼 ROS 2 제어 패키지 | `TRON1` | [Turing-zero](https://github.com/Turing-zero) | 2026 | [코드](https://github.com/Turing-zero/tron1_ctrl_ros2) |
| <a id="p-tron2_camera_calibration"></a>**TRON2 Camera Calibration**: 머리·손목 카메라 캘리브레이션 도구 | `TRON2` | [zengxiong111](https://github.com/zengxiong111) | 2026 | [코드](https://github.com/zengxiong111/tron2_camera_calibration) |
| <a id="p-tron1_wheel_gui"></a>**TRON1 Wheel GUI**: Qt와 ROS를 결합한 제어 패널로 노트북에서 휠풋 실기를 조종 | `TRON1` | [Yang Zhuqi](https://github.com/Y20-code-cpu) | 2026 | [코드](https://github.com/Y20-code-cpu/tron1_wheel_gui) |
| <a id="p-wf_tron1b_deploy"></a>**Wheel-Foot Depth Policy Deploy**: 깊이 인지형·비인지형 휠풋 정책의 sim-to-sim 검증, Docker와 ROS 기반 | `TRON1` | [Leixin Chang](https://github.com/Leixinjonaschang) | 2026 | [코드](https://github.com/Leixinjonaschang/wf_tron1b_deploy) |
| <a id="p-tron_deploy"></a>**TRON Deploy for Windows**: Windows 11 노트북에 포인트풋 SDK를 설치하고 정책 실행 | `TRON1` | [candi4](https://github.com/candi4) | 2026 | [코드](https://github.com/candi4/Tron_Deploy) |
| <a id="p-multi-robot-camera-collector"></a>**Multi-Robot Camera Collector**: 여러 로봇의 카메라를 전환하며 작업 단계별로 프레임을 저장해 데이터 수집 (중국어) | `TRON1` `TRON2` | [oalaaCN](https://github.com/oalaaCN) | 2026 | [코드](https://github.com/oalaaCN/multi_robot_camera_collector) |
| <a id="p-crl-humanoid-ros"></a>**CRL Humanoid ROS**: ETH 취리히의 ROS 2 프레임워크, 시뮬레이션·하드웨어 제어·RL 제어기 포함, G1과 TRON1 지원 | `TRON1` | [Jin Cheng (ETH Zurich CRL)](https://github.com/catachiii) | 2025 | [코드](https://github.com/catachiii/crl-humanoid-ros) |
| <a id="p-websocket_ros"></a>**TRON1 WebSocket-ROS Bridge**: 로봇 WebSocket API를 ROS로 잇는 Docker 브리지, 실기 없이 시험할 가짜 로봇 포함 | `TRON1` | [daweidavidwang](https://github.com/daweidavidwang) | 2025 | [코드](https://github.com/daweidavidwang/websocket_ros) |

### 모델 및 모션 데이터

| 프로젝트 | 기종 | 저자 / 기관 | 연도 | 링크 |
|---|---|---|---|---|
| <a id="p-rimkit"></a>**RIMKit**: 접촉을 고려한 사람 동작 리타게팅, 휴머노이드 17종 지원, 이 기종 모델 포함 | `Oli` | [Taemoon Jeong](https://github.com/tmjeong1103) | 2026 | [코드](https://github.com/tmjeong1103/RIMKit) |
| <a id="p-tron2_revo3_description"></a>**TRON2 with Revo3 Hands**: BrainCo Revo3 손을 단 조립 모델, 바로 학습에 사용 가능 | `TRON2` | [ENDLESS0321](https://github.com/ENDLESS0321) | 2026 | [코드](https://github.com/ENDLESS0321/tron2_revo3_description) |
| <a id="p-limx-3d-measurement-workbench"></a>**LimX 3D Measurement Workbench**: TRON 제품 모델을 보고 부품을 찾아 치수를 재는 웹 도구 | `TRON1` `TRON2` | [voniu](https://github.com/voniu) | 2026 | [코드](https://github.com/voniu/limx-3d-measurement-workbench) |

## 교육 및 대회

_18개: 논문 2 · 코드 15 · 튜토리얼 1_

| 프로젝트 | 기종 | 저자 / 기관 | 연도 | 유형 | 링크 |
|---|---|---|---|---|---|
| <a id="p-atec-2026-simulation-challenge"></a>**ATEC 2026 Simulation Challenge**: ATEC 2026 로봇 시뮬레이션 챌린지 공식 스타터 코드, 기종별 트랙 구성 | `TRON1` `TRON2`&nbsp;*sim* | [ATEC](https://github.com/atecup) | 2026 | 코드 | [코드](https://github.com/atecup/ATEC2026_Simulation_Challenge) |
| <a id="p-troncamp-2026-mani-solution"></a>**TRONCamp 2026 Mani Solution**: 양팔 4개 과제용 ACT 해법, 체크포인트와 시연 데이터 공개 | `TRON2`&nbsp;*sim* | [han-xudong](https://github.com/han-xudong) | 2026 | 코드 | [코드](https://github.com/han-xudong/troncamp-mani)&nbsp;·&nbsp;[모델](https://huggingface.co/han-xudong/troncamp-mani-act)&nbsp;·&nbsp;[데이터셋](https://huggingface.co/datasets/han-xudong/troncamp-mani-dataset) |
| <a id="p-troncamp-2026-locomotion-solution"></a>**TRONCamp 2026 Locomotion Solution**: 팔을 고정한 솔풋 TRON2의 RL 보행 정책, 체크포인트 공개 | `TRON2`&nbsp;*sim* | [han-xudong](https://github.com/han-xudong) | 2026 | 코드 | [코드](https://github.com/han-xudong/troncamp-locomotion)&nbsp;·&nbsp;[모델](https://huggingface.co/han-xudong/troncamp-locomotion-rl) |
| <a id="p-study_tron1"></a>**TRON1 Study Notes**: 로봇 SDK 없이 Isaac Lab으로 학습하기 위한 환경 설정 노트와 학습 기록 | `TRON1`&nbsp;*sim* | [beamkeerati](https://github.com/beamkeerati) | 2026 | 코드 | [코드](https://github.com/beamkeerati/study_tron1) |
| <a id="p-openarm-mobile-manipulation-lab"></a>**OpenArm Mobile Manipulation Lab**: 2일 MuJoCo·ROS 2 실습: OpenArm을 이족 또는 휠 하체에 결합해 자연어 미션으로 구동 | `TRON1`&nbsp;*sim* | [aha645](https://github.com/aha645) | 2026 | 코드 | [코드](https://github.com/aha645/openarms_llm_ex) |
| <a id="p-limx-tron1-learning"></a>**LimX Tron1 Learning**: Isaac Lab 학습 과정을 단계별로 설명하는 인터랙티브 가이드 | `TRON1`&nbsp;*sim* | [jessiezhg](https://huggingface.co/jessiezhg) | 2026 | 튜토리얼 | [튜토리얼](https://huggingface.co/spaces/jessiezhg/LimX-Tron1-Learning) |
| <a id="p-zetin-robocup-2026"></a>**Zetin RoboCup 2026**: Isaac Lab에서 솔풋 TRON1 축구 로봇의 보행, 공 추적, 슈팅 학습 (한국어) | `TRON1`&nbsp;*sim* | [tae2yi](https://github.com/tae2yi) | 2026 | 코드 | [코드](https://github.com/tae2yi/Zetin_Robocup2026) |
| <a id="p-conducting-evaluation-with-oli"></a>**Conducting Evaluation System**: 음악 교육용 지휘 동작 시연 및 평가 시스템, Oli 디지털 트윈에서 시연 | `Oli`&nbsp;*sim* | 광둥페이정학원 | 2026 | 논문 | [논문](https://doi.org/10.1145/3806980.3807204) |
| <a id="p-every-embodied-troncamp-mani"></a>**Every Embodied: TRONCamp Mani**: Datawhale 임바디드 AI 오픈 강좌, TRON2 양팔 과제를 다루는 TRONCamp Mani 챕터 수록 (중국어) | `TRON2`&nbsp;*sim* | [Datawhale](https://github.com/datawhalechina) | 2026 | 코드 | [코드](https://github.com/datawhalechina/every-embodied/tree/main/15-Challenge%E7%AB%9E%E8%B5%9B/TRONCamp-Mani) |
| <a id="p-atec2026-logic-tars"></a>**ATEC 2026 Wheel-Legged Entry**: ATEC 2026 챌린지 참가 팀의 강화학습 학습 및 시뮬레이션 배포 | `TRON1` `TRON2`&nbsp;*sim* | [Logic-TARS](https://github.com/Logic-TARS) | 2026 | 코드 | [코드](https://github.com/Logic-TARS/ATEC2026) |
| <a id="p-zetin-robocup-control"></a>**Zetin RoboCup Control**: RoboCup 2026 경기 운용 코드: TRON1 하체에 자체 제작 상체와 카메라 연결 | `TRON1` | [newb-ops (서울시립대 ZETIN)](https://github.com/newb-ops) | 2026 | 코드 | [코드](https://github.com/newb-ops/robocup-control-portfolio) |
| <a id="p-troncamp-mani-24zlha"></a>**TRONCamp Mani Solution 24ZlhA**: ACT와 하드 샘플 마이닝, 멀티 GPU 학습, 기술 보고서 포함. T4 온라인 점수 79/100 | `TRON2`&nbsp;*sim* | [upset666](https://github.com/upset666) | 2026 | 코드 | [코드](https://github.com/upset666/troncamp-mani-24ZlhA) |
| <a id="p-troncamp-mani-act-dp"></a>**TRONCamp Mani ACT + Diffusion Policy**: T1~T3은 ACT, 그릇 세 개 쌓기는 Diffusion Policy, 설계 문서 포함 (중국어) | `TRON2`&nbsp;*sim* | [irvingskr](https://github.com/irvingskr) | 2026 | 코드 | [코드](https://github.com/irvingskr/troncamp-mani) |
| <a id="p-troncamp-mani-sormaker"></a>**TRONCamp Mani Solution SORMaker**: 네 과제 공통 ACT 학습·배포 파이프라인, T3·T4 정책 실행 영상 포함 | `TRON2`&nbsp;*sim* | [SORMaker](https://github.com/SORMaker) | 2026 | 코드 | [코드](https://github.com/SORMaker/troncamp-mani) |
| <a id="p-hands-on-embodied-ai"></a>**Hands-on Embodied AI**: 알고리즘부터 실기까지의 공개 강좌, 실외 GNSS와 Nav2 내비게이션 포함 (중국어) | `TRON1` | [우한대학교 BRAIN Lab](https://github.com/Whu-BrainLab) | 2025 | 코드 | [코드](https://github.com/Whu-BrainLab/Embodied-AI-Tutorial)&nbsp;·&nbsp;[튜토리얼 (zh)](https://mp.weixin.qq.com/s/YLKVi09hgImSuWUr_S6gJA) |
| <a id="p-canton-tower-robot-climbing-challenge"></a>**광저우타워 로봇 등반 챌린지**: Oli가 FastStair 방법으로 계단 오르기 우승과 최우수 정밀 제어상 수상 | `Oli` | LimX | 2025 | 논문 | [논문](https://arxiv.org/abs/2601.10365)&nbsp;·&nbsp;[결과 (zh)](https://www.sfccn.com/2026/1-1/5NMDE0NzNfMjA5MzM5NA.html) |
| <a id="p-rl-bipedal-locomotion"></a>**RL Bipedal Locomotion**: 남방과기대 ACR2025 수업 과제: Isaac Lab 학습·재생·배포 | `TRON1`&nbsp;*sim* | [81578823 (SUSTech)](https://github.com/81578823) | 2025 | 코드 | [코드](https://github.com/81578823/RL_bipedal_locomotion_Isaaclab) |
| <a id="p-pointfootgym"></a>**pointfootGym**: 남방과기대 CLEAR Lab의 포인트풋 학습 템플릿, Isaac Gym과 legged_gym 기반 | `TRON1`&nbsp;*sim* | [Haokai Su (SUSTech CLEAR Lab)](https://github.com/SuDaxia-kai) | 2024 | 코드 | [코드](https://github.com/SuDaxia-kai/pointfootGym) |

## 산업 적용

_34개 (6개 그룹)_

이 섹션은 LimX가 관리합니다. 공개 보도, 파트너 발표, 기업 오픈소스를 수록하며 각 항목에 출처 링크가 있습니다.

### 적용 사례 및 제품

| 프로젝트 | 기종 | 저자 / 기관 | 연도 | 유형 | 링크 |
|---|---|---|---|---|---|
| <a id="p-tenniix-ultra-max"></a>**TENNIIX ULTRA MAX**: TRON2 휠-레그를 기반으로 한 테니스 로봇, 2026 빌리 진 킹 컵 파이널에서 프로 선수와 대결 | `TRON2` | Enhanced Robotics (Tenniix) | 2026 | 보도 | [보도 (zh)](https://www.news.cn/sports/20260928/f1776d7ca75042568a5137e256fa9425/c.html) |
| <a id="p-zinova-tron2-construction"></a>**ZINOVA Tool Intelligence**: TRON2 두 대가 네일건과 철근으로 축소판 틸트업 공정을 시연 | `TRON2` | ZINOVA, RIC Robotics | 2026 | 보도 | [영상](https://www.youtube.com/watch?v=8KDxnT-4zl0)&nbsp;·&nbsp;[보도](https://www.equipmentworld.com/technology/article/15836367/zinova-limx-bring-toolwielding-robots-to-construction) |
| <a id="p-dongtu-domestic-architecture"></a>**국산 전자 아키텍처 휴머노이드**: 둥투커지 Intewell OS와 AUTBUS를 탑재한 Oli, LimX는 둥투커지 주도 아키텍처 연맹에도 참여 | `Oli` | 둥투커지(Kyland) | 2026 | 보도 | [보도 (zh, WeChat)](http://mp.weixin.qq.com/s?__biz=Mzk0NDU5NjMwMA==&mid=2247495106&idx=1&sn=8b5ffd05d0615a0581d3b23a18f2d830&chksm=c20243eecd5be209a820feecab39fcb0480f5ec903b40f0d655db8f6225b378bd0e8f1db3a1a)&nbsp;·&nbsp;[보도 (zh, 21세기경제보도)](https://m.21jingji.com/article/20260929/herald/af2d0b02d6e7593ed4a2af7d05a191b5.html)&nbsp;·&nbsp;[보도 (zh, 쓰촨온라인)](https://cbgc.scol.com.cn/news/8010385) |
| <a id="p-wuji-hand-2-pharmacy-demo"></a>**Wuji Hand 2 Pharmacy Demo**: WUJI TECH Wuji Hand 2를 단 TRON2가 한약재를 집고, 달고, 갈고, 포장 | `TRON2` | WUJI TECH | 2026 | 보도 | [보도 (ja)](https://robotstart.info/article/2026/08/26/382326.html) |
| <a id="p-d-robotics-rdk-s100-tron1"></a>**RDK S100 on TRON1**: 포인트풋 보행 정책을 D-Robotics RDK S100 BPU로 이식, 공식 응용 사례 | `TRON1` | D-Robotics | 2025 | 보도 | [보도 (zh)](https://forum.d-robotics.cc/t/topic/28833) |

### 기업 오픈소스

| 프로젝트 | 기종 | 저자 / 기관 | 연도 | 유형 | 링크 |
|---|---|---|---|---|---|
| <a id="p-xense-openpi-for-tron2"></a>**Xense OpenPI**: 양팔 조작용 Pi0.5 학습 설정과 실시간 추론 | `TRON2` | [Xense Robotics](https://github.com/XenseRobotics-AI) | 2026 | 코드 | [코드](https://github.com/XenseRobotics-AI/xense-openpi) |
| <a id="p-crest-tron2-description"></a>**TRON2 Description, Crest edition**: SFYG 팔 손목 카메라 마운트에 맞춰 조정한 로봇 모델 | `TRON2` | [Crest Robotics](https://github.com/Crest-Robotics) | 2026 | 코드 | [코드](https://github.com/Crest-Robotics/tron2-robot-description) |
| <a id="p-artefacts-tron1-nav2-newton"></a>**TRON1 Nav2 in Newton**: Newton 물리 시뮬레이터에서 Nav2 경로 추종 테스트 | `TRON1`&nbsp;*sim* | [Artefacts](https://github.com/art-e-fact) | 2026 | 코드 | [코드](https://github.com/art-e-fact/tron-navigation-demo) |
| <a id="p-xense-pico4-teleoperator"></a>**LeRobot Pico4 Teleoperator**: LeRobot용 PICO 4 양팔 원격 조작 플러그인, TRON2 지원 | `TRON2` | [Xense Robotics](https://github.com/XenseRobotics-AI) | 2026 | 코드 | [코드](https://github.com/XenseRobotics-AI/lerobot-teleoperator-pico4) |
| <a id="p-safesentinel-sonic-for-oli"></a>**SONIC Training for Oli**: 31자유도 모델에서 GEAR-SONIC 전신 제어 학습, PICO VR 원격 조작 지원 | `Oli`&nbsp;*sim* | [SafeSentinel](https://github.com/safe-sentinel-co) | 2026 | 코드 | [코드](https://github.com/safe-sentinel-co/hu_d04_sonic_setup) |
| <a id="p-anima-ros2-sim-net"></a>**ANIMA ROS 2 Simulation Network**: TRON1 이족 모델을 포함한 ROS 2·Gazebo 시뮬레이션 스택 | `TRON1`&nbsp;*sim* | [RobotFlow Labs](https://github.com/RobotFlow-Labs) | 2026 | 코드 | [코드](https://github.com/RobotFlow-Labs/anima-ros2-sim-net) |
| <a id="p-artefacts-tron1-workspace"></a>**TRON1 Artefacts Workspace**: Artefacts 로봇 테스트 플랫폼 기반 ROS 2·Gazebo 데모 | `TRON1`&nbsp;*sim* | [Artefacts](https://github.com/art-e-fact) | 2026 | 코드 | [코드](https://github.com/art-e-fact/tron1-artefacts) |
| <a id="p-openmind-om1-sim"></a>**OM1-sim**: 로봇 OS OM1용 Isaac Sim 환경, 휠풋 TRON1·Go2·G1 지원 | `TRON1`&nbsp;*sim* | [OpenMind](https://github.com/OpenMind) | 2026 | 코드 | [코드](https://github.com/OpenMind/OM1-sim) |
| <a id="p-phanthy-motus-driver"></a>**Phanthy Motus Drivers**: 4Paradigm 임바디드 AI 플랫폼 Phanthy Motus의 하드웨어 드라이버, TRON2 양팔 지원 | `TRON2` | [4Paradigm](https://github.com/4paradigm) | 2026 | 코드 | [코드](https://github.com/4paradigm/phanthymotus-driver) |
| <a id="p-xense-tron2-pnp-dataset"></a>**Xense TRON2 Pick-and-Place Dataset**: 촉각 영상 포함 원격 조작 115 에피소드, Voxel51이 FiftyOne 형식으로도 공개 | `TRON2` | [Xense Robotics](https://huggingface.co/Xense) | 2026 | 코드 | [데이터셋](https://huggingface.co/datasets/Xense/tron2rt-pnp-0918)&nbsp;·&nbsp;[데이터셋 (Voxel51)](https://huggingface.co/datasets/Voxel51/xense-tron2rt-pnp-115ep) |
| <a id="p-anima-ros2-bridge"></a>**ANIMA ROS 2 Bridge**: AI 에이전트와 ROS 2 로봇을 잇는 DDS / WebSocket 브리지, LimX 로봇을 자동 인식하고 TRON1 모델 포함 | `TRON1`&nbsp;*sim* | [RobotFlow Labs](https://github.com/RobotFlow-Labs) | 2026 | 코드 | [코드](https://github.com/RobotFlow-Labs/anima-ros2-bridge) |
| <a id="p-cmriat-citadel"></a>**Citadel**: HDF5 기록을 LeRobot v2.1로 일괄 변환하는 로봇 데이터 관리 도구, 예시로 TRON2 데이터 사용 | `TRON2` | [China Merchants Research Institute of Advanced Technology](https://github.com/cmriat) | 2026 | 코드 | [코드](https://github.com/cmriat/Citadel) |
| <a id="p-openmind-brainpack"></a>**OpenMind BrainPack**: TRON1, Unitree G1, Go2에 통합되는 모듈형 컴퓨팅·개발 백팩 | `TRON1` | [OpenMind](https://github.com/OpenMind) | 2025 | 코드 | [코드](https://github.com/OpenMind/brainpack) |

### 상업 공연 및 이벤트

| 프로젝트 | 기종 | 저자 / 기관 | 연도 | 유형 | 링크 |
|---|---|---|---|---|---|
| <a id="p-nio-gba-auto-show"></a>**광둥·홍콩·마카오 모터쇼 NIO 부스**: NIO 부스에서 Oli와 Luna가 인터랙티브 시연 | `Oli` `Luna` | NIO | 2026 | 보도 | [보도 (zh)](https://news.ifeng.com/c/8vmGa3sP4u7) |
| <a id="p-kill-it-finale"></a>**〈킬잇: 스타일 크리에이터 대전쟁〉 결승**: 디자이너 김나라의 우승 결승 무대에 Luna 출연, tvN | `Luna` | tvN, 김나라 | 2026 | 보도 | [보도](https://isplus.com/article/view/isp202607290025) |
| <a id="p-taobao-influencer-festival"></a>**타오바오 인플루언서 페스티벌**: 상하이에서 배우 천이한과 Luna가 런웨이 워킹 | `Luna` | 타오바오 | 2026 | 보도 | [보도](https://interestingengineering.com/ai-robotics/video-china-humanoid-catwalk-taobao-festival) |
| <a id="p-luna-china-gt-opening"></a>**2026 CHINA GT opening ceremony**: Luna 5대가 CHINA GT 모터스포츠 대회 개막식에서 자율 군무 공연 | `Luna` | CHINA GT | 2026 | 보도 | [보도 (ja)](https://robotstart.info/article/2026/09/18/382434.html) |

### 전략적 제휴

| 프로젝트 | 기종 | 저자 / 기관 | 연도 | 유형 | 링크 |
|---|---|---|---|---|---|
| <a id="p-smartcube-partnership"></a>**스마트큐브**: 한국 공식 파트너, 공장·에너지 현장 점검에 휴머노이드와 디지털 트윈 활용 | — | 스마트큐브 | 2026 | 보도 | [보도](https://www.aipostkorea.com/news/articleView.html?idxno=12727) |
| <a id="p-guangyang-partnership"></a>**광양구펀**: 일체형 관절 모듈 공동 개발, 베어링·기어·감속기·드라이버 포함 (공급망 협력) | — | 광양구펀 | 2026 | 보도 | [보도 (zh, NBD)](https://www.nbd.com.cn/articles/2026-03-09/4285402.html)&nbsp;·&nbsp;[보도 (zh, 둥팡차이푸)](https://finance.eastmoney.com/a/202603093666208673.html) |
| <a id="p-nbpu-industry-college"></a>**Ningbo Polytechnic University**: 체화 AI 공동 산업대학, Oli를 핵심 교육 플랫폼으로 채택 | `Oli` | 닝보직업기술대학 | 2026 | 보도 | [보도 (zh)](https://www.nbpu.edu.cn/2026/0612/c2654a6462855/page.htm) |
| <a id="p-saic-beijing-joint-lab"></a>**상하이자동차 베이징 공동 연구소**: 자동차 제조를 위한 임바디드 AI 공동 연구소, LimX는 SAIC의 첫 임바디드 AI 전략 파트너 | — | SAIC 베이징 | 2025 | 보도 | [보도 (zh)](https://www.pingwest.com/a/306356) |

### 지역 파트너 및 판매 채널

| 프로젝트 | 기종 | 저자 / 기관 | 연도 | 유형 | 링크 |
|---|---|---|---|---|---|
| <a id="p-knoxlabs-data-collection"></a>**Knoxlabs**: 미국에서 TRON2·Oli 번들 판매, 데이터 수집용 원격 조작 설정 제공 | `TRON2` `Oli` | Knoxlabs | 2026 | 보도 | [보도](https://www.knoxlabs.com/blogs/articles/robot-teleoperation-data-collection-limx) |
| <a id="p-tron-kk-humanoid-si"></a>**TRON K.K.**: 일본에서 휴머노이드 시스템 통합과 Omniverse 시뮬레이션 제공, LimX 로봇 취급 | — | TRON K.K.(일본) | 2026 | 보도 | [보도 (ja)](https://tron.tokyo/en/service/limx-dynamics/) |
| <a id="p-robot-bank-japan"></a>**Robot Bank**: TRON1, TRON2, Oli를 일본에 출시, 현장 도입 지원 | `TRON1` `TRON2` `Oli` | Robot Bank(일본) | 2026 | 보도 | [보도 (ja)](https://robotstart.info/article/2026/05/15/381891.html) |
| <a id="p-mybotshop-germany"></a>**MYBOTSHOP**: 독일에서 P1 판매·지원, 매뉴얼, ROS 2 설정 가이드, 수리 서비스 제공 | `P1` | MYBOTSHOP GmbH (독일) | 2026 | 보도 | [보도](https://www.docs.mybotshop.de/limx_p1.html) |
| <a id="p-synerex-korea"></a>**씨너렉스**: 한국 공식 파트너, 드론쇼코리아 2025에서 TRON1 국내 첫 공개 | `TRON1` | 씨너렉스 | 2025 | 보도 | [보도](https://www.newswire.co.kr/newsRead.php?no=1005949) |
| <a id="p-r2c2-partnership"></a>**R2C2**: 홍콩 공식 개발사 겸 유통사, 강화학습 로봇을 유틸리티·점검 업무에 활용 | `W1` `P1` | R2C2 Limited(홍콩) | 2024 | 보도 | [발표 (LinkedIn)](https://www.linkedin.com/posts/limx-dynamics_robotics-partnership-innovation-activity-7211709457666310145-ddt9)&nbsp;·&nbsp;[발표 (X)](https://x.com/LimX_Dynamics/status/1806002749722820865) |

### 수상 및 인정

| 프로젝트 | 기종 | 저자 / 기관 | 연도 | 유형 | 링크 |
|---|---|---|---|---|---|
| <a id="p-ieee-spectrum-robot-of-the-month-tron1"></a>**IEEE Spectrum Robot of the Month**: TRON1이 IEEE Spectrum 잡지 '이달의 로봇'에 소개 | `TRON1` | IEEE Spectrum | 2026 | 보도 | [보도](https://doi.org/10.1109/MSPEC.2026.11595926) |
| <a id="p-rbr50-2025-tron1"></a>**RBR50 로보틱스 혁신상 2025**: TRON1이 멀티모달 이족 R&D 플랫폼으로 선정 | `TRON1` | The Robot Report | 2025 | 보도 | [결과](https://www.therobotreport.com/rbr50-company-2025/tron-1-multi-modal-biped-offers-a-unique-rd-platform/) |

## 기종별

기종마다 전용 페이지가 있으며, 해당 기종을 사용한 항목을 모두 모았습니다: [TRON1](robots/TRON1_ko.md) · [TRON2](robots/TRON2_ko.md) · [Oli](robots/Oli_ko.md) · [Luna](robots/Luna_ko.md) · [P1](robots/P1_ko.md) · [W1](robots/W1_ko.md)

기종별·분류별 수록 개수:

| 기종 | 합계 | 보행 | 인지 | 매니퓰레이션 | 임바디드 AI | 도구 | 교육 | 산업 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| [`TRON1`](robots/TRON1_ko.md) | **90** | 32 | 12 | 6 | 1 | 18 | 10 | 11 |
| [`TRON2`](robots/TRON2_ko.md) | **34** | 1 |  | 3 | 6 | 5 | 8 | 11 |
| [`Oli`](robots/Oli_ko.md) | **27** | 13 |  | 2 | 2 | 2 | 2 | 6 |
| [`Luna`](robots/Luna_ko.md) | **7** | 2 | 1 |  |  |  |  | 4 |
| [`P1`](robots/P1_ko.md) | **5** | 3 |  |  |  |  |  | 2 |
| [`W1`](robots/W1_ko.md) | **4** | 2 |  | 1 |  |  |  | 1 |

## 기여하기

자기 추천과 타인 추천 모두 환영합니다. [제출 양식](https://github.com/limxdynamics/awesome-limx/issues/new?template=add-project.yml), Pull Request, 또는 이메일 [opensource@limxdynamics.com](mailto:opensource@limxdynamics.com)으로 보내 주세요. 영어, 중국어, 일본어, 한국어 모두 괜찮습니다. 수록 기준은 [CONTRIBUTING.md](CONTRIBUTING.md)를 참고하세요. 각 분류는 연도 기준 최신순으로 정렬되어 있습니다. '유형' 열은 독자가 얻을 수 있는 것을 나타냅니다: 바로 실행할 수 있는 것(**코드**), 따라 배울 수 있는 것(**튜토리얼**), 읽을 수 있는 것(**논문**), 언론 보도나 발표(**보도**).

수록은 LimX의 보증을 의미하지 않으며 모든 권리는 원저작자에게 있습니다. 소유자는 이유와 관계없이 언제든 삭제를 요청할 수 있습니다.

제휴 및 구매 문의는 [opensource@limxdynamics.com](mailto:opensource@limxdynamics.com)으로 연락해 주세요.


## 라이선스

이 목록은 [CC0 1.0](LICENSE)으로 공개됩니다. 링크된 프로젝트에는 각자의 라이선스가 적용됩니다.
