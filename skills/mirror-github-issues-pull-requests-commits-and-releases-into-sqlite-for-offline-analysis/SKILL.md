---
title: "Mirror GitHub issues, pull requests, commits, and releases into SQLite for offline analysis"
description: "Use dogsheep/github-to-sqlite when an agent needs a local, queryable snapshot of GitHub activity instead of bouncing through the web UI or ad hoc API calls. The agent authenticates once, pulls the exact GitHub objects it needs, and leaves behind a SQLite database that can be inspected, joined, diffed, or handed to downstream tools."
verification: listed
source: "https://github.com/dogsheep/github-to-sqlite"
tool_ecosystem:
  github_repo: "dogsheep/github-to-sqlite"
  github_stars: 461
---

# Mirror GitHub issues, pull requests, commits, and releases into SQLite for offline analysis

Use dogsheep/github-to-sqlite when an agent needs a local, queryable snapshot of GitHub activity instead of bouncing through the web UI or ad hoc API calls. The agent authenticates once, pulls the exact GitHub objects it needs, and leaves behind a SQLite database that can be inspected, joined, diffed, or handed to downstream tools.

## Installation

Choose the path that fits your setup:

1. Clone this repository and use the skill locally.
2. Copy the skill folder into your local skills directory.
3. Add the skill as a Git submodule in your skills workspace.
4. Vendor the files into an internal skill catalog for your team.
5. Reference the upstream source and recreate the skill in your own agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mirror-github-issues-pull-requests-commits-and-releases-into-sqlite-for-offline-analysis/)
