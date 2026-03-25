---
name: "Playwright Test Report to Slack"
description: "Parses Playwright HTML and JSON test reports and posts structured summaries to Slack using the Slack Web API. Reads test results from the playwright-report directory, extracts pass/fail/flaky counts using the @playwright/test reporter API, and posts rich Block Kit messages with test suite breakdowns via chat.postMessage."
category: "CI/CD Integrations"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/playwright-test-report-to-slack/"
tool_ecosystem:
  tool: "playwright"
  github_stars: 84938
  npm_weekly_downloads: 39806814
  github_repo: "microsoft/playwright"
  license: "Apache-2.0"
  maintained: true
---

# Playwright Test Report to Slack

Parses Playwright HTML and JSON test reports and posts structured summaries to Slack using the Slack Web API. Reads test results from the playwright-report directory, extracts pass/fail/flaky counts using the @playwright/test reporter API, and posts rich Block Kit messages with test suite breakdowns via chat.postMessage.

## Overview

This skill automates Playwright test result reporting to Slack by parsing HTML and JSON reports from the playwright-report output directory. It uses the @playwright/test reporter API to extract per-suite pass, fail, flaky, and skipped counts along with failure messages and screenshot attachments. Results are formatted as Slack Block Kit messages with collapsible sections for each test file, inline failure details, and links to the full Playwright HTML report hosted on a configured URL. The skill sends messages via the Slack Web API chat.postMessage endpoint using a bot token with channels:write permission. For CI environments it reads the Playwright JSON report from stdin or a configurable path, and posts thread replies for subsequent runs to keep channels organized. It also supports uploading screenshots for failed tests as Slack file uploads using files.uploadV2. Configurable thresholds trigger @channel alerts for high failure rates.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill playwright-test-report-to-slack
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill playwright-test-report-to-slack -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill playwright-test-report-to-slack -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill playwright-test-report-to-slack -a codex
```

### OpenClaw

```bash
clawhub install playwright-test-report-to-slack
```

## Source

- Marketplace: https://agentskillexchange.com/skills/playwright-test-report-to-slack/
