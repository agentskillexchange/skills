---
name: "Jenkins Pipeline Lint Agent"
description: "Validates Jenkinsfile declarative and scripted pipelines using the Jenkins Pipeline Linter API endpoint. Checks for deprecated step usage, security anti-patterns, and Groovy sandbox violations."
category: "CI/CD Integrations"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/jenkins-pipeline-lint-agent/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "jenkins"  # from ase_tool_match
  github_stars: 25122  # from ase_github_stars (integer, not string)
  github_repo: "jenkinsci/jenkins"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Jenkins Pipeline Lint Agent

Validates Jenkinsfile declarative and scripted pipelines using the Jenkins Pipeline Linter API endpoint. Checks for deprecated step usage, security anti-patterns, and Groovy sandbox violations.

## Overview

The Jenkins Pipeline Lint Agent skill submits Jenkinsfile contents to the Jenkins /pipeline-model-converter/validate REST endpoint for server-side syntax validation. Beyond basic linting, it performs static analysis on both declarative and scripted pipeline syntax to detect deprecated step names, insecure credential handling patterns, and Groovy sandbox escape attempts. The skill maintains a knowledge base of Jenkins plugin compatibility matrices, flagging steps that require specific plugin versions. It checks for common anti-patterns like unbounded node blocks, missing timeout wrappers, and improper shared library imports. The agent can process multi-branch pipeline configurations, validating Jenkinsfile variants across branches via the Jenkins Blue Ocean REST API. Results include line-level annotations with fix suggestions, severity ratings, and links to Jenkins documentation for each finding.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-lint-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-lint-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-lint-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-lint-agent -a codex
```

### OpenClaw

```bash
clawhub install jenkins-pipeline-lint-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/jenkins-pipeline-lint-agent/
