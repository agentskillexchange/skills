---
title: "Schedule and inspect .NET agent jobs with TickerQ"
description: "Use TickerQ to add persistent cron and time-based job scheduling, retries, multi-node coordination, OpenTelemetry, and a live dashboard to .NET agent services."
verification: "listed"
source: "https://github.com/Arcenox-co/TickerQ"
author: "Arcenox LLC"
publisher_type: "open_source"
category:
  - "Templates & Workflows"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "Arcenox-co/TickerQ"
  github_stars: 3536
---

# Schedule and inspect .NET agent jobs with TickerQ

Use TickerQ to add persistent cron and time-based job scheduling, retries, multi-node coordination, OpenTelemetry, and a live dashboard to .NET agent services.

## Prerequisites

.NET application, TickerQ NuGet packages, EF Core or Redis persistence when durable scheduling is needed, optional TickerQ Dashboard and OpenTelemetry instrumentation

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with dotnet add package TickerQ, register services with builder.Services.AddTickerQ(), enable app.UseTickerQ(), add TickerFunction methods for agent jobs, then schedule work through ITimeTickerManager or the dashboard.
```

## Documentation

- https://tickerq.net

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/schedule-and-inspect-dotnet-agent-jobs-with-tickerq/)
