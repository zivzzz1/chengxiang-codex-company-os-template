#!/usr/bin/env python3
from pathlib import Path
import sys
import re

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "AGENTS.md",
    "README.md",
    "prompts/start-general-manager.md",
    "docs/INSTALL.md",
    "docs/CONFIGURATION.md",
    "docs/USAGE.md",
    "docs/LOCKED-CONFIG.md",
    "docs/SKILL-SETUP.md",
    "docs/PRIVACY-AND-SAFETY.md",
    "state/company-version.md",
    "state/current-context.md",
    "state/current-state.md",
    "state/task-board-current.md",
    "tasks/next-task.md",
    "company-runtime/operating-snapshot.md",
    "company-runtime/active-sessions.yml",
    "modules/image-factory/AGENTS.md",
    "modules/ppt-factory/AGENTS.md",
    "companies/MKT-marketing-consulting/projects/_template/README.md",
    "scripts/check_skills.py",
    "skills/COMPANION-SKILLS.md",
]

FORBIDDEN_SNIPPETS = [
    "/Users/ai-company-os-starter/ai-company-os-starter",
    "/Users/liuhongtao",
    "app.notion.com",
    "OPENAI_API_KEY",
    "宜丰红商城",
    "ETS Trader",
    "潮宗街",
    "添锐",
    "凯特利",
]

FORBIDDEN_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9_-]{16,}"),
]

REQUIRED_SNIPPETS = [
    "最终交付为图片",
    "生图模型直接生成完整画面",
    "PPT Factory",
    "项目经理",
    "任务总览板",
    "自动线程标题",
    "CODEX_THREAD_ID",
    "执行前置声明",
    "完成审计",
    "Companion Skills",
    "check_skills.py",
    "one-image-understanding",
    "image-ppt",
    "structured-ppt",
]


def iter_text_files():
    for path in ROOT.rglob("*"):
        if path.is_file() and ".git" not in path.parts:
            if path.suffix.lower() in {".md", ".txt", ".yml", ".yaml", ".py"} or path.name in {"AGENTS.md", "README.md"}:
                yield path


def main():
    errors = []

    for rel in REQUIRED_FILES:
        if not (ROOT / rel).is_file():
            errors.append(f"missing required file: {rel}")

    all_text = []
    for path in iter_text_files():
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append(f"non utf-8 text file: {path.relative_to(ROOT)}")
            continue
        all_text.append((path, text))

    combined = "\n".join(text for _, text in all_text)

    for snippet in REQUIRED_SNIPPETS:
        if snippet not in combined:
            errors.append(f"missing required rule snippet: {snippet}")

    for path, text in all_text:
        if path.relative_to(ROOT).as_posix() == "scripts/check_template.py":
            continue
        for snippet in FORBIDDEN_SNIPPETS:
            if snippet in text:
                errors.append(f"forbidden snippet {snippet!r} in {path.relative_to(ROOT)}")
        for pattern in FORBIDDEN_PATTERNS:
            if pattern.search(text):
                errors.append(f"forbidden secret-like pattern {pattern.pattern!r} in {path.relative_to(ROOT)}")

    if errors:
        print("Template check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Template check passed.")
    print(f"Root: {ROOT}")
    print(f"Checked files: {len(all_text)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
