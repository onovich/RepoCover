# RepoCover 产品策略一手资料研究

研究日期：2026-08-14
研究范围：产品域名、案例选择、2026 年盈利可能性
证据范围：官方文档、产品官网、官方定价页、GitHub API 与当前仓库文件；不采用第三方 SEO 博文或市场规模报告。

本文使用三种标签：

- **官方事实**：平台明确写出的规则、功能或限制。
- **市场观察**：厂商官网展示的产品形态和当前标价，只能证明市场上有人这样卖，不能证明 RepoCover 也能以同样价格成交。
- **策略判断**：结合事实与 RepoCover 当前状态给出的建议，不是平台承诺或收入预测。

## 已确认决策

2026-08-14，项目所有者确认：

- 迁移到 `repo-cover.onovich.com`，并为旧路径保留逐页永久重定向；
- 案例页采用“重点完整案例 + 视觉案例”两层结构，前置问题逐个解决；
- 当前不以盈利为目标，优先让 RepoCover 帮助推广 onovich 与其有实际价值的项目。

具体执行状态与人工操作清单见 [`PROMOTION_ROADMAP.md`](PROMOTION_ROADMAP.md)。

## 结论先行

1. **域名值得迁，但必须有条件。** `repo-cover.onovich.com` 的主要价值是品牌更独立、地址更短，并且 Google 支持在子域根级表达独立站点名称；Google 明确表示子目录和子域在索引、排名上没有偏好，因此不能把迁移说成 SEO 提权。只有能把旧地址逐页做永久重定向时才建议迁移；否则先保留 `https://blog.onovich.com/RepoCover/`，不要只为“看起来更像 SEO”而承担迁移损失。
2. **案例页不能只选最好看的图。** 最佳结构是“两层案例”：视觉图库负责证明风格宽度，重点案例负责证明 RepoCover 对真实、公开、可核验项目有用。首页和完整案例应优先使用公开仓库，并尽可能提供可运行入口、真实输入证据和生成判断。
3. **2026 年存在赚到小规模收入的可能，但没有证据支持被动高收入或立刻做 SaaS。** OpenAI 当前允许 skills-only plugin 进入插件目录，却明确禁止插件销售数字服务、订阅和 credits；GitHub Sponsors 又受收款地区限制。最合理顺序是：免费开源 Skill 获得用户和公开采用案例，站外测试少量人工复核/代办服务，只有出现反复、批量、团队级需求后再考虑托管产品。

## 一、是否迁到 `repo-cover.onovich.com`

### 当前基线

**仓库观察（2026-08-14）：**

- GitHub Pages API 返回当前地址为 `https://blog.onovich.com/RepoCover/`，构建方式为 GitHub Actions，`https_enforced=true`，RepoCover 仓库本身没有单独设置 `cname`。
- `blog.onovich.com` 当前以 CNAME 指向 `onovich.github.io`；`repo-cover.onovich.com` 尚未解析。
- 仓库内共有 132 处完整旧站地址，分布在 21 个文件中，涉及 canonical、hreflang、Open Graph、JSON-LD、sitemap、robots、README、检查脚本和站内链接。迁移不是只改一个 DNS 记录。

### GitHub Pages 的官方规则

**官方事实：** GitHub Pages 支持自定义子域；用户站点的自定义域默认会被同账户的项目站继承，但项目仓库可以设置自己的自定义域来覆盖这个默认地址。[GitHub：About custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages)

**官方事实：** 配置 `repo-cover.onovich.com` 时，应先在 RepoCover 仓库的 **Settings → Pages → Custom domain** 保存该域名，再到 DNS 提供商增加 CNAME，直接指向 `onovich.github.io`，不能带仓库名。当前项目使用自定义 Actions 工作流，因此 GitHub 不要求 `CNAME` 文件，并会忽略已有的 `CNAME` 文件。DNS 传播及 HTTPS 可用性可能需要最多 24 小时。[GitHub：Managing a custom domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)

**官方事实：** GitHub 建议先验证自定义域，再绑定仓库，以降低域名接管风险；同时不建议使用通配符 DNS。[GitHub：Verifying your custom domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages)

**限制：** GitHub 文档明确说明了 apex/`www` 配对时的自动重定向，但没有承诺把任意旧路径 `blog.onovich.com/RepoCover/...` 自动永久重定向到新的子域。不能把 GitHub Pages 的域名绑定本身当作完整迁移方案。

### Google 对子域和迁移的官方规则

