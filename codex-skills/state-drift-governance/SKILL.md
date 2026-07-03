---
name: state-drift-governance
description: Use when local state, dashboard state, project status, or external mirrors may disagree, especially after project state changes, archive, pause, sync, or resume.
---

# State Drift Governance

Use this skill to compare local truth against mirrored summaries.

Rules:

1. Read local source files first.
2. Treat mirrors as secondary.
3. Report drift explicitly instead of silently repairing it.
4. If repair is requested, update local truth first, then external mirrors.
5. Verify after any write or sync.
