---
title: "Probe public TLS endpoints for protocol, cipher, and certificate weaknesses before rollout with testssl.sh"
description: "Use testssl.sh when an agent needs to interrogate a live HTTPS or TLS endpoint and turn the results into an actionable hardening checklist. The agent probes supported protocols, cipher suites, certificate issues, renegotiation, and other security-relevant behaviors before a service goes live or after a change. Invoke this instead of using the product normally when the job is operational verification of a deployed endpoint, not generic certificate browsing or server administration. The boundary is narrow and concrete: endpoint-level TLS assessment with remediation-oriented findings."
verification: listed
source: "https://github.com/testssl/testssl.sh"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "testssl/testssl.sh"
  github_stars: 8986
---

# Probe public TLS endpoints for protocol, cipher, and certificate weaknesses before rollout with testssl.sh

Use testssl.sh when an agent needs to interrogate a live HTTPS or TLS endpoint and turn the results into an actionable hardening checklist. The agent probes supported protocols, cipher suites, certificate issues, renegotiation, and other security-relevant behaviors before a service goes live or after a change. Invoke this instead of using the product normally when the job is operational verification of a deployed endpoint, not generic certificate browsing or server administration. The boundary is narrow and concrete: endpoint-level TLS assessment with remediation-oriented findings.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/probe-public-tls-endpoints-for-protocol-cipher-and-certificate-weaknesses-before-rollout-with-testssl-sh
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/probe-public-tls-endpoints-for-protocol-cipher-and-certificate-weaknesses-before-rollout-with-testssl-sh` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/probe-public-tls-endpoints-for-protocol-cipher-and-certificate-weaknesses-before-rollout-with-testssl-sh/)
