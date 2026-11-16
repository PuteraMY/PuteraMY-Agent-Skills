# Original plugin manifest evidence — 2026-11-16

Read-only verification via connected GitHub file API. The following are **original upstream files** and blob SHAs, not assistant-authored manifests. Repository recursive trees returned `truncated=false` on this run. Vendor metadata is a declaration, not proof of installation or runtime support.

| Upstream repository | Manifest | Git blob SHA | Declared version | Declared skill root | Declared type |
| --- | --- | --- | --- | --- | --- |
| [obra/superpowers](https://github.com/obra/superpowers/blob/main/.codex-plugin/plugin.json) | `.codex-plugin/plugin.json` | `b0bc1308ee4be8082cb5919660478bed2268496f` | 7.0.2 | `./skills/` | Codex plugin manifest + skills |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/blob/main/.codex-plugin/plugin.json) | `.codex-plugin/plugin.json` | `8d40a20dab4afe0aa75e378ce28f2f32990d141b` | 0.6.16 | `./skills/` | Codex plugin manifest + skills |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/.claude-plugin/plugin.json) | `.claude-plugin/plugin.json` | `18aee1918b032bd43d6b7a2daa88adfb1de33e68` | 2.15.0 | `./.claude/skills/` | Claude plugin manifest + skills |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable/blob/main/.claude-plugin/plugin.json) | `.claude-plugin/plugin.json` | `6695c10cd7624df11f78ac0f1ef733c2e5cc02b0` | 4.9.2 | `./.claude/skills/` | Claude plugin manifest + skills |

## Critical distinction
- A vendor `plugin.json` is **not** an MCP server, API integration, or evidence of a connected ChatGPT app.
- A manifest inside a GitHub repository is **not** evidence of installation in ChatGPT Work or Codex. Each requires actual installation/discovery/use checks in its own environment.
- Superpowers' original Codex manifest declares `skills: ./skills/` and references vendor assets for its interface. Copying only one SKILL.md would omit the distribution.
- Addy Osmani's Codex manifest declares `skills: ./skills/` and describes multiple engineering workflows.
- UI UX Pro Max's Claude manifest declares `skills: ./.claude/skills/`; its large local skill data/scripts must be retained for functional parity.
- Impeccable's Claude manifest declares `skills: ./.claude/skills/` and 24 commands; a single SKILL.md is insufficient to assume full command support.

## Verification status
- **Verified:** source repository tree accessible; exact original manifest content and blob SHA fetched; metadata read.
- **Unverified:** vendored support-file completeness in PuteraMY repo; manifest compatibility with any installed host; execution; automated tests; security.
- **No files installed or replaced** in this run. Do not overwrite local modifications or remove unresolved pseudo-skills without review/approval.
- Next: inspect original LICENSE, pinned tree paths and dependency scripts; stage full upstream vendor distributions in a reviewable branch; test each host separately. Preserve all existing projects and never deploy production as part of this audit.

Tree evidence: [local repository at prior baseline](https://github.com/PuteraMY/PuteraMY-Agent-Skills/tree/3eda63c0e5aac318b0e4706eb228d97947c32ed6), [UI UX Pro Max upstream tree](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/e59ff376a41f7ca47b7541ad5c116495cbade3ee), [Impeccable upstream tree](https://github.com/pbakaus/impeccable/tree/d41d9860b0094dcb68030657da63461212835aaa).
