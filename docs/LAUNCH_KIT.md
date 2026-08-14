# RepoCover launch kit

This document contains ready-to-use public copy for RepoCover `v0.1.0`. Keep claims aligned with the repository and replace a channel URL only when that channel is actually used.

## Core positioning

**One line:** RepoCover is a Codex Skill that reads a repository before designing an editable `1280×640` GitHub Social Preview from real project evidence.

**Short hook:** I built 300+ repositories that almost no one noticed, so I made a Codex Skill that reads a repo before designing its social preview.

**Landing page:** `https://blog.onovich.com/RepoCover/`

**Repository:** `https://github.com/onovich/RepoCover`

**Launch image:** `assets/launch-mosaic.png`

## Show HN

### Title

```text
Show HN: RepoCover – A Codex skill that reads a repo before designing its social preview
```

### Body

```text
I have built more than 300 repositories, and most of them received almost no attention. I am much better at building projects than packaging them.

So I made RepoCover, an open-source Codex Skill that reads a repository before designing its GitHub Social Preview. It looks at the README, meaningful code, project rules, working UI, and repository-owned visual assets. Good source material is recomposed; distracting UI is removed; when no useful hero image exists, the visual direction is inferred from the project's real objects, actions, relationships, and results.

The output is an editable SVG plus an exact 1280×640 PNG under GitHub's 1 MB limit. It also checks the result at thumbnail size on light and dark surroundings. Image generation and changing GitHub settings remain separate actions.

I tested the workflow across games, web tools, desktop apps, libraries, and Codex skills. The repository includes eight public examples and the complete Skill source.

Site: https://blog.onovich.com/RepoCover/?utm_source=hackernews&utm_medium=community&utm_campaign=v0_1_0
Source: https://github.com/onovich/RepoCover

I would especially value reports from repositories that have unusual visual evidence—or none at all.
```

## Short English social post

```text
I built 300+ repositories that almost no one noticed.

So I made RepoCover: an open-source Codex Skill that reads a repo before designing its GitHub Social Preview.

Real UI and project assets in. Editable SVG + validated 1280×640 PNG out. No shared template.

https://blog.onovich.com/RepoCover/?utm_source=social&utm_medium=post&utm_campaign=v0_1_0
```

Attach `assets/launch-mosaic.png`.

## Chinese launch post

### Title

```text
我写了三百多个没人看的仓库，于是做了 RepoCover
```

### Body

```text
我知道很多程序员并不擅长包装自己的仓库，我自己也一样：喜欢埋头苦干，直到写出了三百多个几乎无人问津的仓库。

于是，就有了 RepoCover。

它是一个开源 Codex Skill。做封面之前，它会先读 README、关键代码、项目规则、已有界面和仓库自带的视觉素材。原材料本来就好看时，它会保留项目身份并重新构图；截图里有杂乱 UI 时，它会清理；没有截图、Logo 或主形象时，它会从项目真实的对象、动作、关系和结果中推导视觉方向，而不是套模板。

最终会输出可编辑 SVG 和精确的 1280×640 PNG，并检查文件大小、原尺寸和缩略图。生成图片不等于获得上传或修改仓库设置的权限。

我已经用游戏、Web 工具、桌面应用、程序库和 Skill 做过回归测试，仓库里放了 8 个公开案例。

网站：https://blog.onovich.com/RepoCover/zh/?utm_source=cn_community&utm_medium=post&utm_campaign=v0_1_0
源码：https://github.com/onovich/RepoCover

如果你愿意试，我最想看到两类反馈：项目本身有很漂亮的界面时，它有没有保留住身份；项目完全没有主视觉时，它的纯推断是否诚实而且好看。
```

配图使用 `assets/launch-mosaic.png`。

## Product Hunt draft

Use this after independent users can install the Skill and reproduce the result.

**Name:** RepoCover

**Tagline:** Social previews shaped by the repository itself

**Description:**

```text
RepoCover is an open-source Codex Skill that reads your repository before designing its GitHub Social Preview. It preserves useful UI and project artwork, removes visual clutter, and can infer a truthful visual direction when no hero image exists. Every accepted result includes an editable SVG and validated 1280×640 PNG under 1 MB.
```

**Maker comment:**

```text
I built RepoCover after realizing that I had written more than 300 repositories and given almost none of them a clear visual introduction. I wanted AI to understand the project before trying to package it. The hardest part was not image generation—it was deciding when to preserve a beautiful source, when to clean up a screenshot, and when a repository genuinely needs a cold-start visual system. I would love to see what happens on projects outside my own collection.
```

Suggested gallery order:

1. `assets/plugin-showcase.png`
2. `assets/launch-mosaic.png`
3. `examples/littlepng.png`
4. `examples/prismdraft.png`
5. `examples/beat.png`

## OpenAI plugin directory copy

**Short description:** Design social previews from real repository evidence.

**Long description:** RepoCover reads a local or remote repository before composing an editable `1280×640` GitHub Social Preview. It preserves useful screenshots and project artwork, infers a truthful visual direction when no hero image exists, and validates the final SVG and PNG.

**Website:** `https://blog.onovich.com/RepoCover/`

**Support:** `https://blog.onovich.com/RepoCover/support/`

**Privacy:** `https://blog.onovich.com/RepoCover/privacy/`

**Terms:** `https://blog.onovich.com/RepoCover/terms/`

### Positive invocation tests

1. `Use $repo-cover to inspect this local web project, run the available preview, and create a validated GitHub Social Preview.`
2. `Use $repo-cover to improve this repository's existing cover while preserving its character artwork and visual identity.`
3. `Use $repo-cover to create a repository cover even though this library has no screenshot, logo, or hero image.`
4. `Use $repo-cover to create a GitHub Social Preview for this remote repository and state any evidence limitations.`
5. `Use $repo-cover to turn this project's SVG brand asset and real workflow into an editable 1280×640 cover.`

### Negative invocation tests

1. `Audit every repository in my GitHub account and decide which ones I should delete.`
2. `Create a launch presentation and a product demo video for this application.`
3. `Redesign the application's full user interface and implement the new frontend.`

## Tracking links

- Show HN: `?utm_source=hackernews&utm_medium=community&utm_campaign=v0_1_0`
- Product Hunt: `?utm_source=producthunt&utm_medium=launch&utm_campaign=v0_1_0`
- English social: `?utm_source=social&utm_medium=post&utm_campaign=v0_1_0`
- Chinese community: `?utm_source=cn_community&utm_medium=post&utm_campaign=v0_1_0`
- OpenAI directory: `?utm_source=openai_directory&utm_medium=plugin&utm_campaign=v0_1_0`

Do not add artificial star, vote, or like requests. Ask for concrete usage feedback instead.
