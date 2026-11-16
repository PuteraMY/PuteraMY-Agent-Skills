# October 2026 Claude Code Top 10 — source verification queue

Audit date: 2026-11-16
Repository baseline: e076aa25c520035479e06b54cc09077459929b2c
Source: user-provided social media screenshot (rankings and star counts are unverified claims).

This is a non-installing discovery record. Repository existence and top-level GitHub license metadata are NOT proof that an individual skill is a complete upstream distribution, compatible, installed, or usable in ChatGPT Work or Codex.

| Screenshot entry | Candidate upstream | GitHub repository verified | GitHub top-level license | Local inventory | Next gate |
| --- | --- | --- | --- | --- | --- |
| Superpowers | https://github.com/obra/superpowers | Yes | MIT | No top-level superpowers skill directory; related component names exist | Inspect full upstream plugin manifests, skills, hooks, support files and Codex instructions; do not copy partial bundle |
| Ponytail | https://github.com/DietrichGebert/ponytail | Yes | MIT | Not present under this name | Verify skill paths, license coverage, and actual installer |
| UI UX Pro Max | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill | Yes | MIT | .agents/skills/ui-ux-pro-max/SKILL.md present | Compare complete scripts/data/references against pinned upstream tree; previously flagged incomplete |
| Graphify | https://github.com/Graphify-Labs/graphify | Yes | Apache-2.0 | Not present under this name | Classify CLI/tool versus skill/plugin; verify dependencies and provenance |
| Caveman | Unresolved | Not yet verified | Unknown | Not present under this name | Locate exact original upstream, not an unrelated similarly named package |
| Addy Osmani Skills | https://github.com/addyosmani/agent-skills | Yes | MIT | Not present under this name | Identify individual original skills and support files |
| Understand Anything | Unresolved | Not yet verified | Unknown | Not present under this name | Locate exact upstream and check source/license |
| Awesome Claude Skills | Unresolved (ambiguous curated-list name) | Not yet verified | Unknown | Not present under this name | Identify exact repository; do not treat curated list as installable skill |
| Archify | Unresolved | Not yet verified | Unknown | Not present under this name | Identify exact original upstream |
| Impeccable | https://github.com/pbakaus/impeccable | Yes | Apache-2.0 | .agents/skills/impeccable/SKILL.md present | Compare complete upstream distribution and integration instructions |

## Evidence and scope
- GitHub REST repository metadata for six verified upstream repositories was fetched through the connected GitHub integration on 2026-11-16.
- GitHub REST recursive tree for PuteraMY/PuteraMY-Agent-Skills at e076aa2 returned truncated=false, 83 tracked blobs and 43 SKILL.md entrypoints.
- Screenshot GitHub star counts are **not independently validated** and are not installation criteria.
- No upstream files have been copied or modified in this audit; no runtime installation, CI test or Codex/ChatGPT Work compatibility has been demonstrated by this record.

## Next safe work
1. Prioritize Superpowers, UI UX Pro Max, Addy Osmani Skills and Impeccable for ATLAS AI, but retain applicability to every future project.
2. Pin upstream commits, inventory complete trees and compare paths plus hashes, licenses and original plugin manifests.
3. Separate standalone skills, plugin packages, CLIs, MCP servers and connected apps; never invent SKILL.md wrappers.
4. Repair or add only complete authorized upstream distributions with original vendor support files, preferably through reviewable PRs.
5. Test repo validation and then real Codex and ChatGPT Work discovery/use separately. Keep unsupported environments marked unverified.
6. Seek user approval before archiving or removing unresolved legacy entries. No production deployment or destructive changes.
