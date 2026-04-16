---
title: "Zod Schema Generator"
description: "Converts JSON samples, TypeScript interfaces, and OpenAPI specs into Zod validation schemas. Uses ts-morph for AST parsing and zod-to-json-schema for bidirectional conversion."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/zod-schema-generator/"
category:
  - "Library &amp; API Reference"
framework:
  - "Cursor"
---

# Zod Schema Generator

The Zod Schema Generator automates the creation of Zod runtime validation schemas from multiple source formats. It accepts JSON sample data, TypeScript interface definitions, and OpenAPI 3.x specifications as input and produces idiomatic Zod schemas with proper type inference. Using ts-morph for TypeScript AST parsing, it reads interface and type alias definitions directly from .ts files, converting optional properties, union types, discriminated unions, and branded types into their Zod equivalents. For JSON samples, it infers types using json-schema-inferrer and maps them to Zod primitives with appropriate refinements for email, URL, UUID, and date-time patterns detected in sample values. The bidirectional conversion capability via zod-to-json-schema allows generating JSON Schema from existing Zod definitions for documentation or API specification purposes. The generator handles complex patterns including recursive types using z.lazy(), transform pipes with z.transform(), and custom error messages. It also generates companion TypeScript types using z.infer for each schema, eliminating type duplication.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/zod-schema-generator/)
