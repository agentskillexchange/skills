---
title: "Baseline and Review Repository Secret Findings with detect-secrets"
description: "This skill wraps detect-secrets as a repeatable secret-review workflow rather than a generic scanner listing. The agent generates or refreshes a baseline, scans the repository, and focuses review attention on newly introduced findings so teams can gate commits and CI runs without re-triaging known historical noise every time. Invoke it when a repository needs an incremental secret-hygiene check before merge, during pre-commit enforcement, or while cleaning up a legacy codebase in stages. Use the product normally for ad hoc scanning only. Use this skill when the job is specifically baseline management plus review of net-new findings. The scope boundary is narrow and explicit: repository secret detection, baseline upkeep, and review of new alerts. It is not a general AppSec platform, SIEM, or full security program card."
source: "https://github.com/Yelp/detect-secrets"
verification: "listed"
category:
  - "Security &amp; Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "Yelp/detect-secrets"
  github_stars: 4482
---

# Baseline and Review Repository Secret Findings with detect-secrets

This skill wraps detect-secrets as a repeatable secret-review workflow rather than a generic scanner listing. The agent generates or refreshes a baseline, scans the repository, and focuses review attention on newly introduced findings so teams can gate commits and CI runs without re-triaging known historical noise every time. Invoke it when a repository needs an incremental secret-hygiene check before merge, during pre-commit enforcement, or while cleaning up a legacy codebase in stages. Use the product normally for ad hoc scanning only. Use this skill when the job is specifically baseline management plus review of net-new findings. The scope boundary is narrow and explicit: repository secret detection, baseline upkeep, and review of new alerts. It is not a general AppSec platform, SIEM, or full security program card.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/baseline-and-review-repository-secret-findings-with-detect-secrets/)
