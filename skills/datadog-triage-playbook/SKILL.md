---
title: "Datadog Triage Playbook"
description: "Automates alert triage using the Datadog Monitors API v2 and Notebooks API. Correlates metrics with traces via the Datadog APM Trace Search API and generates RCA timelines from the Events Stream API."
slug: "datadog-triage-playbook"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/datadog-triage-playbook/"
---

# Datadog Triage Playbook

Automates alert triage using the Datadog Monitors API v2 and Notebooks API. Correlates metrics with traces via the Datadog APM Trace Search API and generates RCA timelines from the Events Stream API.

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
clawhub install datadog-triage-playbook
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Datadog Triage Playbook skill provides automated incident triage workflows powered by Datadog observability data. It uses the Datadog Monitors API v2 to query active alerts, enrich them with monitor metadata, and automatically adjust notification escalation based on alert severity and duration. The skill correlates infrastructure metrics with application traces using the Datadog APM Trace Search API, identifying slow endpoints, error spikes, and upstream dependency failures. Root cause analysis timelines are generated from the Events Stream API, combining deployment events, configuration changes, and infrastructure modifications into a chronological narrative. The skill leverages the Notebooks API to create shareable incident investigation documents with embedded graphs, log samples, and trace flamegraphs. It supports SLO status checking via the Service Level Objectives API, dashboard snapshot generation for stakeholder communication, and automated runbook execution through Datadog Workflow Automation triggers. Integration with the Incidents API provides structured incident lifecycle management from detection through resolution.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-triage-playbook/)
