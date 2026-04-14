---
title: "GitHub REST API Paginator Library"
description: "Provides a typed pagination wrapper for the GitHub REST API using Octokit.js and the @octokit/plugin-paginate-rest plugin. Handles Link header parsing, rate limit detection via X-RateLimit-Remaining, and automatic retry with exponential backoff. Supports listing issues, pull requests, commits, and workflow runs with async iterator patterns."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/github-rest-api-paginator-library/"
category:
  - "Library &amp; API Reference"
framework:
  - "Codex"
---

# GitHub REST API Paginator Library

This skill implements a robust GitHub REST API pagination utility using Octokit.js with the @octokit/plugin-paginate-rest and @octokit/plugin-throttling plugins. It wraps GitHub list endpoints (issues, pull requests, commits, check runs, workflow runs) with async generator functions that automatically follow Link header pagination. Rate limit detection reads the X-RateLimit-Remaining and X-RateLimit-Reset headers and pauses iteration when limits are close to exhaustion, resuming at the reset timestamp. The @octokit/plugin-throttling plugin adds configurable retry logic with exponential backoff for secondary rate limit responses (HTTP 429). The skill includes TypeScript type definitions generated from the GitHub OpenAPI spec, filter helpers for date ranges and labels, and streaming output for large result sets. Examples cover listing all closed PRs in a date range, paginating through all workflow run logs, and aggregating commit statistics across branches.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-rest-api-paginator-library/)
