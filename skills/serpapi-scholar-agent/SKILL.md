---
title: "SerpAPI Scholar Agent"
description: "Automates academic research using the SerpAPI Google Scholar endpoint. Extracts citation graphs, h-index data, and co-author networks for literature reviews. Supports BibTeX export and cross-references with Semantic Scholar API."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/serpapi-scholar-agent/"
category:
  - "Research & Scraping"
framework:
  - "Claude Code"
---

# SerpAPI Scholar Agent

The SerpAPI Scholar Agent skill enables Claude to conduct systematic academic research by querying Google Scholar through the SerpAPI REST interface. It retrieves paper metadata, citation counts, author profiles, and related works for any given topic or researcher. Key capabilities include building citation graphs that map how papers reference each other, computing h-index and i10-index for author evaluation, and identifying co-author networks. The skill handles pagination across large result sets and deduplicates entries from multiple queries. Output formats include BibTeX for direct import into LaTeX projects, structured JSON for programmatic analysis, and markdown summaries for quick review. The skill cross-references results with the Semantic Scholar API to enrich metadata with abstract text, venue information, and open-access PDF links when available. Designed for graduate students, researchers, and technical writers who need to quickly survey a field, identify seminal papers, or verify citation claims. Rate limiting and caching prevent excessive API calls during iterative searches.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/serpapi-scholar-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/serpapi-scholar-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/serpapi-scholar-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/serpapi-scholar-agent/)
