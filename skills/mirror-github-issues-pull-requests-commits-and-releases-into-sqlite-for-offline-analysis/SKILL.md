---
title: "Mirror GitHub issues, pull requests, commits, and releases into SQLite for offline analysis"
slug: "mirror-github-issues-pull-requests-commits-and-releases-into-sqlite-for-offline-analysis"
description: "Use dogsheep/github-to-sqlite when an agent needs a local, queryable snapshot of GitHub activity instead of bouncing through the web UI or ad hoc API calls. The agent authenticates once, pulls the exact GitHub objects it needs, and leaves behind a SQLite database that can be inspected, joined, diffed, or handed to downstream tools."
github_stars: 461
verification: "security_reviewed"
source: "https://github.com/dogsheep/github-to-sqlite"
author: "Dogsheep"
category: "Integrations & Connectors"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "dogsheep/github-to-sqlite"
  github_stars: 461
---

# Mirror GitHub issues, pull requests, commits, and releases into SQLite for offline analysis

Use dogsheep/github-to-sqlite when an agent needs a local, queryable snapshot of GitHub activity instead of bouncing through the web UI or ad hoc API calls. The agent authenticates once, pulls the exact GitHub objects it needs, and leaves behind a SQLite database that can be inspected, joined, diffed, or handed to downstream tools.

## Prerequisites

Python 3, pip, SQLite, and a GitHub personal access token or GITHUB_TOKEN/auth.json for authenticated or higher-rate fetches.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
pip install github-to-sqlite
```

## Documentation

- https://github-to-sqlite.dogsheep.net/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mirror-github-issues-pull-requests-commits-and-releases-into-sqlite-for-offline-analysis/)
