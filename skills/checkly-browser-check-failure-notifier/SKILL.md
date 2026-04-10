---
name: Checkly Browser Check Failure Notifier
description: Monitors Checkly browser checks via the Checkly Management API and notifies
  teams on Playwright test failures. Extracts failure screenshots, trace URLs, and
  degraded check results.
verification: security_reviewed
source: https://github.com/checkly/checkly-cli
category:
- Monitoring &amp; Alerts
framework:
- Claude Code
tool_ecosystem:
  github_repo: checkly/checkly-cli
  github_stars: 92
---
# Checkly Browser Check Failure Notifier

The Checkly Browser Check Failure Notifier integrates with the Checkly Management API to monitor browser check execution results in real time. It polls the /v1/check-results endpoint filtered by checkType=BROWSER and hasFailures=true, extracting detailed failure information including Playwright trace file URLs, failure screenshots, and assertion error messages. When a browser check fails, the skill compiles a notification bundle with the check name, datacenter location, response timing breakdown, and a direct link to the Checkly dashboard for the failed run. Notifications are dispatched via the Checkly Alert Channels API or directly to Slack, Discord, or email. The skill supports grouping sequential failures to avoid alert storms and tracks check degradation patterns where response times increase without full failure. It also integrates with Checkly's CLI check results to surface failures from CI/CD pipeline runs, parsing the JSON output format from the checkly test command.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/checkly-browser-check-failure-notifier/)
