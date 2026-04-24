---
title: "Audit OpenClaw host security posture and hardening gaps"
description: "This skill uses OpenClaw’s healthcheck workflow to inspect the host running the assistant, surface risky exposure, and turn the findings into a staged hardening plan. It is for operator-style audits with explicit approval gates, not a generic software listing or a replacement for OS administration."
verification: "security_reviewed"
source: "https://github.com/openclaw/openclaw/tree/main/skills/healthcheck"
category:
  - "Security & Verification"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "openclaw/openclaw"
  github_stars: 356821
---

# Audit OpenClaw host security posture and hardening gaps

This skill uses OpenClaw’s healthcheck workflow to inspect the host running the assistant, surface risky exposure, and turn the findings into a staged hardening plan. It is for operator-style audits with explicit approval gates, not a generic software listing or a replacement for OS administration.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/audit-openclaw-host-security-posture-and-hardening-gaps/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/audit-openclaw-host-security-posture-and-hardening-gaps
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/audit-openclaw-host-security-posture-and-hardening-gaps`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-openclaw-host-security-posture-and-hardening-gaps/)
