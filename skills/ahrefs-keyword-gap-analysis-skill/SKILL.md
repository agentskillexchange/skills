---
title: "Ahrefs Keyword Gap Analysis Skill"
description: "This skill performs competitive keyword gap analysis using the Ahrefs REST API v3. It queries the /v3/site-explorer/organic-keywords endpoint for both the target domain and up to 5 competitor domains, using parameters: target (domain), country_code, limit, offset, and volume_min for filtering. The skill cross-references keyword sets to identify three categories: missing keywords (competitors rank, target doesn&#8217;t), weak keywords (target ranks lower than competitors), and untapped keywords (low competition, high volume). For each keyword, it pulls metrics from Ahrefs: search_volume, keyword_difficulty (0-100), cpc (cost per click), traffic, and position. The traffic potential calculation uses: potential_traffic = search_volume * CTR_curve[estimated_position] where CTR curves are based on published click-through-rate studies. Results are scored using a composite metric: opportunity_score = (search_volume * (100 &#8211; keyword_difficulty)) / 100 * cpc_value. The skill generates a prioritized content brief for each high-opportunity keyword including: target word count (based on top-ranking content analysis), required subtopics (from SERP feature analysis), and content type recommendation (blog post, landing page, comparison). Output includes CSV export with all metrics and a markdown summary grouped by content cluster topics."
source: "https://agentskillexchange.com/skills/ahrefs-keyword-gap-analysis-skill/"
verification: "security_reviewed"
category:
  - "Content Writing &amp; SEO"
framework:
  - "ChatGPT Agents"
---

# Ahrefs Keyword Gap Analysis Skill

This skill performs competitive keyword gap analysis using the Ahrefs REST API v3. It queries the /v3/site-explorer/organic-keywords endpoint for both the target domain and up to 5 competitor domains, using parameters: target (domain), country_code, limit, offset, and volume_min for filtering. The skill cross-references keyword sets to identify three categories: missing keywords (competitors rank, target doesn&#8217;t), weak keywords (target ranks lower than competitors), and untapped keywords (low competition, high volume). For each keyword, it pulls metrics from Ahrefs: search_volume, keyword_difficulty (0-100), cpc (cost per click), traffic, and position. The traffic potential calculation uses: potential_traffic = search_volume * CTR_curve[estimated_position] where CTR curves are based on published click-through-rate studies. Results are scored using a composite metric: opportunity_score = (search_volume * (100 &#8211; keyword_difficulty)) / 100 * cpc_value. The skill generates a prioritized content brief for each high-opportunity keyword including: target word count (based on top-ranking content analysis), required subtopics (from SERP feature analysis), and content type recommendation (blog post, landing page, comparison). Output includes CSV export with all metrics and a markdown summary grouped by content cluster topics.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ahrefs-keyword-gap-analysis-skill/)
