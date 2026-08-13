# RepoCover

[简体中文](README.zh-CN.md)

Audit local or remote repositories, then create evidence-bound GitHub social previews that preserve each project's identity.

RepoCover is a Codex skill for both single repositories and portfolios. It can screen empty or extremely incomplete projects before bulk generation, inspect a repository without cloning when authenticated remote evidence is available, diagnose and recompose useful screenshots or artwork, and derive an honest visual system when no usable primary image exists. Every accepted cover includes an editable SVG and an exact `1280×640` PNG.

![RepoCover social preview](docs/social-preview.png)

## Why RepoCover

- **Portfolio-aware:** inventory repositories, explain them in plain language, and separate cover-worthy work from boilerplate or abandoned starts before generating at scale.
- **Remote-capable:** inspect public or authenticated private repositories without cloning and label static evidence honestly.
- **Evidence-first:** visible claims, product states, metrics, and relationships must be supported by repository evidence.
- **Source-sensitive:** preserve attractive native subjects and materials, remove noise, repair composition, and supplement only what the repository proves.
- **Cold-start capable:** when no usable screenshot, logo, or hero asset exists, derive the design from real objects, actions, topology, and outcomes rather than a stock motif.
- **Non-regressing:** preserve older covers, create versioned candidates, and promote only after full-size and thumbnail comparison.
- **Editable and GitHub Social Preview ready:** GitHub accepts PNG, JPG, or GIF files under 1 MB, recommends at least `640×320`, and identifies `1280×640` as the best-display size. RepoCover deliberately outputs an exact `1280×640` PNG under 1 MB and keeps an editable, deterministic SVG beside it. See [GitHub's official Social Preview documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview).
- **Safe by default:** image creation never authorizes README edits, uploads, or repository-setting changes.

## Where you can use a cover

- **GitHub Social Preview:** for a public repository, open `Settings`, find `Social preview`, then choose `Edit` and `Upload an image...`. When the repository URL is shared to a social platform or website that supports link previews, the service can automatically use the image as the repository cover. GitHub notes that these images can only be shared from public repositories.
- **README and documentation:** use it as a banner at the top of a README, a documentation home page, or an examples index.
- **Social posts and release announcements:** reuse it for a project launch, version update, devlog, or community post.
- **Portfolios and promotion:** place it on a personal site, project card, article, presentation, or other promotional material.

Saving the file in a repository does not automatically configure GitHub Social Preview. Uploading it, editing a README, and publishing it elsewhere remain separate actions that require separate authorization.

## Why I built RepoCover

I know many programmers are not good at packaging their repositories. I am one of them: I like keeping my head down and doing the work, and I eventually ended up with more than 300 repositories that almost no one noticed. In an age when vibe coding is everywhere, I came to see how important it is to make a passerby stop for one more look.

So I tried asking AI to read the code first, understand the project, and generate a Social Preview from that understanding. The result was surprisingly good. After refining the process a little, I decided to share it.

RepoCover's prompts, workflow, and visual rules are meant to be adapted. You can change the prompt, `SKILL.md`, or reference rules to explore a wider range of styles, as long as the result remains grounded in the project's facts, identity, and readability.

## Quick start

Install from this repository:

```text
Use $skill-installer to install onovich/RepoCover from skill/repo-cover.
```

Restart Codex, then choose the request that matches your task.

For one local repository:

```text
Use $repo-cover to create and validate a social preview for this repository.
```

For a remote repository without cloning:

```text
Use $repo-cover to inspect this GitHub repository without cloning, then create a social preview from the available remote evidence.
```

For a portfolio:

```text
Use $repo-cover to inventory these repositories, explain and screen them for cover-worthiness, wait for my selection, then generate versioned previews.
```

RepoCover normally writes:

```text
docs/social-preview.svg
docs/social-preview.png
```

When refreshing an existing cover, it creates versioned siblings and keeps the previous preferred version until comparison justifies promotion. It does not change a README or upload an image unless separately requested.

## Examples

The original portable examples cover four materially different repository types:

| PrismDraft | LittlePNG |
| --- | --- |
| ![PrismDraft social preview](examples/prismdraft.png) | ![LittlePNG social preview](examples/littlepng.png) |

| DeskMochi | AudioTrim |
| --- | --- |
| ![DeskMochi social preview](examples/deskmochi.png) | ![AudioTrim social preview](examples/audiotrim.png) |

Four later public regression examples exercise the failure modes learned during portfolio testing:

| [Beat](https://github.com/onovich/Beat) · symbolic audio model | [JustGoal.skill](https://github.com/onovich/JustGoal.skill) · branching workflow |
| --- | --- |
| ![Beat social preview](examples/beat.png) | ![JustGoal.skill social preview](examples/justgoal-skill.png) |

| [Knot](https://github.com/onovich/Knot) · geometric relations | [Ping](https://github.com/onovich/Ping) · weak-source reconstruction |
| --- | --- |
| ![Knot social preview](examples/knot.png) | ![Ping social preview](examples/ping.png) |

These examples intentionally use different materials, abstraction levels, topologies, and composition grammars. They are validation artifacts, not templates to copy.

## How it works

1. Inspect repository rules, authored content, source paths, visual assets, and the available evidence boundary.
2. For portfolios, explain and classify repositories before mass generation.
3. Record one promise, supporting proof, and facts to exclude in a design ledger.
4. Diagnose source material or build a cold-start semantic skeleton.
5. Choose a code-native SVG, source hybrid, or illustration hybrid and compare viable directions before rendering.
6. Preserve existing covers as versioned siblings and record topology, material, asset roles, line semantics, and fragment boundaries.
7. Validate dimensions, byte size, SVG accessibility, full-size composition, and exact `320×160` previews on light and dark surroundings.
8. Upload only after a separate explicit request, then verify the public `og:image`.

Detailed agent instructions and conditionally loaded references live in [`skill/repo-cover/`](skill/repo-cover/).

## Validation evidence

The repository contains eight portable public example PNGs plus the RepoCover product preview. In addition, the project owner completed a versioned regression across 63 accessible public and private repositories spanning games, web projects, developer tools, libraries, utilities, and skills. On 2026-08-14, the latest selected cover for every repository in that owner-run set was accepted.

That portfolio result is an owner acceptance test, not an independent benchmark. Private repository identities and evidence are not bundled here. See [`docs/REGRESSION_BASELINE.md`](docs/REGRESSION_BASELINE.md) for the public, de-identified regression contract.

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
