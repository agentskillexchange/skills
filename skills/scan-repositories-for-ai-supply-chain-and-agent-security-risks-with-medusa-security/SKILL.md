---
name: "Scan repositories for AI supply-chain and agent-security risks with Medusa Security"
slug: "scan-repositories-for-ai-supply-chain-and-agent-security-risks-with-medusa-security"
description: "Use Medusa Security before trusting a repository, dependency, or AI-agent codebase when an agent needs a focused scan for repo poisoning, prompt-injection, MCP, and AI supply-chain findings."
github_stars: 256
verification: "security_reviewed"
source: "https://github.com/Pantheon-Security/medusa"
author: "Pantheon Security"
publisher_type: "organization"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "Pantheon-Security/medusa"
  github_stars: 256
---

# Scan repositories for AI supply-chain and agent-security risks with Medusa Security

Use Medusa Security before trusting a repository, dependency, or AI-agent codebase when an agent needs a focused scan for repo poisoning, prompt-injection, MCP, and AI supply-chain findings.

## Prerequisites

Python 3.10+, pip, local repository path or remote Git URL

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with pip install medusa-security, then run medusa scan against a local repository or use medusa scan --git <repo> to assess a remote repository before trusting it.
```

## Documentation

- https://docs.medusa-security.dev

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scan-repositories-for-ai-supply-chain-and-agent-security-risks-with-medusa-security/)
