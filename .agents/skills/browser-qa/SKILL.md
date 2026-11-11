---
name: browser-qa
description: End-to-end browser verification for web applications, including mobile and accessibility checks.
---
# Browser QA
Use Playwright or an available real browser when the environment supports it. This is a workflow guide; Playwright binaries are not installed by this file.

Inspect project scripts and test configuration. Cover page load, primary task, navigation, form validation, API errors, loading/empty/success states, keyboard and focus, mobile 375px/tablet/desktop, console/network errors and reduced-motion. Prefer stable role/label selectors and isolated test data. Run regression tests and attach evidence. If preview is blocked by authentication, report that rather than claiming visual QA passed. Never submit destructive production actions in tests.
