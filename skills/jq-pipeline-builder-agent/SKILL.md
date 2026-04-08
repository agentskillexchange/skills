---
title: jq Pipeline Builder Agent
description: The jq Pipeline Builder Agent translates natural language data transformation
  requests into optimized jq filter expressions for processing JSON and NDJSON data
  streams. It leverages the full jq language including path expressions, recursive
  descent (..), reduce operators, SQL-style GROUP_BY and UNIQUE_BY, and string interpolation
  for template generation. The agent handles complex operations like cross-referencing
  multiple JSON files with input and slurp modes, building streaming parsers with
  –stream flag for memory-efficient processing of large files, and constructing conditional
  transformations with if-then-else and try-catch error handling. It generates reusable
  jq modules with import statements, supports custom function definitions via def,
  and produces shell-compatible one-liners for pipeline integration with curl, grep,
  and awk. Includes test case generation using jqplay-compatible formats.
verification: security_reviewed
source: https://agentskillexchange.com/skills/jq-pipeline-builder-agent/
category:
- Data Extraction &amp; Transformation
framework:
- Gemini
---

# jq Pipeline Builder Agent

The jq Pipeline Builder Agent translates natural language data transformation requests into optimized jq filter expressions for processing JSON and NDJSON data streams. It leverages the full jq language including path expressions, recursive descent (..), reduce operators, SQL-style GROUP_BY and UNIQUE_BY, and string interpolation for template generation. The agent handles complex operations like cross-referencing multiple JSON files with input and slurp modes, building streaming parsers with –stream flag for memory-efficient processing of large files, and constructing conditional transformations with if-then-else and try-catch error handling. It generates reusable jq modules with import statements, supports custom function definitions via def, and produces shell-compatible one-liners for pipeline integration with curl, grep, and awk. Includes test case generation using jqplay-compatible formats.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jq-pipeline-builder-agent/)
