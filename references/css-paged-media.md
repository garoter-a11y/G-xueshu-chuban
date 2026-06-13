# CSS Paged Media 关键参考

纸质书排版的核心 CSS 规范。

## @page 规则

```css
@page {
  size: 170mm 240mm;           /* 纸张尺寸 */
  margin: 22mm 20mm;           /* 上 右 下 左 */
  @top-center { content: "章名"; }         /* 页眉 */
  @bottom-center { content: counter(page); } /* 页脚页码 */
}
@page :blank { @bottom-center { content: none; } }  /* 空白页无页码 */
@page :first { @bottom-center { content: none; } }   /* 首页无页码 */
```

## 防溢出

```css
p, li { orphans: 3; widows: 3; }
h1, h2, h3 { break-after: avoid; }
table, figure, pre { break-inside: avoid; }
article { break-before: page; }
```

## 工具对比

| 工具 | print CSS支持 | Windows可用性 |
|------|:------------:|:-------------:|
| Playwright (Chromium) | 基础@page ✅ | ✅ 安装简单 |
| WeasyPrint | 完整 ✅ | ❌ 需GTK3 |
| Prince XML | 完整 ✅ | 💰 商业付费 |
| Paged.js CLI | 完整✅ | ❌ 需下载Chrome |
| Edge headless | 基础@page✅ | ❌ 本机代理环境不可用 |

## 注意事项

- `@bottom-center` 等 margin boxes 只在 print formatter 中生效，Edge/Chrome 普通 `window.print()` 不支持
- Playwright 的 `page.pdf()` 会尊重 `@page` 中的 margin boxes
- Google Fonts 在离线打印时不可用 → 换用本地字体 (SimSun/SimHei)
