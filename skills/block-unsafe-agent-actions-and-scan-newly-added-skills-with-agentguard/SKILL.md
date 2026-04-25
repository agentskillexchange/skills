---
title: "Block unsafe agent actions and scan newly added skills with AgentGuard"
description: "Add a runtime guard that evaluates agent actions, blocks dangerous commands or secret exposure, and audits new skills before they run."
verification: "security_reviewed"
source: "https://github.com/GoPlusSecurity/agentguard"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "GoPlusSecurity/agentguard"
  github_stars: 390
  npm_package: "@goplus/agentguard"
  npm_weekly_downloads: 2947
---

# Block unsafe agent actions and scan newly added skills with AgentGuard

Use AgentGuard when the job is to place a security review layer in front of agent actions and newly added skills, then stop obviously dangerous behavior before execution. The upstream project defines a concrete workflow: install the package, enable its hooks or plugin integration, scan new skills, and evaluate risky commands, secret access, and exfiltration patterns at runtime. Invoke this instead of a generic security SDK or passive policy document when you need live guardrail enforcement around agent execution. The scope boundary is specific: AgentGuard audits skills and evaluates agent actions against explicit runtime security rules. That makes it a skill-shaped security workflow, not just a general-purpose library or broad platform listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/block-unsafe-agent-actions-and-scan-newly-added-skills-with-agentguard/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/block-unsafe-agent-actions-and-scan-newly-added-skills-with-agentguard
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/block-unsafe-agent-actions-and-scan-newly-added-skills-with-agentguard`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/block-unsafe-agent-actions-and-scan-newly-added-skills-with-agentguard/)
