# RepoCover SEO 与推广一手资料研究

研究快照：2026-08-14。

本文只使用 GitHub、Google Search Central、Product Hunt 和 Hacker News 自己发布的资料。每一节都把“平台明确说明的事实”与“针对 RepoCover 的建议”分开；建议不代表搜索排名、收录、首页展示或传播效果的保证。

## 结论摘要

RepoCover 应把 GitHub 仓库页和未来的项目网站当作两个不同的入口：

- **GitHub 仓库页负责站内发现、建立信任和完成安装。** GitHub 默认仓库搜索会搜索仓库名、description 和 topics；README 只有在用户显式使用 `in:readme` 时才被纳入仓库搜索。因此关键词不能只藏在 README 里。
- **GitHub Pages 或独立站负责可控的 Google SEO。** 在那里才能直接控制 HTML `<title>`、meta description、页面层级、图片 alt、多语言 URL、站点地图和 Search Console。GitHub 仓库页仍可能出现在搜索结果里，但它的 HTML 和搜索展示不由项目完全控制。
- **推广要建立在“看得懂、装得上、能试用”的产品表面之上。** 先做好仓库元数据、README 首屏、案例、Social Preview 和正式 Release，再考虑 Show HN；Product Hunt 更适合放在具备清晰落地页与演示之后。
- **不要把 SEO 做成关键词堆砌。** Google 明确推荐 people-first 内容；RepoCover 最有价值的长期内容是可验证的真实案例、设计诊断和 GitHub Social Preview 实用指南。

## 当前仓库基线

以下是 2026-08-14 通过 GitHub CLI 读取 `onovich/RepoCover` 得到的项目状态，不是平台规则：

- description 已存在：`A Codex skill for polished 1280x640 GitHub repository social previews, grounded in real project assets.`
- 已有 9 个 topics：`codex-skill`、`design-automation`、`developer-tools`、`github-social-preview`、`og-image`、`open-graph-image`、`repository-branding`、`social-card`、`svg`。
- homepage URL 为空。
- 尚无 GitHub Release。
- 当前公开仓库页已经解析到自定义 `og:image`，说明 Social Preview 已成功设置。
- Stars、forks 以及最近 14 天的 GitHub Traffic 仍为 0；项目刚发布，尚未形成外部引用和使用信号。
- README 已移除批量审计卖点，但 `skill/repo-cover/SKILL.md` 的触发描述与 `agents/openai.yaml` 仍强调 portfolio、空库筛选和批量生成。推广前需要统一产品边界，否则 README、插件目录与模型触发会互相矛盾。

这意味着仓库的 GitHub 站内关键词基础和分享封面已经不错，下一步更大的缺口是统一产品定位、可控的项目落地页、首次 Release 和外部发布材料，而不是继续堆更多近义 topics。

## GitHub 内部发现与分享

### 仓库名、description、topics 与 README

**官方事实**

