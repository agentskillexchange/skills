---
title: "Investigate production issues from Slack with runbooks and monitoring MCPs using DIY AI Debugging Agent Toolkit"
description: "Handle alerts and debugging questions from Slack, query connected monitoring MCP servers, and follow runbook-guided investigation steps for live incidents."
verification: "security_reviewed"
source: "https://github.com/DrDroidLab/sample-debug-agent"
category:
  - "Runbooks & Diagnostics"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "DrDroidLab/sample-debug-agent"
  github_stars: 6
---

# Investigate production issues from Slack with runbooks and monitoring MCPs using DIY AI Debugging Agent Toolkit

Use DIY AI Debugging Agent Toolkit when an agent needs to respond in Slack, inspect monitoring systems through MCP servers, and follow runbook-guided steps during production debugging. The upstream repository is concrete about the workflow: receive alerts or questions in Slack, consult configured monitoring MCP servers, apply prompts or runbooks, and respond with investigative findings. Invoke this instead of using Slack, dashboards, or a raw MCP connection normally when the immediate job is incident debugging with chat-driven triage. The scope boundary is specific enough to be skill-shaped: this is a Slack-anchored production-debugging workflow that consults monitoring MCP tools and runbooks, not a generic observability platform or broad agent framework listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/investigate-production-issues-from-slack-with-runbooks-and-monitoring-mcps-using-diy-ai-debugging-agent-toolkit/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/investigate-production-issues-from-slack-with-runbooks-and-monitoring-mcps-using-diy-ai-debugging-agent-toolkit
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/investigate-production-issues-from-slack-with-runbooks-and-monitoring-mcps-using-diy-ai-debugging-agent-toolkit`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/investigate-production-issues-from-slack-with-runbooks-and-monitoring-mcps-using-diy-ai-debugging-agent-toolkit/)
