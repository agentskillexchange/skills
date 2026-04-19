---
title: "Puppeteer DevTools Protocol Recorder"
description: "The Puppeteer DevTools Protocol Recorder uses Puppeteer&#8217;s page.createCDPSession() to directly interface with Chrome&#8217;s DevTools Protocol domains for comprehensive browser telemetry capture. It enables Network domain events (requestWillBeSent, responseReceived, loadingFinished) for full HAR generation, Performance domain for runtime metrics (ScriptDuration, LayoutDuration, RecalcStyleDuration), and Accessibility domain for full accessibility tree snapshots. The agent records sessions as timestamped CDP event logs that can be replayed for deterministic testing. It captures heap snapshots via HeapProfiler.takeHeapSnapshot, CSS coverage via CSS.startRuleUsageTracking, and JavaScript execution contexts via Runtime.executionContextCreated. For CI integration, recorded sessions serve as regression baselines with replayed sessions comparing network waterfall timing, layout shift scores (CLS), and accessibility tree diffs against recorded baselines. Exports include HAR 1.2 format, Chrome trace JSON for chrome://tracing, and JUnit XML for CI test reporters."
source: "https://github.com/puppeteer/puppeteer"
verification: "security_reviewed"
category:
  - "Developer Tools"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "puppeteer/puppeteer"
  github_stars: 94051
---

# Puppeteer DevTools Protocol Recorder

The Puppeteer DevTools Protocol Recorder uses Puppeteer&#8217;s page.createCDPSession() to directly interface with Chrome&#8217;s DevTools Protocol domains for comprehensive browser telemetry capture. It enables Network domain events (requestWillBeSent, responseReceived, loadingFinished) for full HAR generation, Performance domain for runtime metrics (ScriptDuration, LayoutDuration, RecalcStyleDuration), and Accessibility domain for full accessibility tree snapshots. The agent records sessions as timestamped CDP event logs that can be replayed for deterministic testing. It captures heap snapshots via HeapProfiler.takeHeapSnapshot, CSS coverage via CSS.startRuleUsageTracking, and JavaScript execution contexts via Runtime.executionContextCreated. For CI integration, recorded sessions serve as regression baselines with replayed sessions comparing network waterfall timing, layout shift scores (CLS), and accessibility tree diffs against recorded baselines. Exports include HAR 1.2 format, Chrome trace JSON for chrome://tracing, and JUnit XML for CI test reporters.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-devtools-protocol-recorder/)
