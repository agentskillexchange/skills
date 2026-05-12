---
title: "Git Secret Scanner"
slug: "git-secret-scanner"
description: "Detects leaked secrets in Git repositories using pattern-based scanning with Gitleaks rule definitions and the GitHub Secret Scanning API. Identifies exposed API keys, tokens, and credentials across full commit history using git log --all -p analysis."
verification: "security_reviewed"
source: "https://github.com/gitleaks/gitleaks"
author: "gitleaks"
category: "Security & Verification"
framework: "Claude Agents"
tool_ecosystem:
  github_repo: "gitleaks/gitleaks"
  github_stars: 26420
---

# Git Secret Scanner

Detects leaked secrets in Git repositories using pattern-based scanning with Gitleaks rule definitions and the GitHub Secret Scanning API. Identifies exposed API keys, tokens, and credentials across full commit history using git log --all -p analysis.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/git-secret-scanner/)
