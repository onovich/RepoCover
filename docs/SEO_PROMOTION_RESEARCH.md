# RepoCover SEO 与推广一手资料研究

研究快照：2026-08-14。

本文只使用 Google Search Central、GitHub、OpenAI、X、LinkedIn、Product Hunt、Hacker News 和 Reddit 自己发布的资料。每一节都把“平台明确说明的事实”与“针对 RepoCover 的建议”分开；建议不代表搜索排名、收录、首页展示或传播效果的保证。

文中采用三种证据等级：

- **官方硬规则：** 不满足就无法提交、上传、解析或可能被平台处置的限制。
- **平台建议或可验证行为：** 平台明确推荐的尺寸、写法或展示方式，但不是排名与流量保证。
- **策略推断：** 我们结合 RepoCover 产品形态提出的执行选择，必须用真实发布数据验证。

## 结论摘要

RepoCover 应把 GitHub 仓库页和未来的项目网站当作两个不同的入口：

- **GitHub 仓库页负责站内发现、建立信任和完成安装。** GitHub 默认仓库搜索会搜索仓库名、description 和 topics；README 只有在用户显式使用 `in:readme` 时才被纳入仓库搜索。因此关键词不能只藏在 README 里。
- **GitHub Pages 或独立站负责可控的 Google SEO。** 在那里才能直接控制 HTML `<title>`、meta description、页面层级、图片 alt、多语言 URL、站点地图和 Search Console。GitHub 仓库页仍可能出现在搜索结果里，但它的 HTML 和搜索展示不由项目完全控制。
- **推广要建立在“看得懂、装得上、能试用”的产品表面之上。** 先做好仓库元数据、README 首屏、案例、Social Preview 和正式 Release，再考虑 Show HN；Product Hunt 更适合放在具备清晰落地页与演示之后。
- **不要把 SEO 做成关键词堆砌。** Google 明确推荐 people-first 内容；RepoCover 最有价值的长期内容是可验证的真实案例、设计诊断和 GitHub Social Preview 实用指南。

## 当前仓库基线

以下是 2026-08-14 完成本轮优化后，通过 GitHub CLI 复核 `onovich/RepoCover` 得到的项目状态，不是平台规则：

- description 已更新为：`An open-source AI coding Skill that reads your repository before creating an editable 1280×640 GitHub Social Preview.`
- 已有 13 个 topics：`codex-skill`、`design-automation`、`developer-tools`、`github-social-preview`、`og-image`、`open-graph-image`、`repository-branding`、`social-card`、`svg`、`agent-skill`、`codex-cli`、`openai-codex`、`social-preview`。
- homepage URL 已指向 `https://blog.onovich.com/RepoCover/`。
- 已发布首个 GitHub Release：`v0.1.0`。
- 公开仓库页已经使用自定义 `og:image`，说明 Social Preview 已成功设置。
- README、官网、Skill 触发描述和推广文案目前都围绕单仓库封面生成，不再把批量审计或空库筛选当成产品能力。

这意味着 GitHub 入口、Pages、Release、分享图和基础文案已经完整。下一步更大的缺口是 Search Console 收录、个人主页置顶、陌生用户试用反馈和按渠道发布，而不是继续堆更多近义 topics。

## GitHub 内部发现与分享

### 仓库名、description、topics 与 README

**官方事实**

