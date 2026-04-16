---
title: "Ahrefs Keyword Gap Analysis Skill"
description: "Identifies keyword opportunities by comparing competitor rankings using Ahrefs’ /v3/site-explorer/organic-keywords API endpoint. Calculates traffic potential from search volume, CPC, and keyword difficulty scores."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/ahrefs-keyword-gap-analysis-skill/"
category:
  - "Content Writing &amp; SEO"
framework:
  - "ChatGPT Agents"
---

# Ahrefs Keyword Gap Analysis Skill

This skill performs competitive keyword gap analysis using the Ahrefs REST API v3. It queries the /v3/site-explorer/organic-keywords endpoint for both the target domain and up to 5 competitor domains, using parameters: target (domain), country_code, limit, offset, and volume_min for filtering. The skill cross-references keyword sets to identify three categories: missing keywords (competitors rank, target doesn’t), weak keywords (target ranks lower than competitors), and untapped keywords (low competition, high volume). For each keyword, it pulls metrics from Ahrefs: search_volume, keyword_difficulty (0-100), cpc (cost per click), traffic, and position. The traffic potential calculation uses: potential_traffic = search_volume * CTR_curve[estimated_position] where CTR curves are based on published click-through-rate studies. Results are scored using a composite metric: opportunity_score = (search_volume * (100 – keyword_difficulty)) / 100 * cpc_value. The skill generates a prioritized content brief for each high-opportunity keyword including: target word count (based on top-ranking content analysis), required subtopics (from SERP feature analysis), and content type recommendation (blog post, landing page, comparison). Output includes CSV export with all metrics and a markdown summary grouped by content cluster topics.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ahrefs-keyword-gap-analysis-skill/)
