---
name: "Playwright Trace Harvester for Infinite Scroll APIs"
description: "Captures Playwright trace.zip sessions, Chrome DevTools Protocol network events, and HAR files from infinite-scroll sites so agents can recover the hidden JSON and GraphQL endpoints behind the UI. Useful for pagination reverse engineering, cursor discovery, and turning browser behavior into repeatable API requests."
category: "Research & Scraping"
framework: "OpenClaw"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/playwright-trace-harvester-infinite-scroll-apis-20260324/"
---

# Playwright Trace Harvester for Infinite Scroll APIs

Captures Playwright trace.zip sessions, Chrome DevTools Protocol network events, and HAR files from infinite-scroll sites so agents can recover the hidden JSON and GraphQL endpoints behind the UI. Useful for pagination reverse engineering, cursor discovery, and turning browser behavior into repeatable API requests.

## Overview

This skill uses **Playwright**, the Chrome DevTools Protocol (CDP), and HAR/trace artifacts to map how an infinite-scroll interface actually talks to its backend. Instead of scraping raw HTML forever, it opens the target page, scrolls in controlled batches, records `trace.zip`, inspects XHR and `fetch` traffic, and extracts request URLs, query parameters, GraphQL operation names, cursor tokens, headers, and response shapes. It works well on React, Next.js, and headless commerce sites where the real data arrives through JSON APIs rather than server-rendered markup. The skill produces a compact endpoint inventory, sample replay requests, pagination notes, and a normalized field map that can be reused by Python requests, `curl`, Node SDK scripts, or a later browser automation pass.

Operationally, the workflow starts with a browser session, captures CDP `Network.requestWillBeSent` and `Network.responseReceived` events, then correlates those events with DOM changes and scroll milestones. If the site uses GraphQL, persisted queries, or signed URLs, the skill documents those moving parts and flags anything that requires cookies, CSRF tokens, or short-lived auth. It can optionally emit a small replay harness in JavaScript or Python, plus a CSV or JSONL export schema for downstream ETL. This is especially useful when pairing Playwright with tools like Scrapy, Airbyte, BigQuery, Snowflake, or a webhook-driven ingestion pipeline. The output is a research-ready packet: endpoint list, pagination strategy, replay code, and extraction notes that reduce fragile browser scraping into a more stable API workflow.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill playwright-trace-harvester-infinite-scroll-apis-20260324
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill playwright-trace-harvester-infinite-scroll-apis-20260324 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill playwright-trace-harvester-infinite-scroll-apis-20260324 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill playwright-trace-harvester-infinite-scroll-apis-20260324 -a codex
```

### OpenClaw

```bash
clawhub install playwright-trace-harvester-infinite-scroll-apis-20260324
```

## Source

- Marketplace: https://agentskillexchange.com/skills/playwright-trace-harvester-infinite-scroll-apis-20260324/
