---
title: "Keyword Cluster Generator"
description: "Groups keywords into topical clusters using sentence-transformers all-MiniLM-L6-v2 embeddings with HDBSCAN clustering. Pulls search volume data from Google Ads API and SEMrush API."
slug: "keyword-cluster-generator-agent"
category:
  - "Content Writing &amp; SEO"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/keyword-cluster-generator-agent/"
---

# Keyword Cluster Generator

Groups keywords into topical clusters using sentence-transformers all-MiniLM-L6-v2 embeddings with HDBSCAN clustering. Pulls search volume data from Google Ads API and SEMrush API.

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
clawhub install keyword-cluster-generator-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Keyword Cluster Generator organizes large keyword lists into semantically related topical clusters for content strategy planning. It uses the sentence-transformers library with the all-MiniLM-L6-v2 model to generate 384-dimensional embeddings for each keyword, then applies HDBSCAN density-based clustering to group semantically similar terms without requiring a predefined cluster count. Search volume, CPC, and competition data is pulled from the Google Ads Keyword Planner API and enriched with SEMrush Domain Analytics API for competitor keyword gap analysis. Each cluster receives an auto-generated pillar topic label derived from the centroid keyword and its nearest neighbors. The skill generates a content calendar with recommended publishing order based on keyword difficulty scores and search volume trends. Internal linking opportunities between clusters are identified using cosine similarity thresholds. Output formats include CSV export, interactive HTML treemap visualization using D3.js, and Notion database import via the Notion API.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/keyword-cluster-generator-agent/)
