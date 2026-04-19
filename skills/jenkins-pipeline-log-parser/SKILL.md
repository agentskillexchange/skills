---
title: "Jenkins Pipeline Log Parser"
description: "The Jenkins Pipeline Log Parser skill automates the analysis of Jenkins CI/CD build failures and performance patterns. It connects to Jenkins instances via the REST API and Blue Ocean API for enhanced pipeline visualization data. The skill retrieves build logs and parses them to identify specific stage failures, extracting error messages and stack traces from pipeline step outputs. It uses the Jenkins JUnit plugin API to parse test result XML files, detecting flaky tests through statistical analysis of pass/fail patterns across recent builds. Failure trend analysis tracks recurring error patterns across builds, identifying infrastructure-related failures versus code-related failures. The skill correlates build failures with node allocation data to detect agent-specific issues like disk space exhaustion or network connectivity problems. Reports include build duration trend analysis, queue wait time metrics, and parallel stage execution efficiency measurements. The skill supports Declarative and Scripted pipeline formats, multibranch pipelines, and shared library debugging with source-mapped error locations."
source: "https://github.com/jenkinsci/jenkins"
verification: "security_reviewed"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "jenkinsci/jenkins"
  github_stars: 25189
---

# Jenkins Pipeline Log Parser

The Jenkins Pipeline Log Parser skill automates the analysis of Jenkins CI/CD build failures and performance patterns. It connects to Jenkins instances via the REST API and Blue Ocean API for enhanced pipeline visualization data. The skill retrieves build logs and parses them to identify specific stage failures, extracting error messages and stack traces from pipeline step outputs. It uses the Jenkins JUnit plugin API to parse test result XML files, detecting flaky tests through statistical analysis of pass/fail patterns across recent builds. Failure trend analysis tracks recurring error patterns across builds, identifying infrastructure-related failures versus code-related failures. The skill correlates build failures with node allocation data to detect agent-specific issues like disk space exhaustion or network connectivity problems. Reports include build duration trend analysis, queue wait time metrics, and parallel stage execution efficiency measurements. The skill supports Declarative and Scripted pipeline formats, multibranch pipelines, and shared library debugging with source-mapped error locations.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-log-parser/)
