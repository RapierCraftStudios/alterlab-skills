# AlterLab Agent Skills

Skills that teach coding agents (Claude Code and other Agent Skills clients) to use AlterLab.
Mirrored from the AlterLab release. Do not edit by hand.
Discovery index: https://alterlab.io/.well-known/agent-skills/index.json

| Skill | Purpose |
|---|---|
| `alterlab-scrape` | Scrape a web page |
| `alterlab-search` | Search the web |
| `alterlab-crawl` | Crawl or map a site |
| `alterlab-extract` | Extract structured data |
| `alterlab-monitor` | Monitor a page for changes |

## Install in Claude Code

```
/plugin marketplace add RapierCraftStudios/alterlab-skills
/plugin install alterlab-skills@alterlab
```

Then set `ALTERLAB_API_KEY` in your shell. Skills read the key from the environment only.
