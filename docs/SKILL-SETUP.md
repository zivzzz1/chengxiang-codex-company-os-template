# Skill 配置说明

这个模板已经写好了公司规则，但另一台电脑仍然需要安装或启用对应的 Codex Skill / 插件能力。

## 一键安装

```bash
curl -fsSL https://raw.githubusercontent.com/zivzzz1/chengxiang-codex-company-os-template/main/install.sh | bash
```

它会把 `codex-skills/` 下的公开安全版 Companion Skills 安装到 `~/.codex/skills/`。

## 再跑检查

```bash
python3 scripts/check_skills.py
```

输出分两类：

- `installed`：目标电脑已经有这个 Skill。
- `missing`：目标电脑缺少这个 Skill，需要安装或先降级使用。

## 必装 Companion Skills

这些是从当前系统迁移出来的高频能力。一键安装脚本会安装这些 Skill 的公开安全版：

- `ai-company-recording-system`
- `state-drift-governance`
- `html-visual-reporting`
- `one-image-understanding`
- `image-ppt`
- `structured-ppt`
- `chengxiang-html-craft`
- `chengxiang-mobile-h5`
- `content-research-writer`
- `meeting-notes-and-actions`
- `transcript-learning-summary`
- `file-organizer`
- `spreadsheet-formula-helper`
- `feishu-link-learning-intake`
- `xiaohongshu-app-topic-research`

## 可选 Companion Skills

这些适合保留，但不是公司总管启动的硬依赖：

- `ppt-aesthetic-workflow`
- `studioos-workflow`

## 插件 / 连接器能力

这些不是仓库文件能直接安装的 Skill，需要在 Codex 或对应环境里启用：

- GitHub：仓库、PR、Issue、发布和权限管理。
- Google Drive / Docs / Sheets / Slides：云文档协作。
- Notion：知识库、任务和镜像同步。
- Canva：品牌演示和社交媒体设计。
- Browser / Chrome / Computer Use：网页登录态读取、浏览器操作、本机 UI 操作。
- OpenAI Developers：OpenAI API、Agents SDK、ChatGPT Apps SDK。
- Documents / Presentations / Spreadsheets / PDF：本地 Office / PDF 制作与验证。
- Image generation：图片生成或编辑。

## 缺失时的规则

缺少 Skill 时，总管必须说清楚：

```text
技能未安装：<skill-name>。本轮按模板内置规则降级执行。
```

不能把规则说明当成真实 Skill 调用成功。

## 迁移顺序

1. Clone 仓库。
2. 打开 Codex 工作区。
3. 跑 `bash install.sh`。
4. 跑 `python3 scripts/check_template.py`。
5. 跑 `python3 scripts/check_skills.py`。
6. 补齐缺失插件 / 连接器或确认降级使用。
7. 再说 `启动总管`。
