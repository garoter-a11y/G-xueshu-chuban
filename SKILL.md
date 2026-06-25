---
name: G-xueshu-chuban
description: "学术出版全流程——论文起草→LaTeX排版→印刷级PDF→arXiv/Zenodo投稿。覆盖HCI论文写作（叙事策略+18条陷阱）、中文CJK编译兼容、HTML→印刷级PDF纸质书排版、arXiv endorsement背书流程。"
version: 1.0.0
author: 蹦哒滴路过你身边
license: CC BY-SA 4.0
platforms: [windows]
metadata:
  hermes:
    tags: [论文, LaTeX, arXiv, 排版, 出版, CJK]
    category: research
---

# G-xueshu-chuban — 学术出版全流程

> 写完→排好→投出去。三个阶段递进。

```
阶段1: 论文起草          阶段2: 排版生成            阶段3: 投稿发布
academic-paper-drafting   book-typesetting           latex-arxiv-submission
(写作模板+叙事策略)       (HTML→印刷PDF/CSS)         (arXiv编译+Zenodo)
```

---

# 阶段1：论文起草

## 触发条件

用户要求基于已有文献撰写论文初稿、或从竞品核查转入正文写作时使用。

## 前置检查（动笔前确认）

1. **竞品核查终报** — 完整文献列表、验证状态、研究空白
2. **文献引用总表** — arXiv ID/DOI/作者/年份/核心论点
3. **空白确认** — 至少3项"0 results"三方验证
4. **贡献宣言** — 一句话说清独特贡献

不齐则先走文献核查补全，不要裸写。

## 论文结构模板

```
Title → Abstract(200-250词) → Introduction(1.5页以内)
→ Related Work(分组对标,每组2-3篇,含Gap表)
→ 核心贡献(每章=一个空白, Motivation→Formal Definition→Properties→Comparison)
→ Discussion(可行性表+局限+伦理)
→ Conclusion(有力收尾,不要软结尾)
→ References(16篇以上)
```

## 叙事架构策略

核心原则：**完善，而非对抗**

| 维度 | ❌ 对抗叙事 | ✅ 完善叙事 |
|------|-----------|-----------|
| 起点 | "Agent在消耗生命" | "Agent是永久基础设施" |
| 框架定位 | 外在干预(add-on) | 原生嵌入(framework layer) |
| 公式定位 | 独立贡献需验证 | 推导结论(叙事铺垫到位后自然出现) |
| 词汇选择 | 剥削、提取、掠夺 | 完善、闭环、优化、可持续 |

## 写作规则

- **学术英语，不说废话。** 每段首句=论点
- **主动语态**优先："We introduce..."
- **数字说话**：具体数字是论据骨架
- 每Related Work小节以"What they established / What they missed"收尾
- 变量斜体$T_i^{wait}$，向量粗体$\mathbf{s}$

## 论文陷阱（18条，原academic-paper-drafting完整保留）

