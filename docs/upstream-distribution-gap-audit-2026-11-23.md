# Upstream distribution gap audit — 2026-11-23

This document records an **incomplete vendor snapshot**, not a successful plugin installation.

## Reproducible source and inventory

- Source: https://github.com/addyosmani/agent-skills
- Pinned upstream commit: `8c99fa36d90068c82d547f7c12a9d67a3e95f4ee`
- Upstream recursive Git tree: **381 entries** (directories and blobs), `truncated=false`.
- PuteraMY audit branch baseline: `a55ff163ae357eeb2e0b3a51e36503f8360397d9`, recursive Git tree **191 entries**.
- Exact path comparison under `vendor/addyosmani-agent-skills/` identified **249 missing upstream blob paths** at baseline. One missing original manifest, `.agents/plugins/marketplace.json`, was subsequently added in commit `640c48180de69ecf399c4a90a42e7d6d335ef5ad`. Thus at least **248 baseline gaps remain**, subject to fresh tree reconciliation.
- Upstream marketplace manifest original Git blob: `9ad29f1e5091ea234627664cb09ac7bca52af6bf`.

## Outstanding groups (examples, not exhaustive)

- Remaining `skills/*` original entrypoints and bundled support files, including `skills/idea-refine/scripts/idea-refine.sh` and `skills/constraint-driven-development/scripts/quality-gate.mjs`.
- `hooks/*`, `agents/*`, `commands/*`, `.claude/commands/*`, `.gemini/commands/*`, `references/*`.
- `scripts/*`, `evals/*`, `docs/*`, `README.md`, `AGENTS.md`, `CONTRIBUTING.md`, `CLAUDE.md`, `.github/workflows/test-plugin-install.yml` and `.claude-plugin/marketplace.json`.

Do not activate incomplete vendor hooks or manifests. The missing source files may be needed for plugin behavior or validation; no partial snapshot is certified installable.

## Compatibility and evidence boundaries

| Distribution / environment | Evidence | Status |
| --- | --- | --- |
| Original upstream standalone skill files | Several byte-preserving source files copied to vendor path; compare Git blob SHAs | Partial; not runtime tested |
| Original Codex plugin | `.codex-plugin/plugin.json` copied earlier | Partial distribution; not installed or discovered |
| Original Claude plugin | `.claude-plugin/plugin.json` copied earlier | Partial distribution; not installed or discovered |
| Original agent marketplace | `.agents/plugins/marketplace.json` now copied | Manifest only; not installed or discovered |
| MCP server | Mentions in local guides do not establish installed servers | Unverified |
| ChatGPT Work connected app | Requires actual connection and permission evidence | Unverified |
| Codex skill discovery | Requires actual runtime listing and invocation | Unverified |

## Acceptance criteria

1. Reconcile every upstream Git blob path and content SHA, including license and all support files, without rewriting vendor files.
2. Record whether each retained integration is a standalone skill, plugin, MCP server, connected app or unresolved guide; keep guide claims distinct from vendor provenance.
3. Run vendor and repository validation suites, report exact failing checks, and only then attempt isolated runtime discovery and invocation.
4. Preserve all existing projects and audit history; no removal of unresolved entries without approval, no production deployment, no merge to main.

Structural CI failure is an unresolved blocker, not a reason to relax validation. ATLAS AI's immediate contest needs determine **order**, not scope: the complete collection must be reusable across future projects.
