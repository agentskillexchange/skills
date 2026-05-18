---
name: "Block unsafe agent actions and scan newly added skills with AgentGuard"
slug: "block-unsafe-agent-actions-and-scan-newly-added-skills-with-agentguard"
description: "Add a runtime guard that evaluates agent actions, blocks dangerous commands or secret exposure, and audits new skills before they run."
github_stars: 390
verification: "listed"
source: "https://github.com/GoPlusSecurity/agentguard"
author: "GoPlusSecurity"
publisher_type: "open_source_project"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "GoPlusSecurity/agentguard"
  github_stars: 390
  npm_package: "@goplus/agentguard"
  npm_weekly_downloads: 2947
---

# Block unsafe agent actions and scan newly added skills with AgentGuard

Add a runtime guard that evaluates agent actions, blocks dangerous commands or secret exposure, and audits new skills before they run.

## Prerequisites

Node.js, supported agent runtime such as Claude Code or OpenClaw, local skill directories and agent action hooks

## Installation

Use the upstream install or setup path that matches your environment:
- npm install -g @goplus/agentguard
- git clone https://github.com/GoPlusSecurity/agentguard.git
- npm install @goplus/agentguard

Requirements and caveats from upstream:
- # Requires the local OpenClaw Gateway at 127.0.0.1:18789.
- | 3 | **Network Exposure** | Detects dangerous ports bound to 0.0.0.0 (Redis, Docker API, MySQL, etc.), checks firewall status, flags suspicious outbound connections |
- **Note:** Patrol requires an OpenClaw environment. For non-OpenClaw setups, use /agentguard scan and /agentguard report for manual security checks.

Basic usage or getting-started notes:
- 8 comprehensive security checks run on a configurable schedule
- # skills, and reports matches back. Run in cron / on boot.
- # Optional: after one subscribe run, install an OpenClaw isolated cron job that

- Source: https://github.com/GoPlusSecurity/agentguard
- Extracted from upstream docs: https://raw.githubusercontent.com/GoPlusSecurity/agentguard/HEAD/README.md

## Documentation

- https://github.com/GoPlusSecurity/agentguard

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/block-unsafe-agent-actions-and-scan-newly-added-skills-with-agentguard/)
