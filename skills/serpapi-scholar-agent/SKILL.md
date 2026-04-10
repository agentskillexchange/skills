---
name: SerpAPI Scholar Agent
description: Automates academic research using the SerpAPI Google Scholar endpoint.
  Extracts citation graphs, h-index data, and co-author networks for literature reviews.
  Supports BibTeX export and cross-references with Semantic Scholar API.
verification: security_reviewed
source: https://agentskillexchange.com/skills/serpapi-scholar-agent/
category:
- Research &amp; Scraping
framework:
- Claude Code
---
# SerpAPI Scholar Agent

The SerpAPI Scholar Agent skill enables Claude to conduct systematic academic research by querying Google Scholar through the SerpAPI REST interface. It retrieves paper metadata, citation counts, author profiles, and related works for any given topic or researcher.
Key capabilities include building citation graphs that map how papers reference each other, computing h-index and i10-index for author evaluation, and identifying co-author networks. The skill handles pagination across large result sets and deduplicates entries from multiple queries.
Output formats include BibTeX for direct import into LaTeX projects, structured JSON for programmatic analysis, and markdown summaries for quick review. The skill cross-references results with the Semantic Scholar API to enrich metadata with abstract text, venue information, and open-access PDF links when available.
Designed for graduate students, researchers, and technical writers who need to quickly survey a field, identify seminal papers, or verify citation claims. Rate limiting and caching prevent excessive API calls during iterative searches.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/serpapi-scholar-agent/)
