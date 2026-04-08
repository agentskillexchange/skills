---
title: AsyncAPI Event Catalog Generator
description: The AsyncAPI Event Catalog Generator skill processes AsyncAPI specification
  documents to create comprehensive event-driven architecture documentation and tooling.
  It parses AsyncAPI 2.6 and 3.0 specs using the asyncapi-parser library, extracting
  channel definitions, message schemas, and server bindings for Kafka, RabbitMQ, and
  MQTT protocols. The skill generates event catalog pages using the asyncapi-generator
  with html-template and markdown-template outputs, producing navigable documentation
  of all published and subscribed channels. It creates JSON Schema validators for
  each message payload using ajv with format validation and custom keywords, generates
  AWS EventBridge rule templates from channel filter patterns, and produces CloudEvents
  envelope wrappers for standardized event metadata. The generator also creates TypeScript
  interfaces for message types, produces channel topology diagrams in Mermaid format,
  and validates spec completeness against organizational standards for required fields
  like contact info and message examples.
verification: security_reviewed
source: https://agentskillexchange.com/skills/asyncapi-event-catalog-generator/
category:
- Library &amp; API Reference
framework:
- Claude Code
---

# AsyncAPI Event Catalog Generator

The AsyncAPI Event Catalog Generator skill processes AsyncAPI specification documents to create comprehensive event-driven architecture documentation and tooling. It parses AsyncAPI 2.6 and 3.0 specs using the asyncapi-parser library, extracting channel definitions, message schemas, and server bindings for Kafka, RabbitMQ, and MQTT protocols. The skill generates event catalog pages using the asyncapi-generator with html-template and markdown-template outputs, producing navigable documentation of all published and subscribed channels. It creates JSON Schema validators for each message payload using ajv with format validation and custom keywords, generates AWS EventBridge rule templates from channel filter patterns, and produces CloudEvents envelope wrappers for standardized event metadata. The generator also creates TypeScript interfaces for message types, produces channel topology diagrams in Mermaid format, and validates spec completeness against organizational standards for required fields like contact info and message examples.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/asyncapi-event-catalog-generator/)
