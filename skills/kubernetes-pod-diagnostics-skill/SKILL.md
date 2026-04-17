---
title: "Kubernetes Pod Diagnostics"
description: "Overview\nDiagnoses Kubernetes pod failures using kubectl describe, logs –previous, and the Kubernetes API /api/v1/namespaces/{ns}/events endpoints. Identifies CrashLoopBackOff root causes, OOMKilled memory analysis, and generates remediation steps with resource limit recommendations.\nKey Features\n\nAutomated detection and reporting with structured output formats for downstream integrations\nConfigurable thresholds and rule sets that adapt to project-specific requirements and team conventions\nReal-time feedback loops integrated into developer workflows for immediate actionable insights\nComprehensive logging and audit trails for compliance tracking and historical trend analysis\n\nHow It Works\nKubernetes Pod Diagnostics connects directly to your existing infrastructure through well-documented API endpoints. It authenticates using standard token-based methods (API keys, OAuth tokens, or service account credentials) and operates within your existing permission boundaries. The skill processes incoming data streams, applies configurable analysis rules, and produces structured reports that integrate with notification systems, dashboards, and issue trackers.\nRequirements\n\nValid API credentials with appropriate read/write scopes for the target service\nNetwork access to the relevant API endpoints from the agent runtime environment\nCompatible agent framework installed and configured with the necessary SDK dependencies"
verification: security_reviewed
source: "https://github.com/kubernetes/kubernetes"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes Pod Diagnostics

Overview
Diagnoses Kubernetes pod failures using kubectl describe, logs –previous, and the Kubernetes API /api/v1/namespaces/{ns}/events endpoints. Identifies CrashLoopBackOff root causes, OOMKilled memory analysis, and generates remediation steps with resource limit recommendations.
Key Features

Automated detection and reporting with structured output formats for downstream integrations
Configurable thresholds and rule sets that adapt to project-specific requirements and team conventions
Real-time feedback loops integrated into developer workflows for immediate actionable insights
Comprehensive logging and audit trails for compliance tracking and historical trend analysis

How It Works
Kubernetes Pod Diagnostics connects directly to your existing infrastructure through well-documented API endpoints. It authenticates using standard token-based methods (API keys, OAuth tokens, or service account credentials) and operates within your existing permission boundaries. The skill processes incoming data streams, applies configurable analysis rules, and produces structured reports that integrate with notification systems, dashboards, and issue trackers.
Requirements

Valid API credentials with appropriate read/write scopes for the target service
Network access to the relevant API endpoints from the agent runtime environment
Compatible agent framework installed and configured with the necessary SDK dependencies

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/kubernetes-pod-diagnostics-skill
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/kubernetes-pod-diagnostics-skill` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-diagnostics-skill/)
