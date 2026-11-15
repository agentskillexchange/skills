---
name: "Pulumi Drift Detector & Reconciler"
slug: "pulumi-drift-detector-reconciler"
description: "Runs pulumi refresh on schedule to detect drift between live cloud resources and Pulumi state. Classifies drift by severity and opens a Jira ticket for destructive changes. Non-destructive drift is auto-reconciled via pulumi up --target for specific resources."
github_stars: 25042
verification: "listed"
source: "https://github.com/pulumi/pulumi"
author: "Pulumi"
category: "Runbooks & Diagnostics"
framework: "Codex"
tool_ecosystem:
  github_repo: "pulumi/pulumi"
  github_stars: 25042
  npm_package: "@pulumi/pulumi"
  npm_weekly_downloads: 2073384
---

# Pulumi Drift Detector & Reconciler

Runs pulumi refresh on schedule to detect drift between live cloud resources and Pulumi state. Classifies drift by severity and opens a Jira ticket for destructive changes. Non-destructive drift is auto-reconciled via pulumi up --target for specific resources.

## Installation

No source-backed install or usage instructions could be extracted automatically. Review the upstream project before running this skill in a sensitive workflow.

- Source: https://github.com/pulumi/pulumi

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pulumi-drift-detector-reconciler/)
