---
title: Surfer SEO Content Optimizer
description: The Surfer SEO Content Optimizer reverse-engineers search ranking factors
  by analyzing top-performing pages for target keywords. It uses the DataForSEO SERP
  API to fetch current search results including featured snippets, People Also Ask,
  and related searches. Each competing page is fetched and analyzed using cheerio
  for DOM parsing and natural (NLP library) for entity extraction, term frequency
  analysis, and readability scoring via Flesch-Kincaid. The skill generates comprehensive
  content briefs containing recommended word count ranges (based on top-10 median),
  must-include NLP entities and LSI keywords, optimal heading hierarchy (H2/H3 distribution),
  and internal linking opportunities matched against an existing sitemap. Content
  scoring compares draft articles against the generated brief, producing a 0-100 optimization
  score with specific improvement suggestions. The tool tracks keyword cannibalization
  by cross-referencing target keywords against existing published content via site:domain
  search. Output formats include Markdown briefs, JSON for CMS integration, and HTML
  reports with competitive comparison tables.
verification: security_reviewed
source: https://agentskillexchange.com/skills/surfer-seo-content-optimizer/
category:
- Content Writing &amp; SEO
framework:
- ChatGPT Agents
---

# Surfer SEO Content Optimizer

The Surfer SEO Content Optimizer reverse-engineers search ranking factors by analyzing top-performing pages for target keywords. It uses the DataForSEO SERP API to fetch current search results including featured snippets, People Also Ask, and related searches. Each competing page is fetched and analyzed using cheerio for DOM parsing and natural (NLP library) for entity extraction, term frequency analysis, and readability scoring via Flesch-Kincaid. The skill generates comprehensive content briefs containing recommended word count ranges (based on top-10 median), must-include NLP entities and LSI keywords, optimal heading hierarchy (H2/H3 distribution), and internal linking opportunities matched against an existing sitemap. Content scoring compares draft articles against the generated brief, producing a 0-100 optimization score with specific improvement suggestions. The tool tracks keyword cannibalization by cross-referencing target keywords against existing published content via site:domain search. Output formats include Markdown briefs, JSON for CMS integration, and HTML reports with competitive comparison tables.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/surfer-seo-content-optimizer/)
