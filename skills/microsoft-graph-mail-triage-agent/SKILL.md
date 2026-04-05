---
name: "Microsoft Graph Mail Triage Agent"
description: "Triages Outlook emails using the Microsoft Graph API /me/messages endpoint with $filter OData queries and inferenceClassification. Applies category labels, moves messages to focused/other folders, and creates Planner tasks from flagged items via the Tasks API."
category: "Calendar, Email &amp; Productivity"
framework: "Gemini"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/microsoft-graph-mail-triage-agent/"
---
# Microsoft Graph Mail Triage Agent

Triages Outlook emails using the Microsoft Graph API /me/messages endpoint with $filter OData queries and inferenceClassification. Applies category labels, moves messages to focused/other folders, and creates Planner tasks from flagged items via the Tasks API.

Triages Outlook emails using the Microsoft Graph API /me/messages endpoint with $filter OData queries and inferenceClassification. Applies category labels, moves messages to focused/other folders, and creates Planner tasks from flagged items via the Tasks API.

This skill integrates with production-grade tooling to streamline automation workflows. It handles edge cases such as timeout management, retry logic with exponential backoff, and detailed error reporting. Configuration is managed through environment variables and YAML config files, supporting both local development and CI/CD pipeline environments. The skill outputs structured JSON logs compatible with ELK stack and Datadog for observability. It includes built-in rate limiting to respect API quotas and implements proper credential rotation using vault-based secret management.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill microsoft-graph-mail-triage-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill microsoft-graph-mail-triage-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill microsoft-graph-mail-triage-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill microsoft-graph-mail-triage-agent -a codex
```

### OpenClaw

```bash
clawhub install microsoft-graph-mail-triage-agent
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/microsoft-graph-mail-triage-agent/)
