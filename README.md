# RepoCover

[简体中文](README.zh-CN.md)

[Website](https://repo-cover.onovich.com/) · [Examples](https://repo-cover.onovich.com/examples/) · [GitHub Social Preview guide](https://repo-cover.onovich.com/github-social-preview-guide/)

## About

Many programmers are better at building projects than presenting them. I am one of them. As AI coding makes it easier to create more, giving people a clear reason to look twice may matter.

That is how RepoCover came to be. I made it in a day. It looked pretty good, so I started using it myself.

![RepoCover social preview](docs/social-preview.png)

## What RepoCover does

RepoCover is an open-source AI coding Skill that reads a repository before designing its GitHub Social Preview. It creates an editable SVG and an exact `1280×640` PNG under 1 MB.

- **Reads before it designs:** it looks at the README, code, interface, and project assets before deciding what the cover should show.
- **Chooses a visual approach that fits the project:** a working interface, an existing main visual, and a project with no suitable image each need a different treatment.
- **Improves useful source material:** recognizable screenshots, artwork, and brand elements can be kept, cleaned up, and recomposed instead of pasted into a fixed layout.
- **Still works without a suitable image:** when needed, it can derive a visual direction from what the project actually does rather than applying a template.
- **Works with local and remote repositories:** projects that can be previewed locally—especially web projects with an existing interface—usually provide the best source material.
- **Ready for GitHub Social Preview:** GitHub accepts PNG, JPG, or GIF files under 1 MB, recommends at least `640×320`, and identifies `1280×640` as the best display size. See [GitHub's Social Preview documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview).

## Quick start

Open your AI agent—Codex is recommended—and send these two messages in order:

```text
Install the Skill from https://github.com/onovich/RepoCover.
```

```text
Use $repo-cover to create a cover for the current project.
```

RepoCover writes:

```text
docs/social-preview.svg
docs/social-preview.png
```

Creating the files does not authorize README edits, uploads, or repository-setting changes. Ask for those separately when you want them.

## Examples

The [Research case study](https://repo-cover.onovich.com/examples/#research-case-title) shows how a working bilingual report site was simplified and recomposed without losing its identity.

[![Research social preview](examples/research.png)](https://repo-cover.onovich.com/examples/#research-case-title)

The same Skill produced the eight additional covers below. Each one follows its own project rather than a shared template.

| PrismDraft | LittlePNG |
| --- | --- |
| ![PrismDraft social preview](examples/prismdraft.png) | ![LittlePNG social preview](examples/littlepng.png) |

| DeskMochi | AudioTrim |
| --- | --- |
| ![DeskMochi social preview](examples/deskmochi.png) | ![AudioTrim social preview](examples/audiotrim.png) |

| Beat | JustGoal.skill |
| --- | --- |
| ![Beat social preview](examples/beat.png) | ![JustGoal.skill social preview](examples/justgoal-skill.png) |

| Knot | Ping |
| --- | --- |
| ![Knot social preview](examples/knot.png) | ![Ping social preview](examples/ping.png) |

## How it works

1. Read the repository and identify what the project does.
2. Check whether the available interface, artwork, or other project material is suitable for a small shared image.
3. Keep what already works, remove distracting details, and add only what the composition needs. If no useful image exists, derive a visual direction from the project itself.
4. Export an editable SVG and an exact `1280×640` PNG under 1 MB.
5. Check the result at full size and thumbnail size on light and dark backgrounds.

Detailed Skill instructions live in [`skill/repo-cover/`](skill/repo-cover/).

## Development

Requirements:

- Python 3.10+
- Node.js 20+
- Sharp available when rendering SVG to PNG

Run the repository checks:

```text
python scripts/check.py
```

Release notes and project checks are documented in [`docs/RELEASE_CHECKLIST.md`](docs/RELEASE_CHECKLIST.md).

## License

[MIT](LICENSE)

RepoCover is an independent open-source project and is not affiliated with or endorsed by GitHub, Inc. GitHub is a trademark of GitHub, Inc.
