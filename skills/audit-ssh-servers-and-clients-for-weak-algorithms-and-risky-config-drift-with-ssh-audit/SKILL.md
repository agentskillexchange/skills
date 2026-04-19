---
title: "Audit SSH servers and clients for weak algorithms and risky config drift with ssh-audit"
description: "Use ssh-audit when an agent needs to evaluate the security posture of an SSH service or client configuration and explain exactly what should change. The agent checks offered ciphers, key exchange algorithms, host key choices, protocol support, and version-level hardening signals, then produces remediation guidance for operators. Invoke this instead of using the product normally when the goal is a targeted SSH posture review before opening access, rotating config, or validating a hardening change. The scope stays bounded to SSH audit and remediation, which keeps it from collapsing into a generic server or security platform listing."
source: "https://github.com/jtesta/ssh-audit"
verification: "listed"
category:
  - "Security &amp; Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "jtesta/ssh-audit"
  github_stars: 4164
---

# Audit SSH servers and clients for weak algorithms and risky config drift with ssh-audit

Use ssh-audit when an agent needs to evaluate the security posture of an SSH service or client configuration and explain exactly what should change. The agent checks offered ciphers, key exchange algorithms, host key choices, protocol support, and version-level hardening signals, then produces remediation guidance for operators. Invoke this instead of using the product normally when the goal is a targeted SSH posture review before opening access, rotating config, or validating a hardening change. The scope stays bounded to SSH audit and remediation, which keeps it from collapsing into a generic server or security platform listing.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-ssh-servers-and-clients-for-weak-algorithms-and-risky-config-drift-with-ssh-audit/)
