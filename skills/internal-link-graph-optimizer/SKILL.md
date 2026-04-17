---
title: "Internal Link Graph Optimizer"
description: "Internal Link Graph Optimizer builds a complete model of a site’s internal linking architecture to find gaps, orphan pages, and suboptimal link equity distribution. It ingests crawl data from Screaming Frog or Sitebulb exports, constructing a directed graph using NetworkX where nodes are URLs and edges are internal links with anchor text attributes.\nPageRank computation via networkx.pagerank() reveals which pages receive the most internal authority and which high-value pages are under-linked. The tool identifies orphan pages with zero internal incoming links, deep pages requiring more than four clicks from the homepage, and hub pages that could distribute more equity to target content.\nLink recommendations use BM25 relevance scoring from the rank_bm25 Python library to find contextually appropriate anchor insertion points. For each under-linked target page, the optimizer scans existing content inventory for paragraphs where a natural contextual link would fit, ranking candidates by topical relevance and existing link density. Output includes a prioritized action list with source URL, paragraph location, suggested anchor text, and target URL, formatted as a CSV for editorial teams or as WordPress REST API patch commands for automated insertion."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/internal-link-graph-optimizer/"
framework:
  - "Cursor"
---

# Internal Link Graph Optimizer

Internal Link Graph Optimizer builds a complete model of a site’s internal linking architecture to find gaps, orphan pages, and suboptimal link equity distribution. It ingests crawl data from Screaming Frog or Sitebulb exports, constructing a directed graph using NetworkX where nodes are URLs and edges are internal links with anchor text attributes.
PageRank computation via networkx.pagerank() reveals which pages receive the most internal authority and which high-value pages are under-linked. The tool identifies orphan pages with zero internal incoming links, deep pages requiring more than four clicks from the homepage, and hub pages that could distribute more equity to target content.
Link recommendations use BM25 relevance scoring from the rank_bm25 Python library to find contextually appropriate anchor insertion points. For each under-linked target page, the optimizer scans existing content inventory for paragraphs where a natural contextual link would fit, ranking candidates by topical relevance and existing link density. Output includes a prioritized action list with source URL, paragraph location, suggested anchor text, and target URL, formatted as a CSV for editorial teams or as WordPress REST API patch commands for automated insertion.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/internal-link-graph-optimizer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/internal-link-graph-optimizer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/internal-link-graph-optimizer/)
