---
name: Pulumi Drift Detector & Reconciler
description: Runs pulumi refresh on schedule to detect drift between live cloud resources and Pulumi state. Classifies drift by severity and opens a Jira ticket for destructive changes. Non-destructive drift is auto-reconciled via pulumi up --target for specific resources.
category: Runbooks &amp; Diagnostics
framework: Any Agent
verification: verified_metadata
rating: 4.5
reviews: 49
source: https://agentskillexchange.com/skill/pulumi-drift-detector-reconciler/
---

# Pulumi Drift Detector & Reconciler

Runs pulumi refresh on schedule to detect drift between live cloud resources and Pulumi state. Classifies drift by severity and opens a Jira ticket for destructive changes. Non-destructive drift is auto-reconciled via pulumi up --target for specific resources.

## Overview

Runs pulumi refresh on schedule to detect drift between live cloud resources and Pulumi state. Classifies drift by severity and opens a Jira ticket for destructive changes. Non-destructive drift is auto-reconciled via pulumi up --target for specific resources.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill pulumi-drift-detector-reconciler
```

### OpenClaw

```bash
clawhub install pulumi-drift-detector-reconciler
```

### Claude Code

```bash
claude mcp add pulumi-drift-detector-reconciler
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/pulumi-drift-detector-reconciler/) for detailed installation instructions.

## Verification

- **Status**: verified_metadata
- **Category**: Runbooks &amp; Diagnostics
- **Framework**: Any Agent
- **Rating**: 4.5/5 (49 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/pulumi-drift-detector-reconciler/)
