---
title: "Datadog Triage Playbook"
description: "The Datadog Triage Playbook skill provides automated incident triage workflows powered by Datadog observability data. It uses the Datadog Monitors API v2 to query active alerts, enrich them with monitor metadata, and automatically adjust notification escalation based on alert severity and duration. The skill correlates infrastructure metrics with application traces using the Datadog APM Trace Search API, identifying slow endpoints, error spikes, and upstream dependency failures. Root cause analysis timelines are generated from the Events Stream API, combining deployment events, configuration changes, and infrastructure modifications into a chronological narrative. The skill leverages the Notebooks API to create shareable incident investigation documents with embedded graphs, log samples, and trace flamegraphs. It supports SLO status checking via the Service Level Objectives API, dashboard snapshot generation for stakeholder communication, and automated runbook execution through Datadog Workflow Automation triggers. Integration with the Incidents API provides structured incident lifecycle management from detection through resolution."
source: "https://github.com/DataDog/dd-trace-js"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
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

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-triage-playbook/)
