# RepoCover

[English](README.md)

基于仓库中的真实内容，为 GitHub 仓库生成精致、准确的社交分享预览图。

RepoCover 是一个 Codex Skill。它会读取仓库的 README、截图、Logo 和设计变量，生成可继续编辑的 SVG，以及精确的 `1280×640` PNG；随后分别在完整尺寸和分享卡片尺寸下检查结果。

![RepoCover 社交预览](docs/social-preview.png)

## 为什么使用 RepoCover

- **每个项目都有自己的设计：** 从当前仓库提取产品定位、配色和视觉语言，不套统一模板。
- **只使用真实证据：** 图中的功能、文案和数据必须能够在仓库中找到依据。
- **可以继续编辑：** PNG 旁边始终保留确定性生成的 SVG 源文件。
- **符合 GitHub 要求：** PNG 精确为 `1280×640`，并控制在 1 MB 以内。
- **真正检查缩略效果：** 自动生成 `320×160` 的明暗背景审阅图。
- **默认不会修改线上状态：** 生成图片不代表获得上传或修改仓库设置的权限。

## 快速开始

告诉 Codex：

```text
使用 $skill-installer，从 onovich/RepoCover 的 skill/repo-cover 安装 Skill。
```

重启 Codex，打开需要制作预览图的仓库，然后输入：

```text
使用 $repo-cover 为这个仓库生成 GitHub social preview。
```

默认输出：

```text
docs/social-preview.svg
docs/social-preview.png
```

除非你另外明确要求，否则 RepoCover 不会把图片上传到 GitHub。

## 示例

| PrismDraft | LittlePNG |
| --- | --- |
| ![PrismDraft social preview](examples/prismdraft.png) | ![LittlePNG social preview](examples/littlepng.png) |

| DeskMochi | AudioTrim |
| --- | --- |
| ![DeskMochi social preview](examples/deskmochi.png) | ![AudioTrim social preview](examples/audiotrim.png) |

这四个案例来自不同类型的真实仓库，用于验证 Skill 能否保留各自的产品身份，而不是只会更换标题和配色。

## 工作原理

1. 读取项目规则、产品依据和已有视觉素材。
2. 明确一个核心承诺、支持证据和应该排除的次要内容。
3. 在原生 SVG、真实截图混合或插画混合路线中选择最合适的一种。
4. 输出符合 GitHub 尺寸要求的图片。
5. 检查尺寸、体积、SVG 可访问性、内容相关性、裁剪和碰撞。
6. 在完整尺寸以及明暗背景下的 `320×160` 缩略尺寸中肉眼验收。

完整的 Agent 指令见 [`skill/repo-cover/SKILL.md`](skill/repo-cover/SKILL.md)。

## 开发

需要 Python 3.10+、Node.js 20+；将 SVG 渲染成 PNG 时需要 Sharp。

运行全部仓库检查：

```text
python scripts/check.py
```

当前状态和新会话接手说明见 [`docs/PROJECT_STATUS.md`](docs/PROJECT_STATUS.md)，发布门禁见 [`docs/RELEASE_CHECKLIST.md`](docs/RELEASE_CHECKLIST.md)。

## 许可证

[MIT](LICENSE)

RepoCover 是独立开源项目，与 GitHub, Inc. 不存在隶属或背书关系。GitHub 是 GitHub, Inc. 的商标。
