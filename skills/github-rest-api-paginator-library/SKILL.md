---
title: "GitHub REST API Paginator Library"
description: "Provides a typed pagination wrapper for the GitHub REST API using Octokit.js and the @octokit/plugin-paginate-rest plugin. Handles Link header parsing, rate limit detection via X-RateLimit-Remaining, and automatic retry with exponential backoff. Supports listing issues, pull requests, commits, and workflow runs with async iterator patterns."
verification: "security_reviewed"
source: "https://github.com/octokit/plugin-paginate-rest.js"
category:
  - "Library & API Reference"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "octokit/plugin-paginate-rest.js"
  github_stars: 58
  npm_package: "@octokit/plugin-paginate-rest"
  npm_weekly_downloads: 26656585
---

# GitHub REST API Paginator Library

This skill implements a robust GitHub REST API pagination utility using Octokit.js with the @octokit/plugin-paginate-rest and @octokit/plugin-throttling plugins. It wraps GitHub list endpoints (issues, pull requests, commits, check runs, workflow runs) with async generator functions that automatically follow Link header pagination. Rate limit detection reads the X-RateLimit-Remaining and X-RateLimit-Reset headers and pauses iteration when limits are close to exhaustion, resuming at the reset timestamp. The @octokit/plugin-throttling plugin adds configurable retry logic with exponential backoff for secondary rate limit responses (HTTP 429). The skill includes TypeScript type definitions generated from the GitHub OpenAPI spec, filter helpers for date ranges and labels, and streaming output for large result sets. Examples cover listing all closed PRs in a date range, paginating through all workflow run logs, and aggregating commit statistics across branches.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/github-rest-api-paginator-library/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/github-rest-api-paginator-library
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/github-rest-api-paginator-library`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-rest-api-paginator-library/)
