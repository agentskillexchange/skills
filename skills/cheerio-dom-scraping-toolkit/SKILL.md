---
title: "Cheerio DOM Scraping Toolkit"
description: "Parses static HTML using Cheerio’s jQuery-like API for fast server-side DOM traversal and data extraction. Generates extraction patterns with CSS selectors optimized for resilience to layout changes."
verification: "security_reviewed"
source: "https://github.com/cheeriojs/cheerio"
category:
  - "Research & Scraping"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "cheeriojs/cheerio"
  github_stars: 30270
  npm_package: "cheerio"
  npm_weekly_downloads: 19621708
---

# Cheerio DOM Scraping Toolkit

The Cheerio DOM Scraping Toolkit skill uses Cheerio, the fast and lightweight jQuery-like library for server-side HTML parsing and manipulation. Unlike browser-based scraping, Cheerio operates on raw HTML strings without a DOM environment, making it significantly faster for static page extraction tasks. The skill generates extraction code using Cheerio’s CSS selector engine, supporting complex selectors including attribute selectors, pseudo-classes (:nth-child, :contains, :has), and combinators. It constructs resilient selectors that tolerate minor layout changes by preferring semantic attributes (data-*, aria-*, role) over positional selectors. Key capabilities include table-to-JSON conversion with header detection, structured data extraction from Schema.org/JSON-LD embedded markup, and form field enumeration for understanding submission requirements. The skill handles character encoding detection and conversion, relative URL resolution using Cheerio’s built-in utilities, and generates streaming extraction pipelines using htmlparser2 for memory-efficient processing of large HTML documents. Output includes typed TypeScript interfaces matching the extracted data structure.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/cheerio-dom-scraping-toolkit/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/cheerio-dom-scraping-toolkit
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/cheerio-dom-scraping-toolkit`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cheerio-dom-scraping-toolkit/)
