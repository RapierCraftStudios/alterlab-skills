---
name: alterlab-research
description: Run a budgeted AlterLab research job that plans searches, reads many sources, follows leads and returns a cited report or structured JSON. Use when one search is not enough: comparisons, market or due-diligence questions, or any answer that needs a citation per claim. Do not use it for a quick lookup (use alterlab-search).
---

# Research a hard question with citations with AlterLab

## When to use

- The question needs many sources and a citation for every claim.
- You want a structured JSON answer assembled from the open web.
- Set `max_cost_microcents` to cap platform spend; the job never exceeds it.
- Research runs on your own LLM key (BYOK): without one the API returns `byok_key_required` and charges nothing.

Do not use when:

- A quick lookup or a list of links (use `alterlab-search`).
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
curl -X POST https://api.alterlab.io/api/v1/research \
  -H "X-API-Key: $ALTERLAB_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "Which web scraping APIs offer per-result pricing?", "max_cost_microcents": 500000, "max_sources": 20}'
```

## Helper script

`scripts/research.py` calls the API with the Python standard library only (`python3 scripts/research.py --help`).

## Also available over MCP

Hosted MCP tools: `alterlab_research` (REST: `POST /api/v1/research`, `GET /api/v1/research/{job_id}`) (server `https://mcp.alterlab.io/mcp`).

Docs: https://alterlab.io/docs - API spec: https://alterlab.io/openapi.json
