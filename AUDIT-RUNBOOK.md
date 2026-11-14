# Reproducible full-tree and upstream audit runbook

Updated: 2026-11-14. This is an audit procedure, **not** proof that any skill/plugin/app is installed.

## Evidence acquisition (read-only)

At a trusted checkout of this repository, record the exact revision and **every tracked path**:

```sh
git rev-parse HEAD > audited-commit.txt
git ls-tree -r --name-only HEAD > tracked-tree.txt
wc -l tracked-tree.txt
python -m unittest discover -s tests -p 'test_validate_skills.py' -v
python scripts/validate_skills.py --json > structural-inventory.json
```

Do not substitute `find .agents/skills` for the complete Git tree. Include `.github`, scripts, licenses, documentation, plugin manifests and nested vendor support files. Preserve the raw files as immutable evidence keyed by `audited-commit.txt`. The existing GitHub Actions workflow uploads these three files, but **no successful run or artifact has been inspected as of this update**.

## Per-integration evidence ledger

For each retained integration, capture:
- Local paths and classification: standalone skill, vendor plugin, MCP server, connected app, or unresolved/custom guide.
- Publisher's official source URL and immutable upstream commit/tag; original license and redistribution conditions.
- Recursive vendor file list and checksums, including scripts, assets, references, tests and original manifests. Record missing/extra/modified files; a matching `SKILL.md` alone proves only an entrypoint match.
- Installation mechanism and independent Codex / ChatGPT Work discovery evidence. A Codex skill is **not** automatically a ChatGPT Work plugin; an MCP server is **not** automatically connected or authorized.
- Executed test command, exit code, logs, runtime and date. Mark unexecuted checks **not tested**.
- Remediation, owner and blocker. If no trustworthy upstream distribution exists, mark **unresolved** and obtain approval before archival or removal.

## Safe prioritization

1. ATLAS AI contest-critical frontend/design, testing, security and deployment-related integrations.
2. All remaining retained skills and vendor plugins, including original support trees and licenses.
3. MCP servers and connected apps, tested in their actual authorized environments.
4. Legacy assistant-authored directories: replace only after verified upstream mapping; otherwise retain and flag unresolved pending approval.

## Evidence limitations on 2026-11-14

GitHub connector reads of `COMPATIBILITY.md` and `.github/workflows/skills-audit.yml` succeeded. Latest commit returned by GitHub search: `b0d403cdbd6a34c3e8758774c05ec852108e10f9`. A commit-workflow lookup returned zero runs, **but the connector only searches pull-request-triggered runs**, so this does not establish whether push/manual workflows ran. No full-tree artifact, vendor package completeness proof, Codex runtime discovery or ChatGPT Work installation proof was obtained in this check. No destructive action or production deployment is authorized.
