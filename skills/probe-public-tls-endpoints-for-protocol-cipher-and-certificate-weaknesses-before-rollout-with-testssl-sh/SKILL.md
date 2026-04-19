---
title: "Probe public TLS endpoints for protocol, cipher, and certificate weaknesses before rollout with testssl.sh"
description: "Use testssl.sh when an agent needs to interrogate a live HTTPS or TLS endpoint and turn the results into an actionable hardening checklist. The agent probes supported protocols, cipher suites, certificate issues, renegotiation, and other security-relevant behaviors before a service goes live or after a change. Invoke this instead of using the product normally when the job is operational verification of a deployed endpoint, not generic certificate browsing or server administration. The boundary is narrow and concrete: endpoint-level TLS assessment with remediation-oriented findings."
source: "https://github.com/testssl/testssl.sh"
verification: "listed"
category:
  - "Security &amp; Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "testssl/testssl.sh"
  github_stars: 8986
---

# Probe public TLS endpoints for protocol, cipher, and certificate weaknesses before rollout with testssl.sh

Use testssl.sh when an agent needs to interrogate a live HTTPS or TLS endpoint and turn the results into an actionable hardening checklist. The agent probes supported protocols, cipher suites, certificate issues, renegotiation, and other security-relevant behaviors before a service goes live or after a change. Invoke this instead of using the product normally when the job is operational verification of a deployed endpoint, not generic certificate browsing or server administration. The boundary is narrow and concrete: endpoint-level TLS assessment with remediation-oriented findings.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/probe-public-tls-endpoints-for-protocol-cipher-and-certificate-weaknesses-before-rollout-with-testssl-sh/)
