---
name: "REST API Changelog Tracker"
slug: "rest-api-changelog-tracker"
description: "Tracks breaking changes across REST API versions by diffing OpenAPI specs with oasdiff and monitoring endpoint deprecation headers. Stores version history in SQLite via better-sqlite3."
github_stars: 1184
verification: "security_reviewed"
source: "https://github.com/oasdiff/oasdiff"
author: "oasdiff"
category: "Library & API Reference"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "oasdiff/oasdiff"
  github_stars: 1184
---

# REST API Changelog Tracker

Tracks breaking changes across REST API versions by diffing OpenAPI specs with oasdiff and monitoring endpoint deprecation headers. Stores version history in SQLite via better-sqlite3.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
go install github.com/oasdiff/oasdiff@latest
```

## Documentation

- https://www.oasdiff.com/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rest-api-changelog-tracker/)
