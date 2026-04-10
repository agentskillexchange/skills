---
title: "SerpAPI Scholar Agent"
description: "Automates academic research using the SerpAPI Google Scholar endpoint. Extracts citation graphs, h-index data, and co-author networks for literature reviews. Supports BibTeX export and cross-references with Semantic Scholar API."
slug: "serpapi-scholar-agent"
category:
  - "Research &amp; Scraping"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/serpapi-scholar-agent/"
---

# SerpAPI Scholar Agent

Automates academic research using the SerpAPI Google Scholar endpoint. Extracts citation graphs, h-index data, and co-author networks for literature reviews. Supports BibTeX export and cross-references with Semantic Scholar API.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install serpapi-scholar-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The SerpAPI Scholar Agent skill enables Claude to conduct systematic academic research by querying Google Scholar through the SerpAPI REST interface. It retrieves paper metadata, citation counts, author profiles, and related works for any given topic or researcher.
Key capabilities include building citation graphs that map how papers reference each other, computing h-index and i10-index for author evaluation, and identifying co-author networks. The skill handles pagination across large result sets and deduplicates entries from multiple queries.
Output formats include BibTeX for direct import into LaTeX projects, structured JSON for programmatic analysis, and markdown summaries for quick review. The skill cross-references results with the Semantic Scholar API to enrich metadata with abstract text, venue information, and open-access PDF links when available.
Designed for graduate students, researchers, and technical writers who need to quickly survey a field, identify seminal papers, or verify citation claims. Rate limiting and caching prevent excessive API calls during iterative searches.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/serpapi-scholar-agent/)
