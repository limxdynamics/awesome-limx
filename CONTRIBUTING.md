# Contributing

[中文](CONTRIBUTING_cn.md)

Thanks for sharing your work. This list is useful only if every entry points to something real that people can check.

## How to submit

Pick whichever is easiest:

- Fill in the [submission form](https://github.com/limxdynamics/awesome-limx/issues/new?template=add-project.yml).
- Open a pull request that adds your entry to `README.md` and `README_cn.md`. If you only write one language, we will translate the rest, including the Japanese and Korean editions.
- Email [opensource@limxdynamics.com](mailto:opensource@limxdynamics.com) with the same details the form asks for.

If you are the author or maintainer, say so. It makes review much faster.

## Checks

CI runs on every pull request. It fails only on things that break the page:

- an anchor changed without the link that points at it
- a blank line inside a table, which ends it: every row below renders as text
- a row with a different number of cells than its header
- an entry added to one language edition and not the other

Keep a table's rows on consecutive lines. A blank line looks like spacing, but
GitHub reads it as the end of the table.

The count lines, the section counts in Contents, the By robot table and the Type column are checked too, but
they only warn. The layout of this file will keep changing, and a check that
cannot read the new shape steps aside instead of blocking a contribution.

Push your branch without waiting for CI:

```bash
python scripts/check_list.py
```

Nothing to install, Python 3.9 or newer is enough.

The pages under `robots/` list the entries for one robot each. They are generated from the README files, so do not edit them by hand. CI rebuilds them whenever the README changes on `main`, so you do not need to run anything.

The [gallery](https://limxdynamics.github.io/awesome-limx/) (`docs/index.html`) is generated the same way, by `scripts/build_gallery.py`. See [Gallery, videos and thumbnails](#gallery-videos-and-thumbnails).

## Entry format

Each section is a table. Add one row per project:

```markdown
| **Short name**: what was done, in a few words | `TRON1` | [Author or lab](https://github.com/you) | 2025 | Code | [project](…)&nbsp;·&nbsp;[paper](…)&nbsp;·&nbsp;[code](…) |
```

- **Project**: a short name in bold, then a plain phrase saying what was done. No full sentences.
- **Robot**: TRON1, TRON2, Oli, Luna, an earlier LimX robot such as P1, or LimX SDK, in backticks. List more than one if the work used several. Add `&nbsp;*sim*` after the robots when public sources show the work only in simulation, sim-to-sim included. No mark means it ran on a real robot. Tools are not marked.
- **Author / Org**: your GitHub or Hugging Face handle, linked to your profile, or your lab or institution. For papers with several institutions, name the first two or three and add "et al.", without a link.
- **Year**: the year the work was published or shown, in its own column.
- **Links**: include only the kinds that exist, in this order: project, paper, code, video, model, dataset, tutorial, news, result. Use `news` for press coverage of a deployment and `result` for an official competition result. Separate them with `&nbsp;·&nbsp;` so the links stay on one line.
- **Order**: by year, newest first, within each section. Entries from the same year are not in a particular order.
- **Type**: `Code`, `Tutorial`, `Paper` or `News`, decided by the maintainers. See [Type](#type). Leave it out when you submit.

A section appears in the README once it has its first entry.

## Type

The Type column answers one question: what can a reader do with this?

| Type | What a reader gets |
|---|---|
| **Code** | Something to clone or download: a repository, a model, a dataset |
| **Tutorial** | Something to follow: a tutorial, a course, a Hugging Face Space |
| **Paper** | Something to read: a paper, a project page, a write-up |
| **News** | Only a report: a media article, a company or partner announcement, an award or competition result |

Decide in this order:

1. Links a repository, a model or a dataset: `Code`
2. Links a tutorial or a Space: `Tutorial`
3. Links a paper, a project page or a write-up: `Paper`
4. Links only reports (news, announcement, result, video): `News`

A project with both a paper and a repository is `Code`, because the reader still
gets something to run. A repository that only holds setup notes is `Code` too.

`Paper` does not mean only papers. A write-up or a project page belongs here as
well: there is nothing to run. Industry entries are usually `News`: a
partnership, a show or an award is known from reports, not from a paper.

## Which section

| Section | Put it here if the main result is about |
|---|---|
| Locomotion & whole-body control | walking, running, jumping, terrain, motion tracking, whole-body control |
| Perception & navigation | mapping, localization, planning, obstacle avoidance, autonomous navigation |
| Manipulation | grasping, mobile manipulation, teleoperation, arm control |
| Embodied AI | VLA models, LLM agents, imitation learning, foundation models |
| Tools, simulation & SDK | simulators, robot models, deployment tooling, libraries on the LimX SDK |
| Education & competitions | courses, teaching labs, student teams, competition results |
| Industry deployments | company products, real-world deployments, commercial shows and events, strategic partnerships, regional partners and channels, awards |

If a project fits more than one section, choose the one that best describes its main result. Each project appears once.

## What we accept

| Rule | Why |
|---|---|
| The work used LimX hardware or software, on a real robot or in simulation with official LimX models | That is what this list shows. "Might be compatible" does not count. |
| A public source says so: the paper names the robot, the video shows it, or the README states it | Anyone reading the list should be able to check the claim. |
| There is a public link to the original source | We link to where the work lives. We do not host it. |
| Company projects only with the company's agreement, or once the company has announced the work or the partnership itself | We do not announce someone else's business relationship before they do. |
| Links only: no copied code, papers, videos, screenshots or logos | Those belong to their owners. |

Work by LimX researchers, such as papers and competition results, is welcome on the same terms as anyone else's.

We do not accept:

- LimX's own open-source releases, such as repositories under [limxdynamics](https://github.com/limxdynamics) or official models on [Hugging Face](https://huggingface.co/limxdynamics). Those are listed there.
- Forks of LimX repositories with no changes of your own.
- Work that only mentions LimX in passing and did not use the hardware or software.
- Multi-robot work where the LimX robot is only one bundled asset: a model file in a collection, or one name in a list of supported robots with nothing to run. A LimX robot must be one of the main subjects, or come with a complete, runnable setup (training config, controller or deployment).
- Reposts of LimX's product videos or marketing material.
- Official code or model files re-uploaded as a new repository rather than forked, with nothing added of your own. A URDF collection, or a copy of a training project, is LimX's work, not a community contribution.

Changes on top of official assets do count: a different controller, a new sensor or gripper, a calibration, a retargeting. The line is whether anything was added, not whether official files are inside.

## Company projects

If you submit a product or a company deployment, confirm in the form, pull request or email that the company agrees to be listed. If the company or both partners have already announced the work publicly, link that announcement or the press coverage instead. Public strategic agreements, official regional partners and sales channels, and industry awards count too: they go under Industry deployments. If the company wants to announce first, tell us and we will wait.

## Gallery, videos and thumbnails

The [gallery](https://limxdynamics.github.io/awesome-limx/) shows each entry as a card. What goes on the card, in this order:

1. A thumbnail under `docs/thumbs/<id>.webp` (the id is the entry's anchor, without `p-`): a small 640×360 still taken from a demo image or GIF in the project's own README, or one the owner sent us. `from` in `scripts/gallery.json` records where each still came from, and the card links back to the project. We take stills only of the project's own robot footage, never of people, press photos or diagrams.
2. Otherwise the entry's YouTube video: the card shows YouTube's own thumbnail and plays the video in YouTube's player. bilibili videos and `.mp4` files on the project's own site play in place too, streamed from where they are hosted.
3. Otherwise an illustration drawn in the page from the entry itself: the robot (and its variant, such as wheel-foot TRON1) in a scene picked from the description, such as stairs, a navigation path or a worktable. It is labelled "Illustration" so nobody takes it for footage. The rules are in `scripts/gallery_illustrations.js`; if a scene does not fit an entry, a real thumbnail or video fixes it, or the rules can be adjusted.

A video that is not in the entry's links can be added in `scripts/gallery.json` under `media`, and `featured` there picks the cards shown first, which we change from time to time. If you own a project and want its thumbnail or video changed or taken off the gallery, open an issue or email us and we will do it, no reason needed. Then run `python scripts/build_gallery.py`, or let CI do it after the merge. The README stays the source: the gallery never holds an entry the README does not.

The README itself stays text and links. If you want an image or a logo next to your entry in the README, ask explicitly and confirm that you hold the rights to it.

## Removal

Owners can ask for removal at any time, for any reason, without explanation. We will remove the entry and will not add it back unless you ask.

## House style

- `README.md` in English, `README_cn.md` in Chinese, `README_ja.md` in Japanese and `README_ko.md` in Korean, with the same entries in all four. Submissions can be in any of these languages; the maintainers keep the other editions in step.
- **Name**: a name people can read, in title case: the paper's short name (`FastStair`), the project's own name (`MetalSim`), or a plain description (`TRON1 Wheel GUI`). Not a repository path such as `tron1_wheel_gui`; the link shows that. A library known by its package name, such as `legged_gym`, keeps it.
- **Description**: what was done plus one detail that sets it apart, about 8 to 18 words, no full stop. Good: "replaces GR00T N1.7's diffusion action head with a one-step drifting head to cut inference cost". Too short: "one-step action heads". Too long: a sentence listing every component.
- Do not repeat the robot name in the description unless the variant matters (wheel-foot, sole-foot, dual-arm); the Robot column already says which robot.
- Mark a source in Chinese, Japanese or Korean with its language when it differs from the edition's, e.g. `[news (zh)]` in the English edition. English sources are not marked.
- When an entry has two links of the same kind, tell them apart in the brackets by robot, platform or outlet, e.g. `[code (TRON1)]` · `[code (TRON2)]` or `[news (zh, NBD)]`.
- A post from LimX or the partner itself is an `announcement`, not `news`.
- Say what was done on the robot, not how impressive it is.
- No emoji and no superlatives such as "first ever" or "state of the art".
