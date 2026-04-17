---
title: "Stagehand Browser Automation SDK"
description: "Stagehand Browser Automation SDK is a tool-anchored skill built around the real Stagehand project from Browserbase. Stagehand is an open source browser automation framework that combines natural-language browser actions with code-first control, so agents can interact with websites without giving up the reliability of structured automation. In practice, that makes it useful for login flows, multi-step forms, scraping, browser testing, authenticated navigation, and production automations where pure prompt-driven clicking is too brittle.\nThis skill is for situations where you want an agent to drive a browser with Stagehand and still keep explicit control over what happens. A typical flow is to install the @browserbasehq/stagehand package in a Node.js project, initialize Stagehand with your model and browser settings, and then use its APIs to inspect the page, perform natural-language actions, and fall back to code when a workflow needs precision. Because Stagehand sits in the middle between fully manual Playwright scripting and fully opaque browser agents, it works well for repeatable agent automations that need to survive UI changes.\nIntegration points are straightforward. Stagehand can plug into web automation pipelines, browser-use agents, QA tooling, data extraction jobs, and support workflows that need screenshots, navigation state, or structured actions. Teams can pair it with Playwright-style browser logic, LLM orchestration layers, or agent runtimes that need a reliable browser execution layer. Outputs can include browser state transitions, extracted page data, successful task completion, and reusable automation code patterns. If you need a real browser automation skill backed by an active GitHub repo, docs site, npm package, MIT license, and current maintenance activity, Stagehand clears that bar comfortably."
verification: security_reviewed
source: "https://github.com/browserbase/stagehand"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "browserbase/stagehand"
  github_stars: 22057
---

# Stagehand Browser Automation SDK

Stagehand Browser Automation SDK is a tool-anchored skill built around the real Stagehand project from Browserbase. Stagehand is an open source browser automation framework that combines natural-language browser actions with code-first control, so agents can interact with websites without giving up the reliability of structured automation. In practice, that makes it useful for login flows, multi-step forms, scraping, browser testing, authenticated navigation, and production automations where pure prompt-driven clicking is too brittle.
This skill is for situations where you want an agent to drive a browser with Stagehand and still keep explicit control over what happens. A typical flow is to install the @browserbasehq/stagehand package in a Node.js project, initialize Stagehand with your model and browser settings, and then use its APIs to inspect the page, perform natural-language actions, and fall back to code when a workflow needs precision. Because Stagehand sits in the middle between fully manual Playwright scripting and fully opaque browser agents, it works well for repeatable agent automations that need to survive UI changes.
Integration points are straightforward. Stagehand can plug into web automation pipelines, browser-use agents, QA tooling, data extraction jobs, and support workflows that need screenshots, navigation state, or structured actions. Teams can pair it with Playwright-style browser logic, LLM orchestration layers, or agent runtimes that need a reliable browser execution layer. Outputs can include browser state transitions, extracted page data, successful task completion, and reusable automation code patterns. If you need a real browser automation skill backed by an active GitHub repo, docs site, npm package, MIT license, and current maintenance activity, Stagehand clears that bar comfortably.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/stagehand-browser-automation-sdk
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/stagehand-browser-automation-sdk` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stagehand-browser-automation-sdk/)
