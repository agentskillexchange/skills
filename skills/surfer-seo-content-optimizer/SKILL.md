---
title: "Surfer SEO Content Optimizer"
description: "The Surfer SEO Content Optimizer reverse-engineers search ranking factors by analyzing top-performing pages for target keywords. It uses the DataForSEO SERP API to fetch current search results including featured snippets, People Also Ask, and related searches. Each competing page is fetched and analyzed using cheerio for DOM parsing and natural (NLP library) for entity extraction, term frequency analysis, and readability scoring via Flesch-Kincaid. The skill generates comprehensive content briefs containing recommended word count ranges (based on top-10 median), must-include NLP entities and LSI keywords, optimal heading hierarchy (H2/H3 distribution), and internal linking opportunities matched against an existing sitemap. Content scoring compares draft articles against the generated brief, producing a 0-100 optimization score with specific improvement suggestions. The tool tracks keyword cannibalization by cross-referencing target keywords against existing published content via site:domain search. Output formats include Markdown briefs, JSON for CMS integration, and HTML reports with competitive comparison tables."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/surfer-seo-content-optimizer/"
framework:
  - "ChatGPT Agents"
---

# Surfer SEO Content Optimizer

The Surfer SEO Content Optimizer reverse-engineers search ranking factors by analyzing top-performing pages for target keywords. It uses the DataForSEO SERP API to fetch current search results including featured snippets, People Also Ask, and related searches. Each competing page is fetched and analyzed using cheerio for DOM parsing and natural (NLP library) for entity extraction, term frequency analysis, and readability scoring via Flesch-Kincaid. The skill generates comprehensive content briefs containing recommended word count ranges (based on top-10 median), must-include NLP entities and LSI keywords, optimal heading hierarchy (H2/H3 distribution), and internal linking opportunities matched against an existing sitemap. Content scoring compares draft articles against the generated brief, producing a 0-100 optimization score with specific improvement suggestions. The tool tracks keyword cannibalization by cross-referencing target keywords against existing published content via site:domain search. Output formats include Markdown briefs, JSON for CMS integration, and HTML reports with competitive comparison tables.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/surfer-seo-content-optimizer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/surfer-seo-content-optimizer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/surfer-seo-content-optimizer/)
