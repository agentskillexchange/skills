---
name: "Stagehand Browser Automation SDK"
slug: "stagehand-browser-automation-sdk"
description: "Stagehand is Browserbase's browser automation SDK for combining natural-language actions with deterministic browser code. This skill covers how to use the real Stagehand project for agent-driven web navigation, extraction, and repeatable browser workflows."
github_stars: 22057
verification: "listed"
source: "https://github.com/browserbase/stagehand"
author: "Browserbase"
publisher_type: "Company"
category: "Browser Automation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "browserbase/stagehand"
  github_stars: 22057
  npm_package: "@browserbasehq/stagehand"
  npm_weekly_downloads: 3394138
---

# Stagehand Browser Automation SDK

Stagehand is Browserbase's browser automation SDK for combining natural-language actions with deterministic browser code. This skill covers how to use the real Stagehand project for agent-driven web navigation, extraction, and repeatable browser workflows.

## Prerequisites

Node.js, Playwright

## Installation

Use the upstream install or setup path that matches your environment:
- npx create-browser-app
- git clone https://github.com/browserbase/stagehand.git
- pnpm install
- pnpm run build

Requirements and caveats from upstream:
- If you're looking for the Python implementation, you can find it
- <a href="https://github.com/browserbase/stagehand-python"> here</a>
- Most existing browser automation tools either require you to write low-level code in a framework like Selenium, Playwright, or Puppeteer, or use high-level agents that can be unpredictable in production. By letting de...

Basic usage or getting-started notes:
- **Write once, run forever**: Stagehand's auto-caching combined with self-healing remembers previous actions, runs without LLM inference, and knows when to involve AI whenever the website changes and your automation br...
- Start with Stagehand with one line of code, or check out our [Quickstart Guide](https://docs.stagehand.dev/v3/first-steps/quickstart) for more information:
- bash

- Source: https://github.com/browserbase/stagehand
- Extracted from upstream docs: https://raw.githubusercontent.com/browserbase/stagehand/HEAD/README.md

## Documentation

- https://docs.stagehand.dev

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stagehand-browser-automation-sdk/)
