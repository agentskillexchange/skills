---
name: schema-dts TypeScript Types for Schema.org Structured Data
description: An agent skill built on schema-dts by Google, which provides complete
  TypeScript type definitions for the Schema.org vocabulary. Enables type-safe generation
  and validation of JSON-LD structured data markup for SEO, rich search results, and
  knowledge graph integration.
category: "Content Writing &amp; SEO"
framework: Custom Agents
verification: security_reviewed
source: "https://github.com/google/schema-dts"
tool_ecosystem:
  github_repo: "https://github.com/google/schema-dts"
  github_stars: 1164
  npm_package: schema-dts
  npm_weekly_downloads: 1490370
---
# schema-dts TypeScript Types for Schema.org Structured Data

An agent skill built on schema-dts by Google, which provides complete TypeScript type definitions for the Schema.org vocabulary. Enables type-safe generation and validation of JSON-LD structured data markup for SEO, rich search results, and knowledge graph integration.

schema-dts is an open-source npm package maintained by Google that provides comprehensive TypeScript type definitions for the entire Schema.org vocabulary. With over 1,100 GitHub stars and 35 published versions, it is the standard library for type-safe structured data generation in the TypeScript/JavaScript ecosystem.

What It Does

The package auto-generates TypeScript interfaces from the official Schema.org ontology releases. Every Schema.org type — Article, Product, Organization, Event, Recipe, FAQPage, HowTo, BreadcrumbList, and hundreds more — gets a corresponding TypeScript interface with all properties correctly typed. This means your IDE provides autocomplete, and the TypeScript compiler catches invalid structured data at build time rather than in production.

JSON-LD Generation

schema-dts is designed specifically for JSON-LD output, the format recommended by Google for structured data. Import the types, construct your structured data objects with full type checking, and serialize to JSON-LD for embedding in HTML <script type="application/ld+json"> tags. The library handles the @context, @type, and @id properties correctly.

SEO and Rich Results

Properly structured data is essential for Google Rich Results, knowledge panels, and AI-powered search features. schema-dts ensures your markup conforms to the Schema.org specification, reducing validation errors in Google’s Rich Results Test and Schema Markup Validator. Common use cases include Article markup for blog posts, Product markup for e-commerce, FAQ markup for help pages, and Organization markup for brand identity.

Usage

Install with npm install schema-dts. Import types like import type { Article, WithContext } from 'schema-dts'. The WithContext wrapper type adds the required @context property. Build your structured data object, and TypeScript will validate every property name and value type against the Schema.org specification.

Integration Points

schema-dts integrates with Next.js, Nuxt, Gatsby, Astro, and any TypeScript project. It pairs well with next-seo for Next.js applications and can be used in build pipelines to generate and validate structured data at compile time. The package is licensed under Apache-2.0 and receives regular updates tracking new Schema.org releases.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill schema-dts-typescript-types-schemaorg-structured-data
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill schema-dts-typescript-types-schemaorg-structured-data -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill schema-dts-typescript-types-schemaorg-structured-data -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill schema-dts-typescript-types-schemaorg-structured-data -a codex
```

### OpenClaw

```bash
clawhub install schema-dts-typescript-types-schemaorg-structured-data
```


## Source

- [GitHub](https://github.com/google/schema-dts)
