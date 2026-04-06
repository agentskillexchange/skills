---
name: "Diffbot Knowledge Graph Extractor"
description: "Extracts structured entities from web pages using the Diffbot Extraction API and Knowledge Graph. Supports article, product, and discussion extraction with automatic entity linking via DQL queries."
category: "Research & Scraping"
framework: "Claude Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/diffbot-knowledge-graph-extractor/"
---
# Diffbot Knowledge Graph Extractor

Extracts structured entities from web pages using the Diffbot Extraction API and Knowledge Graph. Supports article, product, and discussion extraction with automatic entity linking via DQL queries.

This skill extracts structured data from web pages using Diffbot’s suite of extraction APIs. It leverages the Automatic Extraction API for content type detection and the specialized Article, Product, Discussion, and Image APIs for domain-specific extraction with high accuracy.



The skill integrates with the Diffbot Knowledge Graph (DKG) for entity resolution and enrichment. Extracted entities are linked to the Knowledge Graph using DQL (Diffbot Query Language) queries, enabling cross-referencing of organizations, people, products, and locations with enriched metadata.



Bulk processing is handled through the Diffbot Bulk API and Crawlbot for site-wide extraction jobs. The skill manages crawl budgets, URL pattern filtering via regex rules, and incremental crawl schedules. Extracted data is normalized into a unified schema with configurable field mapping.



Output formats include JSON-LD with Schema.org markup, CSV for tabular data, and direct integration with downstream databases via webhook notifications on extraction completion.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill diffbot-knowledge-graph-extractor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill diffbot-knowledge-graph-extractor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill diffbot-knowledge-graph-extractor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill diffbot-knowledge-graph-extractor -a codex
```

### OpenClaw

```bash
clawhub install diffbot-knowledge-graph-extractor
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diffbot-knowledge-graph-extractor/)
