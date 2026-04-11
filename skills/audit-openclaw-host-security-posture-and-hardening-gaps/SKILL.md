---
title: "Audit OpenClaw host security posture and hardening gaps"
description: "This skill uses OpenClaw’s healthcheck workflow to inspect the host running the assistant, surface risky exposure, and turn the findings into a staged hardening plan. It is for operator-style audits with explicit approval gates, not a generic software listing or a replacement for OS administration."
verification: "security_reviewed"
source: "https://github.com/openclaw/openclaw/tree/main/skills/healthcheck"
category:
  - "Security &amp; Verification"
framework:
  - "OpenClaw"
---

# Audit OpenClaw host security posture and hardening gaps

This skill uses OpenClaw’s healthcheck workflow to inspect the host running the assistant, surface risky exposure, and turn the findings into a staged hardening plan. It is for operator-style audits with explicit approval gates, not a generic software listing or a replacement for OS administration.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-openclaw-host-security-posture-and-hardening-gaps/)
