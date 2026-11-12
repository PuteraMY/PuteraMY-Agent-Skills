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
