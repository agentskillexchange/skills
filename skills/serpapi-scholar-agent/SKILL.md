---
name: "SerpAPI Scholar Agent"
description: "Automates academic research using the SerpAPI Google Scholar endpoint. Extracts citation graphs, h-index data, and co-author networks for literature reviews. Supports BibTeX export and cross-references with Semantic Scholar API."
category: "Research & Scraping"
framework: "Claude Code"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/serpapi-scholar-agent/"
---

# SerpAPI Scholar Agent

Automates academic research using the SerpAPI Google Scholar endpoint. Extracts citation graphs, h-index data, and co-author networks for literature reviews. Supports BibTeX export and cross-references with Semantic Scholar API.

## Overview

The SerpAPI Scholar Agent skill enables Claude to conduct systematic academic research by querying Google Scholar through the SerpAPI REST interface. It retrieves paper metadata, citation counts, author profiles, and related works for any given topic or researcher.

Key capabilities include building citation graphs that map how papers reference each other, computing h-index and i10-index for author evaluation, and identifying co-author networks. The skill handles pagination across large result sets and deduplicates entries from multiple queries.

Output formats include BibTeX for direct import into LaTeX projects, structured JSON for programmatic analysis, and markdown summaries for quick review. The skill cross-references results with the Semantic Scholar API to enrich metadata with abstract text, venue information, and open-access PDF links when available.

Designed for graduate students, researchers, and technical writers who need to quickly survey a field, identify seminal papers, or verify citation claims. Rate limiting and caching prevent excessive API calls during iterative searches.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill serpapi-scholar-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill serpapi-scholar-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill serpapi-scholar-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill serpapi-scholar-agent -a codex
```

### OpenClaw

```bash
clawhub install serpapi-scholar-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/serpapi-scholar-agent/
