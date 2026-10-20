---
name: "Datacircle"
slug: "datacircle"
description: "Every GTM API plan on datacircle.dev, as one file you download and query. LinkedIn profiles, people and company search, find and validate email and phone, company data, jobs and posts, each plan with its price per 1,000, score, rate limits, the fields it returns and its docs. Use it to compare or price a GTM data API."
github_stars: 0
verification: "listed"
source: "https://github.com/waynehamadi/datacircle"
author: "datacircle"
category: "Library & API Reference"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "waynehamadi/datacircle"
  github_stars: 0
---

# Datacircle

Datacircle lists all the GTM APIs. This skill gives you every plan on datacircle.dev as one file.

Every GTM API we find, one row for each plan of each call: what it costs per 1,000, what it charges when it finds nothing, its rate limits, its speed and the fields it returns.

SKILL.md tells your AI:

- How to download the file, and when to download it again.
- The data model: every key with its type and meaning, and every API with the sheet it is on.
- How to query it, with DuckDB, jq or Python.

Your AI answers from the file on your computer and links each plan's page and docs. The download needs no key and no account. The file is under CC BY 4.0: use it for anything, and credit Datacircle.

## Installation

### Claude Code

```bash
mkdir -p ~/.claude/skills/datacircle && curl -sL -o ~/.claude/skills/datacircle/SKILL.md https://datacircle.dev/SKILL.md
```

### Any other AI that can run commands

Tell it: "Read https://datacircle.dev/SKILL.md and follow it."

### An AI that can't run commands

Add our MCP server: `https://api.datacircle.dev/mcp`, with no key.

- Source: https://github.com/waynehamadi/datacircle

## Usage

Ask, for example: "Which email finder API costs the least per 1,000 on a plan under $50?"

DuckDB reads the file as it is:

```bash
curl -sL --compressed -o datacircle.json https://datacircle.dev/datacircle.json
duckdb -c "SELECT provider, plan, pay, perThousand, score FROM 'datacircle.json' WHERE api = 'Employee email' AND billing != 'free' AND pay <= 50 AND perThousand IS NOT NULL ORDER BY perThousand LIMIT 10"
```

## Documentation

- Site: https://datacircle.dev
- Docs: https://datacircle.dev/docs
- Every field explained: https://datacircle.dev/fields
