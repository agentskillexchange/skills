---
name: "Datacircle GTM API Benchmark"
slug: "datacircle-gtm-api-benchmark"
description: "Find the best GTM APIs. Calls the open Datacircle API at api.datacircle.dev/v1, with no key, to list every GTM API, see which provider is best for each and search every plan by API, provider or price."
verification: "listed"
source: "https://api.datacircle.dev/v1/openapi.json"
author: "Datacircle"
category: "Library & API Reference"
framework: "Custom Agents"
---

# Datacircle GTM API Benchmark

Find the best GTM APIs. Datacircle benchmarks all the GTM APIs and puts the results on its website, https://datacircle.dev. This skill lets an agent read those results over the open API at https://api.datacircle.dev/v1. The API is free and needs no key. It is read only and allows 60 calls a minute from one address.

Use it when a task asks which API to pick for LinkedIn profiles, email finding, company search, web search or any other GTM data call, or what a plan costs per 1,000 results. Each plan comes with its price, its score, its rate limits and a link to the provider's docs.

## Calls

- `GET /apis` lists every API on the sheet.
- `GET /apis/{slug}/best` gives who is best for one API.
- `GET /plans` lists every plan, filtered by API, provider or price.
- `GET /providers/{slug}` gives one provider's ranks.

The full spec is at https://api.datacircle.dev/v1/openapi.json. Read the calls from the spec, as it is the source of truth.

```bash
curl -s https://api.datacircle.dev/v1/apis
curl -s https://api.datacircle.dev/v1/openapi.json
```

## Installation

### Direct repo/manual install

```bash
git clone https://github.com/agentskillexchange/skills.git
cp -R skills/skills/datacircle-gtm-api-benchmark ~/.agent-skills/datacircle-gtm-api-benchmark
```

## Documentation

- https://api.datacircle.dev/v1/openapi.json
- https://datacircle.dev/SKILL.md
- https://datacircle.dev/llms.txt

## Source

- https://datacircle.dev
