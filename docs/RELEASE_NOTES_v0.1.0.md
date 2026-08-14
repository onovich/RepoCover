# RepoCover v0.1.0 — public beta

RepoCover is an open-source Codex Skill that reads a repository before designing its GitHub Social Preview.

## What ships

- Evidence-first inspection of local or remote repositories, with explicit limits when no runtime can be reached.
- Source-material diagnosis for screenshots, working interfaces, logos, illustrations, SVGs, sprites, textures, and other repository-owned visuals.
- Cold-start composition when no useful screenshot, logo, hero image, or previous cover exists.
- Project-specific composition that preserves palette, subject, dimensionality, material, and visual roles instead of applying one template.
- Editable SVG plus an exact `1280×640` PNG under GitHub's 1 MB limit.
- Full-size and `320×160` review on light and dark surroundings.
- Separately authorized GitHub upload and public `og:image` verification.
- A skills-only Codex plugin package at the repository root.
- An English and Simplified Chinese GitHub Pages site with examples, a Social Preview guide, support, privacy, and terms pages.

## Validation

- All repository checks pass locally.
- Canonical and packaged Skill directories pass the Skill validator.
- The root plugin passes the plugin validator.
- Nine checked-in preview images pass exact-dimension and file-size checks.
- The public example set spans product UI, 3D identity, character art, audio workflow, semantic topology, geometric relations, cold-start inference, and weak-source reconstruction.
- The project owner accepted the latest selected cover for each repository in a 63-repository regression. This is owner-run acceptance evidence, not an independent benchmark.

## Known limits

- The Skill needs an available rasterizer such as Sharp and does not silently install dependencies.
- A remote file tree cannot prove runtime behavior, builds, scenes, or tests.
- Mechanical validation cannot replace human taste review.
- Independent-user evidence is still limited, so this release is marked public beta.

## Install

```text
Use $skill-installer to install onovich/RepoCover from skill/repo-cover.
```

Then restart Codex and ask:

```text
Use $repo-cover to understand this project and create a validated GitHub Social Preview.
```
