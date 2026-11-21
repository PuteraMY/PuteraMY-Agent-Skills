# Audit evidence — 2026-11-21 (14:04 MYT)

## Scope and immutable evidence
- Repository: PuteraMY/PuteraMY-Agent-Skills; audit branch HEAD `5bbcd3a477b00a6ff40bba18348d2a05024a3d8f`; main HEAD `cae3aa2bce5f86ffe03bfa0d84523cd64c936979` at read time.
- GitHub recursive tree endpoint: https://api.github.com/repos/PuteraMY/PuteraMY-Agent-Skills/git/trees/5bbcd3a477b00a6ff40bba18348d2a05024a3d8f?recursive=1
- Git tree response: `truncated=false`, 157 entries total, 103 blob/file entries, 43 immediate directories under `.agents/skills/`. Git tree inventory is not upstream provenance validation.
- Latest inspected CI run: https://github.com/PuteraMY/PuteraMY-Agent-Skills/actions/runs/44853102946 ; validate job 136688849965 failed at `python3 scripts/validate_skills.py`. This is not proof that any vendor integration is broken or installed.

## Structural findings
- `scripts/validate_skills.py` still treats every immediate directory under `.agents/skills` as a standalone skill requiring frontmatter `name` and `description` in `SKILL.md`. This conflates skill, plugin, MCP and connected-app installation types.
- The tree includes license files for `anthropic-frontend-design`, `cloudflare-security-audit`, `impeccable`, `ui-ux-pro-max`, and repository-level `LICENSE`. Their presence alone does not establish complete vendor distributions or valid redistribution rights.
- No original plugin manifest was identified by the filename pattern `plugin.json` in this tree. This does **not** establish absence of plugins elsewhere or imply a plugin manifest should be invented.

## Evidence gates (not passed)
1. For each retained integration, identify canonical vendor URL, upstream commit/release, original package type, full file manifest and applicable license; compare exact upstream file bytes/hashes and record any intentional omissions.
2. Distinguish standalone skills, genuine plugins, MCP servers and connected apps; validate each with its own upstream-defined layout rather than forcing `SKILL.md` everywhere.
3. Independently record actual discovery, installation and smoke-test evidence for Codex and ChatGPT Work. Repository presence is **not** runtime installation.
4. Prioritize ATLAS AI's frontend/design, browser QA and security integrations, then VELA and the rest of the collection; avoid touching active application repositories.
5. Where no legitimate upstream is found, mark `UNRESOLVED` and request owner approval before archival/removal.

## Current blockers and safety
- CI remains red; provenance and runtime installation remain unverified.
- No vendor package replaced in this audit, no fabricated manifest/skill, no destructive deletion, no merge and no production deployment.
- Next action: implement a type-aware inventory and verify pinned vendor packages, with isolated tests and traceable commit evidence.
