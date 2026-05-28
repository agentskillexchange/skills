---
name: "SonarQube Code Analysis"
slug: "sonarqube-code-analysis"
description: ""
github_stars: 10595
verification: "security_reviewed"
source: "https://github.com/SonarSource/sonarqube"
author: "Sonar"
category: "Developer Tools"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "sonarsource/sonarqube"
  github_stars: 10595
---

# SonarQube Code Analysis



## Prerequisites

Java

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

## Documentation

- https://docs.sonarsource.com/sonarqube-server/latest/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-code-analysis/)
