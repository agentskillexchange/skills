---
title: "Checkly Browser Check Failure Notifier"
description: "Monitors Checkly browser checks via the Checkly Management API and notifies teams on Playwright test failures. Extracts failure screenshots, trace URLs, and degraded check results."
slug: "checkly-browser-check-failure-notifier"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://github.com/checkly/checkly-cli"
tool_ecosystem:
  github_repo: "checkly/checkly-cli"
  github_stars: 92
---

# Checkly Browser Check Failure Notifier

Monitors Checkly browser checks via the Checkly Management API and notifies teams on Playwright test failures. Extracts failure screenshots, trace URLs, and degraded check results.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install checkly-browser-check-failure-notifier
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Checkly Browser Check Failure Notifier integrates with the Checkly Management API to monitor browser check execution results in real time. It polls the /v1/check-results endpoint filtered by checkType=BROWSER and hasFailures=true, extracting detailed failure information including Playwright trace file URLs, failure screenshots, and assertion error messages. When a browser check fails, the skill compiles a notification bundle with the check name, datacenter location, response timing breakdown, and a direct link to the Checkly dashboard for the failed run. Notifications are dispatched via the Checkly Alert Channels API or directly to Slack, Discord, or email. The skill supports grouping sequential failures to avoid alert storms and tracks check degradation patterns where response times increase without full failure. It also integrates with Checkly’s CLI check results to surface failures from CI/CD pipeline runs, parsing the JSON output format from the checkly test command.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/checkly-browser-check-failure-notifier/)
