---
name: OpenAPI Spec Navigator
description: Parses and navigates OpenAPI 3.1 specifications using swagger-parser
  and @apidevtools/json-schema-ref-parser. Resolves $ref chains, extracts endpoint
  signatures, and generates typed client stubs.
verification: security_reviewed
source: https://agentskillexchange.com/skills/openapi-spec-navigator/
category:
- Library &amp; API Reference
framework:
- Cursor
---
# OpenAPI Spec Navigator

The OpenAPI Spec Navigator skill provides intelligent traversal and analysis of OpenAPI 3.1 specification documents. It uses swagger-parser for spec validation and dereferencing, @apidevtools/json-schema-ref-parser for resolving complex $ref chains including circular references, and generates comprehensive endpoint documentation from path items and operation objects.
The skill extracts complete endpoint signatures including HTTP methods, path parameters with style/explode serialization rules, query parameter schemas with allowReserved handling, and request body content type negotiation. It resolves discriminator-based polymorphic schemas with oneOf/anyOf compositions and generates TypeScript type definitions using json-schema-to-typescript.
Advanced capabilities include security scheme analysis for OAuth2 flows (authorizationCode, clientCredentials, implicit), API key placement detection (header, query, cookie), and server variable template resolution. The skill generates client stubs compatible with axios and node-fetch, handles pagination patterns (cursor, offset, keyset) from x-pagination extensions, and produces Postman collection exports via openapi-to-postmanv2 for interactive testing.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openapi-spec-navigator/)
