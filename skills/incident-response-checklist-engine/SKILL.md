---
title: "Incident Response Checklist Engine"
description: "Generates and tracks incident response checklists using PagerDuty Incident Workflows API and Statuspage.io API. Automates severity classification, stakeholder notification, and post-incident review scheduling with Jira Service Management integration."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/incident-response-checklist-engine/"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Claude Agents"
---

# Incident Response Checklist Engine

The Incident Response Checklist Engine skill provides structured incident management workflows that guide teams through detection, triage, mitigation, and resolution phases. It integrates with PagerDuty Incident Workflows API to automate response procedures based on incident severity and affected services. The skill classifies incident severity (SEV1-SEV4) based on configurable criteria including affected user count, service criticality, and blast radius. Each severity level triggers a corresponding checklist with phase-appropriate tasks: initial assessment, communication setup, investigation, mitigation, resolution, and post-incident review. Statuspage.io API integration enables automatic incident creation and status updates. The skill manages component status transitions (operational → degraded_performance → partial_outage → major_outage) and posts real-time updates visible to end users. Template-based update messages ensure consistent communication. Stakeholder notification chains are managed through PagerDuty escalation policies with automatic escalation timers. The skill integrates with Jira Service Management to create post-incident review tickets with pre-populated timelines, assign action items to responsible parties, and schedule retrospective meetings via calendar API integration.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/incident-response-checklist-engine/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/incident-response-checklist-engine
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/incident-response-checklist-engine`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/incident-response-checklist-engine/)
