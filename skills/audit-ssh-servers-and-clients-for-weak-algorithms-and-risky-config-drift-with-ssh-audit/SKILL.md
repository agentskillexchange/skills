---
title: "Audit SSH servers and clients for weak algorithms and risky config drift with ssh-audit"
description: "Inspect an SSH endpoint or config for outdated ciphers, key exchange choices, and hardening gaps before exposure or upgrades."
verification: "listed"
source: "https://github.com/jtesta/ssh-audit"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "jtesta/ssh-audit"
  github_stars: 4164
---

# Audit SSH servers and clients for weak algorithms and risky config drift with ssh-audit

Use ssh-audit when an agent needs to evaluate the security posture of an SSH service or client configuration and explain exactly what should change. The agent checks offered ciphers, key exchange algorithms, host key choices, protocol support, and version-level hardening signals, then produces remediation guidance for operators. Invoke this instead of using the product normally when the goal is a targeted SSH posture review before opening access, rotating config, or validating a hardening change. The scope stays bounded to SSH audit and remediation, which keeps it from collapsing into a generic server or security platform listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/audit-ssh-servers-and-clients-for-weak-algorithms-and-risky-config-drift-with-ssh-audit/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/audit-ssh-servers-and-clients-for-weak-algorithms-and-risky-config-drift-with-ssh-audit
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/audit-ssh-servers-and-clients-for-weak-algorithms-and-risky-config-drift-with-ssh-audit`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-ssh-servers-and-clients-for-weak-algorithms-and-risky-config-drift-with-ssh-audit/)
