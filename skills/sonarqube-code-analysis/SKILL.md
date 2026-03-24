---
name: "SonarQube Code Analysis"
description: "Use this skill when you need to trigger a SonarQube scan, retrieve quality gate results, or inspect code smell and vulnerability reports for a project. It interfaces with SonarQube’s Web API to surface technical debt, security hotspots, and coverage metrics in AI-readable form."
category: "Developer Tools"
framework: "Claude Code"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/sonarqube-code-analysis/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "sonarqube"  # from ase_tool_match
  github_stars: 10357  # from ase_github_stars (integer, not string)
  github_repo: "SonarSource/sonarqube"  # from ase_github_repo
  license: "LGPL-3.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# SonarQube Code Analysis

Use this skill when you need to trigger a SonarQube scan, retrieve quality gate results, or inspect code smell and vulnerability reports for a project. It interfaces with SonarQube’s Web API to surface technical debt, security hotspots, and coverage metrics in AI-readable form.

## Overview

Use this skill when you need to trigger a SonarQube scan, retrieve quality gate results, or inspect code smell and vulnerability reports for a project. It interfaces with SonarQube’s Web API to surface technical debt, security hotspots, and coverage metrics in AI-readable form.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill sonarqube-code-analysis
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill sonarqube-code-analysis -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill sonarqube-code-analysis -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill sonarqube-code-analysis -a codex
```

### OpenClaw

```bash
clawhub install sonarqube-code-analysis
```

## Source

- Marketplace: https://agentskillexchange.com/skills/sonarqube-code-analysis/
