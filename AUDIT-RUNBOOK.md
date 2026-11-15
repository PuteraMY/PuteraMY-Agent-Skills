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

## Verified Git tree snapshot — 2026-11-15 (GitHub API)

Read-only request: `GET https://api.github.com/repos/PuteraMY/PuteraMY-Agent-Skills/git/trees/main?recursive=1`.

- Resolved tree SHA: `d1e6cb88f67f5b9c5fa89ab07a5b4b1e5f3f938d`.
- API `truncated: false`; 82 tracked blob paths, 43 `.agents/skills/*/SKILL.md` entrypoints.
- This resolves the previous inability to enumerate the complete *tracked Git tree at this revision*. It does not inventory untracked files or certify the original vendor package.
- All 43 entrypoints are **inventory candidates**, not verified upstream distributions, installed plugins, or usable Codex/Work integrations.
- Repository paths (complete tracked-file snapshot):

```text
.agents/skills/3d-asset-optimization/SKILL.md
.agents/skills/animation-performance-qa/SKILL.md
.agents/skills/anthropic-frontend-design/LICENSE.txt
.agents/skills/anthropic-frontend-design/SKILL.md
.agents/skills/apple-design-skill/SKILL.md
.agents/skills/auth-authorization-hardening/SKILL.md
.agents/skills/automated-testing/SKILL.md
.agents/skills/browser-qa/SKILL.md
.agents/skills/cicd-quality-gates/SKILL.md
.agents/skills/cloudflare-security-audit/AI-AND-LLM.md
.agents/skills/cloudflare-security-audit/ATTACK-CLASSES.md
.agents/skills/cloudflare-security-audit/CLIENT-SIDE.md
.agents/skills/cloudflare-security-audit/CLOUD-AND-DEPLOYMENT.md
.agents/skills/cloudflare-security-audit/DATA-ISOLATION-AND-LIFECYCLE.md
.agents/skills/cloudflare-security-audit/DESKTOP-MOBILE-AND-LOCAL-IPC.md
.agents/skills/cloudflare-security-audit/HUNTING.md
.agents/skills/cloudflare-security-audit/LICENSE
.agents/skills/cloudflare-security-audit/MEMORY-SAFETY-AND-BINARY.md
.agents/skills/cloudflare-security-audit/PROTOCOLS-RPC-AND-MESSAGING.md
.agents/skills/cloudflare-security-audit/RECONNAISSANCE.md
.agents/skills/cloudflare-security-audit/RESOURCE-EXHAUSTION-AND-AVAILABILITY.md
.agents/skills/cloudflare-security-audit/SKILL.md
.agents/skills/cloudflare-security-audit/SUPPLY-CHAIN-AND-RELEASE.md
.agents/skills/cloudflare-security-audit/VALIDATION-AND-REPORTING.md
.agents/skills/cloudflare-security-audit/WEB-PROTOCOL-AND-AUTH.md
.agents/skills/cloudflare-security-audit/report-schema.json
.agents/skills/cloudflare-security-audit/validate-coverage-ledger.cjs
.agents/skills/cloudflare-security-audit/validate-coverage-ledger.test.cjs
.agents/skills/cloudflare-security-audit/validate-findings.cjs
.agents/skills/cloudflare-security-audit/validate-findings.test.cjs
.agents/skills/context7-documentation/SKILL.md
.agents/skills/core-web-vitals-seo/SKILL.md
.agents/skills/database-architecture/SKILL.md
.agents/skills/deployment-qa/SKILL.md
.agents/skills/design-system/SKILL.md
.agents/skills/design-to-code-fidelity/SKILL.md
.agents/skills/emil-skills/SKILL.md
.agents/skills/find-skills/SKILL.md
.agents/skills/frontend-design/SKILL.md
.agents/skills/fullstack-development/SKILL.md
.agents/skills/gsap-official-patterns/SKILL.md
.agents/skills/gsap-scroll-storytelling/SKILL.md
.agents/skills/impeccable/LICENSE
.agents/skills/impeccable/SKILL.md
.agents/skills/lottie-rive-animation/SKILL.md
.agents/skills/motion-animation/SKILL.md
.agents/skills/performance-optimization/SKILL.md
.agents/skills/playwright-testing/SKILL.md
.agents/skills/react-performance/SKILL.md
.agents/skills/remotion-video-production/SKILL.md
.agents/skills/security-audit/SKILL.md
.agents/skills/smooth-scroll/SKILL.md
.agents/skills/strix-security-audit/SKILL.md
.agents/skills/supabase-agent-plugin/SKILL.md
.agents/skills/superdesign-skill/SKILL.md
.agents/skills/systematic-debugging/SKILL.md
.agents/skills/taste-skill/SKILL.md
.agents/skills/threejs-3d-experience/SKILL.md
.agents/skills/ui-craft/SKILL.md
.agents/skills/ui-ux-pro-max/LICENSE
.agents/skills/ui-ux-pro-max/SKILL.md
.agents/skills/ui-ux-pro-max/references/pro-rules.md
.agents/skills/ui-ux-pro-max/references/quick-reference.md
.agents/skills/ui-ux-pro-max/scripts/search.py
.agents/skills/ux-ui-agent-skills/SKILL.md
.agents/skills/vercel-react-best-practices/SKILL.md
.agents/skills/vercel-react-best-practices/rules/async-parallel.md
.agents/skills/verification-before-completion/SKILL.md
.agents/skills/visual-regression-testing/SKILL.md
.agents/skills/web-design-guidelines/SKILL.md
.github/workflows/skills-audit.yml
.github/workflows/validate.yml
AGENTS.md
AUDIT-RUNBOOK.md
COMPATIBILITY.md
LICENSE
OFFICIAL-SOURCES-AUDIT.md
README.md
docs/COMPATIBILITY.md
docs/PANDUAN-MS.md
scripts/validate_skills.py
tests/test_validate_skills.py
```

Next: compare each retained skill's recursive directory with a pinned official upstream tree, including license and manifest; record L2 evidence only after exact comparison. Execute tests and runtime discovery independently. No destructive changes are authorized.
