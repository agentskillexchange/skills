---
name: "Mirror GitHub issues, pull requests, commits, and releases into SQLite for offline analysis"
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

Use the upstream install or setup path that matches your environment:
- $ pip install github-to-sqlite

Requirements and caveats from upstream:
- $ github-to-sqlite pull-requests --state=open --org=psf --org=python github.db
- $ github-to-sqlite pull-requests --search='org:python defaultdict state:closed created:<2023-09-01' github.db

Basic usage or getting-started notes:
- Run this command and paste in your new token:
- Example: [issues table](https://github-to-sqlite.dogsheep.net/github/issues)
- While pull requests are a type of issue, you will get more information on pull requests by pulling them separately. For example, whether a pull request has been merged and when.

- Source: https://github.com/dogsheep/github-to-sqlite
- Extracted from upstream docs: https://raw.githubusercontent.com/dogsheep/github-to-sqlite/HEAD/README.md

## Documentation

- https://github-to-sqlite.dogsheep.net/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mirror-github-issues-pull-requests-commits-and-releases-into-sqlite-for-offline-analysis/)
