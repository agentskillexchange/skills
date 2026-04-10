---
title: "Puppeteer DevTools Protocol Recorder"
description: "Records and replays Chrome DevTools Protocol (CDP) sessions via Puppeteer’s CDPSession API, captures Network, Performance, and Accessibility domain events, and exports HAR-compatible traces for CI regression testing."
slug: "puppeteer-devtools-protocol-recorder"
category:
  - "Developer Tools"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://github.com/puppeteer/puppeteer"
tool_ecosystem:
  github_repo: "puppeteer/puppeteer"
  github_stars: 94051
listed: true
---

# Puppeteer DevTools Protocol Recorder

Records and replays Chrome DevTools Protocol (CDP) sessions via Puppeteer’s CDPSession API, captures Network, Performance, and Accessibility domain events, and exports HAR-compatible traces for CI regression testing.

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
clawhub install puppeteer-devtools-protocol-recorder
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Puppeteer DevTools Protocol Recorder uses Puppeteer’s page.createCDPSession() to directly interface with Chrome’s DevTools Protocol domains for comprehensive browser telemetry capture. It enables Network domain events (requestWillBeSent, responseReceived, loadingFinished) for full HAR generation, Performance domain for runtime metrics (ScriptDuration, LayoutDuration, RecalcStyleDuration), and Accessibility domain for full accessibility tree snapshots. The agent records sessions as timestamped CDP event logs that can be replayed for deterministic testing. It captures heap snapshots via HeapProfiler.takeHeapSnapshot, CSS coverage via CSS.startRuleUsageTracking, and JavaScript execution contexts via Runtime.executionContextCreated. For CI integration, recorded sessions serve as regression baselines with replayed sessions comparing network waterfall timing, layout shift scores (CLS), and accessibility tree diffs against recorded baselines. Exports include HAR 1.2 format, Chrome trace JSON for chrome://tracing, and JUnit XML for CI test reporters.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-devtools-protocol-recorder/)
