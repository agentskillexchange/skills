---
title: "Lint and test Helm charts in pull requests before Kubernetes packaging changes merge with chart-testing"
description: "Run chart-focused lint and install checks so changed Helm charts are validated before release or merge."
verification: "listed"
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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-and-test-helm-charts-in-pull-requests-before-kubernetes-packaging-changes-merge-with-chart-testing/)
