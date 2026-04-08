---
title: Incident Response Checklist Engine
description: 'The Incident Response Checklist Engine skill provides structured incident
  management workflows that guide teams through detection, triage, mitigation, and
  resolution phases. It integrates with PagerDuty Incident Workflows API to automate
  response procedures based on incident severity and affected services. The skill
  classifies incident severity (SEV1-SEV4) based on configurable criteria including
  affected user count, service criticality, and blast radius. Each severity level
  triggers a corresponding checklist with phase-appropriate tasks: initial assessment,
  communication setup, investigation, mitigation, resolution, and post-incident review.
  Statuspage.io API integration enables automatic incident creation and status updates.
  The skill manages component status transitions (operational → degraded_performance
  → partial_outage → major_outage) and posts real-time updates visible to end users.
  Template-based update messages ensure consistent communication. Stakeholder notification
  chains are managed through PagerDuty escalation policies with automatic escalation
  timers. The skill integrates with Jira Service Management to create post-incident
  review tickets with pre-populated timelines, assign action items to responsible
  parties, and schedule retrospective meetings via calendar API integration.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/incident-response-checklist-engine/
category:
- Runbooks &amp; Diagnostics
framework:
- Claude Agents
---

# Incident Response Checklist Engine

The Incident Response Checklist Engine skill provides structured incident management workflows that guide teams through detection, triage, mitigation, and resolution phases. It integrates with PagerDuty Incident Workflows API to automate response procedures based on incident severity and affected services. The skill classifies incident severity (SEV1-SEV4) based on configurable criteria including affected user count, service criticality, and blast radius. Each severity level triggers a corresponding checklist with phase-appropriate tasks: initial assessment, communication setup, investigation, mitigation, resolution, and post-incident review. Statuspage.io API integration enables automatic incident creation and status updates. The skill manages component status transitions (operational → degraded_performance → partial_outage → major_outage) and posts real-time updates visible to end users. Template-based update messages ensure consistent communication. Stakeholder notification chains are managed through PagerDuty escalation policies with automatic escalation timers. The skill integrates with Jira Service Management to create post-incident review tickets with pre-populated timelines, assign action items to responsible parties, and schedule retrospective meetings via calendar API integration.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/incident-response-checklist-engine/)
