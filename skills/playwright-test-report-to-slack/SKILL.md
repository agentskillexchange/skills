---
title: "Playwright Test Report to Slack"
description: "Parses Playwright HTML and JSON test reports and posts structured summaries to Slack using the Slack Web API. Reads test results from the playwright-report directory, extracts pass/fail/flaky counts using the @playwright/test reporter API, and posts rich Block Kit messages with test suite breakdowns via chat.postMessage."
verification: "security_reviewed"
source: "https://github.com/microsoft/playwright"
category:
  - "CI/CD Integrations"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "microsoft/playwright"
  github_stars: 86911
  npm_package: "playwright"
  npm_weekly_downloads: 188960132
---

# Playwright Test Report to Slack

Parses Playwright HTML and JSON test reports and posts structured summaries to Slack using the Slack Web API. Reads test results from the playwright-report directory, extracts pass/fail/flaky counts using the @playwright/test reporter API, and posts rich Block Kit messages with test suite breakdowns via chat.postMessage.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/playwright-test-report-to-slack/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/playwright-test-report-to-slack
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/playwright-test-report-to-slack`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-test-report-to-slack/)
