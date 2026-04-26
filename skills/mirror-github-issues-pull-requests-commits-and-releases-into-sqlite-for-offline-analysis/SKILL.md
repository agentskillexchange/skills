---
title: "Mirror GitHub issues, pull requests, commits, and releases into SQLite for offline analysis"
description: "Use dogsheep/github-to-sqlite when an agent needs a local, queryable snapshot of GitHub activity instead of bouncing through the web UI or ad hoc API calls. The agent authenticates once, pulls the exact GitHub objects it needs, and leaves behind a SQLite database that can be inspected, joined, diffed, or handed to downstream tools."
verification: "security_reviewed"
source: "https://github.com/dogsheep/github-to-sqlite"
category:
  - "Integrations & Connectors"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "dogsheep/github-to-sqlite"
  github_stars: 461
---

# Mirror GitHub issues, pull requests, commits, and releases into SQLite for offline analysis

Use dogsheep/github-to-sqlite when an agent needs a local, queryable snapshot of GitHub activity instead of bouncing through the web UI or ad hoc API calls. The agent authenticates once, pulls the exact GitHub objects it needs, and leaves behind a SQLite database that can be inspected, joined, diffed, or handed to downstream tools.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/mirror-github-issues-pull-requests-commits-and-releases-into-sqlite-for-offline-analysis/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/mirror-github-issues-pull-requests-commits-and-releases-into-sqlite-for-offline-analysis
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/mirror-github-issues-pull-requests-commits-and-releases-into-sqlite-for-offline-analysis`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mirror-github-issues-pull-requests-commits-and-releases-into-sqlite-for-offline-analysis/)
