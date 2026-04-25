---
title: "Baseline and Review Repository Secret Findings with detect-secrets"
description: "Scan a repository for secrets, keep an auditable baseline, and review only newly introduced findings during commits or CI checks."
verification: "security_reviewed"
source: "https://github.com/Yelp/detect-secrets"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "Yelp/detect-secrets"
  github_stars: 4482
---

# Baseline and Review Repository Secret Findings with detect-secrets

This skill wraps detect-secrets as a repeatable secret-review workflow rather than a generic scanner listing. The agent generates or refreshes a baseline, scans the repository, and focuses review attention on newly introduced findings so teams can gate commits and CI runs without re-triaging known historical noise every time. Invoke it when a repository needs an incremental secret-hygiene check before merge, during pre-commit enforcement, or while cleaning up a legacy codebase in stages. Use the product normally for ad hoc scanning only. Use this skill when the job is specifically baseline management plus review of net-new findings. The scope boundary is narrow and explicit: repository secret detection, baseline upkeep, and review of new alerts. It is not a general AppSec platform, SIEM, or full security program card.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/baseline-and-review-repository-secret-findings-with-detect-secrets/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/baseline-and-review-repository-secret-findings-with-detect-secrets
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/baseline-and-review-repository-secret-findings-with-detect-secrets`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/baseline-and-review-repository-secret-findings-with-detect-secrets/)
