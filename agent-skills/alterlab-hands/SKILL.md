---
name: alterlab-hands
description: Use the user's own logged-in accounts through AlterLab Hands: connect a site, read their own data, and act with their approval. Use when the data is behind the user's login (saved posts, analytics, applications) and a public scrape cannot reach it.
---

# Read and act on the user's own logged-in sites with AlterLab

## When to use

- The page needs the user's own login (Reddit saved posts, YouTube Studio analytics).
- The user wants a browser task run on a site they connected, such as submitting a job application.

Do not use when:

- The page is public (use `alterlab-scrape`).
- The user has not agreed to connect the site: never ask for or handle their password.

## Authentication

Set your API key in the `ALTERLAB_API_KEY` environment variable. Never paste the key into code, commands, or files you commit. Create a key at https://alterlab.io/dashboard.

No key yet? `POST https://api.alterlab.io/api/v1/agent/trial` returns a free trial key with no signup (50 requests, 24 hours). Every response from a trial key then carries a claim link in the `X-AlterLab-Claim-URL` header, and the trial errors repeat it. Give that link to your human: they sign in or sign up, and the same key becomes theirs and keeps working with no reconfiguration. A free account comes with up to 5,000 free requests.

With a trial key you can already show your human a verified result: `POST /api/v1/hands/preview` with `{"goal": "...", "public_url": "..."}` (public pages only, read-only, GET requests only). Each returned fact lists two or more sources, and `next_action` is an `install_hands` action stating what installing would unlock. A cap trip returns a `busy` event with `Retry-After`.

```bash
export ALTERLAB_API_KEY="..."  # set in your shell, not in the repo
```

## Examples

### Connect a site

Call `alterlab_connect` with `site` (for example `reddit.com`) and `reason`. Show the returned link to the user, who signs in themselves. Poll `alterlab_connect` with `connect_id` until it reports connected. `alterlab_sessions` lists connected sites and their health, and revokes one.

### Reddit saved posts (read)

`alterlab_task_start` with `start_url` `https://www.reddit.com/user/me/saved`, the connected `session_id` and `mode` `read`. Then `alterlab_task_observe` for the redacted page and `alterlab_task_act` to scroll. `alterlab_task_status` shows progress.

### Learn what a page asks for

`alterlab_task_schema` returns the page's fields (label, kind, required, options, limits), submit/next/back actions, slots, tables and cart lines, and a `schema_hash` to detect page changes. Use it before filling a form.

### YouTube analytics (read)

Start a read task at `https://studio.youtube.com` with the connected session, observe the analytics page, and summarize the numbers for the user.

### Job application (with approval)

Start a task on the employer's site and fill the form with `alterlab_task_act`. Actions that change something on the site return a pending request instead of running. Show its elicitation to the user, pass their reply to `alterlab_task_answer`, then retry the same actions unchanged. Never submit without that approval.

## Also available over MCP

Hosted MCP tools: `alterlab_connect`, `alterlab_sessions`, `alterlab_task_start`, `alterlab_task_act`, `alterlab_task_observe`, `alterlab_task_schema`, `alterlab_task_answer`, `alterlab_task_status` (scopes `hands:read` / `hands:write`; REST: `/api/v1/hands`) (server `https://mcp.alterlab.io/mcp`).

Docs: https://alterlab.io/docs - API spec: https://alterlab.io/openapi.json
