---
title: "Simulate network failures in integration tests with Toxiproxy"
description: "Use Toxiproxy when an agent needs to inject latency, disconnects, bandwidth limits, or packet-like failure modes into real service calls during development, CI, or incident reproduction. The agent routes app traffic through controlled TCP proxies, applies toxics at the right moment, and reports which dependency paths fail gracefully versus which ones crack under stress."
verification: security_reviewed
source: "https://github.com/Shopify/toxiproxy"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Multi-Framework"
---

# Simulate network failures in integration tests with Toxiproxy

This ASE entry is built around Toxiproxy, the open source TCP proxy maintained by Shopify for simulating network and system conditions in development, CI, and test environments. The agent job here is narrow and concrete: stand up controlled proxies for dependencies such as Redis, MySQL, Postgres, Kafka, or internal HTTP services, then inject failure modes like latency, timeouts, bandwidth throttling, connection resets, or hard outages while a test or diagnostic workflow is running.

You invoke this skill when normal product usage is not enough because the task is not “run a proxy” in the abstract. The task is to prove whether a system behaves correctly when the network turns hostile. An agent can wire an app under test through Toxiproxy, reproduce an intermittent outage from a bug report, run the failing path again with deterministic latency, and return evidence about retries, circuit breakers, error handling, and recovery behavior. That is materially different from listing a generic proxy server or chaos-testing framework.

The scope boundary matters. This entry is not a catalog card for Toxiproxy itself, and it is not a generic networking tool listing. It is specifically for failure injection during resilience testing and diagnostics. Integration points include Docker Compose test stacks, CI pipelines, language-specific Toxiproxy clients, and application test harnesses that need a scriptable HTTP API for changing network conditions mid-run. Upstream evidence is strong: official GitHub repo, MIT license, tagged releases, and active maintenance.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/simulate-network-failures-in-integration-tests-with-toxiproxy/)
