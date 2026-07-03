# 配置说明

## 必改项

| 文件 | 要改什么 |
| --- | --- |
| `state/company-version.md` | 公司名称、版本号、当前阶段 |
| `state/current-context.md` | 当前业务目标、活跃项目、硬边界 |
| `company-runtime/operating-snapshot.md` | 当前运行方式、项目快照、部门状态 |
| `tasks/next-task.md` | 当前最重要下一步 |
| `state/task-board-current.md` | 活跃任务板 |
| `skills/COMPANION-SKILLS.md` | 目标电脑需要安装或启用的 Skill / 插件能力 |
| `companies/MKT-marketing-consulting/projects/_template/README.md` | 项目模板字段 |

## 公司名替换

默认模板使用“示例公司”。你可以替换成自己的公司名，例如：

```text
示例公司 -> 你的公司名
```

## 项目复制方式

```bash
cp -R companies/MKT-marketing-consulting/projects/_template companies/MKT-marketing-consulting/projects/PROJECT-0001-your-project
```

然后修改项目里的：

- `README.md`
- `STATUS.md`
- `PROJECT-MANAGER.md`
- `task-breakdown.md`

## Codex 使用建议

每次新开对话先说：

```text
启动总管
```

进入某个项目时说：

```text
进入项目 项目名
```

要做图片时说：

```text
启动生图部门 项目名
```

要装 PPT 时说：

```text
启动 PPT Factory 项目名
```

## 技能配置

模板内置的是“规则和触发说明”，不是另一台电脑的全局 Skill 安装包。

目标电脑需要额外检查：

```bash
python3 scripts/check_skills.py
```

如有缺失，按 `docs/SKILL-SETUP.md` 补装或启用对应能力。缺失技能时，总管必须明说缺失并降级执行，不能假装已经调用。
