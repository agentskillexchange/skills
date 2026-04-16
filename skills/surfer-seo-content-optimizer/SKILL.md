---
title: "Surfer SEO Content Optimizer"
description: "Analyzes top SERP competitors using DataForSEO API and generates content optimization briefs with target word count, NLP entity coverage, heading structure, and internal linking recommendations."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/surfer-seo-content-optimizer/"
category:
  - "Content Writing &amp; SEO"
framework:
  - "ChatGPT Agents"
---

# Surfer SEO Content Optimizer

The Surfer SEO Content Optimizer reverse-engineers search ranking factors by analyzing top-performing pages for target keywords. It uses the DataForSEO SERP API to fetch current search results including featured snippets, People Also Ask, and related searches. Each competing page is fetched and analyzed using cheerio for DOM parsing and natural (NLP library) for entity extraction, term frequency analysis, and readability scoring via Flesch-Kincaid. The skill generates comprehensive content briefs containing recommended word count ranges (based on top-10 median), must-include NLP entities and LSI keywords, optimal heading hierarchy (H2/H3 distribution), and internal linking opportunities matched against an existing sitemap. Content scoring compares draft articles against the generated brief, producing a 0-100 optimization score with specific improvement suggestions. The tool tracks keyword cannibalization by cross-referencing target keywords against existing published content via site:domain search. Output formats include Markdown briefs, JSON for CMS integration, and HTML reports with competitive comparison tables.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/surfer-seo-content-optimizer/)
