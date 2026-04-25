---
title: "Drive Chrome with stable accessibility refs for repeatable browser automation"
description: "Use PinchTab when an agent needs repeatable browser automation with stable element references, persistent profiles, and low-token page inspection. It fits tasks where a normal browser library is too noisy, brittle, or expensive in context."
verification: "security_reviewed"
source: "https://github.com/pinchtab/pinchtab/tree/main/skills/pinchtab"
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

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/drive-chrome-with-stable-accessibility-refs-for-repeatable-browser-automation/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/drive-chrome-with-stable-accessibility-refs-for-repeatable-browser-automation
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/drive-chrome-with-stable-accessibility-refs-for-repeatable-browser-automation`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/drive-chrome-with-stable-accessibility-refs-for-repeatable-browser-automation/)
