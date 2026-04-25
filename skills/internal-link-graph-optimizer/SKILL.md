---
title: "Internal Link Graph Optimizer"
description: "Analyzes internal linking structure by crawling sitemaps with Screaming Frog or Sitebulb, computing PageRank distribution via NetworkX graph algorithms, and identifying orphan pages. Recommends contextual link insertions using BM25 text matching against existing content inventory."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/internal-link-graph-optimizer/"
category:
  - "Content Writing & SEO"
framework:
  - "Cursor"
---

# Internal Link Graph Optimizer

Internal Link Graph Optimizer builds a complete model of a site’s internal linking architecture to find gaps, orphan pages, and suboptimal link equity distribution. It ingests crawl data from Screaming Frog or Sitebulb exports, constructing a directed graph using NetworkX where nodes are URLs and edges are internal links with anchor text attributes. PageRank computation via networkx.pagerank() reveals which pages receive the most internal authority and which high-value pages are under-linked. The tool identifies orphan pages with zero internal incoming links, deep pages requiring more than four clicks from the homepage, and hub pages that could distribute more equity to target content. Link recommendations use BM25 relevance scoring from the rank_bm25 Python library to find contextually appropriate anchor insertion points. For each under-linked target page, the optimizer scans existing content inventory for paragraphs where a natural contextual link would fit, ranking candidates by topical relevance and existing link density. Output includes a prioritized action list with source URL, paragraph location, suggested anchor text, and target URL, formatted as a CSV for editorial teams or as WordPress REST API patch commands for automated insertion.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/internal-link-graph-optimizer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/internal-link-graph-optimizer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/internal-link-graph-optimizer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/internal-link-graph-optimizer/)
