---
title: "Nginx Error Log Classifier"
slug: "nginx-error-log-classifier"
description: "Classifies and prioritizes Nginx error log entries using pattern matching against known error signatures and the GoAccess real-time log analyzer. Maps upstream timeout patterns to specific backend service degradation."
github_stars: 29930
verification: "security_reviewed"
source: "https://github.com/nginx/nginx"
category: "Runbooks & Diagnostics"
framework: "Cursor"
tool_ecosystem:
  github_repo: "nginx/nginx"
  github_stars: 29930
---

# Nginx Error Log Classifier

Classifies and prioritizes Nginx error log entries using pattern matching against known error signatures and the GoAccess real-time log analyzer. Maps upstream timeout patterns to specific backend service degradation.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nginx-error-log-classifier/)
