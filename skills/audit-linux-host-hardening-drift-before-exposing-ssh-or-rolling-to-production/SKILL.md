---
title: "Audit Linux host hardening drift before exposing SSH or rolling to production"
description: "Uses Lynis to run an on-host security audit and turn the findings into a prioritized hardening checklist for an agent or operator. Invoke it when a machine is about to become internet-facing, after base image changes, or whenever you need a quick read on hardening drift instead of a generic vulnerability scan."
verification: "security_reviewed"
source: "https://github.com/CISOfy/lynis"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "CISOfy/lynis"
  github_stars: 15505
---

# Audit Linux host hardening drift before exposing SSH or rolling to production

This skill uses Lynis as an on-host auditing workflow for UNIX-like systems. Lynis runs locally, inspects system configuration and installed software, and returns findings, warnings, and hardening suggestions that help an agent understand whether a machine is drifting away from a sane baseline. The job-to-be-done is specific: audit a host before it becomes more exposed, then convert the output into a practical remediation queue.


Invoke this before exposing SSH on a new VPS, after changing base images, before a compliance review, after a round of package or configuration drift, or when a server “feels fine” but nobody has checked the hardening posture in a while. An agent can run ./lynis audit system, collect the high-signal warnings, group them by risk, and recommend the next changes to make, such as tightening SSH settings, reducing unnecessary packages, improving permissions, or addressing outdated software. Because Lynis is local-first, it is especially useful for private systems where you do not want to rely on an external scanner to enumerate the host.


The scope boundary is what keeps this skill shaped correctly. Lynis is not a SIEM, not a patch management platform, and not an active exploitation framework. It is a host audit and hardening assistant. Integration points include periodic cron audits, server build pipelines, security review checklists, package manager updates, and ticketing workflows that need actionable security findings tied to a specific host state.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-linux-host-hardening-drift-before-exposing-ssh-or-rolling-to-production/)
