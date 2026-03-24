---
name: "jq JSON Stream Transformer"
description: "Constructs complex jq filter expressions for transforming JSON/NDJSON streams, including recursive descent, object construction, and reduce operations. Handles multi-gigabyte streams with jq’s streaming parser."
category: "Data Extraction & Transformation"
framework: "MCP-compatible"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/jq-json-stream-transformer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "aws"  # from ase_tool_match
  github_stars: 3594  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 9204385  # from ase_npm_downloads
  github_repo: "aws/aws-sdk-js-v3"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# jq JSON Stream Transformer

Constructs complex jq filter expressions for transforming JSON/NDJSON streams, including recursive descent, object construction, and reduce operations. Handles multi-gigabyte streams with jq’s streaming parser.

## Overview

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

- Marketplace: https://agentskillexchange.com/skills/jq-json-stream-transformer/
