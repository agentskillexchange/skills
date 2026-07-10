---
title: "Audit Linux host hardening drift before exposing SSH or rolling to production"
description: "Uses Lynis to run an on-host security audit and turn the findings into a prioritized hardening checklist for an agent or operator. Invoke it when a machine is about to become internet-facing, after base image changes, or whenever you need a quick read on hardening drift instead of a generic vulnerability scan."
verification: "security_reviewed"
source: "https://github.com/CISOfy/lynis"
author: "CISOfy"
publisher_type: "Company"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "CISOfy/lynis"
  github_stars: 15505
---

# Audit Linux host hardening drift before exposing SSH or rolling to production

Uses Lynis to run an on-host security audit and turn the findings into a prioritized hardening checklist for an agent or operator. Invoke it when a machine is about to become internet-facing, after base image changes, or whenever you need a quick read on hardening drift instead of a generic vulnerability scan.

## Prerequisites

Shell access to the target UNIX-like host, with root or sudo recommended for fuller audit coverage

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
git clone https://github.com/CISOfy/lynis && cd lynis && ./lynis audit system
```

## Documentation

- https://cisofy.com/documentation/lynis/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-linux-host-hardening-drift-before-exposing-ssh-or-rolling-to-production/)
