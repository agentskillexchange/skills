---
name: "Puppeteer DevTools Protocol Recorder"
description: "Records and replays Chrome DevTools Protocol (CDP) sessions via Puppeteer's CDPSession API, captures Network, Performance, and Accessibility domain events, and exports HAR-compatible traces for CI regression testing."
category: "Developer Tools"
framework: "Cursor"
verification: security_reviewed
source: "https://github.com/puppeteer/puppeteer"
tool_ecosystem:
  tool: puppeteer
  github_repo: puppeteer/puppeteer
  github_stars: 93971
  license: Apache-2.0
  maintained: true
---
# Puppeteer DevTools Protocol Recorder

Records and replays Chrome DevTools Protocol (CDP) sessions via Puppeteer's CDPSession API, captures Network, Performance, and Accessibility domain events, and exports HAR-compatible traces for CI regression testing.

## Overview

The Puppeteer DevTools Protocol Recorder uses Puppeteer's page.createCDPSession() to directly interface with Chrome's DevTools Protocol domains for comprehensive browser telemetry capture. It enables Network domain events (requestWillBeSent, responseReceived, loadingFinished) for full HAR generation, Performance domain for runtime metrics (ScriptDuration, LayoutDuration, RecalcStyleDuration), and Accessibility domain for full accessibility tree snapshots. The agent records sessions as timestamped CDP event logs that can be replayed for deterministic testing. It captures heap snapshots via HeapProfiler.takeHeapSnapshot, CSS coverage via CSS.startRuleUsageTracking, and JavaScript execution contexts via Runtime.executionContextCreated. For CI integration, recorded sessions serve as regression baselines with replayed sessions comparing network waterfall timing, layout shift scores (CLS), and accessibility tree diffs against recorded baselines. Exports include HAR 1.2 format, Chrome trace JSON for chrome://tracing, and JUnit XML for CI test reporters.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill puppeteer-devtools-protocol-recorder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill puppeteer-devtools-protocol-recorder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill puppeteer-devtools-protocol-recorder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill puppeteer-devtools-protocol-recorder -a codex
```

### OpenClaw

```bash
clawhub install puppeteer-devtools-protocol-recorder
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-devtools-protocol-recorder/)
