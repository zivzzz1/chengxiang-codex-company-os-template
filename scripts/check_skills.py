#!/usr/bin/env python3
from pathlib import Path

REQUIRED_SKILLS = [
    "ai-company-recording-system",
    "state-drift-governance",
    "html-visual-reporting",
    "one-image-understanding",
    "image-ppt",
    "structured-ppt",
    "chengxiang-html-craft",
    "chengxiang-mobile-h5",
    "content-research-writer",
    "meeting-notes-and-actions",
    "transcript-learning-summary",
    "file-organizer",
    "spreadsheet-formula-helper",
    "feishu-link-learning-intake",
    "xiaohongshu-app-topic-research",
]

OPTIONAL_SKILLS = [
    "ppt-aesthetic-workflow",
    "studioos-workflow",
]


def skill_installed(home: Path, name: str) -> bool:
    return (home / ".codex" / "skills" / name / "SKILL.md").is_file()


def main() -> int:
    home = Path.home()
    missing_required = []
    missing_optional = []

    print("Companion Skills check")
    print(f"Skill root: {home / '.codex' / 'skills'}")
    print()

    print("Required:")
    for name in REQUIRED_SKILLS:
        ok = skill_installed(home, name)
        print(f"- {name}: {'installed' if ok else 'missing'}")
        if not ok:
            missing_required.append(name)

    print()
    print("Optional:")
    for name in OPTIONAL_SKILLS:
        ok = skill_installed(home, name)
        print(f"- {name}: {'installed' if ok else 'missing'}")
        if not ok:
            missing_optional.append(name)

    print()
    if missing_required:
        print("Missing required skills:")
        for name in missing_required:
            print(f"- {name}")
        print()
        print("Install them on this computer, or run with degraded template-only behavior.")
        return 1

    if missing_optional:
        print("Optional skills missing:")
        for name in missing_optional:
            print(f"- {name}")
        print()

    print("All required Companion Skills are installed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