1. **引言太长。** Introduction 控制在 1.5 页以内（~800 words）。把细节留给正文。
2. **Related Work 只罗列不批判。** 每篇必须说出它缺什么——只总结不批判的 Related Work 对论文无贡献。
3. **公式没有解释。** 每个公式下面必须有至少一句白话解释——审稿人不是数学家。
4. **Discussion 逃避。** 必须有一节叫 "Limitations and Open Questions"，诚实列出未验证的假设。
5. **Conclusion 太软。** 不要 "Future work may explore..." 型收尾。最后一句话要有重量。
6. **隐藏注释保护。** G先生的 `[^_^]: # ...` 隐藏注释不可覆盖/删除/修改。编辑含此类注释的文件时，patch 必须精确匹配原文字，不得整段重写。
7. **语力动词过强。** 避免 "We demonstrate"（暗示有自有实验数据）、"We validate"（暗示用户研究验证）、"confirmed research gaps"（暗示系统性综述已穷尽，实际只是搜索0结果）。替代词："We argue"、"We specify"、"We establish"、"identified research gaps"。
8. **审稿报告交叉审计。** 收到多份审稿报告时：(a) 先交叉对比找一致点（高置信度问题），(b) 再找分歧点逐项核实，(c) 优先修复跨报告致命的文献事实错误（会议声称、标题、期刊名），(d) 理论批评类的修改方向先与用户确认再动笔。
9. **叙事定调为"抗议文献"。** 如果引言读起来像某个组织的抗议声明（"Agent 正在消耗我们的生命！"），审稿人会把论文归类为立场声明而非架构方案。正确做法：从基础设施的架构层出发，逐层推导到框架的缺失组件，让解决方案显得**必然**而非**愤怒**。判断标准：读第一节——如果前三段的语气是愤怒/控诉/揭露，重写；如果前三段的语气是分析/建构/完善，正确。
10. **公式被当作"独立贡献"推给审稿人验证。** 如果公式单独占一章、有形式化定义+数学性质+实例计算，审稿人会按核心贡献的标准要求实证数据。如果公式只是前面叙事链走到那一步的**代数收束**，处理方式：(a) 缩为过渡小节（3-4段），(b) 不给性质不给实例不证单调性，(c) 在正文中声明"这不是新公式，只是前面分析的代数表达"。叙事链严密则公式必然——不需要外部验证。
11. **论文多维度打磨未并行化。** 当论文需要同时处理语言审查、图表方案、Discussion扩展、实验设计等独立任务时，不要逐条串行处理——串行总耗时 = Σ(各项耗时)。使用 delegate_task batch 模式并行派给子Agent，主持人只做汇总决策。节省时间 3-4 倍。详见 `references/parallel-agent-editing.md`。
12. **非争议修改列入决策清单。** 数学不可能（如 112% reliability drop）、数字矛盾、格式违规、引用缺失——这类修改不需要等用户拍板，patch 直接落地。用户问"处理了几项"时答案不应是 0。只把涉及论文立论方向、叙事策略、模型设计取舍的项列入决策清单。
13. **用户给绿灯不立即执行。** 用户说"同步进行，完美收官"或"允许执行"就是绿灯——立即开始逐项落地修改，不再等二次确认或追问"现在做吗？"。自问"用户说了开始，为什么还在等"是主持人常犯的方向性跑偏。
14. **子Agent修改执行报告不可信，必须逐项核实。** 子Agent提交的"A-F修订执行报告"声称的每项修改都必须用 search_files 或 read_file 对照实际论文文件逐条核实。本次会话：麦兜报告声称A项改为"unreliability"（实为"error rate"）、D项DOI已补全（实为占位符"xxxxxxx"）——两处声称与实际文件不符。教训：子Agent写报告时的记忆与它实际写入文件的内容可能不同，报告说做了≠文件里做了。
15. **竞品比对报告集成流程。** 收到合并竞品比对终审报告后，P0执行顺序：(a) 术语冲突统一（full-text search→replace→footnote引用先行工作），(b) §2 Related Work按竞品集群分组扩展（每个集群一个新增段落，含What they established/missed），(c) §3 Motivation嵌入实证支撑数据（具体数字+来源），(d) References补全所有新文献（先追加到尾部按字母排列）。详见 `references/competitor-integration-workflow.md`。
16. **多版本文件管理陷阱。** 当论文存在多个版本文件时（如 v1 经典结构文件 vs v2 叙事重构文件），修订操作容易只落在当前打开的文件上，其他版本文件完全未触达。后果：没有任何单一文件同时包含"最新叙事框架 + 全部修订项"。预防：(a) 修订开始前先列出版本矩阵，(b) 每完成一轮修订确认是否需同步，(c) 最终交付明确标注"哪个文件是完整稿，哪个是未同步存档"。跨版本重新打修订时，不要依赖原始修订报告的行号——两个版本行号完全失效。用 search_files 搜索语义模式逐个定位→逐项 patch→再次 search_files 验证零残留。
17. **哲学地基引用（平权器专用）。** 如需引入《实践论》《矛盾论》或王阳明「知行合一」作为架构设计的哲学地基，参考 `references/pingquanqi-philosophy-grounding.md`。关键约束：(a) 西方审稿人可能不熟悉毛选，必须在正文中用英文完整阐述每个核心论点，(b) 参数值（如 α=0.3、τ=0.7）不能写入论文正文作为「已验证阈值」——标注为「illustrative default, requiring empirical calibration」，(c) 哲学引入不增篇幅——每处1-2句作为理论背书，不改变论文主线。
18. **多Agent审阅交叉对标。** 当论文收到3+份Agent审阅意见时，先建四象限矩阵（一致项/分歧项/独有发现/遗漏项）再执行修复：一致项零争议直接落地；评级分歧取更强论证方；独有发现各自贡献不作废；遗漏自评校准审阅质量。执行顺序：P0→P1批量patch，P2提交用户决策。详见 `references/multi-agent-review-synthesis.md`。

