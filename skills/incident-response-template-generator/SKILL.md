---
title: "Incident Response Template Generator"
description: "Creates structured incident response templates using the PagerDuty Events API v2, Jira REST API for ticket creation, and Statuspage.io API for public status updates. Generates runbook-linked response procedures."
slug: "incident-response-template-generator"
category:
  - "Templates &amp; Workflows"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/incident-response-template-generator/"
listed: true
---

# Incident Response Template Generator

Creates structured incident response templates using the PagerDuty Events API v2, Jira REST API for ticket creation, and Statuspage.io API for public status updates. Generates runbook-linked response procedures.

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
clawhub install incident-response-template-generator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Incident Response Template Generator skill creates comprehensive incident response documentation and automation templates. It integrates with the PagerDuty Events API v2 for incident escalation triggers, severity classification, and on-call routing based on service dependencies. Jira REST API integration automates incident ticket creation with properly linked epic hierarchies, custom field population for incident metadata (severity, blast radius, customer impact), and automated subtask generation for response phases. Statuspage.io API integration manages public status page updates including component status changes, incident creation with real-time updates, and maintenance window scheduling. The skill generates structured response templates following the ICS (Incident Command System) framework with defined roles: Incident Commander, Communications Lead, Operations Lead, and Subject Matter Experts. Templates include communication scripts for stakeholder notifications, customer-facing status updates, and internal Slack channel management procedures. Post-incident review templates capture timeline reconstruction, contributing factors analysis, and action item tracking. The generator supports customizable severity matrices, escalation path definitions, and SLA-aware response time targets. Output formats include Confluence wiki pages, Notion databases, and Markdown documents for repository storage.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/incident-response-template-generator/)
