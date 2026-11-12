---
name: alterlab-store
description: Find and run ready-made data products (site scrapers, pipelines, use-case APIs) from the AlterLab Store, billed per valid result. Use when the user wants data from a popular site or use case that a listing already covers, or wants to publish their own listing. Do not use it for an arbitrary URL (use alterlab-scrape).
---

# Run a ready-made data product from the Store with AlterLab

## When to use

- A Store listing already covers the site or use case: search the catalog first with `alterlab_store_search` (free, keyless).
- `alterlab_store_get` shows a listing's price, success rate and `input_schema`.
- Quote before running: `alterlab_store_quote` returns the maximum cost; `alterlab_store_run` reserves it, bills only valid results and refunds the rest.
- Publish your own listing with `alterlab_listing_draft_create`, `alterlab_listing_draft_test` and `alterlab_listing_publish`.

Do not use when:

- No listing fits the target (use `alterlab-scrape` or `alterlab-extract`).

## Authentication

Set your API key in the `ALTERLAB_API_KEY` environment variable. Never paste the key into code, commands, or files you commit. Create a key at https://alterlab.io/dashboard.

No key yet? `POST https://api.alterlab.io/api/v1/agent/trial` returns a free trial key with no signup (50 requests, 24 hours). Every response from a trial key then carries a claim link in the `X-AlterLab-Claim-URL` header, and the trial errors repeat it. Give that link to your human: they sign in or sign up, and the same key becomes theirs and keeps working with no reconfiguration. A free account comes with up to 5,000 free requests.

```bash
export ALTERLAB_API_KEY="..."  # set in your shell, not in the repo
```

## Examples

### curl (quote a listing)

```bash
curl -X POST https://api.alterlab.io/api/v1/listings/example-listing/quote \
  -H "X-API-Key: $ALTERLAB_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"max_results": 100}'
```

### curl (run a listing)

```bash
curl -X POST https://api.alterlab.io/api/v1/listings/example-listing/run \
  -H "X-API-Key: $ALTERLAB_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"input": {"query": "coffee shops in Berlin"}, "max_results": 100}'
```

## Also available over MCP

Hosted MCP tools: `alterlab_store_search`, `alterlab_store_get`, `alterlab_store_quote`, `alterlab_store_run`, `alterlab_listing_draft_create`, `alterlab_listing_draft_test`, `alterlab_listing_publish` (REST: `/api/v1/listings`) (server `https://mcp.alterlab.io/mcp`).

Docs: https://alterlab.io/docs - API spec: https://alterlab.io/openapi.json
