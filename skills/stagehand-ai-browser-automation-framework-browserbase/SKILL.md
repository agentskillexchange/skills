---
title: "Stagehand AI Browser Automation Framework by Browserbase"
description: "Stagehand is Browserbase’s open source browser automation framework that blends natural-language actions with code-level control. It helps agents and developers build more reliable web workflows on top of Playwright-compatible browser sessions, extraction, and repeatable action caching."
slug: "stagehand-ai-browser-automation-framework-browserbase"
category:
  - "Browser Automation"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/browserbase/stagehand"
---

# Stagehand AI Browser Automation Framework by Browserbase

Stagehand is Browserbase’s open source browser automation framework that blends natural-language actions with code-level control. It helps agents and developers build more reliable web workflows on top of Playwright-compatible browser sessions, extraction, and repeatable action caching.

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
clawhub install stagehand-ai-browser-automation-framework-browserbase
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Stagehand is an open source browser automation framework from Browserbase that combines natural-language instructions with code-driven control. It is designed for teams building agentic workflows that still need production-grade determinism. Instead of choosing between brittle selectors and fully autonomous agents, Stagehand lets developers mix both approaches: use structured code when the workflow is known, and fall back to AI-assisted actions when the page is unfamiliar or changing.
The project exposes primitives such as act() for single actions, agent() for multi-step navigation, and extract() for structured data capture. Under the hood, it works with browser sessions and page objects so it fits naturally into TypeScript automation stacks. The upstream quickstart centers on npx create-browser-app, and the package is distributed on npm as @browserbasehq/stagehand. Browserbase also maintains dedicated documentation at docs.stagehand.dev.
For agent builders, Stagehand is useful when an automation needs to log in, click through UI flows, recover from small layout changes, and still return clean structured output. It is especially relevant for web testing, browser-driven research, back-office task automation, and extraction pipelines that cannot rely on static HTML alone. Because the source repository, docs site, npm package, MIT license, and active release activity are all public and verifiable, it clears ASE’s metadata intake threshold comfortably.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stagehand-ai-browser-automation-framework-browserbase/)
