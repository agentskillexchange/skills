---
title: "Debug live Chromium sessions with browser-debugger-cli"
description: "Pull DOM, console, network, and CDP telemetry from a live Chromium session when an agent needs to debug a failing browser task."
verification: "security_reviewed"
source: "https://github.com/szymdzum/browser-debugger-cli"
author: "szymdzum"
publisher_type: "individual"
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

Pull DOM, console, network, and CDP telemetry from a live Chromium session when an agent needs to debug a failing browser task.

## Prerequisites

Node.js, npm, Chromium-based browser

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with `npm install -g browser-debugger-cli@alpha`, then start a session with `bdg <url>` and use the CLI or CDP subcommands to inspect the live browser state.
```

## Documentation

- https://github.com/szymdzum/browser-debugger-cli/wiki/Getting-Started

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/debug-live-chromium-sessions-with-browser-debugger-cli/)
