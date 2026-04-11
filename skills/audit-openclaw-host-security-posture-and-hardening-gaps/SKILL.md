---
title: "Audit OpenClaw host security posture and hardening gaps"
description: "This skill uses OpenClaw’s healthcheck workflow to inspect the host running the assistant, surface risky exposure, and turn the findings into a staged hardening plan. It is for operator-style audits with explicit approval gates, not a generic software listing or a replacement for OS administration."
slug: audit-openclaw-host-security-posture-and-hardening-gaps
verification: security_reviewed
source: "https://github.com/openclaw/openclaw/tree/main/skills/healthcheck"
category:
- "Security & Verification"
framework:
- "OpenClaw"
---
# Audit OpenClaw host security posture and hardening gaps

This skill uses OpenClaw’s healthcheck workflow to inspect the host running the assistant, surface risky exposure, and turn the findings into a staged hardening plan. It is for operator-style audits with explicit approval gates, not a generic software listing or a replacement for OS administration.

## Installation

You can install this skill in any of these ways:

1. Browse and install from Agent Skill Exchange.
2. Clone or download this repository and copy the skill folder into your local skills directory.
3. Add it as a git submodule in your skills workspace.
4. Install it with your preferred agent skill or package manager if your setup supports that.
5. Copy the `SKILL.md` into an existing skill folder and adapt any referenced assets as needed.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-openclaw-host-security-posture-and-hardening-gaps/)
