---
title: "Simulate network failures in integration tests with Toxiproxy"
description: "This ASE entry is built around Toxiproxy, the open source TCP proxy maintained by Shopify for simulating network and system conditions in development, CI, and test environments. The agent job here is narrow and concrete: stand up controlled proxies for dependencies such as Redis, MySQL, Postgres, Kafka, or internal HTTP services, then inject failure modes like latency, timeouts, bandwidth throttling, connection resets, or hard outages while a test or diagnostic workflow is running. You invoke this skill when normal product usage is not enough because the task is not “run a proxy” in the abstract. The task is to prove whether a system behaves correctly when the network turns hostile. An agent can wire an app under test through Toxiproxy, reproduce an intermittent outage from a bug report, run the failing path again with deterministic latency, and return evidence about retries, circuit breakers, error handling, and recovery behavior. That is materially different from listing a generic proxy server or chaos-testing framework. The scope boundary matters. This entry is not a catalog card for Toxiproxy itself, and it is not a generic networking tool listing. It is specifically for failure injection during resilience testing and diagnostics. Integration points include Docker Compose test stacks, CI pipelines, language-specific Toxiproxy clients, and application test harnesses that need a scriptable HTTP API for changing network conditions mid-run. Upstream evidence is strong: official GitHub repo, MIT license, tagged releases, and active maintenance."
source: "https://github.com/Shopify/toxiproxy"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "Shopify/toxiproxy"
  github_stars: 11937
---

# Simulate network failures in integration tests with Toxiproxy

This ASE entry is built around Toxiproxy, the open source TCP proxy maintained by Shopify for simulating network and system conditions in development, CI, and test environments. The agent job here is narrow and concrete: stand up controlled proxies for dependencies such as Redis, MySQL, Postgres, Kafka, or internal HTTP services, then inject failure modes like latency, timeouts, bandwidth throttling, connection resets, or hard outages while a test or diagnostic workflow is running. You invoke this skill when normal product usage is not enough because the task is not “run a proxy” in the abstract. The task is to prove whether a system behaves correctly when the network turns hostile. An agent can wire an app under test through Toxiproxy, reproduce an intermittent outage from a bug report, run the failing path again with deterministic latency, and return evidence about retries, circuit breakers, error handling, and recovery behavior. That is materially different from listing a generic proxy server or chaos-testing framework. The scope boundary matters. This entry is not a catalog card for Toxiproxy itself, and it is not a generic networking tool listing. It is specifically for failure injection during resilience testing and diagnostics. Integration points include Docker Compose test stacks, CI pipelines, language-specific Toxiproxy clients, and application test harnesses that need a scriptable HTTP API for changing network conditions mid-run. Upstream evidence is strong: official GitHub repo, MIT license, tagged releases, and active maintenance.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/simulate-network-failures-in-integration-tests-with-toxiproxy/)
