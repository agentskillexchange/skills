---
title: Microsoft Graph Mail Triage Agent
description: Triages Outlook emails using the Microsoft Graph API /me/messages endpoint
  with $filter OData queries and inferenceClassification. Applies category labels,
  moves messages to focused/other folders, and creates Planner tasks from flagged
  items via the Tasks API. This skill integrates with production-grade tooling to
  streamline automation workflows. It handles edge cases such as timeout management,
  retry logic with exponential backoff, and detailed error reporting. Configuration
  is managed through environment variables and YAML config files, supporting both
  local development and CI/CD pipeline environments. The skill outputs structured
  JSON logs compatible with ELK stack and Datadog for observability. It includes built-in
  rate limiting to respect API quotas and implements proper credential rotation using
  vault-based secret management.
verification: security_reviewed
source: https://agentskillexchange.com/skills/microsoft-graph-mail-triage-agent/
category:
- Calendar, Email &amp; Productivity
framework:
- Gemini
---

# Microsoft Graph Mail Triage Agent

Triages Outlook emails using the Microsoft Graph API /me/messages endpoint with $filter OData queries and inferenceClassification. Applies category labels, moves messages to focused/other folders, and creates Planner tasks from flagged items via the Tasks API. This skill integrates with production-grade tooling to streamline automation workflows. It handles edge cases such as timeout management, retry logic with exponential backoff, and detailed error reporting. Configuration is managed through environment variables and YAML config files, supporting both local development and CI/CD pipeline environments. The skill outputs structured JSON logs compatible with ELK stack and Datadog for observability. It includes built-in rate limiting to respect API quotas and implements proper credential rotation using vault-based secret management.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/microsoft-graph-mail-triage-agent/)
