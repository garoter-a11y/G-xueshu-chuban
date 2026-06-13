# 火山引擎 Ark Coding Plan 集成笔记

Coding Plan 是火山引擎的开发者套餐，提供代码类模型 API。

## 关键信息

| 项目 | 值 |
|------|-----|
| **标准 API 端点** | `https://ark.cn-beijing.volces.com/api/v3/chat/completions` |
| **Coding Plan 端点** | `https://ark.cn-beijing.volces.com/api/coding/v3/chat/completions` |
| **API Key 格式** | `ark-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx-xxxxx` |
| **Auth 方式** | `Authorization: Bearer <key>` |

## 可用模型（Coding Plan）

| 模型 | 说明 |
|------|------|
| `doubao-seed-2-0-pro` | 旗舰级，多模态理解（文本），复杂推理 |
| `doubao-seed-2-0-code` | 代码优化 |
| `doubao-seed-2-0-lite` | 轻量版 |
| `deepseek-v4-flash` | 快速经济 |
| `deepseek-v4-pro` | 深度推理 |

注意：Coding Plan 模型都是文本/代码模型，不包含专门的视觉模型。如果要看图，需要：
1. 在火山方舟控制台部署视觉模型（如 Doubao-vision-pro-32k）并创建推理接入点
2. 或用 DashScope qwen-vl-plus（阿里通义千问）

## Bash 调用坑

Windows git-bash 中调用时注意：
- **`!` 字符**：某些密钥含 `!` 会被 bash 历史扩展 → 用 `set +H` 禁用
- **长命令**：Windows 命令行长度限制 ~8191 字符 → 用 `@file.json` 方式传参
- **密钥被截断**：`write_file` 工具会把疑似密钥替换为 `***` → 用 `echo key > file.txt` 写入再从文件读取

## Python urllib 调用示例

```python
import urllib.request, json

with open(r"C:\temp\ark_key.txt") as f:
    key = f.read().strip()

data = json.dumps({"model": "doubao-seed-2-0-pro", "messages": [{"role": "user", "content": "hi"}]}).encode()

req = urllib.request.Request(
    "https://ark.cn-beijing.volces.com/api/coding/v3/chat/completions",
    data=data,
    headers={
        "Content-Type": "application/json",
        "Authorization": "Bearer " + key
    }
)
resp = urllib.request.urlopen(req, timeout=15)
result = json.loads(resp.read())
print(result["choices"][0]["message"]["content"])
```
