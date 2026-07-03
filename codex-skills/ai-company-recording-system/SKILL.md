---
name: ai-company-recording-system
description: Use when the user asks to record, archive, preserve decisions, update project status, resume a project, or keep company operating context. Local files are source of truth; external mirrors are optional.
---

# AI Company Recording System

Use this skill for `记录`, `存档`, `记录为项目状态`, `进入项目`, `恢复项目`, and company state preservation.

Rules:

1. Local files are source of truth.
2. Include a clear time label when writing records.
3. Choose the smallest sufficient target: project log, state file, task file, or capability candidate.
4. Do not sync Notion, GitHub, Drive, or other external systems unless the user asks.
5. For project resume, report: current status, completed, blocked, next entry, do not do, drift status.
