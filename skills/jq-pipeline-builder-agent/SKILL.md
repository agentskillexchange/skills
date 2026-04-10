---
title: "jq Pipeline Builder Agent"
description: "Constructs complex jq filter pipelines from natural language queries against JSON/NDJSON data streams. Uses jq built-in functions including path expressions, reduce, and SQL-style operators."
slug: "jq-pipeline-builder-agent"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/jq-pipeline-builder-agent/"
listed: true
---

# jq Pipeline Builder Agent

Constructs complex jq filter pipelines from natural language queries against JSON/NDJSON data streams. Uses jq built-in functions including path expressions, reduce, and SQL-style operators.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install jq-pipeline-builder-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The jq Pipeline Builder Agent translates natural language data transformation requests into optimized jq filter expressions for processing JSON and NDJSON data streams. It leverages the full jq language including path expressions, recursive descent (..), reduce operators, SQL-style GROUP_BY and UNIQUE_BY, and string interpolation for template generation. The agent handles complex operations like cross-referencing multiple JSON files with input and slurp modes, building streaming parsers with –stream flag for memory-efficient processing of large files, and constructing conditional transformations with if-then-else and try-catch error handling. It generates reusable jq modules with import statements, supports custom function definitions via def, and produces shell-compatible one-liners for pipeline integration with curl, grep, and awk. Includes test case generation using jqplay-compatible formats.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jq-pipeline-builder-agent/)
