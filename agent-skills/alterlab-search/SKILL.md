---
name: alterlab-search
description: Search the web with AlterLab and get structured results. Use when the user asks a question that needs current web information or asks you to find pages.
---

# Search the web with AlterLab

## When to use

- You need to find pages or current facts and do not yet have a URL.
- Follow up the best results with `alterlab-scrape` to read them in full.

Do not use when:

- You already have the URL (use `alterlab-scrape`).

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
results = client.search("web scraping api", num_results=10)
print(results)
```

### curl

```bash
curl -X POST https://api.alterlab.io/v1/search \
  -H "X-API-Key: $ALTERLAB_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "web scraping api", "num_results": 10}'
```

## Helper script

`scripts/search.py` calls the API with the Python standard library only (`python3 scripts/search.py --help`).

## Also available over MCP

Hosted MCP tools: `alterlab_search` (server `https://mcp.alterlab.io/mcp`).

Docs: https://alterlab.io/docs - API spec: https://alterlab.io/openapi.json
