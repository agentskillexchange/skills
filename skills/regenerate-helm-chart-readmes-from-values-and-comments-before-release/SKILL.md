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

This entry is built around helm-docs, the open source tool in the norwoodj/helm-docs repository that generates markdown documentation from Helm charts. In an agent workflow, the job-to-be-done is very specific: inspect a chart, read its metadata and values, parse inline description comments, regenerate the README or another template-driven markdown file, and return a diff that shows whether chart documentation still matches the shipping configuration surface. That makes the agent useful in repositories where chart values evolve quickly and stale docs create deployment mistakes for other operators.

You should invoke this skill when an agent edits values.yaml, changes Chart.yaml, reviews a Helm chart pull request, or prepares a release that should include refreshed operator-facing documentation. It is also a good fit for pre-commit hooks and CI jobs that fail when generated README content is out of date. The agent can call helm-docs, inspect the generated markdown, point out undocumented values, and decide whether the result is ready to commit or needs human clarification on missing comments.

The scope boundary is clear. This is not a generic Helm deployment workflow, cluster operator, or packaging system. It does not install charts, render templates for runtime, or manage releases. Its lane is documentation generation and documentation drift detection for Helm charts. Integration points include pre-commit, CI pipelines, docs review bots, release automation, and agent loops that update chart values, regenerate docs, and stage both code and documentation changes together.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/regenerate-helm-chart-readmes-from-values-and-comments-before-release
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/regenerate-helm-chart-readmes-from-values-and-comments-before-release` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/regenerate-helm-chart-readmes-from-values-and-comments-before-release/)
