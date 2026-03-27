---
name: "Todoist Natural Language Task Parser"
description: "Parses natural language task descriptions into structured Todoist API v2 task objects with due dates, priority levels, and project assignments. Uses the Todoist Sync API for batch task creation and supports recurring date patterns via the RRule specification."
category: "Calendar, Email & Productivity"
framework: "MCP"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/todoist-natural-language-task-parser/"
tool_ecosystem:
  tool: vault
  github_stars: 35275
  github_repo: hashicorp/vault
  maintained: true
---

# Todoist Natural Language Task Parser

Parses natural language task descriptions into structured Todoist API v2 task objects with due dates, priority levels, and project assignments. Uses the Todoist Sync API for batch task creation and supports recurring date patterns via the RRule specification.

## Overview

Parses natural language task descriptions into structured Todoist API v2 task objects with due dates, priority levels, and project assignments. Uses the Todoist Sync API for batch task creation and supports recurring date patterns via the RRule specification.

This skill provides comprehensive automation for its target domain with production-ready error handling and logging. It implements retry mechanisms with configurable backoff strategies, validates all inputs against JSON Schema definitions, and produces structured output compatible with downstream processing pipelines. Authentication is handled through OAuth 2.0 flows or API key rotation with secure storage in environment variables or secret managers like HashiCorp Vault. The skill supports dry-run mode for safe testing, emits OpenTelemetry traces for distributed debugging, and includes comprehensive unit test coverage with mock fixtures for offline development.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill todoist-natural-language-task-parser
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill todoist-natural-language-task-parser -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill todoist-natural-language-task-parser -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill todoist-natural-language-task-parser -a codex
```

### OpenClaw

```bash
clawhub install todoist-natural-language-task-parser
```

## Source

- Marketplace: https://agentskillexchange.com/skills/todoist-natural-language-task-parser/
