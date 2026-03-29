---
name: "Sentry Error Triage Assistant"
description: "Triages application errors using the Sentry Web API (/api/0/issues/) and Sentry SDK breadcrumb data. Groups issues by stack trace similarity using Sentry fingerprinting rules and queries release health via the /api/0/organizations/{org}/releases/ endpoint."
category: "Runbooks & Diagnostics"
framework: "Claude Agents"
verification: security_reviewed
source: "https://github.com/getsentry/sentry"
tool_ecosystem:
  tool: sentry
  github_stars: 43437
  npm_weekly_downloads: 16379655
  github_repo: getsentry/sentry
  maintained: true
---
# Sentry Error Triage Assistant

Triages application errors using the Sentry Web API (/api/0/issues/) and Sentry SDK breadcrumb data. Groups issues by stack trace similarity using Sentry fingerprinting rules and queries release health via the /api/0/organizations/{org}/releases/ endpoint.

## Overview

The Sentry Error Triage Assistant skill automates the analysis and prioritization of application errors captured by Sentry. It queries the Sentry Web API endpoint /api/0/issues/ to retrieve issue details including event counts, user impact metrics, first and last seen timestamps, and assigned ownership based on CODEOWNERS integration.

This skill analyzes SDK-captured breadcrumb data to reconstruct user journeys leading to errors, identifying common trigger patterns across multiple error occurrences. It uses Sentry fingerprinting rules to group related issues and detect duplicate reports that may appear as separate entries due to minor stack trace variations across deployments.

Release health monitoring is provided through the /api/0/organizations/{org}/releases/ endpoint, correlating error spikes with specific release versions and identifying regression introduction points. The skill tracks crash-free session rates and adoption metrics to assess the urgency of newly introduced errors.

Triage output includes severity classifications based on user impact (unique users affected), frequency trends, and business-critical path analysis. The skill generates recommended actions including issue assignment suggestions based on code ownership, links to relevant source code via Sentry source map integration, and suggested Sentry alert rule configurations for similar future issues.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill sentry-error-triage-assistant
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill sentry-error-triage-assistant -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill sentry-error-triage-assistant -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill sentry-error-triage-assistant -a codex
```

### OpenClaw

```bash
clawhub install sentry-error-triage-assistant
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sentry-error-triage-assistant/)
