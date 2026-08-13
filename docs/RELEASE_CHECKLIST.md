# Release checklist

## Skill integrity

- [ ] `python scripts/check.py` passes locally.
- [ ] GitHub Actions passes on Linux, Windows, and macOS.
- [ ] `SKILL.md` and `agents/openai.yaml` are UTF-8 without BOM.
- [ ] `name: repo-cover`, `display_name: RepoCover`, and `$repo-cover` agree.
- [ ] The installable directory contains no repository-only documentation.

## Behavior

- [ ] A clean install from `onovich/RepoCover`, path `skill/repo-cover`, succeeds.
- [ ] At least one code-native SVG route renders and validates.
- [ ] Review-sheet generation succeeds and refuses accidental overwrite without `--force`.
- [ ] A meaningful skill change is forward-tested on varied repositories.
- [ ] No test output contains unsupported product claims or unlicensed assets.

## Public repository

- [ ] README quick start matches the released ref.
- [ ] Repository description and topics are current.
- [ ] Social preview is uploaded and its public `og:image` is verified.
- [ ] GitHub affiliation disclaimer is visible.
- [ ] Release notes explain user-facing changes and validation evidence.
- [ ] Tag and source commit are immutable and documented.
