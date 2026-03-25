---
name: "PuppeteerSharp Web Scraping Pipeline"
description: "Builds headless Chrome scraping pipelines using PuppeteerSharp for .NET environments. Handles JavaScript-rendered SPAs, Cloudflare challenge bypass via stealth plugins, and exports structured data through Newtonsoft.Json serialization."
category: "Research & Scraping"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/puppeteersharp-web-scraping-pipeline/"
tool_ecosystem:
  tool: "puppeteer"
  github_stars: 93932
  npm_weekly_downloads: 8696130
  github_repo: "puppeteer/puppeteer"
  license: "Apache-2.0"
  maintained: true
---

# PuppeteerSharp Web Scraping Pipeline

Builds headless Chrome scraping pipelines using PuppeteerSharp for .NET environments. Handles JavaScript-rendered SPAs, Cloudflare challenge bypass via stealth plugins, and exports structured data through Newtonsoft.Json serialization.

## Overview

The PuppeteerSharp Web Scraping Pipeline enables robust data extraction from modern JavaScript-heavy websites within .NET ecosystems. Built on PuppeteerSharp, the official .NET port of Google Puppeteer, it launches headless Chromium instances with configurable viewport sizes, user agent rotation, and proxy chain support.

The pipeline handles complex scraping scenarios including infinite scroll pagination, shadow DOM traversal, and iframe content extraction. Anti-detection measures include puppeteer-extra-plugin-stealth patterns adapted for PuppeteerSharp, randomized timing intervals, and residential proxy integration via Bright Data or Oxylabs APIs.

Data extraction uses CSS selectors and XPath queries with automatic retry logic for stale element references. Extracted data flows through a configurable transformation pipeline using Newtonsoft.Json for serialization and AutoMapper for DTO projection. Output destinations include SQL Server via Entity Framework Core, Elasticsearch bulk indexing, or Azure Blob Storage for large datasets. The pipeline supports distributed execution across multiple Chrome instances with work stealing task scheduling.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill puppeteersharp-web-scraping-pipeline
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill puppeteersharp-web-scraping-pipeline -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill puppeteersharp-web-scraping-pipeline -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill puppeteersharp-web-scraping-pipeline -a codex
```

### OpenClaw

```bash
clawhub install puppeteersharp-web-scraping-pipeline
```

## Source

- Marketplace: https://agentskillexchange.com/skills/puppeteersharp-web-scraping-pipeline/
