---
title: "Scan repositories for AI supply-chain and agent-security risks with Medusa Security"
description: "Use Medusa Security before trusting a repository, dependency, or AI-agent codebase when an agent needs a focused scan for repo poisoning, prompt-injection, MCP, and AI supply-chain findings."
verification: "security_reviewed"
source: "https://github.com/Pantheon-Security/medusa"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "Pantheon-Security/medusa"
  github_stars: 256
---

# Scan repositories for AI supply-chain and agent-security risks with Medusa Security

Use Medusa Security when the agent needs a pre-trust repository scan focused on AI and agent attack surfaces. The tool is built around scanning codebases for repo poisoning, prompt-injection-related artifacts, MCP risks, AI supply-chain issues, and broader security findings with dedicated CLI workflows.

Invoke this instead of using the product normally when the task is to vet a repository before adoption, execution, or dependency approval. The operator workflow is specific: install Medusa, scan a local repo or a remote Git URL, then use the findings to decide whether the codebase is safe enough to trust or merge.

The scope boundary keeps it skill-shaped. This is not a generic security platform listing and not a broad package card. It is the bounded workflow of running an AI-focused repository security scan before trust, execution, or handoff.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/scan-repositories-for-ai-supply-chain-and-agent-security-risks-with-medusa-security/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/scan-repositories-for-ai-supply-chain-and-agent-security-risks-with-medusa-security
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/scan-repositories-for-ai-supply-chain-and-agent-security-risks-with-medusa-security`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scan-repositories-for-ai-supply-chain-and-agent-security-risks-with-medusa-security/)
