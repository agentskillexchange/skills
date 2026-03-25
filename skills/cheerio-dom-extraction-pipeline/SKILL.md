---
name: "Cheerio DOM Extraction Pipeline"
description: "Builds configurable data extraction pipelines using Cheerio for server-side DOM parsing with CSS selector chains. Supports JSONPath output mapping, pagination following, and schema validation via Ajv."
category: "Data Extraction & Transformation"
framework: "Codex"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/cheerio-dom-extraction-pipeline/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "cheerio"  # from ase_tool_match
  github_stars: 30229  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 18512628  # from ase_npm_downloads
  github_repo: "cheeriojs/cheerio"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Cheerio DOM Extraction Pipeline

Builds configurable data extraction pipelines using Cheerio for server-side DOM parsing with CSS selector chains. Supports JSONPath output mapping, pagination following, and schema validation via Ajv.

## Overview

The Cheerio DOM Extraction Pipeline enables high-performance structured data extraction from HTML without browser overhead. Using Cheerio’s jQuery-like API for server-side DOM manipulation, it processes HTML documents at thousands of pages per second with minimal memory footprint.

Extraction rules are defined as CSS selector chains with optional attribute extraction, text normalization, and regex post-processing. The pipeline supports nested data structures through recursive selector evaluation, handling complex layouts like product listings with variant tables, review threads, and paginated comment sections.

Output mapping uses JSONPath expressions to transform extracted arrays into structured JSON objects matching target schemas. Schema validation is performed using Ajv (Another JSON Schema Validator) with custom format validators for common data types like prices, dates, URLs, and phone numbers.

Pagination handling supports multiple strategies: next-page link following, URL pattern increment, infinite scroll simulation via API endpoint detection, and cursor-based pagination. Rate limiting is built in with configurable delays and concurrent request limits using p-queue.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill cheerio-dom-extraction-pipeline
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill cheerio-dom-extraction-pipeline -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill cheerio-dom-extraction-pipeline -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill cheerio-dom-extraction-pipeline -a codex
```

### OpenClaw

```bash
clawhub install cheerio-dom-extraction-pipeline
```

## Source

- Marketplace: https://agentskillexchange.com/skills/cheerio-dom-extraction-pipeline/
