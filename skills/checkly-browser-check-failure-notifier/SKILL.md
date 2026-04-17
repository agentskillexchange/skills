---
title: "Checkly Browser Check Failure Notifier"
description: "Monitors Checkly browser checks via the Checkly Management API and notifies teams on Playwright test failures. Extracts failure screenshots, trace URLs, and degraded check results."
verification: security_reviewed
source: "https://github.com/checkly/checkly-cli"
category:
  - "Monitoring & Alerts"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "checkly/checkly-cli"
  github_stars: 92
---

# Checkly Browser Check Failure Notifier

The Checkly Browser Check Failure Notifier integrates with the Checkly Management API to monitor browser check execution results in real time. It polls the /v1/check-results endpoint filtered by checkType=BROWSER and hasFailures=true, extracting detailed failure information including Playwright trace file URLs, failure screenshots, and assertion error messages. When a browser check fails, the skill compiles a notification bundle with the check name, datacenter location, response timing breakdown, and a direct link to the Checkly dashboard for the failed run. Notifications are dispatched via the Checkly Alert Channels API or directly to Slack, Discord, or email. The skill supports grouping sequential failures to avoid alert storms and tracks check degradation patterns where response times increase without full failure. It also integrates with Checkly’s CLI check results to surface failures from CI/CD pipeline runs, parsing the JSON output format from the checkly test command.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/checkly-browser-check-failure-notifier
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/checkly-browser-check-failure-notifier` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/checkly-browser-check-failure-notifier/)
