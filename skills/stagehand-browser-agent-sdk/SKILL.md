---
title: "Stagehand Browser Agent SDK"
description: "Stagehand is Browserbase’s open source SDK for browser agents, combining code-first control with natural language actions. It is aimed at reliable production browser automation, with TypeScript integrations, docs, and npm distribution for agent workflows."
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

# Stagehand Browser Agent SDK

Stagehand is the open source browser agent SDK maintained by Browserbase. The project is designed for developers who want a more reliable middle ground between fragile low-level browser scripts and fully opaque autonomous agents. In practice, Stagehand lets you combine normal code with targeted natural-language browser actions, which is useful when a workflow needs both deterministic steps and flexible page understanding.

The upstream package is published on npm as @browserbasehq/stagehand, backed by a public GitHub repository, official documentation, MIT license, and active release history. Browserbase positions it as an SDK for browser agents, and its documentation includes installation paths, framework integrations, and examples for real automation projects. That gives ASE users a concrete tool rather than a vague pattern.

This skill fits jobs like authenticated browsing flows, form completion, scraping with page interaction, and agent-led QA or operations tooling. It integrates with TypeScript and JavaScript application stacks, supports LLM provider configuration, and can be paired with Browserbase cloud sessions or local browser execution depending on the workflow. For users comparing browser agent foundations, Stagehand is especially relevant when maintainability and production-oriented control matter more than pure prompt-only automation.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stagehand-browser-agent-sdk/)
