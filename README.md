# RepoCover

[简体中文](README.zh-CN.md)

## About

I know many programmers are not good at packaging their repositories. I am the same: I like keeping my head down and building, until I ended up with more than 300 repositories that almost no one noticed. Now that vibe coding is everywhere, I have started to think that giving passers-by a reason to look twice might matter.

That is how RepoCover came to be. I made it in a day. It looked pretty good, so I started using it myself.

![RepoCover social preview](docs/social-preview.png)

## Why RepoCover

RepoCover is a Codex skill that lets AI understand a project before designing its repository cover. It works with local and remote projects. Previewable local projects—especially web projects with an existing interface—usually provide richer visual evidence and produce the strongest results.

- **Reads before it draws:** it checks the README, code, project rules, and visual assets before deciding what the cover should say and show.
- **Makes good source material better:** it keeps recognizable screenshots, artwork, and brand elements, while removing clutter and improving the crop and composition.
- **Still works without a hero image:** when no useful screenshot, logo, or illustration exists, it builds a visual direction from the project's real objects, actions, and results instead of applying a template.
- **Keeps the project recognizable:** the palette, subject, dimensionality, and visual language follow the repository rather than one shared house style.
- **Editable and GitHub Social Preview ready:** GitHub accepts PNG, JPG, or GIF files under 1 MB, recommends at least `640×320`, and identifies `1280×640` as the best-display size. RepoCover deliberately outputs an exact `1280×640` PNG under 1 MB and keeps an editable SVG source beside it. See [GitHub's official Social Preview documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview).
- **Safe by default:** image creation never authorizes README edits, uploads, or repository-setting changes.

## Quick start

Install from this repository:

```text
Use $skill-installer to install onovich/RepoCover from skill/repo-cover.
```

Restart Codex. Open a local repository or provide a remote repository URL, then ask:

```text
Use $repo-cover to understand this project and create a validated GitHub Social Preview.
```

If the project has a runnable local preview or an existing web interface, keep it available during generation. Real product evidence usually improves the result.

RepoCover normally writes:

```text
docs/social-preview.svg
docs/social-preview.png
```

By default, RepoCover only creates and validates the image files. It does not change a README, upload an image, or edit repository settings unless separately requested.

## Examples

These examples come from games, tools, libraries, and Codex skills. Their layouts and materials differ because the project—not a shared template—leads the design.

| PrismDraft | LittlePNG |
| --- | --- |
| ![PrismDraft social preview](examples/prismdraft.png) | ![LittlePNG social preview](examples/littlepng.png) |

| DeskMochi | AudioTrim |
| --- | --- |
| ![DeskMochi social preview](examples/deskmochi.png) | ![AudioTrim social preview](examples/audiotrim.png) |

| [Beat](https://github.com/onovich/Beat) · symbolic audio model | [JustGoal.skill](https://github.com/onovich/JustGoal.skill) · branching workflow |
| --- | --- |
| ![Beat social preview](examples/beat.png) | ![JustGoal.skill social preview](examples/justgoal-skill.png) |

| [Knot](https://github.com/onovich/Knot) · geometric relations | [Ping](https://github.com/onovich/Ping) · weak-source reconstruction |
| --- | --- |
| ![Knot social preview](examples/knot.png) | ![Ping social preview](examples/ping.png) |

## How it works

1. Read the README, code, repository rules, and available visual assets.
2. Work out what the project does, what makes it recognizable, and what the repository can honestly support.
3. Keep and recompose attractive source material; remove distracting UI or clutter. If no useful image exists, infer a visual direction from the project itself.
4. Choose a composition and visual treatment that fit this project instead of reusing one template.
5. Export an editable SVG and an exact `1280×640` PNG under 1 MB, then check both full-size and thumbnail readability on light and dark backgrounds.
6. Stop at the generated files unless the user separately asks for an upload or repository change.

Detailed agent instructions and conditionally loaded references live in [`skill/repo-cover/`](skill/repo-cover/).

## Development

Requirements:

- Python 3.10+
- Node.js 20+
- Sharp available when rendering SVG to PNG

Run the repository checks:

```text
python scripts/check.py
```

The check validates metadata, UTF-8 without BOM, source syntax, all portable example images, and the checked-in product preview. Project state and next-session guidance are in [`docs/PROJECT_STATUS.md`](docs/PROJECT_STATUS.md); release gates are in [`docs/RELEASE_CHECKLIST.md`](docs/RELEASE_CHECKLIST.md).

## License

[MIT](LICENSE)

RepoCover is an independent open-source project and is not affiliated with or endorsed by GitHub, Inc. GitHub is a trademark of GitHub, Inc.
