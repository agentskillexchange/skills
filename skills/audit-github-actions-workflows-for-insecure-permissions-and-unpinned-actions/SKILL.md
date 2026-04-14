---
title: "Audit GitHub Actions workflows for insecure permissions and unpinned actions"
description: "This ASE skill uses zizmor to audit GitHub Actions workflows and composite actions for security mistakes before they ship. An agent can scan local repos or remote GitHub repositories, flag risky permission scopes and unsafe workflow patterns, and return plain output, GitHub-native findings, or SARIF for follow-up automation."
verification: security_reviewed
source: "https://github.com/zizmorcore/zizmor"
category:
  - "Security &amp; Verification"
tool_ecosystem:
  github_repo: "zizmorcore/zizmor"
  github_stars: 4145
---

# Audit GitHub Actions workflows for insecure permissions and unpinned actions

This ASE skill uses zizmor to audit GitHub Actions workflows and composite actions for security mistakes before they ship. An agent can scan local repos or remote GitHub repositories, flag risky permission scopes and unsafe workflow patterns, and return plain output, GitHub-native findings, or SARIF for follow-up automation.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-github-actions-workflows-for-insecure-permissions-and-unpinned-actions/)
