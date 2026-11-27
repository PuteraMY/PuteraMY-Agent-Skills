# Upstream package topology: taste-skill and ui-craft (2026-11-18)

**Scope:** GitHub Git Trees API, recursive and `truncated=false`; source topology only. This is not installation, runtime discovery, license approval or successful CI.

## Baseline

- Local `main`: tree `cae3aa2bce5f86ffe03bfa0d84523cd64c936979`, 139 entries, 86 blobs, 43 `.agents/skills/*/SKILL.md` entrypoints.
- Audit branch before this report: tree `2af36144e78dd8b6d266c9556131ff9ec6722650`, 148 entries, 94 blobs, 43 entrypoints.
- Most recent observed audit-branch CI runs `44280631887` and `44280621306` both failed. Previously retrieved validation logs identify eight malformed/missing frontmatter entries. A passing runtime check has **not** been observed.

## Taste Skill — high priority visual design, ATLAS AI

- Source: https://github.com/Leonxlnx/taste-skill
- Pinned Git tree SHA: `f6b76575f949707b4e3c37cd86cb44b0b98643e8` (non-truncated).
- Full upstream tree has **1,663 tracked blobs**. The `skills/taste-skill/` subtree has **1,631 blobs**. Do not assume the full subtree is the minimum supported installation package without reading its original install docs.
- Actual vendor entrypoint: `skills/taste-skill/SKILL.md`.
- Vendor manifests: `.agents/plugins/marketplace.json`, `.claude-plugin/marketplace.json`, `.codex-plugin/plugin.json`. Root `LICENSE` exists.
- Local `.agents/skills/taste-skill/SKILL.md` is explicitly a PuteraMY-authored guide, **not** the upstream entrypoint. It fails the structural validator.
- **Action:** determine vendor-supported minimal installation layout, inspect dependencies/assets, license and Codex manifest; then stage the complete original distribution in a separate branch. Never replace with a hand-written shim. Confirm actual Codex discovery and smoke test separately.

## UI Craft — visual and UI engineering, ATLAS AI and future projects

- Source: https://github.com/educlopez/ui-craft
- Pinned Git tree SHA: `c1e556ed843b5aad057678f9a152fbcf756eb62c` (non-truncated).
- Full upstream tree has **1,138 tracked blobs**, including several distinct host-specific skill trees.
- Vendor Codex paths include `.codex/skills/ui-craft/SKILL.md`, `.codex/skills/ui-craft-dense-dashboard/SKILL.md`, `.codex/skills/ui-craft-editorial/SKILL.md`, `.codex/skills/ui-craft-minimal/SKILL.md`, and additional skill entrypoints.
- Vendor plugin manifests include `.claude-plugin/plugin.json` and `.codex-plugin/plugin.json`. Root `LICENSE` exists.
- Local `.agents/skills/ui-craft/SKILL.md` is an explicitly PuteraMY-authored guide and fails the structural validator; it must not be treated as a vendor skill.
- **Action:** choose the upstream vendor's supported Codex distribution rather than mixing Claude/Cursor/Gemini/OpenCode copies; preserve vendor files and licensing, run tests and verify discovery.

## Migration decisions and blockers

1. **Do not mass-copy 1,000+ files into a shared skill folder blindly.** Upstream repository size is not necessarily the install package size. Determine original supported distribution from README/manifest and include all its required files.
2. **Do not force green CI by adding invented YAML frontmatter to locally authored guides.** Keep the eight failures visible until genuine migration or explicit classification into non-skill documentation.
3. Track standalone skill vs Codex/Claude plugin vs MCP server vs ChatGPT connected app separately. Vendor manifests do not prove host installation.
4. No files deleted or moved; no production deployment; no merge; no installation claims. Next work: source installation docs, package manifest and license checks; vendor-complete staged migration; CI and per-host smoke tests.
