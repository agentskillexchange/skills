---
title: "Audit SSH servers and clients for weak algorithms and risky config drift with ssh-audit"
slug: "audit-ssh-servers-and-clients-for-weak-algorithms-and-risky-config-drift-with-ssh-audit"
description: "Inspect an SSH endpoint or config for outdated ciphers, key exchange choices, and hardening gaps before exposure or upgrades."
github_stars: 4164
verification: "security_reviewed"
source: "https://github.com/jtesta/ssh-audit"
author: "jtesta"
publisher_type: "individual"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "jtesta/ssh-audit"
  github_stars: 4164
---

# Audit SSH servers and clients for weak algorithms and risky config drift with ssh-audit

Inspect an SSH endpoint or config for outdated ciphers, key exchange choices, and hardening gaps before exposure or upgrades.

## Prerequisites

Python 3 or packaged binary, network access to SSH targets

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install from the repository or package source, then run `ssh-audit <host>` against the SSH endpoint or use its config-audit modes for local review.
```

## Documentation

- https://github.com/jtesta/ssh-audit

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-ssh-servers-and-clients-for-weak-algorithms-and-risky-config-drift-with-ssh-audit/)
