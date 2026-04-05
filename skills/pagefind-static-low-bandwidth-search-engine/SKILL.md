---
name: "Pagefind Static Low-Bandwidth Search Engine"
description: "Pagefind is a static search library written in Rust that indexes your built site and adds a search bundle requiring no server infrastructure. It performs well on large sites while using minimal bandwidth."
category: "Research & Scraping"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/Pagefind/pagefind"
tool_ecosystem:
  tool: pagefind
  github_repo: pagefind/pagefind
  github_stars: 5094
  npm_package: pagefind
  npm_weekly_downloads: 457937
  license: MIT
  maintained: true
---
# Pagefind Static Low-Bandwidth Search Engine

Pagefind is a static search library written in Rust that indexes your built site and adds a search bundle requiring no server infrastructure. It performs well on large sites while using minimal bandwidth.

## Overview

Pagefind is a fully static search library that aims to perform well on large sites while using as little bandwidth as possible and without requiring any hosted infrastructure. Originally created by Liam Bigelow at CloudCannon, Pagefind has become a popular choice for adding search to static sites with over 5,000 GitHub stars.

How It Works

Pagefind operates in two phases. First, you run the pagefind CLI against your built static site (the output directory of Hugo, Astro, Eleventy, Jekyll, or any other generator). It indexes all HTML pages, creating a compressed search index. Second, Pagefind adds a small JavaScript search bundle to your site that loads index fragments on demand as users type, keeping bandwidth low even for sites with thousands of pages.

Search Features

Pagefind supports full-text search with multilingual stemming, filtering by metadata attributes, sorting by custom data attributes, substring matching, and result highlighting. The search index is split into chunks, so only relevant portions are loaded for each query. A typical search uses under 100KB of bandwidth even on sites with tens of thousands of pages.

Prebuilt UI and JavaScript API

Pagefind ships with a prebuilt search UI component that can be dropped into any page with minimal configuration. For custom implementations, a JavaScript API allows programmatic search queries, result fetching, and filter management. Both approaches work without any server-side code.

Agent Integration

Agents can invoke the pagefind CLI to index a site after building (npx pagefind –site public), configure search behavior via data attributes in HTML, and integrate the search UI or API into page templates. Pagefind is installable via npm (npx pagefind) or as a standalone binary, and works with any static site generator that outputs HTML files.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill pagefind-static-low-bandwidth-search-engine
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill pagefind-static-low-bandwidth-search-engine -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill pagefind-static-low-bandwidth-search-engine -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill pagefind-static-low-bandwidth-search-engine -a codex
```

### OpenClaw

```bash
clawhub install pagefind-static-low-bandwidth-search-engine
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagefind-static-low-bandwidth-search-engine/)
