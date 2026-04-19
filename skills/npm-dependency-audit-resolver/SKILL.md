---
title: "npm Dependency Audit Resolver"
description: "The npm Dependency Audit Resolver automates the remediation of npm audit findings by querying the npm registry API for available patches and compatible version ranges. It parses npm audit &#8211;json output to build a vulnerability dependency tree, distinguishing between direct and transitive vulnerabilities, and generates targeted fix strategies including version bumps, overrides in package.json, and selective npm-force-resolutions for deeply nested dependencies. The agent uses npm-check-updates in doctor mode to test upgrade compatibility by running the project test suite against each proposed change. It handles peer dependency conflicts through semver range analysis, supports both npm and yarn lockfile formats, and generates detailed changelogs for each upgraded package by fetching release notes from GitHub. Integration with Socket.dev API adds supply chain risk scoring, detecting typosquatting and malicious package indicators. Produces CI-ready PR descriptions with vulnerability severity summaries and breaking change warnings."
source: "https://agentskillexchange.com/skills/npm-dependency-audit-resolver/"
verification: "security_reviewed"
category:
  - "Security &amp; Verification"
framework:
  - "Claude Code"
---

# npm Dependency Audit Resolver

The npm Dependency Audit Resolver automates the remediation of npm audit findings by querying the npm registry API for available patches and compatible version ranges. It parses npm audit &#8211;json output to build a vulnerability dependency tree, distinguishing between direct and transitive vulnerabilities, and generates targeted fix strategies including version bumps, overrides in package.json, and selective npm-force-resolutions for deeply nested dependencies. The agent uses npm-check-updates in doctor mode to test upgrade compatibility by running the project test suite against each proposed change. It handles peer dependency conflicts through semver range analysis, supports both npm and yarn lockfile formats, and generates detailed changelogs for each upgraded package by fetching release notes from GitHub. Integration with Socket.dev API adds supply chain risk scoring, detecting typosquatting and malicious package indicators. Produces CI-ready PR descriptions with vulnerability severity summaries and breaking change warnings.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-dependency-audit-resolver/)