- GitHub 的仓库搜索默认搜索仓库名、description 和 topics；`in:readme` 需要由搜索者明确指定。[GitHub：Searching for repositories](https://docs.github.com/en/search-github/searching-on-github/searching-for-repositories)
- GitHub REST API 把 `description` 定义为仓库的简短说明，把 `homepage` 定义为“包含该仓库更多信息的 URL”；官方没有把 homepage 描述成搜索排名信号。[GitHub：Update a repository](https://docs.github.com/en/rest/repos/repos#update-a-repository)
- Topics 的目的就是帮助其他人发现项目、寻找可贡献项目和同类解决方案。每个 topic 最多 50 个字符，只能使用小写字母、数字和连字符，每个仓库最多 20 个。[GitHub：Classifying your repository with topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics)
- GitHub 说明 README 往往是访客看到仓库时首先接触的内容，并建议回答：项目做什么、为什么有用、如何开始、去哪里获得帮助、谁在维护。[GitHub：About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)

**对 RepoCover 的建议**

1. 保留品牌名 `RepoCover`，让 description 自然包含一组核心意图词：`AI coding Skill`、`GitHub Social Preview`、`1280×640`。不要把同义词全部塞进一句话。
2. 当前 topics 已覆盖主要搜索意图。可在真实 GitHub 搜索中比较 `social-preview`、`github-social-preview`、`codex-skill` 等查询后再决定是否替换，而不是追求用满 20 个。
3. README 已保留 `About` 作为第一个正式章节，并在随后用 `What RepoCover does` 直接说明输入、输出和适用场景；继续保持这种先讲人话、再讲细节的顺序。
4. README 已把安装和使用压缩成两句可直接发给 AI Agent 的指令。后续只在真实安装路径改变时更新，不再加入“重启 Codex”等非必要步骤。

### Social Preview

**官方事实**

- GitHub 允许为仓库设置在社交平台分享链接时展示的预览图。未设置时，展开的仓库链接只显示基本信息和所有者头像。[GitHub：Customizing a repository's social media preview](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview)
- 图片可用 PNG、JPG 或 GIF，必须小于 1 MB；官方建议至少 `640×320`，并指出 `1280×640` 的显示效果最佳。只有公开仓库的图片可以被公开分享。

**对 RepoCover 的建议**

- RepoCover 当前已成功设置自定义 Social Preview。后续更换封面时，应继续用真实仓库 URL 检查公开 `og:image`，而不是只确认图片存在于文件树。
- Social Preview 应被看作**分享点击率和识别度素材**，而不是 SEO 排名因子。GitHub 官方文档没有声称它会提升 GitHub 搜索或 Google 排名。

### Releases、个人主页与 GitHub Pages

**官方事实**

- GitHub Release 可以基于 tag 打包可用版本、release notes 和下载文件；用户还可以只订阅新 Release 通知。[GitHub：About releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)
- GitHub 个人主页最多可以固定六个仓库或 gist，使访客快速看到最好的作品。[GitHub：Pinning items to your profile](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/pinning-items-to-your-profile)
- GitHub Pages 可以直接从仓库中的 HTML、CSS 和 JavaScript 发布静态项目网站，并支持项目站点和自定义域名。[GitHub：What is GitHub Pages?](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)

**对 RepoCover 的建议**

- 发布一个有明确版本号的首个 Release，说明安装方法、支持范围、固定产物和代表性案例。Release 是可信的版本入口和订阅入口；没有官方证据表明它本身提高搜索排名。
- 把 RepoCover 固定到 `onovich` 个人主页，尤其是在对外发布期间。
- 建立轻量 GitHub Pages 项目站。它不需要变成庞大营销网站，首版只要能完成“理解产品—看案例—安装”即可。

## Google SEO

### 内容、标题、摘要和链接

**官方事实**

- Google 推荐 helpful、reliable、people-first 内容，并建议把用户真正会使用的搜索词自然放在页面标题、主标题、alt 和链接文字等显眼位置；链接应可抓取，也应在相关社区中让潜在用户知道产品。[Google Search Essentials](https://developers.google.com/search/docs/essentials)
- 满足技术要求和最佳实践并不保证 Google 一定抓取、索引或展示页面。
- 搜索结果标题由 Google 自动生成，可能参考 `<title>`、页面主标题、显眼文字、链接文字和 `og:title` 等信息。标题应清晰、简洁、准确且避免关键词堆砌。[Google：Title links](https://developers.google.com/search/docs/appearance/title-link)
- 搜索摘要主要根据页面正文生成；当 meta description 比正文片段更准确时，Google 也可能采用它。重要页面应使用简短、独特、与该页内容一致的 description。[Google：Snippets](https://developers.google.com/search/docs/appearance/snippet)
- Google 没有为 `<title>` 或 meta description 规定固定字符上限；两者都会根据设备宽度按需截断。因此“60 个字符标题”或“160 个字符描述”只能作为编辑习惯，不能写成 Google 硬规则。
- Google 表示，大量新页面是通过链接发现的；逻辑清晰的站内链接和来自其他网页的真实链接都有助于发现。[Google：SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)

**对 RepoCover 的建议**

- 不要试图控制 GitHub 仓库页无法控制的 HTML。把主要 Google SEO 工作放到 Pages：每页一个明确主题、一个主标题、一段准确摘要和可抓取的普通链接。
- 首页建议：

  - `<title>`：`RepoCover — AI GitHub Social Preview Generator for Codex`
  - `<h1>`：`Design GitHub Social Previews from your repository, not a template.`
  - meta description：`Create an editable 1280×640 GitHub Social Preview from your repository. RepoCover reads the project first and chooses a visual approach that fits it.`

- 这些是待验证文案，不是已证明有搜索量的关键词。后续必须用 Search Console 的真实 query 数据修正。

### Canonical、多语言与分享元数据

**官方事实**

- Google 把重定向和 `rel="canonical"` 视为较强的 canonical 信号，把 sitemap 视为较弱信号；不同方法不应为同一页面指向互相冲突的 canonical。Google 推荐 canonical 页面也写自引用 canonical，并推荐使用绝对 URL。[Google：Canonical URLs](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)
- Canonical 不是进入 Google 的硬性前提；Google 明确说明，即使站点不声明 canonical，也会自行选择认为最合适的版本。这里配置 canonical 是为了减少歧义，不是为了获得额外排名。
- 使用 `hreflang` 时，每个语言版本必须列出自己和其他版本，alternate URL 必须是完整 URL；成对页面需要互相返回链接，否则标注可能被忽略。HTML、HTTP header 和 sitemap 三种 hreflang 方法等效，选择一种即可，没有必要三种同时维护。[Google：Localized versions](https://developers.google.com/search/docs/specialty/international/localized-versions)
- Google 通过页面可见正文判断语言，而不是依靠 `hreflang` 或 HTML `lang` 属性。`x-default` 可作为未匹配语言的后备入口，但不是每个双语站都必须添加。
- Google 会把 `og:title` 作为生成搜索结果标题的候选信号之一，但标题生成仍是自动的。LinkedIn 则明确要求可分享页面提供 `og:title`、`og:image`、`og:description` 和 `og:url`。[Google：Title links](https://developers.google.com/search/docs/appearance/title-link)，[LinkedIn：Make your website shareable](https://www.linkedin.com/help/linkedin/answer/a521928/making-your-website-shareable-on-linkedin?lang=en)

**对 RepoCover 的建议**

- 英文 `/` 与中文 `/zh/` 是真实翻译页面，应各自使用自引用 canonical；不要把中文页 canonical 到英文页。两页都放 `en` 与 `zh-Hans` 的双向 hreflang，必要时让英文主页承担 `x-default`。
- canonical、`og:url`、sitemap 和内部链接统一使用最终公开 URL。如果未来从 `github.io` 切换自定义域名，应先确定唯一正式域名并用重定向迁移，避免同时宣传两套 URL。
- Pages 的 Open Graph 图单独输出 `1200×627`，以满足 LinkedIn 链接预览的当前要求；GitHub 仓库 Social Preview 继续保留 `1280×640`。两者不是同一个平台规格。
- 页面发布后用真实 URL 分别在 LinkedIn 和 X 中预览。不要假定一个 `og:image` 在所有平台都会以同样裁切方式展示。

### 图片与案例内容

**官方事实**

- Google 使用图片附近的正文、标题、文件名和 alt 来理解图片；建议使用标准 HTML `<img>`、描述性文件名和有信息量但不堆关键词的 alt。[Google：Image SEO best practices](https://developers.google.com/search/docs/appearance/google-images)
- Google 建议图片放在相关文字附近，并使用清晰、高质量且与页面主题一致的图片。
- `max-image-preview:large` 允许 Google 在搜索结果中显示最大可达视口宽度的较大图片预览，但只是允许上限，不保证一定出现大图。[Google：Robots meta tag](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag)

**对 RepoCover 的建议**

- 不要只做一页九宫格。每个重点案例应说明：仓库是什么、能取得哪些素材、做了什么取舍、最终封面如何保持项目身份。
- 首批案例覆盖三类即可：有现成 Web 界面、只有品牌或主视觉素材、完全没有可用主视觉的冷启动项目。它们恰好证明 RepoCover 的差异化能力。
- 使用描述性文件名，例如 `repocover-web-ui-case-study.png`，并写准确 alt，例如 `RepoCover social preview generated from an existing web game interface`。
- 社交封面通常包含大字号文字；为图片搜索和案例理解，可同时展示局部素材、前后对照或设计诊断，不要让一张带字封面承担全部视觉说明。
- Pages 可以设置 `<meta name="robots" content="max-image-preview:large">`，同时仍需依靠相关正文、准确 alt 和可抓取图片 URL；这不是大图展示保证。

### 独立页面、结构化数据和监测

**官方事实**

- Search Console 可以查看 Google 如何抓取和索引网站，并按 query、page 和 country 查看 impressions、clicks 等数据。Google 建议大约每月或内容发生较大变化后检查；站点地图不是收录的必要条件，但可能加快发现。[Google：Get started with Search Console](https://developers.google.com/search/docs/monitor-debug/search-console-start)
- 结构化数据可以帮助 Google 理解页面并使其具备某些富结果资格，但即使完全符合规则也不保证展示。[Google：General structured data guidelines](https://developers.google.com/search/docs/appearance/structured-data/sd-policies)
- 结构化数据必须真实代表页面可见内容，不能标记隐藏、无关或误导性信息。Google 支持 JSON-LD、Microdata 和 RDFa，并通常推荐较容易维护的 JSON-LD。[Google：Structured data introduction](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)
- Google 的 `SoftwareApplication` 富结果要求 `name`、`offers.price`，并且还要求真实的 rating 或 review 二者之一。[Google：Software application structured data](https://developers.google.com/search/docs/appearance/structured-data/software-app)

**对 RepoCover 的建议**

- Pages 首版结构建议保持小而明确：

  1. `/`：英文主页、定位、精选案例、安装入口。
  2. `/examples/`：三到六个有解释的案例，而不是无上下文图库。
  3. `/github-social-preview-guide/`：尺寸、上传位置、常见构图问题和实用检查清单。
  4. `/zh/`：中文主页；每种语言使用独立 URL，并互相链接。

- 站点上线后接入 Search Console、提交 sitemap，并记录发布前基线。
- 暂不把 `SoftwareApplication` 富结果列为首要任务：RepoCover 没有应被虚构的评分或评论。只有具备真实合规数据时再添加；普通 JSON-LD 并不自动带来特殊展示。
- 候选搜索意图如下，但只能视为测试假设：

  - English：`GitHub social preview generator`、`repository cover generator`、`Codex skill`、`AI GitHub cover`、`1280x640 social preview`。
  - 中文：`GitHub 仓库封面`、`GitHub Social Preview 生成器`、`GitHub 社交预览图`、`Codex Skill 封面`。

## 首次发布渠道

### 平台素材与发布规则速查

| 平台与发布方式 | 官方硬规则 | 平台建议或展示行为 | RepoCover 策略推断 |
| --- | --- | --- | --- |
| GitHub Social Preview | PNG/JPG/GIF，小于 1 MB；公开分享需要公开仓库 | `1280×640` 为最佳显示尺寸 | 直接使用 RepoCover 标准产物 |
| X 原生图片帖 | 图片不超过 5 MB；GIF/JPEG/PNG；普通帖最多 4 个媒体项、280 字符 | 单图在 `2:1` 到 `3:4` 间完整展示；支持每图 alt | 用 `1280×640` PNG 原生上传并附项目 URL，不依赖未验证的链接卡裁切 |
| LinkedIn 链接预览 | 页面必须有指定 OGP 标签；分享图不超过 5 MB且至少 `1200×627` | 推荐 `1.91:1`；帖子最多 3000 字符 | 为 Pages 单独生成 `1200×627` OGP 图 |
| LinkedIn 原生图片帖 | 不超过 5 MB，至少 `552×276`，比例在 `3:1` 到 `4:5`；最多 20 图 | 推荐宽度至少 1080；首图决定多图布局 | 案例叙事可用 3–5 张图，但链接预览与原生图片帖二选一 |
| Product Hunt | 个人账户且至少加入社区一周；tagline 最多 60 字符；thumbnail 必填且图片/GIF 小于 3 MB；gallery 至少 2 图才显示 | 两个官方页面对 description 上限分别写 260 和 500；thumbnail 推荐 `240×240`，gallery 推荐 `1270×760` | 文案保守控制在 260 字符内并以提交表单为准；单独制作方图和 gallery |
| Show HN | 标题以 `Show HN` 开头；必须是可实际尝试、作者亲自制作的项目；不得组织点赞或评论 | 尽量无注册门槛，作者在场交流 | 图片不是提交必需品，入口页和安装体验更重要 |
| Reddit | 遵守站点 Spam 规则和目标 subreddit 自有规则；各社区可关闭 links/images 等帖子类型 | 官方没有统一的全站开源工具发布图片尺寸 | 逐社区核对，不做同文群发；不确定时先问 moderators |

### OpenAI 插件目录

**平台事实**

- OpenAI 当前允许 Skill 在没有 MCP server 的情况下独立工作，也允许一个插件只包含一个或多个 Skill。[OpenAI：Build skills](https://developers.openai.com/plugins/build/skills)
- 每个插件都需要 `.codex-plugin/plugin.json`；skills-only plugin 可以把现有 Skill 放进 `skills/` 后打包。公开插件发布到 ChatGPT 与 Codex 共用的通用插件目录。[OpenAI：Package your plugin](https://developers.openai.com/plugins/build/plugins)
- OpenAI 的公开提交流程明确支持 `Skills only`。提交前需要准备插件介绍、Logo、网站、支持页、隐私政策、条款、5 个正向测试和 3 个负向测试，并使用已验证的开发者或企业身份。[OpenAI：Submit plugins](https://developers.openai.com/plugins/deploy/submission)
- OpenAI Developers 社区页提供官方的项目、Demo 或工作流展示提交入口。[OpenAI Developers：Community](https://developers.openai.com/community)

**对 RepoCover 的建议**

- 这是比泛 SEO 更精准的产品分发入口。RepoCover 不需要为了上架而新建 MCP；应先包装为 skills-only plugin，并继续复用当前已验证的 `SKILL.md`、references、scripts 和示例资产。
- 将公开插件提交放在 Pages 网站完成之后，因为提交材料本身要求网站、支持、隐私和条款 URL。提交前先补 8 个清晰的正负测试，正好也能成为产品回归门禁。
- 插件通过审核或具备稳定安装路径后，再向 OpenAI Developers Showcase 提交案例；不要把“提交”表述成一定会获得展示。

### GitHub 原生发布

**平台事实**

- GitHub 原生可用的公开入口包括 description、topics、README、Social Preview、Release、个人主页固定仓库和 Pages；它们各自承担搜索、说明、分享、版本订阅或展示作用，官方没有把它们描述成通用排名捷径。
- 拥有 push 权限的人可以在 Insights → Traffic 查看最近 14 天的完整 clone、访客、referring sites 和热门内容。[GitHub：Viewing traffic to a repository](https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/viewing-traffic-to-a-repository)

**发布建议**

先完成首个 Release、确认现有 Social Preview 的公开解析、补 homepage URL、固定到个人主页；发布前一天记录 GitHub Traffic、stars 和 clones，发布后按 24 小时、7 天和 14 天复盘。GitHub Traffic 只有短窗口，应及时留存快照。

### X

**官方硬规则与平台行为**

- 标准 X 帖最多 280 字符，可包含链接和最多 4 个媒体项；更长帖子属于 Premium 能力，不应作为公开发布文案的可达性前提。[X：How to post](https://help.x.com/en/using-x/how-to-post)
- 原生照片最大 5 MB，支持 GIF、JPEG 和 PNG；单张图片比例在 `2:1` 到 `3:4` 之间时会完整显示。[X：How to post photos or GIFs](https://help.x.com/en/using-x/posting-gifs-and-pictures)
- 每张图片可以添加不超过 1000 字符的描述，X 建议描述简洁并说明图片发生了什么。[X：Image descriptions](https://help.x.com/en/using-x/picture-descriptions)
- X 禁止批量、重复、不相关或未经请求的推广，也禁止滥用热门 hashtag、在无关回复中引流、复制粘贴同一文案或协调刷互动。[X：Authenticity policy](https://help.x.com/en/rules-and-policies/authenticity)
- X Business 的自然内容建议是使用简洁、口语化的文案和明确行动提示，避免全大写以及文字过多的图片；当前页面还建议避免 hashtag。这是平台内容建议，不是帖子能否发布的硬门槛。[X Business：Organic best practices](https://business.x.com/en/basics/organic-best-practices)

**对 RepoCover 的建议**

- 使用一条简短作者口吻正文、一个 `1280×640` PNG 原生附件和一个项目 URL。RepoCover 的 2:1 图片正好处于 X 官方说明的完整显示范围内。
- 为图片写真正有用的 alt，例如说明“左侧为仓库名与定位，右侧为从项目界面提炼的视觉构图”，不要把帖子正文原样复制进 alt。
- 如要展示多样性，最多用 4 张差异明显的封面；不要用四张相似图稀释主视觉。
- 不在多条回复或不同话题下复制同一链接；首发后用新的案例、设计判断或真实更新形成后续内容。
- 旧版 Twitter Card 详细规格页在本次核对时已重定向到 X Developer 首页，当前官方文档中没有找到可稳定引用的链接卡尺寸规则。因此这里不把历史 `summary_large_image` 参数写成 2026 年硬规则，发布前应以真实预览为准。

### LinkedIn

**官方硬规则与平台建议**

- 可分享网页必须提供 `og:title`、`og:image`、`og:description` 和 `og:url`。LinkedIn 分享模块要求图片不超过 5 MB、至少 `1200×627`，并推荐 `1.91:1`。[LinkedIn：Make your website shareable](https://www.linkedin.com/help/linkedin/answer/a521928/making-your-website-shareable-on-linkedin?lang=en)
- LinkedIn 普通帖子最多 3000 字符。链接预览框使用 `1200×627`、`1.91:1` 的图像框。[LinkedIn：Share articles or links](https://www.linkedin.com/help/linkedin/answer/a525301/sharing-articles-or-links?lang=en)
- 原生图片不超过 5 MB、至少 `552×276`，宽高比须处于 `3:1` 到 `4:5`；最多可上传 20 张，平台推荐宽度达到 1080。LinkedIn 明确说明，同一个帖子选择 URL 链接预览或原生图片，不能同时使用两者。[LinkedIn：Share photos](https://www.linkedin.com/help/linkedin/answer/a527229/sharing-photos-or-videos?lang=en)
- LinkedIn Page 的 super/content admin 可以在发链接时自定义预览图片和标题；这不是所有个人帖都具备的权限。[LinkedIn：Customize a Page post preview](https://www.linkedin.com/help/linkedin/answer/a566445/customize-the-image-and-title-of-a-linkedin-page-post-preview?lang=en)
- LinkedIn 的另一份官方 Marketing Help 针对部分自然链接的小缩略图布局建议 `3:2` 或 `16:9`，而分享模块文档推荐 `1.91:1`。这些建议对应不同展示模块，不能合并成一个全站统一比例。[LinkedIn：Image specifications for organic posts](https://www.linkedin.com/help/lms/answer/a1696024)
- LinkedIn 的官方分享指南建议短文中提出问题或观点、使用相关富媒体并回复评论。这是发布质量建议，不是分发保证。[LinkedIn：Sharing Guide](https://content.linkedin.com/content/dam/help/linkedin/en-us/LinkedIn-Sharing-Guide.pdf)

**对 RepoCover 的建议**

- 如果目标是把人带到 Pages，选择链接预览：准备 `1200×627` OGP 图，让正文讲“问题—方法—可试用入口”。
- 如果目标是展示案例，选择原生多图帖：首图放最清晰的结果，后续依次放原素材、诊断、重构结果。由于首图决定多图布局，发布前必须在 composer 中实际预览。
- `1280×640` 虽然尺寸大于 LinkedIn 最低宽高，但不是分享模块推荐的 `1.91:1`；不要把它强行拉伸为 `1200×627`，应重新排版或安全裁切。由于 LinkedIn 自身对不同模块给出不同建议，最终以真实 composer 预览为准。

### Hacker News / Show HN

**平台事实**

- **提交规则：** 标题必须以 `Show HN` 开头；内容必须是作者亲自制作、其他人可以实际尝试的非平凡项目。普通文章、报名页、纯落地页和尚不能试用的项目不属于 Show HN；不得要求朋友帮忙点赞或评论。[Show HN Guidelines](https://news.ycombinator.com/showhn.html)
- **平台建议：** 尽量降低注册或邮箱等体验门槛，解释做了什么以及为什么做，并由作者留在讨论中回答问题。项目可以处于早期，也不必做得非常精致。
- HN 的通用 Guidelines 还禁止删除后重发、夸张或全大写标题，以及把 HN 主要当作推广渠道；其“评论”规则明确禁止生成式或 AI 润色的文本。该禁令原文位于评论章节，不能扩大解释为已明确覆盖提交标题，但 RepoCover 的首条说明和后续回复仍应由作者亲手写。[Hacker News Guidelines](https://news.ycombinator.com/newsguidelines.html)
- Show HN 没有原生 thumbnail、gallery 或 Social Preview 图片字段，也没有官方图片尺寸；被链接页面是否有封面不会改变 HN 列表本身的提交格式。

**对 RepoCover 的建议**

- Show HN 是优先级较高的首发渠道，因为受众技术性强，RepoCover 也有真实代码、可安装 Skill、明确输入输出和大量实测案例。
- 发布前确保陌生用户可以只看 README 就完成安装并生成第一张图。若仍需要作者手把手协助，就先不要发。
- 标题可以直接陈述：`Show HN: RepoCover – a Codex skill that designs GitHub social previews from your repo`。
- 提交说明和评论由作者本人用自己的语言写，讲为什么做这个工具、截图直用和过度演绎之间的设计难点，并坦率说明限制。不要把生成文案直接贴到 HN，不要写成广告，也不要组织点赞。

### Product Hunt

**平台事实**

- Product Hunt 目前主要展示已经可用的数字产品，关注 useful、novel、high craft 和 creative；其 featuring 指南明确说并非所有提交都会进入首页，并将模板列入通常不展示的类别。[Product Hunt Featuring Guidelines](https://help.producthunt.com/en/articles/9883485-product-hunt-featuring-guidelines)
- **官方硬规则：** 发帖需要个人账户，并至少加入 Product Hunt 社区一周；产品名字段只能写正式名称；tagline 最多 60 字符，launch tags 最多 3 个。主链接应直达产品，GitHub 仓库可以作为主链接，但不接受短链或 tracking link。Thumbnail 必填且图片/GIF 小于 3 MB；gallery 至少两张图片才会显示。[Product Hunt：Preparing for launch](https://www.producthunt.com/launch/preparing-for-launch)，[Product Hunt：Personal vs company account](https://help.producthunt.com/en/articles/771527-personal-account-vs-company-account)
- **官方口径冲突：** Launch Guide 写 description 最多 500 字符，而 Help Center 的发帖页写 260 字符。不能把任一数字伪装成无争议规则；实际准备时控制在 260 字符内，并以当日提交表单为准。[Product Hunt：Preparing for launch](https://www.producthunt.com/launch/preparing-for-launch)，[Product Hunt：How to post a product](https://help.producthunt.com/en/articles/479557-how-to-post-a-product)
- **平台建议：** maker 可以自己提交且不需要 Hunter；thumbnail 推荐方形 `240×240`，gallery 推荐 `1270×760`；主 URL 应直达产品页而不是新闻或博客。官方把美西时间 12:01 AM 视为获得完整发布日的一条经验建议，不是曝光保证。
- 可以先创建 draft 或预约发布。Product Hunt 允许自然分享发布链接，但禁止群发、索取或激励点赞、组织投票；官方鼓励 maker 与评论者真实互动。[Product Hunt：How do I share my post?](https://help.producthunt.com/en/articles/2690626-how-do-i-share-my-post)
- Product Hunt 的评论指南禁止 AI 生成评论。Maker 首条说明和回复应由作者亲自撰写，不应直接粘贴模型生成文案。[Product Hunt：Commenting guidelines](https://help.producthunt.com/en/articles/10030102-commenting-guidelines)

**对 RepoCover 的建议**

- Product Hunt 放在 Show HN 之后或至少放在 Pages 演示完成之后。它更依赖一眼可懂的产品页、gallery 和即时试用体验。
- 不要把 RepoCover 描述成“prompt/template pack”。应证明它是一个会读取项目、诊断素材、生成和验收实际文件的开发者工具；即便如此，是否 featured 仍由 Product Hunt 决定。
- 准备三类素材：一句话动图或短视频演示、三组差异明显的案例、安装到成图的流程图。Gallery 图片需另做 `1270×760` 适配，不能直接假定 `1280×640` Social Preview 会得到最佳展示。
- 首条 maker comment 由作者亲手写，讲真实起因、一天做出原型后如何用大量仓库继续打磨、目前限制和希望获得的反馈。分享时请别人“看看并给反馈”，不要要求 upvote。

### Reddit

**官方硬规则与平台行为**

- Reddit 禁止重复或未经请求的大规模互动。反复群发相同内容、批量私信、反复发布无关链接等都可能被视为 spam 并被删除或封禁。[Reddit：Spam](https://support.reddithelp.com/hc/en-us/articles/360043504051-Spam)
- Reddit 禁止协调投票、多账号刷票和其他操纵互动行为。[Reddit：Disrupting communities](https://support.reddithelp.com/hc/en-us/articles/360043066412-Disrupting-Communities)
- Reddit 明确说明推广内容本身不必然是 spam，但不同社区可以完全禁止推广，或自行采用类似“10% self-promotion”的社区规则；该 10% 不是 Reddit 全站统一硬规则。[Reddit：Keeping spam out of a community](https://support.reddithelp.com/hc/en-us/articles/28012014962580-How-do-I-keep-spam-out-of-my-community)
- 每个 subreddit 都可以独立允许或关闭 Text、Links、Images、Galleries、Videos 等帖子类型，moderators 也可以制定额外的提交要求。[Reddit：Community settings](https://support.reddithelp.com/hc/en-us/articles/15484546290068-Community-settings)
- 标题发布后不能编辑；站点提交 API 的标题上限是 300 字符，但 subreddit 可以设置更严格的资格、flair 和格式要求。[Reddit：Posting and commenting](https://support.reddithelp.com/hc/en-us/articles/360060422572-How-do-I-post-and-comment-on-Reddit)，[Reddit API：submit](https://www.reddit.com/dev/api/#POST_api_submit)
- Reddiquette 提到“适度”分享自己的内容，并把 9:1 作为广泛使用的经验比例；它不是全站硬阈值，仍应以目标社区规则和 moderators 判断为准。[Reddit：Reddiquette](https://support.reddithelp.com/hc/en-us/articles/205926439-Reddiquette)
- 本次核对没有在 Reddit 官方用户帮助中找到适用于所有 subreddit 的开源工具发布图片尺寸。因此不应把 Reddit Ads 规格或某个社区规则误写成有机帖全站规则。

**对 RepoCover 的建议**

- Reddit 不应作为“一天内同步铺量”的首发渠道。先选择作者真实参与、主题确实匹配的 1–2 个社区，阅读 sidebar、pinned post 和发帖表单提示；规则不清楚就先联系 moderators。
- 帖子应以可讨论的技术经验为主体，例如“为什么直接截图和过度重构都会损伤仓库封面”，RepoCover 作为可复现实例放在正文中，而不是只丢 GitHub 链接。
- 不跨 subreddit 原样复制标题、正文和图片。是否允许链接、自荐或图片完全服从目标社区规则。

### 其他相关社区

Google 明确建议在志同道合的相关社区中介绍产品，但这不等于可以跨社区复制同一篇推广文。只有在发布时重新核对各社区规则，并能带来该社区真正关心的经验或案例，才应投稿。没有一套跨 X、LinkedIn、Hacker News、Product Hunt 与 Reddit 通用的最佳文案或图片尺寸。

## 建议执行顺序

### 阶段 1：把 GitHub 入口做完整

1. 已统一 README、`SKILL.md`、`agents/openai.yaml` 和 listing 草案的产品定位。
2. 已完成简洁 README、双语官网、案例和安装入口。
3. 已发布首个带安装说明和案例的 `v0.1.0` Release。
4. 尚需在 GitHub 个人主页手动固定 RepoCover。

### 阶段 2：建立可控的搜索入口

1. 发布轻量 GitHub Pages，先做英文主页、中文主页、案例页和一篇实用指南。
2. 为每页写唯一 title、H1 和 meta description；所有案例图片使用准确文件名和 alt。
3. 设置 homepage URL，提交 sitemap，接入 Search Console。

### 阶段 2.5：进入产品原生分发目录

1. 将现有 Skill 包装成 skills-only plugin，补 `.codex-plugin/plugin.json` 和插件目录元数据。
2. 准备公开网站、支持页、隐私政策、条款、Logo、5 个正向测试和 3 个负向测试。
3. 在本地 marketplace 完成安装与触发测试后，提交 OpenAI 插件审核。
4. 审核通过或安装路径稳定后，提交 OpenAI Developers Showcase。

### 阶段 3：发布而不是群发

1. 先做 Show HN，作者当天亲自回答反馈。
2. 为 X 准备 `1280×640` 原生图片帖，为 LinkedIn 准备 `1200×627` 链接预览或独立多图案例帖，不在两个平台照搬同一段文案。
3. 根据真实反馈补文档和演示，再准备 Product Hunt 的 `240×240` thumbnail、`1270×760` gallery 与 maker comment。
4. Reddit 只进入作者已参与或确有经验可分享的社区；每次先核对社区规则，并围绕该社区的具体问题重写内容。

### 阶段 4：用数据迭代

- Google：按月记录非品牌查询、品牌查询、页面 impressions、clicks、CTR 和国家/语言。
- GitHub：在每次发布后的 24 小时、7 天、14 天记录 visitors、clones、referrers、stars、forks 和 issues。
- 产品：记录从落地页到 GitHub、从 GitHub 到安装说明的点击，以及陌生用户能否独立完成首次生成。
- 内容：优先扩写已经获得真实 impressions 或社区问题的主题；不要批量制造没有第一手案例的关键词页。

## 建议的 30 天执行版

下面的数字是第一轮验证目标，不是增长承诺。

### 第 1 周：定位与发布基础

- 已统一 Skill 触发文案、README、官网和推广材料。
- 已把仓库 description 调整为直接说明 AI coding Skill、GitHub Social Preview 和 `1280×640` 输出。
- 已补充 `agent-skill`、`codex-cli`、`openai-codex` 与 `social-preview` 等相关 topics，没有用满 20 个。
- 已发布 `v0.1.0` 首个公开 Release，并写清安装、输入和输出。
- 将 RepoCover 固定到个人 GitHub 主页。
- 验收门槛：一个从未参与开发的人能只看公开资料完成安装，并知道下一步该输入什么。

### 第 2 周：上线最小 SEO 站点

- 用 GitHub Pages 发布 `/`、`/zh/`、`/examples/` 和 `/github-social-preview-guide/`。
- 首页承担定位与安装；案例页先做三类真实案例：已有 Web UI、只有主视觉素材、完全无主视觉。
- 指南页回答高意图问题：推荐尺寸、1 MB 限制、设置位置、缩略图检查和常见构图错误。
- 添加独立 title、description、canonical、hreflang、图片 alt、sitemap 和 robots.txt；将仓库 homepage 指向 Pages。
- 接入 Search Console，并保存上线日索引基线。

### 第 3 周：原生产品分发

- 包装 skills-only plugin，补公开支持页、隐私政策与条款。
- 编写 5 个正向和 3 个负向测试，并在本地 marketplace 完成安装、触发与输出验证。
- 提交 OpenAI 插件目录审核；同时准备但暂不保证能被收录的 OpenAI Developers Showcase 材料。
- 邀请 3–5 位没有参与项目的人独立生成第一张封面，记录卡点而不是代替他们操作。

### 第 4 周：集中首发

- 先发布 Show HN，标题候选：`Show HN: RepoCover – a Codex skill that designs GitHub social previews from your repo`。
- X 使用原生 `1280×640` 封面和短文；LinkedIn 使用单独的 `1200×627` 链接预览图或有过程说明的多图帖。两边都添加准确图片描述，并用真实 composer 检查裁切。
- 中文渠道以“程序员更擅长做项目、不擅长介绍项目”的共同问题、三种素材情况和可复制安装命令为主体；可向相关社区自荐，但不群发同一篇广告。
- Reddit 仅在目标社区明确允许相关自荐时发布技术复盘；规则不清楚就先询问 moderators，不把 Reddit 当成同步分发列表。
- 根据一周真实反馈修正文档与演示，再决定是否准备 Product Hunt；若发布，必须按开发者工具而不是 prompt/template pack 定位。
- 形成一次公开复盘：哪些仓库素材最好用、何时该保留截图、何时才需要推断。它既是内容资产，也是产品可信度证明。

### 30 天验证指标

- **激活：** 至少 5 位非项目参与者独立完成一次生成。
- **公开证明：** 至少 3 个第三方公开仓库实际采用 RepoCover 封面。
- **发现：** Pages 关键页面被 Search Console 发现，并开始出现至少一个非品牌查询；不预设排名。
- **仓库：** 每次发布后保存 24 小时、7 天、14 天的 visitors、clones、referrers、stars 和 issues 快照。
- **反馈：** 记录首次安装与首次成图的主要失败点，下一轮优先降低这些摩擦，而不是追逐单纯 star 数量。

## 不能从资料中推出的结论

- 无法保证修改 description、topics 或 README 会获得某个 GitHub 排名。
- 无法保证 Social Preview、Release、结构化数据或 sitemap 会提升 Google 排名或触发富结果。
- 无法仅凭关键词措辞判断搜索量；必须等待 Search Console 或其他真实用户数据。
- 无法保证 Show HN 达到首页门槛，也无法保证 Product Hunt featured。
- 无法用一张 `1280×640` 图片覆盖所有平台的最佳展示：LinkedIn 和 Product Hunt 有不同的官方推荐规格，Reddit 又由各社区决定可用帖子类型。
- 无法从 Product Hunt 现有官方页面得到唯一无冲突的 description 上限；260 与 500 两种口径并存，只能以更保守文案和实际表单处理。
- 无法从当前 X 官方文档确认一个适用于所有自然链接卡片的固定图片尺寸；原生图片规则不能冒充链接卡规则。
- 无法保证 Open Graph 图在每个平台立即刷新或采用相同裁切；发布前必须用真实 URL 预览，缓存更新也可能滞后。
- 外链的价值来自真实发现与引用，不应通过交换、群发或组织投票制造。
