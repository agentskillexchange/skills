---
title: "AWS Systems Manager Automation Incident Guide"
description: "Coordinates remediation playbooks with AWS Systems Manager Automation, Incident Manager, and CloudWatch alarm context for repeatable operational recovery. Useful for agents that need to recommend or launch the right runbook when alarms cross into known failure territory."
verification: "security_reviewed"
source: "https://docs.aws.amazon.com/systems-manager/"
category: ["Runbooks &amp; Diagnostics"]
framework: ["ChatGPT Agents"]
---

# AWS Systems Manager Automation Incident Guide

Coordinates remediation playbooks with AWS Systems Manager Automation, Incident Manager, and CloudWatch alarm context for repeatable operational recovery. Useful for agents that need to recommend or launch the right runbook when alarms cross into known failure territory.

## Installation

Choose the install path that fits your setup:

1. Install from the Agent Skill Exchange catalog if your agent client supports it.
2. Copy the skill folder into your local skills directory.
3. Add it as a git submodule in your shared agent-skills repo.
4. Vendor the files directly into a project-specific `.agents/skills/` or equivalent folder.
5. Keep a fork or mirror if you need local modifications or pinned revisions.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-systems-manager-automation-incident-guide/)
