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

### 2. Independent domain — implementation complete, switch pending

- Target domain: `https://repo-cover.onovich.com/`
- The site now reads its public origin from one configuration file.
- Canonical URLs, `hreflang`, Open Graph URLs, JSON-LD, robots, sitemap, README links, plugin links, and campaign links are prepared for the new domain.
- The build rejects unresolved URL tokens and references to the retired public origin.
- External DNS, GitHub Pages binding, HTTPS, and permanent redirects still need to be switched together.

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

## Domain switch handoff

Perform these steps only after the new site build has been pushed successfully.

### GitHub Pages

1. Open `onovich/RepoCover` → **Settings** → **Pages**.
2. Set **Custom domain** to `repo-cover.onovich.com` and save.
3. GitHub Pages uses an Actions workflow here, so no `CNAME` file is required.

### Cloudflare DNS

Create this record:

| Type | Name | Target | Proxy status | TTL |
| --- | --- | --- | --- | --- |
| CNAME | `repo-cover` | `onovich.github.io` | DNS only during certificate setup | Auto |

Wait until `https://repo-cover.onovich.com/` loads correctly and GitHub allows **Enforce HTTPS**. Then enable HTTPS in GitHub Pages.

### Old URL redirect

The redirect is activated only after the new hostname works.

1. In Cloudflare DNS, change the existing `blog` web record to **Proxied** so redirect rules can see its traffic.
2. Open **Rules** → **Redirect Rules** → **Single Redirects**.
3. Create `RepoCover domain migration` with:
   - Match type: **Wildcard pattern**
   - Request URL: `https://blog.onovich.com/RepoCover*`
   - Target URL: `https://repo-cover.onovich.com${1}`
   - Status: **301 Permanent Redirect**
   - Preserve query string: **Enabled**
4. Check the old homepage, Chinese homepage, examples page, guide, one image, and one URL containing UTM parameters.

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
