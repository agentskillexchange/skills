---
title: Sentry Error Triage Assistant
description: Triages application errors using the Sentry Web API (/api/0/issues/)
  and Sentry SDK breadcrumb data. Groups issues by stack trace similarity using Sentry
  fingerprinting rules and queries release health via the /api/0/organizations/{org}/releases/
  endpoint.
verification: security_reviewed
source: https://github.com/getsentry/sentry
category:
- Runbooks & Diagnostics
framework:
- Claude Agents
tool_ecosystem:
  github_repo: getsentry/sentry
  github_stars: 43576
---

# Sentry Error Triage Assistant

Triages application errors using the Sentry Web API (/api/0/issues/) and Sentry SDK breadcrumb data. Groups issues by stack trace similarity using Sentry fingerprinting rules and queries release health via the /api/0/organizations/{org}/releases/ endpoint.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/sentry-error-triage-assistant/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/sentry-error-triage-assistant
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/sentry-error-triage-assistant`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sentry-error-triage-assistant/)
