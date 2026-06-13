---
name: book-typesetting
description: "HTML→印刷级PDF纸质书排版。小16开(170×240mm)、CSS Paged Media、Playwright PDF生成、pypdf合拼+页码。保留原始UI设计，含动态页眉、双面装订留白、自动目录等专业印刷知识。"
version: 3.0.0
author: 蹦哒滴路过你身边
platforms: [windows]
---

# Book Typesetting — 纸质书排版（HTML → 印刷级PDF）

将HTML文档排版为可直接送打印店的印刷级PDF。**保留原始UI设计**（渐变背景、金色装饰、标签配色等），只注入页面尺寸和边距，不替换设计。

## 适用场景

- 个人出书 / 赠书（赛鸽全书2026等）
- 技术文档汇编
- 译文文集排版
- 任何HTML→印刷PDF需求

---

## 排版规格确认（每次必问用户）

| 项目 | 示例 |
|------|------|
| 纸张尺寸 | 170mm × 240mm（小16开） |
| 打印方式 | 单面 / 双面 |
| 页码规则 | 封面/寄语无页码，正文从第1页开始 |
| 排序 | 封面→寄语→第一章→第二章→... |
| 正文字体 | 宋体(SimSun) / 黑体(SimHei) |
| 统计数字 | 横排居中 / 竖排居中（问用户） |

---

## ⚠️ 红线（从教训中总结）

### 设计红线
- **绝对不要替换原始CSS设计！** 用户花精力做的设计（金色装饰、渐变背景、装饰角、标签配色），只能在原有基础上加 `@page` 尺寸和边距
- `@media print { body { background: white !important; } }` 防止原CSS米色背景铺满整页
- 内容块用 `max-width: 130mm` + `margin: 0 auto` 居中，四边留白均匀

### 流程红线
- **必须先问「是否现在执行」，等用户点头再动手** — 不能一听到任务就冲出去
- **先做试排**给用户看效果，再批量处理
- **听用户说完再行动** — 用户可能有后续要求
- 项目完结时用语音播报（配合 voice-announce skill）

---

## 核心工作流

```
源HTML → 注入印刷CSS → Playwright Chromium PDF → pypdf合拼+页码 → 印刷级PDF
```

---

## 第1步：印刷CSS — 从基础到专业

### 基础（必须）

```css
@page {
  size: 170mm 240mm;
  margin: 15mm 15mm 18mm 15mm;   /* 上 右 下 左 */
  @bottom-center {
    content: counter(page);
    font-family: "Georgia", "Times New Roman", serif;
    font-size: 9pt;
    color: #999;
  }
}
@page :blank { @bottom-center { content: none; } }  /* 空白页无页码 */
@page :first { @bottom-center { content: none; } }   /* 首页无页码 */

@media print {
  body { background: white !important; }  /* 防止body背景铺满全页 */
}
```

### 进阶1：动态页眉（🔥 新！章节名自动注入页眉）

让每章的标题自动出现在页眉上，无需手工写：

```css
/* 在HTML中：把标题内容存到"chapter-title"变量 */
h1 { string-set: chapter-title content(text); }
h2 { string-set: section-title content(text); }

/* 在@page中：把变量显示在页眉 */
@page :right {
  @top-right {
    content: string(chapter-title);
    font-size: 9pt;
    color: #666;
  }
}
@page :left {
  @top-left {
    content: string(section-title);
    font-size: 9pt;
    color: #666;
  }
}
```

效果：奇数页右上角显示章名，偶数页左上角显示节名，自动跟随内容变化。

### 进阶2：双面打印 / 装订留白（🔥 新！）

专业书籍需要左右页不对称边距——装订侧（内侧）留更多空间：

```css
@page :left {   /* 偶数页（左页）—— 装订侧在右边 */
  margin: 22mm 20mm 22mm 30mm;  /* 左边更大 = 外侧 */
}
@page :right {  /* 奇数页（右页）—— 装订侧在左边 */
  margin: 22mm 30mm 22mm 20mm;  /* 右边更大 = 外侧 */
}
```

### 进阶3：出血位 + 裁切标记（🔥 新！送打印店用）

如果页面设计有**延伸到纸边的背景/图片**，需要加出血：

```css
@page {
  size: 170mm 240mm;
  bleed: 3mm;         /* 出血3mm */
  marks: crop cross;    /* 裁切标记+十字线 */
}
```

注意：Playwright 的 `page.pdf()` **不支持** `marks` 和 `bleed` CSS属性。如果打印店要求出血+裁切标记，有两个方案：
| 方案 | 做法 | 适用 |
|:----:|------|------|
| 🅰 做图时留出血 | HTML设计图本身四周多3mm内容 | 最简单 |
| 🅱 转PDF工具 | 用 Adobe Acrobat / 打印店软件加裁切线 | 专业 |

### 进阶4：自动目录页码（🔥 新！）

生成目录时自动标注"见第X页"：

