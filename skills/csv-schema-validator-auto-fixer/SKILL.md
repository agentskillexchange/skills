---
title: "CSV Schema Validator & Auto-Fixer"
description: "Validates CSV files against JSON Schema definitions using AJV and csv-parse. Automatically detects and repairs type mismatches, missing required columns, and encoding issues with configurable strictness levels."
verification: "security_reviewed"
source: "https://github.com/ajv-validator/ajv"
category:
  - "Data Extraction & Transformation"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "ajv-validator/ajv"
  github_stars: 14691
  npm_package: "ajv"
  npm_weekly_downloads: 291125331
---

# CSV Schema Validator & Auto-Fixer

The CSV Schema Validator & Auto-Fixer skill provides comprehensive CSV validation and repair capabilities using the AJV JSON Schema validator combined with csv-parse for robust parsing. It accepts CSV files alongside JSON Schema definitions that describe expected column types, required fields, and value constraints. The validation engine processes each row against the schema, flagging type mismatches (e.g., strings in numeric columns), missing required columns, duplicate headers, and encoding anomalies like BOM markers or mixed line endings. When auto-fix mode is enabled, it applies configurable repair strategies: coercing types where safe, inserting default values for missing required fields, deduplicating headers with suffix numbering, and normalizing encoding to UTF-8. The tool generates detailed validation reports in JSON format with per-row error annotations, summary statistics, and a diff of applied fixes. Supports streaming mode for large files exceeding available memory, batch processing of entire directories, and integration with CI/CD pipelines via exit codes and structured output.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/csv-schema-validator-auto-fixer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/csv-schema-validator-auto-fixer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/csv-schema-validator-auto-fixer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/csv-schema-validator-auto-fixer/)
