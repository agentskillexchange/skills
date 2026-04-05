---
name: "Puppeteer Screenshot Diff Engine"
description: "Visual regression testing using Puppeteer page.screenshot() with pixelmatch comparison. Leverages CDP sessions via page.createCDPSession() for precise viewport emulation and network throttling."
category: "Browser Automation"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/puppeteer-screenshot-diff-engine/"
---
# Puppeteer Screenshot Diff Engine

Visual regression testing using Puppeteer page.screenshot() with pixelmatch comparison. Leverages CDP sessions via page.createCDPSession() for precise viewport emulation and network throttling.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-screenshot-diff-engine/)
