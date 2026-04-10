---
title: "Incident Response Checklist Engine"
description: "Generates and tracks incident response checklists using PagerDuty Incident Workflows API and Statuspage.io API. Automates severity classification, stakeholder notification, and post-incident review scheduling with Jira Service Management integration."
slug: "incident-response-checklist-engine"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Claude Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/incident-response-checklist-engine/"
listed: true
---

# Incident Response Checklist Engine

Generates and tracks incident response checklists using PagerDuty Incident Workflows API and Statuspage.io API. Automates severity classification, stakeholder notification, and post-incident review scheduling with Jira Service Management integration.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install incident-response-checklist-engine
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Incident Response Checklist Engine skill provides structured incident management workflows that guide teams through detection, triage, mitigation, and resolution phases. It integrates with PagerDuty Incident Workflows API to automate response procedures based on incident severity and affected services.
The skill classifies incident severity (SEV1-SEV4) based on configurable criteria including affected user count, service criticality, and blast radius. Each severity level triggers a corresponding checklist with phase-appropriate tasks: initial assessment, communication setup, investigation, mitigation, resolution, and post-incident review.
Statuspage.io API integration enables automatic incident creation and status updates. The skill manages component status transitions (operational → degraded_performance → partial_outage → major_outage) and posts real-time updates visible to end users. Template-based update messages ensure consistent communication.
Stakeholder notification chains are managed through PagerDuty escalation policies with automatic escalation timers. The skill integrates with Jira Service Management to create post-incident review tickets with pre-populated timelines, assign action items to responsible parties, and schedule retrospective meetings via calendar API integration.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/incident-response-checklist-engine/)
