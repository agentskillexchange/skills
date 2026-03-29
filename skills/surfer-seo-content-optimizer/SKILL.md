---
name: "Surfer SEO Content Optimizer"
description: "Analyzes top SERP competitors using DataForSEO API and generates content optimization briefs with target word count, NLP entity coverage, heading structure, and internal linking recommendations."
category: "Content Writing & SEO"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/surfer-seo-content-optimizer/"
tool_ecosystem:
  tool: cheerio
  github_stars: 30231
  npm_weekly_downloads: 18512628
  github_repo: cheeriojs/cheerio
  license: MIT
  maintained: true
---
# Surfer SEO Content Optimizer

Analyzes top SERP competitors using DataForSEO API and generates content optimization briefs with target word count, NLP entity coverage, heading structure, and internal linking recommendations.

## Overview

The Surfer SEO Content Optimizer reverse-engineers search ranking factors by analyzing top-performing pages for target keywords. It uses the DataForSEO SERP API to fetch current search results including featured snippets, People Also Ask, and related searches. Each competing page is fetched and analyzed using cheerio for DOM parsing and natural (NLP library) for entity extraction, term frequency analysis, and readability scoring via Flesch-Kincaid. The skill generates comprehensive content briefs containing recommended word count ranges (based on top-10 median), must-include NLP entities and LSI keywords, optimal heading hierarchy (H2/H3 distribution), and internal linking opportunities matched against an existing sitemap. Content scoring compares draft articles against the generated brief, producing a 0-100 optimization score with specific improvement suggestions. The tool tracks keyword cannibalization by cross-referencing target keywords against existing published content via site:domain search. Output formats include Markdown briefs, JSON for CMS integration, and HTML reports with competitive comparison tables.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill surfer-seo-content-optimizer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill surfer-seo-content-optimizer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill surfer-seo-content-optimizer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill surfer-seo-content-optimizer -a codex
```

### OpenClaw

```bash
clawhub install surfer-seo-content-optimizer
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/surfer-seo-content-optimizer/)