```css
/* 目录条目后显示目标页码 */
.toc a::after {
  content: leader('.') target-counter(attr(href), page);
  font-size: 10pt;
  color: #333;
}
```

### 进阶5：防溢出（页末孤行控制）

```css
p, li { orphans: 3; widows: 3; }    /* 至少3行在一起，防止孤行 */
h1, h2, h3 { break-after: avoid; }  /* 标题后不换页 */
table, figure, pre { break-inside: avoid; }  /* 表格/代码块不断开 */
section.chapter { break-before: page; }       /* 每章从新页开始 */
```

---

## 第2步：用 Playwright 生成PDF

### 环境要求

```bash
pip install playwright pypdf
python -m playwright install chromium
```

### 生成命令

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(f"file:///{html_path}", wait_until="networkidle", timeout=30000)
    page.pdf(
        path=pdf_path,
        width="170mm",
        height="240mm",
        margin={"top": "0mm", "bottom": "0mm", "left": "0mm", "right": "0mm"},
        print_background=True,   # 保留渐变背景
    )
    browser.close()
```

**关键：** `page.pdf()` 的 `margin` 参数设 `0mm`，边距由 CSS `@page` 控制，否则边距会叠加。

### 注入CSS脚本

配套脚本 `scripts/generate_print_pdf.py` 已存在，用法：

```bash
python generate_print_pdf.py input.html output.pdf 170mm 240mm
```

自动检测HTML中是否已有 `@page`，没有则注入标准CSS。

---

## 第3步：页码处理

### 方案A：CSS自动页码（推荐 ✅）

在CSS `@page` 中用 `@bottom-center { content: counter(page); }` 即可。

### 方案B：pypdf FreeText（备用，不推荐）

```python
from pypdf import PdfReader, PdfWriter
from pypdf.annotations import FreeText

reader = PdfReader(pdf_path)
writer = PdfWriter()
for i, page in enumerate(reader.pages):
    writer.add_page(page)
    if i >= start_page:  # 跳过封面/扉页
        page_num = i - start_page + 1
        annot = FreeText(
            text=str(page_num),
            rect=(page.mediabox.width/2 - 15, 10, page.mediabox.width/2 + 15, 28),
            font="Times-Roman",
            font_size="9pt",
        )
        writer.add_annotation(page_number=i, annotation=annot)
```

**注意：** pypdf FreeText 在某些阅读器里显示为黑色方块。优先用CSS `@page` 方案。

---

## 第4步：合拼多篇为全书

```python
from pypdf import PdfWriter

writer = PdfWriter()
for pdf_path in sorted_pdf_list:   # 按排序顺序：封面→寄语→繁育→饲养→...
    reader = PdfReader(pdf_path)
    for page in reader.pages:
        writer.add_page(page)
writer.write("赛鸽全书2026_合并.pdf")
```

---

## 工具选择对比（Windows实测）

| 工具 | 印刷CSS支持 | 本机可用 | 说明 |
|:----:|:----------:|:--------:|------|
| ✅ **Playwright** | 基础@page ✅ | ✅ | 唯一稳定方案 |
| ❌ Edge headless | 基础@page ✅ | ❌ | 代理环境冲突，不可用 |
| ❌ WeasyPrint | 完整@page ✅ | ❌ | 需GTK3 DLL凑不齐 |
| ❌ pagedjs-cli | 完整@page ✅ | ❌ | npm install超时 |
| ⭐ Paged.js polyfill | 完整✅ | ✅ 浏览器预览 | 配合Playwright用 |
| 💰 Prince XML | 完整✅ | ❌付费 | 商业版最强，但收费 |

### Paged.js 浏览器预览（🔥 新！）

在HTML中加一行，即可在浏览器预览分页效果：

```html
<script src="https://unpkg.com/pagedjs/dist/paged.polyfill.js"></script>
```

然后本地用 Live Server 打开HTML，浏览器自动显示分页预览。确认效果后，再用 Playwright 生成最终PDF。

---

## PDF生成后验证

```python
from pypdf import PdfReader

r = PdfReader(pdf_path)
print(f"共 {len(r.pages)} 页")
page = r.pages[0]
w_mm = page.mediabox.width / 72 * 25.4
h_mm = page.mediabox.height / 72 * 25.4
print(f"尺寸: {w_mm:.0f}mm × {h_mm:.0f}mm")

# 检查编码/字体是否都正常
for i, p in enumerate(r.pages[:3]):
    text = p.extract_text()[:100]
    print(f"第{i+1}页预览: {text}...")
