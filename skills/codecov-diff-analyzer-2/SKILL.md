---
name: "Codecov Diff Analyzer"
description: "Uses the Codecov API v2 to analyze coverage diffs on pull requests. Surfaces uncovered lines in changed files and compares against Codecov YAML threshold configurations."
category: "Templates & Workflows"
framework: "Codex"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/codecov-diff-analyzer-2/"
---

# Codecov Diff Analyzer

Uses the Codecov API v2 to analyze coverage diffs on pull requests. Surfaces uncovered lines in changed files and compares against Codecov YAML threshold configurations.

## Overview

The Codecov Diff Analyzer skill connects to Codecov REST API to provide detailed coverage analysis for pull request changes. It fetches commit-level coverage data and cross-references with the pull request diff to identify newly introduced uncovered lines. The skill parses codecov.yml configuration files to understand project-specific thresholds for patch coverage, project coverage, and flag-based coverage targets. It supports Codecov Flags for monorepo configurations, analyzes coverage trends across the last N commits, and can detect coverage regressions in critical paths. Output includes a per-file breakdown of covered vs uncovered changed lines, comparison against the target branch baseline, and recommendations for test additions. Integrates with lcov, cobertura, and clover report formats for maximum compatibility.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill codecov-diff-analyzer-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill codecov-diff-analyzer-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill codecov-diff-analyzer-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill codecov-diff-analyzer-2 -a codex
```

### OpenClaw

```bash
clawhub install codecov-diff-analyzer-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/codecov-diff-analyzer-2/
