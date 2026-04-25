---
title: "Incident Response Template Generator"
description: "Creates structured incident response templates using the PagerDuty Events API v2, Jira REST API for ticket creation, and Statuspage.io API for public status updates. Generates runbook-linked response procedures."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/incident-response-template-generator/"
category:
  - "Templates & Workflows"
framework:
  - "Custom Agents"
---

# Incident Response Template Generator

The Incident Response Template Generator skill creates comprehensive incident response documentation and automation templates. It integrates with the PagerDuty Events API v2 for incident escalation triggers, severity classification, and on-call routing based on service dependencies. Jira REST API integration automates incident ticket creation with properly linked epic hierarchies, custom field population for incident metadata (severity, blast radius, customer impact), and automated subtask generation for response phases. Statuspage.io API integration manages public status page updates including component status changes, incident creation with real-time updates, and maintenance window scheduling. The skill generates structured response templates following the ICS (Incident Command System) framework with defined roles: Incident Commander, Communications Lead, Operations Lead, and Subject Matter Experts. Templates include communication scripts for stakeholder notifications, customer-facing status updates, and internal Slack channel management procedures. Post-incident review templates capture timeline reconstruction, contributing factors analysis, and action item tracking. The generator supports customizable severity matrices, escalation path definitions, and SLA-aware response time targets. Output formats include Confluence wiki pages, Notion databases, and Markdown documents for repository storage.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/incident-response-template-generator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/incident-response-template-generator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/incident-response-template-generator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/incident-response-template-generator/)
