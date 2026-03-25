---
name: "AWS Systems Manager Automation Incident Guide"
description: "Coordinates remediation playbooks with AWS Systems Manager Automation, Incident Manager, and CloudWatch alarm context for repeatable operational recovery. Useful for agents that need to recommend or launch the right runbook when alarms cross into known failure territory."
category: "Runbooks & Diagnostics"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/aws-systems-manager-automation-incident-guide/"
tool_ecosystem:
  tool: "aws"
  github_stars: 3594
  npm_weekly_downloads: 9204385
  github_repo: "aws/aws-sdk-js-v3"
  license: "Apache-2.0"
  maintained: true
---

# AWS Systems Manager Automation Incident Guide

Coordinates remediation playbooks with AWS Systems Manager Automation, Incident Manager, and CloudWatch alarm context for repeatable operational recovery. Useful for agents that need to recommend or launch the right runbook when alarms cross into known failure territory.

## Overview

AWS Systems Manager Automation Incident Guide is built for cloud teams that already have operational runbooks but need a more structured way for agents to connect alarms with recovery actions. The skill uses AWS Systems Manager Automation documents, Incident Manager response plans, and CloudWatch alarm context to identify which remediation sequence matches a live issue. That helps when the same classes of EC2, networking, or application failures keep recurring and responders waste time remembering which document to run.

Because the workflow is grounded in real AWS APIs and runbook documents, it can pull alarm metadata, affected resources, and linked remediation steps into one place. It is especially helpful in environments where some incidents only need guided response while others should trigger Automation execution under controlled permissions. The skill can distinguish those cases and prepare a cleaner handoff for humans who still need to approve or supervise the action.

Use this skill when you want incident handling to be based on actual SSM Automation and Incident Manager building blocks rather than informal wiki pages or tribal knowledge.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill aws-systems-manager-automation-incident-guide
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill aws-systems-manager-automation-incident-guide -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill aws-systems-manager-automation-incident-guide -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill aws-systems-manager-automation-incident-guide -a codex
```

### OpenClaw

```bash
clawhub install aws-systems-manager-automation-incident-guide
```

## Source

- Marketplace: https://agentskillexchange.com/skills/aws-systems-manager-automation-incident-guide/
