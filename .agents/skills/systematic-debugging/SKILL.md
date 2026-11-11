---
name: systematic-debugging
description: Diagnose reproducible root causes before fixing bugs.
---
# Systematic Debugging
Upstream: https://github.com/obra/superpowers/tree/main/skills/systematic-debugging
This is a PuteraMY adaptation, not the complete upstream skill.

1. Reproduce and collect evidence (logs, stack traces, inputs, environment, expected/actual).
2. Trace data flow and compare known-good patterns.
3. Form a testable root-cause hypothesis and test it with the smallest experiment.
4. Implement the minimal fix with a regression test; rerun checks.
If three attempted fixes fail, reconsider the diagnosis/architecture. Never claim a bug fixed solely because a build succeeds.
