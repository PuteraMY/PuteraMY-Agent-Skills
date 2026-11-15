# Upstream package completeness evidence — 2026-11-15

This is **read-only Git tree path comparison**, not a file-content checksum comparison, executed test, installation, or endorsement. No vendor files were copied, no projects deployed, and no legacy guides removed.

## Method

Read the recursive Git trees through the authorized GitHub connector using `GET /repos/{owner}/{repo}/git/trees/main?recursive=1`. Each response reported `truncated: false`. Compare **blob paths** under the vendor's skill directory to blob paths under this repository's mapped directory. Path presence alone does not establish byte-for-byte identity; compare blobs and license terms before promoting any integration to L2.

Local repository: `PuteraMY/PuteraMY-Agent-Skills`, revision `9a35781ec88fdb68c121b31a896024c5ab05c41e`; 82 tracked files and 43 skill entrypoints.

| Local integration | Official upstream repository / pinned tree SHA | Upstream skill blobs | Local mapped blobs | Missing upstream paths | Local-only paths | Status |
| --- | --- | ---: | ---: | ---: | --- | --- |
| `ui-ux-pro-max` | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill), `d643997c82e94742dd3bee43210b0198e8bbba3d` | 75 | 5 | **71** | `LICENSE` | Incomplete; L2 blocked |
| `vercel-react-best-practices` | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills), `1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62` | 76 | 2 | **74** | None | Incomplete; L2 blocked |

For UI UX Pro Max, four local paths overlap with the vendor tree; the extra local `LICENSE` must be checked for correct origin and redistribution terms. Missing files include `data/app-interface.csv`, `data/catalog-summary.json`, `data/colors.csv`, `data/stacks/html-tailwind.csv` and other data/script assets. The local `SKILL.md` references a search script and data-backed queries: **do not assume they work** with this incomplete directory.

For Vercel React Best Practices, missing files include `AGENTS.md`, `README.md`, `metadata.json`, `rules/_sections.md`, `rules/_template.md` and most individual rules. The local directory has only `SKILL.md` and `rules/async-parallel.md`.

## Safe remediation

1. Preserve current projects and existing skill folders until a complete vendor package has been reviewed.
2. Copy or install the complete original distribution from a pinned upstream commit, preserving relative paths, scripts, references, licenses and manifests; **do not author substitutes**.
3. Verify every expected path and blob hash against the pinned upstream tree; document vendor license and local-only files separately.
4. Execute vendor-recommended tests and a representative non-destructive task. Check Codex discovery and ChatGPT Work plugin/app availability **independently**.
5. Mark unsupported or untraceable packages unresolved and request approval before archival or removal.

## Runtime and CI evidence

Neither vendor package was installed or executed in this run. No Codex runtime or ChatGPT Work installation was verified. No successful GitHub Actions run or downloadable audit artifact was inspected; the attempted Actions listing URL was rejected by the connector. The repo tree and upstream trees were readable through GitHub API. Do not claim L2–L5 certification.
