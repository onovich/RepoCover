# GitHub social-preview skill branding research

Research snapshot: 2026-08-13.

## Recommendation

Use **RepoCover** as the public product brand.

- Product brand and UI display name: `RepoCover`
- GitHub repository: `onovich/RepoCover`
- Codex skill folder and invocation: `repo-cover` / `$repo-cover`
- Compatibility language during migration: `formerly GitHubPreview`
- One-line positioning: `Create polished, repository-specific social previews from real project evidence.`
- Search-oriented repository description: `A Codex skill that creates polished 1280×640 GitHub repository social preview and Open Graph images from real project assets.`

Keep **GitHub social preview**, **repository social preview**, **Open Graph image**, and **OG image** in the description, README headings, topics, and examples rather than in the primary brand.

## Why not GitHubPreview

`GitHubPreview` is understandable but weak as a long-term brand:

1. It is generic and ambiguous: “GitHub preview” can refer to README rendering, pull-request preview environments, HTML preview, GitHub Pages preview, or social-preview images.
2. GitHub repository search found two exact unpunctuated `GitHubPreview` names and at least 18 punctuation-equivalent names. The broad `github preview in:name` query returned 1,076 results in the dated API snapshot. See the [first-party API query](https://api.github.com/search/repositories?q=GitHubPreview%20in%3Aname&per_page=100) and [GitHub web search](https://github.com/search?q=GitHubPreview+in%3Aname&type=repositories).
3. An established project, [`kei-s/github-preview`](https://github.com/kei-s/github-preview), already owns part of the phrase’s search intent for README previewing.
4. Putting `GitHub` directly into the brand increases the need to avoid any suggestion that the project is made or endorsed by GitHub. GitHub’s official brand guidance says third-party projects must not imply affiliation and must not use a GitHub logo as their own product logo: [GitHub Brand Toolkit](https://brand.github.com/foundations/logo), [GitHub Trademark Policy](https://docs.github.com/en/site-policy/content-removal-policies/github-trademark-policy).

## Why RepoCover

- **Immediate meaning:** a cover for a repository is understandable without knowing “OG image.”
- **Brandable:** shorter and more distinctive than a purely descriptive phrase.
- **Extensible:** the name can later cover repository social previews, README hero images, release cards, or Marketplace visuals without promising those features today.
- **Portfolio fit:** it sits naturally beside RepoPalette without sounding like the same product.
- **Low observed collision:** the dated GitHub API scan returned two `repocover in:name` matches and no exact public repository name. A broader web search found generic uses of the phrase but no clearly established same-purpose product. Name availability remains a snapshot, not a legal clearance.
- **SEO separation:** the brand remains memorable while the description carries precise intent words. GitHub explicitly recommends repository topics to help people find projects, and treats the README as the primary explanation surface: [repository topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics), [README guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes).

## Alternatives

| Name | Verdict | Tradeoff |
| --- | --- | --- |
| `RepoCover` | Recommended | Clear, low observed collision, and expandable; “cover” must be paired once with “social preview” in the tagline. |
| `RepoSlate` | Premium fallback | Distinctive and visually sophisticated, but unclear without explanation. |
| `RepoPoster` | Visual fallback | Memorable and nearly collision-free in the observed GitHub scan, but sounds more promotional and less like an exact 2:1 repository preview. |
| `PreviewForge` | Tooling fallback | Conveys making and craft, but has existing exact/punctuation-equivalent projects and does not say “repository.” |
| `RepoPreview` | Descriptive fallback | Easy to understand but already has an old direct exact-name competitor and remains semantically broad. |

Avoid `RepoCard`, `SocialPreview`, `ShareCard`, `OGPreview`, and `RepoOG`: first-party search found crowded or actively occupied same-purpose namespaces.

## Public identity

Recommended README opening:

> # RepoCover
>
> Create polished GitHub repository social previews from real project evidence.
>
> RepoCover inspects a repository’s README, screenshots, logos, and design tokens; produces an editable SVG plus an exact 1280×640 PNG; and validates the result at full size and thumbnail size.

Suggested topics:

`codex-skill`, `github-social-preview`, `open-graph-image`, `og-image`, `repository-branding`, `svg`, `developer-tools`, `social-card`, `design-automation`

GitHub’s official specification recommends 1280×640 for best display, accepts PNG/JPG/GIF under 1 MB, and warns that solid backgrounds are safer across platforms: [GitHub social-preview documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview).

Use an original RepoCover logo and state in the README footer:

> RepoCover is an independent open-source project and is not affiliated with or endorsed by GitHub, Inc. GitHub is a trademark of GitHub, Inc.

## Migration

For the first public release:

1. Publish under `onovich/RepoCover`.
2. Rename the skill metadata to `repo-cover` and UI display name to `RepoCover`.
3. Mention `formerly GitHubPreview` only for the first one or two releases.
4. Keep a thin local `github-preview` compatibility alias only if existing users already invoke it; new documentation should use `$repo-cover` exclusively.
5. Promote the differentiated workflow—repository evidence, editable SVG, exact GitHub dimensions, thumbnail review, and validation—not merely “AI makes a banner.”

This research is a naming and search assessment, not trademark registration advice. Recheck repository/account availability immediately before creating the public repository.
