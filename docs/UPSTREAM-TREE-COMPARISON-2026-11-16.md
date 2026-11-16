# Upstream tree/hash comparison — 2026-11-16

Read-only GitHub REST recursive tree comparisons against the repository default branch. Trees were returned with `truncated=false`. No installation or runtime claims follow from this check.

| Repository | Tree SHA | Tree entries | Compared distribution | Upstream blobs | Local blobs | Upstream paths absent locally | Same-path Git blob SHA mismatches |
| --- | --- | ---: | --- | ---: | ---: | ---: | ---: |
| PuteraMY/PuteraMY-Agent-Skills | d94885360c5a7008eef639c164839176da4868a1 | 137 | Complete local tree | — | — | — | — |
| nextlevelbuilder/ui-ux-pro-max-skill | e59ff376a41f7ca47b7541ad5c116495cbade3ee | 858 | .claude/skills/ui-ux-pro-max/ → .agents/skills/ui-ux-pro-max/ | 78 | 5 | 74 | 2 |
| pbakaus/impeccable | d41d9860b0094dcb68030657da63461212835aaa | 5417 | .agents/skills/impeccable/ → .agents/skills/impeccable/ | 69 | 2 | 68 | 1 |
| obra/superpowers | 22f0b463e7a5e579904dd6211a520321035526f7 | 308 | skills/ | 80 | Not installed as complete package | Not compared | Not compared |
| addyosmani/agent-skills | 39b723ceebf81474d0557c1fecd01eddab585563 | 368 | skills/ | 33 | Not installed as complete package | Not compared | Not compared |

The 'absent' and 'mismatch' columns are independent: a local extra file can coexist with a missing upstream path, and a same-path mismatch may be a local modification or different upstream revision, not necessarily corruption. In UI UX Pro Max, mismatches include `SKILL.md` and `scripts/search.py`; in Impeccable, `SKILL.md`. These were compared by Git blob SHA, not executable behavior.

## Distribution and classification evidence
- Superpowers includes upstream `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`, `.agents/plugins/marketplace.json`, `hooks/`, `scripts/`, `skills/`, `LICENSE`. **Plugin distribution plus skills**, not a single SKILL.md.
- Addy Osmani Agent Skills includes upstream `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`, `plugin.json`, `scripts/`, `skills/`, `LICENSE`. **Plugin distribution plus skills**.
- UI UX Pro Max includes `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, and a skill with extensive `data/` and `scripts/` dependencies. **Skill plus plugin distribution**.
- Impeccable includes `.claude-plugin/plugin.json`, `.agents/skills/impeccable/agents/`, `reference/`, and additional vendor files. **Skill plus plugin distribution**.
- An upstream plugin manifest does not prove the plugin is installed or that ChatGPT Work supports that manifest. MCP server/connected-app status must be tested separately.
- These are source-tree facts, **not successful installation, execution, or security verification**.

## Next actions
1. Fetch and pin upstream LICENSE and manifest contents; inspect installation instructions and dependencies.
2. Replace partial distributions with complete, original upstream packages only after review, preserving vendor paths, license, provenance and support files. Avoid overwriting local files without assessing their modifications.
3. Run local validation and isolated tests. Verify Codex and ChatGPT Work independently with actual tool discovery and usage evidence.
4. Keep unlocated Caveman, Understand Anything, Awesome Claude Skills and Archify as unresolved. Do not archive or remove without approval.
5. Preserve all working projects; no production deployment or destructive change.

Evidence URLs: https://github.com/PuteraMY/PuteraMY-Agent-Skills/tree/d94885360c5a7008eef639c164839176da4868a1 ; https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/e59ff376a41f7ca47b7541ad5c116495cbade3ee ; https://github.com/pbakaus/impeccable/tree/d41d9860b0094dcb68030657da63461212835aaa ; https://github.com/obra/superpowers/tree/22f0b463e7a5e579904dd6211a520321035526f7 ; https://github.com/addyosmani/agent-skills/tree/39b723ceebf81474d0557c1fecd01eddab585563
