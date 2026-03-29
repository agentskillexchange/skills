---
name: "Keyword Cluster Generator"
description: "Groups keywords into topical clusters using sentence-transformers all-MiniLM-L6-v2 embeddings with HDBSCAN clustering. Pulls search volume data from Google Ads API and SEMrush API."
category: "Content Writing & SEO"
framework: "MCP"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/keyword-cluster-generator-agent/"
tool_ecosystem:
  tool: notion
  github_stars: 5562
  npm_weekly_downloads: 1084242
  github_repo: makenotion/notion-sdk-js
  license: MIT
  maintained: true
---
# Keyword Cluster Generator

Groups keywords into topical clusters using sentence-transformers all-MiniLM-L6-v2 embeddings with HDBSCAN clustering. Pulls search volume data from Google Ads API and SEMrush API.

## Overview

The Keyword Cluster Generator organizes large keyword lists into semantically related topical clusters for content strategy planning. It uses the sentence-transformers library with the all-MiniLM-L6-v2 model to generate 384-dimensional embeddings for each keyword, then applies HDBSCAN density-based clustering to group semantically similar terms without requiring a predefined cluster count. Search volume, CPC, and competition data is pulled from the Google Ads Keyword Planner API and enriched with SEMrush Domain Analytics API for competitor keyword gap analysis. Each cluster receives an auto-generated pillar topic label derived from the centroid keyword and its nearest neighbors. The skill generates a content calendar with recommended publishing order based on keyword difficulty scores and search volume trends. Internal linking opportunities between clusters are identified using cosine similarity thresholds. Output formats include CSV export, interactive HTML treemap visualization using D3.js, and Notion database import via the Notion API.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill keyword-cluster-generator-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill keyword-cluster-generator-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill keyword-cluster-generator-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill keyword-cluster-generator-agent -a codex
```

### OpenClaw

```bash
clawhub install keyword-cluster-generator-agent
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/keyword-cluster-generator-agent/)
