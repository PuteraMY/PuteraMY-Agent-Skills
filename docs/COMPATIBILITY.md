# Compatibility and verification

Last reviewed: 2026-11-16. **No installed/usable status is inferred from repository presence.**

## Integration types (do not conflate)

| Type | Evidence required | Installation/discovery test |
| --- | --- | --- |
| Standalone agent skill | Original upstream `SKILL.md` plus referenced files and license | Confirm the specific host reads the installed path and can use the skill on a harmless task |
| Genuine plugin | Original vendor plugin manifest, complete distribution, declared host support | Use the host's documented plugin installation path, then verify plugin discovery and actual invocation |
| MCP server | Actual server implementation, documented transport/config, authentication and exposed tools | Connect in the target host, enumerate tools, execute an authorized read-only smoke test |
| Connected app | Host-supported app connection and granted permissions | Confirm connected state and successfully call one authorized read action |
| External API | Provider endpoint, credentials, SDK/docs | Test from a safe isolated client; API availability is not MCP/skill installation |
| Curated collection | Upstream index and links | Audit each selected item individually; collection is not itself necessarily installable |

## Host-specific status

| Host | Potential integration route | Verified installed in this repository? | Runtime usable? | Required proof |
| --- | --- | --- | --- | --- |
| Codex | Project `.agents/skills/<skill>/SKILL.md` where supported; vendor Codex plugin route only when documented | No complete installation proof | **Unverified** | Host/version, discovered skill/plugin ID, invocation transcript, dependent scripts/data verified |
| ChatGPT Work | Product-supported connected apps/plugins and available skills, where explicitly supported | Repository files do not install automatically | **Unverified** | Host connection status, actual exposed tool/skill discovery, authorized smoke-test result |
| VS Code GitHub Copilot | Project `.github/skills/<skill>/SKILL.md` where supported | Not established | **Unverified** | Host/version and discovery/invocation evidence |
| Claude Code | Vendor-supported skills/plugin installation, original manifests | Not established | **Unverified** | Vendor installation docs, installed listing, safe invocation |

A `.claude-plugin/plugin.json` file is evidence of a **Claude plugin distribution**, not automatic compatibility with Codex or ChatGPT Work. A `.codex-plugin/plugin.json` file is evidence of a vendor's Codex-targeted distribution, not proof that a particular Codex environment has loaded it. A connected app visible in one ChatGPT session is not proof that the same tool is usable in Codex or all users' Work sessions.

## Priority package gates

| Upstream | Verified source facts | Local state | Next action |
| --- | --- | --- | --- |
| [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Original Claude plugin manifest and dependent skill files | Partial local copy; comparison records 74 missing upstream paths and 2 same-path hash differences | Pin complete vendor distribution, inspect dependencies, preserve original license; test per host |
| [Impeccable](https://github.com/pbakaus/impeccable) | Original Claude plugin manifest and multi-host skill directories | Partial local copy; comparison records 68 missing upstream paths and 1 hash difference | Pin complete distribution, check scripts/references, test per host |
| [Superpowers](https://github.com/obra/superpowers) | Original Claude and Codex plugin manifests, hooks/scripts/skills | Complete package not established locally | Review original install instructions, dependencies and full vendor tree |
| [Addy Osmani Agent Skills](https://github.com/addyosmani/agent-skills) | Original Claude and Codex plugin manifests, scripts/skills | Complete package not established locally | Review individual skills and original distribution |
 
See [upstream tree comparison](UPSTREAM-TREE-COMPARISON-2026-11-16.md) and [original plugin manifest evidence](ORIGINAL-PLUGIN-MANIFEST-EVIDENCE-2026-11-16.md) for pinned source evidence. These source checks are **not runtime smoke tests**.

## Repeatable safe acceptance procedure

1. Record host, version, repository commit, upstream commit, source URL, license and integration type.
2. Inventory *all* original vendor files, scripts, references, manifest(s), dependency declarations and licenses; compare Git paths/hashes.
3. Preserve local modifications and review diffs before any replacement. Never invent missing vendor wrappers or SKILL.md.
4. Run static validation, package-specific tests, then isolated smoke tests with no production credentials.
5. On each host separately, verify installed/discovered state and perform a harmless read-only invocation. Save actual commands, results and logs.
6. Mark `verified` only when both complete package integrity and runtime use are evidenced; otherwise `partial`, `blocked` or `unverified`.
7. Keep unresolved upstream names as unresolved until a genuine source is found; seek approval before archival/removal. Do not deploy production or modify working projects.

## Known blockers

- Existing UI UX Pro Max and Impeccable distributions are incomplete against the pinned upstream trees.
- A verified manifest does not establish that host-specific installation is supported or completed.
- No per-host installation logs or successful runtime invocations are recorded in this file.
- Ambiguous upstream names (Caveman, Understand Anything, Awesome Claude Skills, Archify) require exact source identification before inclusion.
