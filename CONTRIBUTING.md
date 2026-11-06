# Contributing

[中文](CONTRIBUTING_cn.md)

Thanks for sharing your work. This list is useful only if every entry points to something real that people can check.

## How to submit

Pick whichever is easiest:

- Fill in the [submission form](https://github.com/limxdynamics/awesome-limx/issues/new?template=add-project.yml).
- Open a pull request that adds your entry to `README.md` and `README_cn.md`. If you only write one language, we will translate the other.
- Email [opensource@limxdynamics.com](mailto:opensource@limxdynamics.com) with the same details the form asks for.

If you are the author or maintainer, say so. It makes review much faster.

## Entry format

```markdown
- **[Project name](https://primary-link)** — What was done on LimX hardware, in one sentence.<br>
  <sub>Institution or authors · Product · Year · [Paper](…) · [Code](…) · [Video](…)</sub>
```

- **Primary link**: the project page if there is one, otherwise the paper, then the code, then the video.
- **Product**: TRON1, TRON2, Oli, Luna, or LimX SDK. List more than one if the work used several.
- **Year**: the year the work was published or shown.
- **Links**: include only the kinds that exist, in the order Paper, Code, Video, Result. Use `Result` for an official competition result.
- **Order**: newest first within each section.

## Which section

| Section | Put it here if the main result is about |
|---|---|
| Locomotion & whole-body control | walking, running, jumping, terrain, motion tracking, whole-body control |
| Perception & navigation | mapping, localization, planning, obstacle avoidance, autonomous navigation |
| Manipulation | grasping, mobile manipulation, teleoperation, arm control |
| Embodied AI | VLA models, LLM agents, imitation learning, foundation models |
| Tools, simulation & SDK | simulators, robot models, deployment tooling, libraries on the LimX SDK |
| Education & competitions | courses, teaching labs, student teams, competition results |
| Industry deployments | company products and real-world deployments |

If a project fits more than one section, choose the one that best describes its main result. Each project appears once.

## What we accept

| Rule | Why |
|---|---|
| The work used LimX hardware or software, on a real robot or in simulation with official LimX models | That is what this list shows. "Might be compatible" does not count. |
| A public source says so: the paper names the robot, the video shows it, or the README states it | Anyone reading the list should be able to check the claim. |
| There is a public link to the original source | We link to where the work lives. We do not host it. |
| Company projects only with the company's agreement | We do not announce someone else's business relationship before they do. |
| Links only: no copied code, papers, videos, screenshots or logos | Those belong to their owners. |

We do not accept:

- Forks of LimX repositories with no changes of your own.
- Work that only mentions LimX in passing and did not use the hardware or software.
- Reposts of LimX's own videos or marketing material.

## Company projects

If you submit a product or a company deployment, confirm in the form, pull request or email that the company agrees to be listed. If the company wants to announce first, tell us and we will wait.

## Screenshots and logos

An entry is a link plus one line of text. If you want an image or a logo next to your entry, ask explicitly and confirm that you hold the rights to it.

## Removal

Owners can ask for removal at any time, for any reason, without explanation. We will remove the entry and will not add it back unless you ask.

## House style

- `README.md` in English, `README_cn.md` in Chinese, with the same entries in both.
- One sentence per entry. Say what was done on the robot, not how impressive it is.
- No emoji and no superlatives such as "first ever" or "state of the art".
