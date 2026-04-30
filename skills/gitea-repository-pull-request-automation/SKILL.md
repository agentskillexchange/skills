---
title: "Gitea Repository & Pull Request Automation"
description: "Automates repository administration, pull request workflows, issue triage, and release operations against Gitea using its REST API and webhook system. Useful for self-hosted software teams that want GitHub-like automation without leaving their own infrastructure."
verification: "security_reviewed"
source: "https://github.com/go-gitea/gitea"
author: "go-gitea"
publisher_type: "Open Source Project"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "go-gitea/gitea"
  github_stars: 54880
---

# Gitea Repository & Pull Request Automation

Automates repository administration, pull request workflows, issue triage, and release operations against Gitea using its REST API and webhook system. Useful for self-hosted software teams that want GitHub-like automation without leaving their own infrastructure.

## Prerequisites

Docker, Docker Compose, Gitea REST API

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
docker compose up -d
```

## Documentation

- https://docs.gitea.com/api

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitea-repository-pull-request-automation/)
