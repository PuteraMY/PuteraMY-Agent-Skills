# Agent Instructions

Use the appropriate skill from `.agents/skills/<name>/SKILL.md` when relevant. Read the file before beginning work. Inspect existing code, minimize changes, run available tests, and report evidence and limitations. Never modify unrelated repositories, expose secrets, or deploy to production without explicit approval.

## Premium UI/UX workflow

For every user-facing design or frontend task, read and apply `.agents/skills/ui-ux-pro-max/SKILL.md` from the shared PuteraMY-Agent-Skills repository together with `frontend-design` and `design-system`. This is the verified PuteraMY integration guide; the full upstream searchable data/scripts are not installed by this commit. Do not claim otherwise. Prioritize accessible, responsive, distinctive, well-tested product UI.

## Premium engineering quality gates (shared PuteraMY skills)

Before related work, fetch and read these guides from `PuteraMY/PuteraMY-Agent-Skills/.agents/skills/`: `ui-ux-pro-max`, `web-design-guidelines`, `browser-qa`, `systematic-debugging`, and `verification-before-completion`. Use `react-performance` only when the project actually uses React/Next.js. Apply existing `frontend-design`, `design-system`, `security-audit`, `automated-testing`, and `deployment-qa` as applicable.

These are verified repository-local PuteraMY integration guides, not proof of installation of third-party CLI assets, Playwright browser binaries, or the complete upstream skill datasets. For actual upstream installation, review the source and install in the target development environment; verify resulting files. Before marking work complete, report executed tests, visual QA evidence, known limitations and deployment status. Do not alter production without approval.
