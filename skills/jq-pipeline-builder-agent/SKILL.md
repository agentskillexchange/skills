---
name: "jq Pipeline Builder Agent"
description: "Constructs complex jq filter pipelines from natural language queries against JSON/NDJSON data streams. Uses jq built-in functions including path expressions, reduce, and SQL-style operators."
category: "Data Extraction & Transformation"
framework: "Gemini"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/jq-pipeline-builder-agent/"
---

# jq Pipeline Builder Agent

Constructs complex jq filter pipelines from natural language queries against JSON/NDJSON data streams. Uses jq built-in functions including path expressions, reduce, and SQL-style operators.

## Overview

The jq Pipeline Builder Agent translates natural language data transformation requests into optimized jq filter expressions for processing JSON and NDJSON data streams. It leverages the full jq language including path expressions, recursive descent (..), reduce operators, SQL-style GROUP_BY and UNIQUE_BY, and string interpolation for template generation. The agent handles complex operations like cross-referencing multiple JSON files with input and slurp modes, building streaming parsers with –stream flag for memory-efficient processing of large files, and constructing conditional transformations with if-then-else and try-catch error handling. It generates reusable jq modules with import statements, supports custom function definitions via def, and produces shell-compatible one-liners for pipeline integration with curl, grep, and awk. Includes test case generation using jqplay-compatible formats.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill jq-pipeline-builder-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill jq-pipeline-builder-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill jq-pipeline-builder-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill jq-pipeline-builder-agent -a codex
```

### OpenClaw

```bash
clawhub install jq-pipeline-builder-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/jq-pipeline-builder-agent/
