# 跨电脑迁移检查表

## 源电脑

- [ ] 模板检查通过：`python3 scripts/check_template.py`
- [ ] 没有 `.env`、密钥、客户资料、二进制交付物
- [ ] 已提交到 GitHub
- [ ] 已确认仓库权限：公开模板或私有模板

## 目标电脑

- [ ] 安装 Codex
- [ ] 登录正确账号
- [ ] clone 模板仓库
- [ ] 用 Codex 打开模板目录
- [ ] 读取 `AGENTS.md`
- [ ] 发送 `启动总管`
- [ ] 修改公司名、项目名、状态文件
- [ ] 运行 `python3 scripts/check_template.py`

## 目标电脑第一次启动口令

```text
启动总管
```

## 如果恢复失败

先检查：

1. 当前工作区是不是模板根目录。
2. `AGENTS.md` 是否存在。
3. `state/company-version.md` 是否存在。
4. `company-runtime/operating-snapshot.md` 是否存在。
5. 是否把私有文件误删或误提交。
