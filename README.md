# Book Typesetting Skill

**HTML → 印刷级PDF纸质书排版**

将HTML文档排版为可直接送打印店的印刷级PDF。保留原始UI设计（渐变背景、金色装饰等），只注入页面尺寸和边距。

## 特性

- ✅ **小16开(170×240mm)** 纸质书排版
- ✅ **保留原始CSS设计** — 不替换你的UI
- ✅ **动态页眉** — 章节名自动注入页眉
- ✅ **双面装订留白** — 左右页不对称边距
- ✅ **自动目录页码** — target-counter 生成页码引用
- ✅ **防孤行控制** — widows/orphans 专业排版
- ✅ **Playwright Chromium** 生成PDF（Windows稳定方案）
- ✅ **Paged.js 预览** — 浏览器里先看效果
- ✅ **多篇合拼** — pypdf 合并为全书
- ✅ **出版社规范参考** — 国内出版标准

## 适用场景

- 个人出书 / 赠书
- 技术文档汇编
- 译文文集排版
- 任何HTML→印刷PDF需求

## 快速开始

```bash
pip install playwright pypdf
python -m playwright install chromium
python scripts/generate_print_pdf.py input.html output.pdf 170mm 240mm
```

## 依赖

- Python 3.12+
- Playwright (with Chromium)
- pypdf

## 作者

- **王宇**（笔名：蹦哒滴路过你身边）

## 许可

MIT License
