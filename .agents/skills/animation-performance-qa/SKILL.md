---
name: animation-performance-qa
description: Audit and verify animation smoothness, responsiveness and accessibility with measured evidence.
---
# Animation Performance QA — PuteraMY guide

Build a representative interaction matrix: entry, hover, click, menu, modal, scroll, drag, loading, error and exit. Profile main-thread long tasks, frame drops, forced reflow, CLS and memory leaks using browser tooling where available. Prefer composited transform/opacity and minimize expensive blur/shadow/filter animations. Test reduced-motion, mobile touch, keyboard and low-powered devices. Compare before and after; record actual test results and screenshots or traces. A Vercel READY build is not proof that animation is smooth.
