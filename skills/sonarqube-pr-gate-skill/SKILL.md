---
title: SonarQube PR Gate
description: Overview Integrates SonarQube quality gates into pull request workflows
  via the SonarQube Web API /api/qualitygates/project_status. Blocks merges when code
  smells, duplications, or coverage thresholds fail and posts inline annotations using
  the GitHub Checks API. Key Features Automated detection and reporting with structured
  output formats for downstream integrations Configurable thresholds and rule sets
  that adapt to project-specific requirements and team conventions Real-time feedback
  loops integrated into developer workflows for immediate actionable insights Comprehensive
  logging and audit trails for compliance tracking and historical trend analysis How
  It Works SonarQube PR Gate connects directly to your existing infrastructure through
  well-documented API endpoints. It authenticates using standard token-based methods
  (API keys, OAuth tokens, or service account credentials) and operates within your
  existing permission boundaries. The skill processes incoming data streams, applies
  configurable analysis rules, and produces structured reports that integrate with
  notification systems, dashboards, and issue trackers. Requirements Valid API credentials
  with appropriate read/write scopes for the target service Network access to the
  relevant API endpoints from the agent runtime environment Compatible agent framework
  installed and configured with the necessary SDK dependencies
verification: security_reviewed
source: https://agentskillexchange.com/skills/sonarqube-pr-gate-skill/
category:
- Code Quality &amp; Review
framework:
- Codex
---

# SonarQube PR Gate

Overview Integrates SonarQube quality gates into pull request workflows via the SonarQube Web API /api/qualitygates/project_status. Blocks merges when code smells, duplications, or coverage thresholds fail and posts inline annotations using the GitHub Checks API. Key Features Automated detection and reporting with structured output formats for downstream integrations Configurable thresholds and rule sets that adapt to project-specific requirements and team conventions Real-time feedback loops integrated into developer workflows for immediate actionable insights Comprehensive logging and audit trails for compliance tracking and historical trend analysis How It Works SonarQube PR Gate connects directly to your existing infrastructure through well-documented API endpoints. It authenticates using standard token-based methods (API keys, OAuth tokens, or service account credentials) and operates within your existing permission boundaries. The skill processes incoming data streams, applies configurable analysis rules, and produces structured reports that integrate with notification systems, dashboards, and issue trackers. Requirements Valid API credentials with appropriate read/write scopes for the target service Network access to the relevant API endpoints from the agent runtime environment Compatible agent framework installed and configured with the necessary SDK dependencies

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-pr-gate-skill/)
