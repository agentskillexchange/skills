---
title: Todoist Natural Language Task Parser
description: Parses natural language task descriptions into structured Todoist API
  v2 task objects with due dates, priority levels, and project assignments. Uses the
  Todoist Sync API for batch task creation and supports recurring date patterns via
  the RRule specification. This skill provides comprehensive automation for its target
  domain with production-ready error handling and logging. It implements retry mechanisms
  with configurable backoff strategies, validates all inputs against JSON Schema definitions,
  and produces structured output compatible with downstream processing pipelines.
  Authentication is handled through OAuth 2.0 flows or API key rotation with secure
  storage in environment variables or secret managers like HashiCorp Vault. The skill
  supports dry-run mode for safe testing, emits OpenTelemetry traces for distributed
  debugging, and includes comprehensive unit test coverage with mock fixtures for
  offline development.
verification: security_reviewed
source: https://agentskillexchange.com/skills/todoist-natural-language-task-parser/
category:
- Calendar, Email &amp; Productivity
framework:
- MCP
---

# Todoist Natural Language Task Parser

Parses natural language task descriptions into structured Todoist API v2 task objects with due dates, priority levels, and project assignments. Uses the Todoist Sync API for batch task creation and supports recurring date patterns via the RRule specification. This skill provides comprehensive automation for its target domain with production-ready error handling and logging. It implements retry mechanisms with configurable backoff strategies, validates all inputs against JSON Schema definitions, and produces structured output compatible with downstream processing pipelines. Authentication is handled through OAuth 2.0 flows or API key rotation with secure storage in environment variables or secret managers like HashiCorp Vault. The skill supports dry-run mode for safe testing, emits OpenTelemetry traces for distributed debugging, and includes comprehensive unit test coverage with mock fixtures for offline development.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/todoist-natural-language-task-parser/)
