---
title: "Stagehand Browser Agent SDK"
description: "Stagehand is Browserbase’s open source SDK for browser agents, combining code-first control with natural language actions. It is aimed at reliable production browser automation, with TypeScript integrations, docs, and npm distribution for agent workflows."
slug: "stagehand-browser-agent-sdk"
category:
  - "Browser Automation"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/browserbase/stagehand"
tool_ecosystem:
  github_repo: "browserbase/stagehand"
  github_stars: 21947
  npm_package: "stagehand-workspace"
listed: true
---

# Stagehand Browser Agent SDK

Stagehand is Browserbase’s open source SDK for browser agents, combining code-first control with natural language actions. It is aimed at reliable production browser automation, with TypeScript integrations, docs, and npm distribution for agent workflows.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install stagehand-browser-agent-sdk
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Stagehand is the open source browser agent SDK maintained by Browserbase. The project is designed for developers who want a more reliable middle ground between fragile low-level browser scripts and fully opaque autonomous agents. In practice, Stagehand lets you combine normal code with targeted natural-language browser actions, which is useful when a workflow needs both deterministic steps and flexible page understanding.
The upstream package is published on npm as @browserbasehq/stagehand, backed by a public GitHub repository, official documentation, MIT license, and active release history. Browserbase positions it as an SDK for browser agents, and its documentation includes installation paths, framework integrations, and examples for real automation projects. That gives ASE users a concrete tool rather than a vague pattern.
This skill fits jobs like authenticated browsing flows, form completion, scraping with page interaction, and agent-led QA or operations tooling. It integrates with TypeScript and JavaScript application stacks, supports LLM provider configuration, and can be paired with Browserbase cloud sessions or local browser execution depending on the workflow. For users comparing browser agent foundations, Stagehand is especially relevant when maintainability and production-oriented control matter more than pure prompt-only automation.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stagehand-browser-agent-sdk/)
