---
title: SonarQube Scanner Skill
description: The SonarQube Scanner Skill provides end-to-end integration with SonarQube
  for automated code quality analysis. It wraps the sonar-scanner CLI to trigger analysis
  runs and then queries the SonarQube Web API to retrieve detailed results. The skill
  begins by configuring sonar-project.properties dynamically based on the repository
  structure, detecting language profiles for Java, Python, JavaScript, TypeScript,
  Go, and C#. It runs sonar-scanner with appropriate JVM arguments and waits for the
  background task to complete using api/ce/task polling. Once analysis completes,
  it fetches quality gate status from api/qualitygates/project_status and retrieves
  individual issues via api/issues/search with facets for severity, type, and effort.
  Each issue is mapped to its source file and line number, enabling the agent to post
  inline annotations on pull requests through the GitHub or GitLab review API. Additional
  capabilities include tracking quality gate trends over time, comparing metrics between
  branches using api/measures/component, generating PDF reports via api/reports, and
  configuring custom quality profiles through api/qualityprofiles/create.
verification: security_reviewed
source: https://agentskillexchange.com/skills/sonarqube-scanner-skill/
category:
- Code Quality &amp; Review
framework:
- Claude Code
---

# SonarQube Scanner Skill

The SonarQube Scanner Skill provides end-to-end integration with SonarQube for automated code quality analysis. It wraps the sonar-scanner CLI to trigger analysis runs and then queries the SonarQube Web API to retrieve detailed results. The skill begins by configuring sonar-project.properties dynamically based on the repository structure, detecting language profiles for Java, Python, JavaScript, TypeScript, Go, and C#. It runs sonar-scanner with appropriate JVM arguments and waits for the background task to complete using api/ce/task polling. Once analysis completes, it fetches quality gate status from api/qualitygates/project_status and retrieves individual issues via api/issues/search with facets for severity, type, and effort. Each issue is mapped to its source file and line number, enabling the agent to post inline annotations on pull requests through the GitHub or GitLab review API. Additional capabilities include tracking quality gate trends over time, comparing metrics between branches using api/measures/component, generating PDF reports via api/reports, and configuring custom quality profiles through api/qualityprofiles/create.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-scanner-skill/)
