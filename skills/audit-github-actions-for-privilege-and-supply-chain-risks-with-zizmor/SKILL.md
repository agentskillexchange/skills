---
title: "Audit GitHub Actions for privilege and supply-chain risks with zizmor"
description: "Run a focused security pass on GitHub Actions workflows before merge so token misuse, dangerous permissions, and unpinned actions are caught early."
verification: listed
source: "https://github.com/zizmorcore/zizmor"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "zizmorcore/zizmor"
  github_stars: 4186
  license: "MIT"
---

# Audit GitHub Actions for privilege and supply-chain risks with zizmor

Use zizmor when an agent is reviewing GitHub Actions changes and needs a security-first gate before those workflows land. The agent can scan workflow files, flag risky permission scopes, catch untrusted input paths, and surface supply-chain issues such as unsafe action pinning. The boundary is narrow and clear: pre-merge GitHub Actions security review, not a generic CI platform listing or all-purpose GitHub automation card.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/audit-github-actions-for-privilege-and-supply-chain-risks-with-zizmor
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/audit-github-actions-for-privilege-and-supply-chain-risks-with-zizmor` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-github-actions-for-privilege-and-supply-chain-risks-with-zizmor/)
