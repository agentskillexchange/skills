---
title: Jenkins Pipeline Declarative Generator
description: The Jenkins Pipeline Declarative Generator skill creates Jenkinsfile
  configurations using the Declarative Pipeline syntax (pipeline { agent, stages,
  post }) compatible with Jenkins 2.x and Blue Ocean. It leverages Jenkins shared
  libraries (@Library annotations) and pipeline-model-definition-plugin for structured
  pipeline authoring. The skill generates stage definitions with steps including sh,
  bat, powershell, checkout scm, withCredentials, and archiveArtifacts. It configures
  agent blocks with Docker containers (agent { docker { image } }), Kubernetes pods
  (agent { kubernetes { yaml } }), and label-based node selection. Parallel stage
  execution uses the parallel keyword within stage blocks for concurrent testing.
  Advanced features include shared library development with vars/*.groovy global functions
  and src/**/*.groovy class definitions, stash/unstash for cross-stage artifact passing,
  input step configuration for manual approval gates, lock resource management for
  deployment serialization, and when clause conditions (branch, environment, expression,
  changeset) for conditional stage execution. The generator also supports Multibranch
  Pipeline configuration, GitHub Organization scanning, and pipeline replay/restart
  capabilities through the Jenkins CLI and REST API.
verification: security_reviewed
source: https://agentskillexchange.com/skills/jenkins-pipeline-declarative-generator/
category:
- CI/CD Integrations
framework:
- Custom Agents
---

# Jenkins Pipeline Declarative Generator

The Jenkins Pipeline Declarative Generator skill creates Jenkinsfile configurations using the Declarative Pipeline syntax (pipeline { agent, stages, post }) compatible with Jenkins 2.x and Blue Ocean. It leverages Jenkins shared libraries (@Library annotations) and pipeline-model-definition-plugin for structured pipeline authoring. The skill generates stage definitions with steps including sh, bat, powershell, checkout scm, withCredentials, and archiveArtifacts. It configures agent blocks with Docker containers (agent { docker { image } }), Kubernetes pods (agent { kubernetes { yaml } }), and label-based node selection. Parallel stage execution uses the parallel keyword within stage blocks for concurrent testing. Advanced features include shared library development with vars/*.groovy global functions and src/**/*.groovy class definitions, stash/unstash for cross-stage artifact passing, input step configuration for manual approval gates, lock resource management for deployment serialization, and when clause conditions (branch, environment, expression, changeset) for conditional stage execution. The generator also supports Multibranch Pipeline configuration, GitHub Organization scanning, and pipeline replay/restart capabilities through the Jenkins CLI and REST API.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-declarative-generator/)
