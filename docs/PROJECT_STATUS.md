# Project status

Last updated: 2026-08-14.

## Current state

- Canonical repository: `https://github.com/onovich/RepoCover`
- Canonical local workspace: `D:\Skills\RepoCover`
- Product name: `RepoCover`
- Installable skill: `skill/repo-cover`
- Invocation: `$repo-cover`
- License: MIT
- Initial implementation migrated from the locally tested `github-preview` skill.

RepoCover now supports:

- one local repository or an authenticated remote-only repository;
- portfolio inventory and screening before bulk generation;
- empty, boilerplate, and extremely incomplete repository detection, including Unity-specific boilerplate discounting;
- source-quality diagnosis, selective extraction, bounded reconstruction, and seam-integrity review;
- first-use cold-start composition when no usable cover, screenshot, brand mark, or primary visual exists;
- versioned candidates, no-regression scoring, and reversible promotion;
- exact editable SVG, `1280×640` PNG under 1 MB, and light/dark `320×160` review sheets;
- separately authorized GitHub upload and public `og:image` verification.

## Validation evidence

### Portable public examples

Eight checked-in PNGs cover distinct repository and evidence types:

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

1. Perform a clean installation from the public GitHub path into a disposable destination.
2. Run remote CI on Linux, Windows, and macOS for the current skill structure and expanded example set.
3. Decide the next release version, write release notes around portfolio triage, source diagnosis, cold-start inference, and no-regression versioning, then tag only after CI passes.
4. Set or refresh the repository description, topics, and social preview; verify the public `og:image` after upload.
5. Collect independent-user examples before treating the owner-run portfolio result as general external validation.

## Known limitations

- The skill depends on an existing rasterizer such as Sharp; it intentionally does not install dependencies without permission.
- Visual quality still requires model judgment and human review; mechanical validation cannot prove taste.
- Authenticated private-repository inspection depends on the connected GitHub access available to the active environment.
- Remote-static evidence cannot prove runtime behavior, builds, scenes, or tests.
- GitHub social-preview upload has no stable repository API in this project and remains a manual or browser-assisted step.
- The 63-repository regression is owner-run; independent-user evidence is still needed.
