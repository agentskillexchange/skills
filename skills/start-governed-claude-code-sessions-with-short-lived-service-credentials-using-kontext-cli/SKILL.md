---
title: "Start governed Claude Code sessions with short-lived service credentials using Kontext CLI"
description: "Inject short-lived, scoped service credentials into Claude Code sessions so agents can reach approved systems without exposing raw secrets."
verification: "listed"
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

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/start-governed-claude-code-sessions-with-short-lived-service-credentials-using-kontext-cli/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/start-governed-claude-code-sessions-with-short-lived-service-credentials-using-kontext-cli
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/start-governed-claude-code-sessions-with-short-lived-service-credentials-using-kontext-cli`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/start-governed-claude-code-sessions-with-short-lived-service-credentials-using-kontext-cli/)
