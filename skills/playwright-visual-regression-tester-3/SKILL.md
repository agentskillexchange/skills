---
name: "Playwright Visual Regression Tester"
description: "Automates visual regression testing using the Playwright screenshot comparison API and pixelmatch diffing library. Captures baseline snapshots, detects pixel-level UI changes across viewport sizes, and generates HTML diff reports with threshold-based pass/fail results."
category: "Browser Automation"
framework: "OpenClaw"
verification: verified_metadata  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/playwright-visual-regression-tester-3/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "playwright"  # from ase_tool_match
  github_stars: 84874  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 39806814  # from ase_npm_downloads
  github_repo: "microsoft/playwright"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Playwright Visual Regression Tester

Automates visual regression testing using the Playwright screenshot comparison API and pixelmatch diffing library. Captures baseline snapshots, detects pixel-level UI changes across viewport sizes, and generates HTML diff reports with threshold-based pass/fail results.

## Overview

Automates visual regression testing using the Playwright screenshot comparison API and pixelmatch diffing library. Captures baseline snapshots, detects pixel-level UI changes across viewport sizes, and generates HTML diff reports with threshold-based pass/fail results.

This skill integrates with production-grade tooling to streamline automation workflows. It handles edge cases such as timeout management, retry logic with exponential backoff, and detailed error reporting. Configuration is managed through environment variables and YAML config files, supporting both local development and CI/CD pipeline environments. The skill outputs structured JSON logs compatible with ELK stack and Datadog for observability. It includes built-in rate limiting to respect API quotas and implements proper credential rotation using vault-based secret management.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill playwright-visual-regression-tester-3
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill playwright-visual-regression-tester-3 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill playwright-visual-regression-tester-3 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill playwright-visual-regression-tester-3 -a codex
```

### OpenClaw

```bash
clawhub install playwright-visual-regression-tester-3
```

## Source

- Marketplace: https://agentskillexchange.com/skills/playwright-visual-regression-tester-3/
