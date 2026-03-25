---
name: "Jenkins Pipeline Log Parser"
description: "Extracts and analyzes Jenkins Pipeline build logs using the Jenkins REST API and Blue Ocean API. Identifies stage failures, flaky test patterns via JUnit XML parsing, and generates failure trend reports with node allocation insights."
category: "CI/CD Integrations"
framework: "Claude Agents"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/jenkins-pipeline-log-parser/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "jenkins"  # from ase_tool_match
  github_stars: 25122  # from ase_github_stars (integer, not string)
  github_repo: "jenkinsci/jenkins"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Jenkins Pipeline Log Parser

Extracts and analyzes Jenkins Pipeline build logs using the Jenkins REST API and Blue Ocean API. Identifies stage failures, flaky test patterns via JUnit XML parsing, and generates failure trend reports with node allocation insights.

## Overview

The Jenkins Pipeline Log Parser skill automates the analysis of Jenkins CI/CD build failures and performance patterns. It connects to Jenkins instances via the REST API and Blue Ocean API for enhanced pipeline visualization data.

The skill retrieves build logs and parses them to identify specific stage failures, extracting error messages and stack traces from pipeline step outputs. It uses the Jenkins JUnit plugin API to parse test result XML files, detecting flaky tests through statistical analysis of pass/fail patterns across recent builds.

Failure trend analysis tracks recurring error patterns across builds, identifying infrastructure-related failures versus code-related failures. The skill correlates build failures with node allocation data to detect agent-specific issues like disk space exhaustion or network connectivity problems.

Reports include build duration trend analysis, queue wait time metrics, and parallel stage execution efficiency measurements. The skill supports Declarative and Scripted pipeline formats, multibranch pipelines, and shared library debugging with source-mapped error locations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-log-parser
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-log-parser -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-log-parser -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-log-parser -a codex
```

### OpenClaw

```bash
clawhub install jenkins-pipeline-log-parser
```

## Source

- Marketplace: https://agentskillexchange.com/skills/jenkins-pipeline-log-parser/
