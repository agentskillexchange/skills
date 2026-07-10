---
name: "Stagehand Browser Agent SDK"
slug: "stagehand-browser-agent-sdk"
description: "Stagehand is Browserbase's open source SDK for browser agents, combining code-first control with natural language actions. It is aimed at reliable production browser automation, with TypeScript integrations, docs, and npm distribution for agent workflows."
github_stars: 22059
verification: "security_reviewed"
source: "https://github.com/browserbase/stagehand"
author: "browserbase"
category: "Browser Automation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "browserbase/stagehand"
  github_stars: 22059
  npm_package: "@browserbasehq/stagehand"
  npm_weekly_downloads: 3394138
---

# Stagehand Browser Agent SDK

Stagehand is Browserbase's open source SDK for browser agents, combining code-first control with natural language actions. It is aimed at reliable production browser automation, with TypeScript integrations, docs, and npm distribution for agent workflows.

## Prerequisites

npm, pnpm, python, go

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

- https://docs.stagehand.dev/v3/first-steps/quickstart

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stagehand-browser-agent-sdk/)
