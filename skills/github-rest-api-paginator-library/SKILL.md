---
title: GitHub REST API Paginator Library
description: This skill implements a robust GitHub REST API pagination utility using
  Octokit.js with the @octokit/plugin-paginate-rest and @octokit/plugin-throttling
  plugins. It wraps GitHub list endpoints (issues, pull requests, commits, check runs,
  workflow runs) with async generator functions that automatically follow Link header
  pagination. Rate limit detection reads the X-RateLimit-Remaining and X-RateLimit-Reset
  headers and pauses iteration when limits are close to exhaustion, resuming at the
  reset timestamp. The @octokit/plugin-throttling plugin adds configurable retry logic
  with exponential backoff for secondary rate limit responses (HTTP 429). The skill
  includes TypeScript type definitions generated from the GitHub OpenAPI spec, filter
  helpers for date ranges and labels, and streaming output for large result sets.
  Examples cover listing all closed PRs in a date range, paginating through all workflow
  run logs, and aggregating commit statistics across branches.
verification: security_reviewed
source: https://agentskillexchange.com/skills/github-rest-api-paginator-library/
category:
- Library &amp; API Reference
framework:
- Codex
---

# GitHub REST API Paginator Library

This skill implements a robust GitHub REST API pagination utility using Octokit.js with the @octokit/plugin-paginate-rest and @octokit/plugin-throttling plugins. It wraps GitHub list endpoints (issues, pull requests, commits, check runs, workflow runs) with async generator functions that automatically follow Link header pagination. Rate limit detection reads the X-RateLimit-Remaining and X-RateLimit-Reset headers and pauses iteration when limits are close to exhaustion, resuming at the reset timestamp. The @octokit/plugin-throttling plugin adds configurable retry logic with exponential backoff for secondary rate limit responses (HTTP 429). The skill includes TypeScript type definitions generated from the GitHub OpenAPI spec, filter helpers for date ranges and labels, and streaming output for large result sets. Examples cover listing all closed PRs in a date range, paginating through all workflow run logs, and aggregating commit statistics across branches.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-rest-api-paginator-library/)
