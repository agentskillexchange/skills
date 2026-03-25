---
name: "Jenkins Declarative Pipeline Generator"
description: "Generates Jenkins Declarative Pipelines using the Pipeline Model Definition Plugin API and Jenkins shared library conventions. Integrates with the Jenkins REST API for job provisioning and credentials management."
category: "CI/CD Integrations"
framework: "OpenClaw"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/jenkins-declarative-pipeline-generator-2/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "jenkins"  # from ase_tool_match
  github_stars: 25122  # from ase_github_stars (integer, not string)
  github_repo: "jenkinsci/jenkins"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Jenkins Declarative Pipeline Generator

Generates Jenkins Declarative Pipelines using the Pipeline Model Definition Plugin API and Jenkins shared library conventions. Integrates with the Jenkins REST API for job provisioning and credentials management.

## Overview

The Jenkins Declarative Pipeline Generator creates production-ready Jenkinsfiles by analyzing project structure and generating appropriate stage definitions with proper agent selection. It leverages the Pipeline Model Definition Plugin for structured pipeline syntax and integrates with Jenkins shared libraries following the vars/ and src/ directory conventions. The skill uses the Jenkins REST API (jenkins-cli and jenkins-api npm packages) for remote job creation, parameter configuration, and credential store management via the Credentials Plugin API. It supports multi-branch pipeline configurations with automatic SCM trigger setup through the GitHub Branch Source Plugin and Bitbucket Branch Source Plugin. The generator handles complex deployment stages with environment-specific configurations, implementing proper input gates for production deployments and integrating with the Pipeline Stage View Plugin for visual pipeline monitoring. It also configures post-build actions including Slack notifications via the Slack Notification Plugin API and artifact archiving strategies.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill jenkins-declarative-pipeline-generator-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill jenkins-declarative-pipeline-generator-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill jenkins-declarative-pipeline-generator-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill jenkins-declarative-pipeline-generator-2 -a codex
```

### OpenClaw

```bash
clawhub install jenkins-declarative-pipeline-generator-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/jenkins-declarative-pipeline-generator-2/
