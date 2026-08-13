---
name: repo-cover
description: RepoCover creates or refreshes polished GitHub repository social preview images with project-specific visual language, an editable source, exact 1280×640 output, a compressed raster under GitHub's 1 MB limit, and optional upload verification. Use when the user asks for a GitHub social preview, repository Open Graph or OG image, link-share card, GitHub Settings preview image, or an improvement to how a repository looks when shared.
---

# RepoCover

Create a repository-specific social preview that remains legible at thumbnail size. Prefer a deterministic vector composition over a generic AI-generated banner.

## Core requirements

- Deliver an exact `1280×640` raster; use PNG by default.
- Keep the raster under `1,000,000` bytes.
- Use a solid background unless transparency is an intentional, tested requirement.
- Keep an editable source, normally SVG, beside the raster.
- Use only verified product claims, screenshots, metrics, and features.
- Preserve the repository's own identity instead of applying one house style to every project.
- Make every visible element reinforce the primary promise or one selected proof point. A factual repository feature can still be irrelevant to the preview.

Before designing, read [`references/design-recipes.md`](references/design-recipes.md) completely.

## Workflow

### 1. Inspect the repository

Read applicable `AGENTS.md` files, the README, package metadata, existing logos, screenshots, design tokens, generated graphics, and any current social-preview asset. Identify:

- repository name;
- the primary user task and product promise;
- one concrete value statement;
- at most three proof points;
- the strongest real product visual;
- the established palette, typography, spacing, and shape language;
- secondary facts to exclude because they would distract from the primary promise.

If GitHub's image requirements might have changed, verify them against official GitHub documentation before working.

### 2. Choose the production route

Use the smallest route that preserves the product's identity:

- **Code-native SVG — preferred:** use for developer tools, charts, diagrams, logos, and repositories with an existing vector or UI system.
- **Screenshot hybrid:** crop a real product screenshot and place exact vector typography around it. Do not redraw a usable screenshot with AI.
- **Illustration hybrid:** use image generation only when illustration is central to the product identity. Generate artwork without important text, then overlay all wording in SVG.

When an established vector system exists, do not invoke image generation merely to imitate it.

### 3. Define the message

Before drawing, write a compact content ledger:

- **Promise:** the one outcome the image must communicate.
- **Proof:** the one product artifact and up to three facts that support it.
- **Exclude:** true but secondary features, integrations, or implementation details that must not appear.

If a visible element cannot be mapped to the promise or proof list, remove it.

Use this hierarchy:

1. Repository name.
2. One short, concrete value statement.
3. Two or three short proof points when they add information.
4. Optional repository URL or quiet brand signature.

Avoid feature inventories, installation instructions, badges, star counts, and claims that are not proven by repository evidence.

### 4. Build the editable source

Default to `docs/social-preview.svg` and `docs/social-preview.png` unless the repository already has a clear asset convention or the user names a destination.

- Use `apply_patch` for project files.
- Use a `1280 640` viewBox and a full-canvas background.
- Keep essential content inside a roughly 72 px outer safe area.
- Partition copy, product proof, captions, and the quiet signature into explicit non-overlapping regions before adding detail.
- Use system font stacks unless the repository already ships an appropriate licensed font.
- Embed local visual evidence or reproduce it with deterministic SVG primitives.
- Avoid external image, font, filter, or stylesheet dependencies.
- Clip charts, waveforms, screenshots, and repeated marks to their panel or plot bounds. Keep peak marks inside roughly 70–80% of plot height unless the underlying data requires a different scale.
- Preserve an existing asset or create a versioned sibling unless replacement is requested.

### 5. Render the raster

Use the bundled renderer when Sharp is available:

```text
node <skill-directory>/scripts/render_svg.mjs <source.svg> <output.png>
```

Add `--force` only when replacing the named raster is in scope. If Sharp is not directly importable, locate the configured workspace dependencies and set `NODE_PATH` to their Node package directory. Do not install a new dependency without permission.

In Codex Desktop, call `codex_app__load_workspace_dependencies` and use the returned **Node.js packages** path as `NODE_PATH`, then run the returned Node.js executable. Outside Codex Desktop, prefer a project-provided Sharp installation or another already available trusted SVG renderer.

### 6. Validate mechanically

Run:

```text
python <skill-directory>/scripts/validate_preview.py <output.png> --svg <source.svg>
```

On Windows environments whose Python defaults to a legacy code page, set `PYTHONUTF8=1` for skill tooling that reads the UTF-8 Markdown or SVG source.

The validator checks the raster signature, exact dimensions, file-size limit, and the SVG canvas and accessible title/description.

Create the standard thumbnail review sheet:

```text
node <skill-directory>/scripts/create_review_sheet.mjs <preview.png> <review.png>
```

The sheet shows the exact `320×160` preview on both light and dark surroundings. Add `--force` only when replacing the review artifact is in scope.

### 7. Validate visually

Inspect the final raster with the local image viewer at full size and as a small thumbnail. Confirm:

- repository name and value statement are readable at about `320×160`;
- the product visual remains recognizable;
- all text is exact and uncropped;
- contrast, alignment, spacing, and visual weight are intentional;
- no corner, circle, chart, or screenshot is accidentally clipped;
- no text block, caption, URL, chart mark, or decoration collides with another region;
- every secondary element is relevant to the primary product promise rather than merely present in the repository;
- charts retain quiet internal margins and do not use exaggerated peaks that overpower their panel;
- the result still looks correct on both light and dark surrounding pages.

Inspect both the full raster and the generated review sheet. Scan the canvas left-to-right and top-to-bottom for collisions, then compare visual weight at thumbnail size. Iterate on one concrete issue at a time, rerender, rerun the validator, and rebuild the review sheet. Do not hand off a known visual defect.

### 8. Upload only when requested

Creating the asset does not authorize changing GitHub settings. When upload is requested, open:

```text
https://github.com/<owner>/<repo>/settings
```

Use **Social preview → Edit → Upload an image…**. Current GitHub UI may save immediately once the preview appears and leave only an **Edit** button. Follow the active UI confirmation policy for the file upload.

After upload, fetch the public repository page and verify that `og:image` resolves to the new `1280×640` image. Do not report success from the settings-page thumbnail alone.

## Handoff

Show the final image and report:

- editable source path;
- raster path, format, dimensions, and byte size;
- the chosen design rationale in one sentence;
- whether upload was not requested, pending, or publicly verified.

Do not leave project-bound output only in a temporary or model-owned directory.
