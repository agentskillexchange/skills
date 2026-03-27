---
name: "Heisenberg Supply Chain Health Checker"
description: "An open-source software supply chain health check tool that analyzes dependencies using deps.dev, SBOMs, and external advisories. Heisenberg generates health scores, detects risky packages, and produces CSV reports for individual dependencies or entire GitHub organization portfolios."
category: "Security & Verification"
framework: "Custom Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/heisenberg-supply-chain-health-checker/"
---

# Heisenberg Supply Chain Health Checker

An open-source software supply chain health check tool that analyzes dependencies using deps.dev, SBOMs, and external advisories. Heisenberg generates health scores, detects risky packages, and produces CSV reports for individual dependencies or entire GitHub organization portfolios.

## Overview

Heisenberg is an open-source supply chain security tool developed by AppOmni Labs that analyzes software dependencies to identify vulnerabilities and health risks. Licensed under MIT and actively maintained on GitHub, it bridges the gap between generating Software Bills of Materials (SBOMs) and actually acting on them by scoring package health and flagging risky dependencies before they reach production.

How It Works

Heisenberg operates through six CLI modes. The `check` mode inspects a single package at a specific version across npm, PyPI, or Go ecosystems, querying deps.dev for vulnerability data, maintenance signals, and dependency health. The `bulk` mode generates SBOMs for one or more GitHub repositories, then runs parallel health checks across all dependencies and writes a consolidated CSV report. The `sbom` mode generates per-repository SBOMs when you need them standalone. The `vendor` mode assesses third-party vendor SBOMs in CycloneDX, SPDX, or CSV formats. The `analyze` mode searches across your SBOMs to find whether specific compromised packages appear in any of your repositories. The `actions` mode audits GitHub Actions supply chain health, detecting unpinned actions, resolving internal shared actions to their real third-party dependencies, and reporting security advisories.

Health Scoring

Heisenberg calculates a custom health score that blends four signals: popularity (how widely used the package is), maintenance (recent commits, releases, and maintainer activity), vulnerabilities (known CVEs and advisories), and dependents (downstream impact). The scoring weights security signals more heavily than popularity, producing a practical risk ranking rather than a vanity metric. Each CSV row includes cross-reference URLs to deps.dev, Snyk, and Socket for manual investigation.

Integration Points

Heisenberg ships as a GitHub Action that automatically inspects dependency changes in pull requests before they merge. This catches supply chain risks at the PR stage rather than after deployment. The tool requires a GitHub token with repo read permissions and supports organization-wide scanning by setting the GITHUB_ORG environment variable. Installation is available via pipx or pip from the GitHub repository, requiring Python 3.11 or later. For incident response scenarios, the analyze mode accepts comma-separated package lists or text files, enabling rapid triage when a new supply chain compromise is disclosed.

Output and Reports

Heisenberg produces structured CSV reports suitable for import into spreadsheets, dashboards, or security information systems. Reports include package name, version, ecosystem, health score, vulnerability count, maintenance status, and direct links to advisory databases. The bulk mode processes multiple repositories in parallel for efficient organization-wide assessments.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill heisenberg-supply-chain-health-checker
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill heisenberg-supply-chain-health-checker -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill heisenberg-supply-chain-health-checker -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill heisenberg-supply-chain-health-checker -a codex
```

### OpenClaw

```bash
clawhub install heisenberg-supply-chain-health-checker
```

## Source

- Marketplace: https://agentskillexchange.com/skills/heisenberg-supply-chain-health-checker/
