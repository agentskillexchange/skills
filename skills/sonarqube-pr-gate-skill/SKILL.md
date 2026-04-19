---
title: "SonarQube PR Gate"
description: "Overview Integrates SonarQube quality gates into pull request workflows via the SonarQube Web API /api/qualitygates/project_status. Blocks merges when code smells, duplications, or coverage thresholds fail and posts inline annotations using the GitHub Checks API. Key Features Automated detection and reporting with structured output formats for downstream integrations Configurable thresholds and rule sets that adapt to project-specific requirements and team conventions Real-time feedback loops integrated into developer workflows for immediate actionable insights Comprehensive logging and audit trails for compliance tracking and historical trend analysis How It Works SonarQube PR Gate connects directly to your existing infrastructure through well-documented API endpoints. It authenticates using standard token-based methods (API keys, OAuth tokens, or service account credentials) and operates within your existing permission boundaries. The skill processes incoming data streams, applies configurable analysis rules, and produces structured reports that integrate with notification systems, dashboards, and issue trackers. Requirements Valid API credentials with appropriate read/write scopes for the target service Network access to the relevant API endpoints from the agent runtime environment Compatible agent framework installed and configured with the necessary SDK dependencies"
source: "https://github.com/SonarSource/sonarqube"
verification: "security_reviewed"
category:
  - "Code Quality &amp; Review"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "sonarsource/sonarqube"
  github_stars: 10433
---

# SonarQube PR Gate

Overview Integrates SonarQube quality gates into pull request workflows via the SonarQube Web API /api/qualitygates/project_status. Blocks merges when code smells, duplications, or coverage thresholds fail and posts inline annotations using the GitHub Checks API. Key Features Automated detection and reporting with structured output formats for downstream integrations Configurable thresholds and rule sets that adapt to project-specific requirements and team conventions Real-time feedback loops integrated into developer workflows for immediate actionable insights Comprehensive logging and audit trails for compliance tracking and historical trend analysis How It Works SonarQube PR Gate connects directly to your existing infrastructure through well-documented API endpoints. It authenticates using standard token-based methods (API keys, OAuth tokens, or service account credentials) and operates within your existing permission boundaries. The skill processes incoming data streams, applies configurable analysis rules, and produces structured reports that integrate with notification systems, dashboards, and issue trackers. Requirements Valid API credentials with appropriate read/write scopes for the target service Network access to the relevant API endpoints from the agent runtime environment Compatible agent framework installed and configured with the necessary SDK dependencies

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-pr-gate-skill/)
