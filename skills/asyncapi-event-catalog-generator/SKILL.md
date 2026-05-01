---
title: "AsyncAPI Event Catalog Generator"
description: "Parses AsyncAPI 2.x/3.x specifications to generate event-driven architecture catalogs using the AsyncAPI Generator. Produces channel documentation, message schema validators, and EventBridge rule templates."
verification: "security_reviewed"
source: "https://www.asyncapi.com/"
category:
  - "Library & API Reference"
framework:
  - "Claude Code"
---

# AsyncAPI Event Catalog Generator

The AsyncAPI Event Catalog Generator skill processes AsyncAPI specification documents to create comprehensive event-driven architecture documentation and tooling. It parses AsyncAPI 2.6 and 3.0 specs using the asyncapi-parser library, extracting channel definitions, message schemas, and server bindings for Kafka, RabbitMQ, and MQTT protocols. The skill generates event catalog pages using the asyncapi-generator with html-template and markdown-template outputs, producing navigable documentation of all published and subscribed channels. It creates JSON Schema validators for each message payload using ajv with format validation and custom keywords, generates AWS EventBridge rule templates from channel filter patterns, and produces CloudEvents envelope wrappers for standardized event metadata. The generator also creates TypeScript interfaces for message types, produces channel topology diagrams in Mermaid format, and validates spec completeness against organizational standards for required fields like contact info and message examples.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/asyncapi-event-catalog-generator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/asyncapi-event-catalog-generator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/asyncapi-event-catalog-generator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/asyncapi-event-catalog-generator/)
