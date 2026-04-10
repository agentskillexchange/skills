---
name: Microsoft Graph Mail Triage Agent
description: Triages Outlook emails using the Microsoft Graph API /me/messages endpoint
  with $filter OData queries and inferenceClassification. Applies category labels,
  moves messages to focused/other folders, and creates Planner tasks from flagged
  items via the Tasks API.
verification: security_reviewed
source: https://agentskillexchange.com/skills/microsoft-graph-mail-triage-agent/
category:
- Calendar, Email &amp; Productivity
framework:
- Gemini
---
# Microsoft Graph Mail Triage Agent

Triages Outlook emails using the Microsoft Graph API /me/messages endpoint with $filter OData queries and inferenceClassification. Applies category labels, moves messages to focused/other folders, and creates Planner tasks from flagged items via the Tasks API.
This skill integrates with production-grade tooling to streamline automation workflows. It handles edge cases such as timeout management, retry logic with exponential backoff, and detailed error reporting. Configuration is managed through environment variables and YAML config files, supporting both local development and CI/CD pipeline environments. The skill outputs structured JSON logs compatible with ELK stack and Datadog for observability. It includes built-in rate limiting to respect API quotas and implements proper credential rotation using vault-based secret management.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/microsoft-graph-mail-triage-agent/)
