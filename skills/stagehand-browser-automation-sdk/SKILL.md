---
name: Stagehand Browser Automation SDK
description: Stagehand is Browserbase&#8217;s browser automation SDK for combining
  natural-language actions with deterministic browser code. This skill covers how
  to use the real Stagehand project for agent-driven web navigation, extraction, and
  repeatable browser workflows.
verification: security_reviewed
source: https://github.com/browserbase/stagehand
category:
- Browser Automation
framework:
- Multi-Framework
---
# Stagehand Browser Automation SDK

Stagehand Browser Automation SDK is a tool-anchored skill built around the real Stagehand project from Browserbase. Stagehand is an open source browser automation framework that combines natural-language browser actions with code-first control, so agents can interact with websites without giving up the reliability of structured automation. In practice, that makes it useful for login flows, multi-step forms, scraping, browser testing, authenticated navigation, and production automations where pure prompt-driven clicking is too brittle.
This skill is for situations where you want an agent to drive a browser with Stagehand and still keep explicit control over what happens. A typical flow is to install the @browserbasehq/stagehand package in a Node.js project, initialize Stagehand with your model and browser settings, and then use its APIs to inspect the page, perform natural-language actions, and fall back to code when a workflow needs precision. Because Stagehand sits in the middle between fully manual Playwright scripting and fully opaque browser agents, it works well for repeatable agent automations that need to survive UI changes.
Integration points are straightforward. Stagehand can plug into web automation pipelines, browser-use agents, QA tooling, data extraction jobs, and support workflows that need screenshots, navigation state, or structured actions. Teams can pair it with Playwright-style browser logic, LLM orchestration layers, or agent runtimes that need a reliable browser execution layer. Outputs can include browser state transitions, extracted page data, successful task completion, and reusable automation code patterns. If you need a real browser automation skill backed by an active GitHub repo, docs site, npm package, MIT license, and current maintenance activity, Stagehand clears that bar comfortably.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stagehand-browser-automation-sdk/)
