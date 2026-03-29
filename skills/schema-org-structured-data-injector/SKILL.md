---
name: "Schema.org Structured Data Injector"
description: "Generates and validates JSON-LD structured data markup for articles, products, FAQs, and HowTo content types following Schema.org specifications. Integrates with Google’s Rich Results Test API and validates against the Schema.org vocabulary using the sdtt validator."
category: "Content Writing & SEO"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/schema-org-structured-data-injector/"
tool_ecosystem:
  tool: wordpress
  github_stars: 20976
  github_repo: WordPress/WordPress
  maintained: true
---
# Schema.org Structured Data Injector

Generates and validates JSON-LD structured data markup for articles, products, FAQs, and HowTo content types following Schema.org specifications. Integrates with Google’s Rich Results Test API and validates against the Schema.org vocabulary using the sdtt validator.

## Overview

Schema.org Structured Data Injector automates the creation and validation of JSON-LD markup for improved search engine visibility. It analyzes page content to determine the appropriate Schema.org type — Article, Product, FAQPage, HowTo, Recipe, or LocalBusiness — and generates compliant JSON-LD blocks with proper @context and @type declarations.

The injector pulls content signals from HTML heading structure, product metadata, Q&A patterns, and step-by-step instructions to populate schema properties. For Article types, it extracts author, datePublished, dateModified, and headline. Product schemas include offers with price, priceCurrency, and availability from structured product pages. FAQ schemas detect question-answer pairs from accordion or definition list markup.

Validation runs through Google’s Rich Results Test API endpoint and the Schema.org validator to catch missing required properties, incorrect value types, and deprecated markup patterns. The tool outputs both the JSON-LD snippet for manual insertion and a WordPress-compatible wp_head action hook implementation using wp_json_encode() for dynamic injection. Batch processing handles entire sitemaps by crawling URLs and generating schema for each page type.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill schema-org-structured-data-injector
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill schema-org-structured-data-injector -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill schema-org-structured-data-injector -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill schema-org-structured-data-injector -a codex
```

### OpenClaw

```bash
clawhub install schema-org-structured-data-injector
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/schema-org-structured-data-injector/)
