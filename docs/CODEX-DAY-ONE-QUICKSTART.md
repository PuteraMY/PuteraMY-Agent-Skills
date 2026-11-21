# Codex Day-One Quickstart — ATLAS AI (18 November 2026)

**Status:** safe operational checklist, **not** a claim that the shared skills are installed. Applies to all future projects after replacing the project name.

## Start tomorrow without waiting for migration

1. Open the **existing ATLAS AI repository** in Codex. Do not initialize a new project or rebuild an existing one.
2. Read the project-local `AGENTS.md` (if present), `README.md`, package manifest, current branch and git status before edits.
3. Inspect the project's available skill directories and Codex-discovered skills. The separate `PuteraMY-Agent-Skills` GitHub repository does **not** automatically install skills into ATLAS AI.
4. Only use **complete, original, verified** upstream skills already discoverable in this Codex environment. If a desired skill is absent, continue with standard Codex capabilities or follow the vendor's documented installation procedure after reviewing permissions.
5. Work on a feature branch, preserve existing functionality, run the project’s actual typecheck/lint/tests/build, and report evidence. Never deploy production or make destructive changes without approval.
6. Keep tokens/keys in environment secrets, never commit credentials. Treat external model API keys (Groq/OpenRouter) as API access, not MCP or skills.

## Suggested first Codex instruction

> Continue the existing ATLAS AI project for the competition. First inspect the repository, current branch, AGENTS.md, README, scripts, tests, and existing implementation. Do not rebuild or discard working features. Inventory which skills are **actually discovered and usable** in this Codex session, distinguishing complete upstream skills from legacy guides and missing installations. Use only verified relevant skills; otherwise proceed with standard Codex tools. Prioritize a working end-to-end vertical slice, quality UI, security, and automated tests. Work on a feature branch. Run available checks and report actual results, blockers and exact changed files. Do not deploy production, merge, delete files or change secrets without my approval.

## Shared toolkit migration blockers (do not misrepresent)

- Latest checked CI run 44099181768 fails `python3 scripts/validate_skills.py`: 8 malformed/missing frontmatter entries: `context7-documentation`, `playwright-testing`, `strix-security-audit`, `supabase-agent-plugin`, `superdesign-skill`, `taste-skill`, `ui-craft`, `ux-ui-agent-skills`.
- Do **not** add fabricated frontmatter to assistant-authored pseudo-skills just to make CI green. Identify real upstream distributions and separate MCP/plugin/connected app from standalone skills.
- UI UX Pro Max and Impeccable have previously reported missing upstream support files; verify exact pinned upstream trees before installation.
- ChatGPT Work plugin connections and Codex discovery are distinct; test each environment separately.
- This guide is documentation only and does not prove runtime installation, CI success, or skill completeness.

## Exit criteria for shared toolkit

Pinned upstream source and license; complete distribution including vendor scripts/data/manifests; valid structure and CI; runtime discovery/use evidence for Codex and Work separately; unresolved entries documented pending user approval. No unsupported claim of 100% completion.
