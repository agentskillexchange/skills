---
name: "Jenkins Pipeline Shared Library Linter"
description: "Lints Jenkins Declarative and Scripted pipeline syntax using the Jenkins REST API and the Jenkins CLI jar. Checks Jenkinsfile syntax against a live or sandbox Jenkins controller using the /pipeline-model-converter/validate endpoint. Reports errors with line numbers and suggested fixes."
category: "CI/CD Integrations"
framework: "Codex"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/jenkins-pipeline-shared-library-linter/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "jenkins"  # from ase_tool_match
  github_stars: 25122  # from ase_github_stars (integer, not string)
  github_repo: "jenkinsci/jenkins"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Jenkins Pipeline Shared Library Linter

Lints Jenkins Declarative and Scripted pipeline syntax using the Jenkins REST API and the Jenkins CLI jar. Checks Jenkinsfile syntax against a live or sandbox Jenkins controller using the /pipeline-model-converter/validate endpoint. Reports errors with line numbers and suggested fixes.

## Overview

This skill automates linting of Jenkins pipeline files by interacting with the Jenkins REST API and the Jenkins CLI jar. It posts Jenkinsfile content to the /pipeline-model-converter/validate endpoint on a configured Jenkins controller, parses the JSON response for syntax errors, and reports them with exact line numbers and suggested corrections. The skill supports both Declarative and Scripted pipeline syntax, handles authentication via Jenkins API tokens, and works with multibranch pipelines. It integrates with GitHub webhooks and GitLab CI triggers to run on every pull request. Configuration covers Jenkins controller URL, credentials, and branch-specific overrides. Output is formatted for terminal, GitHub Checks annotations, and Slack notifications via the Slack Notification Plugin. Useful for preventing broken pipeline code from merging into protected branches.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-shared-library-linter
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-shared-library-linter -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-shared-library-linter -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-shared-library-linter -a codex
```

### OpenClaw

```bash
clawhub install jenkins-pipeline-shared-library-linter
```

## Source

- Marketplace: https://agentskillexchange.com/skills/jenkins-pipeline-shared-library-linter/
