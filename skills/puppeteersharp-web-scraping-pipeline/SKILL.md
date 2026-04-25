---
title: "PuppeteerSharp Web Scraping Pipeline"
description: "Builds headless Chrome scraping pipelines using PuppeteerSharp for .NET environments. Handles JavaScript-rendered SPAs, Cloudflare challenge bypass via stealth plugins, and exports structured data through Newtonsoft.Json serialization."
verification: "security_reviewed"
source: "https://github.com/hardkoded/puppeteer-sharp"
category:
  - "Research & Scraping"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "hardkoded/puppeteer-sharp"
  github_stars: 3879
---

# PuppeteerSharp Web Scraping Pipeline

The PuppeteerSharp Web Scraping Pipeline enables robust data extraction from modern JavaScript-heavy websites within .NET ecosystems. Built on PuppeteerSharp, the official .NET port of Google Puppeteer, it launches headless Chromium instances with configurable viewport sizes, user agent rotation, and proxy chain support.

The pipeline handles complex scraping scenarios including infinite scroll pagination, shadow DOM traversal, and iframe content extraction. Anti-detection measures include puppeteer-extra-plugin-stealth patterns adapted for PuppeteerSharp, randomized timing intervals, and residential proxy integration via Bright Data or Oxylabs APIs.

Data extraction uses CSS selectors and XPath queries with automatic retry logic for stale element references. Extracted data flows through a configurable transformation pipeline using Newtonsoft.Json for serialization and AutoMapper for DTO projection. Output destinations include SQL Server via Entity Framework Core, Elasticsearch bulk indexing, or Azure Blob Storage for large datasets. The pipeline supports distributed execution across multiple Chrome instances with work stealing task scheduling.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/puppeteersharp-web-scraping-pipeline/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/puppeteersharp-web-scraping-pipeline
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/puppeteersharp-web-scraping-pipeline`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteersharp-web-scraping-pipeline/)
