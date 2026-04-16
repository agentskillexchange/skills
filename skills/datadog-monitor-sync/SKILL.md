---
title: "Datadog Monitor Sync"
description: "Synchronizes Datadog monitor definitions between environments using the Datadog API v2 monitors endpoint. Supports diff-based updates, tag filtering, and Terraform state reconciliation."
verification: "security_reviewed"
source: "https://github.com/DataDog/dd-trace-js"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Claude Code"
---

# Datadog Monitor Sync

Datadog Monitor Sync provides infrastructure-as-code synchronization for Datadog monitors across development, staging, and production environments. Using the Datadog API v2 monitors endpoint with application and API key authentication, it fetches monitor definitions and performs intelligent diff-based synchronization.

The skill reads monitor configurations from YAML definition files, compares them against live Datadog state, and generates change plans showing additions, modifications, and deletions. It supports tag-based filtering to sync only specific monitor groups, and can reconcile with existing Terraform state files to prevent drift conflicts.

Additional features include monitor dependency ordering where composite monitors are updated after their constituent monitors, automatic downtime scheduling during sync operations via the Datadog Downtimes API, and rollback capability that snapshots current state before applying changes. Integration with Datadog Events API posts deployment annotations tracking sync operations.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-monitor-sync/)
