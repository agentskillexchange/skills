---
title: "Baseline and Review Repository Secret Findings with detect-secrets"
slug: "baseline-and-review-repository-secret-findings-with-detect-secrets"
description: "Scan a repository for secrets, keep an auditable baseline, and review only newly introduced findings during commits or CI checks."
github_stars: 4482
verification: "security_reviewed"
source: "https://github.com/Yelp/detect-secrets"
author: "Yelp"
publisher_type: "organization"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "Yelp/detect-secrets"
  github_stars: 4482
---

# Baseline and Review Repository Secret Findings with detect-secrets

Scan a repository for secrets, keep an auditable baseline, and review only newly introduced findings during commits or CI checks.

## Prerequisites

Python, detect-secrets CLI, git repository

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with pip, then create or update a baseline before scanning: pip install detect-secrets && detect-secrets scan > .secrets.baseline
```

## Documentation

- https://github.com/Yelp/detect-secrets

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/baseline-and-review-repository-secret-findings-with-detect-secrets/)
