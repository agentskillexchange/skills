---
title: "Playwright Test Report to Slack"
description: "This skill automates Playwright test result reporting to Slack by parsing HTML and JSON reports from the playwright-report output directory. It uses the @playwright/test reporter API to extract per-suite pass, fail, flaky, and skipped counts along with failure messages and screenshot attachments. Results are formatted as Slack Block Kit messages with collapsible sections for each test file, inline failure details, and links to the full Playwright HTML report hosted on a configured URL. The skill sends messages via the Slack Web API chat.postMessage endpoint using a bot token with channels:write permission. For CI environments it reads the Playwright JSON report from stdin or a configurable path, and posts thread replies for subsequent runs to keep channels organized. It also supports uploading screenshots for failed tests as Slack file uploads using files.uploadV2. Configurable thresholds trigger @channel alerts for high failure rates."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/playwright-test-report-to-slack/"
framework:
  - "ChatGPT Agents"
---

# Playwright Test Report to Slack

This skill automates Playwright test result reporting to Slack by parsing HTML and JSON reports from the playwright-report output directory. It uses the @playwright/test reporter API to extract per-suite pass, fail, flaky, and skipped counts along with failure messages and screenshot attachments. Results are formatted as Slack Block Kit messages with collapsible sections for each test file, inline failure details, and links to the full Playwright HTML report hosted on a configured URL. The skill sends messages via the Slack Web API chat.postMessage endpoint using a bot token with channels:write permission. For CI environments it reads the Playwright JSON report from stdin or a configurable path, and posts thread replies for subsequent runs to keep channels organized. It also supports uploading screenshots for failed tests as Slack file uploads using files.uploadV2. Configurable thresholds trigger @channel alerts for high failure rates.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/playwright-test-report-to-slack
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/playwright-test-report-to-slack` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-test-report-to-slack/)
