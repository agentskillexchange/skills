---
name: "Checkly Browser Check Failure Notifier"
description: "Monitors Checkly browser checks via the Checkly Management API and notifies teams on Playwright test failures. Extracts failure screenshots, trace URLs, and degraded check results."
category: "Monitoring & Alerts"
framework: "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/checkly-browser-check-failure-notifier/"
tool_ecosystem:
  tool: playwright
  github_stars: 84938
  npm_weekly_downloads: 39806814
  github_repo: microsoft/playwright
  license: Apache-2.0
  maintained: true
---

# Checkly Browser Check Failure Notifier

Monitors Checkly browser checks via the Checkly Management API and notifies teams on Playwright test failures. Extracts failure screenshots, trace URLs, and degraded check results.

## Overview

The Checkly Browser Check Failure Notifier integrates with the Checkly Management API to monitor browser check execution results in real time. It polls the /v1/check-results endpoint filtered by checkType=BROWSER and hasFailures=true, extracting detailed failure information including Playwright trace file URLs, failure screenshots, and assertion error messages. When a browser check fails, the skill compiles a notification bundle with the check name, datacenter location, response timing breakdown, and a direct link to the Checkly dashboard for the failed run. Notifications are dispatched via the Checkly Alert Channels API or directly to Slack, Discord, or email. The skill supports grouping sequential failures to avoid alert storms and tracks check degradation patterns where response times increase without full failure. It also integrates with Checkly’s CLI check results to surface failures from CI/CD pipeline runs, parsing the JSON output format from the checkly test command.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill checkly-browser-check-failure-notifier
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill checkly-browser-check-failure-notifier -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill checkly-browser-check-failure-notifier -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill checkly-browser-check-failure-notifier -a codex
```

### OpenClaw

```bash
clawhub install checkly-browser-check-failure-notifier
```

## Source

- Marketplace: https://agentskillexchange.com/skills/checkly-browser-check-failure-notifier/
