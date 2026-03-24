---
name: "Tabula PDF Table Extraction Agent"
description: "Uses Tabula Java library via tabula-py bindings to detect and extract tables from PDF documents. Supports both lattice and stream extraction modes with configurable area coordinates and outputs to pandas DataFrames or CSV."
category: "Data Extraction & Transformation"
framework: "MCP-compatible"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/tabula-pdf-table-extraction-agent/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "pandas"  # from ase_tool_match
  github_stars: 48224  # from ase_github_stars (integer, not string)
  github_repo: "pandas-dev/pandas"  # from ase_github_repo
  license: "BSD-3-Clause"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Tabula PDF Table Extraction Agent

Uses Tabula Java library via tabula-py bindings to detect and extract tables from PDF documents. Supports both lattice and stream extraction modes with configurable area coordinates and outputs to pandas DataFrames or CSV.

## Overview

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

- Marketplace: https://agentskillexchange.com/skills/tabula-pdf-table-extraction-agent/
