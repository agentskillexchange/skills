---
title: "Linear Issue Manager"
description: "Linear Issue Manager is built around GraphQL API ecosystem. The underlying ecosystem is represented by graphql/graphql-js (20,335+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like queries, mutations, schema introspection, fragments, pagination, subscriptions and preserving the operational context […]"
verification: "security_reviewed"
source: "https://linear.app/docs"
category:
  - "Developer Tools"
framework:
  - "Custom Agents"
---

# Linear Issue Manager

Linear Issue Manager is built around GraphQL API ecosystem. The underlying ecosystem is represented by graphql/graphql-js (20,335+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like queries, mutations, schema introspection, fragments, pagination, subscriptions and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to graphql so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The implementation typically relies on queries, mutations, schema introspection, fragments, pagination, subscriptions, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses queries, mutations, schema introspection, fragments, pagination, subscriptions instead of scraping a UI, which makes runs easier to audit and retry.
Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.
Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.
Fits into broader integration points such as typed API access, schema exploration, and integration workflows.

 Key integration points include typed API access, schema exploration, and integration workflows. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/linear-issue-manager/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/linear-issue-manager
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/linear-issue-manager`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/linear-issue-manager/)
