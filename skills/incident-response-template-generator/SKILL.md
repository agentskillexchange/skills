---
title: Incident Response Template Generator
description: 'The Incident Response Template Generator skill creates comprehensive
  incident response documentation and automation templates. It integrates with the
  PagerDuty Events API v2 for incident escalation triggers, severity classification,
  and on-call routing based on service dependencies. Jira REST API integration automates
  incident ticket creation with properly linked epic hierarchies, custom field population
  for incident metadata (severity, blast radius, customer impact), and automated subtask
  generation for response phases. Statuspage.io API integration manages public status
  page updates including component status changes, incident creation with real-time
  updates, and maintenance window scheduling. The skill generates structured response
  templates following the ICS (Incident Command System) framework with defined roles:
  Incident Commander, Communications Lead, Operations Lead, and Subject Matter Experts.
  Templates include communication scripts for stakeholder notifications, customer-facing
  status updates, and internal Slack channel management procedures. Post-incident
  review templates capture timeline reconstruction, contributing factors analysis,
  and action item tracking. The generator supports customizable severity matrices,
  escalation path definitions, and SLA-aware response time targets. Output formats
  include Confluence wiki pages, Notion databases, and Markdown documents for repository
  storage.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/incident-response-template-generator/
category:
- Templates &amp; Workflows
framework:
- Custom Agents
---

# Incident Response Template Generator

The Incident Response Template Generator skill creates comprehensive incident response documentation and automation templates. It integrates with the PagerDuty Events API v2 for incident escalation triggers, severity classification, and on-call routing based on service dependencies. Jira REST API integration automates incident ticket creation with properly linked epic hierarchies, custom field population for incident metadata (severity, blast radius, customer impact), and automated subtask generation for response phases. Statuspage.io API integration manages public status page updates including component status changes, incident creation with real-time updates, and maintenance window scheduling. The skill generates structured response templates following the ICS (Incident Command System) framework with defined roles: Incident Commander, Communications Lead, Operations Lead, and Subject Matter Experts. Templates include communication scripts for stakeholder notifications, customer-facing status updates, and internal Slack channel management procedures. Post-incident review templates capture timeline reconstruction, contributing factors analysis, and action item tracking. The generator supports customizable severity matrices, escalation path definitions, and SLA-aware response time targets. Output formats include Confluence wiki pages, Notion databases, and Markdown documents for repository storage.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/incident-response-template-generator/)
