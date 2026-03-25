---
name: "Checkly Browser Check Failure Notifier"
description: "Monitors Checkly browser checks via the Checkly Management API and notifies teams on Playwright test failures. Extracts failure screenshots, trace URLs, and degraded check results."
category: "40"
framework: "33"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/checkly-browser-check-failure-notifier/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "playwright"  # from ase_tool_match
  github_stars: 84938  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 39806814  # from ase_npm_downloads
  github_repo: "microsoft/playwright"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
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
