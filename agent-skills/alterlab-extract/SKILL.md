---
name: alterlab-extract
description: Extract structured JSON from any web page with AlterLab using a JSON schema. Use when the user wants specific fields (prices, titles, listings, contacts) rather than the full page text.
---

# Extract structured data with AlterLab

## When to use

- You know which fields you need and want them as JSON.
- The same page layout will be read repeatedly and output must be machine-readable.

Do not use when:

- You want the whole page as text (use `alterlab-scrape`).

## Authentication

Set your API key in the `ALTERLAB_API_KEY` environment variable. Never paste the key into code, commands, or files you commit. Create a key at https://alterlab.io/dashboard.

```bash
export ALTERLAB_API_KEY="..."  # set in your shell, not in the repo
```

## Examples

### Python

```python
import os
from alterlab import AlterLabSync

client = AlterLabSync(api_key=os.environ["ALTERLAB_API_KEY"])
result = client.scrape(
    "https://example.com",
    extraction_schema={"type": "object", "properties": {"title": {"type": "string"}, "price": {"type": "string"}, "description": {"type": "string"}}},
)
print(result["filtered_content"])  # dict matching your schema
```

### Node.js

```javascript
import { AlterLab } from "alterlab";

const client = new AlterLab({ apiKey: process.env.ALTERLAB_API_KEY });
const result = await client.scrape({
  url: "https://example.com",
  extraction_schema: { type: "object", properties: { title: { type: "string" }, price: { type: "string" }, description: { type: "string" } } },
});
console.log(result.filtered_content);
```

### curl

```bash
curl -X POST https://api.alterlab.io/v1/scrape \
  -H "X-API-Key: $ALTERLAB_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com", "extraction_schema": {"type": "object", "properties": {"title": {"type": "string"}, "price": {"type": "string"}, "description": {"type": "string"}}}}'
```

## Helper script

`scripts/extract.py` calls the API with the Python standard library only (`python3 scripts/extract.py --help`).

## Also available over MCP

Hosted MCP tools: `alterlab_extract` (server `https://mcp.alterlab.io/mcp`).

Docs: https://alterlab.io/docs - API spec: https://alterlab.io/openapi.json
