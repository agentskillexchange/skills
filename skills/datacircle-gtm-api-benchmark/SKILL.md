---
name: "Datacircle GTM API Benchmark"
slug: "datacircle-gtm-api-benchmark"
description: "Compare GTM APIs using Datacircle rankings. Call the open API at api.datacircle.dev/v1, with no key, to list covered APIs, filter plans by API, search provider or plan names, and sort by price."
verification: "listed"
source: "https://api.datacircle.dev/v1/openapi.json"
author: "Datacircle"
category: "Library & API Reference"
framework: "Custom Agents"
---

# Datacircle GTM API Benchmark

Compare GTM APIs using the benchmarks published by Datacircle at https://datacircle.dev. Read the covered APIs and their results over the open API at https://api.datacircle.dev/v1. The API is free and needs no key. It is read only and allows 60 calls a minute from one address.

Use it when a task asks which API to pick for LinkedIn profiles, email finding, company search, web search or any other GTM data call, or what a plan costs per 1,000 results. Use available plan prices, scores, rate limits and provider documentation links. Treat missing or null fields as unknown, not zero or unlimited. Attribute rankings to Datacircle and check the provider's current pricing and docs before recommending a purchase.

## Calls

- `GET /apis` lists every API on the sheet.
- `GET /apis/{slug}/best` gives who is best for one API.
- `GET /plans` filters plans with `api`, searches provider or plan names with `query`, and sorts with `sort=score|provider|price`. Use `limit` (1–50, default 10) and `offset` to page through results; `total` counts all matching plans. Price sorting uses cost per 1,000; the spec does not define a price-range filter.
- `GET /providers/{slug}` gives one provider's ranks.

The full spec is at https://api.datacircle.dev/v1/openapi.json. Read the calls from the spec, as it is the source of truth.

```bash
curl -s https://api.datacircle.dev/v1/apis
curl -s https://api.datacircle.dev/v1/openapi.json
curl -s 'https://api.datacircle.dev/v1/plans?api=linkedin-profile&query=Bridgly&sort=price&limit=1'
```

## Installation

### Direct repo/manual install

```bash
git clone https://github.com/agentskillexchange/skills.git
mkdir -p ~/.agent-skills
cp -R skills/skills/datacircle-gtm-api-benchmark ~/.agent-skills/datacircle-gtm-api-benchmark
```

## Documentation

- https://api.datacircle.dev/v1/openapi.json
- https://datacircle.dev/SKILL.md
- https://datacircle.dev/llms.txt

## Source

- https://datacircle.dev
