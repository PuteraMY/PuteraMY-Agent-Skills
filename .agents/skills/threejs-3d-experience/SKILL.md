---
name: threejs-3d-experience
description: Accessible, performant interactive 3D scenes for portfolio and product interfaces.
---
# 3D Experience — PuteraMY guide
Official reference: https://threejs.org/docs/
This guide does not install Three.js, models or assets.

Use 3D only when it adds meaningful interaction (product configurator, architecture visualizer, hero illustration). Plan camera, lighting, materials, controls, loading and graceful 2D fallback. Budget geometry, texture resolution, draw calls and memory; lazy-load WebGL and pause when offscreen. Dispose resources on teardown, handle context loss, avoid motion sickness, provide non-WebGL and reduced-motion paths, and verify on mobile devices. Never promise photorealism without suitable assets and testing.
