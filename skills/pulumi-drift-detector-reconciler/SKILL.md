---
name: Pulumi Drift Detector & Reconciler
description: Runs pulumi refresh on schedule to detect drift between live cloud resources
  and Pulumi state. Classifies drift by severity and opens a Jira ticket for destructive
  changes. Non-destructive drift is auto-reconciled via pulumi up –target for specific
  resources.
category: Runbooks & Diagnostics
framework: Codex
verification: security_reviewed
source: https://github.com/pulumi/pulumi
tool_ecosystem:
  github_repo: pulumi/pulumi
  github_stars: 25042
  tool: '@pulumi/pulumi'
  npm_weekly_downloads: 2073384
  license: Apache-2.0
  maintained: true
---
# Pulumi Drift Detector & Reconciler
Runs pulumi refresh on schedule to detect drift between live cloud resources and Pulumi state. Classifies drift by severity and opens a Jira ticket for destructive changes. Non-destructive drift is auto-reconciled via pulumi up –target for specific resources.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/pulumi-drift-detector-reconciler
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/pulumi-drift-detector-reconciler` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pulumi-drift-detector-reconciler/)
