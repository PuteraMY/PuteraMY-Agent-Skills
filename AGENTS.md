# Agent Instructions — PuteraMY upstream-only policy

## Mission

Support ATLAS AI and other projects using **genuine original upstream** skills, plugins and MCP integrations. **Do not write or substitute assistant-authored SKILL.md files for vendor packages.** The audit and verified upstream URLs are recorded in [OFFICIAL-SOURCES-AUDIT.md](OFFICIAL-SOURCES-AUDIT.md).

## Before using any integration

1. Identify the **actual vendor distribution type**: skill, plugin, MCP server or ordinary software tool.
2. Verify original source repository, license, complete files/scripts/data, supported installation instructions and required credentials.
3. Use only the original vendor content for vendored skills. Do not mistake a copied entrypoint for a fully installed skill.
4. Check whether the current execution environment actually discovers the skill or has the plugin/tool connected; report unverified status rather than assuming.
5. Use relevant skills selectively, not all by default. Follow project-local instructions and run appropriate tests.

## Current repository status

Some files under `.agents/skills/` are verified **upstream SKILL.md entrypoint copies**, but their support files and functional installation have **not** all been verified. Other files are legacy assistant-authored integration guides and **must not be represented as official vendor skills**. See the audit for a non-exhaustive classification. Do not use unverified guides as proof of capability.

## ChatGPT Work and Codex

Work plugin installation and Codex skill discovery are **separate**. GitHub files do not install Work plugins. A skill checked into this repository is not automatically available to Codex working in a different repository. Follow the vendor's actual supported installation method for each environment and test it there.

## Quality and safety

Inspect existing project code, preserve functionality, minimize changes, verify security/accessibility/performance where relevant, run available tests and report evidence plus limitations. Never expose secrets, make destructive changes or deploy to production without explicit approval. Never run intrusive security tests against unauthorized targets.

## Migration completion rule

Do not claim 100% complete until the complete repository tree has been inventoried, every retained skill has been verified against its full original upstream distribution and license, custom pseudo-skills have been resolved, and Work/Codex installations have been tested separately. Document blockers rather than inventing replacements.
