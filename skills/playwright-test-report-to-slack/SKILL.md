---
name: "Playwright Test Report to Slack"
slug: "playwright-test-report-to-slack"
description: "Parses Playwright HTML and JSON test reports and posts structured summaries to Slack using the Slack Web API. Reads test results from the playwright-report directory, extracts pass/fail/flaky counts using the @playwright/test reporter API, and posts rich Block Kit messages with test suite breakdowns via chat.postMessage."
github_stars: 86911
verification: "security_reviewed"
source: "https://github.com/microsoft/playwright"
author: "Microsoft"
category: "CI/CD Integrations"
framework: "ChatGPT Agents"
tool_ecosystem:
  github_repo: "microsoft/playwright"
  github_stars: 86911
  npm_package: "playwright"
  npm_weekly_downloads: 188960132
---

# Playwright Test Report to Slack

Parses Playwright HTML and JSON test reports and posts structured summaries to Slack using the Slack Web API. Reads test results from the playwright-report directory, extracts pass/fail/flaky counts using the @playwright/test reporter API, and posts rich Block Kit messages with test suite breakdowns via chat.postMessage.

## Prerequisites

Node.js

## Installation

Use the upstream install or setup path that matches your environment:
- npm install -g @playwright/cli@latest
- npm i playwright

Requirements and caveats from upstream:
- Playwright is also available for [Python](https://playwright.dev/python/docs/intro), [.NET](https://playwright.dev/dotnet/docs/intro), and [Java](https://playwright.dev/java/docs/intro).

Basic usage or getting-started notes:
- bash
- Optionally install skills for richer agent integration:
- playwright-cli install --skills

- Source: https://github.com/microsoft/playwright
- Extracted from upstream docs: https://raw.githubusercontent.com/microsoft/playwright/HEAD/README.md

## Documentation

- https://playwright.dev/docs/test-reporters

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-test-report-to-slack/)
