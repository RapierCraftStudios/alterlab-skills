---
name: alterlab-knowledge
description: Search and read AlterLab's own docs, blog and guides, free and without an API key. Use first when the user asks how to do something with AlterLab: API parameters, SDKs, MCP setup, pricing, error codes, migration from Firecrawl or ScrapingBee, or a guide for scraping a specific site. Do not use it to fetch a third-party URL (use alterlab-scrape).
---

# Search the AlterLab docs with AlterLab

## When to use

- The user asks how to do something with AlterLab: search before answering from memory.
- You need the current docs page for a parameter, error code, SDK or price.
- Read the best result in full with `read_alterlab_page` or its `markdown_url`.

Do not use when:

- You need to fetch a third-party page (use `alterlab-scrape`).

## Authentication

None. Search and read are free: no API key, no account and no credits.

## Examples

### curl (search)

```bash
curl -sS "https://alterlab.io/api/knowledge/search?q=how+to+scrape+a+javascript+page"
```

### curl (read a result)

```bash
curl -sS "https://alterlab.io/api/knowledge/page?url=https://alterlab.io/docs"
```

## Also available over MCP

Hosted MCP tools: `search_alterlab`, `read_alterlab_page` (public: no API key, no credits) (server `https://mcp.alterlab.io/mcp`).

Docs: https://alterlab.io/docs - API spec: https://alterlab.io/openapi.json
