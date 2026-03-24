---
name: "Cheerio DOM Scraping Toolkit"
description: "Parses static HTML using Cheerio’s jQuery-like API for fast server-side DOM traversal and data extraction. Generates extraction patterns with CSS selectors optimized for resilience to layout changes."
category: "Research & Scraping"
framework: "Cursor"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/cheerio-dom-scraping-toolkit/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "cheerio"  # from ase_tool_match
  github_stars: 30229  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 18512628  # from ase_npm_downloads
  github_repo: "cheeriojs/cheerio"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Cheerio DOM Scraping Toolkit

Parses static HTML using Cheerio’s jQuery-like API for fast server-side DOM traversal and data extraction. Generates extraction patterns with CSS selectors optimized for resilience to layout changes.

## Overview

The Cheerio DOM Scraping Toolkit skill uses **Cheerio**, the fast and lightweight jQuery-like library for server-side HTML parsing and manipulation. Unlike browser-based scraping, Cheerio operates on raw HTML strings without a DOM environment, making it significantly faster for static page extraction tasks.

The skill generates extraction code using Cheerio’s CSS selector engine, supporting complex selectors including attribute selectors, pseudo-classes (:nth-child, :contains, :has), and combinators. It constructs resilient selectors that tolerate minor layout changes by preferring semantic attributes (data-*, aria-*, role) over positional selectors.

Key capabilities include table-to-JSON conversion with header detection, structured data extraction from Schema.org/JSON-LD embedded markup, and form field enumeration for understanding submission requirements. The skill handles character encoding detection and conversion, relative URL resolution using Cheerio’s built-in utilities, and generates streaming extraction pipelines using htmlparser2 for memory-efficient processing of large HTML documents. Output includes typed TypeScript interfaces matching the extracted data structure.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill cheerio-dom-scraping-toolkit
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill cheerio-dom-scraping-toolkit -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill cheerio-dom-scraping-toolkit -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill cheerio-dom-scraping-toolkit -a codex
```

### OpenClaw

```bash
clawhub install cheerio-dom-scraping-toolkit
```

## Source

- Marketplace: https://agentskillexchange.com/skills/cheerio-dom-scraping-toolkit/
