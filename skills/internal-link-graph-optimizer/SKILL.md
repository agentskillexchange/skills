---
title: "Internal Link Graph Optimizer"
description: "Analyzes internal linking structure by crawling sitemaps with Screaming Frog or Sitebulb, computing PageRank distribution via NetworkX graph algorithms, and identifying orphan pages. Recommends contextual link insertions using BM25 text matching against existing content inventory."
slug: "internal-link-graph-optimizer"
category:
  - "Content Writing &amp; SEO"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/internal-link-graph-optimizer/"
---

# Internal Link Graph Optimizer

Analyzes internal linking structure by crawling sitemaps with Screaming Frog or Sitebulb, computing PageRank distribution via NetworkX graph algorithms, and identifying orphan pages. Recommends contextual link insertions using BM25 text matching against existing content inventory.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install internal-link-graph-optimizer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Internal Link Graph Optimizer builds a complete model of a site’s internal linking architecture to find gaps, orphan pages, and suboptimal link equity distribution. It ingests crawl data from Screaming Frog or Sitebulb exports, constructing a directed graph using NetworkX where nodes are URLs and edges are internal links with anchor text attributes.
PageRank computation via networkx.pagerank() reveals which pages receive the most internal authority and which high-value pages are under-linked. The tool identifies orphan pages with zero internal incoming links, deep pages requiring more than four clicks from the homepage, and hub pages that could distribute more equity to target content.
Link recommendations use BM25 relevance scoring from the rank_bm25 Python library to find contextually appropriate anchor insertion points. For each under-linked target page, the optimizer scans existing content inventory for paragraphs where a natural contextual link would fit, ranking candidates by topical relevance and existing link density. Output includes a prioritized action list with source URL, paragraph location, suggested anchor text, and target URL, formatted as a CSV for editorial teams or as WordPress REST API patch commands for automated insertion.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/internal-link-graph-optimizer/)
