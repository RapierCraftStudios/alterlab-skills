---
name: alterlab-monitor
description: Watch a web page for changes with AlterLab monitors and scheduled scrapes. Use when the user asks to be told when a price, page or listing changes, or to re-scrape a URL on a schedule.
---

# Monitor a page for changes with AlterLab

## When to use

- The user wants ongoing change detection rather than a one-off fetch.
- A scrape should repeat on a cron schedule.

Do not use when:

- A one-off read (use `alterlab-scrape`).

## Authentication

Set your API key in the `ALTERLAB_API_KEY` environment variable. Never paste the key into code, commands, or files you commit. Create a key at https://alterlab.io/dashboard.

```bash
export ALTERLAB_API_KEY="..."  # set in your shell, not in the repo
```

## Examples

### curl (monitor)

```bash
curl -X POST https://api.alterlab.io/v1/monitors \
  -H "X-API-Key: $ALTERLAB_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"name": "Pricing page", "url": "https://example.com/pricing", "check_interval": "0 */6 * * *"}'
```

### curl (scheduled scrape)

```bash
curl -X POST https://api.alterlab.io/v1/schedules \
  -H "X-API-Key: $ALTERLAB_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"name": "Daily scrape", "urls": ["https://example.com/pricing"], "cron": "0 6 * * *"}'
```

## Helper script

`scripts/monitor.py` calls the API with the Python standard library only (`python3 scripts/monitor.py --help`).

## Also available over MCP

Hosted MCP tools: none (REST only: `/v1/monitors`, `/v1/schedules`) (server `https://mcp.alterlab.io/mcp`).

Docs: https://alterlab.io/docs - API spec: https://alterlab.io/openapi.json
