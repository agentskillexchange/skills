---
name: "SonarQube Gate Checker"
description: "Queries the SonarQube Web API (/api/qualitygates/project_status) to evaluate quality gate conditions before merge. Reports code smells, coverage thresholds, and duplications against configurable SonarQube quality profiles."
category: "Templates & Workflows"
framework: "Claude Code"
verification: listed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/sonarqube-gate-checker-2/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "sonarqube"  # from ase_tool_match
  github_stars: 10358  # from ase_github_stars (integer, not string)
  github_repo: "SonarSource/sonarqube"  # from ase_github_repo
  license: "LGPL-3.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# SonarQube Gate Checker

Queries the SonarQube Web API (/api/qualitygates/project_status) to evaluate quality gate conditions before merge. Reports code smells, coverage thresholds, and duplications against configurable SonarQube quality profiles.

## Overview

**SonarQube Gate Checker** is built around SonarQube code quality platform. The underlying ecosystem is represented by `SonarSource/sonarqube` (10,357+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like quality gates, issues API, measures, coverage, hotspots, branches and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to sonarqube so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Queries the SonarQube Web API (/api/qualitygates/project_status) to evaluate quality gate conditions before merge. Reports code smells, coverage thresholds, and duplications against configurable SonarQube quality profiles. The implementation typically relies on quality gates, issues API, measures, coverage, hotspots, branches, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses quality gates, issues API, measures, coverage, hotspots, branches instead of scraping a UI, which makes runs easier to audit and retry.

Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

Fits into broader integration points such as code health reporting, merge gating, and technical debt analysis.

As a runbook-style skill, the value is not just tool access but operational sequencing: check the right signals first, reduce alert noise, and produce a summary that another engineer can act on immediately. In security-oriented usage, the skill emphasizes read-only discovery, evidence capture, and machine-readable output such as SARIF, JSON, or structured findings so results can flow into existing review pipelines. Key integration points include code health reporting, merge gating, and technical debt analysis. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

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
