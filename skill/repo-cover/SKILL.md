---
name: repo-cover
description: RepoCover creates or refreshes polished GitHub Social Preview images for local or remote repositories, with project-specific visual language, an editable source, exact 1280×640 output, a compressed raster under GitHub's 1 MB limit, and optional upload verification. Use when the user asks for a repository cover, GitHub Social Preview, repository Open Graph or OG image, link-share card, or a stronger visual when sharing a project, including cases with useful screenshots or brand assets and cold starts with no existing hero image.
---

# RepoCover

Create a repository-specific social preview that remains legible at thumbnail size. Prefer deterministic, editable composition over a generic generated banner.

## Product invariants

- Deliver an exact `1280×640` raster, normally PNG, under `1,000,000` bytes.
- Keep an editable source, normally SVG, beside the raster.
- Ground visible claims, metrics, screenshots, and proof in repository evidence.
- Preserve the repository's identity instead of imposing one house style.
- Validate full size and `320×160` on light and dark surroundings.
- Treat image creation and GitHub upload as separate authorization boundaries.
- Do not imply GitHub affiliation or endorsement.

## Load the right references

Read these two files for every cover:

- [`references/common-quality.md`](references/common-quality.md) for universal composition and rejection gates.
- [`references/design-ledger-template.md`](references/design-ledger-template.md) for the evidence, design, and validation record.

Then read only the route that applies:

- Read [`references/source-material.md`](references/source-material.md) when screenshots, runtime captures, logos, illustrations, SVGs, sprites, textures, or other meaningful visuals exist.
- Read [`references/cold-start.md`](references/cold-start.md) when no usable screenshot, runtime capture, brand mark, or repository-owned primary visual exists.
- Read [`references/version-regression.md`](references/version-regression.md) when refreshing an existing cover, comparing candidates, or generating a versioned batch.

Do not load an irrelevant route merely because it exists. `references/design-recipes.md` is only a compatibility index for older prompts.

## Workflow

### 1. Inspect and bound the evidence

Read applicable `AGENTS.md` files, the README, package metadata, meaningful source paths, visual assets, and any existing social preview. Identify:

- repository name and primary user task;
- one concrete value statement;
- at most three proof points;
- the strongest product evidence;
- established visual identity and secondary facts to exclude;
- evidence mode: `remote-static`, `local-static`, `build-tested`, or `runtime-tested`.

Never imply that a build, runtime, scene, or test was executed when only static evidence was inspected. If GitHub's image requirements might have changed, verify them against official GitHub documentation.

For a remote repository, use the available public or authenticated GitHub evidence to inspect its README, tree, manifests, meaningful source files, current preview, and strongest visual assets. Keep outputs in a durable user-facing directory and record source URLs and claim boundaries. If no runtime or representative interface can be reached, state that limitation instead of pretending the remote evidence is equivalent to a working local preview. Previewable local projects, especially web projects with an existing interface, usually provide the richest visual evidence.

### 2. Write the ledger and choose the route

Create a design ledger from the bundled template before drawing. At minimum record:

- **Promise, proof, exclude**;
- evidence mode and claim boundaries;
- source-material diagnosis or cold-start semantic skeleton;
- aspect-fit diagnosis whenever source pixels may be embedded;
- chosen production and interpretation route;
- material, asset-role, topology, and line decisions;
- output version, validation, and promotion verdict when applicable.

Choose the smallest production route that preserves identity:

- **Code-native SVG — preferred:** developer tools, diagrams, charts, logos, libraries, and inferred visual systems.
- **Screenshot or source hybrid:** only when a self-contained source artifact remains the clearest proof after diagnosis.
- **Illustration hybrid:** only when illustration is central to the repository's identity; generate artwork without important text and overlay exact wording in SVG.

Do not invoke image generation merely to imitate an established vector system.

### 3. Build and version the editable source

Default to `docs/social-preview.svg` and `docs/social-preview.png` unless the repository has a clear asset convention or the user names another destination.

- Use a `1280 640` viewBox and a full-canvas background.
- Keep essential content inside a roughly 72 px outer safe area.
- Partition copy, product proof, captions, and signature into non-overlapping regions.
- Use system fonts unless the repository ships an appropriate licensed font.
- Embed local evidence or reproduce it with deterministic SVG primitives; avoid external runtime dependencies.
- Clip charts, screenshots, repeated marks, and waveforms to their owning regions.
- Do not `contain` a narrow screenshot inside a wide proof frame when this creates two inert gutters; crop, extend one continuous scene, or extract and recompose the useful material.
- Preserve an existing cover and create a versioned sibling unless replacement is explicitly requested.

### 4. Render and validate mechanically

Render with the bundled script when Sharp is available:

```text
node <skill-directory>/scripts/render_svg.mjs <source.svg> <output.png>
```

Use `--force` only when replacing the named output is in scope. In Codex Desktop, load workspace dependencies and use the returned Node executable and package path through `NODE_PATH`; do not install a dependency without permission.

Validate the PNG and SVG:

```text
python <skill-directory>/scripts/validate_preview.py <output.png> --svg <source.svg>
```

Create the standard thumbnail sheet:

```text
node <skill-directory>/scripts/create_review_sheet.mjs <preview.png> <review.png>
```

On Windows legacy code pages, set `PYTHONUTF8=1` for tooling that reads UTF-8 source.

### 5. Validate visually

Inspect the raster at full size and inspect the generated review sheet. Confirm:

- repository name and value statement remain readable at `320×160`;
- the product proof is recognizable and technically faithful;
- text, marks, crops, panels, and decorative elements do not collide or clip;
- the composition works on light and dark surroundings;
- every visible element maps to the promise or proof;
- the design passes every applicable route-specific veto.

Scan left-to-right and top-to-bottom, fix one named defect at a time, rerender, and rerun validation. Do not hand off a known defect.

For batches, create a contact sheet and inspect for accidental shared-template drift before promoting candidates.

### 6. Upload only when requested

Creating an asset does not authorize changing GitHub settings. When upload is explicitly requested, open:

```text
https://github.com/<owner>/<repo>/settings
```

Use **Social preview → Edit → Upload an image…** and follow the active UI confirmation policy. After upload, fetch the public repository page and verify that `og:image` resolves to the new `1280×640` image. Do not report success from the settings thumbnail alone.

## Handoff

Show the final image and report:

- editable source path;
- raster path, format, dimensions, and byte size;
- one-sentence design rationale;
- validation and version-promotion status;
- upload status: not requested, pending, or publicly verified.

Do not leave project-bound output only in a temporary or model-owned directory.
