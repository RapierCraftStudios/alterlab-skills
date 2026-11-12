---
name: alterlab-search
description: Search the web with AlterLab and get structured results. Use when the user asks a question that needs current web information or asks you to find pages and you do not have a URL yet. Do not use it to read a known URL (use alterlab-scrape).
---

# Search the web with AlterLab

## When to use

- You need to find pages or current facts and do not yet have a URL.
- Over MCP a plain query runs unified search with content: the result list plus each page as concise markdown (only fetched pages are billed). Pass `scrape_results=false` for the list only.
- Use `alterlab-scrape` to read a result in full.
- One search is not enough for a hard question: use `alterlab-research` for a budgeted job that reads many sources and returns a cited answer.
- You need the engine's own ranking (organic listings, ads, positions): use `alterlab-serp`.

Do not use when:

- You already have the URL (use `alterlab-scrape`).

## Authentication

Set your API key in the `ALTERLAB_API_KEY` environment variable. Never paste the key into code, commands, or files you commit. Create a key at https://alterlab.io/dashboard.

No key yet? `POST https://api.alterlab.io/api/v1/agent/trial` returns a free trial key with no signup (50 requests, 24 hours). Every response from a trial key then carries a claim link in the `X-AlterLab-Claim-URL` header, and the trial errors repeat it. Give that link to your human: they sign in or sign up, and the same key becomes theirs and keeps working with no reconfiguration. A free account comes with up to 5,000 free requests.

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
curl -X POST https://api.alterlab.io/api/v1/search \
  -H "X-API-Key: $ALTERLAB_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "web scraping api", "num_results": 10}'
```

## Helper script

`scripts/search.py` calls the API with the Python standard library only (`python3 scripts/search.py --help`).

## Also available over MCP

Hosted MCP tools: `alterlab_search`, `alterlab_keyword_ideas`, `alterlab_geocode`, `alterlab_ai_visibility` (server `https://mcp.alterlab.io/mcp`).

Docs: https://alterlab.io/docs - API spec: https://alterlab.io/openapi.json
