---
title: "Probe public TLS endpoints for protocol, cipher, and certificate weaknesses before rollout with testssl.sh"
description: "Run a thorough TLS preflight against a host before launch, certificate renewal, or incident review."
verification: "listed"
source: "https://github.com/testssl/testssl.sh"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "testssl/testssl.sh"
  github_stars: 8986
---

# Probe public TLS endpoints for protocol, cipher, and certificate weaknesses before rollout with testssl.sh

Use testssl.sh when an agent needs to interrogate a live HTTPS or TLS endpoint and turn the results into an actionable hardening checklist. The agent probes supported protocols, cipher suites, certificate issues, renegotiation, and other security-relevant behaviors before a service goes live or after a change. Invoke this instead of using the product normally when the job is operational verification of a deployed endpoint, not generic certificate browsing or server administration. The boundary is narrow and concrete: endpoint-level TLS assessment with remediation-oriented findings.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/probe-public-tls-endpoints-for-protocol-cipher-and-certificate-weaknesses-before-rollout-with-testssl-sh/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/probe-public-tls-endpoints-for-protocol-cipher-and-certificate-weaknesses-before-rollout-with-testssl-sh
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/probe-public-tls-endpoints-for-protocol-cipher-and-certificate-weaknesses-before-rollout-with-testssl-sh`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/probe-public-tls-endpoints-for-protocol-cipher-and-certificate-weaknesses-before-rollout-with-testssl-sh/)
