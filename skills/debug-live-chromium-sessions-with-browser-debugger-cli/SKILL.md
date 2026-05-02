---
title: "Debug live Chromium sessions with browser-debugger-cli"
description: "Pull DOM, console, network, and CDP telemetry from a live Chromium session when an agent needs to debug a failing browser task."
verification: "listed"
source: "https://github.com/szymdzum/browser-debugger-cli"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "szymdzum/browser-debugger-cli"
  github_stars: 124
  npm_package: "browser-debugger-cli"
  npm_weekly_downloads: 582
---

# Debug live Chromium sessions with browser-debugger-cli

Use browser-debugger-cli when an agent needs to inspect a live Chromium tab by pulling DOM snapshots, console errors, network activity, cookies, or raw CDP output during a failing browser task. Invoke it instead of using the browser normally when the job is diagnosis and telemetry collection, not routine browsing or end-to-end automation. The scope boundary is tight and skill-shaped: this is a live-session debugging workflow around Chrome DevTools Protocol, not a generic browser platform, SDK, or framework listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/debug-live-chromium-sessions-with-browser-debugger-cli/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/debug-live-chromium-sessions-with-browser-debugger-cli
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/debug-live-chromium-sessions-with-browser-debugger-cli`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/debug-live-chromium-sessions-with-browser-debugger-cli/)
