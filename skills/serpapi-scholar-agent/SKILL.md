---
title: SerpAPI Scholar Agent
description: The SerpAPI Scholar Agent skill enables Claude to conduct systematic
  academic research by querying Google Scholar through the SerpAPI REST interface.
  It retrieves paper metadata, citation counts, author profiles, and related works
  for any given topic or researcher. Key capabilities include building citation graphs
  that map how papers reference each other, computing h-index and i10-index for author
  evaluation, and identifying co-author networks. The skill handles pagination across
  large result sets and deduplicates entries from multiple queries. Output formats
  include BibTeX for direct import into LaTeX projects, structured JSON for programmatic
  analysis, and markdown summaries for quick review. The skill cross-references results
  with the Semantic Scholar API to enrich metadata with abstract text, venue information,
  and open-access PDF links when available. Designed for graduate students, researchers,
  and technical writers who need to quickly survey a field, identify seminal papers,
  or verify citation claims. Rate limiting and caching prevent excessive API calls
  during iterative searches.
verification: security_reviewed
source: https://agentskillexchange.com/skills/serpapi-scholar-agent/
category:
- Research &amp; Scraping
framework:
- Claude Code
---

# SerpAPI Scholar Agent

The SerpAPI Scholar Agent skill enables Claude to conduct systematic academic research by querying Google Scholar through the SerpAPI REST interface. It retrieves paper metadata, citation counts, author profiles, and related works for any given topic or researcher. Key capabilities include building citation graphs that map how papers reference each other, computing h-index and i10-index for author evaluation, and identifying co-author networks. The skill handles pagination across large result sets and deduplicates entries from multiple queries. Output formats include BibTeX for direct import into LaTeX projects, structured JSON for programmatic analysis, and markdown summaries for quick review. The skill cross-references results with the Semantic Scholar API to enrich metadata with abstract text, venue information, and open-access PDF links when available. Designed for graduate students, researchers, and technical writers who need to quickly survey a field, identify seminal papers, or verify citation claims. Rate limiting and caching prevent excessive API calls during iterative searches.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/serpapi-scholar-agent/)
