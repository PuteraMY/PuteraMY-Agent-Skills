# Audit evidence boundaries and next verification gates — 2026-11-17

This document is a checkpoint, **not** an installation or compatibility certification.

## Independently fetched GitHub evidence

- Default-branch recursive tree: `cae3aa2bce5f86ffe03bfa0d84523cd64c936979`, 139 tree entries, `truncated=false`.
- Draft PR #1 head: `audit/2026-11-17-ci-root-cause` at `16efb45bd89f3873638141ecff312cdfd5878abe`; 142 entries, 88 blobs, `truncated=false`. The default branch remains unchanged by this checkpoint.
- The structural-audit workflow runs `python -m unittest discover -s tests -p 'test_validate_skills.py' -v` and `python scripts/validate_skills.py --json > structural-inventory.json`. It uploads `tracked-tree.txt`, `audited-commit.txt` and `structural-inventory.json` as evidence for 30 days.
- Workflow triggers on changes to skills, validation code and selected documents; **documentation-only changes under docs/audits/ do not trigger it**. A green workflow alone would only establish structural validation, not vendor provenance, functional installation or runtime availability.
- Prior CI findings: eight SKILL.md frontmatter failures documented in `docs/audits/2026-11-17-ci-root-cause.md`. Do not bypass them with fabricated upstream metadata.

## Verification matrix — what constitutes evidence

| Category | Source verification | Runtime verification | Current certification |
| --- | --- | --- | --- |
| Standalone upstream skill | Pin original commit, verify complete SKILL.md + scripts/references/assets, original license and file hashes | Test discovery and actual invocation in each supported host | Unverified |
| Vendor plugin | Verify original manifest, package tree, dependencies, license, installation instructions | Install with supported host installer and execute a plugin-provided action | Unverified |
| MCP server | Verify upstream server distribution, transport, auth, capabilities, license | Establish connection, enumerate tools and perform a safe read-only call | Unverified |
| Connected app | Verify supported first-party app/connector and permissions | Check actual connection and perform a safe read-only action | Unverified per host |
| API | Verify official endpoint, auth, limits, pricing and documentation | Perform authorized test request without exposing secrets | Unverified |
| Curated collection | Identify original index and individual project sources | N/A until individual integrations are selected | Not installable as one skill by assumption |

## Next changes (contest priority, reusable across projects)

1. Retrieve pinned upstream trees for Superpowers, UI UX Pro Max, Addy Osmani Agent Skills and Impeccable, including original plugin manifests, supporting scripts, references, licenses and assets. Compare every path and hash before changing local files.
2. Keep partial legacy entries intact pending replacement approval; never represent a directory with a single SKILL.md as a complete vendor distribution without evidence.
3. Implement a machine-readable provenance inventory with one row per retained integration: category, original repository, commit, license, complete file list or manifest path, installation target, last functional test and blockers.
4. Separate Codex and ChatGPT Work verification. A repository file or available GitHub connector does not prove an installed skill or plugin in either runtime.
5. Run validation and inspect the resulting workflow logs after functional changes; do not merge a failing PR or deploy production.
6. Continue across the entire inventory after the contest-critical integrations; mark missing upstream sources unresolved and request approval before archival/removal.

No vendor files were installed or replaced in this checkpoint. No destructive operations, merges or deployments were performed.
