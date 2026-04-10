---
name: Prometheus Alert Resolver
description: Resolves Prometheus alerts by querying the /api/v1/alerts and /api/v1/query_range
  endpoints for metric time series analysis. Executes playbook steps for common alerts
  like HighCPUUsage and DiskSpaceLow, validates PromQL recording rules, and silences
  alerts via Alertmanager /api/v2/silences.
verification: security_reviewed
source: https://agentskillexchange.com/skills/prometheus-alert-resolver-skill/
category:
- Runbooks &amp; Diagnostics
framework:
- Gemini
---
# Prometheus Alert Resolver

Overview
Resolves Prometheus alerts by querying the /api/v1/alerts and /api/v1/query_range endpoints for metric time series analysis. Executes playbook steps for common alerts like HighCPUUsage and DiskSpaceLow, validates PromQL recording rules, and silences alerts via Alertmanager /api/v2/silences.
Key Features

Automated detection and reporting with structured output formats for downstream integrations
Configurable thresholds and rule sets that adapt to project-specific requirements and team conventions
Real-time feedback loops integrated into developer workflows for immediate actionable insights
Comprehensive logging and audit trails for compliance tracking and historical trend analysis

How It Works
Prometheus Alert Resolver connects directly to your existing infrastructure through well-documented API endpoints. It authenticates using standard token-based methods (API keys, OAuth tokens, or service account credentials) and operates within your existing permission boundaries. The skill processes incoming data streams, applies configurable analysis rules, and produces structured reports that integrate with notification systems, dashboards, and issue trackers.
Requirements

Valid API credentials with appropriate read/write scopes for the target service
Network access to the relevant API endpoints from the agent runtime environment
Compatible agent framework installed and configured with the necessary SDK dependencies

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-resolver-skill/)
