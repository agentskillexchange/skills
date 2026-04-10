---
title: "Todoist Natural Language Task Parser"
description: "Parses natural language task descriptions into structured Todoist API v2 task objects with due dates, priority levels, and project assignments. Uses the Todoist Sync API for batch task creation and supports recurring date patterns via the RRule specification."
slug: "todoist-natural-language-task-parser"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/todoist-natural-language-task-parser/"
---

# Todoist Natural Language Task Parser

Parses natural language task descriptions into structured Todoist API v2 task objects with due dates, priority levels, and project assignments. Uses the Todoist Sync API for batch task creation and supports recurring date patterns via the RRule specification.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install todoist-natural-language-task-parser
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill provides comprehensive automation for its target domain with production-ready error handling and logging. It implements retry mechanisms with configurable backoff strategies, validates all inputs against JSON Schema definitions, and produces structured output compatible with downstream processing pipelines. Authentication is handled through OAuth 2.0 flows or API key rotation with secure storage in environment variables or secret managers like HashiCorp Vault. The skill supports dry-run mode for safe testing, emits OpenTelemetry traces for distributed debugging, and includes comprehensive unit test coverage with mock fixtures for offline development.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/todoist-natural-language-task-parser/)
