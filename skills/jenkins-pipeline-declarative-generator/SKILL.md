---
name: "Jenkins Pipeline Declarative Generator"
description: "Creates Jenkins Declarative Pipeline Jenkinsfiles using jenkins-pipeline-syntax and jenkins-shared-libraries. Configures stages, parallel execution, and post-build actions with Blue Ocean compatibility."
category: "CI/CD Integrations"
framework: "Custom Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/jenkins-pipeline-declarative-generator/"
---
# Jenkins Pipeline Declarative Generator

Creates Jenkins Declarative Pipeline Jenkinsfiles using jenkins-pipeline-syntax and jenkins-shared-libraries. Configures stages, parallel execution, and post-build actions with Blue Ocean compatibility.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-declarative-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-declarative-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-declarative-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-declarative-generator -a codex
```

### OpenClaw

```bash
clawhub install jenkins-pipeline-declarative-generator
```

## Details

The Jenkins Pipeline Declarative Generator skill creates Jenkinsfile configurations using the Declarative Pipeline syntax (pipeline { agent, stages, post }) compatible with Jenkins 2.x and Blue Ocean. It leverages Jenkins shared libraries (@Library annotations) and pipeline-model-definition-plugin for structured pipeline authoring.

The skill generates stage definitions with steps including sh, bat, powershell, checkout scm, withCredentials, and archiveArtifacts. It configures agent blocks with Docker containers (agent { docker { image } }), Kubernetes pods (agent { kubernetes { yaml } }), and label-based node selection. Parallel stage execution uses the parallel keyword within stage blocks for concurrent testing.

Advanced features include shared library development with vars/*.groovy global functions and src/**/*.groovy class definitions, stash/unstash for cross-stage artifact passing, input step configuration for manual approval gates, lock resource management for deployment serialization, and when clause conditions (branch, environment, expression, changeset) for conditional stage execution. The generator also supports Multibranch Pipeline configuration, GitHub Organization scanning, and pipeline replay/restart capabilities through the Jenkins CLI and REST API.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-declarative-generator/)
