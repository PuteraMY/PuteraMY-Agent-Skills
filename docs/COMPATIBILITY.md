# Compatibility and verification

| Platform | Installation route | Verification required |
| --- | --- | --- |
| Codex | Project `.agents/skills/<skill>/SKILL.md` | Check skill discovery and invoke a safe dry run |
| VS Code GitHub Copilot | Project `.github/skills/<skill>/SKILL.md` | Confirm discovery in Copilot chat and invoke a safe dry run |
| ChatGPT | Supported skill/plugin workflow or manually provided context | Confirm supported capability in current product and inspect actual output |

## Runtime smoke test
Ask the agent to list the skill's workflow and review a toy component without modifying production. Verify it cites the skill's specific quality gates. Record platform version, date, result and logs.

Static checks cannot guarantee runtime compatibility.
