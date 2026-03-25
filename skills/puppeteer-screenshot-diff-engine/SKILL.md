---
name: "Puppeteer Screenshot Diff Engine"
description: "Visual regression testing using Puppeteer page.screenshot() with pixelmatch comparison. Leverages CDP sessions via page.createCDPSession() for precise viewport emulation and network throttling."
category: "Browser Automation"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/puppeteer-screenshot-diff-engine/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "puppeteer"  # from ase_tool_match
  github_stars: 93932  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 8696130  # from ase_npm_downloads
  github_repo: "puppeteer/puppeteer"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Puppeteer Screenshot Diff Engine

Visual regression testing using Puppeteer page.screenshot() with pixelmatch comparison. Leverages CDP sessions via page.createCDPSession() for precise viewport emulation and network throttling.

## Overview

The Puppeteer Screenshot Diff Engine automates visual regression testing by capturing page screenshots through Puppeteer’s page.screenshot({ fullPage: true }) API and comparing them pixel-by-pixel using the pixelmatch library with configurable threshold values.

It establishes Chrome DevTools Protocol sessions via page.createCDPSession() to precisely control device emulation through Emulation.setDeviceMetricsOverride and simulate network conditions with Network.emulateNetworkConditions. This ensures screenshots are captured under reproducible conditions across CI runs.

The engine supports baseline management with automatic golden image updates, generates HTML diff reports highlighting changed regions with bounding boxes, and integrates with page.waitForSelector() and page.waitForNetworkIdle() to ensure pages are fully rendered before capture. It handles dynamic content by masking regions through CSS injection via page.addStyleTag().

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill puppeteer-screenshot-diff-engine
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill puppeteer-screenshot-diff-engine -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill puppeteer-screenshot-diff-engine -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill puppeteer-screenshot-diff-engine -a codex
```

### OpenClaw

```bash
clawhub install puppeteer-screenshot-diff-engine
```

## Source

- Marketplace: https://agentskillexchange.com/skills/puppeteer-screenshot-diff-engine/
