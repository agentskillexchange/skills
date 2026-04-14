---
title: "Keyword Cluster Generator"
description: "Groups keywords into topical clusters using sentence-transformers all-MiniLM-L6-v2 embeddings with HDBSCAN clustering. Pulls search volume data from Google Ads API and SEMrush API."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/keyword-cluster-generator-agent/"
category:
  - "Content Writing &amp; SEO"
framework:
  - "MCP"
---

# Keyword Cluster Generator

The Keyword Cluster Generator organizes large keyword lists into semantically related topical clusters for content strategy planning. It uses the sentence-transformers library with the all-MiniLM-L6-v2 model to generate 384-dimensional embeddings for each keyword, then applies HDBSCAN density-based clustering to group semantically similar terms without requiring a predefined cluster count. Search volume, CPC, and competition data is pulled from the Google Ads Keyword Planner API and enriched with SEMrush Domain Analytics API for competitor keyword gap analysis. Each cluster receives an auto-generated pillar topic label derived from the centroid keyword and its nearest neighbors. The skill generates a content calendar with recommended publishing order based on keyword difficulty scores and search volume trends. Internal linking opportunities between clusters are identified using cosine similarity thresholds. Output formats include CSV export, interactive HTML treemap visualization using D3.js, and Notion database import via the Notion API.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/keyword-cluster-generator-agent/)
