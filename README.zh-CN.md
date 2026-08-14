# RepoCover

[English](README.md)

[网站](https://blog.onovich.com/RepoCover/zh/) · [案例](https://blog.onovich.com/RepoCover/zh/examples/) · [GitHub Social Preview 指南](https://blog.onovich.com/RepoCover/zh/github-social-preview-guide/)

## 关于

我知道很多程序员并不擅长包装自己的仓库，我自己也一样：喜欢埋头苦干，直到写出了三百多个几乎无人问津的仓库。在 vibe coding 大行其道的今天，我开始意识到，让走过路过的人愿意多看一眼，或许有意义。

于是，就有了 RepoCover。我花了一天时间做的，看上去还不赖，我自己先用了。

![RepoCover 社交预览](docs/social-preview.png)

## 为什么使用 RepoCover

RepoCover 是一个让 AI 先理解项目、再设计仓库封面的 Codex Skill。它既适用于本地项目，也适用于远端项目。能够在本地打开预览的项目，尤其是已有前端界面的 Web 项目，通常能提供更完整的视觉依据，生成效果也会更好。

- **先理解项目，再开始设计：** 它会先看 README、代码、项目规则和已有视觉素材，再决定封面应该讲什么、展示什么。
- **让好的原始素材变得更好：** 保留有辨识度的截图、插画和品牌元素，同时删除杂乱内容，改善裁剪与构图。
- **没有主视觉也能做：** 没有可用截图、Logo 或插画时，会根据项目真实的对象、动作和结果建立视觉方向，而不是套用模板。
- **保留项目自己的样子：** 配色、主体、维度和视觉语言跟随当前项目，不套一套统一画风。
- **可编辑且符合 GitHub Social Preview 要求：** GitHub 接受小于 1 MB 的 PNG、JPG 或 GIF，建议尺寸至少为 `640×320`，并将 `1280×640` 列为最佳显示规格。RepoCover 因此固定输出精确的 `1280×640` PNG，并在旁边保留可编辑的 SVG 源文件。详见 [GitHub 官方 Social Preview 文档](https://docs.github.com/zh/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview)。
- **默认安全：** 生成图片不代表获得 README 修改、上传或更改仓库设置的权限。

## 快速开始

从当前仓库安装：

```text
使用 $skill-installer，从 onovich/RepoCover 的 skill/repo-cover 安装 Skill。
```

重启 Codex。打开一个本地仓库，或提供一个远端仓库地址，然后输入：

```text
使用 $repo-cover 理解这个项目，并生成一张经过验证的 GitHub Social Preview。
```

如果项目可以在本地运行预览，或本身已经有 Web 界面，生成时尽量保持它可访问。真实的产品画面通常会让结果更好。

默认输出：

```text
docs/social-preview.svg
docs/social-preview.png
```

默认情况下，RepoCover 只生成和验证图片文件。除非另外明确要求，否则它不会修改 README、上传图片或更改仓库设置。

## 示例

下面的示例来自游戏、工具、库和 Codex Skill。它们的版式和材料各不相同，因为设计跟随项目，而不是套用同一个模板。

| PrismDraft | LittlePNG |
| --- | --- |
| ![PrismDraft 社交预览](examples/prismdraft.png) | ![LittlePNG 社交预览](examples/littlepng.png) |

| DeskMochi | AudioTrim |
| --- | --- |
| ![DeskMochi 社交预览](examples/deskmochi.png) | ![AudioTrim 社交预览](examples/audiotrim.png) |

| [Beat](https://github.com/onovich/Beat) · 音频符号化 | [JustGoal.skill](https://github.com/onovich/JustGoal.skill) · 分支工作流 |
| --- | --- |
| ![Beat 社交预览](examples/beat.png) | ![JustGoal.skill 社交预览](examples/justgoal-skill.png) |

| [Knot](https://github.com/onovich/Knot) · 几何关系 | [Ping](https://github.com/onovich/Ping) · 弱素材重构 |
| --- | --- |
| ![Knot 社交预览](examples/knot.png) | ![Ping 社交预览](examples/ping.png) |

## 工作原理

1. 阅读 README、代码、仓库规则和已有视觉素材。
2. 弄清项目是做什么的、哪里最有辨识度，以及仓库内容能够证明什么。
3. 保留并重新组织好看的素材，删除干扰性的 UI 和杂乱内容；没有可用图片时，就从项目本身推导视觉方向。
4. 选择适合当前项目的构图和表现方式，而不是复用一套模板。
5. 输出可编辑 SVG 和精确的 `1280×640`、小于 1 MB 的 PNG，再检查完整尺寸和明暗背景下的缩略图是否清楚。
6. 除非用户另外要求上传或修改仓库，否则停在生成文件这一步。

完整 Agent 指令和按场景加载的参考文件位于 [`skill/repo-cover/`](skill/repo-cover/)。

## 开发

需要：

- Python 3.10+
- Node.js 20+
- 将 SVG 渲染为 PNG 时可用的 Sharp

运行仓库检查：

```text
python scripts/check.py
```

该命令检查 metadata、无 BOM 的 UTF-8、源码语法、全部便携示例和项目自身预览图。当前状态与新会话接手说明见 [`docs/PROJECT_STATUS.md`](docs/PROJECT_STATUS.md)，发布门禁见 [`docs/RELEASE_CHECKLIST.md`](docs/RELEASE_CHECKLIST.md)。

## 许可证

[MIT](LICENSE)

RepoCover 是独立开源项目，与 GitHub, Inc. 不存在隶属或背书关系。GitHub 是 GitHub, Inc. 的商标。
