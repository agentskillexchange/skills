---
title: "Jenkins Pipeline Shared Library Linter"
description: "Lints Jenkins Declarative and Scripted pipeline syntax using the Jenkins REST API and the Jenkins CLI jar. Checks Jenkinsfile syntax against a live or sandbox Jenkins controller using the /pipeline-model-converter/validate endpoint. Reports errors with line numbers and suggested fixes."
verification: security_reviewed
source: "https://github.com/jenkinsci/jenkins"
category:
  - "CI/CD Integrations"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "jenkinsci/jenkins"
  github_stars: 25189
  license: "MIT"
---

# Jenkins Pipeline Shared Library Linter

Lints Jenkins Declarative and Scripted pipeline syntax using the Jenkins REST API and the Jenkins CLI jar. Checks Jenkinsfile syntax against a live or sandbox Jenkins controller using the /pipeline-model-converter/validate endpoint. Reports errors with line numbers and suggested fixes.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/jenkins-pipeline-shared-library-linter
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/jenkins-pipeline-shared-library-linter` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-shared-library-linter/)
