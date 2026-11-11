---
name: cicd-quality-gates
description: Automated build, tests and controlled release workflows.
---
# cicd-quality-gates
Source/reference: https://docs.github.com/en/actions

This is a PuteraMY-authored integration guide, not an installation of upstream packages or full third-party skills.

## Workflow
Use lint, typecheck, tests, security checks and preview smoke tests appropriate to stack. Require review before production promotion. Document rollback.

Inspect the target stack before applying. Preserve existing functionality and tests. Run real checks and record evidence. Do not deploy to production without approval.
