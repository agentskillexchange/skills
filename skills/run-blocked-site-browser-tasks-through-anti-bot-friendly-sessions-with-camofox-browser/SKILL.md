---
title: "Run blocked-site browser tasks through anti-bot friendly sessions with Camofox Browser"
description: "Use Camofox Browser to route agent browser work through an anti-detection browser server with stable element refs, snapshots, cookies, proxies, and session isolation."
verification: "security_reviewed"
source: "https://github.com/jo-inc/camofox-browser"
category:
  - "Browser Automation"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "jo-inc/camofox-browser"
  github_stars: 2853
---

# Run blocked-site browser tasks through anti-bot friendly sessions with Camofox Browser

Use Camofox Browser when ordinary headless browser runs keep getting challenged, fingerprinted, or blocked and the agent still needs a repeatable browsing workflow. The upstream project is explicit that it is a browser automation server for AI agents, built around Camoufox, with accessibility snapshots, stable element references, cookie import, proxy support, session isolation, and API endpoints for agent-facing browser control. Invoke this instead of using the product normally when the task is specifically to keep blocked-site browser automation moving, not merely to install another browser framework. The operator loop is concrete: start the server, create or resume a tab session, navigate, inspect a compact snapshot, click or type through stable refs, and reuse cookies or proxies when anti-bot friction appears. The scope boundary is narrower than a plain browser or server listing. This skill is the anti-bot browser-task workflow for agents, not a generic browser product card or undifferentiated automation SDK entry.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/run-blocked-site-browser-tasks-through-anti-bot-friendly-sessions-with-camofox-browser/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/run-blocked-site-browser-tasks-through-anti-bot-friendly-sessions-with-camofox-browser
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/run-blocked-site-browser-tasks-through-anti-bot-friendly-sessions-with-camofox-browser`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-blocked-site-browser-tasks-through-anti-bot-friendly-sessions-with-camofox-browser/)
