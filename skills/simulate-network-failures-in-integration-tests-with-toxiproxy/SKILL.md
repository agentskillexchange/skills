---
title: "Simulate network failures in integration tests with Toxiproxy"
description: "Use Toxiproxy when an agent needs to inject latency, disconnects, bandwidth limits, or packet-like failure modes into real service calls during development, CI, or incident reproduction. The agent routes app traffic through controlled TCP proxies, applies toxics at the right moment, and reports which dependency paths fail gracefully versus which ones crack under stress."
verification: "security_reviewed"
source: "https://github.com/Shopify/toxiproxy"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "Shopify/toxiproxy"
  github_stars: 11937
---

# Simulate network failures in integration tests with Toxiproxy

Use Toxiproxy when an agent needs to inject latency, disconnects, bandwidth limits, or packet-like failure modes into real service calls during development, CI, or incident reproduction. The agent routes app traffic through controlled TCP proxies, applies toxics at the right moment, and reports which dependency paths fail gracefully versus which ones crack under stress.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/simulate-network-failures-in-integration-tests-with-toxiproxy/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/simulate-network-failures-in-integration-tests-with-toxiproxy
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/simulate-network-failures-in-integration-tests-with-toxiproxy`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/simulate-network-failures-in-integration-tests-with-toxiproxy/)
