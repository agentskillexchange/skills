---
title: "Jenkins Pipeline Log Parser"
description: "Extracts and analyzes Jenkins Pipeline build logs using the Jenkins REST API and Blue Ocean API. Identifies stage failures, flaky test patterns via JUnit XML parsing, and generates failure trend reports with node allocation insights."
verification: "security_reviewed"
source: "https://github.com/jenkinsci/jenkins"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "jenkinsci/jenkins"
  github_stars: 25189
---

# Jenkins Pipeline Log Parser

The Jenkins Pipeline Log Parser skill automates the analysis of Jenkins CI/CD build failures and performance patterns. It connects to Jenkins instances via the REST API and Blue Ocean API for enhanced pipeline visualization data.

The skill retrieves build logs and parses them to identify specific stage failures, extracting error messages and stack traces from pipeline step outputs. It uses the Jenkins JUnit plugin API to parse test result XML files, detecting flaky tests through statistical analysis of pass/fail patterns across recent builds.

Failure trend analysis tracks recurring error patterns across builds, identifying infrastructure-related failures versus code-related failures. The skill correlates build failures with node allocation data to detect agent-specific issues like disk space exhaustion or network connectivity problems.

Reports include build duration trend analysis, queue wait time metrics, and parallel stage execution efficiency measurements. The skill supports Declarative and Scripted pipeline formats, multibranch pipelines, and shared library debugging with source-mapped error locations.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/jenkins-pipeline-log-parser/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/jenkins-pipeline-log-parser
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/jenkins-pipeline-log-parser`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-log-parser/)
