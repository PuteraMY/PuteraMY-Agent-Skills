# Official upstream integration inventory

Status: **migration in progress; not a verified installation**.

This is an audit record, not an agent skill, plugin manifest, or substitute for upstream installation. Do not describe any item as installed in ChatGPT Work or Codex solely because files exist in this repository.

## Verified upstream SKILL.md copies (entrypoints only)

| Local directory under .agents/skills | Upstream SKILL.md | Status |
|---|---|---|
| frontend-design | https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md | Entry copied; verify complete support files |
| anthropic-frontend-design | https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md | Duplicate; consolidate after dependency review |
| impeccable | https://github.com/pbakaus/impeccable/blob/main/plugin/skills/impeccable/SKILL.md | Entry copied; plugin assets not fully verified |
| ui-ux-pro-max | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/.claude/skills/ui-ux-pro-max/SKILL.md | Entry copied; scripts/data not fully verified |
| web-design-guidelines | https://github.com/vercel-labs/agent-skills/blob/main/skills/web-design-guidelines/SKILL.md | Entry copied |
| vercel-react-best-practices | https://github.com/vercel-labs/agent-skills/blob/main/skills/react-best-practices/SKILL.md | Entry copied; rule files not fully verified |
| emil-skills | https://github.com/emilkowalski/skills/blob/main/skills/emil-design-eng/SKILL.md | Entry copied; dependencies not audited |
| apple-design-skill | https://github.com/emilkowalski/skills/blob/main/skills/apple-design/SKILL.md | Entry copied; dependencies not audited |
| motion-animation | https://github.com/emilkowalski/skills/blob/main/skills/animate/SKILL.md | Entry copied; dependencies not audited |
| systematic-debugging | https://github.com/obra/superpowers/blob/main/skills/systematic-debugging/SKILL.md | Entry copied; dependencies not audited |
| verification-before-completion | https://github.com/obra/superpowers/blob/main/skills/verification-before-completion/SKILL.md | Entry copied; dependencies not audited |

## Custom guides requiring removal or replacement

Do not treat these as upstream skills until compared against original vendor content: design-system, taste-skill, ux-ui-agent-skills, superdesign-skill, ui-craft, design-to-code-fidelity, fullstack-development, database-architecture, supabase-agent-plugin, auth-authorization-hardening, gsap-scroll-storytelling, gsap-official-patterns, threejs-3d-experience, smooth-scroll, animation-performance-qa, remotion-video-production, lottie-rive-animation, 3d-asset-optimization, browser-qa, automated-testing, visual-regression-testing, deployment-qa, playwright-testing, security-audit, strix-security-audit, react-performance, performance-optimization, core-web-vitals-seo, cicd-quality-gates, context7-documentation. This list comes from documented references and is **not** a complete recursive Git tree audit.

## Official integration model

- **ChatGPT Work:** Install vendor plugins from the ChatGPT Plugin Directory, and authorize any required apps. Files in this GitHub repository do not install a ChatGPT plugin.
- **Codex:** Use upstream plugin distributions where available, or install complete original skill folders in a Codex-discoverable skills directory. A repository-local .agents/skills folder is discovered when Codex runs in that repository; this shared repo does not automatically apply to unrelated projects.
- **MCP and other tools:** Use their original supported setup. Do not invent SKILL.md wrappers and call them official.
- **No repackaging claim:** A custom plugin manifest bundling third-party skills would be a PuteraMY distribution, not an upstream-official plugin. Verify upstream licensing and distribution permissions first.

References: https://learn.chatgpt.com/docs/build-skills and https://help.openai.com/en/articles/20001256-plugins-in-chatgpt .

## Completion criteria

1. Enumerate the complete Git tree and classify every SKILL.md and associated support asset.
2. For each retained third-party skill, compare against original upstream files, license, dependencies and install method.
3. Remove or archive assistant-authored guides only after validating replacements and checking AGENTS.md references.
4. Test Codex discovery and relevant commands in a real Codex environment; verify Work plugin availability and account installation separately.
5. Report unsupported/unavailable upstream plugins honestly. Do not declare 100% until the remaining list is empty and required tests have run.

## Live upstream byte-for-byte checks — 12 November 2026

The following four **entrypoint files** were fetched from both this repository and their upstream repositories and compared for exact text equality (matching Git blob SHA). This does **not** verify complete supporting files or runtime installation:

| Local skill entrypoint | Upstream original | Exact match |
| --- | --- | --- |
| `frontend-design/SKILL.md` | `anthropics/skills/skills/frontend-design/SKILL.md` | YES |
| `impeccable/SKILL.md` | `pbakaus/impeccable/plugin/skills/impeccable/SKILL.md` | YES |
| `web-design-guidelines/SKILL.md` | `vercel-labs/agent-skills/skills/web-design-guidelines/SKILL.md` | YES |
| `vercel-react-best-practices/SKILL.md` | `vercel-labs/agent-skills/skills/react-best-practices/SKILL.md` | YES |

**Still unverified:** all supporting directories, third-party licenses across the full collection, complete Git tree inventory, Work plugin installation, and Codex runtime discovery. Never interpret this comparison as completion.

## New user-requested upstream candidates — 12 November 2026

These are **requested additions**, not installed or verified complete:

