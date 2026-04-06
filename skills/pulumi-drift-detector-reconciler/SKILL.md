---
title: "Pulumi Drift Detector & Reconciler"
description: "Runs pulumi refresh on schedule to detect drift between live cloud resources and Pulumi state. Classifies drift by severity and opens a Jira ticket for destructive changes. Non-destructive drift is auto-reconciled via pulumi up –target for specific resources."
slug: "pulumi-drift-detector-reconciler"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/pulumi-drift-detector-reconciler/"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Codex"
---

# Pulumi Drift Detector & Reconciler

Runs pulumi refresh on schedule to detect drift between live cloud resources and Pulumi state. Classifies drift by severity and opens a Jira ticket for destructive changes. Non-destructive drift is auto-reconciled via pulumi up –target for specific resources.

## Installation

You can install this skill in any of these ways:

1. Install from Agent Skill Exchange in the OpenClaw UI
2. Clone or copy the skill folder into your local skills directory
3. Add it to your workspace-managed skills collection
4. Install via any compatible skill package manager or sync workflow
5. Copy the `SKILL.md` and any referenced files into a compatible AgentSkills directory

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pulumi-drift-detector-reconciler/)
