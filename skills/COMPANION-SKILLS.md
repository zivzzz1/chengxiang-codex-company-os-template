# Companion Skills

本文件是目标电脑需要安装或启用的能力清单。它不是 Skill 源码包；它负责告诉 Codex：什么场景应该调用什么 Skill，缺失时如何降级。

## 必装 Skill

| Skill | 触发场景 | 缺失时降级 |
| --- | --- | --- |
| `ai-company-recording-system` | 记录、存档、项目状态、公司运行记录 | 写本地 Markdown 记录，不同步外部系统 |
| `state-drift-governance` | 状态漂移、同步首页、项目状态不一致 | 只做本地文件对照，不做外部修复 |
| `html-visual-reporting` | HTML 汇报、项目简报、学习总结网页 | 用 Markdown 结构稿替代 |
| `one-image-understanding` | 一张图看懂、信息图、结构图、能力地图 | 先输出图文结构和提示词 |
| `image-ppt` | 图片 PPT、整页生图 PPT、视觉提案页 | 先输出页纲、图内文字和生图派单包 |
| `structured-ppt` | 客户向结构化 PPT、服务介绍、提案 deck | 先输出可读页纲和逐页文案 |
| `chengxiang-html-craft` | 中文 HTML 汇报、客户方案、一页看懂 | 用基础 HTML / Markdown 降级 |
| `chengxiang-mobile-h5` | 手机 H5、朋友可看的 H5、服务介绍 H5 | 先输出 H5 内容结构和页面脚本 |
| `content-research-writer` | 内容研究、文章、选题、引用写作 | 先输出无联网版大纲和待核验点 |
| `meeting-notes-and-actions` | 会议纪要、行动项、决策整理 | 用本地纪要模板整理 |
| `transcript-learning-summary` | 录音转文字后的学习总结、长转写拆解 | 用章节摘要模板整理 |
| `file-organizer` | 文件整理、重复文件、目录清理建议 | 只列建议，不移动文件 |
| `spreadsheet-formula-helper` | 表格公式、透视表、Excel / Sheets 公式 | 输出公式草案和验证说明 |
| `feishu-link-learning-intake` | 飞书、WaytoAGI、外部学习链接吸收 | 只记录链接和待读取问题 |
| `xiaohongshu-app-topic-research` | 小红书选题、爆款内容、用户痛点研究 | 只输出假设，不当作平台证据 |

## 可选 Skill

| Skill | 触发场景 | 备注 |
| --- | --- | --- |
| `ppt-aesthetic-workflow` | 明确要求可编辑 PPT 且强调审美路线 | 不作为默认 PPT 路线 |
| `studioos-workflow` | 明确进入 StudioOS / 文琳 | 不进入公司总管默认边界 |

## 插件 / 连接器

| 能力 | 用途 | 配置方式 |
| --- | --- | --- |
| GitHub | 仓库、PR、Issue、发布、权限 | 在 Codex 启用 GitHub 连接 |
| Google Drive / Docs / Sheets / Slides | 云文档、表格、演示 | 在 Codex 启用 Google Drive |
| Notion | 知识库、任务、镜像同步 | 在 Codex 启用 Notion |
| Canva | 品牌演示、社媒尺寸、设计本地化 | 在 Codex 启用 Canva |
| Browser / Chrome / Computer Use | 浏览器读取、网页登录态、本机 UI 操作 | 在 Codex 启用对应工具 |
| OpenAI Developers | API、Agents SDK、ChatGPT Apps SDK | 在 Codex 启用 OpenAI Developers |
| Documents / Presentations / Spreadsheets / PDF | Office / PDF 生成与验证 | 使用 Codex 内置文档能力 |
| Image generation | 图片生成和编辑 | 使用 Codex 内置生图能力 |

## 调用纪律

1. 先读本地真源，再调用 Skill。
2. Skill 只在触发场景出现时使用，不每轮全量调用。
3. 缺失 Skill 必须明说，不能假装调用。
4. 客户可见、发布、同步、公开仓库前必须做完成审计。
