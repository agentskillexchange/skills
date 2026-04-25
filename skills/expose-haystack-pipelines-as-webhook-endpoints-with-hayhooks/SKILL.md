---
title: "Expose Haystack pipelines as webhook endpoints with Hayhooks"
description: "Turn an existing Haystack pipeline into an HTTP or MCP endpoint without building and maintaining a custom wrapper service."
verification: "listed"
source: "https://github.com/deepset-ai/hayhooks"
category:
  - "Integrations & Connectors"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "deepset-ai/hayhooks"
  github_stars: 138
---

# Expose Haystack pipelines as webhook endpoints with Hayhooks

Use Hayhooks when an agent already has a Haystack pipeline and needs to serve it through HTTP, webhook-style, OpenAI-compatible, or MCP endpoints for other systems to call. The user is not invoking a generic AI platform here. The workflow is narrow: wrap a pipeline, deploy it, and expose a documented endpoint surface for handoffs. That scope boundary, serving existing Haystack pipelines as callable endpoints, keeps it distinct from a plain library or framework listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/expose-haystack-pipelines-as-webhook-endpoints-with-hayhooks/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/expose-haystack-pipelines-as-webhook-endpoints-with-hayhooks
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/expose-haystack-pipelines-as-webhook-endpoints-with-hayhooks`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/expose-haystack-pipelines-as-webhook-endpoints-with-hayhooks/)
