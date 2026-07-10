---
name: "Jenkins Build Log Analyzer"
slug: "jenkins-build-log-analyzer"
description: "Parses Jenkins build console logs via the Jenkins Remote Access API to extract failure patterns, stack traces, and flaky test signatures. Uses regex heuristics and the Jenkins Test Results API to correlate failures with specific changes. Outputs a triage report ranked by recurrence frequency."
github_stars: 25189
verification: "security_reviewed"
source: "https://github.com/jenkinsci/jenkins"
category: "Runbooks & Diagnostics"
framework: "ChatGPT Agents"
tool_ecosystem:
  github_repo: "jenkinsci/jenkins"
  github_stars: 25189
---

# Jenkins Build Log Analyzer

Parses Jenkins build console logs via the Jenkins Remote Access API to extract failure patterns, stack traces, and flaky test signatures. Uses regex heuristics and the Jenkins Test Results API to correlate failures with specific changes. Outputs a triage report ranked by recurrence frequency.

## Installation

Requirements and caveats from upstream:
- [![Docker Pulls](https://img.shields.io/docker/pulls/jenkins/jenkins.svg)](https://hub.docker.com/r/jenkins/jenkins/)
- The Jenkins project provides official distributions as WAR files, Docker images, native packages and installers for platforms including several Linux distributions and Windows.

Basic usage or getting-started notes:
- For more information on setting up your development environment, contributing, and working with Jenkins internals, check the [contributing guide](CONTRIBUTING.md) and the [Jenkins Developer Documentation](https://www....
- # Source
- Our latest and greatest source of Jenkins can be found on [GitHub](https://github.com/jenkinsci/jenkins). Fork us!

- Source: https://github.com/jenkinsci/jenkins
- Extracted from upstream docs: https://raw.githubusercontent.com/jenkinsci/jenkins/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-build-log-analyzer/)
