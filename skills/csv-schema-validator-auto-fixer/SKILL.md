---
name: "CSV Schema Validator & Auto-Fixer"
description: "Validates CSV files against JSON Schema definitions using AJV and csv-parse. Automatically detects and repairs type mismatches, missing required columns, and encoding issues with configurable strictness levels."
category: "Data Extraction & Transformation"
framework: "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/csv-schema-validator-auto-fixer/"
---

# CSV Schema Validator & Auto-Fixer

Validates CSV files against JSON Schema definitions using AJV and csv-parse. Automatically detects and repairs type mismatches, missing required columns, and encoding issues with configurable strictness levels.

## Overview

The CSV Schema Validator & Auto-Fixer skill provides comprehensive CSV validation and repair capabilities using the AJV JSON Schema validator combined with csv-parse for robust parsing. It accepts CSV files alongside JSON Schema definitions that describe expected column types, required fields, and value constraints. The validation engine processes each row against the schema, flagging type mismatches (e.g., strings in numeric columns), missing required columns, duplicate headers, and encoding anomalies like BOM markers or mixed line endings. When auto-fix mode is enabled, it applies configurable repair strategies: coercing types where safe, inserting default values for missing required fields, deduplicating headers with suffix numbering, and normalizing encoding to UTF-8. The tool generates detailed validation reports in JSON format with per-row error annotations, summary statistics, and a diff of applied fixes. Supports streaming mode for large files exceeding available memory, batch processing of entire directories, and integration with CI/CD pipelines via exit codes and structured output.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill csv-schema-validator-auto-fixer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill csv-schema-validator-auto-fixer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill csv-schema-validator-auto-fixer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill csv-schema-validator-auto-fixer -a codex
```

### OpenClaw

```bash
clawhub install csv-schema-validator-auto-fixer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/csv-schema-validator-auto-fixer/
