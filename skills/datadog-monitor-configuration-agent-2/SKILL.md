---
name: Datadog Monitor Configuration Agent
description: Creates and manages Datadog monitors using the datadog-api-client SDK.
  Configures metric, log, APM trace, and composite monitors with proper threshold
  types and notification routing.
category: "Monitoring &amp; Alerts"
framework: Claude Agents
verification: security_reviewed
source: "https://agentskillexchange.com/skills/datadog-monitor-configuration-agent-2/"
---
# Datadog Monitor Configuration Agent

Creates and manages Datadog monitors using the datadog-api-client SDK. Configures metric, log, APM trace, and composite monitors with proper threshold types and notification routing.

The Datadog Monitor Configuration Agent automates monitor lifecycle management through the datadog-api-client Python SDK. It creates metric monitors with correct threshold conditions (above, below, above-or-equal) and recovery thresholds that prevent flapping. The skill handles log monitors with proper query syntax including facet filters, pattern matching, and log pipeline processing awareness. For APM monitors, it constructs trace analytics queries targeting specific service/resource combinations with percentile-based latency thresholds. Composite monitors are built using boolean algebra across existing monitor IDs with correct operator precedence. The agent configures notification channels using @-mention syntax for Slack channels, PagerDuty services, and webhook endpoints. It manages monitor downtimes for maintenance windows, supports tag-based monitor scoping across environments, and generates Terraform datadog_monitor resources for infrastructure-as-code workflows.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill datadog-monitor-configuration-agent-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill datadog-monitor-configuration-agent-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill datadog-monitor-configuration-agent-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill datadog-monitor-configuration-agent-2 -a codex
```

### OpenClaw

```bash
clawhub install datadog-monitor-configuration-agent-2
```


## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-monitor-configuration-agent-2/)
