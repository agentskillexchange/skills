---
title: "AWS Systems Manager Automation Incident Guide"
description: "Coordinates remediation playbooks with AWS Systems Manager Automation, Incident Manager, and CloudWatch alarm context for repeatable operational recovery. Useful for agents that need to recommend or launch the right runbook when alarms cross into known failure territory."
verification: security_reviewed
source: "https://docs.aws.amazon.com/systems-manager/"
category:
  - "Runbooks & Diagnostics"
framework:
  - "ChatGPT Agents"
---

# AWS Systems Manager Automation Incident Guide

Coordinates remediation playbooks with AWS Systems Manager Automation, Incident Manager, and CloudWatch alarm context for repeatable operational recovery. Useful for agents that need to recommend or launch the right runbook when alarms cross into known failure territory.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/aws-systems-manager-automation-incident-guide/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/aws-systems-manager-automation-incident-guide
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/aws-systems-manager-automation-incident-guide`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-systems-manager-automation-incident-guide/)
