---
title: "Sentry Error Intelligence"
description: "The Sentry Error Intelligence skill transforms raw error data into actionable insights for AI agent workflows. It connects to the Sentry API v0, querying /api/0/organizations/{org}/issues/ with Sentry Query Language (SQL) filters to identify trending errors, regressions, and new issue spikes across projects.\nStack trace analysis uses Sentry enhanced event data from the /api/0/issues/{issue_id}/events/latest/ endpoint, parsing frame-level information including source context, variable values, and breadcrumb trails. The skill implements custom fingerprinting rules via the /api/0/projects/{org}/{project}/grouping-configs/ endpoint to improve issue deduplication accuracy.\nAuto-assignment leverages GitHub CODEOWNERS files parsed through the GitHub Contents API, matching error source file paths to responsible teams. The skill creates GitHub issues for persistent errors via the Issues API v3, including Sentry event links, affected user counts, and frequency charts generated from the Sentry Stats API (/api/0/organizations/{org}/stats_v2/). Release health monitoring tracks crash-free session rates through the Sessions API, triggering rollback recommendations when rates drop below configurable thresholds."
verification: security_reviewed
source: "https://github.com/getsentry/sentry"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "getsentry/sentry"
  github_stars: 43576
---

# Sentry Error Intelligence

The Sentry Error Intelligence skill transforms raw error data into actionable insights for AI agent workflows. It connects to the Sentry API v0, querying /api/0/organizations/{org}/issues/ with Sentry Query Language (SQL) filters to identify trending errors, regressions, and new issue spikes across projects.
Stack trace analysis uses Sentry enhanced event data from the /api/0/issues/{issue_id}/events/latest/ endpoint, parsing frame-level information including source context, variable values, and breadcrumb trails. The skill implements custom fingerprinting rules via the /api/0/projects/{org}/{project}/grouping-configs/ endpoint to improve issue deduplication accuracy.
Auto-assignment leverages GitHub CODEOWNERS files parsed through the GitHub Contents API, matching error source file paths to responsible teams. The skill creates GitHub issues for persistent errors via the Issues API v3, including Sentry event links, affected user counts, and frequency charts generated from the Sentry Stats API (/api/0/organizations/{org}/stats_v2/). Release health monitoring tracks crash-free session rates through the Sessions API, triggering rollback recommendations when rates drop below configurable thresholds.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/sentry-error-intelligence
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/sentry-error-intelligence` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sentry-error-intelligence/)
