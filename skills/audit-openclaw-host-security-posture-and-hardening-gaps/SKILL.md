---
name: Audit OpenClaw host security posture and hardening gaps
description: This skill uses OpenClaw’s healthcheck workflow to inspect the host running
  the assistant, surface risky exposure, and turn the findings into a staged hardening
  plan. It is for operator-style audits with explicit approval gates, not a generic
  software listing or a replacement for OS administration.
category: Security & Verification
framework: OpenClaw
verification: security_reviewed
source: https://github.com/openclaw/openclaw/tree/main/skills/healthcheck
tool_ecosystem:
  github_repo: openclaw/openclaw
  github_stars: 356821
  tool: openclaw
  license: MIT
  maintained: true
---
# Audit OpenClaw host security posture and hardening gaps
This skill uses OpenClaw’s healthcheck workflow to inspect the host running the assistant, surface risky exposure, and turn the findings into a staged hardening plan. It is for operator-style audits with explicit approval gates, not a generic software listing or a replacement for OS administration.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/audit-openclaw-host-security-posture-and-hardening-gaps
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/audit-openclaw-host-security-posture-and-hardening-gaps` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-openclaw-host-security-posture-and-hardening-gaps/)
