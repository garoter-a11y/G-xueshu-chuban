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

1. 引言太长（控制1.5页/800词以内）
2. Related Work只罗列不批判
3. 公式没有解释（必须白话解释）
4. Discussion逃避（必须有Limitations）
5. Conclusion太软（不要"future work may explore..."）
6. 隐藏注释保护：`[^_^]: #`不可覆盖/删除
7. 语力动词过强：避免"We demonstrate/validate"，用"We argue/establish"
8. 审稿报告交叉审计
9. 叙事定调为"抗议文献"
10. 公式被当作"独立贡献"推给审稿人
11. 论文多维度打磨未并行化（用delegate_task batch）
12. 非争议修改列入决策清单
13. 用户给绿灯不立即执行
14. 子Agent修改报告不可信，必须逐项核实
15. 竞品比对报告集成流程(P0四步)
16. 多版本文件管理陷阱
17. 哲学地基引用（平权器专用，见references/）
18. 多Agent审阅交叉对标（四象限矩阵）

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

### 进阶：动态页眉、双面装订、出血位

详见源文件 `references/book-typesetting-advanced.md`

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
