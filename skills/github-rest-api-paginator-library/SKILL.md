---
title: "GitHub REST API Paginator Library"
description: "Provides a typed pagination wrapper for the GitHub REST API using Octokit.js and the @octokit/plugin-paginate-rest plugin. Handles Link header parsing, rate limit detection via X-RateLimit-Remaining, and automatic retry with exponential backoff. Supports listing issues, pull requests, commits, and workflow runs with async iterator patterns."
slug: "github-rest-api-paginator-library"
category:
  - "Library &amp; API Reference"
framework:
  - "Codex"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/github-rest-api-paginator-library/"
---

# GitHub REST API Paginator Library

Provides a typed pagination wrapper for the GitHub REST API using Octokit.js and the @octokit/plugin-paginate-rest plugin. Handles Link header parsing, rate limit detection via X-RateLimit-Remaining, and automatic retry with exponential backoff. Supports listing issues, pull requests, commits, and workflow runs with async iterator patterns.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install github-rest-api-paginator-library
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill implements a robust GitHub REST API pagination utility using Octokit.js with the @octokit/plugin-paginate-rest and @octokit/plugin-throttling plugins. It wraps GitHub list endpoints (issues, pull requests, commits, check runs, workflow runs) with async generator functions that automatically follow Link header pagination. Rate limit detection reads the X-RateLimit-Remaining and X-RateLimit-Reset headers and pauses iteration when limits are close to exhaustion, resuming at the reset timestamp. The @octokit/plugin-throttling plugin adds configurable retry logic with exponential backoff for secondary rate limit responses (HTTP 429). The skill includes TypeScript type definitions generated from the GitHub OpenAPI spec, filter helpers for date ranges and labels, and streaming output for large result sets. Examples cover listing all closed PRs in a date range, paginating through all workflow run logs, and aggregating commit statistics across branches.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-rest-api-paginator-library/)
