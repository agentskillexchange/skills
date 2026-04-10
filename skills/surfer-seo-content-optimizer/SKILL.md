---
title: "Surfer SEO Content Optimizer"
description: "Analyzes top SERP competitors using DataForSEO API and generates content optimization briefs with target word count, NLP entity coverage, heading structure, and internal linking recommendations."
slug: "surfer-seo-content-optimizer"
category:
  - "Content Writing &amp; SEO"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/surfer-seo-content-optimizer/"
listed: true
---

# Surfer SEO Content Optimizer

Analyzes top SERP competitors using DataForSEO API and generates content optimization briefs with target word count, NLP entity coverage, heading structure, and internal linking recommendations.

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
clawhub install surfer-seo-content-optimizer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Surfer SEO Content Optimizer reverse-engineers search ranking factors by analyzing top-performing pages for target keywords. It uses the DataForSEO SERP API to fetch current search results including featured snippets, People Also Ask, and related searches. Each competing page is fetched and analyzed using cheerio for DOM parsing and natural (NLP library) for entity extraction, term frequency analysis, and readability scoring via Flesch-Kincaid. The skill generates comprehensive content briefs containing recommended word count ranges (based on top-10 median), must-include NLP entities and LSI keywords, optimal heading hierarchy (H2/H3 distribution), and internal linking opportunities matched against an existing sitemap. Content scoring compares draft articles against the generated brief, producing a 0-100 optimization score with specific improvement suggestions. The tool tracks keyword cannibalization by cross-referencing target keywords against existing published content via site:domain search. Output formats include Markdown briefs, JSON for CMS integration, and HTML reports with competitive comparison tables.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/surfer-seo-content-optimizer/)
