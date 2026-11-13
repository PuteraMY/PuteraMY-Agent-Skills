# Integration compatibility and evidence matrix

Updated: 2026-11-12. **Not an installation certificate.**

| Integration | Distribution type | Repository evidence | Codex installed / usable | ChatGPT Work installed / usable | Blocker |
| --- | --- | --- | --- | --- | --- |
| Anthropic frontend-design | standalone skill | Original SKILL.md SHA matched; duplicate local entrypoints | Not tested | Not verified as Work plugin | Full distribution and runtime discovery |
| Impeccable | skill inside vendor plugin | Original SKILL.md SHA matched | Not tested | Not verified | Plugin manifest, assets, license, runtime |
| UI UX Pro Max | standalone skill with assets | Original SKILL.md SHA matched | Not tested | Not verified | Full scripts/data and license |
| Vercel web-design-guidelines | standalone skill | Original SKILL.md SHA matched | Not tested | Not verified | Full distribution and runtime |
| Vercel react-best-practices | standalone skill | Original SKILL.md SHA matched | Not tested | Not verified | Rules and support files |
| Emil design engineering | standalone skill | Original SKILL.md SHA matched | Not tested | Not verified | Dependencies/license |
| Emil Apple Design | standalone skill | Original SKILL.md SHA matched | Not tested | Not verified | Dependencies/license |
| Emil animate | standalone skill | Original SKILL.md SHA matched | Not tested | Not verified | Dependencies/license |
| Superpowers systematic-debugging | standalone skill | Original SKILL.md SHA matched | Not tested | Not verified | Supporting references/runtime |
| Superpowers verification-before-completion | standalone skill | Original SKILL.md SHA matched | Not tested | Not verified | Supporting references/runtime |
| Cloudflare security-audit | standalone skill with support files | SKILL.md SHA matched; 14 references, JSON schema, two validators and tests previously copied | Not tested | Not verified | Recursive upstream comparison and validator tests |
| Vercel find-skills | standalone skill | Original SKILL.md SHA matched | Not tested | Not verified | CLI runtime and discovery |
| Anti-slop | upstream Codex plugin candidate | README installation commands identified; original manifest and full package not yet checked | Not tested | Not verified | Validate manifest, six skills, license |
| Anatomy | unresolved upstream candidate | No trustworthy upstream package verified | Not tested | Not verified | Publisher/repository/source confirmation |
| Legacy assistant-authored skill directories | **unverified custom guides, not vendor integrations** | See audit list | Not certified | Not certified | Replace with complete originals if available; seek approval before archive/removal |
| GitHub, Supabase, Vercel and other connected services | connected apps / tools, **not skill packages** | Availability is environment-specific | Not established by this repository | Must verify per connection and action | Check actual app authorization and functional read/write scope |

## Verification levels

- **L0 candidate:** named integration without a validated original distribution.
- **L1 entrypoint:** exact upstream SKILL.md text/blob match. This does not establish usable installation.
- **L2 complete vendor package:** recursive manifest, support files, scripts, original plugin manifests and licensing compared against a pinned upstream revision.
- **L3 static and executable validation:** relevant vendor tests pass in a reproducible environment, with command and output recorded.
- **L4 Codex runtime:** installation/discovery and a representative non-destructive task verified in the intended Codex environment.
- **L5 Work runtime:** matching connected app/plugin identified and a permitted representative action tested in ChatGPT Work. Not every Codex skill has a Work equivalent.

No item in this matrix is certified L4 or L5. Exact file matching supports **L1 only**, even where partial supporting files are present.

## Safe installation/discovery procedure

1. Check official upstream source, publisher, license, security and full package contents; pin a revision.
2. For Codex, use the vendor-documented installation mechanism or copy the **complete** upstream skill directory into a Codex-discoverable location. Example for Vercel find-skills: `npx skills add vercel-labs/skills --skill find-skills --global`. **This command is documentation, not a command executed by this audit.**
3. In each project, verify actual discovery and run one bounded task; record runtime, command, output, errors and tested revision.
4. For ChatGPT Work, inspect the Plugin Directory and connected-app state separately; do not infer availability from a GitHub folder, CLI command or Codex plugin manifest.
5. Do not deploy, remove legacy folders, modify production, or install untrusted packages without review.

## Outstanding inventory limitation

The connected GitHub interface used for this audit can fetch known file paths but did not expose a recursive tree listing. The attempted public GitHub recursive-tree API endpoint was inaccessible. Therefore **a complete Git tree inventory has not been performed**; the audit's list of legacy directories is not exhaustive. A future run must obtain a recursive tree from an authorized GitHub interface or a local checkout (for example, `git ls-tree -r --name-only HEAD`), record the total files and classify every path. Do not treat this matrix as complete.

See [OFFICIAL-SOURCES-AUDIT.md](OFFICIAL-SOURCES-AUDIT.md) for original source URLs and detailed provenance.

## CI evidence collection — 13 November 2026

Added [`.github/workflows/skills-audit.yml`](.github/workflows/skills-audit.yml) in commit `836a0b16396e69c8c4de3b800b457fa3562b07c0`. It is a **read-only structural audit**: Python regression tests, complete tracked Git path export via `git ls-tree -r --name-only HEAD`, validator JSON output and downloadable workflow artifact. It does **not** certify full vendor distribution, plugin installation, MCP connectivity or Codex/Work runtime. The workflow's actual execution status and artifacts have **not yet been verified**; GitHub Actions permissions and execution may block it. The `git ls-tree` output is a tracked-tree snapshot, not a classification of every integration; audit the generated list before claiming complete inventory. The validator can fail on legacy folders; a failure must be investigated rather than hidden.

## Structural validator hardening — 13 November 2026, 18:00 MYT

- Commit `1b64f85167622d9515a5d706be31907fd0186da1`: reject empty skill inventories and require actual nonempty `name`/`description` frontmatter fields rather than substring matches.
- Commit `4a658c88eee4556aa78cdaa08bf77d88acb187cf`: add regression cases for zero skill directories, misleading keys and blank names.
- These are **code changes only**; tests and GitHub Actions execution have not been observed in this run. The workflow still needs a successful execution and its `tracked-tree.txt` artifact reviewed. No Codex/Work installation, full vendor package, or complete inventory claim follows from these changes.

## Evidence reliability fix — 13 November 2026, 22:00 MYT

- Commit `66a1eaae2e22f031e487f11e15e1d35e73aa8cec` makes the tracked-tree export and structural inventory run with `if: always()` after regression tests. Previously a failing regression step prevented both evidence files from being generated, so the `always()` artifact upload had little diagnostic value. The workflow also responds to changes in this compatibility matrix and the source audit document.
- **Not yet execution-verified**: the commit establishes workflow configuration only. Retrieve a completed GitHub Actions run and its `skills-structural-audit` artifact before claiming CI passed or the full tree was obtained. A failed structural validator still correctly fails the job, while preserving its JSON output for investigation.
- Repository tree completeness, vendor package recursion, licenses, genuine plugin manifests, Codex installation and Work app usability remain unresolved. No legacy deletion or production deployment is authorized.
