---
name: "CircleCI MCP Server"
description: "CircleCI MCP Server is built around CircleCI continuous integration platform. The underlying ecosystem is represented by circleci/circleci-docs (842+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like CircleCI API v2, Insights API, workflows, jobs, test metadata, artifacts and [&hellip;]"
category: "Developer Tools"
framework: "MCP"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/circleci-mcp-server/"
---
# CircleCI MCP Server

CircleCI MCP Server is built around CircleCI continuous integration platform. The underlying ecosystem is represented by circleci/circleci-docs (842+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like CircleCI API v2, Insights API, workflows, jobs, test metadata, artifacts and [&hellip;]

## Overview

CircleCI MCP Server is built around CircleCI continuous integration platform. The underlying ecosystem is represented by circleci/circleci-docs (842+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like CircleCI API v2, Insights API, workflows, jobs, test metadata, artifacts and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to circleci so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The implementation typically relies on CircleCI API v2, Insights API, workflows, jobs, test metadata, artifacts, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses CircleCI API v2, Insights API, workflows, jobs, test metadata, artifacts instead of scraping a UI, which makes runs easier to audit and retry.
Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.
Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.
Fits into broader integration points such as CI diagnostics, flaky test analysis, pipeline automation, and deployment gates.

Because this is exposed as an MCP skill, the tool surface is designed for agent-safe, structured calls instead of free-form shell usage. That means models can inspect schemas, call a narrow set of operations, and keep context across a longer workflow without re-implementing credentials or connection logic on every step. Key integration points include CI diagnostics, flaky test analysis, pipeline automation, and deployment gates. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill circleci-mcp-server
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill circleci-mcp-server -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill circleci-mcp-server -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill circleci-mcp-server -a codex
```

### OpenClaw

```bash
clawhub install circleci-mcp-server
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-mcp-server/)
