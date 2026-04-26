---
title: "Pulumi Drift Detector & Reconciler"
description: "Runs pulumi refresh on schedule to detect drift between live cloud resources and Pulumi state. Classifies drift by severity and opens a Jira ticket for destructive changes. Non-destructive drift is auto-reconciled via pulumi up –target for specific resources."
verification: "security_reviewed"
source: "https://github.com/pulumi/pulumi"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "pulumi/pulumi"
  github_stars: 25042
  npm_package: "@pulumi/pulumi"
  npm_weekly_downloads: 2073384
---

# Pulumi Drift Detector & Reconciler

Runs pulumi refresh on schedule to detect drift between live cloud resources and Pulumi state. Classifies drift by severity and opens a Jira ticket for destructive changes. Non-destructive drift is auto-reconciled via pulumi up –target for specific resources.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/pulumi-drift-detector-reconciler/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/pulumi-drift-detector-reconciler
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/pulumi-drift-detector-reconciler`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pulumi-drift-detector-reconciler/)
