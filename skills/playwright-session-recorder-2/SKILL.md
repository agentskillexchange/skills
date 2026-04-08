---
title: Playwright Session Recorder
description: The Playwright Session Recorder skill leverages the Playwright codegen
  engine to capture full browser interaction sessions in real time. It hooks into
  page navigation, click events, form submissions, and AJAX requests to produce clean,
  replayable TypeScript or Python test scripts. Key capabilities include automatic
  HAR file generation for network traffic analysis, DOM snapshot capture at configurable
  intervals, and intelligent selector generation that prefers data-testid attributes
  over fragile CSS paths. The skill supports multi-tab recording, iframe traversal,
  and authentication flow capture with credential masking. Output formats include
  Playwright Test files, raw JSON action logs, and Markdown session summaries. Integration
  with CI pipelines allows recorded sessions to become regression tests automatically.
  The recorder handles cookie consent dialogs, popup blockers, and CAPTCHA pauses
  gracefully.
verification: security_reviewed
source: https://agentskillexchange.com/skills/playwright-session-recorder-2/
category:
- Browser Automation
framework:
- Claude Code
---

# Playwright Session Recorder

The Playwright Session Recorder skill leverages the Playwright codegen engine to capture full browser interaction sessions in real time. It hooks into page navigation, click events, form submissions, and AJAX requests to produce clean, replayable TypeScript or Python test scripts. Key capabilities include automatic HAR file generation for network traffic analysis, DOM snapshot capture at configurable intervals, and intelligent selector generation that prefers data-testid attributes over fragile CSS paths. The skill supports multi-tab recording, iframe traversal, and authentication flow capture with credential masking. Output formats include Playwright Test files, raw JSON action logs, and Markdown session summaries. Integration with CI pipelines allows recorded sessions to become regression tests automatically. The recorder handles cookie consent dialogs, popup blockers, and CAPTCHA pauses gracefully.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-session-recorder-2/)
