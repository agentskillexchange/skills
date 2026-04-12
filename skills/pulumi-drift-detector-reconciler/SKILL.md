---
title: "Pulumi Drift Detector & Reconciler"
slug: "pulumi-drift-detector-reconciler"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Codex"
source: "https://agentskillexchange.com/skills/pulumi-drift-detector-reconciler/"
---

# Pulumi Drift Detector & Reconciler

Runs pulumi refresh on schedule to detect drift between live cloud resources and Pulumi state. Classifies drift by severity and opens a Jira ticket for destructive changes. Non-destructive drift is auto-reconciled via pulumi up –target for specific resources.

## Installation

Choose the method that fits your setup:

1. Clone or download this repo and copy the skill folder into your local skills directory.
2. Install from the Agent Skill Exchange repo with your preferred Git workflow.
3. Add the skill folder as a git submodule if you manage skills as dependencies.
4. Copy the files manually into a local custom-skills directory for testing.
5. Use any marketplace or sync tooling you already have for pulling ASE skills.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pulumi-drift-detector-reconciler/)
