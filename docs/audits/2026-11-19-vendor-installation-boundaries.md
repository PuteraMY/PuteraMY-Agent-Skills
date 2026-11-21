# Verified vendor installation boundaries — 2026-11-19 14:04 MYT

Scope: ATLAS AI priority, reusable across VELA and future projects. This is **documentation**, not installation evidence.

## Evidence checked this run

- Branch `audit/2026-11-17-ci-root-cause` at `fbccf56a0c44ebd4e0b1e65271501a180c4812d7`: Git tree `d5183468c9236a1a67ffcbc419b681b16e6da15e`, **150 entries, truncated=false**. Only one tracked `SKILL.md` exists under each of `.agents/skills/taste-skill/` and `.agents/skills/ui-craft/`. Neither local folder is a verified complete upstream distribution.
- Latest GitHub Actions runs `44440676832` and `44440671635` both concluded **failure** at the branch commit above. Do not claim CI passed.
- Original upstream READMEs read from `Leonxlnx/taste-skill` and `educlopez/ui-craft` default branches on 2026-11-19. Both GitHub repository metadata records list MIT; retain and check their **actual original LICENSE files** before redistribution. README instructions are upstream claims, not local runtime tests.

## Vendor-documented routes (NOT executed)

| Integration | Type / boundary | Official vendor instruction | Prerequisites | Codex verified here? | ChatGPT Work verified here? |
|---|---|---|---|---|---|
| Taste Skill | Standalone Agent Skill, plus separately advertised Codex/Claude plugin | `npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"`; vendor also documents `codex plugin marketplace add Leonxlnx/taste-skill` then `codex plugin add taste-skill@taste-skill` | Node 22+, Chrome/Edge/Chromium for browser checks; optional ffmpeg | NO | NO |
| UI Craft | Agent Skills subset; separate cross-harness CLI installer, plugin and MCP quality gates | `npx skills add educlopez/ui-craft` (skill-only); vendor recommends its official `ui-craft install` CLI for full system | CLI installer and binary compatibility; MCP runtime separately | NO | NO |

Taste Skill upstream README: https://github.com/Leonxlnx/taste-skill/blob/main/README.md . It states the current skill name is **`design-taste-frontend`** (not `taste-skill`) and that other old skills have moved to other repositories. Its skill includes `scripts/`, `assets/`, `library/` and browser-based checks; copying a lone entrypoint cannot satisfy those references.

UI Craft upstream README: https://github.com/educlopez/ui-craft/blob/main/README.md . It explicitly distinguishes `npx skills add` (skill-only) from full CLI/plugin installation, including MCP gates, agents, commands and design memory. Its Claude Code plugin documents `npx -y ui-craft-mcp@0.9.1`, but **that does not mean ChatGPT Work or Codex has this MCP server installed**. Vendor installer executes code and changes harness configuration: review before any actual installation; never silently run `curl | bash`.

## Next safe steps

1. Fetch and pin vendor commit SHAs and inspect their original `LICENSE`, `SKILL.md`, manifests, and all referenced support files; choose complete, license-compliant distribution boundaries.
2. Replace legacy assistant-authored entrypoints **only after** upstream match and safe migration plan. Do not fabricate frontmatter or mark unsupported integrations as installed.
3. Validate static repository structure and actual vendor checks; then test Codex discovery in an isolated project. Separately test ChatGPT Work connected apps/plugins. Report environment-specific evidence, not assumptions.
4. Keep other unresolved skills in inventory pending verification and user approval for archival/removal. No production deploy, merge or destructive deletion.

This report supersedes any suggestion that UI Craft and Taste Skill were installed merely because upstream READMEs were read.
