# Release checklist

## Skill integrity

- [ ] `python scripts/check.py` passes locally.
- [ ] GitHub Actions passes on Linux, Windows, and macOS.
- [ ] `SKILL.md` and `agents/openai.yaml` are UTF-8 without BOM.
- [ ] `name: repo-cover`, `display_name: RepoCover`, and `$repo-cover` agree.
- [ ] The installable directory contains no repository-only documentation.
- [ ] `SKILL.md` routes to `common-quality.md`, `source-material.md`, `cold-start.md`, `version-regression.md`, and `design-ledger-template.md` without requiring every route for every task.
- [ ] Every relative Markdown link in the installable skill resolves.

## Behavior

- [ ] A clean install from `onovich/RepoCover`, path `skill/repo-cover`, succeeds.
- [ ] At least one code-native SVG route renders and validates.
- [ ] Review-sheet generation succeeds and refuses accidental overwrite without `--force`.
- [ ] A meaningful skill change is forward-tested on varied repositories.
- [ ] No test output contains unsupported product claims or unlicensed assets.
- [ ] Cold-start testing does not assume a previous cover exists.
- [ ] Existing-cover testing preserves versioned siblings and records a post-inspection promotion verdict.
- [ ] Source-material testing checks identity anchors, fragment closure, seam integrity, dimensionality, and asset roles.
- [ ] Batch testing includes a contact-sheet review for repeated template grammar.

## Public repository

- [ ] README quick start matches the released ref.
- [ ] English and Chinese README capability and validation claims agree.
- [ ] `docs/PROJECT_STATUS.md` and `docs/REGRESSION_BASELINE.md` describe the current accepted evidence without exposing private repository identities.
- [ ] Repository description and topics are current.
- [ ] Social preview is uploaded and its public `og:image` is verified.
- [ ] GitHub affiliation disclaimer is visible.
- [ ] Release notes explain user-facing changes and validation evidence.
- [ ] Tag and source commit are immutable and documented.
