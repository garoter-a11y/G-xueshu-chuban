#!/usr/bin/env python3
"""
Generate a print-ready PDF from HTML using Playwright.
Usage: python generate_print_pdf.py <input.html> <output.pdf> [width] [height]

Width/height default to 170mm x 240mm (小16开).
"""
import sys, os, re
from playwright.sync_api import sync_playwright

HTML = sys.argv[1]
PDF  = sys.argv[2]
W    = sys.argv[3] if len(sys.argv) > 3 else "170mm"
H    = sys.argv[4] if len(sys.argv) > 4 else "240mm"
MARGIN = "22mm"

# Inject @page CSS if not present
with open(HTML, "r", encoding="utf-8") as f:
    html = f.read()

# Inject body background fix + page CSS
inject = f"""
<style>
@page {{
  size: {W} {H};
  margin: {MARGIN};
  @bottom-center {{
    content: counter(page);
    font-family: "Georgia", "Times New Roman", serif;
    font-size: 9pt;
    color: #999;
  }}
}}
@page :blank {{
  @bottom-center {{ content: none; }}
}}
@media print {{
  body {{ background: white !important; }}
}}
</style>
"""

if "@page" not in html:
    html = html.replace("</head>", f"\n{inject}\n</head>")
    with open(HTML, "w", encoding="utf-8") as f:
        f.write(html)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(f"file:///{os.path.abspath(HTML)}", wait_until="networkidle", timeout=30000)
    # IMPORTANT: page.pdf() margin must be 0mm — margins are controlled by CSS @page
    page.pdf(path=PDF, width=W, height=H, margin={"top": "0mm", "bottom": "0mm", "left": "0mm", "right": "0mm"}, print_background=True)
    browser.close()

from pypdf import PdfReader
r = PdfReader(PDF)
print(f"✅ {PDF} — {len(r.pages)} pages, {r.pages[0].mediabox.width/72*25.4:.0f}x{r.pages[0].mediabox.height/72*25.4:.0f}mm")
