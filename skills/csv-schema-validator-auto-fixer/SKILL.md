---
name: "CSV Schema Validator & Auto-Fixer"
description: "Validates CSV files against JSON Schema definitions using AJV and csv-parse. Automatically detects and repairs type mismatches, missing required columns, and encoding issues with configurable strictness levels."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/csv-schema-validator-auto-fixer/"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "OpenClaw"
---

# CSV Schema Validator & Auto-Fixer

The CSV Schema Validator & Auto-Fixer skill provides comprehensive CSV validation and repair capabilities using the AJV JSON Schema validator combined with csv-parse for robust parsing. It accepts CSV files alongside JSON Schema definitions that describe expected column types, required fields, and value constraints. The validation engine processes each row against the schema, flagging type mismatches (e.g., strings in numeric columns), missing required columns, duplicate headers, and encoding anomalies like BOM markers or mixed line endings. When auto-fix mode is enabled, it applies configurable repair strategies: coercing types where safe, inserting default values for missing required fields, deduplicating headers with suffix numbering, and normalizing encoding to UTF-8. The tool generates detailed validation reports in JSON format with per-row error annotations, summary statistics, and a diff of applied fixes. Supports streaming mode for large files exceeding available memory, batch processing of entire directories, and integration with CI/CD pipelines via exit codes and structured output.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/csv-schema-validator-auto-fixer/)
