# CI and upstream migration decision ledger — 2026-11-18 17:55 MYT

## Verified repository snapshots (GitHub Git Trees API)

- Default branch `main`: commit `cae3aa2bce5f86ffe03bfa0d84523cd64c936979`, `truncated=false`, **139 tree entries / 86 blobs / 43 SKILL.md entrypoints**.
- Draft audit branch `audit/2026-11-17-ci-root-cause`: commit `4f63b7c26cd3392d8f9a9df1a55553ee4f926dce`, `truncated=false`, **147 tree entries / 93 blobs / 43 SKILL.md entrypoints**.
- These counts describe tracked Git tree objects, **not** vendor package completeness or successful installation.
- Source: `GET /repos/PuteraMY/PuteraMY-Agent-Skills/git/trees/{ref}?recursive=1`.

## Latest CI evidence

- GitHub Actions runs [44247748688](https://github.com/PuteraMY/PuteraMY-Agent-Skills/actions/runs/44247748688) and [44247742638](https://github.com/PuteraMY/PuteraMY-Agent-Skills/actions/runs/44247742638) completed **failure** at audit commit `4f63b7c`.
- Run 44247748688, job `validate`, failed step `python3 scripts/validate_skills.py`. The latest full error output has not been re-read in this ledger; the eight named structural errors below come from the **previously retrieved** run 44099181768. Do not assume a new error list without checking the latest log.
- Previous confirmed failing directories: `context7-documentation`, `playwright-testing`, `strix-security-audit`, `supabase-agent-plugin`, `superdesign-skill`, `taste-skill`, `ui-craft`, `ux-ui-agent-skills`.
- Structural CI is deliberately not equivalent to upstream completeness, runtime discovery or Work plugin connection.

## Prioritized safe remediation

1. **ATLAS AI:** Verify vendor's full original distribution, license, support scripts/data, manifest and pinned revision for UI UX Pro Max, Impeccable, and the video-production candidate. `remotion-video-production/SKILL.md` is a locally authored guide, not evidence of an official Remotion skill. Do not invent a vendor entrypoint.
2. **VELA:** Verify upstream provenance and full distribution of database/testing/performance entries. A passing static validator alone is not sufficient for database correctness or safe tool execution.
3. **CI:** Resolve the eight malformed entries by installing complete genuine upstream packages when available; otherwise classify and quarantine unresolved legacy guides through an approved, non-destructive migration. **Do not add fabricated frontmatter or weaken checks merely to obtain green CI.**
4. **Runtime:** For each retained integration, record separate observed Codex skill discovery and ChatGPT Work plugin/app connection or execution tests, including environment, date, command/action and outcome. No installation is claimed in this ledger.
5. **Future projects:** Continue auditing all 43 entrypoints. Entries without a verifiable upstream must remain `unresolved` until owner approval for archival/removal.

## Safety / change boundary

This commit changes **documentation only** on the draft audit branch. No legacy content removed, no merge, no production deployment, no credentials changed. It does not certify that any integration works.
