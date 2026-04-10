---
name: Jenkins Pipeline Log Parser
description: Extracts and analyzes Jenkins Pipeline build logs using the Jenkins REST
  API and Blue Ocean API. Identifies stage failures, flaky test patterns via JUnit
  XML parsing, and generates failure trend reports with node allocation insights.
verification: security_reviewed
source: https://agentskillexchange.com/skills/jenkins-pipeline-log-parser/
category:
- CI/CD Integrations
framework:
- Claude Agents
---
# Jenkins Pipeline Log Parser

The Jenkins Pipeline Log Parser skill automates the analysis of Jenkins CI/CD build failures and performance patterns. It connects to Jenkins instances via the REST API and Blue Ocean API for enhanced pipeline visualization data.
The skill retrieves build logs and parses them to identify specific stage failures, extracting error messages and stack traces from pipeline step outputs. It uses the Jenkins JUnit plugin API to parse test result XML files, detecting flaky tests through statistical analysis of pass/fail patterns across recent builds.
Failure trend analysis tracks recurring error patterns across builds, identifying infrastructure-related failures versus code-related failures. The skill correlates build failures with node allocation data to detect agent-specific issues like disk space exhaustion or network connectivity problems.
Reports include build duration trend analysis, queue wait time metrics, and parallel stage execution efficiency measurements. The skill supports Declarative and Scripted pipeline formats, multibranch pipelines, and shared library debugging with source-mapped error locations.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-log-parser/)
