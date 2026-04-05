---
name: "browser-use Browser Automation Framework"
description: "Use browser-use to turn natural-language web tasks into repeatable browser automation backed by Playwright and agent loops. This skill helps an agent open sites, inspect page state, click, type, extract data, and recover from common UI changes with a real automation framework instead of brittle one-off scripts."
category: "Browser Automation"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/browser-use/browser-use"
tool_ecosystem:
  tool: browser-use
  github_repo: browser-use/browser-use
  github_stars: 85193
  license: MIT
  maintained: true
---
# browser-use Browser Automation Framework

Use browser-use to turn natural-language web tasks into repeatable browser automation backed by Playwright and agent loops. This skill helps an agent open sites, inspect page state, click, type, extract data, and recover from common UI changes with a real automation framework instead of brittle one-off scripts.

## Overview

The browser-use project is an open source browser automation framework built for AI agents that need to operate real websites instead of just reading static HTML. A skill centered on browser-use is useful when the job-to-be-done is “go do this in a browser and bring back a structured result” — things like form submission, lead capture, page QA, authenticated data collection, invoice download, or multi-step research.

In practice, the skill would use browser-use with Playwright, DOM inspection, action planning, and step-by-step tool execution. It can open a target URL, inspect interactive elements, reason about page state, click buttons, fill inputs, follow redirects, wait for network or DOM conditions, and extract outputs such as tables, screenshots, links, status messages, PDFs, or normalized JSON. Because browser-use is agent-oriented, the skill can include retry logic, selector recovery, and guardrails for login pages, modals, cookie banners, and changing layouts.

The integration points are strong: browser-use can sit inside Python workflows, connect to LLM reasoning layers, and hand results to downstream systems like CRM syncs, scraping pipelines, or QA reports. Technical terms that matter here include Playwright sessions, DOM snapshots, selectors, action traces, headless execution, state persistence, authentication, and structured extraction. The end result is not just “use a browser,” but a reproducible browser operator skill anchored to the real browser-use framework.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill browser-use-browser-automation-framework
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill browser-use-browser-automation-framework -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill browser-use-browser-automation-framework -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill browser-use-browser-automation-framework -a codex
```

### OpenClaw

```bash
clawhub install browser-use-browser-automation-framework
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/browser-use-browser-automation-framework/)
