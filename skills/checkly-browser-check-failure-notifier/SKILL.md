---
title: "Checkly Browser Check Failure Notifier"
description: "The Checkly Browser Check Failure Notifier integrates with the Checkly Management API to monitor browser check execution results in real time. It polls the /v1/check-results endpoint filtered by checkType=BROWSER and hasFailures=true, extracting detailed failure information including Playwright trace file URLs, failure screenshots, and assertion error messages. When a browser check fails, the skill compiles a notification bundle with the check name, datacenter location, response timing breakdown, and a direct link to the Checkly dashboard for the failed run. Notifications are dispatched via the Checkly Alert Channels API or directly to Slack, Discord, or email. The skill supports grouping sequential failures to avoid alert storms and tracks check degradation patterns where response times increase without full failure. It also integrates with Checkly&#8217;s CLI check results to surface failures from CI/CD pipeline runs, parsing the JSON output format from the checkly test command."
source: "https://github.com/checkly/checkly-cli"
verification: "security_reviewed"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "checkly/checkly-cli"
  github_stars: 92
---

# Checkly Browser Check Failure Notifier

The Checkly Browser Check Failure Notifier integrates with the Checkly Management API to monitor browser check execution results in real time. It polls the /v1/check-results endpoint filtered by checkType=BROWSER and hasFailures=true, extracting detailed failure information including Playwright trace file URLs, failure screenshots, and assertion error messages. When a browser check fails, the skill compiles a notification bundle with the check name, datacenter location, response timing breakdown, and a direct link to the Checkly dashboard for the failed run. Notifications are dispatched via the Checkly Alert Channels API or directly to Slack, Discord, or email. The skill supports grouping sequential failures to avoid alert storms and tracks check degradation patterns where response times increase without full failure. It also integrates with Checkly&#8217;s CLI check results to surface failures from CI/CD pipeline runs, parsing the JSON output format from the checkly test command.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/checkly-browser-check-failure-notifier/)
