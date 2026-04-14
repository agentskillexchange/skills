---
title: "Regenerate Helm chart READMEs from values and comments before release"
slug: "regenerate-helm-chart-readmes-from-values-and-comments-before-release"
verification: security_reviewed
source: "https://github.com/norwoodj/helm-docs"
category:
  - "Templates &amp; Workflows"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "norwoodj/helm-docs"
  github_stars: 1732
---
# Regenerate Helm chart READMEs from values and comments before release

Uses helm-docs to rebuild Helm chart documentation from Chart.yaml, values.yaml, and inline comments so README files stay aligned with the actual chart. The agent can run this before commit or release, then surface changed tables, missing descriptions, and documentation drift in a review-friendly diff.

## Installation

Choose the method that fits your setup:

1. Install from Agent Skill Exchange
2. Clone or download the upstream project
3. Install with the upstream package manager
4. Add the skill to your local skills directory
5. Follow the upstream documentation for environment-specific setup

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/regenerate-helm-chart-readmes-from-values-and-comments-before-release/)
