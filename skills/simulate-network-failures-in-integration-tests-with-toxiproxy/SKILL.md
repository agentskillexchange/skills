---
name: "Simulate network failures in integration tests with Toxiproxy"
slug: "simulate-network-failures-in-integration-tests-with-toxiproxy"
description: "Use Toxiproxy when an agent needs to inject latency, disconnects, bandwidth limits, or packet-like failure modes into real service calls during development, CI, or incident reproduction. The agent routes app traffic through controlled TCP proxies, applies toxics at the right moment, and reports which dependency paths fail gracefully versus which ones crack under stress."
github_stars: 11937
verification: "security_reviewed"
source: "https://github.com/Shopify/toxiproxy"
author: "Shopify"
publisher_type: "Company"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "Shopify/toxiproxy"
  github_stars: 11937
---

# Simulate network failures in integration tests with Toxiproxy

Use Toxiproxy when an agent needs to inject latency, disconnects, bandwidth limits, or packet-like failure modes into real service calls during development, CI, or incident reproduction. The agent routes app traffic through controlled TCP proxies, applies toxics at the right moment, and reports which dependency paths fail gracefully versus which ones crack under stress.

## Prerequisites

Toxiproxy server plus a client library or HTTP API access from the test harness

## Installation

Use the upstream install or setup path that matches your environment:
- $ brew tap shopify/shopify
- $ brew install toxiproxy
- $ docker pull ghcr.io/shopify/toxiproxy
- $ docker run --rm -it ghcr.io/shopify/toxiproxy

Requirements and caveats from upstream:
- cross-platform and require root, which makes them problematic in test,
- [toxiproxy-python](https://github.com/douglas/toxiproxy-python)
- [toxiproxy-node-client](https://github.com/ihsw/toxiproxy-node-client)

Basic usage or getting-started notes:
- Toxiproxy usage consists of two parts. A TCP proxy written in Go (what this
- and can then manipulate their health via HTTP. See [Usage](#usage)
- For example, to add 1000ms of latency to the response of MySQL from the [Ruby

- Source: https://github.com/Shopify/toxiproxy
- Extracted from upstream docs: https://raw.githubusercontent.com/Shopify/toxiproxy/HEAD/README.md

## Documentation

- https://github.com/Shopify/toxiproxy

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/simulate-network-failures-in-integration-tests-with-toxiproxy/)
