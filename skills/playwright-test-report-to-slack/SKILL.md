---
title: "Playwright Test Report to Slack"
description: "Parses Playwright HTML and JSON test reports and posts structured summaries to Slack using the Slack Web API. Reads test results from the playwright-report directory, extracts pass/fail/flaky counts using the @playwright/test reporter API, and posts rich Block Kit messages with test suite breakdowns via chat.postMessage."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/playwright-test-report-to-slack/"
category:
  - "CI/CD Integrations"
framework:
  - "ChatGPT Agents"
---

# Playwright Test Report to Slack

This skill automates Playwright test result reporting to Slack by parsing HTML and JSON reports from the playwright-report output directory. It uses the @playwright/test reporter API to extract per-suite pass, fail, flaky, and skipped counts along with failure messages and screenshot attachments. Results are formatted as Slack Block Kit messages with collapsible sections for each test file, inline failure details, and links to the full Playwright HTML report hosted on a configured URL. The skill sends messages via the Slack Web API chat.postMessage endpoint using a bot token with channels:write permission. For CI environments it reads the Playwright JSON report from stdin or a configurable path, and posts thread replies for subsequent runs to keep channels organized. It also supports uploading screenshots for failed tests as Slack file uploads using files.uploadV2. Configurable thresholds trigger @channel alerts for high failure rates.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-test-report-to-slack/)
