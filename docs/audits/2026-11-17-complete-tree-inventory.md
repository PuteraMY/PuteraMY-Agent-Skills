# Complete tracked-tree inventory — 2026-11-17

Source: GitHub REST `GET /repos/PuteraMY/PuteraMY-Agent-Skills/git/trees/main?recursive=1`, tree SHA `cae3aa2bce5f86ffe03bfa0d84523cd64c936979`, `truncated=false`.

This is a **tracked-file inventory**, not an installation audit. Directories and file counts alone cannot certify original upstream provenance, license coverage, completeness, compatibility, or actual installation.

## Baseline counts
- 139 Git tree entries, including directories
- 86 tracked blobs (files)
- 43 named directories under `.agents/skills/`
- 70 files under those directories; 16 other repository files
- 38/43 skill directories contain only one tracked file; 5 contain multiple files
- 43 skill directories must not be interpreted as 43 complete upstream packages

## Multi-file skill directories
| Directory | Tracked files |
| --- | ---: |
| anthropic-frontend-design | 2 |
| cloudflare-security-audit | 21 |
| impeccable | 2 |
| ui-ux-pro-max | 5 |
| vercel-react-best-practices | 2 |

## Single-file skill directories
3d-asset-optimization, animation-performance-qa, apple-design-skill, auth-authorization-hardening, automated-testing, browser-qa, cicd-quality-gates, context7-documentation, core-web-vitals-seo, database-architecture, deployment-qa, design-system, design-to-code-fidelity, emil-skills, find-skills, frontend-design, fullstack-development, gsap-official-patterns, gsap-scroll-storytelling, lottie-rive-animation, motion-animation, performance-optimization, playwright-testing, react-performance, remotion-video-production, security-audit, smooth-scroll, strix-security-audit, supabase-agent-plugin, superdesign-skill, systematic-debugging, taste-skill, threejs-3d-experience, ui-craft, ux-ui-agent-skills, verification-before-completion, visual-regression-testing, web-design-guidelines.

## Repository files outside skill directories
`.github/workflows/skills-audit.yml`, `.github/workflows/validate.yml`, `AGENTS.md`, `AUDIT-RUNBOOK.md`, `COMPATIBILITY.md`, `LICENSE`, `OFFICIAL-SOURCES-AUDIT.md`, `README.md`, `TOP-10-CLAUDE-SKILLS-AUDIT.md`, `docs/COMPATIBILITY.md`, `docs/ORIGINAL-PLUGIN-MANIFEST-EVIDENCE-2026-11-16.md`, `docs/PANDUAN-MS.md`, `docs/UPSTREAM-PACKAGE-GAPS-2026-11-15.md`, `docs/UPSTREAM-TREE-COMPARISON-2026-11-16.md`, `scripts/validate_skills.py`, `tests/test_validate_skills.py`.

## Verification gates and blockers
1. **Provenance:** For each retained item, record original vendor URL, pinned commit, exact original relative path, license and tree/file hashes; classify copied/adapted/pseudo-skill distinctly. A repository-level license is not necessarily sufficient for bundled third-party files.
2. **Completeness:** Compare all original support files, data, scripts, dependencies and manifests, not only `SKILL.md`. UI UX Pro Max (5 local files) and Impeccable (2 local files) remain high-priority incomplete candidates per earlier upstream comparisons.
3. **Type:** A directory called `supabase-agent-plugin` or `context7-documentation` is **not evidence** of a vendor plugin or MCP server. Verify actual manifest/server implementation independently. Do not invent wrappers.
4. **Validation:** Existing `scripts/validate_skills.py` checks structural frontmatter and is **not** a provenance, license or runtime validator. Its tests likewise do not certify installation. The earlier eight invalid entrypoints remain unresolved until corrected with authentic upstream packages or explicitly separated without destructive deletion.
5. **Runtime:** Record actual successful tool discovery and invocation separately for Codex and ChatGPT Work; neither can be inferred from this Git tree or from upstream plugin manifests. Connected ChatGPT apps are a separate installation/authorization path.
6. **Safe remediation:** Work in reviewable branches/PRs. Do not merge, deploy, remove or archive unresolved files without approval. Prioritize contest-critical packages first, then the whole future-project collection.

## This audit's limitations
The inventory was checked against `main`, not an installed agent environment. This document is added to draft PR #1; it does not change existing skills, fix CI, or certify runtime compatibility.
