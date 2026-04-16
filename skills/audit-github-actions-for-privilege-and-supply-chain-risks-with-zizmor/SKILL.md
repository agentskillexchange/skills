---
title: "Audit GitHub Actions for privilege and supply-chain risks with zizmor"
description: "Run a focused security pass on GitHub Actions workflows before merge so token misuse, dangerous permissions, and unpinned actions are caught early."
verification: "listed"
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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-github-actions-for-privilege-and-supply-chain-risks-with-zizmor/)
