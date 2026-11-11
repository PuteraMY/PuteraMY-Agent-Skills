---
name: gsap-scroll-storytelling
description: High-quality scroll-linked storytelling, section transitions and timeline choreography with GSAP.
---
# GSAP Scroll Storytelling — PuteraMY guide
Official docs: https://gsap.com/docs/v3/ and https://gsap.com/docs/v3/Plugins/ScrollTrigger/
This is a workflow guide; GSAP is not installed by adding this file.

Use GSAP/ScrollTrigger only when a deliberate editorial or cinematic narrative benefits from scrub, pin or coordinated timelines. Define a storyboard first; keep interactions usable without animation. Scope selectors, revert/kill timelines and triggers on teardown, recalculate on resize, avoid unnecessary scroll pinning and expensive layout reads. Respect prefers-reduced-motion, keyboard navigation and small screens. Measure real browser performance and verify no scroll trapping or overlapping content. Do not layer GSAP and Motion over the same property without an explicit ownership plan.
