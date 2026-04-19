---
title: "Cheerio DOM Extraction Pipeline"
description: "The Cheerio DOM Extraction Pipeline enables high-performance structured data extraction from HTML without browser overhead. Using Cheerio&#8217;s jQuery-like API for server-side DOM manipulation, it processes HTML documents at thousands of pages per second with minimal memory footprint. Extraction rules are defined as CSS selector chains with optional attribute extraction, text normalization, and regex post-processing. The pipeline supports nested data structures through recursive selector evaluation, handling complex layouts like product listings with variant tables, review threads, and paginated comment sections. Output mapping uses JSONPath expressions to transform extracted arrays into structured JSON objects matching target schemas. Schema validation is performed using Ajv (Another JSON Schema Validator) with custom format validators for common data types like prices, dates, URLs, and phone numbers. Pagination handling supports multiple strategies: next-page link following, URL pattern increment, infinite scroll simulation via API endpoint detection, and cursor-based pagination. Rate limiting is built in with configurable delays and concurrent request limits using p-queue."
source: "https://github.com/cheeriojs/cheerio"
verification: "security_reviewed"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "cheeriojs/cheerio"
  github_stars: 30270
  npm_package: "cheerio"
  npm_weekly_downloads: 19621708
---

# Cheerio DOM Extraction Pipeline

The Cheerio DOM Extraction Pipeline enables high-performance structured data extraction from HTML without browser overhead. Using Cheerio&#8217;s jQuery-like API for server-side DOM manipulation, it processes HTML documents at thousands of pages per second with minimal memory footprint. Extraction rules are defined as CSS selector chains with optional attribute extraction, text normalization, and regex post-processing. The pipeline supports nested data structures through recursive selector evaluation, handling complex layouts like product listings with variant tables, review threads, and paginated comment sections. Output mapping uses JSONPath expressions to transform extracted arrays into structured JSON objects matching target schemas. Schema validation is performed using Ajv (Another JSON Schema Validator) with custom format validators for common data types like prices, dates, URLs, and phone numbers. Pagination handling supports multiple strategies: next-page link following, URL pattern increment, infinite scroll simulation via API endpoint detection, and cursor-based pagination. Rate limiting is built in with configurable delays and concurrent request limits using p-queue.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cheerio-dom-extraction-pipeline/)
