# 开源发布检查清单

> 合并来源：GitHub Blog 协作清单 + G先生自检项 + 开源指南补充
> 适用项目：文档/知识库、代码/技能、插件/市场上架
> 作者：[蹦哒滴路过你身边](https://github.com/garoter-a11y)

---

## 🚀 快速发布（所有项目必查）

### 仓库设置

- [ ] **Visibility**：Public（开源项目标准）
- [ ] **About 描述**：中英双语，一句话说清项目干什么
- [ ] **Topics 标签**：5–7 个英文标签，提升搜索命中
- [ ] **Social Preview**：1200×630 图片（可选但推荐）
- [ ] **Default branch**：`main`（非 `master`）

### 四份标配文件

- [ ] **LICENSE**：OSI 批准的许可证（MIT / Apache 2.0 / CC BY-SA 4.0），文件不为空模板
- [ ] **README.md**：回答四个问题 —— 干什么 / 为什么有用 / 怎么上手 / 去哪求助
- [ ] **CONTRIBUTING.md**：如何提 bug、如何提 PR、代码规范
- [ ] **Code of Conduct**：`CODE_OF_CONDUCT.md` 或 README 中的行为准则声明

### 版本与发布

- [ ] **git tag 格式规范**：`v1.0.0`（非 `1.0`，非 `V1.0`）
- [ ] **Release Notes**：含 What's New / Breaking Changes / Known Issues
- [ ] **唯一版本号**：每次发布打 tag，语义化版本（SemVer）
- [ ] **Changelog**：`CHANGELOG.md` 或 Release Notes 中记录变更

### 网络与推送

- [ ] **推送走代理**：`git config http.proxy http://127.0.0.1:7897`
- [ ] **推送用 HTTPS**：SSH 可能超时，HTTPS + 代理更稳
- [ ] **SSH 指纹弹窗**：点 OK 确认

### 赞助（可选但推荐）

- [ ] **Sponsor 链接**：README 末尾 `## 赞助` + GitHub Sponsors 链接

---

## 🔒 溯源与安全（所有项目必查）

### API Key 扫描
- [ ] `grep -rn "sk-\|tp-\|api_key\|token" .` 全量扫，确认无真实 Key 泄露
- [ ] 无硬编码 API Key / Token / Secret

### .gitignore
- [ ] 必须含：`.env` `*.bak` `Desktop/` `Temp/` `*.local` `credentials.*`
- [ ] 确认敏感文件未被追踪：`git ls-files | grep -E "\.env|\.bak|credentials"` 返回空

### 溯源签名
- [ ] `[^_^]: #` 隐藏注释完整性 —— 不删、不改、不覆盖
- [ ] 作者署名一致性：`蹦哒滴路过你身边` / `garoter-a11y` 统一（README、LICENSE、SKILL.md）

### 依赖审计
- [ ] 依赖声明文件完整（`requirements.txt` / `package.json` / `pyproject.toml`）
- [ ] 无冗余依赖（未 import 的包不列入）
- [ ] 若有可执行脚本：审计无外连/后门/数据外传

### 跨 Agent 文件审计
- [ ] 其它 Agent 自动生成的文件（如 `maintenance-workflow.md`）发布前确认是你写的
- [ ] 非本人创建的文件标记来源

---

## 📚 文档/知识库项目附加

> 适用：model-provider-config-ops-kit 等纯文档/知识库项目

- [ ] **数量自洽**：SKILL.md / index.md / 实际文件 —— 三处数字一致，目录树一对一
- [ ] **URL 全通**：所有 `官方技术文档:` 后的 URL 逐个 `curl -sI` 验证返回 200
- [ ] **模板规范**：所有文件遵循 `_template.md` 统一格式
- [ ] **交叉引用**：index.md → 各 provider 文件 → 工作流文件，链接不 404
- [ ] **中英双语**：关键字段（端点、模型名、能力）双语标注，Agent 检索友好
- [ ] **关键词标注**：Obsidian 索引用关键词（tags / frontmatter）

---

## 🛠️ 代码/技能项目附加

> 适用：cross-window-agent-orchestrator 等含代码的技能项目

- [ ] **安全审计**：`SKILL.md` 中无命令注入风险，`terminal()` 参数不拼接用户输入
- [ ] **路径泛化**：无硬编码绝对路径（`C:\Users\xxx`），用 `%USERPROFILE%` / `$HOME` / `~`
- [ ] **多平台兼容**：Windows / Linux / macOS 路径写法分离或统一 POSIX
- [ ] **防注入**：timestamp 指纹验证、外部输入消毒
- [ ] **红线文档**：安全约束、操作边界、禁止操作明确写在 SKILL.md 或 references/
- [ ] **README 含 5 分钟跑通**：`clone → install → 一条命令验证 → 看到效果`
- [ ] **per-agent/ 目录**：多 Agent 适配文件齐全，文件命名含 Agent 名

---

## 📦 插件/市场上架附加

> 适用：TokenPulse 等需上架 Space 市场 / VS Code Marketplace 的插件

- [ ] **manifest 完整性**：name / version / description / author / license 齐全
- [ ] **打包规范**：`zip` 包含所有必需文件，无多余临时文件
- [ ] **图标资源**：icon.png (≥256×256)、screenshot 预览图
- [ ] **PropertyInspector**：可调参数（透明度等）在 PI 中暴露
- [ ] **版本号一致性**：manifest.json / package.json / CHANGELOG.md 三处一致
- [ ] **上架前自测**：本地安装 → 全功能走通 → 截图保存

---

## 🏅 进阶（CII Badge 预留）

> 项目有代码、测试、CI 后再跑

- [ ] 自动化测试覆盖（Passing 级要求至少一套测试）
- [ ] CI/CD 流水线（GitHub Actions 或等效）
- [ ] 静态分析 / Linter 集成
- [ ] 安全策略 `SECURITY.md`
- [ ] Issue / PR 模板（`.github/ISSUE_TEMPLATE/`）
- [ ] CODEOWNERS 文件（`.github/CODEOWNERS`）
- [ ] 依赖自动更新（Dependabot / Renovate）

---

## 📎 参考来源

| 来源 | 链接 |
|------|------|
| GitHub Blog 协作清单 | https://github.blog/enterprise-software/collaboration/a-checklist-and-guide-to-get-your-repository-collaboration-ready/ |
| OpenSSF Best Practices | https://www.bestpractices.dev |
| opensource.guide | https://opensource.guide/starting-a-project/ |
| Eko Open-Source Guidelines | https://ekoindia.github.io/open-source-guidelines |

---

> 最后更新：2026-06-17

[^_^]: # 蹦哒滴路过你身边 / garoter-a11y — 溯源签名，请勿删除
