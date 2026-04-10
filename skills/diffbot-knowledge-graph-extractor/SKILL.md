---
name: Diffbot Knowledge Graph Extractor
description: Extracts structured entities from web pages using the Diffbot Extraction
  API and Knowledge Graph. Supports article, product, and discussion extraction with
  automatic entity linking via DQL queries.
verification: security_reviewed
source: https://agentskillexchange.com/skills/diffbot-knowledge-graph-extractor/
category:
- Research &amp; Scraping
framework:
- Claude Agents
---
# Diffbot Knowledge Graph Extractor

This skill extracts structured data from web pages using Diffbot's suite of extraction APIs. It leverages the Automatic Extraction API for content type detection and the specialized Article, Product, Discussion, and Image APIs for domain-specific extraction with high accuracy.
The skill integrates with the Diffbot Knowledge Graph (DKG) for entity resolution and enrichment. Extracted entities are linked to the Knowledge Graph using DQL (Diffbot Query Language) queries, enabling cross-referencing of organizations, people, products, and locations with enriched metadata.
Bulk processing is handled through the Diffbot Bulk API and Crawlbot for site-wide extraction jobs. The skill manages crawl budgets, URL pattern filtering via regex rules, and incremental crawl schedules. Extracted data is normalized into a unified schema with configurable field mapping.
Output formats include JSON-LD with Schema.org markup, CSV for tabular data, and direct integration with downstream databases via webhook notifications on extraction completion.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diffbot-knowledge-graph-extractor/)
