# PuteraMY Agent Skills — upstream migration

**Status: IN PROGRESS. Not a fully installed plugin collection.**

This repository is being migrated from assistant-authored guides to **original upstream skill/plugin/MCP distributions**. Its purpose is a reusable development toolkit for **all current and future PuteraMY projects**, across ChatGPT Work and Codex. ATLAS AI is the immediate contest priority, not the toolkit's scope. See [OFFICIAL-SOURCES-AUDIT.md](OFFICIAL-SOURCES-AUDIT.md) for source URLs, copied entrypoints, incomplete dependencies, and blockers.

## What works where

- **Codex:** In a project where Codex discovers `.agents/skills/`, original complete skill folders can be used after checking their dependencies. To use skills in another project, install/copy the **complete upstream folder** into that project's supported location and verify discovery. This shared GitHub repository does **not** automatically configure other projects.
- **ChatGPT Work:** Use the supported ChatGPT plugin/app installation and authorization flow. A GitHub `SKILL.md`, plugin manifest, or README does **not** automatically install a plugin in Work. Availability depends on the product and connected apps.
- **MCP/tools:** Follow official vendor installation and authorization instructions. Do not call a custom `SKILL.md` wrapper an official plugin.

## Trust policy

1. **No assistant-authored third-party skills.** Retain vendor originals and all required files, with upstream URLs and licenses.
2. Treat a copied `SKILL.md` as an **entrypoint only** until its complete vendor package, dependencies and runtime are verified.
3. Existing custom guides are **legacy/unverified**, not official vendor integrations; do not use them as proof of a working tool.
4. Never claim all skills are installed or functional without environment-specific tests.
5. Preserve existing projects; do not deploy production or remove files destructively without approval.

## Validation

Run `python3 scripts/validate_skills.py` in a checked-out copy. This is a **static repository check only**, not a test of Work plugin installation, Codex discovery, browser automation or vendor dependencies.

## Licensing

**Do not assume a single MIT license covers all files.** Third-party skills and plugin distributions retain their own upstream licenses and attribution requirements. Inspect each upstream project and any included license files before redistribution.

## Progress

See [the live audit](OFFICIAL-SOURCES-AUDIT.md) and [commits](../../commits/main). The migration is unfinished until each retained integration has a complete source, compatible installation path and verified tests.
