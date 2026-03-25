---
name: "Playwright Session Recorder"
description: "Records browser sessions using Playwright codegen and exports replayable test scripts. Captures network HAR files alongside DOM snapshots for full session fidelity."
category: "Browser Automation"
framework: "Claude Code"
verification: listed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/playwright-session-recorder-2/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "playwright"  # from ase_tool_match
  github_stars: 84938  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 39806814  # from ase_npm_downloads
  github_repo: "microsoft/playwright"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Playwright Session Recorder

Records browser sessions using Playwright codegen and exports replayable test scripts. Captures network HAR files alongside DOM snapshots for full session fidelity.

## Overview

The Playwright Session Recorder skill leverages the Playwright codegen engine to capture full browser interaction sessions in real time. It hooks into page navigation, click events, form submissions, and AJAX requests to produce clean, replayable TypeScript or Python test scripts.

Key capabilities include automatic HAR file generation for network traffic analysis, DOM snapshot capture at configurable intervals, and intelligent selector generation that prefers data-testid attributes over fragile CSS paths. The skill supports multi-tab recording, iframe traversal, and authentication flow capture with credential masking.

Output formats include Playwright Test files, raw JSON action logs, and Markdown session summaries. Integration with CI pipelines allows recorded sessions to become regression tests automatically. The recorder handles cookie consent dialogs, popup blockers, and CAPTCHA pauses gracefully.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill playwright-session-recorder-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill playwright-session-recorder-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill playwright-session-recorder-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill playwright-session-recorder-2 -a codex
```

### OpenClaw

```bash
clawhub install playwright-session-recorder-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/playwright-session-recorder-2/
