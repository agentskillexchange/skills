---
name: "Sentry Error Intelligence"
description: "Connects to the Sentry API v0 to analyze error trends, group similar stack traces using fingerprinting rules, and auto-assigns issues to code owners via GitHub CODEOWNERS integration."
category: "Monitoring & Alerts"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/sentry-error-intelligence/"
tool_ecosystem:
  tool: sentry
  github_stars: 43437
  npm_weekly_downloads: 16379655
  github_repo: getsentry/sentry
  maintained: true
---

# Sentry Error Intelligence

Connects to the Sentry API v0 to analyze error trends, group similar stack traces using fingerprinting rules, and auto-assigns issues to code owners via GitHub CODEOWNERS integration.

## Overview

The Sentry Error Intelligence skill transforms raw error data into actionable insights for AI agent workflows. It connects to the Sentry API v0, querying /api/0/organizations/{org}/issues/ with Sentry Query Language (SQL) filters to identify trending errors, regressions, and new issue spikes across projects.

Stack trace analysis uses Sentry enhanced event data from the /api/0/issues/{issue_id}/events/latest/ endpoint, parsing frame-level information including source context, variable values, and breadcrumb trails. The skill implements custom fingerprinting rules via the /api/0/projects/{org}/{project}/grouping-configs/ endpoint to improve issue deduplication accuracy.

Auto-assignment leverages GitHub CODEOWNERS files parsed through the GitHub Contents API, matching error source file paths to responsible teams. The skill creates GitHub issues for persistent errors via the Issues API v3, including Sentry event links, affected user counts, and frequency charts generated from the Sentry Stats API (/api/0/organizations/{org}/stats_v2/). Release health monitoring tracks crash-free session rates through the Sessions API, triggering rollback recommendations when rates drop below configurable thresholds.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill sentry-error-intelligence
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill sentry-error-intelligence -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill sentry-error-intelligence -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill sentry-error-intelligence -a codex
```

### OpenClaw

```bash
clawhub install sentry-error-intelligence
```

## Source

- Marketplace: https://agentskillexchange.com/skills/sentry-error-intelligence/
