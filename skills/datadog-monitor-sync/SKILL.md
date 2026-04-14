---
title: "Datadog Monitor Sync"
description: "Synchronizes Datadog monitor definitions between environments using the Datadog API v2 monitors endpoint. Supports diff-based updates, tag filtering, and Terraform state reconciliation."
verification: security_reviewed
source: "https://github.com/DataDog/dd-trace-js"
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

Datadog Monitor Sync provides infrastructure-as-code synchronization for Datadog monitors across development, staging, and production environments. Using the Datadog API v2 monitors endpoint with application and API key authentication, it fetches monitor definitions and performs intelligent diff-based synchronization.

The skill reads monitor configurations from YAML definition files, compares them against live Datadog state, and generates change plans showing additions, modifications, and deletions. It supports tag-based filtering to sync only specific monitor groups, and can reconcile with existing Terraform state files to prevent drift conflicts.

Additional features include monitor dependency ordering where composite monitors are updated after their constituent monitors, automatic downtime scheduling during sync operations via the Datadog Downtimes API, and rollback capability that snapshots current state before applying changes. Integration with Datadog Events API posts deployment annotations tracking sync operations.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-monitor-sync/)
