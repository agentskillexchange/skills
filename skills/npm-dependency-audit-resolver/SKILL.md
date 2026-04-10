---
name: npm Dependency Audit Resolver
description: Resolves npm audit vulnerabilities by analyzing the npm registry API
  for patched versions, generating targeted package.json overrides, and testing upgrades
  via npm-check-updates compatibility mode.
verification: security_reviewed
source: https://agentskillexchange.com/skills/npm-dependency-audit-resolver/
category:
- Security &amp; Verification
framework:
- Claude Code
---
# npm Dependency Audit Resolver

The npm Dependency Audit Resolver automates the remediation of npm audit findings by querying the npm registry API for available patches and compatible version ranges. It parses npm audit -json output to build a vulnerability dependency tree, distinguishing between direct and transitive vulnerabilities, and generates targeted fix strategies including version bumps, overrides in package.json, and selective npm-force-resolutions for deeply nested dependencies. The agent uses npm-check-updates in doctor mode to test upgrade compatibility by running the project test suite against each proposed change. It handles peer dependency conflicts through semver range analysis, supports both npm and yarn lockfile formats, and generates detailed changelogs for each upgraded package by fetching release notes from GitHub. Integration with Socket.dev API adds supply chain risk scoring, detecting typosquatting and malicious package indicators. Produces CI-ready PR descriptions with vulnerability severity summaries and breaking change warnings.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-dependency-audit-resolver/)
