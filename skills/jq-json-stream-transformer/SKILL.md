---
title: jq JSON Stream Transformer
description: 'The jq JSON Stream Transformer skill generates and optimizes jq filter
  expressions for complex JSON data transformations. It handles common patterns including
  nested object restructuring, array aggregation, conditional filtering, and cross-referencing
  between JSON documents using jq’s input and inputs functions. The skill constructs
  jq programs using advanced features: recursive descent (..), try-catch for error
  handling, reduce for stateful aggregation, label-break for early termination, and
  custom function definitions via def. It optimizes filter chains to minimize memory
  usage and leverages jq’s streaming parser (–stream flag) for processing multi-gigabyte
  JSON files. Key capabilities include NDJSON (newline-delimited JSON) processing
  for log analysis, JSON-to-CSV conversion with configurable column mapping, and schema-aware
  transformations that preserve type information. The skill generates shell pipeline
  integrations combining jq with curl, aws-cli, and kubectl for API response processing,
  and produces annotated jq programs with comments explaining each transformation
  step.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/jq-json-stream-transformer/
category:
- Data Extraction &amp; Transformation
framework:
- MCP
---

# jq JSON Stream Transformer

The jq JSON Stream Transformer skill generates and optimizes jq filter expressions for complex JSON data transformations. It handles common patterns including nested object restructuring, array aggregation, conditional filtering, and cross-referencing between JSON documents using jq’s input and inputs functions. The skill constructs jq programs using advanced features: recursive descent (..), try-catch for error handling, reduce for stateful aggregation, label-break for early termination, and custom function definitions via def. It optimizes filter chains to minimize memory usage and leverages jq’s streaming parser (–stream flag) for processing multi-gigabyte JSON files. Key capabilities include NDJSON (newline-delimited JSON) processing for log analysis, JSON-to-CSV conversion with configurable column mapping, and schema-aware transformations that preserve type information. The skill generates shell pipeline integrations combining jq with curl, aws-cli, and kubectl for API response processing, and produces annotated jq programs with comments explaining each transformation step.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jq-json-stream-transformer/)
