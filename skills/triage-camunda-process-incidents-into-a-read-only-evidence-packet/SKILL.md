---
name: "Triage Camunda process incidents into a read-only evidence packet"
slug: "triage-camunda-process-incidents-into-a-read-only-evidence-packet"
description: "Search and inspect scoped Camunda 8 incidents, distinguish observed errors from suspected causes, and hand off a read-only triage packet."
github_stars: 4367
verification: "security_reviewed"
source: "https://github.com/camunda/camunda"
author: "Camunda"
publisher_type: "community"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "camunda/camunda"
  github_stars: 4367
---

# Triage Camunda process incidents into a read-only evidence packet

Search and inspect scoped Camunda 8 incidents, distinguish observed errors from suspected causes, and hand off a read-only triage packet.

## Prerequisites

HTTP client; existing Camunda 8 Orchestration Cluster; deployment-specific authentication with incident read permissions

## Installation

Install or set up from the source-backed instructions:

Use an existing version-matched Camunda 8 cluster. Configure its /v2 REST base and supported authentication; grant READ_PROCESS_INSTANCE where authorization is enabled. No separate agent package is required. Start with a bounded POST /incidents/search and selected GET /incidents/:incidentKey requests.

- Source: https://github.com/camunda/camunda

## Documentation

- https://docs.camunda.io/docs/apis-tools/camunda-api-rest/specifications/search-incidents/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/triage-camunda-process-incidents-into-a-read-only-evidence-packet/)
