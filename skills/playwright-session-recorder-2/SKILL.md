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
---

# Playwright Session Recorder

The Playwright Session Recorder skill leverages the Playwright codegen engine to capture full browser interaction sessions in real time. It hooks into page navigation, click events, form submissions, and AJAX requests to produce clean, replayable TypeScript or Python test scripts.

Key capabilities include automatic HAR file generation for network traffic analysis, DOM snapshot capture at configurable intervals, and intelligent selector generation that prefers data-testid attributes over fragile CSS paths. The skill supports multi-tab recording, iframe traversal, and authentication flow capture with credential masking.

Output formats include Playwright Test files, raw JSON action logs, and Markdown session summaries. Integration with CI pipelines allows recorded sessions to become regression tests automatically. The recorder handles cookie consent dialogs, popup blockers, and CAPTCHA pauses gracefully.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-session-recorder-2/)
