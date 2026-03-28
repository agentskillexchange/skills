---
name: "PagerDuty Incident Orchestrator"
description: "Manages PagerDuty incident lifecycle using the PagerDuty Events API v2 and REST API. Automates escalation policies, runbook attachment, and post-incident timeline generation."
category: "Monitoring & Alerts"
framework: "MCP"
verification: security_reviewed
source: "https://github.com/PagerDuty/pdjs"
tool_ecosystem:
  tool: pagerduty
  github_stars: 69
  npm_weekly_downloads: 210829
  github_repo: PagerDuty/pdjs
  license: Apache-2.0
  maintained: false
---

# PagerDuty Incident Orchestrator

Manages PagerDuty incident lifecycle using the PagerDuty Events API v2 and REST API. Automates escalation policies, runbook attachment, and post-incident timeline generation.

## Overview

The PagerDuty Incident Orchestrator skill automates incident management workflows through the PagerDuty Events API v2 and REST API v2. It creates and manages incidents with proper severity classification, service assignment, and escalation policy routing. The skill automatically attaches relevant runbooks from a configured knowledge base when incidents match predefined alert patterns, using the PagerDuty Rulesets API for intelligent routing. It manages on-call schedule queries via the Schedules API to identify current responders, triggers incident actions through the Incident Workflows API, and generates post-incident timelines by correlating PagerDuty log entries with deployment events and monitoring alerts. The orchestrator supports incident merging for related alerts, configures response plays for common scenarios, and produces incident review documents with MTTD, MTTA, and MTTR metrics calculated from the Analytics API.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill pagerduty-incident-orchestrator-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill pagerduty-incident-orchestrator-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill pagerduty-incident-orchestrator-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill pagerduty-incident-orchestrator-2 -a codex
```

### OpenClaw

```bash
clawhub install pagerduty-incident-orchestrator-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/pagerduty-incident-orchestrator-2/
