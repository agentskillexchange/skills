---
title: "Embed an in-page GUI agent with Page Agent"
description: "Add a JavaScript GUI agent to a web app so users or agents can complete UI tasks through natural-language commands without a headless browser."
verification: "listed"
source: "https://github.com/alibaba/page-agent"
author: "Alibaba"
publisher_type: "organization"
category:
  - "Browser Automation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "alibaba/page-agent"
  github_stars: 18551
  npm_package: "page-agent"
  npm_weekly_downloads: 37044
---

# Embed an in-page GUI agent with Page Agent

Add a JavaScript GUI agent to a web app so users or agents can complete UI tasks through natural-language commands without a headless browser.

## Prerequisites

JavaScript, npm or script tag, LLM API endpoint, optional Chrome extension or MCP-compatible client for multi-page control

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with `npm install page-agent` and instantiate `new PageAgent({ model, baseURL, apiKey, language })`, or load the documented IIFE script for evaluation. Then call `agent.execute('...')` from the page context.
```

## Documentation

- https://alibaba.github.io/page-agent/docs/introduction/overview

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/embed-an-in-page-gui-agent-with-page-agent/)
