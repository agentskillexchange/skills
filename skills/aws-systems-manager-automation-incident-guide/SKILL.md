---
name: "AWS Systems Manager Automation Incident Guide"
description: "Coordinates remediation playbooks with AWS Systems Manager Automation, Incident Manager, and CloudWatch alarm context for repeatable operational recovery. Useful for agents that need to recommend or launch the right runbook when alarms cross into known failure territory."
verification: security_reviewed
source: "https://docs.aws.amazon.com/systems-manager/"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "ChatGPT Agents"
---

# AWS Systems Manager Automation Incident Guide

AWS Systems Manager Automation Incident Guide is built for cloud teams that already have operational runbooks but need a more structured way for agents to connect alarms with recovery actions. The skill uses AWS Systems Manager Automation documents, Incident Manager response plans, and CloudWatch alarm context to identify which remediation sequence matches a live issue. That helps when the same classes of EC2, networking, or application failures keep recurring and responders waste time remembering which document to run.
Because the workflow is grounded in real AWS APIs and runbook documents, it can pull alarm metadata, affected resources, and linked remediation steps into one place. It is especially helpful in environments where some incidents only need guided response while others should trigger Automation execution under controlled permissions. The skill can distinguish those cases and prepare a cleaner handoff for humans who still need to approve or supervise the action.
Use this skill when you want incident handling to be based on actual SSM Automation and Incident Manager building blocks rather than informal wiki pages or tribal knowledge.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-systems-manager-automation-incident-guide/)
