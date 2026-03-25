---
name: "Keyword Cannibalization Detector"
description: "Detects keyword cannibalization issues using Google Search Console API performance data and Semrush keyword tracking. Maps URL-to-keyword overlaps and suggests content consolidation strategies."
category: "Content Writing & SEO"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/keyword-cannibalization-detector/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "wordpress"  # from ase_tool_match
  github_stars: 20976  # from ase_github_stars (integer, not string)
  github_repo: "WordPress/WordPress"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Keyword Cannibalization Detector

Detects keyword cannibalization issues using Google Search Console API performance data and Semrush keyword tracking. Maps URL-to-keyword overlaps and suggests content consolidation strategies.

## Overview

The Keyword Cannibalization Detector identifies and resolves instances where multiple pages compete for the same search queries, diluting SEO performance. It connects to the Google Search Console API searchAnalytics.query endpoint to pull query-level data with page, position, clicks, and impressions dimensions. The agent cross-references this data with Semrush position tracking API to identify keywords where multiple URLs rank within the top 100 results. It calculates cannibalization severity scores based on position volatility, click distribution, and impression share between competing pages. The detector generates actionable recommendations including 301 redirect maps, canonical tag suggestions, content merge plans, and internal link restructuring using a PageRank-inspired link equity model. It integrates with the Ahrefs Batch Analysis API to assess backlink profiles of competing pages and determine which URL should be the canonical target. The agent monitors cannibalization trends over time using BigQuery exports from Search Console and generates weekly reports via the Google Sheets API. Supports WordPress sites through direct WP REST API integration for implementing canonical tags and redirect rules via the Redirection plugin API.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill keyword-cannibalization-detector
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill keyword-cannibalization-detector -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill keyword-cannibalization-detector -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill keyword-cannibalization-detector -a codex
```

### OpenClaw

```bash
clawhub install keyword-cannibalization-detector
```

## Source

- Marketplace: https://agentskillexchange.com/skills/keyword-cannibalization-detector/
