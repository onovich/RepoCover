# Codex Operations Workflow

RepoCover has no dependency installation or long-running service. Its main project operation is:

```powershell
python scripts/check.py
```

That check validates skill metadata, UTF-8 without BOM, Python and JavaScript syntax, all bundled examples, and the repository social preview. Run it after any instruction, script, metadata, or preview change.

For a public release, also complete `docs/RELEASE_CHECKLIST.md` and perform a clean install from the GitHub subdirectory `skill/repo-cover`.
