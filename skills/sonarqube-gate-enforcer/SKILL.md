---
name: "SonarQube Gate Enforcer"
description: "Enforces SonarQube quality gate conditions in CI pipelines using the SonarQube Web API /api/qualitygates/project_status endpoint. Blocks merges when coverage drops, duplications exceed thresholds, or new bugs are introduced."
category: "Code Quality & Review"
framework: "Cursor"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/sonarqube-gate-enforcer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "sonarqube"  # from ase_tool_match
  github_stars: 10357  # from ase_github_stars (integer, not string)
  github_repo: "SonarSource/sonarqube"  # from ase_github_repo
  license: "LGPL-3.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# SonarQube Gate Enforcer

Enforces SonarQube quality gate conditions in CI pipelines using the SonarQube Web API /api/qualitygates/project_status endpoint. Blocks merges when coverage drops, duplications exceed thresholds, or new bugs are introduced.

## Overview

The SonarQube Gate Enforcer skill integrates SonarQube quality gate checks directly into CI/CD pipelines via the SonarQube Web API. It polls the /api/qualitygates/project_status endpoint after analysis completion to retrieve gate conditions and their pass/fail status. The skill supports custom quality gate profiles with configurable thresholds for code coverage percentage, duplication density, maintainability rating, reliability rating, and security hotspot review percentage. When a gate fails, it generates detailed failure reports showing exactly which conditions were violated, the delta from the threshold, and specific files contributing to the failure via the /api/issues/search endpoint. The tool integrates with GitHub, GitLab, and Bitbucket APIs to post quality gate status as commit checks and PR comments. It supports branch analysis for feature branches and pull request decoration with inline code annotations from SonarQube findings.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill sonarqube-gate-enforcer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill sonarqube-gate-enforcer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill sonarqube-gate-enforcer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill sonarqube-gate-enforcer -a codex
```

### OpenClaw

```bash
clawhub install sonarqube-gate-enforcer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/sonarqube-gate-enforcer/
