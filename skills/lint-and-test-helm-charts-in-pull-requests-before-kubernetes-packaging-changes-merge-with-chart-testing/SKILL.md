---
title: "Lint and test Helm charts in pull requests before Kubernetes packaging changes merge with chart-testing"
description: "Run chart-focused lint and install checks so changed Helm charts are validated before release or merge."
verification: listed
source: "https://github.com/helm/chart-testing"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "helm/chart-testing"
  github_stars: 1627
---

# Lint and test Helm charts in pull requests before Kubernetes packaging changes merge with chart-testing

Use chart-testing when an agent needs to identify changed Helm charts, lint them, and optionally install-test them as part of CI or release review. A user should invoke this instead of using Helm normally when the task is chart QA and changed-chart gating, not chart authoring or cluster management itself. The scope boundary is specific and skill-shaped: it is a Helm chart validation workflow for CI, not a generic Kubernetes tool or packaging platform listing.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/lint-and-test-helm-charts-in-pull-requests-before-kubernetes-packaging-changes-merge-with-chart-testing
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/lint-and-test-helm-charts-in-pull-requests-before-kubernetes-packaging-changes-merge-with-chart-testing` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-and-test-helm-charts-in-pull-requests-before-kubernetes-packaging-changes-merge-with-chart-testing/)
