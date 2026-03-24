---
name: "Jenkins Pipeline Generator"
description: "Generates declarative Jenkins pipeline scripts using the Jenkins Pipeline Syntax reference and shared library patterns. Integrates with the Jenkins REST API (/api/json) for job configuration and the Blue Ocean API for pipeline visualization."
category: "CI/CD Integrations"
framework: "Custom Agents"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/jenkins-pipeline-generator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "jenkins"  # from ase_tool_match
  github_stars: 25122  # from ase_github_stars (integer, not string)
  github_repo: "jenkinsci/jenkins"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Jenkins Pipeline Generator

Generates declarative Jenkins pipeline scripts using the Jenkins Pipeline Syntax reference and shared library patterns. Integrates with the Jenkins REST API (/api/json) for job configuration and the Blue Ocean API for pipeline visualization.

## Overview

The Jenkins Pipeline Generator skill automates the creation of declarative and scripted Jenkins pipeline definitions following the official Pipeline Syntax reference. It generates Jenkinsfile content with proper stage definitions, parallel execution blocks, post-condition handlers, and agent specifications for both traditional and Kubernetes-based executors.

This skill integrates with the Jenkins REST API (/api/json) to discover existing job configurations, installed plugins, and available build agents. It queries the Blue Ocean API endpoints for pipeline run visualization data and uses the Pipeline Model Definition API to validate generated pipeline syntax before deployment.

Shared library integration is a core capability, generating vars/ scripts and src/ classes that follow Jenkins shared library conventions. The skill creates library configurations with proper @Library annotations and manages version pinning for reproducible builds across teams.

Advanced features include generating multibranch pipeline configurations with custom branch discovery strategies, creating pipeline templates for common patterns like build-test-deploy with approval gates, and configuring credential bindings using the Jenkins Credentials API. The skill also generates proper Groovy sandbox-compatible code to avoid script approval requirements.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-generator -a codex
```

### OpenClaw

```bash
clawhub install jenkins-pipeline-generator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/jenkins-pipeline-generator/
