---
title: "Playwright Test Report to Slack"
description: "Parses Playwright HTML and JSON test reports and posts structured summaries to Slack using the Slack Web API. Reads test results from the playwright-report directory, extracts pass/fail/flaky counts using the @playwright/test reporter API, and posts rich Block Kit messages with test suite breakdowns via chat.postMessage."
verification: "security_reviewed"
source: "https://github.com/microsoft/playwright"
author: "Microsoft"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
npm init playwright@latest
```

## Documentation

- https://playwright.dev/docs/test-reporters

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-test-report-to-slack/)
