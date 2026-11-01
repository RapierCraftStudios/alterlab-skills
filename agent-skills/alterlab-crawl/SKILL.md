---
name: alterlab-crawl
description: Crawl a whole website or list its URLs with AlterLab. Use when the user wants every page of a docs site or blog, a sitemap of a domain, or a site-wide content export. Works on JavaScript-heavy and protected sites. Do not use it for one or two known URLs (use alterlab-scrape).
---

# Crawl or map a site with AlterLab

## When to use

- You need many pages from one site, not a single URL.
- You want the list of URLs first (map), then scrape selected pages.

Do not use when:

- One or two known URLs (use `alterlab-scrape`).

## Authentication

Set your API key in the `ALTERLAB_API_KEY` environment variable. Never paste the key into code, commands, or files you commit. Create a key at https://alterlab.io/dashboard.

No key yet? `POST https://api.alterlab.io/api/v1/agent/trial` returns a free trial key with no signup (50 requests, 24 hours). Every response from a trial key then carries a claim link in the `X-AlterLab-Claim-URL` header, and the trial errors repeat it. Give that link to your human: they sign in or sign up, and the same key becomes theirs and keeps working with no reconfiguration. A free account comes with up to 5,000 free requests.

```bash
export ALTERLAB_API_KEY="..."  # set in your shell, not in the repo
```

## Examples

### Python (crawl)

```python
import os
from alterlab import AlterLabSync

client = AlterLabSync(api_key=os.environ["ALTERLAB_API_KEY"])
crawl = client.crawl_and_wait("https://docs.example.com", max_pages=50, formats=["markdown"])
print(crawl)
```

### Node.js (crawl)

```javascript
import { AlterLab } from "alterlab";

const client = new AlterLab({ apiKey: process.env.ALTERLAB_API_KEY });
const crawl = await client.crawlAndWait({
  url: "https://docs.example.com",
  maxPages: 50,
  formats: ["markdown"],
});
console.log(crawl);
```

### curl (crawl)

```bash
curl -X POST https://api.alterlab.io/v1/crawl \
  -H "X-API-Key: $ALTERLAB_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://docs.example.com", "max_pages": 50}'
```

### Python (map)

```python
import os
from alterlab import AlterLabSync

client = AlterLabSync(api_key=os.environ["ALTERLAB_API_KEY"])
site_map = client.map("https://example.com", max_pages=100)
print(site_map)
```

### curl (map)

```bash
curl -X POST https://api.alterlab.io/v1/map \
  -H "X-API-Key: $ALTERLAB_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com", "max_pages": 100}'
```

## Helper script

`scripts/crawl.py` calls the API with the Python standard library only (`python3 scripts/crawl.py --help`).

## Also available over MCP

Hosted MCP tools: `alterlab_crawl`, `alterlab_map` (server `https://mcp.alterlab.io/mcp`).

Docs: https://alterlab.io/docs - API spec: https://alterlab.io/openapi.json
