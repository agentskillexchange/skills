---
title: "Datadog Incident Runbook Runner"
slug: "datadog-incident-runbook-runner-2"
description: "Fetches an active Datadog incident, retrieves associated monitors and dashboards, pulls the last 30 minutes of metric data, and walks through a runbook checklist with automated triage steps. Reduces mean time to diagnosis by surfacing signal without dashboard navigation."
verification: security_reviewed
source: "https://github.com/DataDog/dd-trace-js"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
---

# Datadog Incident Runbook Runner

Fetches an active Datadog incident, retrieves associated monitors and dashboards, pulls the last 30 minutes of metric data, and walks through a runbook checklist with automated triage steps. Reduces mean time to diagnosis by surfacing signal without dashboard navigation.

## Installation

1. Clone this skill into your local skills directory.
2. Review the required tools and environment variables.
3. Install dependencies with your preferred package manager or runtime.
4. Run the upstream install command from the project documentation, if needed.
5. Validate the installation and test the skill in your agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-incident-runbook-runner-2/)
