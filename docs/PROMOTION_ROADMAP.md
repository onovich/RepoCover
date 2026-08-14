# RepoCover promotion roadmap

Last updated: 2026-08-14.

## Goal

Use RepoCover as a useful open-source project that introduces onovich and leads interested developers toward the wider project portfolio. Monetization is not a current objective.

The primary path is:

`search or social post → RepoCover site → RepoCover GitHub repository`

## Current progress

### 1. GitHub foundation — complete

- Repository name, description, topics, license, README, Social Preview, and first release are present.
- English and Simplified Chinese documentation are available.
- The website identifies onovich as the author without adding a separate promotional profile link.

### 2. Independent domain — complete

- Target domain: `https://repo-cover.onovich.com/`
- The site now reads its public origin from one configuration file.
- Canonical URLs, `hreflang`, Open Graph URLs, JSON-LD, robots, sitemap, README links, plugin links, and campaign links now use the new domain.
- The build rejects unresolved URL tokens and references to the retired public origin.
- Cloudflare DNS and the GitHub Pages custom domain are active, and the new build has deployed successfully.
- Both Cloudflare authoritative nameservers and GitHub's Pages health check validate the CNAME. GitHub's dedicated certificate is active and HTTPS enforcement is enabled.
- GitHub currently returns one-to-one `301` redirects from the old homepage, Chinese page, examples, guide, images, and parameterized URLs while preserving the path and query string.

### 3. Examples — neutral gallery ready

- Nine covers appear at the same level; no owner project is labelled as a featured or especially valuable case.
- Every card opens the corresponding public GitHub repository so visitors can inspect it without extra promotional framing.
- `Research` now uses a reconstructed bilingual editorial spread instead of a webpage screenshot.
- Future additions should improve the range of project types, and independent-user examples should take priority when available.

### 4. Launch material — ready for review

- Channel-specific images exist for X, LinkedIn, Chinese social feeds, and Product Hunt.
- English and Chinese launch copy, Show HN copy, community drafts, image descriptions, and UTM links are collected in `docs/LAUNCH_KIT.md`.
- Launch copy points to the gallery as a whole rather than promoting one owner project as a special case.

## Domain switch record

The following settings were applied on 2026-08-14.

### GitHub Pages

- Custom domain: `repo-cover.onovich.com`
- Build type: GitHub Actions workflow
- No repository `CNAME` file is required.

### Cloudflare DNS

Active record:

| Type | Name | Target | Proxy status | TTL |
| --- | --- | --- | --- | --- |
| CNAME | `repo-cover` | `onovich.github.io` | DNS only during certificate setup | Auto |

Keep this record DNS-only. The complete public site has been checked through HTTPS, including both languages, examples, the guide, the Research image, and the sitemap.

### Old URL redirects

No Cloudflare redirect rule is currently necessary. After the Pages custom domain was saved, GitHub began returning permanent redirects from `https://blog.onovich.com/RepoCover/...` to the equivalent path on `repo-cover.onovich.com` and preserved query strings.

Keep the existing `blog` CNAME DNS-only. Recheck the redirect set after HTTPS enforcement and during later site reviews. Use a Cloudflare wildcard redirect only as a fallback if GitHub stops preserving these paths or queries; proxying the entire blog solely for a redundant redirect would add unnecessary risk.

Keep the redirect for at least one year. Do not remove the old hostname from search tools immediately.

## Publishing order

1. Domain switch and live validation — complete.
2. GitHub repository homepage field — updated to the new domain.
3. Submit the new sitemap/domain property to Google Search Console if available.
4. Pin RepoCover on the onovich GitHub profile.
5. Publish the general launch post with the visual-range image.
6. Submit to Show HN after the site and installation flow have survived real visits.
7. Use early questions to improve the README and site before considering Product Hunt.

Public posts and profile pinning remain manual review actions. Do not publish, vote, or comment automatically.

## What to measure

Review after 7, 30, and 90 days:

- GitHub repository unique visitors and referring sites;
- clones and stars as signs of genuine project interest;
- clicks from the example gallery to public repositories;
- Search Console impressions and clicks for `github social preview`, `github repository cover`, `AI repository cover`, and Chinese equivalents;
- traffic by the UTM sources in the launch kit;
- installation questions, issue quality, and independent examples.

The useful result is not maximum impressions. It is more qualified visitors reaching RepoCover, understanding the work, and continuing into the wider onovich portfolio.
