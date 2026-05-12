---
title: "GitHub REST API Paginator Library"
slug: "github-rest-api-paginator-library"
description: "Provides a typed pagination wrapper for the GitHub REST API using Octokit.js and the @octokit/plugin-paginate-rest plugin. Handles Link header parsing, rate limit detection via X-RateLimit-Remaining, and automatic retry with exponential backoff. Supports listing issues, pull requests, commits, and workflow runs with async iterator patterns."
verification: "security_reviewed"
source: "https://github.com/octokit/plugin-paginate-rest.js"
author: "Octokit"
category: "Library & API Reference"
framework: "Codex"
tool_ecosystem:
  github_repo: "octokit/plugin-paginate-rest.js"
  github_stars: 58
  npm_package: "@octokit/plugin-paginate-rest"
  npm_weekly_downloads: 26656585
---

# GitHub REST API Paginator Library

Provides a typed pagination wrapper for the GitHub REST API using Octokit.js and the @octokit/plugin-paginate-rest plugin. Handles Link header parsing, rate limit detection via X-RateLimit-Remaining, and automatic retry with exponential backoff. Supports listing issues, pull requests, commits, and workflow runs with async iterator patterns.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
npm install @octokit/plugin-paginate-rest
```

## Documentation

- https://github.com/octokit/plugin-paginate-rest.js#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-rest-api-paginator-library/)
