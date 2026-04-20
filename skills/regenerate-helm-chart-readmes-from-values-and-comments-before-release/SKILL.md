---
title: "Regenerate Helm chart READMEs from values and comments before release"
description: "Uses helm-docs to rebuild Helm chart documentation from Chart.yaml, values.yaml, and inline comments so README files stay aligned with the actual chart. The agent can run this before commit or release, then surface changed tables, missing descriptions, and documentation drift in a review-friendly diff."
verification: security_reviewed
source: "https://github.com/norwoodj/helm-docs"
category:
  - "Templates & Workflows"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "norwoodj/helm-docs"
  github_stars: 1732
---

# Regenerate Helm chart READMEs from values and comments before release

Uses helm-docs to rebuild Helm chart documentation from Chart.yaml, values.yaml, and inline comments so README files stay aligned with the actual chart. The agent can run this before commit or release, then surface changed tables, missing descriptions, and documentation drift in a review-friendly diff.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/regenerate-helm-chart-readmes-from-values-and-comments-before-release/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/regenerate-helm-chart-readmes-from-values-and-comments-before-release
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/regenerate-helm-chart-readmes-from-values-and-comments-before-release`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/regenerate-helm-chart-readmes-from-values-and-comments-before-release/)
