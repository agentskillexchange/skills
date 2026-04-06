---
name: "Schema Markup Generator for SEO"
description: "Generates JSON-LD structured data using schema-dts TypeScript definitions and Google Rich Results Test API validation. Supports Article, Product, FAQ, HowTo, and LocalBusiness schema types."
category: "Content Writing &amp; SEO"
framework: "Codex"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/schema-markup-generator-seo/"
---
# Schema Markup Generator for SEO

Generates JSON-LD structured data using schema-dts TypeScript definitions and Google Rich Results Test API validation. Supports Article, Product, FAQ, HowTo, and LocalBusiness schema types.

The Schema Markup Generator automates JSON-LD structured data creation using schema-dts TypeScript definitions for type-safe schema authoring. It generates valid Schema.org markup that passes Google Rich Results Test validation for enhanced search engine visibility.

The agent supports all major schema types including Article, Product, FAQ, HowTo, LocalBusiness, Event, Recipe, and Organization. It analyzes page content to automatically determine the appropriate schema type and populates required and recommended properties from existing page elements, meta tags, and Open Graph data.

Advanced features include nested schema generation with proper @id references for entity linking, automated breadcrumb markup from URL structure analysis, and aggregate rating schema from review data. The agent validates output against Google’s structured data guidelines, identifies missing recommended fields, and generates schema for multiple entities per page. It also supports dynamic schema injection via Google Tag Manager dataLayer events and server-side rendering integration.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill schema-markup-generator-seo
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill schema-markup-generator-seo -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill schema-markup-generator-seo -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill schema-markup-generator-seo -a codex
```

### OpenClaw

```bash
clawhub install schema-markup-generator-seo
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/schema-markup-generator-seo/)
