---
name: "Outlook Mail Triage Skill"
description: "Triages Outlook inboxes using Microsoft Graph API v1.0 with delta query support for incremental mail sync. Applies ML-based priority scoring via Azure Cognitive Services Text Analytics and auto-files messages into folders based on learned patterns."
category: "Calendar, Email &amp; Productivity"
framework: "Claude Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/outlook-mail-triage-microsoft-graph/"
---
# Outlook Mail Triage Skill

Triages Outlook inboxes using Microsoft Graph API v1.0 with delta query support for incremental mail sync. Applies ML-based priority scoring via Azure Cognitive Services Text Analytics and auto-files messages into folders based on learned patterns.

Triages Outlook inboxes using Microsoft Graph API v1.0 with delta query support for incremental mail sync. Applies ML-based priority scoring via Azure Cognitive Services Text Analytics and auto-files messages into folders based on learned patterns.

This skill provides a comprehensive automation layer for developers and teams who need reliable, repeatable workflows. It handles authentication, rate limiting, and error recovery automatically, so you can focus on the logic that matters. The agent monitors for changes in real time and applies incremental updates to minimize API calls and reduce latency. Configuration is handled through a simple YAML manifest that defines inputs, outputs, and trigger conditions. Built-in logging captures every action for audit trails and debugging. Supports both interactive and headless modes, making it suitable for CI/CD pipelines as well as local development. The skill includes pre-built templates for common use cases and can be extended with custom plugins. Error handling follows exponential backoff with jitter for transient failures and provides clear diagnostic messages for permanent errors. Compatible with major operating systems and containerized environments. Tested against production workloads with comprehensive integration test suites.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill outlook-mail-triage-microsoft-graph
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill outlook-mail-triage-microsoft-graph -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill outlook-mail-triage-microsoft-graph -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill outlook-mail-triage-microsoft-graph -a codex
```

### OpenClaw

```bash
clawhub install outlook-mail-triage-microsoft-graph
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/outlook-mail-triage-microsoft-graph/)
