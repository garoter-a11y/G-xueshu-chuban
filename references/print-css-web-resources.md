# 印刷排版网络资源索引

> 2026-06-13 搜索汇总

## 教程与指南

| 资源 | 链接 | 说明 |
|------|------|------|
| Smashing Magazine | https://www.smashingmagazine.com/2015/01/designing-for-print-with-css | CSS印刷设计经典文章，Rachel Andrew |
| print-css.rocks | https://print-css.rocks | 完整PrintCSS教程，7款工具对比（2025年后legacy模式） |
| CSS Paged Media Guide | https://doppio.sh/guide/css-paged-media | 完整指南：@page、分页、命名页面 |
| Paged.js Docs | https://pagedjs.org/en/documentation/5-web-design-for-print | 浏览器内分页预览工具 |
| CSS-Tricks @page | https://css-tricks.com/almanac/rules/p/page | @page 速查 |
| W3C CSS Paged Media Spec | https://www.w3.org/TR/css-page-3/ | 官方规范 |
| W3C Generated Content for Paged Media | https://www.w3.org/TR/css-gcpm-3/ | 动态页眉页脚、string-set、running elements |

## 中文资源

| 资源 | 链接 | 说明 |
|------|------|------|
| CSDN 出版社排版规则 | https://blog.csdn.net/chenby186119/article/details/150154906 | 方正书版标准、国内出版规范 |
| Playwright Web打印PDF | https://blog.csdn.net/weixiaoyiDM/article/details/150016650 | 浏览器实例复用、内存管理 |
| Playwright page.pdf 踩坑 | https://runebook.dev/zh/docs/playwright/api/class-page/page-pdf | 字体、边距、渐变注意事项 |
| 纸张尺寸对照表 | https://sizepedia.com/zh/paper-size | A4、B5、16开等尺寸对照 |

## GitHub 项目

| 项目 | 链接 | 说明 |
|------|------|------|
| pagedjs/pagedjs | https://github.com/pagedjs/pagedjs | ⭐ 浏览器分页工具 |
| zopyx/print-css-rocks | https://github.com/zopyx/print-css-rocks | PrintCSS教程+工具对比 |
| michaelperrin/blog-css-book-demo | https://github.com/michaelperrin/blog-css-book-demo | 完整书籍CSS Demo |
| markovskiL/pdf-generation | https://github.com/markovskiL/pdf-generation | WeasyPrint PDF生成方案 |
| coockie/css-for-print | https://blog.csdn.net/gitblog_00014/article/details/139189813 | 打印CSS样例 + book.html |

## 商业工具

| 工具 | 链接 | 说明 |
|------|------|------|
| PDFreactor | https://www.pdfreactor.com | 商业HTML→PDF引擎，完整CSS Paged Media支持 |
| Prince XML | https://www.princexml.com | 商业，最完善的PrintCSS引擎 |
| Antenna House | https://www.antennahouse.com | 商业排版引擎 |
| DocRaptor | https://docraptor.com | 基于Prince的云API |

## 关键技巧速查

### 动态页眉（running headers）
```css
h1 { string-set: chapter-title content(text); }
@page { @top-center { content: string(chapter-title); } }
```

### 双面打印装订边距
```css
@page :left  { margin: 20mm 15mm 20mm 25mm; }
@page :right { margin: 20mm 25mm 20mm 15mm; }
```

### 目录自动页码
```css
.toc-entry a::after {
  content: " · 第" target-counter(attr(href), page) "页";
}
```

### 空白页隐藏页码
```css
@page :blank { @bottom-center { content: none; } }
```

### 防溢出
```css
p, li { orphans: 3; widows: 3; }
h1, h2, h3 { break-after: avoid; }
table, figure, pre { break-inside: avoid; }
```
