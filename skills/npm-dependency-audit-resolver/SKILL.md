---
name: "npm Dependency Audit Resolver"
description: "Resolves npm audit vulnerabilities by analyzing the npm registry API for patched versions, generating targeted package.json overrides, and testing upgrades via npm-check-updates compatibility mode."
category: "Security & Verification"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/npm-dependency-audit-resolver/"
---
# npm Dependency Audit Resolver

Resolves npm audit vulnerabilities by analyzing the npm registry API for patched versions, generating targeted package.json overrides, and testing upgrades via npm-check-updates compatibility mode.

## Overview

The npm Dependency Audit Resolver automates the remediation of npm audit findings by querying the npm registry API for available patches and compatible version ranges. It parses npm audit –json output to build a vulnerability dependency tree, distinguishing between direct and transitive vulnerabilities, and generates targeted fix strategies including version bumps, overrides in package.json, and selective npm-force-resolutions for deeply nested dependencies. The agent uses npm-check-updates in doctor mode to test upgrade compatibility by running the project test suite against each proposed change. It handles peer dependency conflicts through semver range analysis, supports both npm and yarn lockfile formats, and generates detailed changelogs for each upgraded package by fetching release notes from GitHub. Integration with Socket.dev API adds supply chain risk scoring, detecting typosquatting and malicious package indicators. Produces CI-ready PR descriptions with vulnerability severity summaries and breaking change warnings.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill npm-dependency-audit-resolver
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill npm-dependency-audit-resolver -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill npm-dependency-audit-resolver -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill npm-dependency-audit-resolver -a codex
```

### OpenClaw

```bash
clawhub install npm-dependency-audit-resolver
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-dependency-audit-resolver/)
