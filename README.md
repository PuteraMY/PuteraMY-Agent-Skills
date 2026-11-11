# PuteraMY Agent Skills

Eight reusable skills for software design, development, testing, security and deployment.

## Skills
- **frontend-design** — Build distinctive, accessible, responsive interfaces.
- **design-system** — Create coherent reusable design foundations.
- **fullstack-development** — Implement safe, maintainable end-to-end features.
- **database-architecture** — Design reliable PostgreSQL schemas for Supabase or Neon.
- **security-audit** — Identify and prioritize web application security risks.
- **automated-testing** — Build reliable tests across unit, integration and E2E levels.
- **performance-optimization** — Improve real user performance without sacrificing usability.
- **deployment-qa** — Verify GitHub Actions and Vercel release readiness.

## Installation

**Codex:** Copy selected directories from `.agents/skills/` to the target project's `.agents/skills/`. Add relevant guidance to `AGENTS.md`.

**VS Code / GitHub Copilot:** Copy selected directories to the target project's `.github/skills/`; confirm discovery in your installed Copilot version. This repository uses `.agents/skills/` as the canonical source.

**ChatGPT:** GitHub repositories are not automatically installed as ChatGPT skills. Use supported skill/plugin integration when available, or provide a relevant SKILL.md as context.

## Validate
Run `python3 scripts/validate_skills.py`. GitHub Actions runs the same check on pushes and pull requests. This is **static validation**, not proof of runtime compatibility.

## Security
Review skills before running; never commit secrets. Require explicit approval for production changes.

## License
MIT.
