---
title: "Cheerio DOM Extraction Pipeline"
description: "Builds configurable data extraction pipelines using Cheerio for server-side DOM parsing with CSS selector chains. Supports JSONPath output mapping, pagination following, and schema validation via Ajv."
verification: security_reviewed
source: "https://github.com/cheeriojs/cheerio"
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

The Cheerio DOM Extraction Pipeline enables high-performance structured data extraction from HTML without browser overhead. Using Cheerio’s jQuery-like API for server-side DOM manipulation, it processes HTML documents at thousands of pages per second with minimal memory footprint.

Extraction rules are defined as CSS selector chains with optional attribute extraction, text normalization, and regex post-processing. The pipeline supports nested data structures through recursive selector evaluation, handling complex layouts like product listings with variant tables, review threads, and paginated comment sections.

Output mapping uses JSONPath expressions to transform extracted arrays into structured JSON objects matching target schemas. Schema validation is performed using Ajv (Another JSON Schema Validator) with custom format validators for common data types like prices, dates, URLs, and phone numbers.

Pagination handling supports multiple strategies: next-page link following, URL pattern increment, infinite scroll simulation via API endpoint detection, and cursor-based pagination. Rate limiting is built in with configurable delays and concurrent request limits using p-queue.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cheerio-dom-extraction-pipeline/)
