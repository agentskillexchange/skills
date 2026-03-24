---
name: "Disk Space Emergency Runbook"
description: "Use this skill to quickly identify and clean large files consuming disk space when systems are running critically low. It walks through du, df, lsof, and log rotation commands to free space fast. Trigger when disk usage hits critical thresholds, services are failing due to no space left on device, or disk I/O is saturated."
category: "Monitoring & Alerts"
framework: "Custom Agents"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/disk-space-emergency-runbook/"
---

# Disk Space Emergency Runbook

Use this skill to quickly identify and clean large files consuming disk space when systems are running critically low. It walks through du, df, lsof, and log rotation commands to free space fast. Trigger when disk usage hits critical thresholds, services are failing due to no space left on device, or disk I/O is saturated.

## Overview

Use this skill to quickly identify and clean large files consuming disk space when systems are running critically low. It walks through du, df, lsof, and log rotation commands to free space fast. Trigger when disk usage hits critical thresholds, services are failing due to no space left on device, or disk I/O is saturated.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill disk-space-emergency-runbook
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill disk-space-emergency-runbook -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill disk-space-emergency-runbook -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill disk-space-emergency-runbook -a codex
```

### OpenClaw

```bash
clawhub install disk-space-emergency-runbook
```

## Source

- Marketplace: https://agentskillexchange.com/skills/disk-space-emergency-runbook/
