---
name: "Pulumi Drift Detector & Reconciler"
description: "Runs pulumi refresh on schedule to detect drift between live cloud resources and Pulumi state. Classifies drift by severity and opens a Jira ticket for destructive changes. Non-destructive drift is auto-reconciled via pulumi up –target for specific resources."
category: "Runbooks & Diagnostics"
framework: "Codex"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/pulumi-drift-detector-reconciler/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "pulumi"  # from ase_tool_match
  npm_weekly_downloads: 1484747  # from ase_npm_downloads
---

# Pulumi Drift Detector & Reconciler

Runs pulumi refresh on schedule to detect drift between live cloud resources and Pulumi state. Classifies drift by severity and opens a Jira ticket for destructive changes. Non-destructive drift is auto-reconciled via pulumi up –target for specific resources.

## Overview

Runs pulumi refresh on schedule to detect drift between live cloud resources and Pulumi state. Classifies drift by severity and opens a Jira ticket for destructive changes. Non-destructive drift is auto-reconciled via pulumi up –target for specific resources.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill pulumi-drift-detector-reconciler
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill pulumi-drift-detector-reconciler -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill pulumi-drift-detector-reconciler -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill pulumi-drift-detector-reconciler -a codex
```

### OpenClaw

```bash
clawhub install pulumi-drift-detector-reconciler
```

## Source

- Marketplace: https://agentskillexchange.com/skills/pulumi-drift-detector-reconciler/
