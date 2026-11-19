# 2026-11-19 — UI Craft upstream distribution boundary (evidence ledger)

Scope: non-destructive source verification only. **No installation, copying, CI repair or runtime capability is claimed.**

## Observed upstream files

Source: https://github.com/educlopez/ui-craft (GitHub Contents API, inspected 2026-11-19). The upstream root contains `distribution-manifest.json`, `.codex-plugin/`, `.agents/`, `skills/`, `mcp/`, `scripts/`, `LICENSE`, `package.json`, `pnpm-lock.yaml`, and `.mcp.json`. This is a multi-component distribution, **not** a standalone one-file skill.

- `distribution-manifest.json` declares detector `ui-craft-detect@0.13.0` (Node >=18), MCP `ui-craft-mcp@0.9.1` (Node >=20), CLI 1.x (Go >=1.23), canonical skill source `skills/`, canonical MCP source `mcp/src/`, and the `mcp-tools-v1` contract.
- `.codex-plugin/plugin.json` declares `name: ui-craft`, `version: 1.0.0`, `skills: ./skills/`, `mcpServers: ./.mcp.json`, `requires_local_executor: true`, and `license: MIT`. These are **vendor manifest claims**, not proof that this plugin format is installed or supported by a given Codex session.
- `.agents/skills/` lists 29 directories including `ui-craft`, `animate`, `audit`, `polish`, `tokens` and `typeset`. This is a discovery-oriented layout; do not assume that every directory is a complete independently installable package.
- Upstream `LICENSE` exists; its actual text and any third-party licensing obligations must be reviewed before vendoring.

Evidence URLs:
- https://github.com/educlopez/ui-craft/blob/main/distribution-manifest.json
- https://github.com/educlopez/ui-craft/blob/main/.codex-plugin/plugin.json
- https://github.com/educlopez/ui-craft/tree/main/.agents/skills

## Classification and installation boundary

| Component | Evidence of type | Codex installed/usable | ChatGPT Work installed/usable |
| --- | --- | --- | --- |
| `skills/` and `.agents/skills/` | Upstream skill assets | UNVERIFIED | UNVERIFIED |
| `.codex-plugin/plugin.json` | Vendor Codex plugin manifest | UNVERIFIED | Not proof of Work integration |
| `.mcp.json`, `mcp/src/` | MCP launcher/source | UNVERIFIED | UNVERIFIED |
| `cli/`, `scripts/detect/` | Executable CLI/detector | UNVERIFIED | UNVERIFIED |

**Do not** copy only `SKILL.md`, invent a wrapper, or label a GitHub copy as installed. The vendor manifest explicitly requires a local executor for its plugin; runtime availability, supported installation procedure, exact dependencies and authorization must be checked in the target environment.

## CI and migration blockers

GitHub Actions run https://github.com/PuteraMY/PuteraMY-Agent-Skills/actions/runs/44320257824 (latest checked on 2026-11-19) concluded **failure** at commit `fd376d5501bee6a70779fd7dd469a510c3b7f1ef`. Earlier CI logs identify eight malformed/missing frontmatter entries; do not assert these are the only remaining failures without reading the latest job logs.

Taste Skill upstream https://github.com/Leonxlnx/taste-skill has `.agents/`, `.claude-plugin/`, `.codex-plugin/`, `skills/`, `install.sh`, `tests/`, and `LICENSE` at root. Its installer, manifests, pinned revision and license must be reviewed before any migration. The mere presence of these directories does not establish installation in Work/Codex.

## Next actions (no destructive changes)

1. Pin exact upstream commit SHAs and inspect upstream licenses, install instructions, scripts, manifests, package lockfiles and security implications.
2. For each legacy pseudo-skill, map to a genuine supported upstream distribution **or mark unresolved**. Request user approval before archival/removal.
3. In a disposable checkout, install the complete verified vendor distribution according to its supported instructions, then test skill discovery, MCP handshake and plugin availability **separately** in Codex and Work.
4. Repair validation only after distinguishing legitimate skills from MCP/plugin documentation; run static CI and record job logs. Keep existing projects untouched.
