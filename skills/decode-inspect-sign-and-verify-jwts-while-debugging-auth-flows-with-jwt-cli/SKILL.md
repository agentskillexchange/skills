---
title: "Decode, inspect, sign, and verify JWTs while debugging auth flows with jwt-cli"
description: "Decode JWTs, inspect claims, and verify or sign tokens with local keys during auth debugging and test setup."
verification: "listed"
source: "https://github.com/mike-engel/jwt-cli"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "mike-engel/jwt-cli"
  github_stars: 1464
  npm_package: "jwt-cli"
  npm_weekly_downloads: 3419
---

# Decode, inspect, sign, and verify JWTs while debugging auth flows with jwt-cli

Use jwt-cli when an agent needs to decode JWT headers and claims, inspect token contents, or sign and verify tokens against local secrets or keys while debugging an authentication flow or building test fixtures. A user should invoke this instead of using an auth provider or SDK normally when the task is token-level inspection or offline verification, not running the identity platform itself. The scope boundary is specific and skill-shaped: it operates on supplied JWTs and keys to return decoded data or verification results, not a generic auth product, SDK, or identity service listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/decode-inspect-sign-and-verify-jwts-while-debugging-auth-flows-with-jwt-cli/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/decode-inspect-sign-and-verify-jwts-while-debugging-auth-flows-with-jwt-cli
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/decode-inspect-sign-and-verify-jwts-while-debugging-auth-flows-with-jwt-cli`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/decode-inspect-sign-and-verify-jwts-while-debugging-auth-flows-with-jwt-cli/)