## 完成后的交付

1. 统计文件规模（KB / 行 / 词 / 引用数）
2. 给出章节结构总表
3. 明确下一步选项（继续精修 / 送审读 / 发给合作者）

---

# 阶段2：排版生成（HTML→印刷级PDF）

## 适用场景

- 个人出书/赠书
- 技术文档汇编
- 译文文集排版
- 任何HTML→印刷PDF需求

## 排版规格确认（每次必问）

| 项目 | 示例 |
|------|------|
| 纸张尺寸 | 170mm×240mm（小16开） |
| 打印方式 | 单面/双面 |
| 页码规则 | 封面无页码，正文从第1页 |
| 正文字体 | 宋体(SimSun)/黑体(SimHei) |

## 红线

- **绝不替换原始CSS设计！** 只在原有基础上加@page尺寸和边距
- **先试排**给用户看效果，再批量处理
- 听用户说完再行动

## 印刷CSS

```css
@page {
  size: 170mm 240mm;
  margin: 15mm 15mm 18mm 15mm;
  @bottom-center { content: counter(page); }
}
@page :blank { @bottom-center { content: none; } }
@page :first { @bottom-center { content: none; } }
@media print { body { background: white !important; } }
```

### 进阶1：动态页眉（章节名自动注入）

```css
/* HTML中标题内容存到变量 */
h1 { string-set: chapter-title content(text); }
h2 { string-set: section-title content(text); }

/* 奇数页右上角=章名，偶数页左上角=节名 */
@page :right {
  @top-right { content: string(chapter-title); font-size: 9pt; color: #666; }
}
@page :left {
  @top-left { content: string(section-title); font-size: 9pt; color: #666; }
}
```

### 进阶2：双面打印/装订留白

```css
@page :left {   /* 偶数页——装订侧在右边 */
  margin: 22mm 20mm 22mm 30mm;  /* 左边更大=外侧 */
}
@page :right {  /* 奇数页——装订侧在左边 */
  margin: 22mm 30mm 22mm 20mm;  /* 右边更大=外侧 */
}
```

### 进阶3：出血位+裁切标记（送打印店）

```css
@page {
  size: 170mm 240mm;
  bleed: 3mm;         /* 出血3mm */
  marks: crop cross;   /* 裁切标记+十字线 */
}
```

⚠️ Playwright的`page.pdf()`不支持`marks`和`bleed` CSS属性。两个替代方案：
| 方案 | 做法 | 适用 |
|------|------|------|
| 🅰 做图时留出血 | HTML设计图本身四周多3mm内容 | 最简单 |
| 🅱 转PDF工具 | Adobe Acrobat/打印店软件加裁切线 | 专业 |

### 进阶4：自动目录页码

```css
.toc a::after {
  content: leader('.') target-counter(attr(href), page);
}
```

### 进阶5：防溢出（页末孤行控制）

```css
p, li { orphans: 3; widows: 3; }       /* 至少3行在一起 */
h1, h2, h3 { break-after: avoid; }      /* 标题后不换页 */
table, figure, pre { break-inside: avoid; }  /* 表格/代码块不断开 */
section.chapter { break-before: page; }      /* 每章从新页开始 */
```

## Playwright PDF生成

```python
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(f"file:///{html_path}", wait_until="networkidle")
    page.pdf(path=pdf_path, width="170mm", height="240mm",
             margin={"top":"0mm","bottom":"0mm","left":"0mm","right":"0mm"},
             print_background=True)
    browser.close()
```

