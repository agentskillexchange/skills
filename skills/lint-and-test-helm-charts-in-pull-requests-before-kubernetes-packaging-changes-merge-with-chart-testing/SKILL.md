---
title: "Lint and test Helm charts in pull requests before Kubernetes packaging changes merge with chart-testing"
slug: "lint-and-test-helm-charts-in-pull-requests-before-kubernetes-packaging-changes-merge-with-chart-testing"
description: "Run chart-focused lint and install checks so changed Helm charts are validated before release or merge."
github_stars: 1627
verification: "security_reviewed"
source: "https://github.com/helm/chart-testing"
author: "Helm"
publisher_type: "organization"
category: "CI/CD Integrations"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "helm/chart-testing"
  github_stars: 1627
---

# Lint and test Helm charts in pull requests before Kubernetes packaging changes merge with chart-testing

Run chart-focused lint and install checks so changed Helm charts are validated before release or merge.

## Prerequisites

ct binary or Docker image, Helm, Git, Kubernetes test environment for install checks

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install `ct` from Homebrew, releases, or the published Docker image, then run commands like `ct lint`, `ct install`, or `ct lint-and-install` against changed chart directories in CI.
```

## Documentation

- https://github.com/helm/chart-testing

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-and-test-helm-charts-in-pull-requests-before-kubernetes-packaging-changes-merge-with-chart-testing/)
