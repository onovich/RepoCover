# Project status

Last updated: 2026-08-13.

## Current state

- Canonical repository: `https://github.com/onovich/RepoCover`
- Canonical local workspace: `D:\Skills\RepoCover`
- Product name: `RepoCover`
- Installable skill: `skill/repo-cover`
- Invocation: `$repo-cover`
- License: MIT
- Initial implementation migrated from the locally tested `github-preview` skill.

The skill has been forward-tested on four materially different repositories:

- PrismDraft: C11 faceted 3D modeling
- LittlePNG: local-first browser image preparation
- DeskMochi: Godot desktop companion
- AudioTrim: Python/Tkinter game-audio trimming

All four reference outputs passed exact-size, file-size, SVG accessibility, content relevance, collision, clipping, full-size, and light/dark thumbnail checks. The checked-in PNGs under `examples/` are the portable evidence set.

## Decisions already made

- `RepoCover` replaces `GitHubPreview` as the public brand.
- The public brand avoids implying an official GitHub product while repository descriptions retain accurate search terms.
- The source repository wraps a pure installable skill under `skill/repo-cover/`.
- A preview must start from a content ledger: Promise, Proof, and Exclude.
- Charts and waveforms use explicit plot bounds and restrained visual amplitude.
- Text, proof, captions, and signatures occupy non-overlapping regions.
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

## Recommended next work

1. Start a fresh Codex workspace at `D:\Skills\RepoCover` and restart Codex so `@RepoCover` is discovered.
2. Review the initial logo and social preview as product-brand assets; revise them before broad promotion if desired.
3. Perform a clean installation from the public GitHub path into a disposable destination.
4. Decide the first release version, create release notes, and tag only after the remote CI passes.
5. Set the repository description, topics, and social preview; verify the public `og:image` after upload.
6. Prepare the launch post around the differentiators: repository evidence, project-specific design, editable SVG, exact output, and visual validation.
7. Collect external examples before adding more design recipes.

## Known limitations

- The skill depends on an existing rasterizer such as Sharp; it intentionally does not install dependencies without permission.
- Visual quality still requires model judgment and human review; mechanical validation cannot prove taste.
- GitHub social-preview upload has no stable repository API in this project and remains a manual or browser-assisted step.
- The four examples demonstrate breadth but are maintained by the project owner; independent-user evidence is still needed.
