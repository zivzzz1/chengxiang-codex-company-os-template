# Chengxiang Codex Company OS Template

这是一个可下载、可复制、可二次配置的 Codex 公司操作系统模板。

它适合把 Codex 当成一个长期协作系统来使用：先有总管入口，再有公司规则、部门边界、项目经理、工作流、任务板和本地状态。

本模板只包含架构、规则、路线和空项目模板，不包含真实客户资料、Notion 镜像、运行日志、图片/PPT/PDF 交付物或任何个人本机路径。

## 你拿到后先做什么

1. 下载或 clone 本仓库。
2. 在 Codex 中打开本目录。
3. 先读 `AGENTS.md`。
4. 再把 `prompts/start-general-manager.md` 的内容发给 Codex。
5. 按 `docs/CONFIGURATION.md` 把公司名、项目名、部门名和状态文件改成你自己的。
6. 按 `docs/SKILL-SETUP.md` 配置目标电脑上的全局 Skill。
7. 按 `docs/LOCKED-CONFIG.md` 检查回复格式、自动标题和功能调用边界。
8. 用 `python3 scripts/check_template.py` 和 `python3 scripts/check_skills.py` 做最小检查。

## 目录结构

```text
.
├── AGENTS.md                         # Codex 入口规则
├── prompts/                          # 启动提示词
├── docs/                             # 使用说明、配置、迁移和安全说明
├── state/                            # 当前状态、版本号、任务板
├── tasks/                            # 下一步任务
├── company-runtime/                  # 运行快照和活跃会话
├── companies/                        # 公司、部门、项目和工作流
├── modules/                          # 生图、PPT、视频等执行部门规则
├── skills/                           # 可复用能力说明
├── scripts/                          # 本地检查脚本
└── tests/                            # 测试说明
```

## 默认入口

在 Codex 里说：

```text
启动总管
```

或：

```text
进入项目 示例项目
```

## 核心原则

- 本地文件是真源，外部工具只是镜像或发布通道。
- 项目经理只做文字、页纲、图内文字、提示词、派单包和验收点。
- 最终是图片或图片化页面时，必须由生图模型直接生成完整画面和图内文字。
- PPT Factory 只装配用户确认过的整页图，不改策略、不补文案、不在图片上叠字。
- 新项目先做任务定型，再推进生产。
- 客户可见、报价、合同、金融收益承诺等高风险任务必须先过边界检查。

## 最小测试

```bash
python3 scripts/check_template.py
python3 scripts/check_skills.py
```

测试会检查：

- 必需文件是否存在。
- 是否残留本机绝对路径。
- 是否残留 Notion / 客户项目 / 敏感输出目录。
- 图片生产硬规则是否存在。

## 许可证

见 `LICENSE`。
