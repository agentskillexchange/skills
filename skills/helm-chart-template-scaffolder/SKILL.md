---
title: "Helm Chart Template Scaffolder"
description: "Scaffolds Helm 3 chart templates with Go templating best practices. Uses helm-unittest for test generation and Polaris for Kubernetes resource validation scoring."
verification: "security_reviewed"
source: "https://github.com/helm/helm"
category:
  - "Templates & Workflows"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "helm/helm"
  github_stars: 29693
  license: "Apache-2.0"
---

# Helm Chart Template Scaffolder

The Helm Chart Template Scaffolder generates production-ready Helm 3 charts from application specifications. It creates properly structured templates using Go template functions from the Sprig library, including conditionals, loops, and named template definitions. Values.yaml files are generated with sensible defaults, JSON Schema validation (values.schema.json), and documented parameters. The skill produces templates for Deployments, Services, Ingresses, ConfigMaps, ServiceAccounts, HorizontalPodAutoscalers, and PodDisruptionBudgets. Each chart includes helm-unittest test suites that verify template rendering with different value combinations. Polaris integration scores generated resources against security and reliability best practices, flagging issues like missing resource limits, running as root, or absent health checks. The skill supports Helm library charts for shared templates and handles chart dependencies with proper version constraints in Chart.yaml.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/helm-chart-template-scaffolder/)
