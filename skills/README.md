# Skills 说明

本目录记录两层能力：

1. 模板内置能力：写在本仓库里，Codex 读文件即可执行。
2. Companion Skills：需要目标电脑实际安装或启用，清单见 `skills/COMPANION-SKILLS.md`。

如果目标电脑没有安装对应全局 Skill，模板只能按规则降级执行，不能真正调用那个 Skill。

## 内置能力

- 入口任务定型
- 自动线程标题命名
- 执行前置声明
- 能力触发完成审计
- 项目经理恢复
- 整页 AI 图片 PPT 路线
- 客户首诊增长路线图
- 图片最终交付生图模型硬 Gate

## 迁移检查

```bash
python3 scripts/check_skills.py
```
