---
title: "Diffbot Knowledge Graph Extractor"
description: "This skill extracts structured data from web pages using Diffbot’s suite of extraction APIs. It leverages the Automatic Extraction API for content type detection and the specialized Article, Product, Discussion, and Image APIs for domain-specific extraction with high accuracy.\nThe skill integrates with the Diffbot Knowledge Graph (DKG) for entity resolution and enrichment. Extracted entities are linked to the Knowledge Graph using DQL (Diffbot Query Language) queries, enabling cross-referencing of organizations, people, products, and locations with enriched metadata.\nBulk processing is handled through the Diffbot Bulk API and Crawlbot for site-wide extraction jobs. The skill manages crawl budgets, URL pattern filtering via regex rules, and incremental crawl schedules. Extracted data is normalized into a unified schema with configurable field mapping.\nOutput formats include JSON-LD with Schema.org markup, CSV for tabular data, and direct integration with downstream databases via webhook notifications on extraction completion."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/diffbot-knowledge-graph-extractor/"
framework:
  - "Claude Agents"
---

# Diffbot Knowledge Graph Extractor

This skill extracts structured data from web pages using Diffbot’s suite of extraction APIs. It leverages the Automatic Extraction API for content type detection and the specialized Article, Product, Discussion, and Image APIs for domain-specific extraction with high accuracy.
The skill integrates with the Diffbot Knowledge Graph (DKG) for entity resolution and enrichment. Extracted entities are linked to the Knowledge Graph using DQL (Diffbot Query Language) queries, enabling cross-referencing of organizations, people, products, and locations with enriched metadata.
Bulk processing is handled through the Diffbot Bulk API and Crawlbot for site-wide extraction jobs. The skill manages crawl budgets, URL pattern filtering via regex rules, and incremental crawl schedules. Extracted data is normalized into a unified schema with configurable field mapping.
Output formats include JSON-LD with Schema.org markup, CSV for tabular data, and direct integration with downstream databases via webhook notifications on extraction completion.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/diffbot-knowledge-graph-extractor
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/diffbot-knowledge-graph-extractor` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diffbot-knowledge-graph-extractor/)
