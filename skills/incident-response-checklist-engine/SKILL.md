---
title: "Incident Response Checklist Engine"
description: "Generates and tracks incident response checklists using PagerDuty Incident Workflows API and Statuspage.io API. Automates severity classification, stakeholder notification, and post-incident review scheduling with Jira Service Management integration."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/incident-response-checklist-engine/"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Claude Agents"
---

# Incident Response Checklist Engine

The Incident Response Checklist Engine skill provides structured incident management workflows that guide teams through detection, triage, mitigation, and resolution phases. It integrates with PagerDuty Incident Workflows API to automate response procedures based on incident severity and affected services.

The skill classifies incident severity (SEV1-SEV4) based on configurable criteria including affected user count, service criticality, and blast radius. Each severity level triggers a corresponding checklist with phase-appropriate tasks: initial assessment, communication setup, investigation, mitigation, resolution, and post-incident review.

Statuspage.io API integration enables automatic incident creation and status updates. The skill manages component status transitions (operational → degraded_performance → partial_outage → major_outage) and posts real-time updates visible to end users. Template-based update messages ensure consistent communication.

Stakeholder notification chains are managed through PagerDuty escalation policies with automatic escalation timers. The skill integrates with Jira Service Management to create post-incident review tickets with pre-populated timelines, assign action items to responsible parties, and schedule retrospective meetings via calendar API integration.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/incident-response-checklist-engine/)
