# Contributing

Thank you for improving RepoCover.

## Before changing the skill

1. Read [`AGENTS.md`](AGENTS.md) and [`skill/repo-cover/SKILL.md`](skill/repo-cover/SKILL.md).
2. Keep the installable skill focused; public project documentation belongs at the repository root or under `docs/`.
3. Preserve exact `1280×640` output, the 1 MB ceiling, editable SVG delivery, evidence-based claims, and explicit upload authorization.
4. Add reusable instructions only when they address a demonstrated failure or recurring workflow.
5. Read [`docs/REGRESSION_BASELINE.md`](docs/REGRESSION_BASELINE.md) before changing visual judgment, source treatment, cold-start inference, or version-promotion rules.

## Validate

```text
python scripts/check.py
```

For a visual change, forward-test against repositories with different product and evidence types, inspect the full raster plus the light/dark `320×160` review sheet, and use a contact sheet for batches. Do not claim the complete owner-run portfolio was rerun unless it actually was.

## Pull requests

Keep changes scoped. Explain the observed problem, the reusable rule or tooling change, the repositories used for validation, and any remaining limitation.
