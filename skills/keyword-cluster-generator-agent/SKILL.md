---
title: "Keyword Cluster Generator"
description: "Groups keywords into topical clusters using sentence-transformers all-MiniLM-L6-v2 embeddings with HDBSCAN clustering. Pulls search volume data from Google Ads API and SEMrush API."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/keyword-cluster-generator-agent/"
category:
  - "Content Writing & SEO"
framework:
  - "MCP"
---

# Keyword Cluster Generator

The Keyword Cluster Generator organizes large keyword lists into semantically related topical clusters for content strategy planning. It uses the sentence-transformers library with the all-MiniLM-L6-v2 model to generate 384-dimensional embeddings for each keyword, then applies HDBSCAN density-based clustering to group semantically similar terms without requiring a predefined cluster count. Search volume, CPC, and competition data is pulled from the Google Ads Keyword Planner API and enriched with SEMrush Domain Analytics API for competitor keyword gap analysis. Each cluster receives an auto-generated pillar topic label derived from the centroid keyword and its nearest neighbors. The skill generates a content calendar with recommended publishing order based on keyword difficulty scores and search volume trends. Internal linking opportunities between clusters are identified using cosine similarity thresholds. Output formats include CSV export, interactive HTML treemap visualization using D3.js, and Notion database import via the Notion API.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/keyword-cluster-generator-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/keyword-cluster-generator-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/keyword-cluster-generator-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/keyword-cluster-generator-agent/)
