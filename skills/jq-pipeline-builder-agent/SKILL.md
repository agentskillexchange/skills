---
title: "jq Pipeline Builder Agent"
description: "Constructs complex jq filter pipelines from natural language queries against JSON/NDJSON data streams. Uses jq built-in functions including path expressions, reduce, and SQL-style operators."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/jq-pipeline-builder-agent/"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Gemini"
---

# jq Pipeline Builder Agent

The jq Pipeline Builder Agent translates natural language data transformation requests into optimized jq filter expressions for processing JSON and NDJSON data streams. It leverages the full jq language including path expressions, recursive descent (..), reduce operators, SQL-style GROUP_BY and UNIQUE_BY, and string interpolation for template generation. The agent handles complex operations like cross-referencing multiple JSON files with input and slurp modes, building streaming parsers with –stream flag for memory-efficient processing of large files, and constructing conditional transformations with if-then-else and try-catch error handling. It generates reusable jq modules with import statements, supports custom function definitions via def, and produces shell-compatible one-liners for pipeline integration with curl, grep, and awk. Includes test case generation using jqplay-compatible formats.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jq-pipeline-builder-agent/)
