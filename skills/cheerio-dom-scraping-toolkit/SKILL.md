---
title: "Cheerio DOM Scraping Toolkit"
description: "The Cheerio DOM Scraping Toolkit skill uses Cheerio , the fast and lightweight jQuery-like library for server-side HTML parsing and manipulation. Unlike browser-based scraping, Cheerio operates on raw HTML strings without a DOM environment, making it significantly faster for static page extraction tasks. The skill generates extraction code using Cheerio&#8217;s CSS selector engine, supporting complex selectors including attribute selectors, pseudo-classes (:nth-child, :contains, :has), and combinators. It constructs resilient selectors that tolerate minor layout changes by preferring semantic attributes (data-*, aria-*, role) over positional selectors. Key capabilities include table-to-JSON conversion with header detection, structured data extraction from Schema.org/JSON-LD embedded markup, and form field enumeration for understanding submission requirements. The skill handles character encoding detection and conversion, relative URL resolution using Cheerio&#8217;s built-in utilities, and generates streaming extraction pipelines using htmlparser2 for memory-efficient processing of large HTML documents. Output includes typed TypeScript interfaces matching the extracted data structure."
source: "https://github.com/cheeriojs/cheerio"
verification: "security_reviewed"
category:
  - "Research &amp; Scraping"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "cheeriojs/cheerio"
  github_stars: 30270
  npm_package: "cheerio"
  npm_weekly_downloads: 19621708
---

# Cheerio DOM Scraping Toolkit

The Cheerio DOM Scraping Toolkit skill uses Cheerio , the fast and lightweight jQuery-like library for server-side HTML parsing and manipulation. Unlike browser-based scraping, Cheerio operates on raw HTML strings without a DOM environment, making it significantly faster for static page extraction tasks. The skill generates extraction code using Cheerio&#8217;s CSS selector engine, supporting complex selectors including attribute selectors, pseudo-classes (:nth-child, :contains, :has), and combinators. It constructs resilient selectors that tolerate minor layout changes by preferring semantic attributes (data-*, aria-*, role) over positional selectors. Key capabilities include table-to-JSON conversion with header detection, structured data extraction from Schema.org/JSON-LD embedded markup, and form field enumeration for understanding submission requirements. The skill handles character encoding detection and conversion, relative URL resolution using Cheerio&#8217;s built-in utilities, and generates streaming extraction pipelines using htmlparser2 for memory-efficient processing of large HTML documents. Output includes typed TypeScript interfaces matching the extracted data structure.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cheerio-dom-scraping-toolkit/)
