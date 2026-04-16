---
title: "Argo Workflows Linter"
description: "Lints and validates Argo Workflows templates using the argo CLI and Argo Server REST API. Detects DAG dependency cycles, invalid artifact references, and parameter type mismatches across workflow steps."
verification: "security_reviewed"
source: "https://github.com/argoproj/argo-workflows"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "argoproj/argo-workflows"
  github_stars: 16616
  license: "Apache-2.0"
---

# Argo Workflows Linter

The Argo Workflows Linter skill performs static analysis on Argo Workflows templates to catch errors before submission to your Kubernetes cluster. Built on top of the argo CLI lint command and the Argo Server v1alpha1 REST API, it provides deep validation that goes beyond basic YAML syntax checking.

The linter detects DAG dependency cycles by building a directed graph of step dependencies and running topological sort. It validates artifact references between steps, ensuring that output artifacts from producer steps match the expected input artifact names in consumer steps. Parameter type checking verifies that string, integer, and JSON parameters conform to their declared types across template boundaries.

Additional checks include resource quota estimation (computing aggregate CPU and memory requests across parallel steps), volume mount validation against PersistentVolumeClaim definitions, and retry strategy analysis. The skill outputs structured JSON reports compatible with CI systems like GitHub Actions, GitLab CI, and Jenkins, making it easy to integrate into existing pipelines as a quality gate.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argo-workflows-linter/)
