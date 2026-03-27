---
name: "Schema.org Markup Generator"
description: "Generates structured data markup using Schema.org vocabulary in JSON-LD format. Supports Article, Product, FAQPage, HowTo, and LocalBusiness schemas with Google Rich Results Test API validation."
category: "Content Writing & SEO"
framework: "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/schema-org-markup-generator-agent/"
---

# Schema.org Markup Generator

Generates structured data markup using Schema.org vocabulary in JSON-LD format. Supports Article, Product, FAQPage, HowTo, and LocalBusiness schemas with Google Rich Results Test API validation.

## Overview

Schema.org Markup Generator creates valid JSON-LD structured data for web pages following the Schema.org vocabulary specification. It analyzes page content and generates appropriate markup for types including `Article`, `Product`, `FAQPage`, `HowTo`, `LocalBusiness`, `BreadcrumbList`, and `VideoObject`.

The agent constructs nested schema objects with proper `@context`, `@type`, and `@id` references, handling multi-entity pages with `@graph` arrays. For Product schema, it includes `AggregateRating`, `Offer` with `priceValidUntil`, and `Review` markup meeting Google’s merchant listing requirements.

Validates generated markup against Google’s Rich Results Test API (`https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run`) and Schema.org’s official validator. Handles conditional properties like `isAccessibleForFree` for paywalled content and `speakable` for voice search optimization. Outputs ready-to-embed `<script type="application/ld+json">` blocks with proper escaping.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill schema-org-markup-generator-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill schema-org-markup-generator-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill schema-org-markup-generator-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill schema-org-markup-generator-agent -a codex
```

### OpenClaw

```bash
clawhub install schema-org-markup-generator-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/schema-org-markup-generator-agent/
