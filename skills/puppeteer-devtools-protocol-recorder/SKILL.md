---
title: "Puppeteer DevTools Protocol Recorder"
description: "Records and replays Chrome DevTools Protocol (CDP) sessions via Puppeteer’s CDPSession API, captures Network, Performance, and Accessibility domain events, and exports HAR-compatible traces for CI regression testing."
verification: "security_reviewed"
source: "https://github.com/puppeteer/puppeteer"
category:
  - "Developer Tools"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "puppeteer/puppeteer"
  github_stars: 94051
---

# Puppeteer DevTools Protocol Recorder

The Puppeteer DevTools Protocol Recorder uses Puppeteer’s page.createCDPSession() to directly interface with Chrome’s DevTools Protocol domains for comprehensive browser telemetry capture. It enables Network domain events (requestWillBeSent, responseReceived, loadingFinished) for full HAR generation, Performance domain for runtime metrics (ScriptDuration, LayoutDuration, RecalcStyleDuration), and Accessibility domain for full accessibility tree snapshots. The agent records sessions as timestamped CDP event logs that can be replayed for deterministic testing. It captures heap snapshots via HeapProfiler.takeHeapSnapshot, CSS coverage via CSS.startRuleUsageTracking, and JavaScript execution contexts via Runtime.executionContextCreated. For CI integration, recorded sessions serve as regression baselines with replayed sessions comparing network waterfall timing, layout shift scores (CLS), and accessibility tree diffs against recorded baselines. Exports include HAR 1.2 format, Chrome trace JSON for chrome://tracing, and JUnit XML for CI test reporters.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-devtools-protocol-recorder/)
