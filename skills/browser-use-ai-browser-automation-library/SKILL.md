---
name: Browser Use AI Browser Automation Library
description: Automates browser tasks with Browser Use, the open-source library that
  connects LLM reasoning to Playwright-driven web actions. Useful for navigating sites,
  filling forms, extracting structured page data, and running agentic browser workflows
  with screenshots and stateful sessions.
verification: security_reviewed
source: https://github.com/browser-use/browser-use
category:
- Browser Automation
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: browser-use/browser-use
  github_stars: 85193
  license: MIT
---
# Browser Use AI Browser Automation Library

Browser Use AI Browser Automation Library is aimed at teams building browser-capable agents that need more than a raw Playwright script. The skill is anchored to the real browser-use project, which combines large language model planning with browser control primitives such as navigation, DOM inspection, clicking, typing, and page-state reasoning. That makes it a good fit for tasks like guided form submission, site monitoring, lead capture, competitive research, and agent-run quality assurance on authenticated web apps.
The skill helps map a high-level user goal into a safer browser workflow: open the target page, inspect the available elements, decide which action to take next, recover from layout changes, and produce artifacts that explain what happened. Because Browser Use sits on top of browser automation foundations like Playwright, it can also surface technical concepts such as selectors, session state, screenshots, retries, and stepwise execution traces. This is useful when the site changes frequently and brittle one-shot automation is not enough.
Outputs can include structured extraction results, screenshots, execution logs, captured URLs, form submissions, or an audit trail describing each action the agent took in the browser. Integration points include Python applications, AI agent runtimes, retrieval or research pipelines that need live web interaction, and internal tools that wrap Browser Use into a controlled automation service. Use this skill when the job is natural-language browser execution with observable steps, not just low-level browser scripting.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/browser-use-ai-browser-automation-library/)
