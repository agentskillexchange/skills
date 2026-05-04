---
title: "Pulumi Drift Detector &amp; Reconciler"
slug: "pulumi-drift-detector-reconciler"
description: "Runs pulumi refresh on schedule to detect drift between live cloud resources and Pulumi state. Classifies drift by severity and opens a Jira ticket for destructive changes. Non-destructive drift is auto-reconciled via pulumi up &#8211;target for specific resources."
verification: security_reviewed
source: "https://github.com/pulumi/pulumi"
category: "Runbooks &amp; Diagnostics"
framework: "Codex"
tool_ecosystem:
  github_repo: "pulumi/pulumi"
  github_stars: 25042
  npm_package: "@pulumi/pulumi"
  npm_weekly_downloads: 2073384
---
# Pulumi Drift Detector &amp; Reconciler

Runs pulumi refresh on schedule to detect drift between live cloud resources and Pulumi state. Classifies drift by severity and opens a Jira ticket for destructive changes. Non-destructive drift is auto-reconciled via pulumi up &#8211;target for specific resources.

## Installation

1. Clone this skill repository.
2. Open this skill folder.
3. Review prerequisites and setup needs.
4. Install required dependencies.
5. Run and test in your environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pulumi-drift-detector-reconciler/)
