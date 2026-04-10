---
title: "Playwright Test Report to Slack"
description: "Parses Playwright HTML and JSON test reports and posts structured summaries to Slack using the Slack Web API. Reads test results from the playwright-report directory, extracts pass/fail/flaky counts using the @playwright/test reporter API, and posts rich Block Kit messages with test suite breakdowns via chat.postMessage."
slug: "playwright-test-report-to-slack"
category:
  - "CI/CD Integrations"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/playwright-test-report-to-slack/"
---

# Playwright Test Report to Slack

Parses Playwright HTML and JSON test reports and posts structured summaries to Slack using the Slack Web API. Reads test results from the playwright-report directory, extracts pass/fail/flaky counts using the @playwright/test reporter API, and posts rich Block Kit messages with test suite breakdowns via chat.postMessage.

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
clawhub install playwright-test-report-to-slack
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill automates Playwright test result reporting to Slack by parsing HTML and JSON reports from the playwright-report output directory. It uses the @playwright/test reporter API to extract per-suite pass, fail, flaky, and skipped counts along with failure messages and screenshot attachments. Results are formatted as Slack Block Kit messages with collapsible sections for each test file, inline failure details, and links to the full Playwright HTML report hosted on a configured URL. The skill sends messages via the Slack Web API chat.postMessage endpoint using a bot token with channels:write permission. For CI environments it reads the Playwright JSON report from stdin or a configurable path, and posts thread replies for subsequent runs to keep channels organized. It also supports uploading screenshots for failed tests as Slack file uploads using files.uploadV2. Configurable thresholds trigger @channel alerts for high failure rates.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-test-report-to-slack/)
