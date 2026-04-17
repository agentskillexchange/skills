---
title: "GitHub REST API Paginator Library"
description: "Provides a typed pagination wrapper for the GitHub REST API using Octokit.js and the @octokit/plugin-paginate-rest plugin. Handles Link header parsing, rate limit detection via X-RateLimit-Remaining, and automatic retry with exponential backoff. Supports listing issues, pull requests, commits, and workflow runs with async iterator patterns."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/github-rest-api-paginator-library/"
category:
  - "Library & API Reference"
framework:
  - "Codex"
---

# GitHub REST API Paginator Library

This skill implements a robust GitHub REST API pagination utility using Octokit.js with the @octokit/plugin-paginate-rest and @octokit/plugin-throttling plugins. It wraps GitHub list endpoints (issues, pull requests, commits, check runs, workflow runs) with async generator functions that automatically follow Link header pagination. Rate limit detection reads the X-RateLimit-Remaining and X-RateLimit-Reset headers and pauses iteration when limits are close to exhaustion, resuming at the reset timestamp. The @octokit/plugin-throttling plugin adds configurable retry logic with exponential backoff for secondary rate limit responses (HTTP 429). The skill includes TypeScript type definitions generated from the GitHub OpenAPI spec, filter helpers for date ranges and labels, and streaming output for large result sets. Examples cover listing all closed PRs in a date range, paginating through all workflow run logs, and aggregating commit statistics across branches.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/github-rest-api-paginator-library
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/github-rest-api-paginator-library` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-rest-api-paginator-library/)
