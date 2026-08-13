# RepoCover

[简体中文](README.zh-CN.md)

Create polished GitHub repository social previews from real project evidence.

RepoCover is a Codex skill that reads a repository's README, screenshots, logos, and design tokens; creates an editable SVG and an exact `1280×640` PNG; then validates the result at full size and at sharing-card size.

![RepoCover social preview](docs/social-preview.png)

## Why RepoCover

- **Repository-specific:** the design follows the project's actual product, palette, and visual language.
- **Evidence-first:** visible claims and product proof must come from repository evidence.
- **Editable:** every result includes a deterministic SVG source beside the PNG.
- **GitHub-ready:** PNG output is exactly `1280×640` and kept under GitHub's 1 MB limit.
- **Visually reviewed:** a generated `320×160` sheet checks readability on light and dark surroundings.
- **Safe by default:** creating an image never authorizes uploading it or changing repository settings.

## Quick start

Ask Codex:

```text
Use $skill-installer to install onovich/RepoCover from skill/repo-cover.
```

Restart Codex, open a repository, and ask:

```text
Use $repo-cover to create a social preview for this repository.
```

RepoCover normally writes:

```text
docs/social-preview.svg
docs/social-preview.png
```

It does not upload the image unless you explicitly request that separate action.

## Examples

| PrismDraft | LittlePNG |
| --- | --- |
| ![PrismDraft social preview](examples/prismdraft.png) | ![LittlePNG social preview](examples/littlepng.png) |

| DeskMochi | AudioTrim |
| --- | --- |
| ![DeskMochi social preview](examples/deskmochi.png) | ![AudioTrim social preview](examples/audiotrim.png) |

The four examples were produced from different repository types to test whether the skill preserves distinct product identities rather than applying one generic template.

## How it works

1. Inspect repository rules, product evidence, and existing visual assets.
2. Define one promise, supporting proof, and facts to exclude.
3. Choose a code-native SVG, screenshot hybrid, or illustration hybrid route.
4. Render an exact GitHub social-preview raster.
5. Validate dimensions, byte size, SVG accessibility, content relevance, clipping, and collisions.
6. Review the image at full size and at `320×160` on light and dark surroundings.

Detailed agent instructions live in [`skill/repo-cover/SKILL.md`](skill/repo-cover/SKILL.md).

## Development

Requirements:

- Python 3.10+
- Node.js 20+
- Sharp available when rendering SVG to PNG

Run the repository checks:

```text
python scripts/check.py
```

The check validates skill metadata, UTF-8 files, JavaScript and Python syntax, the four reference outputs, and the checked-in RepoCover social preview.

Project state and next-session guidance are in [`docs/PROJECT_STATUS.md`](docs/PROJECT_STATUS.md). Release gates are in [`docs/RELEASE_CHECKLIST.md`](docs/RELEASE_CHECKLIST.md).

## License

[MIT](LICENSE)

RepoCover is an independent open-source project and is not affiliated with or endorsed by GitHub, Inc. GitHub is a trademark of GitHub, Inc.
