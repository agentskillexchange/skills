---
title: "Datadog Triage Playbook"
description: "Automates alert triage using the Datadog Monitors API v2 and Notebooks API. Correlates metrics with traces via the Datadog APM Trace Search API and generates RCA timelines from the Events Stream API."
verification: security_reviewed
source: "https://github.com/DataDog/dd-trace-js"
category:
  - "Runbooks & Diagnostics"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "datadog/dd-trace-js"
  github_stars: 791
  npm_package: "dd-trace"
  npm_weekly_downloads: 6596660
---

# Datadog Triage Playbook

The Datadog Triage Playbook skill provides automated incident triage workflows powered by Datadog observability data. It uses the Datadog Monitors API v2 to query active alerts, enrich them with monitor metadata, and automatically adjust notification escalation based on alert severity and duration. The skill correlates infrastructure metrics with application traces using the Datadog APM Trace Search API, identifying slow endpoints, error spikes, and upstream dependency failures. Root cause analysis timelines are generated from the Events Stream API, combining deployment events, configuration changes, and infrastructure modifications into a chronological narrative. The skill leverages the Notebooks API to create shareable incident investigation documents with embedded graphs, log samples, and trace flamegraphs. It supports SLO status checking via the Service Level Objectives API, dashboard snapshot generation for stakeholder communication, and automated runbook execution through Datadog Workflow Automation triggers. Integration with the Incidents API provides structured incident lifecycle management from detection through resolution.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/datadog-triage-playbook
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/datadog-triage-playbook` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-triage-playbook/)
