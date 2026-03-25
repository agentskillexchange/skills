---
name: "Jenkins Pipeline DSL Generator"
description: "Generates Jenkins Declarative and Scripted Pipeline DSL using the Jenkins REST API and Job DSL plugin. Creates Jenkinsfile configurations with parallel stages, shared libraries, and credential binding."
category: "CI/CD Integrations"
framework: "Claude Code"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/jenkins-pipeline-dsl-generator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "jenkins"  # from ase_tool_match
  github_stars: 25122  # from ase_github_stars (integer, not string)
  github_repo: "jenkinsci/jenkins"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Jenkins Pipeline DSL Generator

Generates Jenkins Declarative and Scripted Pipeline DSL using the Jenkins REST API and Job DSL plugin. Creates Jenkinsfile configurations with parallel stages, shared libraries, and credential binding.

## Overview

The Jenkins Pipeline DSL Generator skill automates the creation of Jenkins pipeline configurations in both Declarative and Scripted Pipeline syntax. It communicates with Jenkins instances via the Jenkins REST API to discover available plugins, credentials, and agent labels.

The skill generates Jenkinsfile content with proper stage definitions, parallel execution blocks, and post-build actions. It integrates with the Jenkins Shared Library mechanism to produce reusable Groovy functions under vars/ and src/ directories, following the standard Jenkins library structure.

Key features include automatic credential binding using withCredentials blocks for secrets stored in the Jenkins Credentials Provider, Docker agent configuration with custom Dockerfile builds, and matrix builds using the Matrix Authorization Strategy plugin. The skill validates pipeline syntax using the Jenkins Pipeline Linter API endpoint and suggests optimizations for build caching with stash/unstash patterns.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-dsl-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-dsl-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-dsl-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-dsl-generator -a codex
```

### OpenClaw

```bash
clawhub install jenkins-pipeline-dsl-generator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/jenkins-pipeline-dsl-generator/
