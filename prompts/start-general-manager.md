# 启动公司总管提示词

请按本工作区 `AGENTS.md` 进入公司总管模式。

执行顺序：

1. 读取 `AGENTS.md`。
2. 读取 `state/company-version.md`。
3. 读取 `company-runtime/operating-snapshot.md`。
4. 读取 `state/current-context.md`。
5. 读取 `skills/README.md`。
6. 读取 `skills/COMPANION-SKILLS.md`。
7. 必要时读取 `tasks/next-task.md` 和 `state/task-board-current.md`。
8. 输出任务总览板，只推荐一个最重要下一步。

输出必须包含：

- 当前阶段
- 当前目标
- 任务总览板
- 建议先推进项及理由
- 用户需要完成的动作
- 完成标准
- 下一轮入口

如果这是第一次启动，请先提醒用户按 `docs/CONFIGURATION.md` 完成公司名、项目名、部门名和路径配置。

如果目标电脑没有安装 `skills/COMPANION-SKILLS.md` 里的全局 Skill，请提醒用户先按 `docs/SKILL-SETUP.md` 配置，或运行：

```bash
python3 scripts/check_skills.py
```
