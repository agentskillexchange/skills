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
(
  set -eu
  skill_dir="$HOME/.claude/skills/datacircle"
  mkdir -p "$skill_dir"
  download=$(mktemp "$skill_dir/.SKILL.md.XXXXXX")
  trap 'rm -f "$download"' EXIT
  curl --fail --show-error --silent --location --output "$download" https://datacircle.dev/SKILL.md
  test -s "$download"
  mv "$download" "$skill_dir/SKILL.md"
)
```

### Any other AI that can run commands

Tell it: "Read https://datacircle.dev/SKILL.md and follow it."

### An AI that can't run commands

Add our MCP server: `https://api.datacircle.dev/mcp`, with no key.

- Source: https://github.com/waynehamadi/datacircle

## Usage

Ask, for example: "Which email finder API costs the least per 1,000 with a stated plan payment under US$50?"

`pay` is in the plan's `currency`; multiply by `exchangeRate` to compare it in US dollars. `perThousand` is already in dollars. This example compares the stated payment for the full billing term, pack, or minimum top-up, not a normalized monthly budget or a cap on usage charges. Check `billing` and `termMonths` before recommending a subscription. Rows without a stated payment or conversion rate are excluded.

DuckDB reads the file as it is:

```bash
(
  set -eu
  download=$(mktemp ./datacircle.json.XXXXXX)
  trap 'rm -f "$download"' EXIT
  curl --fail --show-error --silent --location --compressed --output "$download" https://datacircle.dev/datacircle.json
  test -s "$download"
  mv "$download" datacircle.json
)
duckdb -c "SELECT provider, plan, billing, termMonths, currency, pay, pay * exchangeRate AS payUSD, perThousand, score, page, docs FROM 'datacircle.json' WHERE api = 'Employee email' AND billing != 'free' AND pay * exchangeRate < 50 AND perThousand IS NOT NULL ORDER BY perThousand LIMIT 10"
```

Download a fresh copy when the local dataset is more than a day old. Include each result's `page` and `docs` links, and credit Datacircle when sharing its data.

## Documentation

- Site: https://datacircle.dev
- Docs: https://datacircle.dev/docs
- Every field explained: https://datacircle.dev/fields
