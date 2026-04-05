---
name: "jq JSON Stream Transformer"
description: "Constructs complex jq filter expressions for transforming JSON/NDJSON streams, including recursive descent, object construction, and reduce operations. Handles multi-gigabyte streams with jq’s streaming parser."
category: "Data Extraction & Transformation"
framework: "MCP"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/jq-json-stream-transformer/"
---
# jq JSON Stream Transformer

Constructs complex jq filter expressions for transforming JSON/NDJSON streams, including recursive descent, object construction, and reduce operations. Handles multi-gigabyte streams with jq’s streaming parser.

The jq JSON Stream Transformer skill generates and optimizes jq filter expressions for complex JSON data transformations. It handles common patterns including nested object restructuring, array aggregation, conditional filtering, and cross-referencing between JSON documents using jq’s input and inputs functions.



The skill constructs jq programs using advanced features: recursive descent (..), try-catch for error handling, reduce for stateful aggregation, label-break for early termination, and custom function definitions via def. It optimizes filter chains to minimize memory usage and leverages jq’s streaming parser (–stream flag) for processing multi-gigabyte JSON files.



Key capabilities include NDJSON (newline-delimited JSON) processing for log analysis, JSON-to-CSV conversion with configurable column mapping, and schema-aware transformations that preserve type information. The skill generates shell pipeline integrations combining jq with curl, aws-cli, and kubectl for API response processing, and produces annotated jq programs with comments explaining each transformation step.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill jq-json-stream-transformer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill jq-json-stream-transformer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill jq-json-stream-transformer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill jq-json-stream-transformer -a codex
```

### OpenClaw

```bash
clawhub install jq-json-stream-transformer
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jq-json-stream-transformer/)
