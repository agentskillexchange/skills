---
name: "PagerDuty Incident Runbook Automator"
description: "Automates incident response runbooks using the PagerDuty Events API v2 and REST API. Manages incident creation, escalation policies, and automated diagnostics triggered by alert severity."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/pagerduty-incident-runbook-automator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "pagerduty"  # from ase_tool_match
  github_stars: 69  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 210829  # from ase_npm_downloads
  github_repo: "PagerDuty/pdjs"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: false  # from ase_tool_maintained
---

# PagerDuty Incident Runbook Automator

Automates incident response runbooks using the PagerDuty Events API v2 and REST API. Manages incident creation, escalation policies, and automated diagnostics triggered by alert severity.

## Overview

The PagerDuty Incident Runbook Automator skill integrates with the PagerDuty Events API v2 (events.pagerduty.com/v2/enqueue) and REST API (api.pagerduty.com) to automate incident response workflows. It creates incidents via the Events API with routing_key, event_action (trigger, acknowledge, resolve), and severity levels (critical, error, warning, info).

The skill manages incident lifecycle through REST API endpoints: POST /incidents for manual creation, PUT /incidents/{id} for status updates and reassignment, POST /incidents/{id}/notes for timeline annotations, and GET /incidents/{id}/log_entries for audit trail retrieval. It configures escalation policies using /escalation_policies with multi-level escalation rules and timeout-based progression.

Key capabilities include automated runbook execution triggered by webhook events (incident.trigger, incident.acknowledge), integration with monitoring tools via Events API v2 change events and alert grouping (time-based, intelligent, content-based), service dependency mapping through /service_dependencies for impact analysis, and response play automation with /response_plays for coordinated team mobilization. The automator also supports maintenance window management, on-call schedule rotation queries via /oncalls, and status page integration for external communication during incidents.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill pagerduty-incident-runbook-automator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill pagerduty-incident-runbook-automator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill pagerduty-incident-runbook-automator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill pagerduty-incident-runbook-automator -a codex
```

### OpenClaw

```bash
clawhub install pagerduty-incident-runbook-automator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/pagerduty-incident-runbook-automator/
