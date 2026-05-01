---
title: "Broker API credentials to AI agents without exposing raw keys using OneCLI"
description: "Store credentials once, then inject them into outbound agent requests at runtime so agents can call services without receiving raw secrets."
verification: "security_reviewed"
source: "https://github.com/onecli/onecli"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "onecli/onecli"
  github_stars: 1859
---

# Broker API credentials to AI agents without exposing raw keys using OneCLI

Use OneCLI when an agent must call external APIs but should not receive raw credentials directly. The upstream project is specific about the workflow: store credentials once, issue scoped agent access, match outbound requests by host or path, and inject the real secrets at request time through the gateway.

Invoke this instead of wiring secrets into agents, prompts, or app config normally when the job is controlled credential brokering for agent HTTP calls. The scope boundary is narrow enough to stay skill-shaped: OneCLI is being used here for per-agent secret injection and access control on outbound requests, not as a generic vault, dashboard, or platform listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/broker-api-credentials-to-ai-agents-without-exposing-raw-keys-using-onecli/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/broker-api-credentials-to-ai-agents-without-exposing-raw-keys-using-onecli
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/broker-api-credentials-to-ai-agents-without-exposing-raw-keys-using-onecli`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/broker-api-credentials-to-ai-agents-without-exposing-raw-keys-using-onecli/)
