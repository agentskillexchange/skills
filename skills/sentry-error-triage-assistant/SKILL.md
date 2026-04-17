---
title: "Sentry Error Triage Assistant"
description: "The Sentry Error Triage Assistant skill automates the analysis and prioritization of application errors captured by Sentry. It queries the Sentry Web API endpoint /api/0/issues/ to retrieve issue details including event counts, user impact metrics, first and last seen timestamps, and assigned ownership based on CODEOWNERS integration.\nThis skill analyzes SDK-captured breadcrumb data to reconstruct user journeys leading to errors, identifying common trigger patterns across multiple error occurrences. It uses Sentry fingerprinting rules to group related issues and detect duplicate reports that may appear as separate entries due to minor stack trace variations across deployments.\nRelease health monitoring is provided through the /api/0/organizations/{org}/releases/ endpoint, correlating error spikes with specific release versions and identifying regression introduction points. The skill tracks crash-free session rates and adoption metrics to assess the urgency of newly introduced errors.\nTriage output includes severity classifications based on user impact (unique users affected), frequency trends, and business-critical path analysis. The skill generates recommended actions including issue assignment suggestions based on code ownership, links to relevant source code via Sentry source map integration, and suggested Sentry alert rule configurations for similar future issues."
verification: security_reviewed
source: "https://github.com/getsentry/sentry"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "getsentry/sentry"
  github_stars: 43576
---

# Sentry Error Triage Assistant

The Sentry Error Triage Assistant skill automates the analysis and prioritization of application errors captured by Sentry. It queries the Sentry Web API endpoint /api/0/issues/ to retrieve issue details including event counts, user impact metrics, first and last seen timestamps, and assigned ownership based on CODEOWNERS integration.
This skill analyzes SDK-captured breadcrumb data to reconstruct user journeys leading to errors, identifying common trigger patterns across multiple error occurrences. It uses Sentry fingerprinting rules to group related issues and detect duplicate reports that may appear as separate entries due to minor stack trace variations across deployments.
Release health monitoring is provided through the /api/0/organizations/{org}/releases/ endpoint, correlating error spikes with specific release versions and identifying regression introduction points. The skill tracks crash-free session rates and adoption metrics to assess the urgency of newly introduced errors.
Triage output includes severity classifications based on user impact (unique users affected), frequency trends, and business-critical path analysis. The skill generates recommended actions including issue assignment suggestions based on code ownership, links to relevant source code via Sentry source map integration, and suggested Sentry alert rule configurations for similar future issues.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/sentry-error-triage-assistant
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/sentry-error-triage-assistant` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sentry-error-triage-assistant/)
