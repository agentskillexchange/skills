---
title: "Simulate network failures in integration tests with Toxiproxy"
description: "Use Toxiproxy when an agent needs to inject latency, disconnects, bandwidth limits, or packet-like failure modes into real service calls during development, CI, or incident reproduction. The agent routes app traffic through controlled TCP proxies, applies toxics at the right moment, and reports which dependency paths fail gracefully versus which ones crack under stress."
verification: security_reviewed
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

This ASE entry is built around Toxiproxy, the open source TCP proxy maintained by Shopify for simulating network and system conditions in development, CI, and test environments. The agent job here is narrow and concrete: stand up controlled proxies for dependencies such as Redis, MySQL, Postgres, Kafka, or internal HTTP services, then inject failure modes like latency, timeouts, bandwidth throttling, connection resets, or hard outages while a test or diagnostic workflow is running.

You invoke this skill when normal product usage is not enough because the task is not “run a proxy” in the abstract. The task is to prove whether a system behaves correctly when the network turns hostile. An agent can wire an app under test through Toxiproxy, reproduce an intermittent outage from a bug report, run the failing path again with deterministic latency, and return evidence about retries, circuit breakers, error handling, and recovery behavior. That is materially different from listing a generic proxy server or chaos-testing framework.

The scope boundary matters. This entry is not a catalog card for Toxiproxy itself, and it is not a generic networking tool listing. It is specifically for failure injection during resilience testing and diagnostics. Integration points include Docker Compose test stacks, CI pipelines, language-specific Toxiproxy clients, and application test harnesses that need a scriptable HTTP API for changing network conditions mid-run. Upstream evidence is strong: official GitHub repo, MIT license, tagged releases, and active maintenance.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/simulate-network-failures-in-integration-tests-with-toxiproxy
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/simulate-network-failures-in-integration-tests-with-toxiproxy` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/simulate-network-failures-in-integration-tests-with-toxiproxy/)
