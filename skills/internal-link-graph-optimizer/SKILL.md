---
name: "Internal Link Graph Optimizer"
description: "Analyzes internal linking structure by crawling sitemaps with Screaming Frog or Sitebulb, computing PageRank distribution via NetworkX graph algorithms, and identifying orphan pages. Recommends contextual link insertions using BM25 text matching against existing content inventory."
category: "Content Writing & SEO"
framework: "Cursor"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/internal-link-graph-optimizer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "wordpress"  # from ase_tool_match
  github_stars: 20973  # from ase_github_stars (integer, not string)
  github_repo: "WordPress/WordPress"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Internal Link Graph Optimizer

Analyzes internal linking structure by crawling sitemaps with Screaming Frog or Sitebulb, computing PageRank distribution via NetworkX graph algorithms, and identifying orphan pages. Recommends contextual link insertions using BM25 text matching against existing content inventory.

## Overview

Internal Link Graph Optimizer builds a complete model of a site’s internal linking architecture to find gaps, orphan pages, and suboptimal link equity distribution. It ingests crawl data from Screaming Frog or Sitebulb exports, constructing a directed graph using NetworkX where nodes are URLs and edges are internal links with anchor text attributes.

PageRank computation via networkx.pagerank() reveals which pages receive the most internal authority and which high-value pages are under-linked. The tool identifies orphan pages with zero internal incoming links, deep pages requiring more than four clicks from the homepage, and hub pages that could distribute more equity to target content.

Link recommendations use BM25 relevance scoring from the rank_bm25 Python library to find contextually appropriate anchor insertion points. For each under-linked target page, the optimizer scans existing content inventory for paragraphs where a natural contextual link would fit, ranking candidates by topical relevance and existing link density. Output includes a prioritized action list with source URL, paragraph location, suggested anchor text, and target URL, formatted as a CSV for editorial teams or as WordPress REST API patch commands for automated insertion.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill internal-link-graph-optimizer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill internal-link-graph-optimizer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill internal-link-graph-optimizer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill internal-link-graph-optimizer -a codex
```

### OpenClaw

```bash
clawhub install internal-link-graph-optimizer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/internal-link-graph-optimizer/
