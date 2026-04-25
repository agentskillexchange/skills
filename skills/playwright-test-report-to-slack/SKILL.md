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

This skill automates Playwright test result reporting to Slack by parsing HTML and JSON reports from the playwright-report output directory. It uses the @playwright/test reporter API to extract per-suite pass, fail, flaky, and skipped counts along with failure messages and screenshot attachments. Results are formatted as Slack Block Kit messages with collapsible sections for each test file, inline failure details, and links to the full Playwright HTML report hosted on a configured URL. The skill sends messages via the Slack Web API chat.postMessage endpoint using a bot token with channels:write permission. For CI environments it reads the Playwright JSON report from stdin or a configurable path, and posts thread replies for subsequent runs to keep channels organized. It also supports uploading screenshots for failed tests as Slack file uploads using files.uploadV2. Configurable thresholds trigger @channel alerts for high failure rates.

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
