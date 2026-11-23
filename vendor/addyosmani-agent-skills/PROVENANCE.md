# Upstream provenance — frontend-ui-engineering

- Vendor: Addy Osmani
- Upstream repository: https://github.com/addyosmani/agent-skills
- Pinned upstream Git commit: `8c99fa36d90068c82d547f7c12a9d67a3e95f4ee`
- Upstream path: `skills/frontend-ui-engineering/SKILL.md`
- Upstream blob SHA: `556b9878808486abb0d3e39daa985e6e34fa341c`
- Original license: `LICENSE` (MIT; blob SHA `d67778ada6b9cda6227e9130da182c13e73c8b2e`)
- Upstream tree check: only one file exists below `skills/frontend-ui-engineering/` at the pinned commit.
- Local vendored path: `vendor/addyosmani-agent-skills/skills/frontend-ui-engineering/SKILL.md`

## Evidence boundary

This is a verbatim, pinned copy of a **standalone skill entrypoint**, with its original upstream license preserved. It is not a complete installation of the vendor's **plugin distribution**; the upstream repository also has `.codex-plugin/plugin.json`, `.claude-plugin/plugin.json`, and `plugin.json`. The three original manifests are now preserved at their original relative paths in this vendor snapshot. However, the rest of the upstream plugin distribution (other skills, commands, evals and support files) has **not** been copied; the manifest references are therefore incomplete. **Do not install this partial snapshot as a plugin.** No plugin installation or runtime functionality is claimed.

No runtime discovery was performed. **Codex installation: unverified. ChatGPT Work availability: unverified.** The source is not an MCP server or a connected ChatGPT app.

## Safe discovery and installation

1. Check the target environment's current documented skill discovery locations and permission requirements.
2. Install or register the unmodified `frontend-ui-engineering` directory through the environment's supported skill mechanism; preserve the upstream `SKILL.md` and license.
3. Restart/reload discovery only when the environment's documented workflow requires it.
4. Verify the skill appears in the runtime's discovered skills list, invoke it on a disposable test task, and record the result.
5. For **plugin** installation, use the original upstream plugin package and manifests instead of treating this standalone skill copy as a plugin.
6. Never infer ChatGPT Work connection from a repository file; inspect actual connected apps and their permissions.

No project deployment, branch merge, or deletion is authorized by this provenance note.

## Original manifest evidence (pinned upstream)

- `.codex-plugin/plugin.json` blob `35323f5f6305f5d8f56844fcb26100b4ca12e326`
- `.claude-plugin/plugin.json` blob `d04705d5bbc8c200e4d46c5c754403a1dca95c9d`
- `plugin.json` blob `9825d67e5b89a9ac6ac2b0a996b84683a5f57efb`

**Next:** obtain the complete pinned upstream tree, including all manifest-referenced paths, and verify integrity before considering plugin installation. Standalone skill files and plugin manifests must be evaluated independently.


## Additional pinned upstream skills imported 2026-11-23

All paths below were fetched from the same pinned upstream commit above and stored verbatim under this vendor directory:

| Original upstream path | Git blob SHA |
| --- | --- |
| `skills/security-and-hardening/SKILL.md` | `c714f94a5ca2a9e73429e66ef624ef09d48088df` |
| `skills/security-and-hardening/references/hardening-patterns.md` | `34b65e524c48f878d4cdc4b93c73ea493506de76` |
| `skills/browser-testing-with-devtools/SKILL.md` | `ca0044e859e5637c33250dbba1fc1a24540b7ad3` |
| `skills/performance-optimization/SKILL.md` | `296cf3f79eaa4c910cae44ecd50fcc4246e2b9d5` |
| `skills/performance-optimization/references/optimization-patterns.md` | `63e27bcc7a051c3dc23c164f146f374e119874cc` |
| `skills/test-driven-development/SKILL.md` | `5dc0ae7e4ae4e4f6d60a6815f2643cda6ba3e99c` |

The pinned upstream Git tree was inspected for these four skill directories: security-and-hardening and performance-optimization each contain their listed reference file, while browser-testing-with-devtools and test-driven-development each contain only SKILL.md. These are **standalone skill directories**, not evidence of an installed plugin or MCP server. The vendor's full plugin distribution remains incomplete here. Codex and ChatGPT Work runtime discovery remain **UNVERIFIED**.

