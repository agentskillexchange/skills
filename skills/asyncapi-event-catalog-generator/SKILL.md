---
name: "AsyncAPI Event Catalog Generator"
description: "Parses AsyncAPI 2.x/3.x specifications to generate event-driven architecture catalogs using the AsyncAPI Generator. Produces channel documentation, message schema validators, and EventBridge rule templates."
category: "Library & API Reference"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/asyncapi-event-catalog-generator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "kafka"  # from ase_tool_match
  github_stars: 3988  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 2396148  # from ase_npm_downloads
  github_repo: "tulios/kafkajs"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: false  # from ase_tool_maintained
---

# AsyncAPI Event Catalog Generator

Parses AsyncAPI 2.x/3.x specifications to generate event-driven architecture catalogs using the AsyncAPI Generator. Produces channel documentation, message schema validators, and EventBridge rule templates.

## Overview

The AsyncAPI Event Catalog Generator skill processes AsyncAPI specification documents to create comprehensive event-driven architecture documentation and tooling. It parses AsyncAPI 2.6 and 3.0 specs using the asyncapi-parser library, extracting channel definitions, message schemas, and server bindings for Kafka, RabbitMQ, and MQTT protocols. The skill generates event catalog pages using the asyncapi-generator with html-template and markdown-template outputs, producing navigable documentation of all published and subscribed channels. It creates JSON Schema validators for each message payload using ajv with format validation and custom keywords, generates AWS EventBridge rule templates from channel filter patterns, and produces CloudEvents envelope wrappers for standardized event metadata. The generator also creates TypeScript interfaces for message types, produces channel topology diagrams in Mermaid format, and validates spec completeness against organizational standards for required fields like contact info and message examples.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill asyncapi-event-catalog-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill asyncapi-event-catalog-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill asyncapi-event-catalog-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill asyncapi-event-catalog-generator -a codex
```

### OpenClaw

```bash
clawhub install asyncapi-event-catalog-generator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/asyncapi-event-catalog-generator/
