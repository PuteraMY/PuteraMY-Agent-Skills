# Audit evidence — 2026-11-21 evening (MYT)

Scope: `PuteraMY/PuteraMY-Agent-Skills`, branch `audit/2026-11-17-ci-root-cause`, commit `a74be2fa7e10155fb910630d7145deb1ef5e565f` (Git tree SHA `4d4f5d1ef2a8085513fc9d48ede9bca28432db93`).

## Verified read-only evidence
- GitHub Git Trees API recursive response: `truncated=false`, **159 entries**, **105 blobs**, **43 direct skill directories** under `.agents/skills/`. These are repository objects, not 43 verified upstream installations. Source: https://api.github.com/repos/PuteraMY/PuteraMY-Agent-Skills/git/trees/4d4f5d1ef2a8085513fc9d48ede9bca28432db93?recursive=1
- Latest inspected PR workflow run **44892639603**, completed **failure** on 2026-11-21 10:05 UTC. Source: https://github.com/PuteraMY/PuteraMY-Agent-Skills/actions/runs/44892639603
- Job **136811561965**: Python unittest suite **8/8 passed**; `git ls-tree -r --name-only HEAD` counted **105** tracked paths; `python scripts/validate_skills.py --json` exited **1**; provenance inventory ran and the four-file artifact was uploaded (artifact **14703025813**). Source: https://github.com/PuteraMY/PuteraMY-Agent-Skills/actions/runs/44892639603/artifacts/14703025813

## Evidence boundaries / blockers
1. Structural validator currently requires a valid `SKILL.md` for *every* directory, without a verified classification of standalone skill vs plugin vs MCP server vs connected app. This is not sufficient to certify vendor distributions or reject genuine non-skill integrations.
2. Git-tree completeness is confirmed only for the cited commit, not for upstream packages or installed runtimes.
3. **No** Codex or ChatGPT Work runtime discovery/installation test was performed in this audit. Do not interpret presence in Git as installed.
4. **No** upstream source hash comparison, vendor license completeness or original plugin manifest verification was completed. Any uncertain or assistant-authored entry remains unresolved until independently checked.

## Safe next actions
- Prioritize ATLAS AI's browser QA, frontend design, security and CI integrations; then VELA and the remaining catalog.
- Build a typed integration manifest with explicit `unverified` defaults and per-item upstream URL, pinned revision, license, full file manifest, runtime compatibility, install evidence and test result. Require authoritative evidence before marking `verified`.
- Split CI validation by confirmed integration type. Never fabricate vendor `SKILL.md` or claim installation merely to pass CI.
- Preserve all existing files pending upstream comparison and approval for any archival/removal. No production deployment or merge.

This document records evidence only, not completion or a claim of installation.
