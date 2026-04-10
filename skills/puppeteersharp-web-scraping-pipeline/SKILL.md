---
name: PuppeteerSharp Web Scraping Pipeline
description: Builds headless Chrome scraping pipelines using PuppeteerSharp for .NET
  environments. Handles JavaScript-rendered SPAs, Cloudflare challenge bypass via
  stealth plugins, and exports structured data through Newtonsoft.Json serialization.
verification: security_reviewed
source: https://agentskillexchange.com/skills/puppeteersharp-web-scraping-pipeline/
category:
- Research &amp; Scraping
framework:
- Claude Code
---
# PuppeteerSharp Web Scraping Pipeline

The PuppeteerSharp Web Scraping Pipeline enables robust data extraction from modern JavaScript-heavy websites within .NET ecosystems. Built on PuppeteerSharp, the official .NET port of Google Puppeteer, it launches headless Chromium instances with configurable viewport sizes, user agent rotation, and proxy chain support.
The pipeline handles complex scraping scenarios including infinite scroll pagination, shadow DOM traversal, and iframe content extraction. Anti-detection measures include puppeteer-extra-plugin-stealth patterns adapted for PuppeteerSharp, randomized timing intervals, and residential proxy integration via Bright Data or Oxylabs APIs.
Data extraction uses CSS selectors and XPath queries with automatic retry logic for stale element references. Extracted data flows through a configurable transformation pipeline using Newtonsoft.Json for serialization and AutoMapper for DTO projection. Output destinations include SQL Server via Entity Framework Core, Elasticsearch bulk indexing, or Azure Blob Storage for large datasets. The pipeline supports distributed execution across multiple Chrome instances with work stealing task scheduling.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteersharp-web-scraping-pipeline/)
