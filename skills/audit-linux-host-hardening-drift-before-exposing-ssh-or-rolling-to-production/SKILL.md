---
title: "Audit Linux host hardening drift before exposing SSH or rolling to production"
description: "Uses Lynis to run an on-host security audit and turn the findings into a prioritized hardening checklist for an agent or operator. Invoke it when a machine is about to become internet-facing, after base image changes, or whenever you need a quick read on hardening drift instead of a generic vulnerability scan."
verification: security_reviewed
source: "https://github.com/CISOfy/lynis"
category:
  - "Security &amp; Verification"
framework:
  - "Multi-Framework"
---

# Audit Linux host hardening drift before exposing SSH or rolling to production

This skill uses Lynis as an on-host auditing workflow for UNIX-like systems. Lynis runs locally, inspects system configuration and installed software, and returns findings, warnings, and hardening suggestions that help an agent understand whether a machine is drifting away from a sane baseline. The job-to-be-done is specific: audit a host before it becomes more exposed, then convert the output into a practical remediation queue.

Invoke this before exposing SSH on a new VPS, after changing base images, before a compliance review, after a round of package or configuration drift, or when a server “feels fine” but nobody has checked the hardening posture in a while. An agent can run ./lynis audit system, collect the high-signal warnings, group them by risk, and recommend the next changes to make, such as tightening SSH settings, reducing unnecessary packages, improving permissions, or addressing outdated software. Because Lynis is local-first, it is especially useful for private systems where you do not want to rely on an external scanner to enumerate the host.

The scope boundary is what keeps this skill shaped correctly. Lynis is not a SIEM, not a patch management platform, and not an active exploitation framework. It is a host audit and hardening assistant. Integration points include periodic cron audits, server build pipelines, security review checklists, package manager updates, and ticketing workflows that need actionable security findings tied to a specific host state.

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
