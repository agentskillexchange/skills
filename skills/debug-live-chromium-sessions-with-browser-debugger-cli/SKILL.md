---
title: "Debug live Chromium sessions with browser-debugger-cli"
description: "Pull DOM, console, network, and CDP telemetry from a live Chromium session when an agent needs to debug a failing browser task."
verification: listed
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

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/debug-live-chromium-sessions-with-browser-debugger-cli
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/debug-live-chromium-sessions-with-browser-debugger-cli` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/debug-live-chromium-sessions-with-browser-debugger-cli/)
