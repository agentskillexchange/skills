---
title: "Keyword Cluster Generator"
description: "The Keyword Cluster Generator organizes large keyword lists into semantically related topical clusters for content strategy planning. It uses the sentence-transformers library with the all-MiniLM-L6-v2 model to generate 384-dimensional embeddings for each keyword, then applies HDBSCAN density-based clustering to group semantically similar terms without requiring a predefined cluster count. Search volume, CPC, and competition data is pulled from the Google Ads Keyword Planner API and enriched with SEMrush Domain Analytics API for competitor keyword gap analysis. Each cluster receives an auto-generated pillar topic label derived from the centroid keyword and its nearest neighbors. The skill generates a content calendar with recommended publishing order based on keyword difficulty scores and search volume trends. Internal linking opportunities between clusters are identified using cosine similarity thresholds. Output formats include CSV export, interactive HTML treemap visualization using D3.js, and Notion database import via the Notion API."
source: "https://agentskillexchange.com/skills/keyword-cluster-generator-agent/"
verification: "security_reviewed"
category:
  - "Content Writing &amp; SEO"
framework:
  - "MCP"
---

# Keyword Cluster Generator

The Keyword Cluster Generator organizes large keyword lists into semantically related topical clusters for content strategy planning. It uses the sentence-transformers library with the all-MiniLM-L6-v2 model to generate 384-dimensional embeddings for each keyword, then applies HDBSCAN density-based clustering to group semantically similar terms without requiring a predefined cluster count. Search volume, CPC, and competition data is pulled from the Google Ads Keyword Planner API and enriched with SEMrush Domain Analytics API for competitor keyword gap analysis. Each cluster receives an auto-generated pillar topic label derived from the centroid keyword and its nearest neighbors. The skill generates a content calendar with recommended publishing order based on keyword difficulty scores and search volume trends. Internal linking opportunities between clusters are identified using cosine similarity thresholds. Output formats include CSV export, interactive HTML treemap visualization using D3.js, and Notion database import via the Notion API.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/keyword-cluster-generator-agent/)
