---
title: "Jenkins Pipeline Declarative Generator"
description: "Creates Jenkins Declarative Pipeline Jenkinsfiles using jenkins-pipeline-syntax and jenkins-shared-libraries. Configures stages, parallel execution, and post-build actions with Blue Ocean compatibility."
verification: "security_reviewed"
source: "https://github.com/jenkinsci/jenkins"
category:
  - "CI/CD Integrations"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "jenkinsci/jenkins"
  github_stars: 25189
  license: "MIT"
---

# Jenkins Pipeline Declarative Generator

The Jenkins Pipeline Declarative Generator skill creates Jenkinsfile configurations using the Declarative Pipeline syntax (pipeline { agent, stages, post }) compatible with Jenkins 2.x and Blue Ocean. It leverages Jenkins shared libraries (@Library annotations) and pipeline-model-definition-plugin for structured pipeline authoring.


The skill generates stage definitions with steps including sh, bat, powershell, checkout scm, withCredentials, and archiveArtifacts. It configures agent blocks with Docker containers (agent { docker { image } }), Kubernetes pods (agent { kubernetes { yaml } }), and label-based node selection. Parallel stage execution uses the parallel keyword within stage blocks for concurrent testing.


Advanced features include shared library development with vars/*.groovy global functions and src/**/*.groovy class definitions, stash/unstash for cross-stage artifact passing, input step configuration for manual approval gates, lock resource management for deployment serialization, and when clause conditions (branch, environment, expression, changeset) for conditional stage execution. The generator also supports Multibranch Pipeline configuration, GitHub Organization scanning, and pipeline replay/restart capabilities through the Jenkins CLI and REST API.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-declarative-generator/)