```

---

## 排版检查清单

- [ ] 纸张尺寸正确（170×240mm）
- [ ] 四周留白均匀（15~22mm）
- [ ] 内容块在页面居中（max-width: 130mm）
- [ ] 原始UI设计保留（渐变、金色、标签配色）
- [ ] body背景色被 `white !important` 覆盖（防铺满）
- [ ] 封面底部/目录顶部有额外间距
- [ ] 页码正确（封面/扉页无页码，正文从1开始）
- [ ] 无「溢出一行多一页」问题（看 widows/orphans 控制）
- [ ] 双面打印时左右页边距对称（如需要）
- [ ] 动态页眉正确显示章节名（如需要）
- [ ] PDF可正常打开（用 pypdf 验证尺寸+页数+文字）

---

## 出版社排版规范参考

来自国内出版行业标准：

| 项目 | 规范 |
|:----|:----|
| 小16开（787×1092 1/16） | 185×260mm |
| 大16开（850×1168 1/16） | 210×285mm |
| 本书采用尺寸 | 170×240mm（自定义小16开） |
| 正文行距 | 默认1.5倍行距 / 固定值22pt |
| 段首缩进 | 2字符（text-indent: 2em） |
| 一级标题 | 黑体/标宋，三号(~16pt) |
| 二级标题 | 黑体/标宋，四号(~14pt) |
| 正文 | 宋体，五号(~10.5pt) |
| 页眉 | 书名（左页）+ 章名（右页） |
| 通栏插图 | 居中，下空1行 |
| 表格 | 用三线表，表头加粗 |

来源：CSDN 中国出版社书籍排版规则、WPS出版规范

---

## 网络资源索引

以下资源是本次调研中找到的有用参考，可随时查阅：

### CSS Paged Media 教程
| 资源 | 地址 | 说明 |
|:----|:----|:----|
| Smashing Magazine | https://www.smashingmagazine.com/2015/01/designing-for-print-with-css | Rachel Andrew 经典教程 |
| print-css.rocks | https://print-css.rocks | 7款工具对比教程（2026.7下线） |
| Doppio CSS Guide | https://doppio.sh/guide/css-paged-media | 完整CSS Paged Media指南 |
| W3C Paged Media Spec | https://www.w3.org/TR/css-page-3/ | 官方规范 |
| W3C Generated Content | https://www.w3.org/TR/css-gcpm-3/ | 动态页眉/页脚官方规范 |

### 开源项目
| 项目 | 地址 | 说明 |
|:----|:----|:----|
| Paged.js | https://github.com/pagedjs/pagedjs | 浏览器分页预览库 |
| Paged.js官网 | https://pagedjs.org | 文档+教程 |
| print-css-rocks源码 | https://github.com/zopyx/print-css-rocks | 教程源码 |
| CSS Book Demo | https://github.com/michaelperrin/blog-css-book-demo | 完整书籍CSS Demo |

### Playwright PDF相关
| 资源 | 地址 |
|:----|:----|
| Playwright Web打印PDF | https://blog.csdn.net/weixiaoyiDM/article/details/150016650 |
| Playwright page.pdf踩坑 | https://runebook.dev/zh/docs/playwright/api/class-page/page-pdf |
| web-print-pdf批量打印 | https://cloud.tencent.com.cn/developer/article/2554264 |

### 中文排版规范
| 资源 | 地址 |
|:----|:----|
| 中国出版社排版规则 | https://blog.csdn.net/chenby186119/article/details/150154906 |
| 纸张尺寸对照 | https://sizepedia.com/zh/paper-size |
| 书籍排版格式标准 | 百度文库搜索关键词 |

---

## 踩坑记录（本机Windows特有）

### Edge headless不可用
Clash Verge 7897端口代理环境下，Edge `--print-to-pdf` 无法通过 `file://` 加载本地HTML。只能接受极短data URI。**必须用 Playwright 的 Chromium**。

### Playwright PermissionError
如果输出PDF正在被阅读器打开，Playwright无法写入。换用新文件名（`_新`/`_v2` 后缀）。

### 模型不支持看图
当前模型 deepseek-v4-flash 无 vision。用户发送截图时，需要通过外部视觉API（DashScope qwen3-vl 或 qwen-vl-plus）分析。

### body背景色铺满问题
用户HTML的 `body { background: ... }` 会铺满整页包括 `@page` 边距区。必须用 `@media print { body { background: white !important; } }` 覆盖。

---

## 本机参考路径

- 排版工具脚本: `~/.openclaw/workspace/mcp-bridge/book_typesetter_v2.py`
- 章节简介PDF生成: `~/.openclaw/workspace/mcp-bridge/gen_intro_pw.py`
- API仪表盘: `~/.openclaw/workspace/mcp-bridge/api_dashboard_server.py`
- 源HTML目录: `Desktop\12篇\项目章节\`
- 文章PDF目录: `Desktop\赛鸽全书2026_第一章_PDF - 副本\`
- 备份路径: `D:\BaiduSyncdisk\Garoter datebase\general\备份\hermes备份\`
- 配套生成脚本: 本skill的 `scripts/generate_print_pdf.py`

---

## 参考文件

本skill附带的参考文件：
- `references/css-paged-media.md` — CSS Paged Media 关键参考速查
- `references/vision-review.md` — 视觉API看图分析
- `references/ark-coding-plan.md` — 火山引擎Coding Plan配置
- `scripts/generate_print_pdf.py` — 一键PDF生成脚本
