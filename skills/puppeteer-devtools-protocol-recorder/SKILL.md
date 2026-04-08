---
title: Puppeteer DevTools Protocol Recorder
description: The Puppeteer DevTools Protocol Recorder uses Puppeteer’s page.createCDPSession()
  to directly interface with Chrome’s DevTools Protocol domains for comprehensive
  browser telemetry capture. It enables Network domain events (requestWillBeSent,
  responseReceived, loadingFinished) for full HAR generation, Performance domain for
  runtime metrics (ScriptDuration, LayoutDuration, RecalcStyleDuration), and Accessibility
  domain for full accessibility tree snapshots. The agent records sessions as timestamped
  CDP event logs that can be replayed for deterministic testing. It captures heap
  snapshots via HeapProfiler.takeHeapSnapshot, CSS coverage via CSS.startRuleUsageTracking,
  and JavaScript execution contexts via Runtime.executionContextCreated. For CI integration,
  recorded sessions serve as regression baselines with replayed sessions comparing
  network waterfall timing, layout shift scores (CLS), and accessibility tree diffs
  against recorded baselines. Exports include HAR 1.2 format, Chrome trace JSON for
  chrome://tracing, and JUnit XML for CI test reporters.
verification: security_reviewed
source: https://github.com/puppeteer/puppeteer
category:
- Developer Tools
framework:
- Cursor
tool_ecosystem:
  github_repo: puppeteer/puppeteer
  github_stars: 94012
---

# Puppeteer DevTools Protocol Recorder

The Puppeteer DevTools Protocol Recorder uses Puppeteer’s page.createCDPSession() to directly interface with Chrome’s DevTools Protocol domains for comprehensive browser telemetry capture. It enables Network domain events (requestWillBeSent, responseReceived, loadingFinished) for full HAR generation, Performance domain for runtime metrics (ScriptDuration, LayoutDuration, RecalcStyleDuration), and Accessibility domain for full accessibility tree snapshots. The agent records sessions as timestamped CDP event logs that can be replayed for deterministic testing. It captures heap snapshots via HeapProfiler.takeHeapSnapshot, CSS coverage via CSS.startRuleUsageTracking, and JavaScript execution contexts via Runtime.executionContextCreated. For CI integration, recorded sessions serve as regression baselines with replayed sessions comparing network waterfall timing, layout shift scores (CLS), and accessibility tree diffs against recorded baselines. Exports include HAR 1.2 format, Chrome trace JSON for chrome://tracing, and JUnit XML for CI test reporters.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-devtools-protocol-recorder/)
