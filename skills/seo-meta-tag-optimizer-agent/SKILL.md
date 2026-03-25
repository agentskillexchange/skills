---
name: "SEO Meta Tag Optimizer"
description: "Generates optimized title tags, meta descriptions, and Open Graph markup using Google NLP API for entity salience scoring. Integrates with Yoast SEO REST API for WordPress deployments."
category: "Content Writing & SEO"
framework: "ChatGPT Agents"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/seo-meta-tag-optimizer-agent/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "wordpress"  # from ase_tool_match
  github_stars: 20973  # from ase_github_stars (integer, not string)
  github_repo: "WordPress/WordPress"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# SEO Meta Tag Optimizer

Generates optimized title tags, meta descriptions, and Open Graph markup using Google NLP API for entity salience scoring. Integrates with Yoast SEO REST API for WordPress deployments.

## Overview

The SEO Meta Tag Optimizer analyzes page content and generates search-engine-optimized metadata using the Google Cloud Natural Language API for entity extraction and salience scoring. It identifies primary and secondary entities in content, then crafts title tags under 60 characters and meta descriptions under 155 characters that maximize click-through rate. The skill uses the DataForSEO SERP API to analyze competitor meta tags for target keywords and identify content gaps. Open Graph and Twitter Card markup is generated automatically with proper og:type, og:image dimensions, and twitter:card variants. For WordPress sites, it integrates directly with the Yoast SEO REST API to push optimized metadata without manual editing. The skill includes A/B testing support by generating multiple title/description variants scored by predicted CTR using a trained logistic regression model. Schema.org JSON-LD markup is generated for Article, Product, FAQ, and HowTo content types.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill seo-meta-tag-optimizer-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill seo-meta-tag-optimizer-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill seo-meta-tag-optimizer-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill seo-meta-tag-optimizer-agent -a codex
```

### OpenClaw

```bash
clawhub install seo-meta-tag-optimizer-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/seo-meta-tag-optimizer-agent/
