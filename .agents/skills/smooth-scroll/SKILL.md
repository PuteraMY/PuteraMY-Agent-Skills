---
name: smooth-scroll
description: Evaluate accessible smooth scrolling with native scrolling first and Lenis only when justified.
---
# Smooth Scroll — PuteraMY guide
Official docs: https://lenis.dev/
This file is not a Lenis installation.

Default to native browser scrolling and CSS scroll-behavior where suitable. Consider Lenis only when scroll-linked immersive scenes need synchronization and user testing supports it. Preserve anchors, back/forward, keyboard navigation, focus, touch and reduced-motion behavior. Avoid scroll hijacking, duplicate RAF loops, nested scroll conflicts and excess CPU usage. Test low-end phones and browsers before shipping.
