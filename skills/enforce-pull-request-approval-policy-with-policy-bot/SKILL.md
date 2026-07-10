---
title: "Enforce pull-request approval policy with Policy Bot"
description: "Codify complex GitHub review rules, evaluate pull requests, and expose approval status as a required check."
verification: "security_reviewed"
source: "https://github.com/palantir/policy-bot"
author: "Palantir"
publisher_type: "organization"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "palantir/policy-bot"
  github_stars: 1032
---

# Enforce pull-request approval policy with Policy Bot

Codify complex GitHub review rules, evaluate pull requests, and expose approval status as a required check.

## Prerequisites

Policy Bot GitHub App, GitHub repository, policy.yml

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Deploy Policy Bot as a GitHub App, configure the required repository permissions and webhook, add a policy.yml file to each repository, and make the Policy Bot status check required where merge gating is needed.
```

## Documentation

- https://github.com/palantir/policy-bot

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/enforce-pull-request-approval-policy-with-policy-bot/)
