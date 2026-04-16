---
title: "SEO Meta Tag Optimizer"
description: "Generates optimized title tags, meta descriptions, and Open Graph markup using Google NLP API for entity salience scoring. Integrates with Yoast SEO REST API for WordPress deployments."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/seo-meta-tag-optimizer-agent/"
category:
  - "Content Writing &amp; SEO"
framework:
  - "ChatGPT Agents"
---

# SEO Meta Tag Optimizer

The SEO Meta Tag Optimizer analyzes page content and generates search-engine-optimized metadata using the Google Cloud Natural Language API for entity extraction and salience scoring. It identifies primary and secondary entities in content, then crafts title tags under 60 characters and meta descriptions under 155 characters that maximize click-through rate. The skill uses the DataForSEO SERP API to analyze competitor meta tags for target keywords and identify content gaps. Open Graph and Twitter Card markup is generated automatically with proper og:type, og:image dimensions, and twitter:card variants. For WordPress sites, it integrates directly with the Yoast SEO REST API to push optimized metadata without manual editing. The skill includes A/B testing support by generating multiple title/description variants scored by predicted CTR using a trained logistic regression model. Schema.org JSON-LD markup is generated for Article, Product, FAQ, and HowTo content types.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/seo-meta-tag-optimizer-agent/)
