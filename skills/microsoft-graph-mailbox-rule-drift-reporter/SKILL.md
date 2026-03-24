---
name: "Microsoft Graph Mailbox Rule Drift Reporter"
description: "Detects unexpected Outlook inbox rule changes with Microsoft Graph /mailFolders, /messageRules, and delta query endpoints. It compares the live mailbox configuration to a baseline so silent forwarding, deletion, or category changes become visible immediately."
category: "Calendar, Email & Productivity"
framework: "MCP-compatible"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/microsoft-graph-mailbox-rule-drift-reporter/"
---

# Microsoft Graph Mailbox Rule Drift Reporter

Detects unexpected Outlook inbox rule changes with Microsoft Graph /mailFolders, /messageRules, and delta query endpoints. It compares the live mailbox configuration to a baseline so silent forwarding, deletion, or category changes become visible immediately.

## Overview

**Microsoft Graph Mailbox Rule Drift Reporter** is designed for teams that need a repeatable workflow around Microsoft Graph API, messageRules endpoint, delta query, OAuth 2.0, JSON diffing. Instead of treating CI, security, or productivity data as isolated dashboards, the skill pulls records from the relevant API or CLI, normalizes the payloads, and explains what changed in operational terms. A typical run collects JSON from REST or GraphQL endpoints, enriches it with webhook or audit-log context, and then applies rule-based checks so the result is useful inside a pull request, incident channel, or weekly operations review. This makes it practical to move from raw API responses to an opinionated report without hand-building the same filters every time.

Under the hood, the skill works like a small integration pipeline. It authenticates with OAuth, personal access tokens, or service credentials as needed, queries the upstream SDK or CLI, and then transforms the response into a stable schema that can be versioned in Git. The workflow is comfortable around technical primitives such as API pagination, webhook replay, JSON diffing, npm or pip package metadata, Docker image tags, Kubernetes resource names, Terraform variables, and policy bundles. Where useful, it can compare current state against a baseline, detect drift, and produce a deterministic pass/fail gate for automation. That makes it fit naturally into GitHub Actions, GitLab CI, Buildkite, Argo CD, cron jobs, and other scheduled or event-driven systems.

The output is intentionally practical: a mailbox rule drift report, baseline vs current diffs, alert payloads for suspicious forwarding or deletion rules. Each result is easy to hand off to another tool, whether that means posting a Markdown summary to Slack, uploading JSON to S3, opening a Jira issue, or feeding a downstream ETL job. Because the content includes exact API entities, resource identifiers, and integration points such as Outlook mailboxes, Teams webhooks, SIEM alerts, ticketing systems, the skill can slot into larger workflows without losing technical detail. It is especially useful when you want a skill to do more than paraphrase logs; it produces actionable artifacts that engineers, security reviewers, release managers, and operations teams can actually use.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill microsoft-graph-mailbox-rule-drift-reporter
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill microsoft-graph-mailbox-rule-drift-reporter -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill microsoft-graph-mailbox-rule-drift-reporter -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill microsoft-graph-mailbox-rule-drift-reporter -a codex
```

### OpenClaw

```bash
clawhub install microsoft-graph-mailbox-rule-drift-reporter
```

## Source

- Marketplace: https://agentskillexchange.com/skills/microsoft-graph-mailbox-rule-drift-reporter/