**官方事实：** Google 在索引和排名上不偏好子目录或子域，建议选择更容易组织和管理的方式。[Google：Crawling and indexing FAQ](https://developers.google.com/search/help/crawling-index-faq)

**官方事实：** Google Search 的站点名称支持域名和子域根级，不支持子目录级。因此 `repo-cover.onovich.com` 可以作为独立站点名称的根，而 `blog.onovich.com/RepoCover/` 不能拥有独立的子目录站点名称。这是展示和品牌控制优势，不是排名保证。[Google：Site names](https://developers.google.com/search/docs/appearance/site-names)

**官方事实：** URL 迁移应准备一对一 URL 映射，以服务端 `301` 或其他永久重定向把旧页直接指向对应新页，避免重定向链；同时更新内部链接、canonical、sitemap，并在 Search Console 验证和监控新旧站。Google 建议永久重定向至少保留一年，并提示迁移期间搜索可见性可能短期波动。[Google：Site moves with URL changes](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes)

**官方事实：** Search Console 的 Change of Address 只能用于域名级属性，不能从 `blog.onovich.com/RepoCover/` 这样的路径级属性发起。因此只迁 RepoCover 这一段路径时，无法依靠该工具传递迁移信号，逐页永久重定向更重要。[Google：Change of Address tool](https://support.google.com/webmasters/answer/9370220)

### 品牌、SEO 与成本比较

| 维度 | 保留 `blog.onovich.com/RepoCover/` | 迁到 `repo-cover.onovich.com` |
| --- | --- | --- |
| 品牌识别 | 像个人博客下的一个栏目 | 更像独立、长期维护的产品 |
| Google 固有排名优势 | 无已证实优势 | 同样无已证实优势 |
| 独立站点名称 | 子目录级不受支持 | 子域根级受支持，但最终显示仍由 Google 决定 |
| URL 可读性 | 较长，含大小写路径 | 更短，产品词直接可见 |
| 迁移风险 | 无 | 需要逐页永久重定向；短期可见性可能波动 |
| 当前改造量 | 无迁移改造 | 至少涉及 21 个文件、132 处完整旧地址，并需 DNS、HTTPS、Search Console 与旧址重定向 |
| 后续独立运营 | 与博客域和路径结构耦合 | 更容易独立维护站点、结构化数据和产品品牌 |

### 策略判断

**建议迁移，但设置一个硬门槛：必须先证明旧址能够对每个有效 URL 返回到对应新 URL 的服务端永久重定向。**

- 如果能够控制 `blog.onovich.com` 的旧路径重定向，建议在正式大规模推广前迁移。产品还新，当前积累的外链和索引信号通常比未来少，越晚迁移，协调成本往往越高。这是时机判断，不是 Google 的排名规则。
- 如果旧站只能放一个 JavaScript 或 meta refresh 跳转页，无法提供可靠的 `301/308`，建议先不迁。继续使用当前地址并不会因为它是子目录而受到 Google 排名惩罚。
- 迁移不要同时大改内容、导航和信息架构。Google 明确提示，把站点迁移和重设计叠加会增加重新理解页面的成本。[Google：Change of Address tool](https://support.google.com/webmasters/answer/9370220)

### 迁移执行门禁

在全部满足后再切换：

1. 列出所有现有可索引 URL，并建立旧 URL 到新 URL 的一对一映射。
2. 先把站点 origin 与 base path 集中到构建配置中，避免继续维护 132 处硬编码。
3. 在账户级验证 `onovich.com`，然后先在 RepoCover 的 Pages 设置中保存 `repo-cover.onovich.com`。
4. DNS 新增 `repo-cover.onovich.com CNAME onovich.github.io`；确认解析后启用并验证 HTTPS。
5. 新站同步更新 canonical、hreflang、Open Graph、JSON-LD、sitemap、robots、README 和对外资料。
6. 在旧站或可控制的边缘层启用逐页 `301/308`，直接到最终地址，不经过中间跳转。
7. 验证新旧 Search Console 属性，提交新 sitemap，抽查首页、案例、指南、隐私、条款和中英文对应页。
8. 监控 404、索引、展示和点击；重定向至少保留一年，用户仍可能访问时宜长期保留。

## 二、案例页应该展示什么

### 可验证内容比纯视觉陈列更有说服力

**官方事实：** Google 对 people-first 内容的自查问题包括：是否提供原创分析、完整描述、清晰来源、第一手经验，以及能否说明内容由谁、如何、为何产生。对于 AI 辅助内容，Google也建议在读者合理关心时解释自动化如何参与。[Google：Creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)

**策略推论：** 对 RepoCover 来说，公开仓库、可运行界面、原始素材和最终封面之间的可追溯关系，就是最强的第一手证据。单纯展示一张好看的图，只能证明“能画得好看”；把仓库、原证据、诊断和结果连起来，才能证明“能读懂不同项目并作出合适判断”。

### 当前案例页的观察

当前中英文案例页展示 8 张图和简短设计说明，但没有给每个案例附仓库或在线演示链接。2026-08-14 的 GitHub 查询中，`PrismDraft`、`AudioTrim`、`Beat`、`DeskMochi`、`JustGoal.skill`、`Knot`、`Ping` 能按当前名称解析为公开仓库；`onovich/LittlePNG` 未按该名称解析。上述 7 个公开仓库的 GitHub API 均未报告 Pages 站点。

这套页面已经能证明视觉范围，但还不能让访客方便核验项目是否真实可用，也不能展示封面是否真的被仓库采用。

### 建议采用“两层案例”

#### 1. 视觉图库

用途是让访客在十几秒内看见风格和项目类型的多样性。

- 以最终图和一句大白话说明为主。
- 可以保留视觉很强、但暂时没有在线演示的项目。
- 私有项目只有在权利、隐私和可见信息都确认后才能展示；不得写访客无法验证的功能或效果。
- 图库负责“好看与多样”，不承担完整转化证明。

#### 2. 重点案例

用途是证明 RepoCover 确实理解了真实项目，并让访客能继续体验或检查。

- 必须是公开仓库，或已获得项目所有者明确展示授权。
- 项目本身要有清楚用途、实质内容和稳定入口；有在线演示最好，没有演示时也应能从 README 安装或运行。
- 页面应包含：项目用途、公开仓库、可运行入口（如有）、使用了哪些截图/主视觉/代码证据、前置诊断、保留与重构了什么、最终封面、实际 Social Preview 采用状态。
- 明确说明 AI 做了什么、人工验收做了什么，避免把生成过程包装成不可解释的魔法。

### 案例入选框架

先过硬门槛，再评分。

**硬门槛：**

1. 展示权利与隐私已确认。
2. 仓库不是空壳，项目用途能够用一句话讲清楚。
3. 可见文案和图形均可追溯到仓库证据或明确标注的设计推导。
4. 封面通过 1280×640 和 320×160、亮色与暗色背景验收。
5. 重点案例必须有稳定的公开仓库 URL；仅图库项目可在缺少公开 URL 时例外。

**重点案例评分：**

| 指标 | 分值 | 判断问题 |
| --- | ---: | --- |
| 公开与可核验性 | 25 | 访客能否查看仓库、README、发布物或演示？ |
| 项目实用性与推广价值 | 20 | 它是否解决了真实问题，值得访客继续了解？ |
| 最终视觉质量 | 20 | 全尺寸与缩略图是否都清楚、有辨识度？ |
| 能否讲清独特设计判断 | 20 | 是否代表真实 UI、现成主视觉、代码推导等不同输入模式？ |
| 样本代表性 | 10 | 是否补足 Web、工具、游戏、程序库、Skill 等组合？ |
| 稳定与维护状态 | 5 | 链接、说明和运行入口是否仍有效？ |

建议总分达到 75 且无硬门槛失败，才进入重点案例；否则留在视觉图库或暂不展示。分数只用于内部取舍，不需要显示给访客。

### 推荐的首批重点案例组合

不要全选同一种“最好看”的图，而应覆盖至少三种证据路径：

1. **已有真实界面：** 能打开 Web 或本地应用，展示如何删冗余、补缺漏、重构构图而不改掉产品身份。
2. **已有主视觉：** 仓库自带角色、Logo、SVG 或关键图形，展示如何保留优秀材料并重新组织。
3. **没有可用图片：** 从代码中的真实对象、动作、拓扑或结果推导画面，展示纯推断也不等于套模板。

每类先选 1–2 个真正公开、可体验或容易安装的项目。视觉更强但项目入口较弱的作品继续留在图库，不应成为首页唯一证据。

## 三、2026 年的盈利可能性

### RepoCover 当前产品事实

- 仓库采用 MIT License，允许他人使用、修改、分发甚至销售副本；这有利于传播，但也意味着“提示词本身稀缺”不是可靠壁垒。
- 当前 Skill 在用户的 Codex 环境里运行；公开隐私页说明项目方不接收或保存仓库内容，站点为无账号、无分析、无广告、无表单的静态站。
- 当前没有托管后端、计费、用量账户或团队权限系统。运营成本和隐私风险较低，但也没有天然的按量收费或订阅入口。

### OpenAI/Codex 的分发与收费边界

**官方事实：** OpenAI 允许只包含 Skills 的 plugin 提交审核；公开提交还需要开发者身份、官网/支持/隐私/条款、listing、starter prompts 和正负测试等材料。[OpenAI：Submit plugins](https://developers.openai.com/plugins/deploy/submission)；[OpenAI：Build skills](https://developers.openai.com/plugins/build/skills)

**官方事实：** 当前公开的 plugin manifest 与提交流程没有价格字段，也没有文档化的付费安装、按调用分成或创作者结算机制。正确说法是“官方没有提供或证实”，而不是断言以后永远不会有。

**官方硬限制：** 插件目前只允许实物商品交易。数字产品或服务、订阅、数字内容、tokens、credits，以及 freemium 升级均不允许。用户可以登录已有付费账户使用已购权益，但插件不得展示订阅方案、发起订阅或推广升级，也不得直链 checkout；插件还不得投放广告或主要作为广告载体。[OpenAI：Plugin guidelines—Commerce and monetization](https://developers.openai.com/plugins/app-guidelines#commerce-and-monetization)

**官方事实：** OpenAI 的 checkout 文档同样说明，当前审批限于实物商品插件；ChatGPT payment sheet 仅对少数 marketplace partners 处于 beta。[OpenAI：Checkout API](https://developers.openai.com/plugins/build/monetization)

**策略判断：** OpenAI 插件目录目前只能作为 RepoCover 的免费分发和发现渠道，不能作为售卖仓库封面、订阅或 credits 的店铺。若未来另建站外付费服务，也不能把插件交互设计成升级漏斗；最多让已在站外拥有权益的用户登录使用，并持续复核届时政策。

### GitHub Sponsors 的边界

**官方事实：** 收款人必须居住或合法运营于 GitHub Sponsors 支持地区。2026-08-14 的官方列表包含 Hong Kong SAR 和 Macao SAR，但未列中国大陆或台湾；任何地区都可以赞助别人，不等于任何地区都能收款。[GitHub：About GitHub Sponsors—Supported regions](https://docs.github.com/en/sponsors/getting-started-with-github-sponsors/about-github-sponsors#supported-regions-for-github-sponsors)

**策略判断：** 必须按作者的实际居住地或主体所在地核对资格。如果作者位于中国大陆，当前不能把 GitHub Sponsors 设为主要收入 CTA。官方的 fiscal host 文档列出了可用代管机构，但没有说明它能绕过地区资格，因此不能当作确定解法。[GitHub：Using a fiscal host](https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/using-a-fiscal-host-to-receive-github-sponsors-payouts)

**官方事实：** GitHub Sponsors 支持最多 10 个一次性 tier 和 10 个月付 tier；个人账户发起的赞助 GitHub 不收手续费，组织账户发起的赞助最多收 6%。维护者需自行评估并缴税，提供有价值的回报还可能产生销售税义务。[GitHub：Managing sponsorship tiers](https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/managing-your-sponsorship-tiers)；[GitHub：Fees and taxes](https://docs.github.com/en/sponsors/sponsoring-open-source-contributors/about-sponsorships-fees-and-taxes)；[GitHub：Tax information](https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/tax-information-for-github-sponsors)

**策略判断：** 如果地区资格成立，Sponsors 适合作为“支持持续维护”的辅助收入，优先使用纯支持、致谢等简单回报；它不是销量可预测的产品结算渠道，也不应预估固定月收入。

### 相邻产品在卖什么

以下是厂商当前官网标价，均为厂商自己的产品说明：

| 产品 | 当前公开价格示例 | 主要收费对象 |
| --- | --- | --- |
| ogimg.xyz | 免费 50 张/月；Hobby US$4.90/月含 1,000 张；Pro US$9.90/月含 10,000 张 | 固定模板、参数化 OG 图片 API |
| HTML/CSS to Image | 免费 50 张/月；Basic US$14/月；Pro US$149/月；Scale US$749/月 | HTML/URL 渲染、模板、批量、组织与集成 |
| ScreenshotOne | 免费 100 张；Basic US$17/月含 2,000 张；Growth US$79/月含 10,000 张；Scale US$259/月含 50,000 张 | 稳定截图、HTML/PDF 渲染、自动化与基础设施 |
| Bannerbear | 30 credits 试用；Automate US$49/月含 1,000 API credits；Scale US$149；Enterprise US$299 | 模板、图片/视频 API、集成、团队、CDN 与治理 |

来源：[ogimg.xyz](https://ogimg.xyz/)；[HTML/CSS to Image](https://htmlcsstoimage.com/pricing)；[ScreenshotOne](https://screenshotone.com/pricing/)；[Bannerbear](https://www.bannerbear.com/pricing/)

**市场观察：** 相邻产品已经证明“稳定批量生成、API、模板管理、工作流集成、团队权限和托管基础设施”可以形成订阅产品。但这些价格不能证明用户愿意为 RepoCover 的单张、低频、需要判断和验收的封面付费。

**市场观察：** 通用渲染已经很便宜，而且 Vercel 的开源 [Satori](https://github.com/vercel/satori) 可以把 HTML/CSS/JSX 转成 SVG，用于 OG/social 图片。RepoCover 不能把“输出一张 PNG”本身当作高价壁垒。

**策略判断：** RepoCover 真正可能收费的部分是：读懂仓库、提取证据、判断该保留或重构什么、避免失真、人工或自动 QA、处理私有仓库、遵守团队品牌规则，以及多仓库审批与更新流程。

### 建议的商业化顺序

#### 阶段 1：免费开源产品，先证明有人采用

- 完成公开插件提交与安装体验。
- 把 3–6 个重点案例做成可核验案例，并展示封面确实被仓库设置为 Social Preview。
- 记录独立用户数、成功生成数、公开采用数、失败原因和平均修改轮次。

这一阶段的目标不是收入，而是证明问题真实存在、结果值得采用。

#### 阶段 2：站外测试一次性人工复核服务

- 限量接受单仓库和多仓库组合包，由作者人工复核证据、构图与最终验收。
- 价格不要照抄 API 厂商；先按实际工时、模型/工具成本、沟通和返工建立成本底线，再测试 2–3 个价格点。
- 首批只做少量付费名额，记录成交率、平均工时、返工次数、最常见需求和客户是否愿意再次购买。
- 收款与服务说明必须独立于 OpenAI 插件交互，并遵守所在地的税务、付款和隐私要求。

这是当前最容易验证的收入路径，因为它销售的是判断与质量，而不是廉价渲染量。

#### 阶段 3：只有出现重复团队需求，才考虑托管产品

可能形成持续付费的功能包括：

- 私有仓库授权与最小权限访问；
- 团队品牌规则和禁止项；
- 多仓库队列、版本对比、审批与审计记录；
- Release 或 README 更新时的封面刷新；
- CI 集成、组织级资产管理和人工 review。

如果需求仍然是“每个仓库偶尔做一次封面”，按仓库/项目包通常比月订阅更自然。只有客户持续管理很多仓库或频繁更新，订阅才有合理基础。

### 进入下一阶段的验证门槛

以下是内部策略门槛，不是行业标准：

1. 至少 10 名非作者本人用户成功完成生成。
2. 至少 5 个公开仓库实际采用生成图，而不只是表示“好看”。
3. 至少 5 次真实付费试单，且能测出可接受的平均工时和返工率。
4. 至少 3 个客户明确提出重复、批量、私有仓库或团队审批需求，才进入托管产品设计。
5. 若大多数用户只愿意免费使用、付费试单工时过高或没有重复需求，应保持为开源工具和作品入口，而不是勉强做 SaaS。

## 四、现在还不能下的结论

- 不能说迁到子域会直接提升 Google 排名；Google 官方明确不偏好子域或子目录。
- 不能说 OpenAI 插件目录支持付费安装、按调用分成或销售 RepoCover 数字服务；当前文档没有前两者，后者被明确禁止。
- 不能假设中国大陆居民可以直接收取 GitHub Sponsors，也不能假设 fiscal host 自动绕过地区限制。
- 不能用相邻 SaaS 的标价推导 RepoCover 的成交价或收入规模。
- 不能只凭“用户觉得图很好看”推断商业需求；真正信号是设置为 Social Preview、愿意公开背书、愿意付费、愿意再次购买或提出团队需求。

## 最终建议

- **域名：** 有可靠逐页永久重定向能力就尽早迁到 `repo-cover.onovich.com`；没有就暂缓，不为虚假的 SEO 加成冒险。
- **案例：** 保留视觉图库，但把首页和重点案例换成真正公开、可核验、最好可试用且已采用封面的仓库。
- **盈利：** 把免费 Skill 和插件目录当获客，把一次性人工复核服务当第一项付费实验；Sponsors 仅在地区资格成立时作为辅助；有重复团队需求后再做托管产品。

所有平台规则与价格均以 2026-08-14 可访问页面为准。OpenAI 插件商业政策、GitHub Sponsors 地区和 SaaS 价格都可能变化，执行前应再次核对。
