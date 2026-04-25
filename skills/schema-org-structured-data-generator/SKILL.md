---
title: "Schema.org Structured Data Generator"
description: "Generates JSON-LD structured data markup for articles, products, FAQs, and how-to pages using Schema.org vocabulary. Validates output against Google Rich Results Test API and SchemaValidator.org endpoints."
verification: "security_reviewed"
source: "https://github.com/schemaorg/schemaorg"
category:
  - "Content Writing & SEO"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "schemaorg/schemaorg"
  github_stars: 6017
---

# Schema.org Structured Data Generator

This skill automatically generates valid JSON-LD structured data markup following the Schema.org vocabulary for SEO-critical page types. It supports multiple schema types: Article (with author, datePublished, dateModified, publisher), Product (with offers, aggregateRating, review), FAQPage (with mainEntity Question/Answer pairs), HowTo (with step, tool, supply, totalTime), BreadcrumbList (with itemListElement), and LocalBusiness (with address, geo, openingHours). The skill analyzes page content to extract relevant entities and properties, populating schema fields from existing HTML elements using CSS selectors or natural language extraction. For e-commerce pages, it generates Product schema with Offer properties including price, priceCurrency, availability (InStock/OutOfStock/PreOrder), and priceValidUntil. The FAQ schema generator parses content for question patterns and generates compliant FAQPage markup with proper mainEntity arrays. Validation runs against two endpoints: Google’s Rich Results Test API (POST to https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run) and Schema.org’s validator. The skill outputs minified JSON-LD wrapped in

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/schema-org-structured-data-generator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/schema-org-structured-data-generator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/schema-org-structured-data-generator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/schema-org-structured-data-generator/)
