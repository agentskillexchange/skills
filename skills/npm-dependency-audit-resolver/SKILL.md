---
title: "npm Dependency Audit Resolver"
description: "Resolves npm audit vulnerabilities by analyzing the npm registry API for patched versions, generating targeted package.json overrides, and testing upgrades via npm-check-updates compatibility mode."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/npm-dependency-audit-resolver/"
category:
  - "Security & Verification"
framework:
  - "Claude Code"
---

# npm Dependency Audit Resolver

The npm Dependency Audit Resolver automates the remediation of npm audit findings by querying the npm registry API for available patches and compatible version ranges. It parses npm audit –json output to build a vulnerability dependency tree, distinguishing between direct and transitive vulnerabilities, and generates targeted fix strategies including version bumps, overrides in package.json, and selective npm-force-resolutions for deeply nested dependencies. The agent uses npm-check-updates in doctor mode to test upgrade compatibility by running the project test suite against each proposed change. It handles peer dependency conflicts through semver range analysis, supports both npm and yarn lockfile formats, and generates detailed changelogs for each upgraded package by fetching release notes from GitHub. Integration with Socket.dev API adds supply chain risk scoring, detecting typosquatting and malicious package indicators. Produces CI-ready PR descriptions with vulnerability severity summaries and breaking change warnings.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/npm-dependency-audit-resolver
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/npm-dependency-audit-resolver` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-dependency-audit-resolver/)
