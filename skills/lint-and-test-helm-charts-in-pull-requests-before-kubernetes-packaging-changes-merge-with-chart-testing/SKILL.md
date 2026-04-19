---
title: "Lint and test Helm charts in pull requests before Kubernetes packaging changes merge with chart-testing"
description: "Use chart-testing when an agent needs to identify changed Helm charts, lint them, and optionally install-test them as part of CI or release review. A user should invoke this instead of using Helm normally when the task is chart QA and changed-chart gating, not chart authoring or cluster management itself. The scope boundary is specific and skill-shaped: it is a Helm chart validation workflow for CI, not a generic Kubernetes tool or packaging platform listing."
source: "https://github.com/helm/chart-testing"
verification: "listed"
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

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-and-test-helm-charts-in-pull-requests-before-kubernetes-packaging-changes-merge-with-chart-testing/)
