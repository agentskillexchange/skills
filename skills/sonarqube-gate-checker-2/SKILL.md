---
name: "SonarQube Gate Checker"
description: "Queries the SonarQube Web API (/api/qualitygates/project_status) to evaluate quality gate conditions before merge. Reports code smells, coverage thresholds, and duplications against configurable SonarQube quality profiles."
category: "Templates & Workflows"
framework: "Codex"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/sonarqube-gate-checker-2/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "sonarqube"  # from ase_tool_match
  github_stars: 10357  # from ase_github_stars (integer, not string)
  github_repo: "SonarSource/sonarqube"  # from ase_github_repo
  license: "LGPL-3.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# SonarQube Gate Checker

Queries the SonarQube Web API (/api/qualitygates/project_status) to evaluate quality gate conditions before merge. Reports code smells, coverage thresholds, and duplications against configurable SonarQube quality profiles.

## Overview

The SonarQube Gate Checker skill integrates directly with SonarQube Server or SonarCloud to evaluate quality gate status for a given project. It authenticates via user token or project analysis token against the /api/qualitygates/project_status endpoint and retrieves conditions including code coverage percentage, duplicated lines density, reliability rating, security hotspot review status, and maintainability metrics. The skill compares current analysis results against the configured quality profile thresholds and produces a pass/fail summary with specific metric breakdowns. It supports both branch analysis and pull request decoration modes, can query historical trend data via /api/measures/search_history, and formats output suitable for CI pipeline decision points. When gates fail, it provides actionable remediation guidance pointing to the specific files and rules triggering failures.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill sonarqube-gate-checker-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill sonarqube-gate-checker-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill sonarqube-gate-checker-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill sonarqube-gate-checker-2 -a codex
```

### OpenClaw

```bash
clawhub install sonarqube-gate-checker-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/sonarqube-gate-checker-2/
