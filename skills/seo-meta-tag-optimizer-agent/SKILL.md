---
name: "SEO Meta Tag Optimizer"
description: "Generates optimized title tags, meta descriptions, and Open Graph markup using Google NLP API for entity salience scoring. Integrates with Yoast SEO REST API for WordPress deployments."
category: "Content Writing & SEO"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/seo-meta-tag-optimizer-agent/"
---
# SEO Meta Tag Optimizer

Generates optimized title tags, meta descriptions, and Open Graph markup using Google NLP API for entity salience scoring. Integrates with Yoast SEO REST API for WordPress deployments.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/seo-meta-tag-optimizer-agent/)
