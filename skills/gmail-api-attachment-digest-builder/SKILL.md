---
name: "Gmail API Attachment Digest Builder"
description: "Builds a daily attachment digest from Gmail API threads, labels, and message parts, then classifies files by MIME type, sender, and urgency. It uses users.messages.list, users.messages.get, and attachment payload metadata to surface invoices, contracts, screenshots, or CSV drops without opening each email manually."
category: "Calendar, Email & Productivity"
framework: "OpenClaw"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/gmail-api-attachment-digest-builder/"
---

# Gmail API Attachment Digest Builder

Builds a daily attachment digest from Gmail API threads, labels, and message parts, then classifies files by MIME type, sender, and urgency. It uses users.messages.list, users.messages.get, and attachment payload metadata to surface invoices, contracts, screenshots, or CSV drops without opening each email manually.

## Overview

**Gmail API Attachment Digest Builder** is designed for teams that need a repeatable workflow around Gmail API, users.messages.list, users.messages.get, MIME multipart parsing, Google Drive API. Instead of treating CI, security, or productivity data as isolated dashboards, the skill pulls records from the relevant API or CLI, normalizes the payloads, and explains what changed in operational terms. A typical run collects JSON from REST or GraphQL endpoints, enriches it with webhook or audit-log context, and then applies rule-based checks so the result is useful inside a pull request, incident channel, or weekly operations review. This makes it practical to move from raw API responses to an opinionated report without hand-building the same filters every time.

Under the hood, the skill works like a small integration pipeline. It authenticates with OAuth, personal access tokens, or service credentials as needed, queries the upstream SDK or CLI, and then transforms the response into a stable schema that can be versioned in Git. The workflow is comfortable around technical primitives such as API pagination, webhook replay, JSON diffing, npm or pip package metadata, Docker image tags, Kubernetes resource names, Terraform variables, and policy bundles. Where useful, it can compare current state against a baseline, detect drift, and produce a deterministic pass/fail gate for automation. That makes it fit naturally into GitHub Actions, GitLab CI, Buildkite, Argo CD, cron jobs, and other scheduled or event-driven systems.

The output is intentionally practical: an attachment digest email or Markdown report, sender-grouped file summaries, download queues for high-priority attachments. Each result is easy to hand off to another tool, whether that means posting a Markdown summary to Slack, uploading JSON to S3, opening a Jira issue, or feeding a downstream ETL job. Because the content includes exact API entities, resource identifiers, and integration points such as Gmail labels, Google Drive folders, Slack digest channels, Notion databases, the skill can slot into larger workflows without losing technical detail. It is especially useful when you want a skill to do more than paraphrase logs; it produces actionable artifacts that engineers, security reviewers, release managers, and operations teams can actually use.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill gmail-api-attachment-digest-builder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill gmail-api-attachment-digest-builder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill gmail-api-attachment-digest-builder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill gmail-api-attachment-digest-builder -a codex
```

### OpenClaw

```bash
clawhub install gmail-api-attachment-digest-builder
```

## Source

- Marketplace: https://agentskillexchange.com/skills/gmail-api-attachment-digest-builder/
