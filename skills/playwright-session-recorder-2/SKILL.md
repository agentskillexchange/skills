---
title: "Playwright Session Recorder"
description: "Records browser sessions using Playwright codegen and exports replayable test scripts. Captures network HAR files alongside DOM snapshots for full session fidelity."
verification: security_reviewed
source: "https://github.com/microsoft/playwright"
category:
  - "Browser Automation"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "microsoft/playwright"
  github_stars: 86409
  npm_package: "playwright"
  npm_weekly_downloads: 47883561
  license: "Apache-2.0"
---

# Playwright Session Recorder

The Playwright Session Recorder skill leverages the Playwright codegen engine to capture full browser interaction sessions in real time. It hooks into page navigation, click events, form submissions, and AJAX requests to produce clean, replayable TypeScript or Python test scripts.

Key capabilities include automatic HAR file generation for network traffic analysis, DOM snapshot capture at configurable intervals, and intelligent selector generation that prefers data-testid attributes over fragile CSS paths. The skill supports multi-tab recording, iframe traversal, and authentication flow capture with credential masking.

Output formats include Playwright Test files, raw JSON action logs, and Markdown session summaries. Integration with CI pipelines allows recorded sessions to become regression tests automatically. The recorder handles cookie consent dialogs, popup blockers, and CAPTCHA pauses gracefully.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/playwright-session-recorder-2
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/playwright-session-recorder-2` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-session-recorder-2/)
