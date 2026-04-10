---
name: AsyncAPI Event Catalog Generator
description: Parses AsyncAPI 2.x/3.x specifications to generate event-driven architecture
  catalogs using the AsyncAPI Generator. Produces channel documentation, message schema
  validators, and EventBridge rule templates.
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

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/asyncapi-event-catalog-generator/)
