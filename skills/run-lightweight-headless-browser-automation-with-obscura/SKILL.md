---
title: "Run lightweight headless browser automation with Obscura"
description: "Use Obscura as a lightweight headless browser runtime for agent scraping, page inspection, parallel extraction, and CDP-driven Playwright or Puppeteer workflows."
verification: "listed"
source: "https://github.com/h4ckf0r0day/obscura"
author: "h4ckf0r0day"
publisher_type: "open_source_project"
category:
  - "Browser Automation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "h4ckf0r0day/obscura"
  github_stars: 16139
---

# Run lightweight headless browser automation with Obscura

Use Obscura as a lightweight headless browser runtime for agent scraping, page inspection, parallel extraction, and CDP-driven Playwright or Puppeteer workflows.

## Prerequisites

Obscura binary or Docker image; optional puppeteer-core or playwright-core for CDP-driven automation; optional proxy configuration for scraping workflows

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Download the latest platform archive from https://github.com/h4ckf0r0day/obscura/releases, extract the obscura and obscura-worker binaries together, or run docker run -d --name obscura -p 127.0.0.1:9222:9222 h4ckf0r0day/obscura. Build from source with git clone https://github.com/h4ckf0r0day/obscura.git && cd obscura && cargo build --release.
```

## Documentation

- https://github.com/h4ckf0r0day/obscura

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-lightweight-headless-browser-automation-with-obscura/)
