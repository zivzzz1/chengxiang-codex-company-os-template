# 安装说明

## 1. 下载模板

```bash
git clone <your-template-repo-url>
cd chengxiang-codex-company-os-template
```

如果你下载的是 zip，解压后进入目录即可。

## 2. 用 Codex 打开目录

在 Codex 中选择这个工作区目录，或在终端进入目录后启动 Codex。

## 3. 第一次启动

把下面这句话发给 Codex：

```text
启动总管
```

或把 `prompts/start-general-manager.md` 的内容发给 Codex。

## 4. 做本地检查

```bash
python3 scripts/check_template.py
python3 scripts/check_skills.py
```

`check_template.py` 检查模板文件完整性；`check_skills.py` 检查当前电脑是否已经安装推荐的全局 Skill。

如果 `check_skills.py` 报缺失，先按 `docs/SKILL-SETUP.md` 配置技能，再开始正式使用。

## 5. 推荐配置顺序

1. 改 `state/company-version.md`。
2. 改 `state/current-context.md`。
3. 改 `company-runtime/operating-snapshot.md`。
4. 按 `docs/SKILL-SETUP.md` 检查全局 Skill。
5. 根据你的业务复制 `companies/MKT-marketing-consulting/projects/_template/`。
6. 用 `tasks/next-task.md` 写当前最重要任务。
