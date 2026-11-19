# 2026-11-19 — CI evidence and safe remediation queue

Evidence collected from GitHub Actions run [44469560583](https://github.com/PuteraMY/PuteraMY-Agent-Skills/actions/runs/44469560583), job 135375438823 (2026-11-19 06:04 UTC). Run commit: `9c81cb00a30e8f20e6844d49742bb0aeacc00156`.

## Complete repository tree snapshot

- `main` commit `cae3aa2bce5f86ffe03bfa0d84523cd64c936979`: 139 recursive Git tree entries, `truncated=false`.
- Audit branch commit `9c81cb00a30e8f20e6844d49742bb0aeacc00156`: 151 recursive Git tree entries, 97 blobs, `truncated=false`.
- `.agents/skills/taste-skill/` and `.agents/skills/ui-craft/` each currently contain only `SKILL.md` in the tracked tree. These are not evidence of complete vendor packages.

## Reproduced failure from the latest job log

`python3 scripts/validate_skills.py` fails with exactly eight frontmatter errors:
`context7-documentation`, `playwright-testing`, `strix-security-audit`, `supabase-agent-plugin`, `superdesign-skill`, `taste-skill`, `ui-craft`, `ux-ui-agent-skills`.

Summary emitted by validator: `FAIL: 43 skill directories; 8 structural failures; tracked files: 97`.

**Do not repair by inserting fabricated YAML into pseudo-skills.** The validator's error is structural; the root cause for each entry may be incorrect distribution type or non-upstream content.

## Next implementation queue (no destructive operations)

1. **ATLAS AI:** For `taste-skill`, `ui-craft`, `superdesign-skill`, `ux-ui-agent-skills`, first pin vendor commit/tag, inspect license and installation instructions, then stage exact original distribution (including support files) in a separate path/branch before any replacement. Distinguish skill vs plugin vs MCP, and verify Codex discovery in the target project.
2. **VELA and reusable backend/testing:** For `playwright-testing`, `context7-documentation`, `supabase-agent-plugin`, and `strix-security-audit`, classify original product/distribution type before any move; a connected app or MCP is not a `SKILL.md` package.
3. For each retained entry, record upstream URL + immutable SHA, license, full package file list, installation steps, dependency/security notes, static validation, actual Codex discovery test, actual Work connection test. Mark unavailable environments `not tested`.
4. Where no authentic upstream exists, leave existing files intact, label unresolved, and obtain user approval before archival/removal.
5. After actual migrations, rerun validation, review false assumptions in validator, and test a clean install in each supported runtime. CI green alone is insufficient.

## Current verified result

No vendor package replacement, Codex installation, Work plugin connection, merge, deletion or production deployment is claimed by this report. This commit records a fresh, independently reproduced failure and exact remediation queue, not a fix.