关键：`page.pdf()`的margin设0mm，边距由CSS @page控制，否则叠加。

---

# 阶段3：投稿发布（arXiv / Zenodo）

## 核心问题

arXiv编译服务器=Linux+TeX Live，无Windows专有中文字体。

| 本地字体(Windows) | arXiv Linux替代 |
|-------------------|-----------------|
| SimSun | FandolSong-Regular.otf |
| SimHei | FandolHei-Regular.otf |
| KaiTi | FandolKai-Regular.otf |
| FangSong | FandolFang-Regular.otf |

## 推荐方案：ctexart + Fandol

```latex
\documentclass[11pt,a4paper]{ctexart}
\setCJKmainfont{FandolSong-Regular.otf}[BoldFont=FandolHei-Regular.otf]
\setCJKsansfont{FandolHei-Regular.otf}
\setCJKmonofont{FandolFang-Regular.otf}
```

⚠️ 必须用File Name（`FandolSong-Regular.otf`），不能用Font Name。

## 编译验证

```bash
xelatex -interaction=nonstopmode -halt-on-error file.tex
xelatex -interaction=nonstopmode -halt-on-error file.tex  # 二次稳定交叉引用
```

## 打包命名规则

| ❌ | ✅ |
|----|----|
| Pingquanqi_V3_arXiv.zip | pingquanqi.zip |
| Pingquanqi_V3_Final.zip | （纯英文、小写、无版本号） |

## arXiv提交（Agent引导，用户确权）

Agent辅助填表（CDP浏览器），最终提交由用户点击。cs.CY首次投稿需endorsement。

## Endorsement背书（cs.CY必须）

| 路径 | 条件 |
|------|------|
| 自动背书 | 机构邮箱(.edu/.ac.cn)+已claim论文署名 |
| 个人背书 | 找arXiv CS领域≥3篇论文的endorser担保 |

Endorser资格：arXiv任意CS子类≥3篇、3个月~5年内发表。

### 浏览器投递流程（Agent引导，用户确权）

| 步骤 | 操作 | 谁做 |
|------|------|------|
| ① | Agent 导航到 `https://arxiv.org/login` | Agent |
| ② | 用户输入密码登录（Agent 不接触凭证） | 用户 |
| ③ | 登录后 Agent 导航到提交页 | Agent |
| ④ | Agent 从 `.tex` 提取元数据，预填表单 | Agent |
| ⑤ | 用户审核元数据并确认上传 zip | 用户 |
| ⑥ | arXiv 在线编译 → 用户/Agent 一起看编译日志 | 双方 |
| ⑦ | 编译通过 → 选 CC BY-SA 4.0 → 最终提交 | 用户确权 |

**元数据提取（Agent 从 .tex 自动读取）：** `\title{...}` → 标题 / `\author{...}` → 作者、机构、ORCID、邮箱 / `\begin{abstract}...\end{abstract}` → 摘要

## Zenodo DOI首发（arXiv endorsement被卡时的替代）

| | arXiv | Zenodo |
|--|-------|--------|
| 注册门槛 | 需endorsement | GitHub/Google直接登 |
| DOI | 无 | ✅ 有 |
| 接收格式 | .tex源码 | 直接传PDF |
| 补发 | — | 随时同步到arXiv |

操作：zenodo.org → New Upload → 拖PDF → Reserve DOI → 填表 → Publish。国内访问需走代理127.0.0.1:7897。

---

## 参考

- `references/hci-journal-comparison.md` — 期刊路线对比
- `references/arxiv-submission-checklist.md` — arXiv格式审核清单
- `references/arxiv-endorsement-workflow.md` — endorsement详解
- `references/zenodo-first-publication.md` — Zenodo首发流程
- `references/pingquanqi-philosophy-grounding.md` — 哲学地基引用
- 配套脚本：`scripts/generate_print_pdf.py`

---

[^_^]: # G-xueshu-chuban — 论文起草+排版+投稿 | 蹦哒滴路过你身边 2026-06-25
[^_^]: # 合并自：academic-paper-drafting + book-typesetting-skill + latex-arxiv-submission
