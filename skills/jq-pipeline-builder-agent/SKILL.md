---
name: "jq Pipeline Builder Agent"
description: "Constructs complex jq filter pipelines from natural language queries against JSON/NDJSON data streams. Uses jq built-in functions including path expressions, reduce, and SQL-style operators."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/jq-pipeline-builder-agent/"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Gemini"
---

# jq Pipeline Builder Agent

The jq Pipeline Builder Agent translates natural language data transformation requests into optimized jq filter expressions for processing JSON and NDJSON data streams. It leverages the full jq language including path expressions, recursive descent (..), reduce operators, SQL-style GROUP_BY and UNIQUE_BY, and string interpolation for template generation. The agent handles complex operations like cross-referencing multiple JSON files with input and slurp modes, building streaming parsers with -stream flag for memory-efficient processing of large files, and constructing conditional transformations with if-then-else and try-catch error handling. It generates reusable jq modules with import statements, supports custom function definitions via def, and produces shell-compatible one-liners for pipeline integration with curl, grep, and awk. Includes test case generation using jqplay-compatible formats.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jq-pipeline-builder-agent/)
