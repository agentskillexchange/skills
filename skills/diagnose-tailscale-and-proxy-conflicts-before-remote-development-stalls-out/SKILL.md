---
title: "Diagnose Tailscale and proxy conflicts before remote development stalls out"
description: "Use tunnel-doctor in Claude Code when Tailscale partially works but SSH, browser, git, or Docker paths fail because proxy, route, or double-tunneling conflicts need a structured diagnosis."
verification: "security_reviewed"
source: "https://github.com/daymade/claude-code-skills/blob/main/tunnel-doctor/SKILL.md"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "daymade/claude-code-skills"
  github_stars: 910
---

# Diagnose Tailscale and proxy conflicts before remote development stalls out

tunnel-doctor is a Claude Code skill for diagnosing and fixing multi-layer conflicts between Tailscale and proxy/VPN tooling on macOS. It walks an agent through symptom-based checks for route hijacking, HTTP proxy environment variables, system proxy bypass, SSH ProxyCommand double tunneling, and VM or container proxy propagation, including remote development and WSL-over-Tailscale edge cases.

Invoke this instead of using Tailscale, Shadowrocket, Clash, Surge, Docker, or SSH normally when basic connectivity signals are misleading — for example when tailscale ping works but SSH times out, curl and browser disagree, git push fails through relays, or Docker image fetches break behind TUN and proxy layers. The scope boundary is clear: this is not a product listing for Tailscale or proxy software. It is a repeatable operator runbook for isolating the failing network layer and applying the right remediation path inside a Claude Code troubleshooting workflow.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/diagnose-tailscale-and-proxy-conflicts-before-remote-development-stalls-out/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/diagnose-tailscale-and-proxy-conflicts-before-remote-development-stalls-out
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/diagnose-tailscale-and-proxy-conflicts-before-remote-development-stalls-out`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diagnose-tailscale-and-proxy-conflicts-before-remote-development-stalls-out/)
