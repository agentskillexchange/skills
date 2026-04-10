---
title: "Cheerio DOM Extraction Pipeline"
description: "Builds configurable data extraction pipelines using Cheerio for server-side DOM parsing with CSS selector chains. Supports JSONPath output mapping, pagination following, and schema validation via Ajv."
slug: "cheerio-dom-extraction-pipeline"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Codex"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/cheerio-dom-extraction-pipeline/"
---

# Cheerio DOM Extraction Pipeline

Builds configurable data extraction pipelines using Cheerio for server-side DOM parsing with CSS selector chains. Supports JSONPath output mapping, pagination following, and schema validation via Ajv.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install cheerio-dom-extraction-pipeline
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Cheerio DOM Extraction Pipeline enables high-performance structured data extraction from HTML without browser overhead. Using Cheerio’s jQuery-like API for server-side DOM manipulation, it processes HTML documents at thousands of pages per second with minimal memory footprint.
Extraction rules are defined as CSS selector chains with optional attribute extraction, text normalization, and regex post-processing. The pipeline supports nested data structures through recursive selector evaluation, handling complex layouts like product listings with variant tables, review threads, and paginated comment sections.
Output mapping uses JSONPath expressions to transform extracted arrays into structured JSON objects matching target schemas. Schema validation is performed using Ajv (Another JSON Schema Validator) with custom format validators for common data types like prices, dates, URLs, and phone numbers.
Pagination handling supports multiple strategies: next-page link following, URL pattern increment, infinite scroll simulation via API endpoint detection, and cursor-based pagination. Rate limiting is built in with configurable delays and concurrent request limits using p-queue.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cheerio-dom-extraction-pipeline/)
