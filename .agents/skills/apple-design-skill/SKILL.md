# Apple HIG-informed cross-platform UI review

Source to review: https://github.com/dickwu/apple-design-skill

## Status
This file is a PuteraMY-authored integration guide referencing an external repository. It is **not** a copy of the upstream skill and does **not** install its CLI, scripts, datasets, or tools. Verify the upstream README, license, dependencies and actual skill files before using upstream commands. GitHub star counts shown on social media are not verified here.

## When to use
Use to review native or native-like UI across mobile and desktop. Check platform conventions, navigation, touch targets, hierarchy, input behaviors, accessibility, dynamic text and interaction feedback. Treat as a reviewer, not an automatic UI generator. Respect Android, web and platform-specific norms rather than blindly applying iOS patterns.

## Workflow
1. Read the project's AGENTS.md, product brief and existing code before changing anything.
2. Choose one measurable design goal and the smallest suitable set of tools.
3. Inspect actual UI, interactions and implementation constraints.
4. Produce a distinct, context-appropriate design direction; keep functionality intact.
5. Implement in small reversible steps, with accessibility and reduced-motion safeguards.
6. Run applicable typecheck, lint, unit/integration tests and build; inspect browser screenshots and motion playback where possible.
7. Report what was verified, what was not, and any remaining limitations. Never claim a tool or skill is installed without checking.

## Safety
Do not deploy production, delete data, change credentials, or perform destructive operations without explicit approval.
