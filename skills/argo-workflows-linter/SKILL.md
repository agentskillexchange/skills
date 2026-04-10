---
title: "Argo Workflows Linter"
description: "Lints and validates Argo Workflows templates using the argo CLI and Argo Server REST API. Detects DAG dependency cycles, invalid artifact references, and parameter type mismatches across workflow steps."
slug: "argo-workflows-linter"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/argo-workflows-linter/"
---

# Argo Workflows Linter

Lints and validates Argo Workflows templates using the argo CLI and Argo Server REST API. Detects DAG dependency cycles, invalid artifact references, and parameter type mismatches across workflow steps.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install argo-workflows-linter
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Argo Workflows Linter skill performs static analysis on Argo Workflows templates to catch errors before submission to your Kubernetes cluster. Built on top of the argo CLI lint command and the Argo Server v1alpha1 REST API, it provides deep validation that goes beyond basic YAML syntax checking.
The linter detects DAG dependency cycles by building a directed graph of step dependencies and running topological sort. It validates artifact references between steps, ensuring that output artifacts from producer steps match the expected input artifact names in consumer steps. Parameter type checking verifies that string, integer, and JSON parameters conform to their declared types across template boundaries.
Additional checks include resource quota estimation (computing aggregate CPU and memory requests across parallel steps), volume mount validation against PersistentVolumeClaim definitions, and retry strategy analysis. The skill outputs structured JSON reports compatible with CI systems like GitHub Actions, GitLab CI, and Jenkins, making it easy to integrate into existing pipelines as a quality gate.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argo-workflows-linter/)
