# RepoCover promotion roadmap

Last updated: 2026-08-14.

## Goal

Use RepoCover as a useful open-source project that introduces onovich and leads interested developers toward the wider project portfolio. Monetization is not a current objective.

The primary path is:

`search or social post → RepoCover site → useful case → GitHub repository or onovich profile`

## Current progress

### 1. GitHub foundation — complete

- Repository name, description, topics, license, README, Social Preview, and first release are present.
- English and Simplified Chinese documentation are available.
- The website and repository identify onovich as the author.

### 2. Independent domain — deployed, HTTPS provisioning

- Target domain: `https://repo-cover.onovich.com/`
- The site now reads its public origin from one configuration file.
- Canonical URLs, `hreflang`, Open Graph URLs, JSON-LD, robots, sitemap, README links, plugin links, and campaign links now use the new domain.
- The build rejects unresolved URL tokens and references to the retired public origin.
- Cloudflare DNS and the GitHub Pages custom domain are active, and the new build has deployed successfully.
- Both Cloudflare authoritative nameservers and GitHub's Pages health check now validate the CNAME. GitHub is still provisioning the dedicated HTTPS certificate.
- GitHub currently returns one-to-one `301` redirects from the old homepage, Chinese page, examples, guide, images, and parameterized URLs while preserving the path and query string.

### 3. Examples — first complete case ready

- `Research` is the first featured case because it has a useful public repository, a working product, a recognizable interface, and a clear before-to-result design decision.
- Eight earlier covers remain below it as a visual-range gallery.
- The next featured case will be selected only after its repository name, public description, live product link, and source material are internally consistent.

Next candidates, in order:

1. `LitPng`: resolve the `LitPng` / `LittlePNG` naming mismatch before publication.
2. `Inscape`: complete public repository metadata and a stable product/demo link.
3. `RepoPalette`: confirm the source repository and live product path before writing the case.

### 4. Launch material — ready for review

- Channel-specific images exist for X, LinkedIn, Chinese social feeds, and Product Hunt.
- English and Chinese launch copy, Show HN copy, community drafts, image descriptions, and UTM links are collected in `docs/LAUNCH_KIT.md`.
- A follow-up post uses the Research case to promote both RepoCover and another useful onovich project.

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

Keep this record DNS-only. When GitHub finishes issuing the certificate, enable HTTPS enforcement and recheck the complete public site.

### Old URL redirects

No Cloudflare redirect rule is currently necessary. After the Pages custom domain was saved, GitHub began returning permanent redirects from `https://blog.onovich.com/RepoCover/...` to the equivalent path on `repo-cover.onovich.com` and preserved query strings.

Keep the existing `blog` CNAME DNS-only. Recheck the redirect set after HTTPS enforcement and during later site reviews. Use a Cloudflare wildcard redirect only as a fallback if GitHub stops preserving these paths or queries; proxying the entire blog solely for a redundant redirect would add unnecessary risk.

Keep the redirect for at least one year. Do not remove the old hostname from search tools immediately.

## Publishing order

1. Finish the domain switch and live validation.
2. Update the GitHub repository homepage field to the new domain.
3. Submit both sitemaps/domain properties to Google Search Console if available.
4. Pin RepoCover and Research on the onovich GitHub profile.
5. Publish the general launch post with the visual-range image.
6. Publish the Research case follow-up several days later.
7. Submit to Show HN after the site and installation flow have survived real visits.
8. Use early questions to improve the README and site before considering Product Hunt.

Public posts and profile pinning remain manual review actions. Do not publish, vote, or comment automatically.

## What to measure

Review after 7, 30, and 90 days:

- GitHub repository unique visitors and referring sites;
- clones and stars as signs of genuine project interest;
- visits to the onovich profile and featured-case repositories;
- Search Console impressions and clicks for `github social preview`, `github repository cover`, `AI repository cover`, and Chinese equivalents;
- traffic by the UTM sources in the launch kit;
- installation questions, issue quality, and independent examples.

The useful result is not maximum impressions. It is more qualified visitors reaching RepoCover, understanding the work, and continuing into the wider onovich portfolio.
