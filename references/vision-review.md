# 视觉审查 PDF 排版

当主模型不支持看图时，通过外部视觉 API 审查排版效果。

## 方案一：DashScope（阿里通义千问）

已验证可用的视觉模型：
- 🏆 `qwen3-vl-235b-a22b-thinking` — **最强视觉模型**，235B参数+深度思考能力，描述最精准
- 🥈 `qwen3-vl-32b-thinking` — 32B+思考，平衡之选
- 🥉 `qwen-vl-max` — 高级版
- `qwen-vl-plus` — 标准版

无权限的模型：`qwen2.5-vl-72b-instruct`, `qwen2.5-vl-7b-instruct`（需另外开通）

**开通方式**：在阿里云Model Studio控制台 → 模型广场 → 找到目标模型 → 点击「开启」，选「免费额度用完即停」。每个模型有100万token免费额度。

API端点兼容OpenAI格式。

```bash
curl -s -X POST https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer *** \
  -d '{"model":"qwen-vl-plus","messages":[{"role":"user","content":[{"type":"image_url","image_url":{"url":"data:image/png;base64,..."}},{"type":"text","text":"描述这张截图"}}]}'
```

注意：
- API key 可能被系统截断（显示为 `sk-0d...b052`），需用户手动补齐
- 图片用 base64 编码传入
- 响应包含 `choices[0].message.content`

## OpenClaw 视觉模型配置修复

`vision_analyze` 工具依赖 `tools.media.image.models` 列表顺序。当前配置：

```json
"tools": {
  "media": {
    "image": {
      "models": [
        { "provider": "deepseek-vision", "model": "deepseek-chat" },
        { "provider": "dashscope", "model": "qwen-vl-plus" }
      ]
    }
  }
}
```

**问题**：`deepseek-vision` 用 `api: "openai-completions"` 协议，不支持 `image_url` 内容类型。排第一位导致 vision_analyze 总是先尝试它然后失败，轮不到 dashscope。

**修复**：把 dashscope 排到第一位：

```json
"tools": {
  "media": {
    "image": {
      "models": [
        { "provider": "dashscope", "model": "qwen-vl-max" },
        { "provider": "deepseek-vision", "model": "deepseek-chat" }
      ]
    }
  }
}
```

也可将 `qwen-vl-plus` 升级为 `qwen-vl-max`（更强大）。

## Coding Plan 视觉能力

Coding Plan endpoint (`/api/coding/v3`) 验证可用，但模型 (doubao-seed-2-0-pro) 是纯文本代码模型，不支持视觉输入。看图请求会超时。

Coding Plan 的视觉能力需在火山方舟控制台部署专用视觉模型。

## Windows 上调用 API 的坑

- 命令行中 API key 含 `!` 字符会被 bash 历史扩展：用 `set +H` 禁用或从文件读取
- 命令行长度不能超过 ~8191 字符（Windows 限制），长 base64 需用 `@file.json` 方式传参
- `write_file` 工具会自动把疑似密钥的字符串替换为 `***`，需要从文件读取真实 key
- **推荐用 Python subprocess 调用 curl**（比 bash 直接调稳定），或者直接用 Python `urllib`

## Python urllib 方式（绕过 bash 坑）

```python
import urllib.request, json

with open(r"C:\temp\vision_key.txt") as f:
    key = f.read().strip()

with open("image.png", "rb") as f:
    import base64
    b64 = base64.b64encode(f.read()).decode("ascii")

payload = {
    "model": "qwen-vl-plus",
    "messages": [{"role": "user", "content": [
        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64}"}},
        {"type": "text", "text": "描述这张截图"}
    ]}]
}

req = urllib.request.Request(
    "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions",
    data=json.dumps(payload).encode(),
    headers={"Content-Type": "application/json", "Authorization": "Bearer " + key}
)
resp = urllib.request.urlopen(req, timeout=30)
result = json.loads(resp.read())
print(result["choices"][0]["message"]["content"])
```
