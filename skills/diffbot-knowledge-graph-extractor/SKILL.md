---
title: "Diffbot Knowledge Graph Extractor"
description: "Extracts structured entities from web pages using the Diffbot Extraction API and Knowledge Graph. Supports article, product, and discussion extraction with automatic entity linking via DQL queries."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/diffbot-knowledge-graph-extractor/"
category:
  - "Research &amp; Scraping"
framework:
  - "Claude Agents"
---

# Diffbot Knowledge Graph Extractor

This skill extracts structured data from web pages using Diffbot’s suite of extraction APIs. It leverages the Automatic Extraction API for content type detection and the specialized Article, Product, Discussion, and Image APIs for domain-specific extraction with high accuracy.

The skill integrates with the Diffbot Knowledge Graph (DKG) for entity resolution and enrichment. Extracted entities are linked to the Knowledge Graph using DQL (Diffbot Query Language) queries, enabling cross-referencing of organizations, people, products, and locations with enriched metadata.

Bulk processing is handled through the Diffbot Bulk API and Crawlbot for site-wide extraction jobs. The skill manages crawl budgets, URL pattern filtering via regex rules, and incremental crawl schedules. Extracted data is normalized into a unified schema with configurable field mapping.

Output formats include JSON-LD with Schema.org markup, CSV for tabular data, and direct integration with downstream databases via webhook notifications on extraction completion.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diffbot-knowledge-graph-extractor/)
