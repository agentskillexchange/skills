---
name: "SonarQube Code Scanner Agent"
description: "Automated code quality scanning using SonarQube REST API and SonarScanner CLI. Detects code smells, bugs, and vulnerabilities across 30+ languages with configurable quality gates."
category: "Code Quality & Review"
framework: "OpenClaw"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/sonarqube-code-scanner-agent/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "sonarqube"  # from ase_tool_match
  github_stars: 10357  # from ase_github_stars (integer, not string)
  github_repo: "SonarSource/sonarqube"  # from ase_github_repo
  license: "LGPL-3.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# SonarQube Code Scanner Agent

Automated code quality scanning using SonarQube REST API and SonarScanner CLI. Detects code smells, bugs, and vulnerabilities across 30+ languages with configurable quality gates.

## Overview

The SonarQube Code Scanner Agent integrates directly with SonarQube Server REST API (api/qualitygates, api/issues, api/measures) and SonarScanner CLI to perform comprehensive static code analysis. It supports Java, Python, JavaScript, TypeScript, C#, Go, and 25+ additional languages out of the box.

The agent triggers scans via sonar-scanner with configurable sonar-project.properties, monitors analysis progress through the ce/task endpoint, and retrieves detailed results including code smells, bugs, security vulnerabilities, and technical debt metrics. Quality gate status is checked via api/qualitygates/project_status.

Key capabilities include pull request decoration with inline comments on new issues, branch analysis comparison, and trend tracking across multiple project versions. The agent can enforce custom quality profiles and block merges when quality gates fail.

Integration with CI/CD pipelines is supported through webhook listeners that process analysis completion events and route results to Slack, Teams, or email notifications.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill sonarqube-code-scanner-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill sonarqube-code-scanner-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill sonarqube-code-scanner-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill sonarqube-code-scanner-agent -a codex
```

### OpenClaw

```bash
clawhub install sonarqube-code-scanner-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/sonarqube-code-scanner-agent/
