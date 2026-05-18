---
name: "SonarQube Quality Gate Checker"
slug: "sonarqube-quality-gate-checker"
description: "Queries SonarQube Web API for project quality gate status, code coverage metrics, and technical debt analysis. Integrates with sonar-scanner CLI for on-demand analysis and pr-decoration via the SonarQube ALM integration API."
github_stars: 10433
verification: "listed"
source: "https://github.com/SonarSource/sonarqube"
category: "Code Quality & Review"
framework: "Gemini"
tool_ecosystem:
  github_repo: "sonarsource/sonarqube"
  github_stars: 10433
---

# SonarQube Quality Gate Checker

Queries SonarQube Web API for project quality gate status, code coverage metrics, and technical debt analysis. Integrates with sonar-scanner CLI for on-demand analysis and pr-decoration via the SonarQube ALM integration API.

## Installation

Use the upstream install or setup path that matches your environment:
- Make sure that you follow our [code style](https://github.com/SonarSource/sonar-developer-toolset#code-style) and all tests are passing (Travis build is executed for each pull request).
- yarn
- yarn build
- yarn generate-translation-keys

Requirements and caveats from upstream:
- Native Git - Must be installed and available in your PATH
- But if your contribution also contains UI changes, you must clone the sonarqube-webapp repository, do your changes there, build it locally and then build the sonarqube repository using the WEBAPP_BUILD_PATH environmen...

Basic usage or getting-started notes:
- Java 17 - Required to build the project
- npm - Required for building
- Tests - Can be disabled if needed by adding -x test to the gradle command (useful if you just want to build without running tests)

- Source: https://github.com/SonarSource/sonarqube
- Extracted from upstream docs: https://raw.githubusercontent.com/SonarSource/sonarqube/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-quality-gate-checker/)
