---
title: "Audit OpenClaw host security posture and hardening gaps"
description: "This skill uses OpenClaw's healthcheck workflow to inspect the host running the assistant, surface risky exposure, and turn the findings into a staged hardening plan. It is for operator-style audits with explicit approval gates, not a generic software listing or a replacement for OS administration."
verification: security_reviewed
source: "https://github.com/openclaw/openclaw/tree/main/skills/healthcheck"
---

# Audit OpenClaw host security posture and hardening gaps

This skill uses OpenClaw's healthcheck workflow to inspect the host running the assistant, surface risky exposure, and turn the findings into a staged hardening plan. It is for operator-style audits with explicit approval gates, not a generic software listing or a replacement for OS administration.

## Installation

Choose the path that fits your setup:

1. Clone this repository and use the skill locally.
2. Copy the skill folder into your local skills directory.
3. Add the skill as a Git submodule in your skills workspace.
4. Vendor the files into an internal skill catalog for your team.
5. Reference the upstream source and recreate the skill in your own agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-openclaw-host-security-posture-and-hardening-gaps/)
