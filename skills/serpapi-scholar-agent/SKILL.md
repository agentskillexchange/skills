---
title: "SerpAPI Scholar Agent"
description: "The SerpAPI Scholar Agent skill enables Claude to conduct systematic academic research by querying Google Scholar through the SerpAPI REST interface. It retrieves paper metadata, citation counts, author profiles, and related works for any given topic or researcher.\nKey capabilities include building citation graphs that map how papers reference each other, computing h-index and i10-index for author evaluation, and identifying co-author networks. The skill handles pagination across large result sets and deduplicates entries from multiple queries.\nOutput formats include BibTeX for direct import into LaTeX projects, structured JSON for programmatic analysis, and markdown summaries for quick review. The skill cross-references results with the Semantic Scholar API to enrich metadata with abstract text, venue information, and open-access PDF links when available.\nDesigned for graduate students, researchers, and technical writers who need to quickly survey a field, identify seminal papers, or verify citation claims. Rate limiting and caching prevent excessive API calls during iterative searches."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/serpapi-scholar-agent/"
framework:
  - "Claude Code"
---

# SerpAPI Scholar Agent

The SerpAPI Scholar Agent skill enables Claude to conduct systematic academic research by querying Google Scholar through the SerpAPI REST interface. It retrieves paper metadata, citation counts, author profiles, and related works for any given topic or researcher.
Key capabilities include building citation graphs that map how papers reference each other, computing h-index and i10-index for author evaluation, and identifying co-author networks. The skill handles pagination across large result sets and deduplicates entries from multiple queries.
Output formats include BibTeX for direct import into LaTeX projects, structured JSON for programmatic analysis, and markdown summaries for quick review. The skill cross-references results with the Semantic Scholar API to enrich metadata with abstract text, venue information, and open-access PDF links when available.
Designed for graduate students, researchers, and technical writers who need to quickly survey a field, identify seminal papers, or verify citation claims. Rate limiting and caching prevent excessive API calls during iterative searches.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/serpapi-scholar-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/serpapi-scholar-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/serpapi-scholar-agent/)
