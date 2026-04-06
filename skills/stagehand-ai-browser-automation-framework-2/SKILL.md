---
name: Stagehand AI Browser Automation Framework
description: Build browser automations with Stagehand, Browserbase’s AI browser automation
  framework. It combines natural-language actions with code-level control so agents
  can navigate sites, extract data, and turn brittle scripts into more resilient Playwright-style
  workflows.
category: Browser Automation
framework: Multi-Framework
verification: listed
source: "https://github.com/browserbase/stagehand"
---
# Stagehand AI Browser Automation Framework

Build browser automations with Stagehand, Browserbase’s AI browser automation framework. It combines natural-language actions with code-level control so agents can navigate sites, extract data, and turn brittle scripts into more resilient Playwright-style workflows.

Stagehand is Browserbase’s AI browser automation framework for teams that want natural-language browser control without giving up code-level reliability. A Stagehand skill is useful when an agent needs to open websites, click through unfamiliar interfaces, extract structured data, or turn a prompt into a repeatable browser workflow. The upstream project exposes primitives such as act(), agent(), and extract(), letting a workflow mix natural-language navigation with typed extraction and ordinary browser automation code.

In practice, this kind of skill fits tasks like login flows, dashboard QA, lead capture, form filling, scraping dynamic pages, and multi-step browser tasks where the DOM changes often. Stagehand is built to bridge the gap between pure code automation and autonomous agents: it can use AI when the page is unfamiliar, then fall back to deterministic browser control when the workflow stabilizes. The project’s own docs emphasize repeatable production automations, auto-caching, and self-healing behavior when web pages change.

Integration points include Browserbase for remote browser sessions, LLM provider API keys for natural-language actions, and common TypeScript or Node.js application stacks. If you want an agent skill anchored to a real browser automation framework rather than a vague “web assistant,” Stagehand gives you a concrete, well-documented foundation with active maintenance, published releases, and a large developer user base.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill stagehand-ai-browser-automation-framework-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill stagehand-ai-browser-automation-framework-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill stagehand-ai-browser-automation-framework-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill stagehand-ai-browser-automation-framework-2 -a codex
```

### OpenClaw

```bash
clawhub install stagehand-ai-browser-automation-framework-2
```


## Source

- [GitHub](https://github.com/browserbase/stagehand)
