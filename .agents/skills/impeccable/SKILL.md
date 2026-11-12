# Systematic interface polish and design-language audits

Source to review: https://github.com/pbakaus/impeccable

## Status
This file is a PuteraMY-authored integration guide referencing an external repository. It is **not** a copy of the upstream skill and does **not** install its CLI, scripts, datasets, or tools. Verify the upstream README, license, dependencies and actual skill files before using upstream commands. GitHub star counts shown on social media are not verified here.

## When to use
Use for a structured UI polish pass: inspect current UI, define product design principles and a PRODUCT.md-style brief, audit spacing, typography, contrast, responsive layouts, states and interactions. Make targeted improvements without replacing working features. Verify before/after screenshots, accessibility and browser tests. Do not invoke commands named polish/typeset/colorize unless the upstream package and commands are actually installed.

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