| Candidate | Source | Verified observation | Next action |
| --- | --- | --- | --- |
| Cloudflare Security Audit | https://github.com/cloudflare/security-audit-skill | Original README accessible; documents `npx skills add https://github.com/cloudflare/security-audit-skill --skill security-audit` and an MIT license; repository root `SKILL.md` was not accessible by direct fetch | Locate complete upstream skill folder and required audit reference files, verify license and Codex support before copying/installing |
| Anatomy | https://github.com/heresryan22/anatomy | Original GitHub README and guessed skill paths were not accessible in connected GitHub lookup | Verify repo existence, actual publisher and official installation instructions before adding; do not invent files |
| Anti-slop | https://github.com/miqdadbadjuber/anti-slop | Original README accessible; advertises `npx skills add miqdadbadjuber/anti-slop` and Codex plugin commands `codex plugin marketplace add miqdadbadjuber/anti-slop`, then `codex plugin add antislop@anti-slop` | Verify original plugin manifest, six skill folders and required files; test Codex installation in target environment; Work installation remains separate and unverified |

Security audit skills must be used only on explicitly authorized targets, with scoped non-destructive testing and no production deployment.

## Cloudflare security-audit full vendor folder — 12 November 2026

Copied the original upstream `skills/security-audit/` package from `cloudflare/security-audit-skill` into `.agents/skills/cloudflare-security-audit/`, including `SKILL.md`, 14 markdown support references, JSON report schema, two Node.js validators and their two test files, plus upstream root MIT `LICENSE`. These are original upstream files, not assistant-written wrappers. The previously listed Cloudflare entrypoint-only blocker is superseded by this package copy. **Still to verify:** exact file count/tree against upstream, execute validator tests in a suitable Node.js environment, and install/test agent discovery in the user's actual Codex environment. GitHub copy is not a ChatGPT Work plugin installation.

## Vercel find-skills — 12 November 2026

Added `.agents/skills/find-skills/SKILL.md` verbatim from `vercel-labs/skills/skills/find-skills/SKILL.md` (upstream blob SHA `a41bdd074bb587afd861332cf2f473f3154de4d7`). Source: https://github.com/vercel-labs/skills/tree/main/skills/find-skills. The upstream repository is the skills.sh CLI and documents Codex support. This is a **skill**, not proof of a ChatGPT Work plugin or a global Codex installation. The skill's discovery/install commands require a supported CLI runtime and should be tested in the target environment. Discovering skills does not establish that a discovered skill is safe; inspect provenance, license and contents before installation.

## Audit run — 12 November 2026, evening (Malaysia)

- **Verified regression:** previous `scripts/validate_skills.py` hard-coded exactly eight skill directories and demanded assistant-authored headings. This contradicted the migration policy and would fail once authentic upstream skills were added. Replaced it with a dynamic, read-only structural inventory. Commit: `e2a8e5a3807f4b2faa7b87904727ee639361e758`.
- New validator enumerates all immediate skill directories, records recursive file paths and counts, checks only basic YAML frontmatter delimiters/name/description, and attempts `git ls-files -z` for a complete **tracked-file** inventory. JSON output: `python3 scripts/validate_skills.py --json`. It does **not** claim provenance, dependency completeness, runtime installation or vendor compatibility. Untracked/ignored files are outside `git ls-files`.
- **Execution limitation:** GitHub connector can fetch named files but this run did not obtain a recursive tree listing. Direct checkout failed because the execution container could not resolve `github.com`. Consequently neither a full-tree inventory nor a run of the updated validator against a checkout was completed. The validator is committed but **not yet runtime-tested**. Do not record a passing test.
- **Concrete dependency warning:** vendored `impeccable/SKILL.md` instructs users to run a bundled `scripts/impeccable` launcher and read files under `reference/`. Matching its `SKILL.md` alone is insufficient; binary, launcher, references, license and original plugin manifest must be compared before L2 certification. Avoid executing a downloaded launcher without reviewing its origin and behavior.
- No vendor skills were removed, no project repository was changed, no production deployment occurred. Next run should acquire the full Git tree through a suitable tree API or authenticated checkout, run the new validator, then reconcile all missing vendor support files against pinned upstream revisions.

## Audit run — 13 November 2026 (Malaysia)

- Rechecked the actual repository policy, compatibility matrix and validator source through the connected GitHub API. The repository still explicitly labels L4 Codex and L5 Work as unverified.
- **Executed an isolated smoke test of the current validator source** in a temporary fixture, not a repository checkout: a valid frontmatter fixture produced JSON `status: PASS` and a malformed fixture produced `status: FAIL`. This only confirms those two paths in isolation; it is **not** a successful whole-repository test.
- Added three regression tests in `tests/test_validate_skills.py` (valid fixture, malformed frontmatter, missing entrypoint). Commit `e5461de8f070189b325757fca4038e169d206412`. **The newly committed test suite has not yet been executed in a checkout**, so no passing test-suite claim is made.
- Retried `git ls-remote https://github.com/PuteraMY/PuteraMY-Agent-Skills.git HEAD` in the execution container; DNS lookup failed (`Could not resolve host: github.com`). The connected GitHub interface still offers named-file reads and commits but no recursive tree read. Full-tree inventory remains blocked.
- No upstream vendor files were replaced or removed, no production deployments, and no Codex/Work installation claims. Next: run `python3 -m unittest discover -s tests -v` in a real checkout, obtain recursive `git ls-tree -r --name-only HEAD`, compare all vendor files at pinned revisions, and separately verify real runtime discovery.
