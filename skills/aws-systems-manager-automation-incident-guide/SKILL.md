---
title: "AWS Systems Manager Automation Incident Guide"
description: "AWS Systems Manager Automation Incident Guide is built for cloud teams that already have operational runbooks but need a more structured way for agents to connect alarms with recovery actions. The skill uses AWS Systems Manager Automation documents, Incident Manager response plans, and CloudWatch alarm context to identify which remediation sequence matches a live issue. That helps when the same classes of EC2, networking, or application failures keep recurring and responders waste time remembering which document to run. Because the workflow is grounded in real AWS APIs and runbook documents, it can pull alarm metadata, affected resources, and linked remediation steps into one place. It is especially helpful in environments where some incidents only need guided response while others should trigger Automation execution under controlled permissions. The skill can distinguish those cases and prepare a cleaner handoff for humans who still need to approve or supervise the action. Use this skill when you want incident handling to be based on actual SSM Automation and Incident Manager building blocks rather than informal wiki pages or tribal knowledge."
source: "https://docs.aws.amazon.com/systems-manager/"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "ChatGPT Agents"
---

# AWS Systems Manager Automation Incident Guide

AWS Systems Manager Automation Incident Guide is built for cloud teams that already have operational runbooks but need a more structured way for agents to connect alarms with recovery actions. The skill uses AWS Systems Manager Automation documents, Incident Manager response plans, and CloudWatch alarm context to identify which remediation sequence matches a live issue. That helps when the same classes of EC2, networking, or application failures keep recurring and responders waste time remembering which document to run. Because the workflow is grounded in real AWS APIs and runbook documents, it can pull alarm metadata, affected resources, and linked remediation steps into one place. It is especially helpful in environments where some incidents only need guided response while others should trigger Automation execution under controlled permissions. The skill can distinguish those cases and prepare a cleaner handoff for humans who still need to approve or supervise the action. Use this skill when you want incident handling to be based on actual SSM Automation and Incident Manager building blocks rather than informal wiki pages or tribal knowledge.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-systems-manager-automation-incident-guide/)
