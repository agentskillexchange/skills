---
name: "Baseline and Review Repository Secret Findings with detect-secrets"
slug: "baseline-and-review-repository-secret-findings-with-detect-secrets"
description: "Scan a repository for secrets, keep an auditable baseline, and review only newly introduced findings during commits or CI checks."
github_stars: 4482
verification: "listed"
source: "https://github.com/Yelp/detect-secrets"
author: "Yelp"
publisher_type: "organization"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "Yelp/detect-secrets"
  github_stars: 4482
---

# Baseline and Review Repository Secret Findings with detect-secrets

Scan a repository for secrets, keep an auditable baseline, and review only newly introduced findings during commits or CI checks.

## Prerequisites

Python, detect-secrets CLI, git repository

## Installation

Use the upstream install or setup path that matches your environment:
- $ pip install detect-secrets
- $ brew install detect-secrets
- $ pip install detect-secrets[word_list]
- $ pip install detect-secrets[gibberish]

Requirements and caveats from upstream:
- python
- Specify path to custom filter. May be a python module
- is great for non-structured secrets, but may require tuning to adjust the scanning precision.

Basic usage or getting-started notes:
- Create a baseline of potential secrets currently found in your git repository.
- bash
- $ detect-secrets scan > .secrets.baseline

- Source: https://github.com/Yelp/detect-secrets
- Extracted from upstream docs: https://raw.githubusercontent.com/Yelp/detect-secrets/HEAD/README.md

## Documentation

- https://github.com/Yelp/detect-secrets

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/baseline-and-review-repository-secret-findings-with-detect-secrets/)
