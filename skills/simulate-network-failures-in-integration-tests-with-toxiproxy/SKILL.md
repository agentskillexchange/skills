---
title: Simulate network failures in integration tests with Toxiproxy
description: Use Toxiproxy when an agent needs to inject latency, disconnects, bandwidth limits, or packet-like failure modes into real service calls during development, CI, or incident reproduction. The agent routes app traffic through controlled TCP proxies, applies toxics at the right moment, and reports which dependency paths fail gracefully versus which ones crack under stress.
slug: simulate-network-failures-in-integration-tests-with-toxiproxy
verification: listed
source: https://github.com/Shopify/toxiproxy
category:
- Runbooks &amp; Diagnostics
framework:
- Multi-Framework
---
# Simulate network failures in integration tests with Toxiproxy

Use Toxiproxy when an agent needs to inject latency, disconnects, bandwidth limits, or packet-like failure modes into real service calls during development, CI, or incident reproduction. The agent routes app traffic through controlled TCP proxies, applies toxics at the right moment, and reports which dependency paths fail gracefully versus which ones crack under stress.

## Installation

You can install this skill in any of these ways:

1. Browse and install from Agent Skill Exchange.
2. Clone or download this repository and copy the skill folder into your local skills directory.
3. Add it as a git submodule in your skills workspace.
4. Install it with your preferred agent skill or package manager if your setup supports that.
5. Copy the `SKILL.md` into an existing skill folder and adapt any referenced assets as needed.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/simulate-network-failures-in-integration-tests-with-toxiproxy/)
