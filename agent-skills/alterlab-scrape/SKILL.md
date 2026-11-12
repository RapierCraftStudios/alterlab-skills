---
name: alterlab-scrape
description: Use when you have one URL and want its content; for an image use alterlab_screenshot, for 2-20 URLs alterlab_batch_scrape, for a whole site alterlab_crawl. Fetch any URL as clean markdown, text, HTML or JSON with AlterLab, including JavaScript-heavy and protected pages. Also use when the user asks to read, fetch, download or summarize a web page, take a screenshot, or scrape a list of URLs.
---

# Scrape a web page with AlterLab

## When to use

- You need the content of a specific URL as LLM-ready markdown.
- A plain HTTP fetch fails, returns a challenge page, or the page needs JavaScript.
- You have a short list of URLs to fetch in one request (batch).

Do not use when:

- The user needs a whole site (use `alterlab-crawl`) or structured fields (use `alterlab-extract`).

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
result = client.scrape("https://example.com")
print(result["content"])
```

### Node.js

```javascript
import { AlterLab } from "alterlab";

const client = new AlterLab({ apiKey: process.env.ALTERLAB_API_KEY });
const result = await client.scrape({ url: "https://example.com" });
console.log(result.content);
```

### curl

```bash
curl -X POST https://api.alterlab.io/api/v1/scrape \
  -H "X-API-Key: $ALTERLAB_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com"}'
```

### curl (batch of URLs)

```bash
curl -X POST https://api.alterlab.io/api/v1/batch \
  -H "X-API-Key: $ALTERLAB_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"urls": ["https://example.com/a", "https://example.com/b"]}'
```

## Helper script

`scripts/scrape.py` calls the API with the Python standard library only (`python3 scripts/scrape.py --help`).

## Also available over MCP

Hosted MCP tools: `alterlab_scrape`, `alterlab_screenshot`, `alterlab_batch_scrape`, `alterlab_batch`, `alterlab_estimate_cost`, `alterlab_site_profile`, `alterlab_create_account`, `alterlab_job`, `alterlab_balance`, `alterlab_workflow_run` (server `https://mcp.alterlab.io/mcp`).

Docs: https://alterlab.io/docs - API spec: https://alterlab.io/openapi.json
