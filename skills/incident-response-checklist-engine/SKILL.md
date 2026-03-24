---
name: "Incident Response Checklist Engine"
description: "Generates and tracks incident response checklists using PagerDuty Incident Workflows API and Statuspage.io API. Automates severity classification, stakeholder notification, and post-incident review scheduling with Jira Service Management integration."
category: "Runbooks & Diagnostics"
framework: "Claude Agents"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/incident-response-checklist-engine/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "pagerduty"  # from ase_tool_match
  github_stars: 69  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 210829  # from ase_npm_downloads
  github_repo: "PagerDuty/pdjs"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: false  # from ase_tool_maintained
---

# Incident Response Checklist Engine

Generates and tracks incident response checklists using PagerDuty Incident Workflows API and Statuspage.io API. Automates severity classification, stakeholder notification, and post-incident review scheduling with Jira Service Management integration.

## Overview

The Incident Response Checklist Engine skill provides structured incident management workflows that guide teams through detection, triage, mitigation, and resolution phases. It integrates with PagerDuty Incident Workflows API to automate response procedures based on incident severity and affected services.

The skill classifies incident severity (SEV1-SEV4) based on configurable criteria including affected user count, service criticality, and blast radius. Each severity level triggers a corresponding checklist with phase-appropriate tasks: initial assessment, communication setup, investigation, mitigation, resolution, and post-incident review.

Statuspage.io API integration enables automatic incident creation and status updates. The skill manages component status transitions (operational → degraded_performance → partial_outage → major_outage) and posts real-time updates visible to end users. Template-based update messages ensure consistent communication.

Stakeholder notification chains are managed through PagerDuty escalation policies with automatic escalation timers. The skill integrates with Jira Service Management to create post-incident review tickets with pre-populated timelines, assign action items to responsible parties, and schedule retrospective meetings via calendar API integration.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill incident-response-checklist-engine
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill incident-response-checklist-engine -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill incident-response-checklist-engine -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill incident-response-checklist-engine -a codex
```

### OpenClaw

```bash
clawhub install incident-response-checklist-engine
```

## Source

- Marketplace: https://agentskillexchange.com/skills/incident-response-checklist-engine/
