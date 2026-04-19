---
title: "Datadog Monitor Sync"
description: "Datadog Monitor Sync provides infrastructure-as-code synchronization for Datadog monitors across development, staging, and production environments. Using the Datadog API v2 monitors endpoint with application and API key authentication, it fetches monitor definitions and performs intelligent diff-based synchronization. The skill reads monitor configurations from YAML definition files, compares them against live Datadog state, and generates change plans showing additions, modifications, and deletions. It supports tag-based filtering to sync only specific monitor groups, and can reconcile with existing Terraform state files to prevent drift conflicts. Additional features include monitor dependency ordering where composite monitors are updated after their constituent monitors, automatic downtime scheduling during sync operations via the Datadog Downtimes API, and rollback capability that snapshots current state before applying changes. Integration with Datadog Events API posts deployment annotations tracking sync operations."
source: "https://github.com/DataDog/dd-trace-js"
verification: "security_reviewed"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "datadog/dd-trace-js"
  github_stars: 791
  npm_package: "dd-trace"
  npm_weekly_downloads: 6596660
---

# Datadog Monitor Sync

Datadog Monitor Sync provides infrastructure-as-code synchronization for Datadog monitors across development, staging, and production environments. Using the Datadog API v2 monitors endpoint with application and API key authentication, it fetches monitor definitions and performs intelligent diff-based synchronization. The skill reads monitor configurations from YAML definition files, compares them against live Datadog state, and generates change plans showing additions, modifications, and deletions. It supports tag-based filtering to sync only specific monitor groups, and can reconcile with existing Terraform state files to prevent drift conflicts. Additional features include monitor dependency ordering where composite monitors are updated after their constituent monitors, automatic downtime scheduling during sync operations via the Datadog Downtimes API, and rollback capability that snapshots current state before applying changes. Integration with Datadog Events API posts deployment annotations tracking sync operations.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-monitor-sync/)
