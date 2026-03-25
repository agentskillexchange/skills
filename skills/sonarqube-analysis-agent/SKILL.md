---
name: "SonarQube Analysis Agent"
description: "Integrates with the SonarQube REST API to run static code analysis scans, retrieve quality gate results, and flag code smells. Supports SonarCloud and on-premise SonarQube instances via token-based authentication."
category: "Code Quality & Review"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/sonarqube-analysis-agent/"
tool_ecosystem:
  tool: "sonarqube"
  github_stars: 10358
  github_repo: "SonarSource/sonarqube"
  license: "LGPL-3.0"
  maintained: true
---

# SonarQube Analysis Agent

Integrates with the SonarQube REST API to run static code analysis scans, retrieve quality gate results, and flag code smells. Supports SonarCloud and on-premise SonarQube instances via token-based authentication.

## Overview

The SonarQube Analysis Agent connects to your SonarQube or SonarCloud instance via the official REST API (api/qualitygates, api/issues, api/measures) to automate static code analysis workflows. It authenticates using project-scoped tokens and retrieves detailed quality gate status, code smell counts, vulnerability reports, and technical debt estimates.

Designed for CI/CD pipelines, the agent can be triggered after each commit or pull request to run incremental analysis. It parses the SonarQube webhook payload to determine pass/fail status and surfaces actionable findings directly in your development workflow. Supports multi-language projects including Java, Python, JavaScript, TypeScript, Go, and C#.

The agent also tracks quality trends over time by querying the measures API for metrics like cyclomatic complexity, duplicated lines percentage, and coverage ratios. Results can be formatted as markdown reports or posted as PR comments via the GitHub Checks API integration.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill sonarqube-analysis-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill sonarqube-analysis-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill sonarqube-analysis-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill sonarqube-analysis-agent -a codex
```

### OpenClaw

```bash
clawhub install sonarqube-analysis-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/sonarqube-analysis-agent/
