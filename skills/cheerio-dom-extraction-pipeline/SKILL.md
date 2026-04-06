---
name: "Cheerio DOM Extraction Pipeline"
description: "Builds configurable data extraction pipelines using Cheerio for server-side DOM parsing with CSS selector chains. Supports JSONPath output mapping, pagination following, and schema validation via Ajv."
category: "Data Extraction &amp; Transformation"
framework: "Codex"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/cheerio-dom-extraction-pipeline/"
---
# Cheerio DOM Extraction Pipeline

Builds configurable data extraction pipelines using Cheerio for server-side DOM parsing with CSS selector chains. Supports JSONPath output mapping, pagination following, and schema validation via Ajv.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cheerio-dom-extraction-pipeline/)
