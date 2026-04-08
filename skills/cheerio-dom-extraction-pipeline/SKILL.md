---
title: Cheerio DOM Extraction Pipeline
description: 'The Cheerio DOM Extraction Pipeline enables high-performance structured
  data extraction from HTML without browser overhead. Using Cheerio’s jQuery-like
  API for server-side DOM manipulation, it processes HTML documents at thousands of
  pages per second with minimal memory footprint. Extraction rules are defined as
  CSS selector chains with optional attribute extraction, text normalization, and
  regex post-processing. The pipeline supports nested data structures through recursive
  selector evaluation, handling complex layouts like product listings with variant
  tables, review threads, and paginated comment sections. Output mapping uses JSONPath
  expressions to transform extracted arrays into structured JSON objects matching
  target schemas. Schema validation is performed using Ajv (Another JSON Schema Validator)
  with custom format validators for common data types like prices, dates, URLs, and
  phone numbers. Pagination handling supports multiple strategies: next-page link
  following, URL pattern increment, infinite scroll simulation via API endpoint detection,
  and cursor-based pagination. Rate limiting is built in with configurable delays
  and concurrent request limits using p-queue.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/cheerio-dom-extraction-pipeline/
category:
- Data Extraction &amp; Transformation
framework:
- Codex
---

# Cheerio DOM Extraction Pipeline

The Cheerio DOM Extraction Pipeline enables high-performance structured data extraction from HTML without browser overhead. Using Cheerio’s jQuery-like API for server-side DOM manipulation, it processes HTML documents at thousands of pages per second with minimal memory footprint. Extraction rules are defined as CSS selector chains with optional attribute extraction, text normalization, and regex post-processing. The pipeline supports nested data structures through recursive selector evaluation, handling complex layouts like product listings with variant tables, review threads, and paginated comment sections. Output mapping uses JSONPath expressions to transform extracted arrays into structured JSON objects matching target schemas. Schema validation is performed using Ajv (Another JSON Schema Validator) with custom format validators for common data types like prices, dates, URLs, and phone numbers. Pagination handling supports multiple strategies: next-page link following, URL pattern increment, infinite scroll simulation via API endpoint detection, and cursor-based pagination. Rate limiting is built in with configurable delays and concurrent request limits using p-queue.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cheerio-dom-extraction-pipeline/)
