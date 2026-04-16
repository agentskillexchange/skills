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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-ssh-servers-and-clients-for-weak-algorithms-and-risky-config-drift-with-ssh-audit/)
