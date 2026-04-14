---
title: "Simulate network failures in integration tests with Toxiproxy"
slug: "simulate-network-failures-in-integration-tests-with-toxiproxy"
verification: security_reviewed
source: "https://github.com/Shopify/toxiproxy"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "Shopify/toxiproxy"
  github_stars: 11937
---
# Simulate network failures in integration tests with Toxiproxy

Use Toxiproxy when an agent needs to inject latency, disconnects, bandwidth limits, or packet-like failure modes into real service calls during development, CI, or incident reproduction. The agent routes app traffic through controlled TCP proxies, applies toxics at the right moment, and reports which dependency paths fail gracefully versus which ones crack under stress.

## Installation

Choose the method that fits your setup:

1. Install from Agent Skill Exchange
2. Clone or download the upstream project
3. Install with the upstream package manager
4. Add the skill to your local skills directory
5. Follow the upstream documentation for environment-specific setup

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/simulate-network-failures-in-integration-tests-with-toxiproxy/)
