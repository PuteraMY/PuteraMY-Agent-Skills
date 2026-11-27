# Audit checkpoint — 2026-11-18 (Asia/Kuala_Lumpur)

## Verified repository state
- GitHub REST recursive tree `main`: SHA `cae3aa2bce5f86ffe03bfa0d84523cd64c936979`, `truncated=false`, **139 entries**, **86 blobs**, **43 SKILL.md entrypoints**.
- Audit branch `audit/2026-11-17-ci-root-cause`: SHA `1a4aa1eb368e242f71a0722a89dcf1939304fbf3`, `truncated=false`, **145 entries**, **91 blobs**, **43 SKILL.md entrypoints**.
- CI runs `44148507257` and `44148489760` on audit branch are **failure**. Earlier run `44099181768` explicitly logs eight malformed/missing frontmatter entries: `context7-documentation`, `playwright-testing`, `strix-security-audit`, `supabase-agent-plugin`, `superdesign-skill`, `taste-skill`, `ui-craft`, `ux-ui-agent-skills`. Do not mark CI green or invent vendor metadata to silence this.
- Latest branch contains `docs/CODEX-DAY-ONE-QUICKSTART.md`; its presence is **not** runtime installation evidence.

## New confirmed provenance issue — contest-relevant
`.agents/skills/remotion-video-production/SKILL.md` expressly says **“This is a PuteraMY-authored integration guide, not an installation of upstream packages or full third-party skills.”** It links to `https://github.com/remotion-dev/skills`. This is a legacy guide and **must not be counted as a genuine upstream distribution**. Preserve pending upstream mapping and explicit approval for any removal. Video production is ATLAS AI relevant, so prioritize its genuine vendor distribution investigation.

## Fresh upstream snapshots (GitHub REST recursive trees)
- `nextlevelbuilder/ui-ux-pro-max-skill` at `e59ff376a41f7ca47b7541ad5c116495cbade3ee`: 858 tree entries / 725 blobs, `truncated=false`. Includes `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `LICENSE`, data and other support files. **Do not compare 725 whole-repository blobs to a single skill package**: first select the vendor's canonical installation distribution and verify its scoped subtree and pinned hashes.
- `pbakaus/impeccable` at `d41d9860b0094dcb68030657da63461212835aaa`: 5,417 tree entries / 4,780 blobs, `truncated=false`. Includes Claude and Cursor plugin manifests and `LICENSE`. Same caveat: whole repository is not the installable skill distribution.
- Local `ui-ux-pro-max`: `SKILL.md`, `LICENSE`, `references/pro-rules.md`, `references/quick-reference.md`, `scripts/search.py` (5 blobs). Local `impeccable`: `SKILL.md`, `LICENSE` (2 blobs). **Completeness not verified.**

## Prioritized remediation (safe and non-destructive)
1. **ATLAS AI:** map Remotion guide to canonical vendor skill and dependencies; verify UI UX Pro Max/Impeccable canonical package contents and licenses; only then stage original complete files, scripts/data/manifests on a feature branch. Do not claim ChatGPT Work connection or Codex discovery from repository files.
2. **VELA:** prioritize upstream verification for systematic debugging, verification-before-completion, database architecture and automated testing; never import generic assistant-authored `SKILL.md` as vendor originals.
3. **CI:** classify legacy guide entries separately from real vendor skills and enforce a provenance manifest for vendored directories; do not forge frontmatter or delete entries.
4. **Runtime:** verify Codex discovery in an actual target project; verify ChatGPT Work connected apps/plugins independently. Record install path, supported product, exact test and outcome. Until tested, mark **unverified**.
5. Maintain unresolved source identities for packages without an authenticated upstream; require user approval before archive/removal.

## Evidence links
- Main tree: https://api.github.com/repos/PuteraMY/PuteraMY-Agent-Skills/git/trees/main?recursive=1
- Audit branch tree: https://api.github.com/repos/PuteraMY/PuteraMY-Agent-Skills/git/trees/audit/2026-11-17-ci-root-cause?recursive=1
- CI: https://github.com/PuteraMY/PuteraMY-Agent-Skills/actions/runs/44148507257
- UI UX upstream: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/e59ff376a41f7ca47b7541ad5c116495cbade3ee
- Impeccable upstream: https://github.com/pbakaus/impeccable/tree/d41d9860b0094dcb68030657da63461212835aaa

No production deploy, merge, removal or runtime installation performed in this audit.
