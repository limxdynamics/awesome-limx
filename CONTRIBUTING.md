# Contributing

Thanks for wanting to add something. This list stays useful only if every entry is a project someone can actually run.

## Adding an entry

1. Fork this repository and edit `README.md`, or open the [add-project issue](https://github.com/limxdynamics/awesome-limx/issues/new?template=add-project.yml).
2. Put the entry in the section that fits. One entry, one line plus a short italic attribution line.
3. Keep entries in the existing format:

```markdown
- [owner/repo](https://github.com/owner/repo) — one line on what it does.
  _By Team or Person (TRON1, limxsdk)_
```

4. Open a pull request. If you are the maintainer, say so — it makes review much faster.

## What gets accepted

| Rule | Why |
|---|---|
| Runs on LimX hardware or `limxsdk` | This is the whole point of the list. "Might be compatible" does not count. |
| Public repository with a README that explains the project | A link to an empty repo helps nobody. |
| Not abandoned (commits within roughly 18 months, or a clear statement that it is finished and stable) | Dead entries are worse than missing ones. |
| Link only — no copied code, no mirrors, no forks of LimX repositories | We do not redistribute other people's code. |
| Existing LimX licence terms respected | If a project ships LimX binaries, check what the upstream licence allows. |

We do **not** accept:

- Forks of LimX repositories with no changes of your own.
- Commercial projects listed without the maintainer's agreement (see below).
- Anything that mostly resells or rebrands LimX hardware without adding engineering work.

## Commercial and product projects

If the project is a product or a company integration, we ask the maintainer before listing it. This is not about permission to link — it is about not announcing someone else's commercial relationship before they do.

If you are submitting on behalf of a company, please confirm in the issue or PR that you are allowed to make the association public.

## Screenshots and logos

By default an entry is a link plus one line of text. If you also want a screenshot or a company logo in the README, say so explicitly — those are covered by copyright and trademark, unlike a plain link.

## Removal

Any maintainer can ask for removal at any time, for any reason, without explanation. We will remove the entry and will not re-add it unless you ask us to.

## House style

- English entries, even for projects with Chinese documentation.
- One sentence per entry. Describe what it does, not how impressive it is.
- No emoji, no superlatives ("blazing fast", "revolutionary").
- Keep sections alphabetical once there are more than a handful of entries.
