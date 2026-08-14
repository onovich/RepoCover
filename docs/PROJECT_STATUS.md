# Project status

Last updated: 2026-08-14.

## Current state

- Canonical repository: `https://github.com/onovich/RepoCover`
- Canonical local workspace: `D:\Skills\RepoCover`
- Product name: `RepoCover`
- Installable skill: `skill/repo-cover`
- Invocation: `$repo-cover`
- License: MIT
- Website: `https://repo-cover.onovich.com/`
- Skills-only plugin manifest: `.codex-plugin/plugin.json`
- Initial implementation migrated from the locally tested `github-preview` skill.

RepoCover now supports:

- one local or remote repository, with explicit evidence limits when no runtime can be reached;
- source-quality diagnosis, selective extraction, bounded reconstruction, and seam-integrity review;
- first-use cold-start composition when no usable cover, screenshot, brand mark, or primary visual exists;
- versioned candidates, no-regression scoring, and reversible promotion;
- exact editable SVG, `1280×640` PNG under 1 MB, and light/dark `320×160` review sheets;
- separately authorized GitHub upload and public `og:image` verification.

The public website includes English and Simplified Chinese landing pages, a complete Research case study, eight additional visual examples, a practical GitHub Social Preview guide, support, privacy, and terms pages. GitHub Pages is deployed through the official Pages Actions workflow. The repository root is also packaged as a skills-only Codex plugin. `skill/repo-cover/` remains the single source of truth; `skills/repo-cover/` is a generated plugin-distribution copy enforced by byte-for-byte checks.

## Validation evidence

### Portable public examples

Research is the first complete public case: a useful repository with a working bilingual report product, a live website, a clear design decision, and a final RepoCover result. Eight additional checked-in PNGs cover distinct repository and evidence types:

- PrismDraft: faceted 3D modeling;
- LittlePNG: local-first browser image preparation;
- DeskMochi: desktop companion;
- AudioTrim: game-audio trimming;
- Beat: cold-start symbolic audio representation;
- JustGoal.skill: branch, parallel review, merge, gate, and fix-loop topology;
- Knot: geometric overlap and projection semantics;
- Ping: bounded reconstruction from weak runtime evidence without invented telemetry.

Every portable example passes the exact-size and file-size validator. The product preview also passes SVG accessibility validation.

### Owner-run portfolio regression

On 2026-08-14, the project owner accepted the latest selected cover for each repository in a 63-repository versioned regression spanning accessible public and private games, web projects, developer tools, libraries, utilities, and skills.

The regression covered remote-static inspection, local runtime evidence, repository-owned visual assets, screenshot extraction, weak-source reconstruction, cold-start inference, version retention, full-size review, `320×160` light/dark review, and batch contact-sheet comparison.

This is strong owner acceptance evidence, not an independent benchmark. Private repository identities and evidence remain outside the public project. See [`REGRESSION_BASELINE.md`](REGRESSION_BASELINE.md).

## Skill structure

The canonical skill uses progressive disclosure:

- `SKILL.md`: product invariants, reference routing, core workflow, rendering, validation, upload, and handoff;
- `references/common-quality.md`: universal composition and rejection gates;
- `references/source-material.md`: screenshot and repository-artifact diagnosis, extraction, reconstruction, and seams;
- `references/cold-start.md`: evidence-inferred composition without a previous cover or primary visual;
- `references/version-regression.md`: preservation contracts, candidate comparison, and promotion;
- `references/design-ledger-template.md`: reusable evidence and validation record;
- `references/design-recipes.md`: compatibility index for older prompts.

## Decisions already made

- `RepoCover` replaces `GitHubPreview` as the public brand.
- The public brand avoids implying an official GitHub product while retaining accurate search terms.
- The source repository wraps a pure installable skill under `skill/repo-cover/`.
- Every cover starts from a content ledger: Promise, Proof, and Exclude.
- Strong source identity limits the reconstruction radius; screenshots are evidence and visual dictionaries, not automatic final canvases.
- Cold-start work starts from objects, actions, topology, and outcome rather than a repository category or previous cover.
- Every repository asset receives a role before use; components, masks, textures, and backgrounds are not complete artifacts.
- Lines require semantic roles, endpoints or bounds, and evidence.
- Independent panels do not overlap unless the product relationship itself is overlap.
- Existing covers remain versioned siblings; novelty alone cannot promote a candidate.
- Uploading remains a separately authorized operation.

See [`BRAND_NAMING_RESEARCH.md`](BRAND_NAMING_RESEARCH.md) for the dated naming evidence.

## Verification

Run:

```text
python scripts/check.py
```

For renderer smoke testing, expose an existing Sharp installation through `NODE_PATH`, then run:

```text
node skill/repo-cover/scripts/render_svg.mjs docs/social-preview.svg .tmp/rendered.png
node skill/repo-cover/scripts/create_review_sheet.mjs .tmp/rendered.png .tmp/review.png
python skill/repo-cover/scripts/validate_preview.py .tmp/rendered.png --svg docs/social-preview.svg
```

For skill metadata validation, run the available `skill-creator/scripts/quick_validate.py` against `skill/repo-cover/` in an environment with PyYAML.

## Recommended next work

1. Submit and monitor the new sitemap in Google Search Console, then review the working GitHub-managed old-path redirects after 7 and 30 days as described in [`PROMOTION_ROADMAP.md`](PROMOTION_ROADMAP.md).
2. Present `LitPng` as the repository name and `LittlePNG` as the product name, then complete its public metadata and live-product prerequisite before promoting it as the next complete case.
3. Collect independent-user examples before treating the owner-run portfolio result as general external validation.
4. Record search impressions, repository traffic, and portfolio referrals after the first launch period.
5. Use external feedback to prepare a later release instead of adding features for promotion alone.

## Known limitations

- The skill depends on an existing rasterizer such as Sharp; it intentionally does not install dependencies without permission.
- Visual quality still requires model judgment and human review; mechanical validation cannot prove taste.
- Authenticated private-repository inspection depends on the connected GitHub access available to the active environment.
- Remote-static evidence cannot prove runtime behavior, builds, scenes, or tests.
- GitHub social-preview upload has no stable repository API in this project and remains a manual or browser-assisted step.
- The 63-repository regression is owner-run; independent-user evidence is still needed.
