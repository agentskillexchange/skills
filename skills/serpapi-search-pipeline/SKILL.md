---
name: "SerpAPI Search Pipeline"
description: "Automates multi-engine searches via SerpAPI (Google, Bing, DuckDuckGo) with structured JSON extraction. Supports pagination, location targeting, and result deduplication using MinHash LSH."
category: "Research & Scraping"
framework: "OpenClaw"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/serpapi-search-pipeline/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "sqlite"  # from ase_tool_match
  github_stars: 7043  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 4960915  # from ase_npm_downloads
  github_repo: "WiseLibs/better-sqlite3"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# SerpAPI Search Pipeline

Automates multi-engine searches via SerpAPI (Google, Bing, DuckDuckGo) with structured JSON extraction. Supports pagination, location targeting, and result deduplication using MinHash LSH.

## Overview

The SerpAPI Search Pipeline skill provides a comprehensive interface for automated web research through the SerpAPI service. It connects to Google Search, Bing, DuckDuckGo, and Yahoo engines via a unified API layer.

Key capabilities include automatic pagination handling across result sets, geographic targeting using UULE parameters for location-specific results, and intelligent result deduplication using MinHash Locality-Sensitive Hashing to eliminate near-duplicate content.

The skill supports structured output in JSON, CSV, and Markdown table formats. It includes rate limiting with exponential backoff, proxy rotation support, and cached result storage using SQLite for repeat queries. SERP feature extraction captures knowledge panels, featured snippets, and People Also Ask data automatically.

Configuration supports custom extraction rules via CSS selectors and XPath expressions for specialized data capture beyond standard search results.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill serpapi-search-pipeline
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill serpapi-search-pipeline -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill serpapi-search-pipeline -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill serpapi-search-pipeline -a codex
```

### OpenClaw

```bash
clawhub install serpapi-search-pipeline
```

## Source

- Marketplace: https://agentskillexchange.com/skills/serpapi-search-pipeline/
