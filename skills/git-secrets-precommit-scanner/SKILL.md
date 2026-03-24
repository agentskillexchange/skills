---
name: "Git Secrets Pre-Commit Scanner"
description: "Scans git diffs for exposed secrets using truffleHog entropy detection and custom regex patterns. Integrates with pre-commit hooks and GitHub push protection API for real-time blocking."
category: "Security & Verification"
framework: "OpenClaw"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/git-secrets-precommit-scanner/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "stripe"  # from ase_tool_match
  github_stars: 4377  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 8442269  # from ase_npm_downloads
  github_repo: "stripe/stripe-node"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Git Secrets Pre-Commit Scanner

Scans git diffs for exposed secrets using truffleHog entropy detection and custom regex patterns. Integrates with pre-commit hooks and GitHub push protection API for real-time blocking.

## Overview

The Git Secrets Pre-Commit Scanner prevents credential leaks by analyzing git diffs before commits are finalized. It combines truffleHog high-entropy string detection with configurable regex patterns for API keys, tokens, passwords, and private key formats across 40+ service providers including AWS, GCP, Stripe, and GitHub. The agent installs as a pre-commit hook using the pre-commit framework, scanning staged changes in real-time with sub-second performance. It supports allowlisting known safe patterns via .gitallowed files, scanning entire repository history for retroactive detection, and generating remediation scripts that rotate compromised credentials. Integration with GitHub push protection API enables server-side blocking as a secondary defense layer. The scanner handles binary file detection, large file skipping, and produces structured JSON output for security dashboard ingestion.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill git-secrets-precommit-scanner
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill git-secrets-precommit-scanner -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill git-secrets-precommit-scanner -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill git-secrets-precommit-scanner -a codex
```

### OpenClaw

```bash
clawhub install git-secrets-precommit-scanner
```

## Source

- Marketplace: https://agentskillexchange.com/skills/git-secrets-precommit-scanner/
