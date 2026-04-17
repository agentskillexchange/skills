---
title: "Microsoft Graph Mail Triage Agent"
description: "Triages Outlook emails using the Microsoft Graph API /me/messages endpoint with $filter OData queries and inferenceClassification. Applies category labels, moves messages to focused/other folders, and creates Planner tasks from flagged items via the Tasks API.\nThis skill integrates with production-grade tooling to streamline automation workflows. It handles edge cases such as timeout management, retry logic with exponential backoff, and detailed error reporting. Configuration is managed through environment variables and YAML config files, supporting both local development and CI/CD pipeline environments. The skill outputs structured JSON logs compatible with ELK stack and Datadog for observability. It includes built-in rate limiting to respect API quotas and implements proper credential rotation using vault-based secret management."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/microsoft-graph-mail-triage-agent/"
framework:
  - "Gemini"
---

# Microsoft Graph Mail Triage Agent

Triages Outlook emails using the Microsoft Graph API /me/messages endpoint with $filter OData queries and inferenceClassification. Applies category labels, moves messages to focused/other folders, and creates Planner tasks from flagged items via the Tasks API.
This skill integrates with production-grade tooling to streamline automation workflows. It handles edge cases such as timeout management, retry logic with exponential backoff, and detailed error reporting. Configuration is managed through environment variables and YAML config files, supporting both local development and CI/CD pipeline environments. The skill outputs structured JSON logs compatible with ELK stack and Datadog for observability. It includes built-in rate limiting to respect API quotas and implements proper credential rotation using vault-based secret management.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/microsoft-graph-mail-triage-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/microsoft-graph-mail-triage-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/microsoft-graph-mail-triage-agent/)
