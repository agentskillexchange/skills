---
title: "Simulate network failures in integration tests with Toxiproxy"
slug: "simulate-network-failures-in-integration-tests-with-toxiproxy"
description: "Use Toxiproxy when an agent needs to inject latency, disconnects, bandwidth limits, or packet-like failure modes into real service calls during development, CI, or incident reproduction. The agent routes app traffic through controlled TCP proxies, applies toxics at the right moment, and reports which dependency paths fail gracefully versus which ones crack under stress."
verification: security_reviewed
source: "https://github.com/Shopify/toxiproxy"
category:
  - "Runbooks &amp; Diagnostics"
tool_ecosystem:
  github_repo: "https://github.com/Shopify/toxiproxy"
  github_stars: 11934
---

# Simulate network failures in integration tests with Toxiproxy

Use Toxiproxy when an agent needs to inject latency, disconnects, bandwidth limits, or packet-like failure modes into real service calls during development, CI, or incident reproduction. The agent routes app traffic through controlled TCP proxies, applies toxics at the right moment, and reports which dependency paths fail gracefully versus which ones crack under stress.

## Installation

Choose the setup path that fits your environment:

1. Install from the Agent Skill Exchange UI
2. Clone or download this skill into your skills directory
3. Install with your agent platform's skill manager, if supported
4. Vendor the skill into your workspace or repo
5. Copy the skill files manually for local customization

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/simulate-network-failures-in-integration-tests-with-toxiproxy/)
