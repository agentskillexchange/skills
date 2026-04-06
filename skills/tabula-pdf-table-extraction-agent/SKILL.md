---
name: "Tabula PDF Table Extraction Agent"
description: "Uses Tabula Java library via tabula-py bindings to detect and extract tables from PDF documents. Supports both lattice and stream extraction modes with configurable area coordinates and outputs to pandas DataFrames or CSV."
category: "Data Extraction &amp; Transformation"
framework: "MCP"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/tabula-pdf-table-extraction-agent/"
---
# Tabula PDF Table Extraction Agent

Uses Tabula Java library via tabula-py bindings to detect and extract tables from PDF documents. Supports both lattice and stream extraction modes with configurable area coordinates and outputs to pandas DataFrames or CSV.

Overview

This skill provides automated integration capabilities designed for production agent workflows. It handles authentication, rate limiting, and error recovery out of the box, allowing agents to focus on high-level task orchestration rather than low-level API management.

Key Features

- Automatic retry logic with exponential backoff for API rate limits

- Structured output formatting compatible with downstream agent pipelines

- Comprehensive error handling with actionable diagnostic messages

- Configurable caching layer to reduce redundant API calls

Usage

Install via the Agent Skill Exchange registry and configure with your API credentials. The skill exposes a standardized interface that works across supported agent frameworks, with framework-specific optimizations applied automatically during initialization.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill tabula-pdf-table-extraction-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill tabula-pdf-table-extraction-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill tabula-pdf-table-extraction-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill tabula-pdf-table-extraction-agent -a codex
```

### OpenClaw

```bash
clawhub install tabula-pdf-table-extraction-agent
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tabula-pdf-table-extraction-agent/)
