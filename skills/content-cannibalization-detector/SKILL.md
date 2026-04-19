---
title: "Content Cannibalization Detector"
description: "Content Cannibalization Detector finds pages competing for the same search queries by cross-referencing Google Search Console Performance API data with on-page content analysis. It pulls query-level impressions and clicks per URL through the searchAnalytics.query method, grouping results by query to identify URLs sharing keyword targeting. The detection algorithm computes TF-IDF vectors for page content and calculates cosine similarity between pages ranking for overlapping queries. Pages with similarity scores above 0.7 that share more than three ranking queries are flagged as cannibalization candidates. The tool also checks title tags, H1 headers, and meta descriptions for direct keyword overlap using fuzzy string matching via python-Levenshtein. Output includes a prioritized list of cannibalization pairs with recommended actions: merge content into the stronger page, differentiate keyword targeting, or implement 301 redirects. Redirect maps are generated in CSV format compatible with Screaming Frog&#8217;s redirect chain validation. The tool integrates with Screaming Frog crawl exports to correlate internal link equity, showing which cannibalized page receives more internal authority signals to inform the consolidation decision."
source: "https://agentskillexchange.com/skills/content-cannibalization-detector/"
verification: "security_reviewed"
category:
  - "Content Writing &amp; SEO"
framework:
  - "Gemini"
---

# Content Cannibalization Detector

Content Cannibalization Detector finds pages competing for the same search queries by cross-referencing Google Search Console Performance API data with on-page content analysis. It pulls query-level impressions and clicks per URL through the searchAnalytics.query method, grouping results by query to identify URLs sharing keyword targeting. The detection algorithm computes TF-IDF vectors for page content and calculates cosine similarity between pages ranking for overlapping queries. Pages with similarity scores above 0.7 that share more than three ranking queries are flagged as cannibalization candidates. The tool also checks title tags, H1 headers, and meta descriptions for direct keyword overlap using fuzzy string matching via python-Levenshtein. Output includes a prioritized list of cannibalization pairs with recommended actions: merge content into the stronger page, differentiate keyword targeting, or implement 301 redirects. Redirect maps are generated in CSV format compatible with Screaming Frog&#8217;s redirect chain validation. The tool integrates with Screaming Frog crawl exports to correlate internal link equity, showing which cannibalized page receives more internal authority signals to inform the consolidation decision.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/content-cannibalization-detector/)
