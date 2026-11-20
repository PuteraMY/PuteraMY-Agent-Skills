# 2026-11-20 — CI run evidence and upstream-only triage

Scope: non-destructive audit; no vendor file has been replaced or installed by this checkpoint. Evidence is scoped to the exact branch SHA and Actions job below.

## Verified repository state
- Branch: `audit/2026-11-17-ci-root-cause`; starting SHA: `1cdc65f1df702f8883f18d3d7d5a17ce9b2e0b8f`.
- Recursive Git tree: 155 entries, 101 blobs, `truncated=false`. Main at `cae3aa2bce5f86ffe03bfa0d84523cd64c936979`: 139 entries, `truncated=false`.
- Latest examined run: https://github.com/PuteraMY/PuteraMY-Agent-Skills/actions/runs/44715978152 — completed failure; job `136219367545`, step `Run python3 scripts/validate_skills.py`, exit 1.
- Validator reports **43 directories, 8 structural failures, 101 tracked files**.

## Exact eight validation failures
All reported `missing or malformed SKILL.md frontmatter`:
`context7-documentation`, `playwright-testing`, `strix-security-audit`, `supabase-agent-plugin`, `superdesign-skill`, `taste-skill`, `ui-craft`, `ux-ui-agent-skills`.

These are **structural** failures, not proof that each named package is a genuine standalone skill. Do **not** manufacture frontmatter or a `SKILL.md` to make CI green. First classify each entry from the original vendor distribution as standalone skill, plugin, MCP server, connected app, or unresolved; record the pinned upstream commit/tag, license, complete package boundaries, manifests, scripts and support files. Validate each type against its own contract. An upstream plugin or MCP package need not contain a standalone skill file.

## Verification gates and blockers
1. ATLAS AI priority: inspect Taste Skill, UI Craft, Superdesign and relevant testing/animation dependencies; retrieve complete licensed upstream distribution at pinned revisions before changing tracked content.
2. For every retained entry: provenance URL and immutable revision; original license; original manifest; complete required files; verified vendor install/discovery instructions; integrity checks; actual functional test evidence.
3. Runtime checks must be **separate**: repository-present, Codex installed/discovered, ChatGPT Work available/connected, and successful invocation. No inference from a GitHub folder or ChatGPT plugin listing.
4. Preserve pseudo-skill content pending approved replacement strategy; where no legitimate upstream exists, mark `UNRESOLVED` and seek approval before archival/removal.
5. VELA and future projects remain in scope after contest-critical triage. No production deploy, merge, or destructive action.

## Next check
Read complete upstream manifests, licenses and vendor instructions; implement type-aware validation without suppressing genuine errors; rerun CI and attach logs. This checkpoint records evidence only, not a claim of repaired CI or runtime installation.
