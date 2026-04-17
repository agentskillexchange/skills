---
name: Mirror GitHub issues, pull requests, commits, and releases into SQLite for offline
  analysis
description: Use dogsheep/github-to-sqlite when an agent needs a local, queryable
  snapshot of GitHub activity instead of bouncing through the web UI or ad hoc API
  calls. The agent authenticates once, pulls the exact GitHub objects it needs, and
  leaves behind a SQLite database that can be inspected, joined, diffed, or handed
  to downstream tools.
category: Integrations & Connectors
framework: Multi-Framework
verification: security_reviewed
source: https://github.com/dogsheep/github-to-sqlite
tool_ecosystem:
  github_repo: dogsheep/github-to-sqlite
  github_stars: 461
  tool: github-to-sqlite
---
# Mirror GitHub issues, pull requests, commits, and releases into SQLite for offline analysis
Use dogsheep/github-to-sqlite when an agent needs a local, queryable snapshot of GitHub activity instead of bouncing through the web UI or ad hoc API calls. The agent authenticates once, pulls the exact GitHub objects it needs, and leaves behind a SQLite database that can be inspected, joined, diffed, or handed to downstream tools.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/mirror-github-issues-pull-requests-commits-and-releases-into-sqlite-for-offline-analysis
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/mirror-github-issues-pull-requests-commits-and-releases-into-sqlite-for-offline-analysis` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mirror-github-issues-pull-requests-commits-and-releases-into-sqlite-for-offline-analysis/)
