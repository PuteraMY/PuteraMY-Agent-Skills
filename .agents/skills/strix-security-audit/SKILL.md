# Authorized AI-assisted security testing with Strix

Upstream: https://github.com/usestrix/strix

## Verification and scope
The upstream GitHub README was inspected on 2026-11-12. This is a locally authored PuteraMY integration guide, **not** an installed copy of the upstream software, MCP server or complete skills. Check the current upstream docs, license and compatibility before installing or running anything.

## When and how to use
Use only for systems explicitly owned by or authorized for the user, preferably local or isolated staging. First agree on targets, scope, rate limits and test window. Do not attack third-party or production targets without specific authorization. Use non-destructive scanning, preserve logs, validate findings manually, redact secrets and propose fixes before applying. Do not imply Strix is installed or that a pentest was run merely because this guide exists.

## Quality gates
1. Inspect existing project instructions, code and environment.
2. Confirm tool availability and required authorization.
3. Pick a narrow, reversible workflow and preserve working behavior.
4. Execute appropriate checks and collect actual evidence.
5. Report commands run, results, known limitations and outstanding work. Never fabricate verification.

## Production safety
No destructive actions, secret exposure, security attacks, or production deployment without explicit approval.
