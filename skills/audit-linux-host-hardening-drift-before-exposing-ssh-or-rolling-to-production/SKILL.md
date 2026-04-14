---
title: "Audit Linux host hardening drift before exposing SSH or rolling to production"
description: "Uses Lynis to run an on-host security audit and turn the findings into a prioritized hardening checklist for an agent or operator. Invoke it when a machine is about to become internet-facing, after base image changes, or whenever you need a quick read on hardening drift instead of a generic vulnerability scan."
verification: security_reviewed
source: "https://github.com/CISOfy/lynis"
category:
  - "Security &amp; Verification"
---

# Audit Linux host hardening drift before exposing SSH or rolling to production

Uses Lynis to run an on-host security audit and turn the findings into a prioritized hardening checklist for an agent or operator. Invoke it when a machine is about to become internet-facing, after base image changes, or whenever you need a quick read on hardening drift instead of a generic vulnerability scan.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-linux-host-hardening-drift-before-exposing-ssh-or-rolling-to-production/)
