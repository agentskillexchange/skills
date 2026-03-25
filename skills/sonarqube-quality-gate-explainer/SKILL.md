---
name: "SonarQube Quality Gate Explainer"
description: "Fetches the latest SonarQube project analysis result, explains why the Quality Gate failed in plain English, and links to specific issues. Covers coverage drops, new bugs, and security hotspots. Supports SonarQube Server and SonarCloud. Diagnostic only."
category: "Code Quality & Review"
framework: "Claude Code"
verification: listed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/sonarqube-quality-gate-explainer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "sonarqube"  # from ase_tool_match
  github_stars: 10357  # from ase_github_stars (integer, not string)
  github_repo: "SonarSource/sonarqube"  # from ase_github_repo
  license: "LGPL-3.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# SonarQube Quality Gate Explainer

Fetches the latest SonarQube project analysis result, explains why the Quality Gate failed in plain English, and links to specific issues. Covers coverage drops, new bugs, and security hotspots. Supports SonarQube Server and SonarCloud. Diagnostic only.

## Overview

Fetches the latest SonarQube project analysis result, explains why the Quality Gate failed in plain English, and links to specific issues. Covers coverage drops, new bugs, and security hotspots. Supports SonarQube Server and SonarCloud. Diagnostic only.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill sonarqube-quality-gate-explainer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill sonarqube-quality-gate-explainer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill sonarqube-quality-gate-explainer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill sonarqube-quality-gate-explainer -a codex
```

### OpenClaw

```bash
clawhub install sonarqube-quality-gate-explainer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/sonarqube-quality-gate-explainer/
