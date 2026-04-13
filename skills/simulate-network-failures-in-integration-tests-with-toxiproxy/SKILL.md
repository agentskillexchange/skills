---
title: "Simulate network failures in integration tests with Toxiproxy"
description: "Use Toxiproxy when an agent needs to inject latency, disconnects, bandwidth limits, or packet-like failure modes into real service calls during development, CI, or incident reproduction. The agent routes app traffic through controlled TCP proxies, applies toxics at the right moment, and reports which dependency paths fail gracefully versus which ones crack under stress."
verification: "security_reviewed"
source: "https://github.com/Shopify/toxiproxy"
category: ["Runbooks &amp; Diagnostics"]
framework: ["Multi-Framework"]
tool_ecosystem:
  github_repo: "Shopify/toxiproxy"
  github_stars: 11937
---

# Simulate network failures in integration tests with Toxiproxy

Use Toxiproxy when an agent needs to inject latency, disconnects, bandwidth limits, or packet-like failure modes into real service calls during development, CI, or incident reproduction. The agent routes app traffic through controlled TCP proxies, applies toxics at the right moment, and reports which dependency paths fail gracefully versus which ones crack under stress.

## Installation

Choose the install path that fits your setup:

1. Install from the Agent Skill Exchange catalog if your agent client supports it.
2. Copy the skill folder into your local skills directory.
3. Add it as a git submodule in your shared agent-skills repo.
4. Vendor the files directly into a project-specific `.agents/skills/` or equivalent folder.
5. Keep a fork or mirror if you need local modifications or pinned revisions.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/simulate-network-failures-in-integration-tests-with-toxiproxy/)
