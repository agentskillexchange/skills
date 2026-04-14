---
title: "Stagehand AI Browser Automation Framework by Browserbase"
description: "Stagehand is Browserbase’s open source browser automation framework that blends natural-language actions with code-level control. It helps agents and developers build more reliable web workflows on top of Playwright-compatible browser sessions, extraction, and repeatable action caching."
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

# Stagehand AI Browser Automation Framework by Browserbase

Stagehand is an open source browser automation framework from Browserbase that combines natural-language instructions with code-driven control. It is designed for teams building agentic workflows that still need production-grade determinism. Instead of choosing between brittle selectors and fully autonomous agents, Stagehand lets developers mix both approaches: use structured code when the workflow is known, and fall back to AI-assisted actions when the page is unfamiliar or changing.

The project exposes primitives such as act() for single actions, agent() for multi-step navigation, and extract() for structured data capture. Under the hood, it works with browser sessions and page objects so it fits naturally into TypeScript automation stacks. The upstream quickstart centers on npx create-browser-app, and the package is distributed on npm as @browserbasehq/stagehand. Browserbase also maintains dedicated documentation at docs.stagehand.dev.

For agent builders, Stagehand is useful when an automation needs to log in, click through UI flows, recover from small layout changes, and still return clean structured output. It is especially relevant for web testing, browser-driven research, back-office task automation, and extraction pipelines that cannot rely on static HTML alone. Because the source repository, docs site, npm package, MIT license, and active release activity are all public and verifiable, it clears ASE’s metadata intake threshold comfortably.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stagehand-ai-browser-automation-framework-browserbase/)
