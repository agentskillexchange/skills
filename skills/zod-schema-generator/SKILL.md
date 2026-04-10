---
title: "Zod Schema Generator"
description: "Converts JSON samples, TypeScript interfaces, and OpenAPI specs into Zod validation schemas. Uses ts-morph for AST parsing and zod-to-json-schema for bidirectional conversion."
slug: "zod-schema-generator"
category:
  - "Library &amp; API Reference"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/zod-schema-generator/"
listed: true
---

# Zod Schema Generator

Converts JSON samples, TypeScript interfaces, and OpenAPI specs into Zod validation schemas. Uses ts-morph for AST parsing and zod-to-json-schema for bidirectional conversion.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install zod-schema-generator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Zod Schema Generator automates the creation of Zod runtime validation schemas from multiple source formats. It accepts JSON sample data, TypeScript interface definitions, and OpenAPI 3.x specifications as input and produces idiomatic Zod schemas with proper type inference. Using ts-morph for TypeScript AST parsing, it reads interface and type alias definitions directly from .ts files, converting optional properties, union types, discriminated unions, and branded types into their Zod equivalents. For JSON samples, it infers types using json-schema-inferrer and maps them to Zod primitives with appropriate refinements for email, URL, UUID, and date-time patterns detected in sample values. The bidirectional conversion capability via zod-to-json-schema allows generating JSON Schema from existing Zod definitions for documentation or API specification purposes. The generator handles complex patterns including recursive types using z.lazy(), transform pipes with z.transform(), and custom error messages. It also generates companion TypeScript types using z.infer for each schema, eliminating type duplication.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/zod-schema-generator/)
