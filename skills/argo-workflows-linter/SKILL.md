---
title: "Argo Workflows Linter"
description: "Lints and validates Argo Workflows templates using the argo CLI and Argo Server REST API. Detects DAG dependency cycles, invalid artifact references, and parameter type mismatches across workflow steps."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/argo-workflows-linter/"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
---

# Argo Workflows Linter

The Argo Workflows Linter skill performs static analysis on Argo Workflows templates to catch errors before submission to your Kubernetes cluster. Built on top of the argo CLI lint command and the Argo Server v1alpha1 REST API, it provides deep validation that goes beyond basic YAML syntax checking.

The linter detects DAG dependency cycles by building a directed graph of step dependencies and running topological sort. It validates artifact references between steps, ensuring that output artifacts from producer steps match the expected input artifact names in consumer steps. Parameter type checking verifies that string, integer, and JSON parameters conform to their declared types across template boundaries.

Additional checks include resource quota estimation (computing aggregate CPU and memory requests across parallel steps), volume mount validation against PersistentVolumeClaim definitions, and retry strategy analysis. The skill outputs structured JSON reports compatible with CI systems like GitHub Actions, GitLab CI, and Jenkins, making it easy to integrate into existing pipelines as a quality gate.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argo-workflows-linter/)
