---
title: "SEO Meta Tag Optimizer"
description: "The SEO Meta Tag Optimizer analyzes page content and generates search-engine-optimized metadata using the Google Cloud Natural Language API for entity extraction and salience scoring. It identifies primary and secondary entities in content, then crafts title tags under 60 characters and meta descriptions under 155 characters that maximize click-through rate. The skill uses the DataForSEO SERP API to analyze competitor meta tags for target keywords and identify content gaps. Open Graph and Twitter Card markup is generated automatically with proper og:type, og:image dimensions, and twitter:card variants. For WordPress sites, it integrates directly with the Yoast SEO REST API to push optimized metadata without manual editing. The skill includes A/B testing support by generating multiple title/description variants scored by predicted CTR using a trained logistic regression model. Schema.org JSON-LD markup is generated for Article, Product, FAQ, and HowTo content types."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/seo-meta-tag-optimizer-agent/"
framework:
  - "ChatGPT Agents"
---

# SEO Meta Tag Optimizer

The SEO Meta Tag Optimizer analyzes page content and generates search-engine-optimized metadata using the Google Cloud Natural Language API for entity extraction and salience scoring. It identifies primary and secondary entities in content, then crafts title tags under 60 characters and meta descriptions under 155 characters that maximize click-through rate. The skill uses the DataForSEO SERP API to analyze competitor meta tags for target keywords and identify content gaps. Open Graph and Twitter Card markup is generated automatically with proper og:type, og:image dimensions, and twitter:card variants. For WordPress sites, it integrates directly with the Yoast SEO REST API to push optimized metadata without manual editing. The skill includes A/B testing support by generating multiple title/description variants scored by predicted CTR using a trained logistic regression model. Schema.org JSON-LD markup is generated for Article, Product, FAQ, and HowTo content types.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/seo-meta-tag-optimizer-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/seo-meta-tag-optimizer-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/seo-meta-tag-optimizer-agent/)
