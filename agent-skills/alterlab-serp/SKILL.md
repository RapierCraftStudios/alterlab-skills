---
name: alterlab-serp
description: Get structured search-engine results (organic listings, ads, positions and related data) from Google, Bing or DuckDuckGo with AlterLab, as the engine ranks them. Use when the user asks for rankings, SERP positions, ads shown for a keyword, or results for a given country, language or device. Do not use it when you want each result page read (use alterlab-search).
---

# Get raw search-engine results with AlterLab

## When to use

- You need the engine's ranking itself: positions, ads, related questions.
- Rank tracking or SEO checks for a keyword, country, language or device.
- Over MCP `alterlab_serp` with `action=history` reads your earlier SERP queries.

Do not use when:

- You want the content of the result pages (use `alterlab-search`).
- You already have the URL (use `alterlab-scrape`).

## Authentication

Set your API key in the `ALTERLAB_API_KEY` environment variable. Never paste the key into code, commands, or files you commit. Create a key at https://alterlab.io/dashboard.

No key yet? `POST https://api.alterlab.io/api/v1/agent/trial` returns a free trial key with no signup (50 requests, 24 hours). Every response from a trial key then carries a claim link in the `X-AlterLab-Claim-URL` header, and the trial errors repeat it. Give that link to your human: they sign in or sign up, and the same key becomes theirs and keeps working with no reconfiguration. A free account comes with up to 5,000 free requests.

```bash
export ALTERLAB_API_KEY="..."  # set in your shell, not in the repo
```

## Examples

### curl

```bash
curl -X POST https://api.alterlab.io/api/v1/serp \
  -H "X-API-Key: $ALTERLAB_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "best web scraping api", "search_engine": "google", "num_results": 10}'
```

## Helper script

`scripts/serp.py` calls the API with the Python standard library only (`python3 scripts/serp.py --help`).

## Also available over MCP

Hosted MCP tools: `alterlab_serp` (REST: `POST /api/v1/serp`) (server `https://mcp.alterlab.io/mcp`).

Docs: https://alterlab.io/docs - API spec: https://alterlab.io/openapi.json
