---
title: "Run declarative Kubernetes test suites against clusters before operator or manifest changes merge with KUTTL"
description: "Use KUTTL when an agent needs to run declarative Kubernetes tests made of setup, apply, wait, and assert steps against a cluster. A user should invoke this instead of using kubectl or Helm normally when the task is repeatable cluster-level verification of operators, controllers, or manifest behavior before merge or release. The scope boundary is clear: YAML-defined Kubernetes test execution and assertions, not a generic cluster management tool listing."
source: "https://github.com/kudobuilder/kuttl"
verification: "listed"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "kudobuilder/kuttl"
  github_stars: 804
---

# Run declarative Kubernetes test suites against clusters before operator or manifest changes merge with KUTTL

Use KUTTL when an agent needs to run declarative Kubernetes tests made of setup, apply, wait, and assert steps against a cluster. A user should invoke this instead of using kubectl or Helm normally when the task is repeatable cluster-level verification of operators, controllers, or manifest behavior before merge or release. The scope boundary is clear: YAML-defined Kubernetes test execution and assertions, not a generic cluster management tool listing.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-declarative-kubernetes-test-suites-against-clusters-before-operator-or-manifest-changes-merge-with-kuttl/)
