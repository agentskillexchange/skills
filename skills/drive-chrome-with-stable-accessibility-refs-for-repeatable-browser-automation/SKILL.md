---
title: "Drive Chrome with stable accessibility refs for repeatable browser automation"
description: "PinchTab is a browser automation bridge for agents, but the useful skill-shaped job is narrower than the product itself. This entry is about driving Chrome through stable accessibility refs, persistent browser instances, and low-token inspection so an agent can reliably navigate sites, fill forms, click through flows, capture screenshots, and extract structured page state without re-describing the whole DOM every turn. Invoke this when you want an agent to work through a browser task that benefits from repeatability. Good examples are regression checks, account workflows, setup wizards, scraping a known sequence of pages, or any flow where the agent needs references like e5 and e12 to remain stable across actions. That is the practical difference between using this as a skill versus just listing PinchTab as software. The scope boundary is clear. This is not a generic listing for a browser framework, dashboard, or orchestration server. The value is the agent playbook: inspect the page, target stable refs, act on them, and keep the workflow deterministic across multiple browser steps. If you only need to know that PinchTab exists, or you want to build your own browser stack from scratch, that belongs elsewhere. Integration points from upstream are concrete: the tool supports a CLI, an HTTP API fallback, screenshots/PDF output, persistent profiles, and multiple instances. That makes it a strong fit for agents handling web QA, admin flows, and structured browser operations where repeatability is more important than free-form browsing."
source: "https://github.com/pinchtab/pinchtab/tree/main/skills/pinchtab"
verification: "security_reviewed"
category:
  - "Browser Automation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "pinchtab/pinchtab"
  github_stars: 8694
---

# Drive Chrome with stable accessibility refs for repeatable browser automation

PinchTab is a browser automation bridge for agents, but the useful skill-shaped job is narrower than the product itself. This entry is about driving Chrome through stable accessibility refs, persistent browser instances, and low-token inspection so an agent can reliably navigate sites, fill forms, click through flows, capture screenshots, and extract structured page state without re-describing the whole DOM every turn. Invoke this when you want an agent to work through a browser task that benefits from repeatability. Good examples are regression checks, account workflows, setup wizards, scraping a known sequence of pages, or any flow where the agent needs references like e5 and e12 to remain stable across actions. That is the practical difference between using this as a skill versus just listing PinchTab as software. The scope boundary is clear. This is not a generic listing for a browser framework, dashboard, or orchestration server. The value is the agent playbook: inspect the page, target stable refs, act on them, and keep the workflow deterministic across multiple browser steps. If you only need to know that PinchTab exists, or you want to build your own browser stack from scratch, that belongs elsewhere. Integration points from upstream are concrete: the tool supports a CLI, an HTTP API fallback, screenshots/PDF output, persistent profiles, and multiple instances. That makes it a strong fit for agents handling web QA, admin flows, and structured browser operations where repeatability is more important than free-form browsing.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/drive-chrome-with-stable-accessibility-refs-for-repeatable-browser-automation/)
