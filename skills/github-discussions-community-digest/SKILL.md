---
name: "GitHub Discussions Community Digest"
description: "Queries GitHub GraphQL API for new and unanswered Discussions, ranks them by reaction count and recency, and drafts a weekly digest via SendGrid. Automatically labels stale discussions as needs-triage via the GitHub REST API. Digest content is also mirrored as a pinned post to a linked Discord channel."
category: "Integrations & Connectors"
framework: "MCP-compatible"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/github-discussions-community-digest/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "sendgrid"  # from ase_tool_match
  github_stars: 3054  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 3287627  # from ase_npm_downloads
  github_repo: "sendgrid/sendgrid-nodejs"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# GitHub Discussions Community Digest

Queries GitHub GraphQL API for new and unanswered Discussions, ranks them by reaction count and recency, and drafts a weekly digest via SendGrid. Automatically labels stale discussions as needs-triage via the GitHub REST API. Digest content is also mirrored as a pinned post to a linked Discord channel.

## Overview

**GitHub Discussions Community Digest** is built around SendGrid email delivery platform. The underlying ecosystem is represented by `sendgrid/sendgrid-nodejs` (3,054+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like mail/send, templates, contact lists, event webhooks, suppression groups and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to sendgrid so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Queries GitHub GraphQL API for new and unanswered Discussions, ranks them by reaction count and recency, and drafts a weekly digest via SendGrid. Automatically labels stale discussions as needs-triage via the GitHub REST API. Digest content is also mirrored as a pinned post to a linked Discord channel. The implementation typically relies on mail/send, templates, contact lists, event webhooks, suppression groups, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses mail/send, templates, contact lists, event webhooks, suppression groups instead of scraping a UI, which makes runs easier to audit and retry.

Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

Fits into broader integration points such as transactional email, digests, notifications, and deliverability workflows.

Key integration points include transactional email, digests, notifications, and deliverability workflows. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill github-discussions-community-digest
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill github-discussions-community-digest -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill github-discussions-community-digest -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill github-discussions-community-digest -a codex
```

### OpenClaw

```bash
clawhub install github-discussions-community-digest
```

## Source

- Marketplace: https://agentskillexchange.com/skills/github-discussions-community-digest/
