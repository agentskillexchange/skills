---
name: "Datadog Triage Playbook"
description: "Automates alert triage using the Datadog Monitors API v2 and Notebooks API. Correlates metrics with traces via the Datadog APM Trace Search API and generates RCA timelines from the Events Stream API."
category: "Runbooks & Diagnostics"
framework: "MCP"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/datadog-triage-playbook/"
---
# Datadog Triage Playbook

Automates alert triage using the Datadog Monitors API v2 and Notebooks API. Correlates metrics with traces via the Datadog APM Trace Search API and generates RCA timelines from the Events Stream API.

## Overview

The Datadog Triage Playbook skill provides automated incident triage workflows powered by Datadog observability data. It uses the Datadog Monitors API v2 to query active alerts, enrich them with monitor metadata, and automatically adjust notification escalation based on alert severity and duration. The skill correlates infrastructure metrics with application traces using the Datadog APM Trace Search API, identifying slow endpoints, error spikes, and upstream dependency failures. Root cause analysis timelines are generated from the Events Stream API, combining deployment events, configuration changes, and infrastructure modifications into a chronological narrative. The skill leverages the Notebooks API to create shareable incident investigation documents with embedded graphs, log samples, and trace flamegraphs. It supports SLO status checking via the Service Level Objectives API, dashboard snapshot generation for stakeholder communication, and automated runbook execution through Datadog Workflow Automation triggers. Integration with the Incidents API provides structured incident lifecycle management from detection through resolution.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill datadog-triage-playbook
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill datadog-triage-playbook -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill datadog-triage-playbook -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill datadog-triage-playbook -a codex
```

### OpenClaw

```bash
clawhub install datadog-triage-playbook
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-triage-playbook/)
