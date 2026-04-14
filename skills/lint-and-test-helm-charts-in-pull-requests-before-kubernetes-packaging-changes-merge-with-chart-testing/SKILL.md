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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-and-test-helm-charts-in-pull-requests-before-kubernetes-packaging-changes-merge-with-chart-testing/)
