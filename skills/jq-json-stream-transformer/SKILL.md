---
title: "jq JSON Stream Transformer"
description: "Constructs complex jq filter expressions for transforming JSON/NDJSON streams, including recursive descent, object construction, and reduce operations. Handles multi-gigabyte streams with jq’s streaming parser."
verification: "security_reviewed"
source: "https://github.com/jqlang/jq"
category:
  - "Data Extraction & Transformation"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "jqlang/jq"
  github_stars: 34478
---

# jq JSON Stream Transformer

The jq JSON Stream Transformer skill generates and optimizes jq filter expressions for complex JSON data transformations. It handles common patterns including nested object restructuring, array aggregation, conditional filtering, and cross-referencing between JSON documents using jq’s input and inputs functions. The skill constructs jq programs using advanced features: recursive descent (..), try-catch for error handling, reduce for stateful aggregation, label-break for early termination, and custom function definitions via def. It optimizes filter chains to minimize memory usage and leverages jq’s streaming parser (–stream flag) for processing multi-gigabyte JSON files. Key capabilities include NDJSON (newline-delimited JSON) processing for log analysis, JSON-to-CSV conversion with configurable column mapping, and schema-aware transformations that preserve type information. The skill generates shell pipeline integrations combining jq with curl, aws-cli, and kubectl for API response processing, and produces annotated jq programs with comments explaining each transformation step.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/jq-json-stream-transformer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/jq-json-stream-transformer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/jq-json-stream-transformer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jq-json-stream-transformer/)
