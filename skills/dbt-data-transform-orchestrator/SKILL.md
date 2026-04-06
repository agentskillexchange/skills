---
name: "dbt Data Transform Orchestrator"
description: "Integrates with dbt Cloud Administrative API v2 to trigger and monitor data transformation jobs. Manages model runs, source freshness checks, and test execution through dbt API endpoints with Snowflake and BigQuery adapter support."
category: "Data Extraction &amp; Transformation"
framework: "Custom Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/dbt-data-transform-orchestrator/"
---
# dbt Data Transform Orchestrator

Integrates with dbt Cloud Administrative API v2 to trigger and monitor data transformation jobs. Manages model runs, source freshness checks, and test execution through dbt API endpoints with Snowflake and BigQuery adapter support.

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
npx skills add agentskillexchange/skills --skill dbt-data-transform-orchestrator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill dbt-data-transform-orchestrator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill dbt-data-transform-orchestrator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill dbt-data-transform-orchestrator -a codex
```

### OpenClaw

```bash
clawhub install dbt-data-transform-orchestrator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dbt-data-transform-orchestrator/)
