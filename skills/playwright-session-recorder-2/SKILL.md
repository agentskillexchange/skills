---
title: "Playwright Session Recorder"
description: "Records browser sessions using Playwright codegen and exports replayable test scripts. Captures network HAR files alongside DOM snapshots for full session fidelity."
slug: "playwright-session-recorder-2"
category:
  - "Browser Automation"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/playwright-session-recorder-2/"
---

# Playwright Session Recorder

Records browser sessions using Playwright codegen and exports replayable test scripts. Captures network HAR files alongside DOM snapshots for full session fidelity.

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
clawhub install playwright-session-recorder-2
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Playwright Session Recorder skill leverages the Playwright codegen engine to capture full browser interaction sessions in real time. It hooks into page navigation, click events, form submissions, and AJAX requests to produce clean, replayable TypeScript or Python test scripts.
Key capabilities include automatic HAR file generation for network traffic analysis, DOM snapshot capture at configurable intervals, and intelligent selector generation that prefers data-testid attributes over fragile CSS paths. The skill supports multi-tab recording, iframe traversal, and authentication flow capture with credential masking.
Output formats include Playwright Test files, raw JSON action logs, and Markdown session summaries. Integration with CI pipelines allows recorded sessions to become regression tests automatically. The recorder handles cookie consent dialogs, popup blockers, and CAPTCHA pauses gracefully.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-session-recorder-2/)
