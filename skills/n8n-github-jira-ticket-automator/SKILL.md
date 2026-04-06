---
name: "n8n GitHub Issue-to-Jira Ticket Automator"
description: "Deploys an n8n workflow via the n8n REST API using the GitHub Trigger node to capture new issue events and transform them into Jira tickets via the Jira Cloud REST API. Labels, priority mappings, and assignee routing rules are configured using n8n’s Function node with custom JavaScript."
category: "Developer Tools"
framework: "Codex"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/n8n-github-jira-ticket-automator/"
---
# n8n GitHub Issue-to-Jira Ticket Automator

Deploys an n8n workflow via the n8n REST API using the GitHub Trigger node to capture new issue events and transform them into Jira tickets via the Jira Cloud REST API. Labels, priority mappings, and assignee routing rules are configured using n8n’s Function node with custom JavaScript.

n8n GitHub Issue-to-Jira Ticket Automator is built around Jira issue tracking platform. It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like JQL, issues, workflows, comments, transitions, custom fields, sprint APIs and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to jira so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Deploys an n8n workflow via the n8n REST API using the GitHub Trigger node to capture new issue events and transform them into Jira tickets via the Jira Cloud REST API. Labels, priority mappings, and assignee routing rules are configured using n8n's Function node with custom JavaScript. The implementation typically relies on JQL, issues, workflows, comments, transitions, custom fields, sprint APIs, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

- Accesses JQL, issues, workflows, comments, transitions, custom fields, sprint APIs instead of scraping a UI, which makes runs easier to audit and retry.

- Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

- Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

- Fits into broader integration points such as ticket triage, sprint planning, incident tracking, and project automation.

Key integration points include ticket triage, sprint planning, incident tracking, and project automation. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill n8n-github-jira-ticket-automator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill n8n-github-jira-ticket-automator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill n8n-github-jira-ticket-automator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill n8n-github-jira-ticket-automator -a codex
```

### OpenClaw

```bash
clawhub install n8n-github-jira-ticket-automator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/n8n-github-jira-ticket-automator/)
