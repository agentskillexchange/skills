---
title: "Argo Workflows Linter"
description: "The Argo Workflows Linter skill performs static analysis on Argo Workflows templates to catch errors before submission to your Kubernetes cluster. Built on top of the argo CLI lint command and the Argo Server v1alpha1 REST API, it provides deep validation that goes beyond basic YAML syntax checking. The linter detects DAG dependency cycles by building a directed graph of step dependencies and running topological sort. It validates artifact references between steps, ensuring that output artifacts from producer steps match the expected input artifact names in consumer steps. Parameter type checking verifies that string, integer, and JSON parameters conform to their declared types across template boundaries. Additional checks include resource quota estimation (computing aggregate CPU and memory requests across parallel steps), volume mount validation against PersistentVolumeClaim definitions, and retry strategy analysis. The skill outputs structured JSON reports compatible with CI systems like GitHub Actions, GitLab CI, and Jenkins, making it easy to integrate into existing pipelines as a quality gate."
source: "https://github.com/argoproj/argo-workflows"
verification: "security_reviewed"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "argoproj/argo-workflows"
  github_stars: 16616
---

# Argo Workflows Linter

The Argo Workflows Linter skill performs static analysis on Argo Workflows templates to catch errors before submission to your Kubernetes cluster. Built on top of the argo CLI lint command and the Argo Server v1alpha1 REST API, it provides deep validation that goes beyond basic YAML syntax checking. The linter detects DAG dependency cycles by building a directed graph of step dependencies and running topological sort. It validates artifact references between steps, ensuring that output artifacts from producer steps match the expected input artifact names in consumer steps. Parameter type checking verifies that string, integer, and JSON parameters conform to their declared types across template boundaries. Additional checks include resource quota estimation (computing aggregate CPU and memory requests across parallel steps), volume mount validation against PersistentVolumeClaim definitions, and retry strategy analysis. The skill outputs structured JSON reports compatible with CI systems like GitHub Actions, GitLab CI, and Jenkins, making it easy to integrate into existing pipelines as a quality gate.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argo-workflows-linter/)
