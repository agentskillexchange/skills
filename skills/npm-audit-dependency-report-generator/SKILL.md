---
title: "npm Audit Dependency Report Generator"
description: "Generates comprehensive vulnerability reports from npm audit JSON output and the OSV (Open Source Vulnerabilities) API. Parses npm audit –json results, enriches each CVE with CVSS scores from the NVD REST API, and groups findings by severity. Produces SARIF output compatible with GitHub Advanced Security."
verification: security_reviewed
source: "https://docs.npmjs.com/cli/v10/commands/npm-audit/"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Agents"
---

# npm Audit Dependency Report Generator

Generates comprehensive vulnerability reports from npm audit JSON output and the OSV (Open Source Vulnerabilities) API. Parses npm audit –json results, enriches each CVE with CVSS scores from the NVD REST API, and groups findings by severity. Produces SARIF output compatible with GitHub Advanced Security.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/npm-audit-dependency-report-generator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/npm-audit-dependency-report-generator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/npm-audit-dependency-report-generator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-audit-dependency-report-generator/)
