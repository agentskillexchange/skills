---
name: "Helm Chart Template Scaffolder"
description: "Scaffolds Helm 3 chart templates with Go templating best practices. Uses helm-unittest for test generation and Polaris for Kubernetes resource validation scoring."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/helm-chart-template-scaffolder/"
category:
  - "Templates &amp; Workflows"
framework:
  - "Codex"
---

# Helm Chart Template Scaffolder

The Helm Chart Template Scaffolder generates production-ready Helm 3 charts from application specifications. It creates properly structured templates using Go template functions from the Sprig library, including conditionals, loops, and named template definitions. Values.yaml files are generated with sensible defaults, JSON Schema validation (values.schema.json), and documented parameters. The skill produces templates for Deployments, Services, Ingresses, ConfigMaps, ServiceAccounts, HorizontalPodAutoscalers, and PodDisruptionBudgets. Each chart includes helm-unittest test suites that verify template rendering with different value combinations. Polaris integration scores generated resources against security and reliability best practices, flagging issues like missing resource limits, running as root, or absent health checks. The skill supports Helm library charts for shared templates and handles chart dependencies with proper version constraints in Chart.yaml.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/helm-chart-template-scaffolder/)
