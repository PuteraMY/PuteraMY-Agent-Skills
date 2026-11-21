# 2026-11-21 — Evidence boundary and validator design review

Scope: non-destructive inspection of branch `audit/2026-11-17-ci-root-cause` via connected GitHub file reads. This checkpoint does **not** certify a complete fresh recursive Git tree, a successful runtime installation, or a green CI run.

## Directly inspected files
- [scripts/inventory_provenance.py](../../scripts/inventory_provenance.py), Git blob `332d3bb45b9d817c2823135b9b85cf10daab5949`.
- [2026-11-20 CI evidence and type-aware triage](2026-11-20-evening-ci-and-type-aware-triage.md), Git blob `4c74bc70caf85031eadf9c5ca95f59b007d86843`.
- [README.md](../../README.md), Git blob `69969f63b9a8e6f9926fd9ca699cd2ee51e0187f`.

## Concrete findings
1. `inventory_provenance.py` obtains tracked **files** with `git ls-files -z`, then enumerates immediate directories under `.agents/skills`. This is useful as a local file inventory, but **not** proof of a complete recursive Git *tree* including directory entries, gitlinks/submodules, or upstream package completeness. For a complete tree audit, capture the branch commit SHA and `git ls-tree -r -t --full-tree <sha>`, and independently confirm API tree `truncated=false`.
2. The script unconditionally evaluates `SKILL.md` frontmatter for every immediate directory. A genuine MCP server, connected app or plugin without a vendor `SKILL.md` can therefore appear as a frontmatter failure. Preserve structural failures as observations; do not auto-create frontmatter. A future type-aware validator should use a reviewed classification registry and separate validation contracts.
3. `contains_license_named_file` and `contains_plugin_manifest` are only filename heuristics; they do **not** prove vendor origin, license compatibility, original manifest integrity or completeness. `self_identifies_local_guide` is also only a keyword heuristic. None of these fields should be promoted to an installed/verified status.
4. `upstream_complete`, `codex_discovered`, and `work_connected` are correctly hardcoded `UNVERIFIED`. Preserve that conservative behavior until actual pinned source and runtime evidence is recorded.
5. The previous report records eight structural failures at CI run [44715978152](https://github.com/PuteraMY/PuteraMY-Agent-Skills/actions/runs/44715978152), but that is **prior-run evidence**, not a fresh CI result for this checkpoint.

## Acceptance criteria for subsequent changes
- Record immutable upstream revision, source URL, license text, original manifests and all required scripts/assets for each retained distribution.
- Classify as standalone skill / vendor plugin / MCP server / connected app / unresolved **before** selecting validation rules.
- Record separate evidence fields for repository-present, Codex discovery, Codex invocation, Work connection and Work invocation; `unknown` is not `failed` and neither is `passed`.
- ATLAS AI design/testing dependencies first; then VELA database/testing/security and remaining future-project entries.
- Do not replace or archive unresolved legacy content without source evidence and approval. Do not merge or deploy production.

## Outstanding blockers
No new vendor distribution was imported or installed in this checkpoint. No fresh complete-tree count, CI result or end-to-end host test was obtained. Next run should capture an exact branch SHA and full recursive tree, then implement type-aware classification with regression tests, before claiming structural CI remediation.
