---
name: "Run .NET background and recurring agent jobs with Hangfire"
slug: "run-dotnet-background-recurring-agent-jobs-with-hangfire"
description: "Use Hangfire to enqueue, schedule, retry, and supervise durable .NET jobs that support agent maintenance, ingestion, reports, and workflow handoffs."
github_stars: 10140
verification: "security_reviewed"
source: "https://github.com/HangfireIO/Hangfire"
author: "HangfireIO"
publisher_type: "organization"
category: "Templates & Workflows"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "HangfireIO/Hangfire"
  github_stars: 10140
---

# Run .NET background and recurring agent jobs with Hangfire

Use Hangfire to enqueue, schedule, retry, and supervise durable .NET jobs that support agent maintenance, ingestion, reports, and workflow handoffs.

## Prerequisites

.NET or .NET Core application, Hangfire NuGet packages, SQL Server/Redis/SQL Azure/MSMQ or supported storage, Hangfire Dashboard

## Installation

Install or set up from the source-backed instructions:

Install the Hangfire NuGet package, configure storage with `GlobalConfiguration.Configuration.UseSqlServerStorage(...)` or another supported provider, add `UseHangfireServer()` and `UseHangfireDashboard()`, then enqueue, schedule, or register recurring jobs from the .NET service.

- Source: https://github.com/HangfireIO/Hangfire

## Documentation

- https://docs.hangfire.io/en/latest/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-dotnet-background-recurring-agent-jobs-with-hangfire/)
