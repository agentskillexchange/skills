---
name: "Datadog Monitor Sync"
description: "Synchronizes Datadog monitor definitions between environments using the Datadog API v2 monitors endpoint. Supports diff-based updates, tag filtering, and Terraform state reconciliation."
category: "Monitoring & Alerts"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/datadog-monitor-sync/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "datadog"  # from ase_tool_match
  github_stars: 787  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 6043057  # from ase_npm_downloads
  github_repo: "DataDog/dd-trace-js"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Datadog Monitor Sync

Synchronizes Datadog monitor definitions between environments using the Datadog API v2 monitors endpoint. Supports diff-based updates, tag filtering, and Terraform state reconciliation.

## Overview

Datadog Monitor Sync provides infrastructure-as-code synchronization for Datadog monitors across development, staging, and production environments. Using the Datadog API v2 monitors endpoint with application and API key authentication, it fetches monitor definitions and performs intelligent diff-based synchronization.

The skill reads monitor configurations from YAML definition files, compares them against live Datadog state, and generates change plans showing additions, modifications, and deletions. It supports tag-based filtering to sync only specific monitor groups, and can reconcile with existing Terraform state files to prevent drift conflicts.

Additional features include monitor dependency ordering where composite monitors are updated after their constituent monitors, automatic downtime scheduling during sync operations via the Datadog Downtimes API, and rollback capability that snapshots current state before applying changes. Integration with Datadog Events API posts deployment annotations tracking sync operations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill datadog-monitor-sync
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill datadog-monitor-sync -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill datadog-monitor-sync -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill datadog-monitor-sync -a codex
```

### OpenClaw

```bash
clawhub install datadog-monitor-sync
```

## Source

- Marketplace: https://agentskillexchange.com/skills/datadog-monitor-sync/
