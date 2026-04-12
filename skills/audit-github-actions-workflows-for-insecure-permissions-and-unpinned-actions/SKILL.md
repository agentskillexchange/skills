---
title: "Audit GitHub Actions workflows for insecure permissions and unpinned actions"
slug: "audit-github-actions-workflows-for-insecure-permissions-and-unpinned-actions"
verification: "security_reviewed"
category:
  - "Security &amp; Verification"
framework:
  - "Multi-Framework"
source: "https://github.com/zizmorcore/zizmor"
tool_ecosystem:
  github_repo: "zizmorcore/zizmor"
  github_stars: 4132
---

# Audit GitHub Actions workflows for insecure permissions and unpinned actions

This ASE skill uses zizmor to audit GitHub Actions workflows and composite actions for security mistakes before they ship. An agent can scan local repos or remote GitHub repositories, flag risky permission scopes and unsafe workflow patterns, and return plain output, GitHub-native findings, or SARIF for follow-up automation.

## Installation

Choose the method that fits your setup:

1. Clone or download this repo and copy the skill folder into your local skills directory.
2. Install from the Agent Skill Exchange repo with your preferred Git workflow.
3. Add the skill folder as a git submodule if you manage skills as dependencies.
4. Copy the files manually into a local custom-skills directory for testing.
5. Use any marketplace or sync tooling you already have for pulling ASE skills.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-github-actions-workflows-for-insecure-permissions-and-unpinned-actions/)
