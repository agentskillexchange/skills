---
name: "SerpAPI Research Pipeline"
description: "Builds structured research datasets by querying SerpAPI Google Search, Google Scholar, and Google News endpoints. Extracts entities via spaCy NER and stores results in SQLite with full-text search."
category: "Research & Scraping"
framework: "Codex"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/serpapi-research-pipeline/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "sqlite"  # from ase_tool_match
  npm_weekly_downloads: 4960915  # from ase_npm_downloads
---

# SerpAPI Research Pipeline

Builds structured research datasets by querying SerpAPI Google Search, Google Scholar, and Google News endpoints. Extracts entities via spaCy NER and stores results in SQLite with full-text search.

## Overview

The SerpAPI Research Pipeline automates multi-source research by orchestrating queries across SerpAPI Google Search, Google Scholar, and Google News JSON endpoints. For each research topic, it generates query variations using synonym expansion and boolean operators to maximize coverage. Search results are parsed and deduplicated using URL normalization and content fingerprinting. The pipeline extracts named entities from result snippets using spaCy NER models, identifying people, organizations, locations, and technical terms relevant to the research domain. All results are stored in a SQLite database with FTS5 full-text search indexes for rapid retrieval. The agent supports iterative deepening where initial results inform follow-up queries for comprehensive topic coverage. Citation graphs are built by cross-referencing Google Scholar results. Export formats include CSV, JSON, and formatted Markdown research briefs with source attribution and confidence scoring.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill serpapi-research-pipeline
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill serpapi-research-pipeline -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill serpapi-research-pipeline -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill serpapi-research-pipeline -a codex
```

### OpenClaw

```bash
clawhub install serpapi-research-pipeline
```

## Source

- Marketplace: https://agentskillexchange.com/skills/serpapi-research-pipeline/
