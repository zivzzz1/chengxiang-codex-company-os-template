#!/usr/bin/env bash
set -euo pipefail

REPO_URL="${REPO_URL:-https://github.com/zivzzz1/chengxiang-codex-company-os-template.git}"
TARGET_DIR="${TARGET_DIR:-$HOME/chengxiang-codex-company-os-template}"
SKILL_ROOT="${SKILL_ROOT:-$HOME/.codex/skills}"
export SKILL_ROOT

echo "Chengxiang Codex Company OS installer"
echo "Repo: $REPO_URL"
echo "Target: $TARGET_DIR"
echo "Skill root: $SKILL_ROOT"
echo

if ! command -v git >/dev/null 2>&1; then
  echo "Missing git. Install git first."
  exit 1
fi

if [ -d "$TARGET_DIR/.git" ]; then
  echo "Updating existing workspace..."
  git -C "$TARGET_DIR" pull --ff-only
elif [ -e "$TARGET_DIR" ]; then
  echo "Target exists but is not a git repository: $TARGET_DIR"
  echo "Move it aside or set TARGET_DIR to another path."
  exit 1
else
  echo "Cloning workspace..."
  git clone "$REPO_URL" "$TARGET_DIR"
fi

mkdir -p "$SKILL_ROOT"

echo
echo "Installing Companion Skills..."
for skill_dir in "$TARGET_DIR"/codex-skills/*; do
  [ -d "$skill_dir" ] || continue
  skill_name="$(basename "$skill_dir")"
  dest="$SKILL_ROOT/$skill_name"
  if [ -e "$dest" ]; then
    backup="$dest.backup.$(date +%Y%m%d-%H%M%S)"
    echo "- $skill_name: existing skill found, backup -> $backup"
    mv "$dest" "$backup"
  else
    echo "- $skill_name: install"
  fi
  cp -R "$skill_dir" "$dest"
done

echo
echo "Running checks..."
python3 "$TARGET_DIR/scripts/check_template.py"
python3 "$TARGET_DIR/scripts/check_skills.py"

echo
echo "Done."
echo "Open this folder in Codex:"
echo "$TARGET_DIR"
echo
echo "Start prompt:"
echo "启动总管"