- GitHub 的仓库搜索默认搜索仓库名、description 和 topics；`in:readme` 需要由搜索者明确指定。[GitHub：Searching for repositories](https://docs.github.com/en/search-github/searching-on-github/searching-for-repositories)
- Topics 的目的就是帮助其他人发现项目、寻找可贡献项目和同类解决方案。每个 topic 最多 50 个字符，只能使用小写字母、数字和连字符，每个仓库最多 20 个。[GitHub：Classifying your repository with topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics)
- GitHub 说明 README 往往是访客看到仓库时首先接触的内容，并建议回答：项目做什么、为什么有用、如何开始、去哪里获得帮助、谁在维护。[GitHub：About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)

**对 RepoCover 的建议**

1. 保留品牌名 `RepoCover`，让 description 自然包含一组核心意图词：`Codex skill`、`GitHub Social Preview`、`Open Graph image`、`1280×640`。不要把同义词全部塞进一句话。
2. 当前 topics 已覆盖主要搜索意图。可在真实 GitHub 搜索中比较 `social-preview`、`github-social-preview`、`codex-skill` 等查询后再决定是否替换，而不是追求用满 20 个。
3. 在 README 的 `# RepoCover` 后、`About` 标题前增加一句极短的英文定位，不必移动“About”：

   > A Codex skill that reads your project and creates a polished 1280×640 GitHub Social Preview from real project evidence.

   这样可以让首次访问者先知道产品是什么，同时保留个人故事作为第一个正式章节。
4. README 首屏应尽快出现最终封面、安装方式和一句差异点，例如 “from your repository, not a template”。更长的流程和开发说明继续放在下方。

### Social Preview

**官方事实**

- GitHub 允许为仓库设置在社交平台分享链接时展示的预览图。未设置时，展开的仓库链接只显示基本信息和所有者头像。[GitHub：Customizing a repository's social media preview](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview)
- 图片可用 PNG、JPG 或 GIF，必须小于 1 MB；官方建议至少 `640×320`，并指出 `1280×640` 的显示效果最佳。只有公开仓库的图片可以被公开分享。

**对 RepoCover 的建议**

- 为 RepoCover 自己上传当前已经验收的 `1280×640` 封面。这直接验证产品承诺，也让外部分享链接具备一致视觉身份。
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
- Google 表示，大量新页面是通过链接发现的；逻辑清晰的站内链接和来自其他网页的真实链接都有助于发现。[Google：SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)

**对 RepoCover 的建议**

- 不要试图控制 GitHub 仓库页无法控制的 HTML。把主要 Google SEO 工作放到 Pages：每页一个明确主题、一个主标题、一段准确摘要和可抓取的普通链接。
- 首页建议：

  - `<title>`：`RepoCover — AI GitHub Social Preview Generator for Codex`
  - `<h1>`：`Design GitHub Social Previews from your repository, not a template.`
  - meta description：`RepoCover reads your repository and creates an editable SVG plus a polished 1280×640 GitHub Social Preview grounded in real project evidence.`

- 这些是待验证文案，不是已证明有搜索量的关键词。后续必须用 Search Console 的真实 query 数据修正。

### 图片与案例内容

**官方事实**

- Google 使用图片附近的正文、标题、文件名和 alt 来理解图片；建议使用标准 HTML `<img>`、描述性文件名和有信息量但不堆关键词的 alt。[Google：Image SEO best practices](https://developers.google.com/search/docs/appearance/google-images)
- Google 建议图片放在相关文字附近，并使用清晰、高质量且与页面主题一致的图片。

**对 RepoCover 的建议**

- 不要只做一页九宫格。每个重点案例应说明：仓库是什么、能取得哪些素材、做了什么取舍、最终封面如何保持项目身份。
- 首批案例覆盖三类即可：有现成 Web 界面、只有品牌或主视觉素材、完全没有可用主视觉的冷启动项目。它们恰好证明 RepoCover 的差异化能力。
- 使用描述性文件名，例如 `repocover-web-ui-case-study.png`，并写准确 alt，例如 `RepoCover social preview generated from an existing web game interface`。
- 社交封面通常包含大字号文字；为图片搜索和案例理解，可同时展示局部素材、前后对照或设计诊断，不要让一张带字封面承担全部视觉说明。

### 独立页面、结构化数据和监测

**官方事实**

- Search Console 可以查看 Google 如何抓取和索引网站，并按 query、page 和 country 查看 impressions、clicks 等数据。Google 建议大约每月或内容发生较大变化后检查；站点地图不是收录的必要条件，但可能加快发现。[Google：Get started with Search Console](https://developers.google.com/search/docs/monitor-debug/search-console-start)
- 结构化数据可以帮助 Google 理解页面并使其具备某些富结果资格，但即使完全符合规则也不保证展示。[Google：General structured data guidelines](https://developers.google.com/search/docs/appearance/structured-data/sd-policies)
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

先完成首个 Release、上传 Social Preview、补 homepage URL、固定到个人主页；发布前一天记录 GitHub Traffic、stars 和 clones，发布后按 24 小时、7 天和 14 天复盘。GitHub Traffic 只有短窗口，应及时留存快照。

### Hacker News / Show HN

**平台事实**

- Show HN 面向作者亲自制作、其他人可以实际尝试的非平凡项目；应尽量降低注册或邮箱等体验门槛，并说明做了什么以及为什么做。[Show HN Guidelines](https://news.ycombinator.com/showhn.html)
- 标题必须以 `Show HN` 开头。项目尚不能试用时不应发布；普通文章、报名页和纯落地页不属于 Show HN。
- 作者需要在讨论中出现并回答问题；不得要求朋友帮忙点赞或评论。

**对 RepoCover 的建议**

- Show HN 是优先级较高的首发渠道，因为受众技术性强，RepoCover 也有真实代码、可安装 Skill、明确输入输出和大量实测案例。
- 发布前确保陌生用户可以只看 README 就完成安装并生成第一张图。若仍需要作者手把手协助，就先不要发。
- 标题可以直接陈述：`Show HN: RepoCover – a Codex skill that designs GitHub social previews from your repo`。
- 正文由作者本人用自己的语言写，讲三百多个仓库、为什么做这个工具、截图直用和过度演绎之间的设计难点，并坦率说明限制。不要写成广告，也不要组织点赞。

### Product Hunt

**平台事实**

- Product Hunt 目前主要展示已经可用的数字产品，关注 useful、novel、high craft 和 creative；其 featuring 指南明确说并非所有提交都会进入首页，并将模板列入通常不展示的类别。[Product Hunt Featuring Guidelines](https://help.producthunt.com/en/articles/9883485-product-hunt-featuring-guidelines)
- 发帖需要个人账户；官方建议 maker 自己提交，不需要 Hunter。提交项包括产品直达 URL、最多 260 字符的 description、gallery、maker 信息和 first comment。Gallery 至少两张图片才会显示，推荐尺寸为 `1270×760`。[Product Hunt：How to post a product](https://help.producthunt.com/en/articles/479557-how-to-post-a-product)
- 可以先创建 draft 或预约发布。Product Hunt 允许自然分享发布链接，但禁止群发、索取或激励点赞、组织投票；官方鼓励 maker 与评论者真实互动。[Product Hunt：How do I share my post?](https://help.producthunt.com/en/articles/2690626-how-do-i-share-my-post)

**对 RepoCover 的建议**

- Product Hunt 放在 Show HN 之后或至少放在 Pages 演示完成之后。它更依赖一眼可懂的产品页、gallery 和即时试用体验。
- 不要把 RepoCover 描述成“prompt/template pack”。应证明它是一个会读取项目、诊断素材、生成和验收实际文件的开发者工具；即便如此，是否 featured 仍由 Product Hunt 决定。
- 准备三类素材：一句话动图或短视频演示、三组差异明显的案例、安装到成图的流程图。Gallery 图片需另做 `1270×760` 适配，不能直接假定 `1280×640` Social Preview 会得到最佳展示。
- 首条 maker comment 讲真实起因、一天做出原型后如何用大量仓库继续打磨、目前限制和希望获得的反馈。分享时请别人“看看并给反馈”，不要要求 upvote。

### 其他相关社区

Google 明确建议在志同道合的相关社区中介绍产品，但这不等于可以跨社区复制同一篇推广文。只有在发布时重新核对各社区规则，并能带来该社区真正关心的经验或案例，才应投稿。Reddit 各 subreddit 规则差异很大，本研究没有找到能代表所有 subreddit 的统一可靠发布规则，因此不列出通用 Reddit 发布方案。

## 建议执行顺序

### 阶段 1：把 GitHub 入口做完整

1. 先统一 README、`SKILL.md`、`agents/openai.yaml` 和未来插件 listing 的产品定位，移除不再属于产品能力的 portfolio 与空库筛选触发描述。
2. 在 H1 后补一句清晰定位，同时保留“About”为第一个正式章节。
3. 发布首个带安装说明、案例和已知限制的版本。
4. 固定到 GitHub 个人主页。

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
2. 根据真实反馈补文档和演示，再准备 Product Hunt gallery 与 maker comment。
3. 只进入作者已参与或确有经验可分享的开发者社区；每次围绕该社区的具体问题重写内容。

### 阶段 4：用数据迭代

- Google：按月记录非品牌查询、品牌查询、页面 impressions、clicks、CTR 和国家/语言。
- GitHub：在每次发布后的 24 小时、7 天、14 天记录 visitors、clones、referrers、stars、forks 和 issues。
- 产品：记录从落地页到 GitHub、从 GitHub 到安装说明的点击，以及陌生用户能否独立完成首次生成。
- 内容：优先扩写已经获得真实 impressions 或社区问题的主题；不要批量制造没有第一手案例的关键词页。

## 建议的 30 天执行版

下面的数字是第一轮验证目标，不是增长承诺。

### 第 1 周：定位与发布基础

- 统一 Skill 触发文案与 README 定位。
- 将仓库 description 调整为：`A Codex skill that reads your repository and creates an editable 1280×640 GitHub Social Preview from real project evidence.`
- 在现有 topics 基础上测试补充 `agent-skill`、`openai-codex` 与 `social-preview`，不为凑数量添加无关词。
- 发布 `v0.1.0` 首个公开 Release；写清安装、输入、输出、代表案例和已知限制。
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
- 中文渠道以“三百多个仓库”故事、三组前后对照和可复制安装命令为主体；可向 GitHubDaily 的 Issue 自荐，但不群发同一篇广告。
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
- 外链的价值来自真实发现与引用，不应通过交换、群发或组织投票制造。
