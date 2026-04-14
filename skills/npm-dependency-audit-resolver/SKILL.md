---
title: "npm Dependency Audit Resolver"
description: "Resolves npm audit vulnerabilities by analyzing the npm registry API for patched versions, generating targeted package.json overrides, and testing upgrades via npm-check-updates compatibility mode."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/npm-dependency-audit-resolver/"
category:
  - "Security &amp; Verification"
framework:
  - "Claude Code"
---

# npm Dependency Audit Resolver

The npm Dependency Audit Resolver automates the remediation of npm audit findings by querying the npm registry API for available patches and compatible version ranges. It parses npm audit –json output to build a vulnerability dependency tree, distinguishing between direct and transitive vulnerabilities, and generates targeted fix strategies including version bumps, overrides in package.json, and selective npm-force-resolutions for deeply nested dependencies. The agent uses npm-check-updates in doctor mode to test upgrade compatibility by running the project test suite against each proposed change. It handles peer dependency conflicts through semver range analysis, supports both npm and yarn lockfile formats, and generates detailed changelogs for each upgraded package by fetching release notes from GitHub. Integration with Socket.dev API adds supply chain risk scoring, detecting typosquatting and malicious package indicators. Produces CI-ready PR descriptions with vulnerability severity summaries and breaking change warnings.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-dependency-audit-resolver/)
