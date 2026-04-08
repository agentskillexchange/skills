---
title: Playwright Test Report to Slack
description: This skill automates Playwright test result reporting to Slack by parsing
  HTML and JSON reports from the playwright-report output directory. It uses the @playwright/test
  reporter API to extract per-suite pass, fail, flaky, and skipped counts along with
  failure messages and screenshot attachments. Results are formatted as Slack Block
  Kit messages with collapsible sections for each test file, inline failure details,
  and links to the full Playwright HTML report hosted on a configured URL. The skill
  sends messages via the Slack Web API chat.postMessage endpoint using a bot token
  with channels:write permission. For CI environments it reads the Playwright JSON
  report from stdin or a configurable path, and posts thread replies for subsequent
  runs to keep channels organized. It also supports uploading screenshots for failed
  tests as Slack file uploads using files.uploadV2. Configurable thresholds trigger
  @channel alerts for high failure rates.
verification: security_reviewed
source: https://agentskillexchange.com/skills/playwright-test-report-to-slack/
category:
- CI/CD Integrations
framework:
- ChatGPT Agents
---

# Playwright Test Report to Slack

This skill automates Playwright test result reporting to Slack by parsing HTML and JSON reports from the playwright-report output directory. It uses the @playwright/test reporter API to extract per-suite pass, fail, flaky, and skipped counts along with failure messages and screenshot attachments. Results are formatted as Slack Block Kit messages with collapsible sections for each test file, inline failure details, and links to the full Playwright HTML report hosted on a configured URL. The skill sends messages via the Slack Web API chat.postMessage endpoint using a bot token with channels:write permission. For CI environments it reads the Playwright JSON report from stdin or a configurable path, and posts thread replies for subsequent runs to keep channels organized. It also supports uploading screenshots for failed tests as Slack file uploads using files.uploadV2. Configurable thresholds trigger @channel alerts for high failure rates.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-test-report-to-slack/)
