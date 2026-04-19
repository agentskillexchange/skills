---
title: "Playwright Session Recorder"
description: "The Playwright Session Recorder skill leverages the Playwright codegen engine to capture full browser interaction sessions in real time. It hooks into page navigation, click events, form submissions, and AJAX requests to produce clean, replayable TypeScript or Python test scripts. Key capabilities include automatic HAR file generation for network traffic analysis, DOM snapshot capture at configurable intervals, and intelligent selector generation that prefers data-testid attributes over fragile CSS paths. The skill supports multi-tab recording, iframe traversal, and authentication flow capture with credential masking. Output formats include Playwright Test files, raw JSON action logs, and Markdown session summaries. Integration with CI pipelines allows recorded sessions to become regression tests automatically. The recorder handles cookie consent dialogs, popup blockers, and CAPTCHA pauses gracefully."
source: "https://github.com/microsoft/playwright"
verification: "security_reviewed"
category:
  - "Browser Automation"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "microsoft/playwright"
  github_stars: 86409
  npm_package: "playwright"
  npm_weekly_downloads: 47883561
---

# Playwright Session Recorder

The Playwright Session Recorder skill leverages the Playwright codegen engine to capture full browser interaction sessions in real time. It hooks into page navigation, click events, form submissions, and AJAX requests to produce clean, replayable TypeScript or Python test scripts. Key capabilities include automatic HAR file generation for network traffic analysis, DOM snapshot capture at configurable intervals, and intelligent selector generation that prefers data-testid attributes over fragile CSS paths. The skill supports multi-tab recording, iframe traversal, and authentication flow capture with credential masking. Output formats include Playwright Test files, raw JSON action logs, and Markdown session summaries. Integration with CI pipelines allows recorded sessions to become regression tests automatically. The recorder handles cookie consent dialogs, popup blockers, and CAPTCHA pauses gracefully.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-session-recorder-2/)
