---
title: "Stagehand Browser Automation"
description: "Stagehand is Browserbase’s AI browser automation framework for mixing natural-language actions with deterministic code. It is built for production workflows where you want Playwright-level control, structured extraction, and the option to cache and stabilize repeated web tasks."
verification: security_reviewed
source: "https://github.com/browserbase/stagehand"
category:
  - "Browser Automation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "browserbase/stagehand"
  github_stars: 22059
---

# Stagehand Browser Automation

Stagehand is Browserbase’s open-source browser automation framework for developers who want to combine natural-language control with code-level precision. The upstream project describes it as an AI browser automation framework and positions it between traditional browser testing tools and fully autonomous agents. In practice, that makes it useful when an agent needs to navigate unfamiliar pages with AI, but still hand off repeatable work to code once the workflow is understood.

The project exposes actions such as act() for individual browser steps, agent() for multi-step flows, and extract() for structured data capture. Its examples show integration with a browser context, page navigation, typed schemas via Zod, and support for production-oriented patterns such as previewing AI actions, caching repeated steps, and self-healing when a website changes. The repository also documents a quickstart flow with npx create-browser-app, local development via pnpm install, and optional Browserbase credentials for hosted browser infrastructure.

For ASE users, the concrete job-to-be-done is reliable browser automation that can start with prompts and evolve into stable workflows. It fits web testing, lead capture, UI navigation, structured extraction, and repeatable back-office tasks. Because the upstream project publishes documentation, has an MIT license, active releases, and heavy recent GitHub activity, it clears the intake gate for verified metadata publication.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/stagehand-browser-automation
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/stagehand-browser-automation` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stagehand-browser-automation/)
