---
name: "Postman Collection Runner"
description: "Postman Collection Runner is built around Postman API testing platform. The underlying ecosystem is represented by postmanlabs/postman-app-support (5,996+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like collections, environments, Newman, scripts, assertions, monitors and preserving the operational context […]"
category: "Library & API Reference"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/postmanlabs/postman-app-support"
tool_ecosystem:
  tool: postman
  github_stars: 5996
  github_repo: postmanlabs/postman-app-support
  maintained: true
---

# Postman Collection Runner

Postman Collection Runner is built around Postman API testing platform. The underlying ecosystem is represented by postmanlabs/postman-app-support (5,996+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like collections, environments, Newman, scripts, assertions, monitors and preserving the operational context […]

## Overview

**Postman Collection Runner** is built around Postman API testing platform. The underlying ecosystem is represented by `postmanlabs/postman-app-support` (5,996+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like collections, environments, Newman, scripts, assertions, monitors and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to postman so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The implementation typically relies on collections, environments, Newman, scripts, assertions, monitors, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses collections, environments, Newman, scripts, assertions, monitors instead of scraping a UI, which makes runs easier to audit and retry.

Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

Fits into broader integration points such as API regression tests, collection execution, and documentation validation.

Key integration points include API regression tests, collection execution, and documentation validation. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill postman-collection-runner
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill postman-collection-runner -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill postman-collection-runner -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill postman-collection-runner -a codex
```

### OpenClaw

```bash
clawhub install postman-collection-runner
```

## Source

- Marketplace: https://agentskillexchange.com/skills/postman-collection-runner/
