---
title: "Probe public TLS endpoints for protocol, cipher, and certificate weaknesses before rollout with testssl.sh"
description: "Run a thorough TLS preflight against a host before launch, certificate renewal, or incident review."
verification: "listed"
source: "https://github.com/testssl/testssl.sh"
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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/probe-public-tls-endpoints-for-protocol-cipher-and-certificate-weaknesses-before-rollout-with-testssl-sh/)
