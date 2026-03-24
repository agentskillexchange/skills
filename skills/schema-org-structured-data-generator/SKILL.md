---
name: "Schema.org Structured Data Generator"
description: "Generates JSON-LD structured data markup for articles, products, FAQs, and how-to pages using Schema.org vocabulary. Validates output against Google Rich Results Test API and SchemaValidator.org endpoints."
category: "Content Writing & SEO"
framework: "Gemini"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/schema-org-structured-data-generator/"
---

# Schema.org Structured Data Generator

Generates JSON-LD structured data markup for articles, products, FAQs, and how-to pages using Schema.org vocabulary. Validates output against Google Rich Results Test API and SchemaValidator.org endpoints.

## Overview

This skill automatically generates valid JSON-LD structured data markup following the Schema.org vocabulary for SEO-critical page types. It supports multiple schema types: Article (with author, datePublished, dateModified, publisher), Product (with offers, aggregateRating, review), FAQPage (with mainEntity Question/Answer pairs), HowTo (with step, tool, supply, totalTime), BreadcrumbList (with itemListElement), and LocalBusiness (with address, geo, openingHours). The skill analyzes page content to extract relevant entities and properties, populating schema fields from existing HTML elements using CSS selectors or natural language extraction. For e-commerce pages, it generates Product schema with Offer properties including price, priceCurrency, availability (InStock/OutOfStock/PreOrder), and priceValidUntil. The FAQ schema generator parses content for question patterns and generates compliant FAQPage markup with proper mainEntity arrays. Validation runs against two endpoints: Google’s Rich Results Test API (POST to https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run) and Schema.org’s validator. The skill outputs minified JSON-LD wrapped in

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill schema-org-structured-data-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill schema-org-structured-data-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill schema-org-structured-data-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill schema-org-structured-data-generator -a codex
```

### OpenClaw

```bash
clawhub install schema-org-structured-data-generator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/schema-org-structured-data-generator/
