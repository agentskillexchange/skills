---
title: "Pulumi Drift Detector & Reconciler"
description: "Runs pulumi refresh on schedule to detect drift between live cloud resources and Pulumi state. Classifies drift by severity and opens a Jira ticket for destructive changes. Non-destructive drift is auto-reconciled via pulumi up –target for specific resources."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/pulumi-drift-detector-reconciler/"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Codex"
---

# Pulumi Drift Detector & Reconciler

Runs pulumi refresh on schedule to detect drift between live cloud resources and Pulumi state. Classifies drift by severity and opens a Jira ticket for destructive changes. Non-destructive drift is auto-reconciled via pulumi up –target for specific resources.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pulumi-drift-detector-reconciler/)
