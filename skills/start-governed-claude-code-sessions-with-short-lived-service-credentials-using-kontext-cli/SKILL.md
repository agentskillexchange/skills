---
title: "Start governed Claude Code sessions with short-lived service credentials using Kontext CLI"
description: "Inject short-lived, scoped service credentials into Claude Code sessions so agents can reach approved systems without exposing raw secrets."
verification: listed
source: "https://github.com/kontext-security/kontext-cli"
category:
  - "Security & Verification"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "kontext-security/kontext-cli"
  github_stars: 143
---

# Start governed Claude Code sessions with short-lived service credentials using Kontext CLI

Use Kontext CLI when you need Claude Code to call systems like GitHub, Stripe, or internal services without handing the agent long-lived keys in plain env files. Invoke it instead of using the product normally when the job is starting a governed agent session with scoped credentials, hosted provider connection, and traceable tool activity, not generic secret storage or identity management. The boundary is the session-start credential brokering workflow for Claude Code, which is narrower than a general security platform or SDK listing.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/start-governed-claude-code-sessions-with-short-lived-service-credentials-using-kontext-cli
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/start-governed-claude-code-sessions-with-short-lived-service-credentials-using-kontext-cli` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/start-governed-claude-code-sessions-with-short-lived-service-credentials-using-kontext-cli/)
