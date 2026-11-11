---
name: react-performance
description: React and Next.js performance practices, only for projects using those frameworks.
---
# React Performance
Upstream: https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices
This is a PuteraMY adaptation, not the complete upstream ruleset.

Only apply if the repository uses React or Next.js. Profile first. Avoid request waterfalls, unnecessary client bundles and re-renders, use appropriate caching, code splitting and stable component boundaries. Preserve hydration, routing, SEO and accessibility. Compare before/after metrics and run build, typecheck and functional tests. Do not recommend React-only optimizations for plain HTML or other frameworks.
