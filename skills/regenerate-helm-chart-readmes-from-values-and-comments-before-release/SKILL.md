---
name: "regenerate-helm-chart-readmes-from-values-and-comments-before-release"
title: "Regenerate Helm chart READMEs from values and comments before release"
description: "Uses helm-docs to rebuild Helm chart documentation from Chart.yaml, values.yaml, and inline comments so README files stay aligned with the actual chart. The agent can run this before commit or release, then surface changed tables, missing descriptions, and documentation drift in a review-friendly diff."
category: "Templates &amp; Workflows"
framework: "Multi-Framework"
verification: "listed"
source: "https://github.com/norwoodj/helm-docs"
tool_ecosystem:
  github_repo: "norwoodj/helm-docs"
  github_stars: 1732
---

# Regenerate Helm chart READMEs from values and comments before release

Uses helm-docs to rebuild Helm chart documentation from Chart.yaml, values.yaml, and inline comments so README files stay aligned with the actual chart. The agent can run this before commit or release, then surface changed tables, missing descriptions, and documentation drift in a review-friendly diff.

## Installation

You can install this skill using any of these methods:

1. OpenClaw skill installer
2. ClawHub CLI
3. Git clone into your skills directory
4. Download and extract the skill folder manually
5. Copy the skill folder from a local checkout

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/regenerate-helm-chart-readmes-from-values-and-comments-before-release/)
