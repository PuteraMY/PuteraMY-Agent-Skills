# Playwright browser automation and end-to-end testing

Upstream: https://github.com/microsoft/playwright

## Verification and scope
The upstream GitHub README was inspected on 2026-11-12. This is a locally authored PuteraMY integration guide, **not** an installed copy of the upstream software, MCP server or complete skills. Check the current upstream docs, license and compatibility before installing or running anything.

## When and how to use
For browser QA on web apps: cover critical user journeys, form validation, navigation, keyboard access, responsive viewport, loading/error states, screenshots and console/network errors. Prefer stable role-based locators, deterministic test fixtures and trace artifacts. Run against a permitted local/staging environment, never assume Playwright or browsers are installed. Use alongside browser-qa, not as a replacement.

## Quality gates
1. Inspect existing project instructions, code and environment.
2. Confirm tool availability and required authorization.
3. Pick a narrow, reversible workflow and preserve working behavior.
4. Execute appropriate checks and collect actual evidence.
5. Report commands run, results, known limitations and outstanding work. Never fabricate verification.

## Production safety
No destructive actions, secret exposure, security attacks, or production deployment without explicit approval.
