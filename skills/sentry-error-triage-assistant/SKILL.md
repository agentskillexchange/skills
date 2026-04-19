---
title: "Sentry Error Triage Assistant"
description: "The Sentry Error Triage Assistant skill automates the analysis and prioritization of application errors captured by Sentry. It queries the Sentry Web API endpoint /api/0/issues/ to retrieve issue details including event counts, user impact metrics, first and last seen timestamps, and assigned ownership based on CODEOWNERS integration. This skill analyzes SDK-captured breadcrumb data to reconstruct user journeys leading to errors, identifying common trigger patterns across multiple error occurrences. It uses Sentry fingerprinting rules to group related issues and detect duplicate reports that may appear as separate entries due to minor stack trace variations across deployments. Release health monitoring is provided through the /api/0/organizations/{org}/releases/ endpoint, correlating error spikes with specific release versions and identifying regression introduction points. The skill tracks crash-free session rates and adoption metrics to assess the urgency of newly introduced errors. Triage output includes severity classifications based on user impact (unique users affected), frequency trends, and business-critical path analysis. The skill generates recommended actions including issue assignment suggestions based on code ownership, links to relevant source code via Sentry source map integration, and suggested Sentry alert rule configurations for similar future issues."
source: "https://github.com/getsentry/sentry"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "getsentry/sentry"
  github_stars: 43576
---

# Sentry Error Triage Assistant

The Sentry Error Triage Assistant skill automates the analysis and prioritization of application errors captured by Sentry. It queries the Sentry Web API endpoint /api/0/issues/ to retrieve issue details including event counts, user impact metrics, first and last seen timestamps, and assigned ownership based on CODEOWNERS integration. This skill analyzes SDK-captured breadcrumb data to reconstruct user journeys leading to errors, identifying common trigger patterns across multiple error occurrences. It uses Sentry fingerprinting rules to group related issues and detect duplicate reports that may appear as separate entries due to minor stack trace variations across deployments. Release health monitoring is provided through the /api/0/organizations/{org}/releases/ endpoint, correlating error spikes with specific release versions and identifying regression introduction points. The skill tracks crash-free session rates and adoption metrics to assess the urgency of newly introduced errors. Triage output includes severity classifications based on user impact (unique users affected), frequency trends, and business-critical path analysis. The skill generates recommended actions including issue assignment suggestions based on code ownership, links to relevant source code via Sentry source map integration, and suggested Sentry alert rule configurations for similar future issues.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sentry-error-triage-assistant/)
