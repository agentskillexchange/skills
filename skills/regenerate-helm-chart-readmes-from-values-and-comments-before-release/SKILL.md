---
title: "Regenerate Helm chart READMEs from values and comments before release"
slug: "regenerate-helm-chart-readmes-from-values-and-comments-before-release"
verification: "listed"
category:
  - "Templates &amp; Workflows"
framework:
  - "Multi-Framework"
source: "https://github.com/norwoodj/helm-docs"
---

# Regenerate Helm chart READMEs from values and comments before release

Uses helm-docs to rebuild Helm chart documentation from Chart.yaml, values.yaml, and inline comments so README files stay aligned with the actual chart. The agent can run this before commit or release, then surface changed tables, missing descriptions, and documentation drift in a review-friendly diff.

## Installation

Choose the method that fits your setup:

1. Clone or download this repo and copy the skill folder into your local skills directory.
2. Install from the Agent Skill Exchange repo with your preferred Git workflow.
3. Add the skill folder as a git submodule if you manage skills as dependencies.
4. Copy the files manually into a local custom-skills directory for testing.
5. Use any marketplace or sync tooling you already have for pulling ASE skills.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/regenerate-helm-chart-readmes-from-values-and-comments-before-release/)
