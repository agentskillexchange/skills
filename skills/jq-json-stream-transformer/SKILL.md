---
title: "jq JSON Stream Transformer"
description: "Constructs complex jq filter expressions for transforming JSON/NDJSON streams, including recursive descent, object construction, and reduce operations. Handles multi-gigabyte streams with jq’s streaming parser."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/jq-json-stream-transformer/"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "MCP"
---

# jq JSON Stream Transformer

The jq JSON Stream Transformer skill generates and optimizes jq filter expressions for complex JSON data transformations. It handles common patterns including nested object restructuring, array aggregation, conditional filtering, and cross-referencing between JSON documents using jq’s input and inputs functions.

The skill constructs jq programs using advanced features: recursive descent (..), try-catch for error handling, reduce for stateful aggregation, label-break for early termination, and custom function definitions via def. It optimizes filter chains to minimize memory usage and leverages jq’s streaming parser (–stream flag) for processing multi-gigabyte JSON files.

Key capabilities include NDJSON (newline-delimited JSON) processing for log analysis, JSON-to-CSV conversion with configurable column mapping, and schema-aware transformations that preserve type information. The skill generates shell pipeline integrations combining jq with curl, aws-cli, and kubectl for API response processing, and produces annotated jq programs with comments explaining each transformation step.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jq-json-stream-transformer/)
